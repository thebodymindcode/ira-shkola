# -*- coding: utf-8 -*-
"""Гейт кадров: фотография обязана заполнять рамку целиком.
Ловит две беды разом: срез (часть кадра ушла под нож) и пустые поля
(снимок болтается маленьким внутри большой рамки)."""
import asyncio, glob, os, sys
from playwright.async_api import async_playwright

SREZ_PREDEL = 2      # процентов кадра под ножом
POLE_PREDEL = 2      # процентов площади рамки пустует
MELKO = 300          # кадр уже этого на десктопе выглядит бедно

JS = """() => [...document.querySelectorAll('.split .ph, .kadr .ph')].map(ph => {
  const im = ph.querySelector('img');
  if (!im || !im.naturalWidth) return null;
  const r = ph.getBoundingClientRect();
  const fit = getComputedStyle(im).objectFit;
  const kr = r.width / r.height, ki = im.naturalWidth / im.naturalHeight;
  let srez = 0, pole = 0;
  if (fit === 'cover') srez = kr > ki ? (1 - ki / kr) : (1 - kr / ki);
  if (fit === 'contain') pole = kr > ki ? (1 - ki / kr) : (1 - kr / ki);
  return {src: im.getAttribute('src').split('/').pop(), w: Math.round(r.width),
          h: Math.round(r.height), srez: Math.round(srez * 100), pole: Math.round(pole * 100)};
}).filter(Boolean)"""


async def main():
    stranicy = [''] + sorted({os.path.dirname(p) + '/' for p in
                              glob.glob('*/index.html') + glob.glob('*/*/index.html')})
    bed = []
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        for w in (1280, 375):
            ctx = await br.new_context(viewport={'width': w, 'height': 900})
            pg = await ctx.new_page()
            for p in stranicy:
                await pg.goto('http://127.0.0.1:8899/ira-shkola/' + p, wait_until='load')
                await pg.wait_for_timeout(70)
                for k in await pg.evaluate(JS):
                    if k['srez'] > SREZ_PREDEL:
                        bed.append(f'@{w} {p or "главная":20} {k["src"]:22} срез {k["srez"]}%')
                    if k['pole'] > POLE_PREDEL:
                        bed.append(f'@{w} {p or "главная":20} {k["src"]:22} пустое поле {k["pole"]}%')
                    if w == 1280 and k['w'] < MELKO:
                        bed.append(f'@{w} {p or "главная":20} {k["src"]:22} кадр мелкий {k["w"]}px')
            await ctx.close()
        await br.close()
    print('БРАКА В КАДРАХ:', len(bed))
    for b in bed[:30]:
        print(' ', b)
    sys.exit(1 if bed else 0)

asyncio.run(main())
