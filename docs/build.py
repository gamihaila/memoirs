#!/usr/bin/env python3
"""Generate a self-contained index.html from contents.yaml.

Reads the book metadata and chapter list from contents.yaml, then embeds each
chapter's markdown (plain paragraph text) directly into a single styled HTML
file. The output works fully offline (no CDN, no fetch) and opens from file://.

Usage:
    python3 build.py            # reads ./contents.yaml, writes ./index.html
"""

import html
import re


def parse_contents(path='contents.yaml'):
    """Parse the simple, tailored contents.yaml into (meta, chapters)."""
    meta = {}
    chapters = []
    cur = None
    with open(path, encoding='utf-8') as f:
        in_chapters = False
        for raw in f:
            line = raw.rstrip('\n')
            if not line.strip():
                continue
            if line.startswith('chapters:'):
                in_chapters = True
                continue
            if not in_chapters:
                if ':' in line:
                    k, v = line.split(':', 1)
                    meta[k.strip()] = v.strip()
            else:
                m = re.match(r'\s*-\s*file:\s*(.+)', line)
                if m:
                    if cur:
                        chapters.append(cur)
                    cur = {'file': m.group(1).strip()}
                else:
                    m2 = re.match(r'\s*title:\s*(.+)', line)
                    if m2 and cur is not None:
                        cur['title'] = m2.group(1).strip()
        if cur:
            chapters.append(cur)
    return meta, chapters


def md_to_paragraphs(text):
    """Split plain-text markdown into HTML-escaped paragraphs on blank lines."""
    blocks = re.split(r'\n\s*\n', text.strip())
    out = []
    for b in blocks:
        # collapse internal single newlines into spaces
        p = ' '.join(seg.strip() for seg in b.split('\n'))
        p = html.escape(p)
        if p:
            out.append(p)
    return out


def build(contents_path='contents.yaml', out_path='index.html'):
    meta, chapters = parse_contents(contents_path)

    title = meta.get('title', 'Untitled')
    author = meta.get('author', '')
    lang = meta.get('language', 'en')
    cover = meta.get('cover', '')

    toc_items = []
    chapter_html = []
    for i, ch in enumerate(chapters, 1):
        fname = ch['file']
        ctitle = ch.get('title', fname)
        cid = 'ch' + str(i)
        with open(fname, encoding='utf-8') as f:
            paras = md_to_paragraphs(f.read())
        toc_items.append(
            f'      <li><a href="#{cid}"><span class="toc-num">{i}</span>'
            f'<span class="toc-title">{html.escape(ctitle)}</span></a></li>')
        body = '\n'.join(f'      <p>{p}</p>' for p in paras)
        chapter_html.append(f'''    <section class="chapter" id="{cid}">
      <p class="chapter-num">Chapter {i}</p>
      <h2>{html.escape(ctitle)}</h2>
{body}
      <p class="top-link"><a href="#top">&uarr; Contents</a></p>
    </section>''')

    toc = '\n'.join(toc_items)
    chapters_joined = '\n'.join(chapter_html)
    cover_html = (
        f'    <img class="cover" src="{html.escape(cover)}" alt="Cover">\n'
        if cover else '')

    doc = f'''<!DOCTYPE html>
<html lang="{html.escape(lang)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="{html.escape(author)}">
<title>{html.escape(title)}</title>
<style>
  :root {{
    --bg: #f4f1ea;
    --paper: #fffdf8;
    --ink: #2b2620;
    --muted: #8a8172;
    --accent: #7c5c3b;
    --rule: #e3dccd;
  }}
  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font-family: Georgia, "Iowan Old Style", "Palatino Linotype", serif;
    line-height: 1.75;
    font-size: 19px;
  }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}

  header.title-page {{
    max-width: 720px;
    margin: 0 auto;
    padding: 12vh 32px 8vh;
    text-align: center;
  }}
  header.title-page .cover {{
    max-width: 320px;
    width: 60%;
    height: auto;
    border-radius: 4px;
    box-shadow: 0 12px 40px rgba(0,0,0,.28);
    margin-bottom: 40px;
  }}
  header.title-page h1 {{
    font-size: 2.6rem;
    line-height: 1.2;
    margin: 0 0 .4em;
    font-weight: 600;
    letter-spacing: .5px;
  }}
  header.title-page .author {{
    font-size: 1.2rem;
    color: var(--muted);
    font-style: italic;
    margin: 0;
  }}

  nav.toc {{
    max-width: 720px;
    margin: 0 auto;
    padding: 0 32px 6vh;
  }}
  nav.toc h2 {{
    text-align: center;
    font-size: 1rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--muted);
    border-bottom: 1px solid var(--rule);
    padding-bottom: 16px;
    margin-bottom: 8px;
    font-weight: 600;
  }}
  nav.toc ol {{ list-style: none; margin: 0; padding: 0; }}
  nav.toc li a {{
    display: flex;
    align-items: baseline;
    gap: 16px;
    padding: 11px 8px;
    border-bottom: 1px solid var(--rule);
    color: var(--ink);
  }}
  nav.toc li a:hover {{ background: rgba(124,92,59,.06); text-decoration: none; }}
  nav.toc .toc-num {{
    color: var(--accent);
    font-variant-numeric: tabular-nums;
    min-width: 1.8em;
    text-align: right;
    font-size: .95rem;
  }}
  nav.toc .toc-title {{ flex: 1; }}

  main {{
    max-width: 720px;
    margin: 0 auto;
    padding: 0 32px;
  }}
  section.chapter {{
    background: var(--paper);
    padding: 8vh 6% 6vh;
    margin: 40px 0;
    border-radius: 3px;
    box-shadow: 0 1px 3px rgba(0,0,0,.06);
  }}
  section.chapter .chapter-num {{
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 3px;
    font-size: .78rem;
    color: var(--muted);
    margin: 0 0 .3em;
  }}
  section.chapter h2 {{
    text-align: center;
    font-size: 2rem;
    font-weight: 600;
    margin: 0 0 1.6em;
    padding-bottom: .6em;
    border-bottom: 1px solid var(--rule);
  }}
  section.chapter p {{ margin: 0 0 1.1em; text-align: justify; hyphens: auto; }}
  .top-link {{
    text-align: center;
    margin-top: 3em !important;
    font-size: .85rem;
  }}
  .top-link a {{ color: var(--muted); }}

  footer {{
    text-align: center;
    color: var(--muted);
    font-size: .8rem;
    padding: 4vh 32px 8vh;
  }}

  @media (max-width: 600px) {{
    body {{ font-size: 17px; }}
    header.title-page h1 {{ font-size: 2rem; }}
    section.chapter {{ padding: 6vh 7% 5vh; }}
  }}
</style>
</head>
<body>
<a id="top"></a>
<header class="title-page">
{cover_html}    <h1>{html.escape(title)}</h1>
    <p class="author">{html.escape(author)}</p>
</header>

<nav class="toc">
  <h2>Contents</h2>
  <ol>
{toc}
  </ol>
</nav>

<main>
{chapters_joined}
</main>

<footer>
  &copy; {html.escape(author)}
</footer>
</body>
</html>
'''

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(doc)

    print(f"Wrote {out_path} — {len(chapters)} chapters, {len(doc)} bytes")


if __name__ == '__main__':
    build()
