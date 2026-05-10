import json
import re
from pathlib import Path

try:
    import fitz
except ImportError:
    raise SystemExit("PyMuPDF is not installed. Run: python -m pip install pymupdf pillow")

PDF_PATH = Path("source/GL-Revision-Maths.pdf")
QUESTIONS_JS = Path("education-game/questions.js")
OUT_JS = Path("education-game/choice_map.js")
REPORT = Path("choice_extraction_report.txt")

if not PDF_PATH.exists():
    raise SystemExit(f"PDF not found: {PDF_PATH}")

if not QUESTIONS_JS.exists():
    raise SystemExit(f"questions.js not found: {QUESTIONS_JS}")

raw = QUESTIONS_JS.read_text(encoding="utf-8")
m = re.search(r"window\.QUESTIONS\s*=\s*(\[[\s\S]*?\]);\s*window\.SELECTED_REFS", raw)
if not m:
    raise SystemExit("Could not parse window.QUESTIONS from public/questions.js")

questions = json.loads(m.group(1))

def norm(s):
    s = str(s or "").lower().strip()
    s = s.replace("−", "-").replace("–", "-").replace("—", "-")
    s = s.replace("²", "2").replace("³", "3").replace("×", "x")
    s = re.sub(r"degrees?|degree|fahrenheit|celsius", "", s)
    s = re.sub(r"([0-9])\s*°?\s*[cf]\b", r"\1", s)
    s = re.sub(r"metres|meters", "m", s)
    s = s.replace("litres", "l")
    s = re.sub(r"minutes|minute|mins|min", "m", s)
    s = re.sub(r"seconds|second|secs|sec", "s", s)
    s = re.sub(r"hours|hour|hrs|hr", "h", s)
    s = re.sub(r"pounds?", "£", s)
    s = s.replace(" ", "")
    s = re.sub(r"[£°',()]", "", s)
    s = s.replace("and", "")
    return s

def clean(s):
    return re.sub(r"\s+", " ", str(s or "")).strip()

def get_page_text(doc, page_num):
    idx = int(page_num) - 1
    if idx < 0 or idx >= len(doc):
        return ""
    return doc[idx].get_text("text")

def isolate_question(page_text, qnum):
    # Try line based start at the question number, then stop at next question number.
    lines = [ln.rstrip() for ln in page_text.splitlines()]
    start = None
    qpat = re.compile(rf"^\s*{qnum}\b")
    for i, ln in enumerate(lines):
        if qpat.search(ln):
            start = i
            break
    if start is None:
        # fallback: find number anywhere
        pat = re.compile(rf"\b{qnum}\b")
        flat = "\n".join(lines)
        mt = pat.search(flat)
        if not mt:
            return page_text
        nxt = re.search(rf"\b{qnum+1}\b", flat[mt.end():])
        return flat[mt.start(): mt.end() + (nxt.start() if nxt else 2500)]
    end = len(lines)
    next_pat = re.compile(rf"^\s*{qnum+1}\b")
    for j in range(start + 1, len(lines)):
        if next_pat.search(lines[j]):
            end = j
            break
    return "\n".join(lines[start:end])

def parse_options(block):
    text = clean(block)
    options = {}

    # Pattern 1: horizontal options: A 10 B 15 C 20 D 25 E 35
    matches = list(re.finditer(r"(?<![A-Za-z])([A-E])\s+(.+?)(?=(?<![A-Za-z])[A-E]\s+|$)", text))
    for mt in matches:
        letter = mt.group(1)
        value = clean(mt.group(2))
        # Keep short-ish option text; discard if it includes too much question prose.
        if value and len(value) <= 120:
            options[letter] = value

    # Pattern 2: vertical list, one option per line.
    for letter in "ABCDE":
        pat = re.compile(rf"^\s*{letter}\s+(.+)$", re.MULTILINE)
        mt = pat.search(block)
        if mt:
            options[letter] = clean(mt.group(1))

    # Remove obvious trailing page footer contamination.
    for k, v in list(options.items()):
        v = re.split(r"\bPage\s+\d+\b|\bPlease go on\b|\bEnd of Test\b", v)[0].strip()
        options[k] = v

    return options

def find_correct_letter(options, answer):
    ans = clean(answer)
    if re.fullmatch(r"[A-E]", ans, re.I):
        return ans.upper()
    na = norm(ans)
    for letter, opt in options.items():
        if norm(opt) == na:
            return letter
    # Accept containment for cases like "B (Greyholme...)" or "C rectangle"
    for letter, opt in options.items():
        no = norm(opt)
        if na and (na in no or no in na):
            return letter
    return ""

doc = fitz.open(PDF_PATH)
choice_map = {}
ok = 0
fail = 0
lines = []

for q in questions:
    block = isolate_question(get_page_text(doc, q["page"]), int(q["questionNumber"]))
    opts = parse_options(block)
    correct = find_correct_letter(opts, q.get("answer", ""))
    choice_map[q["id"]] = {
        "options": opts,
        "correctLetter": correct,
        "answer": q.get("answer", "")
    }
    if correct:
        ok += 1
        lines.append(f"OK   {q['id']}: {correct}  answer={q.get('answer','')}")
    else:
        fail += 1
        lines.append(f"MISS {q['id']}: answer={q.get('answer','')} options={opts}")

OUT_JS.write_text(
    "window.CHOICE_MAP = " + json.dumps(choice_map, indent=2, ensure_ascii=False) + ";\n",
    encoding="utf-8"
)

REPORT.write_text(
    f"Choice extraction complete.\nMatched: {ok}\nNeeds review: {fail}\n\n" + "\n".join(lines),
    encoding="utf-8"
)

print(f"Choice extraction complete.")
print(f"Matched: {ok}")
print(f"Needs review: {fail}")
print(f"Wrote: {OUT_JS}")
print(f"Report: {REPORT}")
