# Writes the summary of 11 November 2026 world news to /output/entry.txt
# (or MAKEFUN_OUTPUT_DIR outside the grader). Deterministic: copies the
# fixed summary.txt beside this file, byte for byte; no network, no clock.
import os
import shutil

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
shutil.copyfile(
    os.path.join(os.path.dirname(__file__), "summary.txt"),
    os.path.join(out, "entry.txt"),
)
