# -*- coding: utf-8 -*-
"""Гейт геометрии: левые края, горизонтальный скролл, SVG, рамки фото, консоль."""
import asyncio, sys, json
from playwright.async_api import async_playwright

ROOT = 'http://127.0.0.1:8899/ira-shkola/'
PAGES = ['', 'shkola/', 'kursy/', 'kursy/gekata/', 'kursy/runy/', 'kursy/besy/',
         'kursy/nastavnichestvo/', 'taro/', 'zhurnal/', 'oberegi/', 'nechist/',
         'ob-irine/', 'vopros-otvet/', 'kontakty/', 'politika/',
         'zhurnal/02-domovoy/', 'zhurnal/16-upyr/', 'zhurnal/01-otlivka-voskom/']
SHIRINY = [1440, 1024, 430, 390, 375]

async def main():
    problems = []
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        for w in SHIRINY:
            ctx = await br.new_context(viewport={'width': w, 'height': 900},
                                       device_scale_factor=1)
            page = await ctx.new_page()
            errs = []
            page.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
            page.on('pageerror', lambda e: errs.append(str(e)))
            for p in PAGES:
                await page.goto(ROOT + p, wait_until='networkidle')
                r = await page.evaluate("""() => {
                  const out = {scroll: document.documentElement.scrollWidth > window.innerWidth + 1,
                              sw: document.documentElement.scrollWidth, iw: window.innerWidth,
                              lefts: [], bigsvg: [], ramki: [], centr: 0, h: document.body.scrollHeight};
                  document.querySelectorAll('section > .wrap > h2, section > .wrap > .eyebrow, section > .wrap > h1, main > section .wrap > h2').forEach(el=>{
                    const b = el.getBoundingClientRect(); out.lefts.push(Math.round(b.left));
                  });
                  document.querySelectorAll('svg').forEach(el=>{
                    const b = el.getBoundingClientRect();
                    if (b.width > 60 || b.height > 60) out.bigsvg.push([el.getAttribute('class')||'', Math.round(b.width), Math.round(b.height)]);
                  });
                  document.querySelectorAll('.ph').forEach(el=>{
                    const img = el.querySelector('img'); if(!img) return;
                    const a = el.getBoundingClientRect(), b = img.getBoundingClientRect();
                    if (Math.abs(a.height-b.height) > 4 || Math.abs(a.width-b.width) > 4)
                      out.ramki.push([Math.round(a.height), Math.round(b.height)]);
                  });
                  document.querySelectorAll('*').forEach(el=>{
                    const st = getComputedStyle(el);
                    if (st.textAlign === 'center' && el.textContent.trim().length > 40) out.centr++;
                  });
                  return out;
                }""")
                if r['scroll']:
                    problems.append(f'{p} @{w}: горизонтальная прокрутка {r["sw"]}>{r["iw"]}')
                lefts = sorted(set(r['lefts']))
                if len(lefts) > 1:
                    problems.append(f'{p} @{w}: разные левые края заголовков {lefts}')
                if r['bigsvg']:
                    problems.append(f'{p} @{w}: крупные svg {r["bigsvg"][:3]}')
                if r['ramki']:
                    problems.append(f'{p} @{w}: фото не заполняет рамку {r["ramki"][:3]}')
                if r['centr']:
                    problems.append(f'{p} @{w}: центрированный длинный текст, блоков {r["centr"]}')
                if w == 390 and r['h'] > 900 * 16:
                    problems.append(f'{p} @390: страница {round(r["h"]/900,1)} экранов, тяжело')
            if errs:
                problems.append(f'@{w}: ошибки консоли {errs[:3]}')
            await ctx.close()
        await br.close()
    print('ПРОБЛЕМ:', len(problems))
    for x in problems:
        print('  •', x)

asyncio.run(main())
