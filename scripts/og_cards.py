# -*- coding: utf-8 -*-
"""Брендированные og-карточки 1200x630 под каждую страницу."""
import asyncio, json, os, sys, base64
sys.path.insert(0, os.path.dirname(__file__))
from playwright.async_api import async_playwright

ROOT = os.path.abspath('.')

def b64(p):
    return "data:image/jpeg;base64," + base64.b64encode(open(p,"rb").read()).decode()


ZNAK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
        'stroke-linecap="round"><circle cx="8" cy="8" r="3.6"/>'
        '<path d="M10.6 10.6 20 20m-3-3 2-2m-4 1 1.6-1.6"/></svg>')


def ikonka(imya):
    import engine
    d = engine.ICONS.get(imya) or engine.MENU_ICONS.get(imya) or ''
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" '
            'stroke-linecap="round" stroke-linejoin="round">' + d + '</svg>')


def shablon(zag, pod, img, metka, bullety, portret=''):
    """Карточка ссылки. Телеграм в ленте режет её до квадрата по центру,
    поэтому вся смысловая часть стоит по центру, а не у левого края."""
    razmer = 54 if len(zag) < 22 else (46 if len(zag) < 32 else 39)
    puli = ''.join(f'<span class="puly">{ikonka(i)}{t}</span>' for i, t in bullety)
    portret_html = (f'<div class="portret"><img src="{portret}"></div>' if portret else '')
    return f"""<!doctype html><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Prata&family=Forum&family=Montserrat:wght@500;600&display=swap" rel="stylesheet">
<style>
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;background:#0E0C11;color:#E9E3DA;font-family:Montserrat,sans-serif;
 position:relative;overflow:hidden}}
.fon{{position:absolute;inset:0}}
.fon img{{width:100%;height:100%;object-fit:cover;opacity:.8}}
.fon::after{{content:"";position:absolute;inset:0;background:
 radial-gradient(78% 68% at 50% 48%,rgba(14,12,17,.36) 0%,rgba(14,12,17,.74) 58%,rgba(14,12,17,.94) 100%),
 linear-gradient(180deg,rgba(14,12,17,.72) 0%,rgba(14,12,17,.12) 30%,rgba(14,12,17,.86) 100%)}}
.svet{{position:absolute;left:50%;top:52%;width:920px;height:560px;transform:translate(-50%,-50%);
 background:radial-gradient(closest-side,rgba(201,162,39,.2),rgba(201,162,39,.05) 55%,transparent 78%);
 z-index:1}}
.in{{position:relative;z-index:2;height:630px;display:flex;flex-direction:column;
 align-items:center;justify-content:space-between;text-align:center;padding:40px 60px 36px}}
.znak{{display:flex;align-items:center;gap:11px;font-family:Prata,serif;font-size:23px;color:#F3EDE3}}
.znak svg{{width:28px;height:28px;color:#C9A227}}
.serdce{{display:flex;flex-direction:column;align-items:center;gap:15px;max-width:600px}}
.metka{{font-family:Forum,serif;font-size:15px;letter-spacing:5px;text-transform:uppercase;color:#C9A227}}
h1{{font-family:Prata,serif;font-size:{razmer}px;line-height:1.14;color:#F8F4EC;letter-spacing:.2px;
 text-shadow:0 6px 30px rgba(0,0,0,.6)}}
p{{font-size:19px;line-height:1.5;color:#C6BEB2;max-width:560px}}
.puli{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:4px}}
.puly{{display:inline-flex;align-items:center;gap:9px;padding:10px 17px;border-radius:999px;
 border:1px solid rgba(201,162,39,.42);background:rgba(201,162,39,.1);
 font-size:16px;font-weight:600;color:#F0E7D2;white-space:nowrap}}
.puly svg{{width:20px;height:20px;color:#E3C15B;flex:0 0 20px}}
.niz{{font-size:15px;color:#9C9284;letter-spacing:.4px}}
.niz b{{color:#C9A227;font-weight:600}}
.portret{{position:absolute;right:-8px;top:0;height:630px;width:462px;z-index:1}}
.portret img{{width:100%;height:100%;object-fit:cover;object-position:52% 10%;opacity:.94}}
.portret::after{{content:"";position:absolute;inset:0;background:
 linear-gradient(90deg,#0E0C11 0%,rgba(14,12,17,.95) 24%,rgba(14,12,17,.48) 60%,rgba(14,12,17,.18) 100%),
 linear-gradient(180deg,rgba(14,12,17,.32) 0%,rgba(14,12,17,0) 32%,rgba(14,12,17,.5) 100%)}}
.ramka{{position:absolute;inset:22px;border:1px solid rgba(201,162,39,.3);border-radius:14px;z-index:1}}
.ugol{{position:absolute;width:34px;height:34px;border:2px solid #C9A227;z-index:3;opacity:.85}}
.u1{{left:22px;top:22px;border-right:0;border-bottom:0;border-radius:14px 0 0 0}}
.u2{{right:22px;bottom:22px;border-left:0;border-top:0;border-radius:0 0 14px 0}}
</style>
<div class="fon"><img src="{img}"></div>{portret_html}<div class="svet"></div>
<div class="ramka"></div><div class="ugol u1"></div><div class="ugol u2"></div>
<div class="in">
<div class="znak">{ZNAK}<span>Школа Ирины Волковой</span></div>
<div class="serdce">
<div class="metka">{metka}</div>
<h1>{zag}</h1>
<p>{pod}</p>
<div class="puli">{puli}</div>
</div>
<div class="niz"><b>Таро · Магия · Обереги</b> &nbsp;·&nbsp; thebodymindcode.github.io/ira-shkola</div>
</div>"""


async def main():
    articles = json.load(open('content/articles.json', encoding='utf-8'))
    zadachi = [
      ('glavnaya', 'Школа магии и таро', 'Таро, ритуальная магия, руны и домашние обереги. Обучение у Ирины Волковой.',
       'images/obrazy/k-gekata.jpg', 'Школа',
       [('karta', '22 аркана'), ('runa', '24 руны'), ('dom', '7 оберегов')],
       'images/obrazy/p-glavnaya.jpg'),
      ('shkola', 'Как здесь учат', 'Закрытые каналы, задание после каждой темы, разбор работ вслух.',
       'images/obrazy/k-besy.jpg', 'Обучение',
       [('kniga', 'Источник у темы'), ('ruka', 'Задание руками'), ('glaz', 'Разбор вслух')],
       'images/obrazy/p-shkola.jpg'),
      ('kursy', 'Курсы школы', 'Шесть направлений: таро, Чёрный Гримуар, руны, бесы, обереги дома и личная работа.',
       'images/obrazy/h-kursy.jpg', 'Курсы',
       [('karta', 'Таро и арканы'), ('ogon', 'Ритуальная магия'), ('runa', 'Северные знаки')],
       'images/obrazy/p-taro.jpg'),
      ('grimuar', 'Чёрный Гримуар', 'Живой курс по колоде Некрономикон: девять ступеней от инструментов до ритуальной работы.',
       'images/obrazy/k-grimuar.jpg', 'Курс',
       [('kniga', '9 ступеней'), ('glaz', 'Диагностика'), ('chas', 'Дважды в неделю')],
       'images/obrazy/p-irina2.jpg'),
      ('gekata', 'Геката: ритуальная магия', 'Четыре ступени работы с богиней перекрёстков, ключей и факелов.',
       'images/obrazy/k-gekata.jpg', 'Курс',
       [('perekryostok', 'Перекрёсток'), ('svecha', 'Обряд и свеча'), ('krug', '4 ступени')],
       'images/obrazy/p-irina1.jpg'),
      ('runy', 'Руны: старший футарк', 'Двадцать четыре знака, рунические поэмы, работа с поставом.',
       'images/obrazy/k-runy.jpg', 'Курс',
       [('runa', '24 знака'), ('kniga', 'Рунические поэмы'), ('nit', 'Работа с поставом')],
       'images/obrazy/p-irina2.jpg'),
      ('besy', 'Славянская демонология', 'Кого зовут, о чём просят и чем расплачиваются. Два ритуала призыва и четыре заговора.',
       'images/obrazy/k-besy.jpg', 'Курс',
       [('ogon', '2 ритуала'), ('nit', '4 заговора'), ('chas', '66 минут')],
       'images/obrazy/p-irina1.jpg'),
      ('nastavnichestvo', 'Личная работа', 'Разбор своей практики один на один с Ириной Волковой.',
       'images/obrazy/k-nastav.jpg', 'Наставничество',
       [('ruka', 'Один на один'), ('glaz', 'Свои случаи'), ('krug', 'Своя система')],
       'images/obrazy/p-irina1.jpg'),
      ('taro', 'Обучение таро', 'Вопрос, расклад, чтение связок и разговор с человеком.',
       'images/obrazy/k-taro.jpg', 'Направление',
       [('karta', '78 карт'), ('glaz', 'Чтение связок'), ('ruka', 'Разбор раскладов')],
       'images/obrazy/p-taro.jpg'),
      ('karty', 'Значения старших арканов', 'Двадцать два аркана: образ, прямое и перевёрнутое значение, совет чтецу.',
       'images/obrazy/k-taro.jpg', 'Справочник',
       [('karta', '22 аркана'), ('zerkalo', 'Прямое и перевёрнутое'), ('kniga', 'Колода Уэйта')],
       'images/obrazy/p-taro.jpg'),
      ('luna', 'Лунный круг', 'Восемь фаз и работа в каждой. Потоки школы идут по этому же кругу.',
       'images/obrazy/h-nechist.jpg', 'Как считают время',
       [('luna', '8 фаз'), ('krug', '29,5 суток'), ('chas', 'Набор на молодую')],
       'images/obrazy/p-irina2.jpg'),
      ('kviz', 'Какой аркан ведёт вас', 'Шесть вопросов, и колода назовёт карту, с которой у вас общий язык.',
       'images/obrazy/k-taro.jpg', 'Вопросник',
       [('karta', '6 вопросов'), ('zerkalo', 'Ваш аркан'), ('strela', 'Минута времени')],
       'images/obrazy/p-taro.jpg'),
      ('zhurnal', 'Ведьмин дневник', 'Двадцать семь разборов про домашние обереги и нечистую силу.',
       'images/obrazy/k-grimuar.jpg', 'Дневник',
       [('dom', '7 оберегов'), ('les', '20 существ'), ('kniga', 'По источникам')],
       'images/obrazy/p-shkola.jpg'),
      ('oberegi', 'Обереги славянского дома', 'Нож на ночь, красный угол, крапива у порога, громничная свеча.',
       'images/obrazy/h-oberegi.jpg', 'Раздел',
       [('dom', 'Порог и окна'), ('svecha', 'Громничная свеча'), ('podkova', 'Красный угол')],
       'images/obrazy/p-irina1.jpg'),
      ('nechist', 'Нечистая сила деревни', 'Домовой, леший, банник, полудница, мара. Двадцать разборов.',
       'images/obrazy/h-nechist.jpg', 'Раздел',
       [('les', 'Лес и вода'), ('dom', 'Двор и баня'), ('chas', 'Свои часы')],
       'images/obrazy/p-irina2.jpg'),
      ('slovar', 'Словарь школы', 'Слова, которые встречаются на занятиях и в разборах, простым языком.',
       'images/obrazy/k-grimuar.jpg', 'Справочник',
       [('kniga', 'Термины'), ('glaz', 'Без тумана'), ('nit', 'Со ссылками')],
       'images/obrazy/p-shkola.jpg'),
      ('irina', 'Ирина Волкова', 'Первая колода в одиннадцать лет, практика с двадцати трёх, курсы с 2014 года.',
       'images/obrazy/k-nastav.jpg', 'Кто ведёт',
       [('svecha', 'С 2014 года'), ('kniga', 'Психология и гипноз'), ('luna', 'Работа по луне')],
       'images/obrazy/p-irina1.jpg'),
      ('vopros', 'Вопросы о школе', 'С чего начать, нужен ли дар, как идут потоки и чем занимается школа.',
       'images/obrazy/h-vopros.jpg', 'Вопросы',
       [('glaz', 'Нужен ли дар'), ('strela', 'С чего начать'), ('chas', 'Как идут потоки')],
       'images/obrazy/p-shkola.jpg'),
      ('kontakty', 'Как связаться', 'Телеграм-канал школы и Instagram Ирины Волковой.',
       'images/obrazy/h-vopros.jpg', 'Связь',
       [('tg', 'Канал школы'), ('ig', 'Instagram'), ('ruka', 'Ответ лично')],
       'images/obrazy/p-irina1.jpg'),
    ]
    for a in articles:
        oberegi = a['kind'] == 'oberegi'
        zadachi.append((f'st-{a["slug"]}', a['name'], a['anons'],
                        f'images/zhurnal/{a["slug"]}.jpg',
                        'Обереги дома' if oberegi else 'Нечисть',
                        [('dom', 'Домашняя защита'), ('kniga', 'По записям собирателей'), ('ruka', 'Как делали')]
                        if oberegi else
                        [('les', 'Где живёт'), ('chas', 'Когда встречали'), ('podkova', 'Как обходились')]))
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        ctx = await br.new_context(viewport={'width': 1200, 'height': 630}, device_scale_factor=1)
        pg = await ctx.new_page()
        for zad in zadachi:
            name, zag, pod, img, metka, bullety = zad[:6]
            portret = b64(zad[6]) if len(zad) > 6 else ''
            await pg.set_content(shablon(zag, pod, b64(img), metka, bullety, portret))
            await pg.wait_for_timeout(700)
            await pg.screenshot(path=f'images/og/{name}.jpg', type='jpeg', quality=86)
        await ctx.close(); await br.close()
    print('og-карточек:', len(zadachi))

asyncio.run(main())
