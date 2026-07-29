#!/usr/bin/env python3
"""Verifies generate_readme.py produces the expected structure and byte-exact ANSI codes.

Run: python3 scripts/test_generate_readme.py
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"

PROJECT_NAMES = [
    "Adaptive-Cognitive-Runtime",
    "Production-RAG",
    "APK-Reasoning-System",
    "Context-Compression",
    "Knowledge-Graphs",
]


def check(condition: bool, message: str) -> None:
    if not condition:
        print(f"FAIL: {message}")
        sys.exit(1)
    print(f"PASS: {message}")


def main() -> None:
    subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "generate_readme.py")],
        check=True,
    )
    text = README.read_text(encoding="utf-8")

    check(README.exists(), "README.md was created")
    check(text.count("```ansi") == 7, "contains exactly 7 ansi fenced blocks")
    check("\x1b[38;2;217;119;6m" in text, "contains orange truecolor escape (#D97706)")
    check("\x1b[38;2;63;185;80m" not in text, "contains no green truecolor escape (single-accent design, no #3FB950 anywhere)")
    check("\x1b[38;2;230;237;243m" in text, "contains primary-text truecolor escape (#E6EDF3)")
    check("\x1b[38;2;139;148;158m" in text, "contains secondary-text truecolor escape (#8B949E)")
    check("\x1b[0m" in text, "contains ANSI reset codes")
    check('<img src="assets/banner.svg"' in text, "hero banner is embedded")
    check('<img src="assets/terminal.svg"' in text, "section divider is embedded")
    check('<img src="assets/icons/category-ai.svg"' in text, "AI category icon is embedded")
    check('<img src="assets/icons/category-backend.svg"' in text, "Backend category icon is embedded")
    check('<img src="assets/icons/category-languages.svg"' in text, "Languages category icon is embedded")
    check("mailto:ajogdand375@gmail.com" in text, "contact mailto link present")
    check("https://www.linkedin.com/in/adityanjogdand/" in text, "LinkedIn link present")
    check("#TODO_RESUME_LINK" in text, "resume placeholder link present")
    check("github-readme-stats.vercel.app" in text, "GitHub stats card embedded")
    check("streak-stats.demolab.com" in text, "streak stats card embedded")
    check("Adaptive-Cognitive-Runtime" in text, "projects section lists Adaptive-Cognitive-Runtime")
    for name in PROJECT_NAMES:
        check(f"[{name}](" not in text, f"{name} is not wrapped in a markdown link")

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
