# Agent instructions — AgencyHandy Documentation

Instructions for AI coding agents working in this repository. Human contributors should
read [README.md](README.md) for setup and structure; this file captures the rules an agent
must follow to avoid breaking the build.

## About this project

- A documentation site built on [Mintlify](https://mintlify.com).
- Pages are `.mdx` files: YAML frontmatter (`title`, `sidebarTitle`, `description`) + Markdown
  and Mintlify components (`<Card>`, `<CardGroup>`, `<Steps>`, `<Note>`, `<Tip>`, etc.).
- All configuration (theme, colors, logo, navigation, languages) lives in `docs.json`.
- The site has three tabs — **For Agency**, **For Client**, **API Reference** — and is
  localized into **25 languages**.

## Running and validating

```bash
mint dev            # local preview at http://localhost:3000; validates docs.json on startup
mint broken-links   # checks internal links across all languages
```

Always run **both** before considering a change done:
- `mint broken-links` catches broken internal links.
- `mint dev` catches `docs.json` schema errors (including invalid language codes), which
  `mint broken-links` does **not** check.

## 🌍 The #1 rule: every page change is multiplied across 25 languages

Each language is a complete copy of the docs under its own folder (`fr/`, `es/`, `ja/`,
`pt-BR/`, …), mirroring the English structure. A change is **not** complete until it is
reflected in every language.

When you **add, rename, move, or delete** a page:

1. Make the change to the **English** page (root-level folders like `orders/`, `client/`, `api/`).
2. Apply the same change to **every language folder** at the identical relative path.
   - Translate frontmatter `title` / `sidebarTitle` / `description` and the body prose.
   - Prefix internal links with the language code: `/orders/overview` → `/fr/orders/overview`.
   - Do **not** translate: component names, attribute names, `icon="..."` values, `className`,
     code blocks, inline code, URLs, or brand names (AgencyHandy, Stripe, PayPal, Slack, …).
3. Register the page in `docs.json` for **every** language, using the language-prefixed path
   (`fr/orders/refunds`, `ja/orders/refunds`, …), under the correct group.
4. Validate with `mint broken-links` and `mint dev`.

If `docs.json` references a page that doesn't exist on disk, the build fails. Keep filenames
and folder structure identical across all languages.

### Supported languages

Live: `en` (default), `fr, es, zh, zh-Hant, de, ko, cs, ja, it, lv, no, ar, sv, da, pl, nl,
tr, uz, ru, pt, pt-BR, id, fi, ro`.

Mintlify only accepts a fixed enum of language codes. **Bengali (bn), Persian (fa), Thai (th),
Lithuanian (lt), Mongolian (mn) are NOT supported** — their translated files remain on disk
but are excluded via `.mintignore` and removed from `docs.json`. Do not re-add them to the
navigation; `mint dev` will reject them.

`scripts/assemble_i18n_nav.py` regenerates the translated navigation blocks in `docs.json`
from a labels map + the canonical English structure.

## MDX gotchas

- **Quotes in `title="..."`**: a straight `"` inside a JSX attribute value breaks the MDX
  parser. Use curly quotes (`“ ”`, or `„ “`/`„ ”` per language) for quoted phrases inside
  Step/Card titles. Single quotes `'...'` are also safe.
- Headings, anchors, and links inside translated pages must use the language-prefixed path.

## Style preferences

- Active voice, second person ("you").
- Concise sentences — one idea per sentence.
- Sentence case for headings.
- **Bold** for UI elements: Click **Settings**.
- `Code formatting` for file names, commands, paths, fields, and code references.

## Terminology

Use AgencyHandy product terms consistently: **workspace** (not "project"), **client**,
**order**, **task**, **invoice**, **proposal**, **service**, **lead**, **portal**,
**support ticket**, **team member**.
