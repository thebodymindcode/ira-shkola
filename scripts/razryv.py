# -*- coding: utf-8 -*-
"""Гейт разорванных слов: заголовок не имеет права ломаться посреди слова.
Считает построчно через Range: если строка кончается не на границе слова, это брак."""
import asyncio, glob, os, sys
from playwright.async_api import async_playwright

SHIRINY = (1280, 768, 414, 375, 360)
JS = """() => {
  const bed = [];
  document.querySelectorAll('h1,h2,h3,h4,.eyebrow,.btn').forEach(el => {
    for (const uzel of el.childNodes) {
      if (uzel.nodeType !== 3) continue;
      const t = uzel.textContent;
      const r = document.createRange();
      let prosh = 0, verh = null;
      for (let i = 0; i <= t.length; i++) {
        r.setStart(uzel, i); r.setEnd(uzel, Math.min(i + 1, t.length));
        const box = r.getBoundingClientRect();
        if (!box.height) continue;
        if (verh === null) { verh = box.top; continue; }
        if (box.top - verh > 2) {           // началась новая строка
          const do_ = t[i - 1] || '', posle = t[i] || '';
          if (do_ && posle && !/[\\s\\u00A0.,;:!?)»—-]/.test(do_) && !/[\\s\\u00A0(«]/.test(posle))
            bed.push([el.tagName, t.slice(Math.max(0, i - 14), i) + '|' + t.slice(i, i + 10)]);
          verh = box.top;
        }
        prosh = i;
      }
      r.detach && r.detach();
    }
  });
  return bed;
}"""

async def main():
    stranicy = [''] + sorted({os.path.dirname(p) + '/' for p in
                              glob.glob('*/index.html') + glob.glob('*/*/index.html')})
    bed = []
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        for w in SHIRINY:
            ctx = await br.new_context(viewport={'width': w, 'height': 900})
            pg = await ctx.new_page()
            for p in stranicy:
                await pg.goto('http://127.0.0.1:8899/ira-shkola/' + p, wait_until='load')
                await pg.wait_for_timeout(80)
                for tag, kusok in await pg.evaluate(JS):
                    bed.append(f'@{w} {p or "главная":20} <{tag}> {kusok}')
            await ctx.close()
        await br.close()
    print('РАЗОРВАННЫХ СЛОВ:', len(bed))
    for b in bed[:25]:
        print(' ', b)
    sys.exit(1 if bed else 0)

asyncio.run(main())
