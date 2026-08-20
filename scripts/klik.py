import asyncio
from playwright.async_api import async_playwright
ROOT='http://127.0.0.1:8899/ira-shkola/'
async def main():
    bad=[]
    async with async_playwright() as pw:
        br=await pw.chromium.launch()
        # мобильное меню
        for w in (390, 430, 900):
            ctx=await br.new_context(viewport={'width':w,'height':800})
            pg=await ctx.new_page()
            await pg.goto(ROOT, wait_until='networkidle')
            vis=await pg.is_visible('#burger')
            if not vis:
                bad.append(f'@{w}: бургер не виден'); await ctx.close(); continue
            await pg.click('#burger')
            await pg.wait_for_timeout(450)          # панель выезжает с анимацией
            if not await pg.is_visible('#mobmenu a'):
                bad.append(f'@{w}: меню не открылось')
            await pg.click('#burger')
            await pg.wait_for_timeout(450)
            if await pg.is_visible('#mobmenu a'):
                bad.append(f'@{w}: меню не закрылось повторным нажатием')
            await pg.click('#burger')
            await pg.wait_for_timeout(450)
            await pg.click('#mobmenu a:has-text("Курсы")')
            await pg.wait_for_load_state('networkidle')
            if 'kursy' not in pg.url:
                bad.append(f'@{w}: переход из мобильного меню не сработал ({pg.url})')
            if await pg.is_visible('#mobmenu a'):
                bad.append(f'@{w}: меню осталось открытым после перехода')
            await ctx.close()
        # десктопное меню и детали
        ctx=await br.new_context(viewport={'width':1440,'height':900})
        pg=await ctx.new_page()
        await pg.goto(ROOT+'kursy/gekata/', wait_until='networkidle')
        d=pg.locator('details.vopros').first
        await d.locator('summary').click()
        if not await d.locator('.otvet').is_visible():
            bad.append('вопрос не раскрылся кликом')
        # проходим все пункты меню кликом
        await pg.goto(ROOT, wait_until='networkidle')
        n=await pg.locator('.nav > a, .nav .hasmega > a').count()
        for i in range(n):
            await pg.goto(ROOT, wait_until='networkidle')
            a=pg.locator('.nav > a, .nav .hasmega > a').nth(i)
            name=(await a.inner_text()).strip()
            await a.click(); await pg.wait_for_load_state('networkidle')
            t=await pg.title()
            if not t or 'Not Found' in t:
                bad.append(f'меню «{name}» ведёт в пустоту: {pg.url}')
        await ctx.close(); await br.close()
    print('ПРОБЛЕМ:',len(bad))
    for b in bad: print('  •',b)
asyncio.run(main())
