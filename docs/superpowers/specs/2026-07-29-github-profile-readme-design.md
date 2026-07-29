# GitHub Profile README — Design Spec

Date: 2026-07-29
Repo: `AdityaJogdand/AdityaJogdand` (special GitHub profile repo — must be named exactly the account username)

## Goal

Build a GitHub profile README that reads as "opening an AI coding assistant inside a terminal" — minimal, premium, dark, orange-accented, monospace. Inspired by the visual philosophy of tools like Claude Code, Warp, Ghostty, VS Code Dark+, and Cursor, without copying any product's logo, wordmark, or trademarked branding.

## Palette (fixed, no light-mode variant)

| Token | Hex |
|---|---|
| Background | `#0D1117` |
| Panel | `#161B22` |
| Primary text | `#E6EDF3` |
| Secondary text | `#8B949E` |
| Accent (orange) | `#D97706` |
| Borders | `#30363D` |

Orange (`#D97706`) is the single accent color used everywhere an accent is needed — `$` prompts, cursors, the status dot, checkmarks, section labels. There is no separate green; an earlier draft of this spec used `#3FB950` ("prompt green") for terminal-success elements, but the user asked for a single-accent look, so every one of those uses is orange instead.

Typography: JetBrains Mono / IBM Plex Mono / Fira Code — monospace throughout.

## Key technical constraint driving the whole design

GitHub's README HTML sanitizer strips `<style>` blocks and inline `style="..."` attributes from markdown body content. This rules out any approach that colors text via custom CSS classes or inline styles directly in `README.md`. Two techniques get real color and real animation onto the page anyway:

1. **` ```ansi ` fenced code blocks** — GitHub natively renders true-color ANSI escape sequences inside these fences. Used for every "terminal output" content section.
2. **Standalone SVG files referenced via `<img src="assets/....svg">`** — an SVG loaded as an image resource renders its own embedded `<style>` and CSS `@keyframes`/SMIL animations in full, because it's fetched and rendered as an independent document, not sanitized as inline markdown HTML. Used for the animated hero banner and section-divider chip.

Rejected alternatives: rasterizing all content as images (kills copy/search/accessibility), and plain unstyled code fences (fails the brief's "colored terminal" requirement).

## Repo structure

```
AdityaJogdand/
├── README.md
├── assets/
│   ├── banner.svg
│   ├── terminal.svg
│   └── icons/
│       ├── status-dot.svg
│       ├── category-ai.svg
│       ├── category-backend.svg
│       └── category-languages.svg
└── svg/
    └── README.md
```

- `assets/banner.svg` — hero animated terminal window.
- `assets/terminal.svg` — small reusable "> _" divider chip placed between major README sections instead of a plain `---` rule.
- `assets/icons/category-*.svg` — three minimal single-color line glyphs (chip/cpu for AI, server for Backend, angle-brackets for Languages), placed inline next to the corresponding `tree skills` category headers.
- `svg/README.md` — short notes describing how the hand-authored SVG markup and animation timings are structured, so future edits to the animated assets don't require reverse-engineering the keyframes from scratch.

## Hero banner (assets/banner.svg)

- Rounded terminal window: rounded-rect body, soft drop-shadow filter, subtle background gradient (`#0D1117` → `#161B22`).
- Title bar: orange-tinted gradient strip, three **neutral gray-scale** window-control dots (deliberately not red/yellow/green — that combination reads as a generic/macOS terminal cliché; staying neutral keeps the identity original and restrained).
- Body content, revealed via a CSS `@keyframes` typing animation (width/clip-path reveal per line, staggered `animation-delay`, `steps()` timing function for a crisp per-character terminal feel rather than a smooth fade):
  ```
  > whoami

  Aditya Jogdand

  AI Engineer
  Researcher
  LLM Systems
  Backend
  ```
- A blinking block cursor (opacity `@keyframes` loop) follows the last revealed line.
- `Status ● Coding` bottom-right, dot pulsing via the shared `status-dot` animation.
- Fully self-contained SVG (no external font loading — uses SVG `<text>` with `font-family` fallback stack), so it renders identically regardless of viewer.

## Content sections (README.md body)

All rendered as ` ```ansi ` fenced blocks. Color mapping used consistently across every block:
- `$` prompt / command text → orange `#D97706`
- Section/category labels → orange `#D97706`
- Primary values (names, tech names, project names) → near-white `#E6EDF3`
- Secondary/supporting text → gray `#8B949E`
- Checkmarks (research section) → orange `#D97706`

Sections, in order, each preceded by an `<h2>` and (from the second section onward) the `assets/terminal.svg` divider chip:

1. **Hero** — `assets/banner.svg` centered via `<div align="center">`.
2. **About** (`$ cat about.md`) — Name, Location (India), Focus (AI Systems, LLMs, Agents, Research, Backend Engineering), Education (B.Tech AI & DS). Content exactly as user-specified.
3. **Skills** (`$ tree skills`) — three categories exactly as specified (AI: PyTorch, TensorFlow, Transformers, LangChain, HuggingFace; Backend: FastAPI, Flask, PostgreSQL, Redis, Docker; Languages: Python, C++, SQL, JavaScript), tree-drawn with `├──`/`└──` characters. Category icon (`assets/icons/category-*.svg`) sits inline before each category header.
4. **Projects** (`$ tree projects`) — Adaptive-Cognitive-Runtime, Production-RAG, APK-Reasoning-System, Context-Compression, Knowledge-Graphs. Plain styled text, **not hyperlinked** (per user decision). Each gets a plausible one-line AI-engineer-appropriate description authored to fit the name (final wording confirmed at implementation time, easy to hand-edit).
5. **Research** (`$ cat research.md`) — Agent Memory, Context Engineering, Long Context, Efficient Inference, Retrieval, AI Infrastructure, each prefixed with an orange ✓.
6. **GitHub Stats** — `$ ./stats.sh` caption, then a centered `<table>`:
   - Row 1: `github-readme-stats` card + `github-readme-streak-stats` card side by side, both using custom-theme query params set to the exact palette hex values (no `#` prefix, per that service's URL format): `bg_color=0D1117&title_color=D97706&icon_color=D97706&text_color=E6EDF3&border_color=30363D`.
   - Row 2: top-languages card, same custom theme params, full width.
7. **Command Palette** (`$ help`) — lists `whoami`, `skills`, `projects`, `research`, `github`, `resume`, `contact`. Only `resume` and `contact` are real links: `contact` → `mailto:ajogdand375@gmail.com` and `https://www.linkedin.com/in/adityanjogdand/`; `resume` → a clearly marked placeholder anchor (`#TODO_RESUME_LINK`) with a visible `# TODO: add hosted resume link` note so it's easy to find and swap later. The rest render as plain (non-linked) list text.
8. **Footer** (`$ exit`) — "Thanks for visiting.", centered.

## Out of scope

- No JavaScript anywhere (SVG/CSS animation only, per requirement).
- No light-mode palette — single fixed dark theme.
- No real repo links for the projects tree (explicit user decision).
- No `.github/` directory — the contribution-snake workflow was scoped and then dropped by request; GitHub Stats is just the two badge cards + top-languages card.
