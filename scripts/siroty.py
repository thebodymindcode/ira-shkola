# -*- coding: utf-8 -*-
"""Гейт сирот: ищет строки из одного слова в заголовках, лидах, врезках и кнопках."""
import asyncio, sys
from playwright.async_api import async_playwright

ROOT = 'http://127.0.0.1:8899/ira-shkola/'
PAGES = ['', 'shkola/', 'kursy/', 'kursy/gekata/', 'kursy/runy/', 'kursy/besy/',
         'kursy/nastavnichestvo/', 'taro/', 'zhurnal/', 'oberegi/', 'nechist/',
         'ob-irine/', 'vopros-otvet/', 'kontakty/', 'politika/',
         'zhurnal/domovoy/', 'zhurnal/leshy/', 'zhurnal/upyr/', 'zhurnal/nozh-na-noch/']
SHIRINY = [int(x) for x in (sys.argv[1:] or ['1440', '390', '375'])]

JS = """() => {
  const sel = 'h1,h2,h3,.lid,.podzag,.vrez,.btn,.fside b,.side .cifra,.zov h3,.card h3,.kadr h3,.niz span,.kroshki';
  const out = [];
  document.querySelectorAll(sel).forEach(el => {
    const t = el.textContent.replace(/\\s+/g,' ').trim();
    if (!t || t.split(' ').length < 3) return;
    const r = document.createRange();
    const walk = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    const stroki = [];
    let node;
    while (node = walk.nextNode()) {
      const s = node.textContent;
      let start = 0;
      for (let i = 0; i <= s.length; i++) {
        if (i === s.length || s[i] === ' ' || s[i] === '\\u00a0') {
          if (i > start) {
            r.setStart(node, start); r.setEnd(node, i);
            const b = r.getBoundingClientRect();
            stroki.push([Math.round(b.top), s.slice(start, i)]);
          }
          start = i + 1;
        }
      }
    }
    if (!stroki.length) return;
    const po = {};
    stroki.forEach(([y, w]) => { (po[y] = po[y] || []).push(w); });
    const ys = Object.keys(po).map(Number).sort((a,b)=>a-b);
    if (ys.length < 2) return;
    const last = po[ys[ys.length-1]];
    if (last.length === 1 && last[0].length > 1)
      out.push([el.className || el.tagName, t.slice(0,58), last[0]]);
  });
  return out;
}"""

async def main():
    vsego = 0
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        for w in SHIRINY:
            ctx = await br.new_context(viewport={'width': w, 'height': 900})
            pg = await ctx.new_page()
            for p in PAGES:
                await pg.goto(ROOT + p, wait_until='networkidle')
                await pg.wait_for_timeout(150)
                r = await pg.evaluate(JS)
                for cls, txt, hvost in r:
                    vsego += 1
                    print(f'@{w} {p or "главная":22} [{cls[:16]}] …{hvost}  ← {txt}')
            await ctx.close()
        await br.close()
    print('СИРОТ:', vsego)

asyncio.run(main())
