# SVG Source Notes

Hand-authored SVGs live in `assets/`. This file documents how they're built so future edits don't require reverse-engineering the animation timing.

## Shared conventions

- Font stack: `"JetBrains Mono", "Fira Code", "IBM Plex Mono", ui-monospace, monospace` — matches the README's monospace requirement even where the font isn't installed on the viewer's system (falls through to their OS monospace default).
- Colors are always the literal hex values from the palette (`#0D1117`, `#161B22`, `#E6EDF3`, `#8B949E`, `#D97706`, `#30363D`) — never CSS variables for color, since GitHub loads each SVG as an independent image document with no shared stylesheet across files. `#D97706` is the single accent — there is no separate green.
- Animations use CSS `@keyframes` inside an inline `<style>` element. This only works because each SVG is referenced via `<img src="assets/...">` rather than pasted inline into the README body — GitHub strips `<style>` blocks and animations when SVG markup is inlined directly into markdown, but renders a linked SVG file as its own document with full CSS support.
- Typewriter reveal effect (used in `banner.svg`): each line of text sits behind a `<clipPath>` containing a `<rect class="line-clip">`. That rect's `width` animates from `0` to a per-line `--w` custom property via the shared `typeLine` keyframe, with a per-line `animation-delay` inline style so lines reveal in sequence. `animation-fill-mode: both` keeps the rect at width `0` before its delay elapses and holds it at full `--w` after the animation finishes, so lines that haven't "typed" yet stay invisible instead of flashing full-width at load.
- Blinking cursor: `opacity` toggled with `steps(1, end)`, not `ease`, so it snaps instantly like a real terminal cursor rather than fading in and out.
- Status dot pulse: `transform: scale()` + `opacity` on a loop, with `transform-origin` set to the dot's own center so it scales in place instead of drifting.

## Files

| File | Purpose | Animated? |
|---|---|---|
| `assets/banner.svg` | Hero terminal window | Yes — typewriter lines, blinking cursor, pulsing status dot |
| `assets/terminal.svg` | Section-divider chip | Yes — blinking cursor block |
| `assets/icons/status-dot.svg` | Standalone pulsing dot | Yes |
| `assets/icons/category-ai.svg`, `category-backend.svg`, `category-languages.svg` | Static single-color line icons for the skills section | No |

## Editing

Each SVG is fully self-contained (its own `<style>`, its own `<defs>`) because GitHub renders every `<img>`-referenced SVG as an independent document — there is no way to share a stylesheet or a `<symbol>` library across separate files on GitHub. If a color or the font stack changes, update it in every file individually.
