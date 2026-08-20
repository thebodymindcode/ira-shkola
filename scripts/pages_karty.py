# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'content'))
from engine import ico, typo, TG, DOMAIN
from layout import page, u
from pages_main import hero, KNOPKI_TG
from pages_kursy import finalny
from karta_svg import karta
from arkany import ARKANY
import json

T = typo
HOME = ('Главная', '')
KR = [HOME, ('Значения карт', 'karty/')]


def spisok(punkty, ikonka):
    return '<div class="dlist"><ul>' + ''.join(
        f'<li>{ico(ikonka)}<span>{T(p)}</span></li>' for p in punkty) + '</ul></div>'


def hab():
    kletki = ''.join(f"""<a class="ark-k" href="{u('karty/' + a['slug'] + '/')}">
{karta(a['slug'], a['n'], a['name'])}</a>""" for a in ARKANY)
    body = f"""
{hero('images/obrazy/h-taro.jpg', 'Справочник', 'Значения старших арканов',
      'Двадцать два аркана: образ, прямое и перевёрнутое значение, на что смотреть '
      'в раскладе. Собрано по классической традиции Уэйта.', KNOPKI_TG)}

<section><div class="wrap">
<p class="eyebrow">Двадцать два</p>
<h2>Старшие арканы по порядку</h2>
<p class="lid">{T('Счёт идёт от Шута, у которого номер ноль, до Мира. Порядок не случайный: '
                  'это дорога, на которой каждая карта отвечает за свой отрезок.')}</p>
<div class="ark-grid">{kletki}</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Как устроен путь</p>
<h2>Три ряда по семь</h2>
{shemy.put_duraka()}
</div></section>

{finalny('Научиться читать колоду',
         'Значения это только словарь. Читать расклад учат на потоке: как ставить вопрос, '
         'как связывать карты между собой и когда сказать, что ответа нет.',
         vtoraya=('taro/', 'Курс по таро'), knopka='Спросить про набор',
         side=('78 карт', 'Двадцать два старших аркана и пятьдесят шесть младших.'))}
"""
    page('karty/', 'Значения карт таро: 22 старших аркана',
         'Справочник старших арканов: образ карты, прямое и перевёрнутое значение, '
         'на что смотреть в раскладе. По классической традиции Уэйта.',
         body, active='karty/', og='images/og/taro.jpg', crumbs=[HOME, ('Значения карт', None)])


def stranica(a, prev_a, next_a):
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "Article",
        "headline": f"{a['name']}: значение карты таро",
        "description": f"{a['name']} в таро: {', '.join(a['pryamo'][:3])}.",
        "author": {"@type": "Person", "name": "Ирина Волкова"},
        "publisher": {"@type": "Organization", "name": "Школа Ирины Волковой"},
        "mainEntityOfPage": f"{DOMAIN}/karty/{a['slug']}/",
    }, ensure_ascii=False)
    sosedi = ''
    if prev_a:
        sosedi += (f'<a href="{u("karty/" + prev_a["slug"] + "/")}"><span>Предыдущий аркан</span>'
                   f'<b>{prev_a["name"]}</b></a>')
    if next_a:
        sosedi += (f'<a href="{u("karty/" + next_a["slug"] + "/")}"><span>Следующий аркан</span>'
                   f'<b>{next_a["name"]}</b></a>')
    body = f"""
<section style="padding-top:34px"><div class="wrap">
<div class="ark-verh">
<div class="ark-foto">{karta(a['slug'], a['n'], a['name'])}</div>
<div class="ark-txt">
<p class="eyebrow">Старший аркан {a['n']}</p>
<h1>{T(a['name'])}</h1>
<p class="podzag">{T(a['lat'])} · {T(a['stihiya'])}</p>
<p class="lid">{T(a['obraz'])}</p>
</div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Прямое положение</p>
<h2>Что говорит карта</h2>
{spisok(a['pryamo'], 'karta')}
</div></section>

<section><div class="wrap">
<p class="eyebrow">Перевёрнутое положение</p>
<h2>Как меняется смысл</h2>
{spisok(a['perev'], 'zerkalo')}
</div></section>

<section><div class="wrap">
<p class="eyebrow">Суть</p>
<h2>О чём эта карта на самом деле</h2>
<div class="tside"><div class="col">
<p>{T(a['smysl'])}</p>
<p>{T(a['sovet'])}</p>
</div>
<aside class="side"><h4>В раскладе</h4>
<p>{T('Значение карты меняют соседи. Один и тот же аркан в разных местах расклада '
      'говорит разное, и этому учат отдельно.')}</p>
<div class="plashki" style="margin-top:14px">
<a class="plashka" href="{u('taro/')}">{ico('strela')} Курс по таро</a></div>
</aside></div>
<div class="sosedi">{sosedi}</div>
</div></section>

{finalny('Читать колоду целиком',
         'Словарь значений это начало. Дальше идёт связка карт между собой, постановка '
         'вопроса и разговор с человеком, которому вы читаете.',
         vtoraya=('karty/', 'Все двадцать два аркана'), knopka='Написать Ирине',
         side=(f'Аркан {a["n"]}', f'{a["lat"]}, стихия и планета: {a["stihiya"]}.'))}
"""
    page(f'karty/{a["slug"]}/', f'{a["name"]}: значение карты таро',
         f'{a["name"]} в таро: {", ".join(a["pryamo"][:3])}. Перевёрнутое положение, '
         f'образ карты и на что смотреть в раскладе.',
         body, active='karty/', og='images/og/taro.jpg',
         crumbs=KR + [(a['name'], None)],
         schema=f'<script type="application/ld+json">{schema}</script>')


import shemy
