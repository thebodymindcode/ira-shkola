import asyncio
from playwright.async_api import async_playwright
ROOT='http://127.0.0.1:8899/ira-shkola/'
PAGES=[('','glavnaya'),('shkola/','shkola'),('kursy/','kursy'),('kursy/gekata/','gekata'),
       ('kursy/runy/','runy'),('kursy/besy/','besy'),('kursy/nastavnichestvo/','nastav'),
       ('taro/','taro'),('zhurnal/','zhurnal'),('oberegi/','oberegi'),('nechist/','nechist'),
       ('ob-irine/','irina'),('vopros-otvet/','faq'),('kontakty/','kontakty'),
       ('zhurnal/02-domovoy/','statya-domovoy'),('politika/','politika')]
async def main():
    async with async_playwright() as pw:
        br=await pw.chromium.launch()
        for w,tag in ((1440,'d'),(390,'m')):
            ctx=await br.new_context(viewport={'width':w,'height':1000},device_scale_factor=1)
            pg=await ctx.new_page()
            for path,name in PAGES:
                await pg.goto(ROOT+path,wait_until='networkidle')
                await pg.wait_for_timeout(350)
                await pg.screenshot(path=f'/tmp/skrin-ira/{tag}-{name}.jpg',full_page=True,
                                    type='jpeg',quality=72)
            await ctx.close()
        await br.close()
asyncio.run(main())
print('готово')
