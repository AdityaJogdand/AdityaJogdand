#!/usr/bin/env python3
"""Generates README.md from the section content defined below.

Run: python3 scripts/generate_readme.py
"""

from pathlib import Path

ORANGE = "#D97706"
PRIMARY = "#E6EDF3"
SECONDARY = "#8B949E"

REPO_ROOT = Path(__file__).resolve().parent.parent


def _rgb(hex_color: str) -> tuple[int, int, int]:
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def c(hex_color: str, text: str) -> str:
    r, g, b = _rgb(hex_color)
    return f"\x1b[38;2;{r};{g};{b}m{text}\x1b[0m"


def ansi_block(lines: list[str]) -> str:
    body = "\n".join(lines)
    return f"```ansi\n{body}\n```"


ABOUT = ansi_block([
    c(ORANGE, "$ cat about.md"),
    "",
    c(ORANGE, "Name:"),
    c(PRIMARY, "  Aditya Jogdand"),
    "",
    c(ORANGE, "Location:"),
    c(PRIMARY, "  India"),
    "",
    c(ORANGE, "Focus:"),
    c(SECONDARY, "  AI Systems"),
    c(SECONDARY, "  LLMs"),
    c(SECONDARY, "  Agents"),
    c(SECONDARY, "  Research"),
    c(SECONDARY, "  Backend Engineering"),
    "",
    c(ORANGE, "Education:"),
    c(PRIMARY, "  B.Tech AI & DS"),
])

SKILLS = ansi_block([
    c(ORANGE, "$ tree skills"),
    "",
    c(ORANGE, "AI/"),
    c(PRIMARY, "├── PyTorch"),
    c(PRIMARY, "├── TensorFlow"),
    c(PRIMARY, "├── Transformers"),
    c(PRIMARY, "├── LangChain"),
    c(PRIMARY, "└── HuggingFace"),
    "",
    c(ORANGE, "Backend/"),
    c(PRIMARY, "├── FastAPI"),
    c(PRIMARY, "├── Flask"),
    c(PRIMARY, "├── PostgreSQL"),
    c(PRIMARY, "├── Redis"),
    c(PRIMARY, "└── Docker"),
    "",
    c(ORANGE, "Languages/"),
    c(PRIMARY, "├── Python"),
    c(PRIMARY, "├── C++"),
    c(PRIMARY, "├── SQL"),
    c(PRIMARY, "└── JavaScript"),
])

PROJECTS = ansi_block([
    c(ORANGE, "$ tree projects"),
    "",
    c(PRIMARY, "├── Adaptive-Cognitive-Runtime") + "  " + c(SECONDARY, "# self-tuning inference runtime that adapts context strategy per query"),
    c(PRIMARY, "├── Production-RAG") + "  " + c(SECONDARY, "# retrieval-augmented pipeline hardened for production traffic"),
    c(PRIMARY, "├── APK-Reasoning-System") + "  " + c(SECONDARY, "# static + LLM-assisted reasoning over Android APK behavior"),
    c(PRIMARY, "├── Context-Compression") + "  " + c(SECONDARY, "# long-context compression for cheaper, faster LLM calls"),
    c(PRIMARY, "└── Knowledge-Graphs") + "  " + c(SECONDARY, "# entity/relation extraction feeding graph-grounded retrieval"),
])

RESEARCH = ansi_block([
    c(ORANGE, "$ cat research.md"),
    "",
    c(SECONDARY, "Current interests:"),
    "",
    c(ORANGE, "✓ ") + c(PRIMARY, "Agent Memory"),
    c(ORANGE, "✓ ") + c(PRIMARY, "Context Engineering"),
    c(ORANGE, "✓ ") + c(PRIMARY, "Long Context"),
    c(ORANGE, "✓ ") + c(PRIMARY, "Efficient Inference"),
    c(ORANGE, "✓ ") + c(PRIMARY, "Retrieval"),
    c(ORANGE, "✓ ") + c(PRIMARY, "AI Infrastructure"),
])

STATS_CAPTION = ansi_block([
    c(ORANGE, "$ ./stats.sh"),
])

HELP = ansi_block([
    c(ORANGE, "$ help"),
    "",
    c(SECONDARY, "Available commands"),
    "",
    c(PRIMARY, "whoami"),
    c(PRIMARY, "skills"),
    c(PRIMARY, "projects"),
    c(PRIMARY, "research"),
    c(PRIMARY, "github"),
    c(ORANGE, "resume") + c(SECONDARY, "    -> see link below"),
    c(ORANGE, "contact") + c(SECONDARY, "   -> see link below"),
])

EXIT = ansi_block([
    c(ORANGE, "$ exit"),
    "",
    c(PRIMARY, "Thanks for visiting."),
])

GH_USER = "AdityaJogdand"
STATS_THEME = "bg_color=0D1117&title_color=D97706&icon_color=D97706&text_color=E6EDF3&border_color=30363D"
STREAK_THEME = (
    "background=0D1117&border=30363D&stroke=30363D&ring=D97706&fire=D97706"
    "&currStreakNum=E6EDF3&sideNums=E6EDF3&currStreakLabel=E6EDF3&sideLabels=8B949E&dates=8B949E"
)

DIVIDER = '<div align="center">\n  <img src="assets/terminal.svg" width="480" alt="">\n</div>'

README = f"""<div align="center">
  <img src="assets/banner.svg" width="760" alt="Terminal banner: whoami output for Aditya Jogdand">
</div>

<br>

## About

{ABOUT}

{DIVIDER}

## Skills

<img src="assets/icons/category-ai.svg" width="16" alt=""> **AI**&nbsp;&nbsp;&nbsp;
<img src="assets/icons/category-backend.svg" width="16" alt=""> **Backend**&nbsp;&nbsp;&nbsp;
<img src="assets/icons/category-languages.svg" width="16" alt=""> **Languages**

{SKILLS}

{DIVIDER}

## Projects

{PROJECTS}

{DIVIDER}

## Research

{RESEARCH}

{DIVIDER}

## GitHub Stats

{STATS_CAPTION}

<div align="center">
<table>
<tr>
<td width="50%">
<img src="https://github-readme-stats.vercel.app/api?username={GH_USER}&show_icons=true&hide_border=true&{STATS_THEME}" alt="GitHub stats" width="100%">
</td>
<td width="50%">
<img src="https://streak-stats.demolab.com/?user={GH_USER}&hide_border=true&{STREAK_THEME}" alt="GitHub streak stats" width="100%">
</td>
</tr>
<tr>
<td colspan="2">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username={GH_USER}&layout=compact&hide_border=true&{STATS_THEME}" alt="Top languages" width="100%">
</td>
</tr>
</table>
</div>

{DIVIDER}

## Command Palette

{HELP}

<div align="center">

[resume](#TODO_RESUME_LINK) <!-- TODO: replace with hosted resume link --> &middot; [contact](mailto:ajogdand375@gmail.com) &middot; [LinkedIn](https://www.linkedin.com/in/adityanjogdand/)

</div>

{DIVIDER}

<div align="center">

{EXIT}

</div>
"""


def main() -> None:
    (REPO_ROOT / "README.md").write_text(README, encoding="utf-8")
    print(f"Wrote {REPO_ROOT / 'README.md'}")


if __name__ == "__main__":
    main()
