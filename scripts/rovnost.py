# -*- coding: utf-8 -*-
"""Гейт ровности: единый левый край, совпадение верхов в парных блоках, ровные ряды карточек."""
import asyncio, sys
from playwright.async_api import async_playwright

ROOT='http://127.0.0.1:8899/ira-shkola/'
PAGES=['','shkola/','kursy/','kursy/grimuar/','kursy/besy/','kursy/gekata/','kursy/runy/',
       'kursy/nastavnichestvo/','taro/','karty/','karty/luna/','kviz/','luna/','slovar/',
       'zhurnal/','oberegi/','nechist/','ob-irine/','vopros-otvet/','kontakty/','zhurnal/domovoy/']

JS = """() => {
  const p = [];
  // 1. один левый край у заголовков секций
  const kraya = new Set();
  document.querySelectorAll('main section > .wrap > h2, main section > .wrap > .eyebrow, main section > .wrap > h1, main section > .wrap > .lid')
    .forEach(el => kraya.add(Math.round(el.getBoundingClientRect().left)));
  if (kraya.size > 1) p.push('разные левые края: ' + [...kraya].sort((a,b)=>a-b).join(', '));
  // 2. парные блоки: верх и низ вровень
  document.querySelectorAll('.split, .tside').forEach(s => {
    const a = s.children[0], b = s.children[1];
    if (!a || !b) return;
    const ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
    const dve = ra.width < s.getBoundingClientRect().width * 0.72;   // колонки рядом, а не стопкой
    if (dve && Math.abs(ra.top - rb.top) > 3)
      p.push('верх не вровень: ' + Math.round(ra.top - rb.top) + 'px');
  });
  // 3. ряды карточек одной высоты
  document.querySelectorAll('.grid2, .grid3').forEach(g => {
    const h = [...g.children].map(c => Math.round(c.getBoundingClientRect().height));
    const ryady = {};
    [...g.children].forEach((c, i) => {
      const t = Math.round(c.getBoundingClientRect().top);
      (ryady[t] = ryady[t] || []).push(h[i]);
    });
    Object.values(ryady).forEach(r => {
      if (r.length > 1 && Math.max(...r) - Math.min(...r) > 2)
        p.push('карточки ряда разной высоты: ' + r.join('/'));
    });
  });
  // 4. картинки заполняют рамку
  document.querySelectorAll('.ph').forEach(f => {
    const im = f.querySelector('img'); if (!im) return;
    const a = f.getBoundingClientRect(), b = im.getBoundingClientRect();
    if (Math.abs(a.height - b.height) > 3 || Math.abs(a.width - b.width) > 3)
      p.push('фото не заполняет рамку');
  });
  return p;
}"""

async def main():
    shiriny=[int(x) for x in (sys.argv[1:] or ['1440','390'])]
    vsego=0
    async with async_playwright() as pw:
        br=await pw.chromium.launch()
        for w in shiriny:
            ctx=await br.new_context(viewport={'width':w,'height':900}); pg=await ctx.new_page()
            for u in PAGES:
                await pg.goto(ROOT+u, wait_until='networkidle')
                await pg.evaluate("document.querySelectorAll('img[loading]').forEach(i=>i.removeAttribute('loading'))")
                await pg.wait_for_timeout(180)
                for s in set(await pg.evaluate(JS)):
                    vsego+=1
                    print(f'@{w} {u or "главная":22} {s}')
            await ctx.close()
        await br.close()
    print('НЕРОВНОСТЕЙ:', vsego)

asyncio.run(main())
