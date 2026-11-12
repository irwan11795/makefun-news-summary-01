# Writes the summary of 11 November 2026 world news to /output/entry.txt
# (or MAKEFUN_OUTPUT_DIR outside the grader). Deterministic: copies the
# fixed summary.txt beside this file; no network, no clock. Enforces the
# competition's 1-2,000 code-point limit before writing, so an over-long
# summary fails loudly here instead of at the gate.
import os

here = os.path.dirname(__file__)
with open(os.path.join(here, "summary.txt"), encoding="utf-8") as f:
    text = f.read()
if not 1 <= len(text) <= 2000:
    raise SystemExit(f"summary.txt is {len(text)} code points, outside 1-2000")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(text)
