# -*- coding: utf-8 -*-
"""Гейт лиц: считает, сколько исходника срезано сверху в каждом кадре страницы.
Портреты собраны с воздухом 15% над головой, поэтому срез больше 13% = голова под ножом."""
import asyncio, sys, glob, os
from playwright.async_api import async_playwright

PORTRETY = ('p-glavnaya', 'p-irina1', 'p-irina2', 'p-shkola', 'p-taro')
PREDEL = 0.13

async def main():
    stranicy = ['/'] + sorted({os.path.dirname(p).replace('.', '') + '/'
                               for p in glob.glob('*/index.html') + glob.glob('*/*/index.html')})
    bed = []
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        for shirina in (1280, 375):
            ctx = await br.new_context(viewport={'width': shirina, 'height': 900})
            pg = await ctx.new_page()
            for s in stranicy:
                await pg.goto('http://127.0.0.1:8899/ira-shkola' + s, wait_until='load')
                await pg.wait_for_timeout(120)
                dannye = await pg.evaluate("""()=>Array.from(document.images).map(function(im){
                  var r=im.getBoundingClientRect(), st=getComputedStyle(im);
                  if(!r.width||!im.naturalWidth) return null;
                  var poz=parseFloat(st.objectPosition.split(' ')[1])||50;
                  return {src:im.getAttribute('src'), bw:r.width, bh:r.height,
                          iw:im.naturalWidth, ih:im.naturalHeight, fit:st.objectFit, poz:poz};
                }).filter(Boolean)""")
                for d in dannye:
                    if d['fit'] != 'cover':
                        continue
                    k = max(d['bw'] / d['iw'], d['bh'] / d['ih'])
                    vysota = d['ih'] * k
                    lishnee = max(0, vysota - d['bh'])
                    dolya = (lishnee * d['poz'] / 100) / vysota
                    imya = os.path.basename(d['src']).split('.')[0]
                    if imya in PORTRETY and dolya > PREDEL:
                        bed.append(f'{s} [{shirina}px] {imya}: срезано сверху {dolya*100:.0f}%')
            await ctx.close()
        await br.close()
    print('ЛИЦА ПОД НОЖОМ:', len(bed))
    for b in bed:
        print(' ', b)
    sys.exit(1 if bed else 0)

asyncio.run(main())
