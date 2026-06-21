# CLAUDE.md

Guidance for Claude Code working in this repository.

The full agent instructions live in **[AGENTS.md](AGENTS.md)** — read it first. Human-facing
setup and structure are in **[README.md](README.md)**. This file highlights the essentials.

## What this is

A [Mintlify](https://mintlify.com) documentation site for AgencyHandy. Pages are `.mdx`;
all config (theme, colors, logo, navigation, languages) is in `docs.json`. Three tabs —
**For Agency**, **For Client**, **API Reference** — localized into **25 languages**.

## Run & validate

```bash
mint dev            # preview at localhost:3000; validates docs.json schema
mint broken-links   # checks internal links across all languages
```

Run both after any change. Only `mint dev` validates the language config; `mint broken-links`
does not.

## Must-follow rules

1. **Every page change is multiplied across 25 languages.** Each language is a full copy under
   its own folder (`fr/`, `ja/`, `pt-BR/`, …). When adding/renaming/moving/deleting a page:
   do it in English, replicate it in every language folder at the same path (translating
   frontmatter + body, prefixing internal links with the language code, leaving components/
   code/URLs/brand names untouched), and register it in `docs.json` for every language. A page
   listed in `docs.json` but missing on disk fails the build. See AGENTS.md for the full checklist.

2. **Don't re-add unsupported languages.** Mintlify rejects `bn, fa, th, lt, mn`; their files
   are parked on disk and excluded via `.mintignore`.

3. **Watch MDX quotes.** A straight `"` inside a `title="..."` JSX attribute breaks the parser —
   use curly quotes for quoted phrases in Step/Card titles.

## Style

Active voice, second person, sentence-case headings, **bold** for UI elements, `code` for
files/commands/paths. Use consistent product terms (workspace, client, order, task, invoice,
proposal, service, lead, portal, support ticket).
