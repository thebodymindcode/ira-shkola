# -*- coding: utf-8 -*-
"""Брендированные og-карточки 1200x630 под каждую страницу."""
import asyncio, json, os, sys, base64
sys.path.insert(0, os.path.dirname(__file__))
from playwright.async_api import async_playwright

ROOT = os.path.abspath('.')

def b64(p):
    return "data:image/jpeg;base64," + base64.b64encode(open(p,"rb").read()).decode()


def shablon(zag, pod, img, metka):
    return f"""<!doctype html><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Montserrat:wght@500;600&display=swap" rel="stylesheet">
<style>
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;background:#0E0C11;color:#E9E3DA;
 font-family:Montserrat,sans-serif;display:flex;overflow:hidden}}
.lev{{width:700px;padding:56px 40px 48px 60px;display:flex;flex-direction:column;justify-content:space-between;position:relative;z-index:2}}
.znak{{display:flex;align-items:center;gap:12px;font-family:'Cormorant Garamond',serif;
 font-size:25px;color:#F3EDE3;font-weight:600}}
.znak svg{{width:30px;height:30px;color:#C9A227}}
.metka{{font-size:13px;letter-spacing:2.6px;text-transform:uppercase;color:#C9A227;font-weight:600;margin-bottom:16px}}
h1{{font-family:'Cormorant Garamond',serif;font-size:{54 if len(zag)<34 else 44}px;line-height:1.1;
 font-weight:600;color:#F6F1E8;letter-spacing:.3px}}
p{{margin-top:18px;font-size:19px;line-height:1.5;color:#A79E93;max-width:560px}}
.niz{{font-size:15px;color:#8A8175;letter-spacing:.4px}}
.niz b{{color:#C9A227;font-weight:600}}
.prav{{position:absolute;right:0;top:0;width:620px;height:630px}}
.prav img{{width:100%;height:100%;object-fit:cover;opacity:.95}}
.prav::after{{content:"";position:absolute;inset:0;
 background:linear-gradient(90deg,#0E0C11 0%,rgba(14,12,17,.92) 22%,rgba(14,12,17,.35) 62%,rgba(14,12,17,.12) 100%)}}
.polosa{{position:absolute;left:0;top:0;width:6px;height:630px;background:linear-gradient(180deg,#C9A227,#7A2033)}}
</style>
<div class="prav"><img src="{img}"></div>
<div class="polosa"></div>
<div class="lev">
<div class="znak"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"
 stroke-linecap="round"><circle cx="8" cy="8" r="3.6"/><path d="M10.6 10.6 20 20m-3-3 2-2m-4 1 1.6-1.6"/></svg>
<span>Школа Ирины Волковой</span></div>
<div><div class="metka">{metka}</div><h1>{zag}</h1><p>{pod}</p></div>
<div class="niz"><b>Таро · Магия · Обереги</b> &nbsp;·&nbsp; thebodymindcode.github.io/ira-shkola</div>
</div>"""

async def main():
    articles = json.load(open('content/articles.json', encoding='utf-8'))
    zadachi = [
      ('glavnaya', 'Школа магии и таро', 'Таро, ритуальная магия, руны и домашние обереги. Обучение у Ирины Волковой.', 'images/obrazy/h-glavnaya.jpg', 'Школа'),
      ('shkola', 'Как здесь учат', 'Закрытые каналы, задание после каждой темы, разбор работ вслух.', 'images/obrazy/h-shkola.jpg', 'Обучение'),
      ('kursy', 'Курсы школы', 'Шесть направлений: Геката, руны, бесы, таро, обереги, личная работа.', 'images/obrazy/h-kursy.jpg', 'Курсы'),
      ('gekata', 'Геката: ритуальная магия', 'Четыре ступени работы с богиней перекрёстков, ключей и факелов.', 'images/obrazy/k-gekata.jpg', 'Курс'),
      ('runy', 'Руны: старший футарк', 'Двадцать четыре знака, рунические поэмы, работа с поставом.', 'images/obrazy/k-runy.jpg', 'Курс'),
      ('besy', 'Славянская демонология', 'Кто такие бесы в народной вере и по каким правилам с ними обходились.', 'images/obrazy/k-besy.jpg', 'Курс'),
      ('nastavnichestvo', 'Личная работа', 'Разбор своей практики один на один с Ириной Волковой.', 'images/obrazy/k-nastav.jpg', 'Наставничество'),
      ('taro', 'Обучение таро', 'Вопрос, расклад, чтение связок и разговор с человеком.', 'images/obrazy/h-taro.jpg', 'Направление'),
      ('zhurnal', 'Журнал разборов', 'Двадцать семь разборов про домашние обереги и нечистую силу.', 'images/obrazy/h-zhurnal.jpg', 'Журнал'),
      ('oberegi', 'Обереги славянского дома', 'Нож на ночь, красный угол, крапива у порога, громничная свеча.', 'images/obrazy/h-oberegi.jpg', 'Раздел'),
      ('nechist', 'Нечистая сила деревни', 'Домовой, леший, банник, полудница, мара. Двадцать разборов.', 'images/obrazy/h-nechist.jpg', 'Раздел'),
      ('irina', 'Ирина Волкова', 'Первая колода в одиннадцать лет, практика с двадцати трёх, курсы с 2014 года.', 'images/obrazy/h-irina.jpg', 'Кто ведёт'),
      ('vopros', 'Вопросы о школе', 'С чего начать, нужен ли дар, как идут потоки и чем занимается школа.', 'images/obrazy/h-vopros.jpg', 'Вопросы'),
      ('kontakty', 'Как связаться', 'Телеграм-канал школы и Instagram Ирины Волковой.', 'images/obrazy/h-kontakty.jpg', 'Связь'),
    ]
    for a in articles:
        zadachi.append((f'st-{a["slug"]}', a['name'], a['anons'],
                        f'images/zhurnal/{a["slug"]}.jpg',
                        'Обереги дома' if a['kind'] == 'oberegi' else 'Нечисть'))
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        ctx = await br.new_context(viewport={'width': 1200, 'height': 630}, device_scale_factor=1)
        pg = await ctx.new_page()
        for name, zag, pod, img, metka in zadachi:
            await pg.set_content(shablon(zag, pod, b64(img), metka))
            await pg.wait_for_timeout(700)
            await pg.screenshot(path=f'images/og/{name}.jpg', type='jpeg', quality=86)
        await ctx.close(); await br.close()
    print('og-карточек:', len(zadachi))

asyncio.run(main())
