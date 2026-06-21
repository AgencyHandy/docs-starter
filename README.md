# AgencyHandy Documentation

The source for the AgencyHandy documentation site, built with [Mintlify](https://mintlify.com).
The site is organized into three tabs — **For Agency**, **For Client**, and **API Reference** —
and is fully localized into 25 languages.

## Running locally

You need [Node.js](https://nodejs.org) installed.

```bash
# 1. Install the Mintlify CLI (one time)
npm install -g mint

# 2. From the project root, start the live preview
mint dev
```

The site opens at `http://localhost:3000` (it picks the next free port if 3000 is taken)
and hot-reloads as you edit files.

### Useful commands

| Command | What it does |
|---|---|
| `mint dev` | Run the local preview server (also validates `docs.json` on startup). |
| `mint broken-links` | Check every internal link across all languages. |
| `mint update` | Update the Mintlify CLI to the latest version. |

> **Tip:** `mint broken-links` does **not** validate the language switcher config — only
> `mint dev` does. Run `mint dev` after editing `docs.json` to catch schema errors.

## Project structure

```
docs-starter/
├── docs.json              # Site config: theme, colors, logo, navigation, languages
├── index.mdx              # English home page (other langs: <code>/index.mdx)
├── favicon.ico
├── logo/                  # Logo assets (see "Branding" below)
│
├── getting-started/       # ─┐
├── workspace/             #  │
├── crm/                   #  │
├── services/              #  │
├── orders/                #  │  English content for the "For Agency" tab
├── proposals/             #  │
├── invoices/              #  │
├── teams/ tasks/ tickets/ #  │
├── forms/ files/          #  │
├── account/               #  │
├── integrations/          # ─┘  (payments + integrations)
│
├── client/                # English content for the "For Client" tab
├── api/                   # English content for the "API Reference" tab
│
├── fr/  es/  de/  ja/ ...  # Translated copies, one folder per language code.
│                           # Each mirrors the English folder structure exactly.
│
├── scripts/
│   └── assemble_i18n_nav.py  # Regenerates translated nav blocks in docs.json
├── sources/               # Raw scraped reference material (ignored, not published)
└── .mintignore            # Files/folders excluded from the build
```

Every page is an `.mdx` file: YAML frontmatter (`title`, `sidebarTitle`, `description`)
followed by Markdown + Mintlify components (`<Card>`, `<Steps>`, `<Note>`, etc.).
The sidebar/tab order is **not** inferred from the filesystem — it is defined explicitly
in `docs.json` under `navigation.languages[].tabs[].groups[].pages`.

## Branding

The logo is configured in `docs.json` under `"logo"` with light/dark variants:

- `logo/agencyhandy-light.png` — icon + "AgencyHandy product guide", dark text (light mode)
- `logo/agencyhandy-dark.png` — same, white text (dark mode)
- `logo/icon.png` — the standalone purple mark
- `logo/agencyhandy.png` — the original full wordmark

Primary brand color is purple (`#6C5CE7`), set under `"colors"` in `docs.json`.

## Internationalization

The site ships in **25 languages**, configured under `navigation.languages` in `docs.json`.
English (`en`) is the default. Each language has its own folder (e.g. `fr/`, `ja/`, `pt-BR/`)
mirroring the English structure, and its own translated navigation block (tab names, group
names, sidebar anchors, and the Sign In button).

Live languages: `en, fr, es, zh, zh-Hant, de, ko, cs, ja, it, lv, no, ar, sv, da, pl, nl,
tr, uz, ru, pt, pt-BR, id, fi, ro`.

> **Note:** Mintlify only supports a fixed list of language codes. Bengali (`bn`),
> Persian (`fa`), Thai (`th`), Lithuanian (`lt`), and Mongolian (`mn`) are **not** supported —
> their translations exist on disk but are excluded via `.mintignore`.

### ⚠️ Adding or changing a doc — do it for ALL languages

Because every language is a full copy, a change to one page is **not** complete until it's
reflected everywhere. When you **add, rename, move, or delete** a page:

1. **Create the English page** (e.g. `orders/refunds.mdx`).
2. **Add a translated copy in every language folder** at the same relative path
   (`fr/orders/refunds.mdx`, `ja/orders/refunds.mdx`, … for all 25 codes).
   - Translate the frontmatter `title` / `sidebarTitle` / `description` and the body.
   - Prefix internal links with the language code: `/orders/overview` → `/fr/orders/overview`.
   - Leave components, code blocks, icons, URLs, and brand names unchanged.
3. **Register the page in `docs.json`** under the matching group, for **every** language,
   using the language-prefixed path (`fr/orders/refunds`, `ja/orders/refunds`, …).
4. **Validate:** run `mint broken-links` (link integrity) and `mint dev` (schema), and fix
   any reported issues. A common gotcha: straight `"` quotes inside `title="..."` JSX
   attributes break the MDX parser — use curly quotes (`“ ”`) for quoted text in titles.

> If a page exists in `docs.json` for a language but the file is missing, the build fails.
> Keep filenames and folder structure identical across all languages.
