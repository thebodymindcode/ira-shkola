# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'content'))
from engine import ico, typo, TG
from layout import page, u
from pages_main import hero, KNOPKI_TG
from pages_kursy import finalny
from karta_svg import karta
from arkany import ARKANY

T = typo
HOME = ('Главная', '')

VOPROSY = [
    ('С чем вы чаще приходите к картам?',
     [('Хочется понять, что происходит вокруг', 'luna'),
      ('Нужно принять решение', 'vlyublyonnye'),
      ('Хочется начать что-то новое', 'durak'),
      ('Нужно навести порядок в своей жизни', 'imperator')]),
    ('Что даётся вам труднее всего?',
     [('Ждать, когда ничего не понятно', 'zhritsa'),
      ('Отпускать то, что закончилось', 'smert'),
      ('Держать себя в руках', 'sila'),
      ('Идти, когда не видно дороги', 'otshelnik')]),
    ('Как вы обычно принимаете решения?',
     [('Долго думаю и взвешиваю', 'spravedlivost'),
      ('Слушаю, что откликается внутри', 'zhritsa'),
      ('Делаю и разбираюсь по ходу', 'kolesnica'),
      ('Жду знака или случая', 'koleso')]),
    ('Что вам ближе в работе с собой?',
     [('Разобрать причину до конца', 'otshelnik'),
      ('Собрать силы и сделать рывок', 'kolesnica'),
      ('Найти меру и не спешить', 'umerennost'),
      ('Освободиться от того, что держит', 'dyavol')]),
    ('Чего вы ждёте от обучения?',
     [('Ясности и понимания', 'solnce'),
      ('Порядка и системы', 'imperator'),
      ('Опоры и веры в себя', 'zvezda'),
      ('Завершить начатое когда-то', 'mir')]),
    ('Что для вас магия?',
     [('Ремесло, которому учатся', 'mag'),
      ('Традиция, которую передают', 'ierofant'),
      ('Внутренняя работа', 'zhritsa'),
      ('Дорога, у которой нет конца', 'durak')]),
]

# Углы веера: шесть карт от левого края к правому, шаг 10.8 градуса.
UGLY = [-27, -16.2, -5.4, 5.4, 16.2, 27]


def _reshetka():
    """Ромбовидная сетка на рубашке. Центр оставлен пустым под знак луны."""
    kusochki = []
    for r in range(10):
        y = 32 + r * 22
        for c in range(9):
            x = 22 + c * 20 + (10 if r % 2 else 0)
            if x > 162 or y > 240:
                continue
            if abs(x - 92) < 52 and abs(y - 134) < 52:
                continue
            kusochki.append(f'M{x} {y - 6}l6 6-6 6-6-6z')
    return '<path d="' + ''.join(kusochki) + '"/>'


def rubashka():
    """Рубашка карты: рисуется один раз, дальше карты веера берут её через use."""
    return f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
<symbol id="rubashka" viewBox="0 0 184 268">
<rect x="1" y="1" width="182" height="266" rx="14" fill="#151120" stroke="#C9A227" stroke-width="1.3"/>
<rect x="9" y="9" width="166" height="250" rx="9" fill="none" stroke="#C9A227"
 stroke-width=".8" opacity=".42"/>
<g fill="none" stroke="#C9A227" stroke-width=".8" opacity=".34">{_reshetka()}</g>
<circle cx="92" cy="134" r="40" fill="#100D17"/>
<circle cx="92" cy="134" r="40" fill="none" stroke="#C9A227" stroke-width="1" opacity=".7"/>
<circle cx="92" cy="134" r="33" fill="none" stroke="#C9A227" stroke-width=".7" opacity=".35"/>
<path d="M104 114a24 24 0 1 0 0 40 19 19 0 0 1 0-40Z" fill="#E3C15B" opacity=".9"/>
<path d="M92 24l3.4 9.2 9.2 3.4-9.2 3.4L92 49.2 88.6 40l-9.2-3.4 9.2-3.4Z" fill="#C9A227" opacity=".8"/>
<path d="M92 219l3.4 9.2 9.2 3.4-9.2 3.4-3.4 9.2-3.4-9.2-9.2-3.4 9.2-3.4Z" fill="#C9A227" opacity=".8"/>
</symbol></svg>'''


def kviz():
    dannye = json.dumps({
        'voprosy': [{'q': q, 'o': [{'t': t, 's': sl} for t, sl in oo]} for q, oo in VOPROSY],
        'karty': {a['slug']: {'name': a['name'], 'n': a['n'],
                              'smysl': a['smysl'], 'pryamo': a['pryamo'][:3]}
                  for a in ARKANY},
    }, ensure_ascii=False)
    kartinki = ''.join(f'<template data-slug="{a["slug"]}">{karta(a["slug"], a["n"], a["name"])}</template>'
                       for a in ARKANY)
    luny = ''.join('<i></i>' for _ in VOPROSY)
    veer = ''.join(
        f'<div class="veer-k" style="--rot:{a}deg">'
        f'<div class="veer-in">'
        f'<div class="veer-storona veer-bok">'
        f'<svg viewBox="0 0 184 268" aria-hidden="true"><use href="#rubashka"/></svg></div>'
        f'<div class="veer-storona veer-lico"></div>'
        f'</div></div>' for a in UGLY)

    body = f"""
{hero('images/obrazy/h-vopros.jpg', 'Короткий вопросник', 'Какой аркан ведёт вас сейчас',
      'Шесть вопросов о том, как вы решаете и чего ждёте. В ответе будет старший аркан, '
      'который отвечает за этот отрезок дороги, и его разбор.')}

<section><div class="wrap">
{rubashka()}
<div id="kviz" class="kviz" data-kviz='{dannye}' data-karty="{u('karty/')}">
<div class="kviz-telo">
<div class="kviz-levo">
<div class="kviz-shag"><span class="kviz-nomer">Вопрос 1 из {len(VOPROSY)}</span>
<div class="kviz-luny" aria-hidden="true">{luny}</div></div>
<h2 class="kviz-vopros">Загрузка</h2>
<div class="kviz-otvety"></div>
<p class="kviz-snoska">{T('Карта открывается на каждом ответе. Ни один ответ не уходит дальше '
                          'вашего браузера.')}</p>
</div>
<div class="kviz-veer" aria-hidden="true">{veer}</div>
</div>
<div class="kviz-itog" hidden></div>
</div>
{kartinki}
</div></section>

<section><div class="wrap">
<p class="eyebrow">Что дальше</p>
<h2>Аркан это не приговор</h2>
<div class="tside"><div class="col">
<p>{T('Вопросник показывает, какая карта описывает нынешний отрезок дороги. Он не предсказывает '
      'события и не решает за человека: старшие арканы говорят о состоянии, а не о судьбе.')}</p>
<p>{T('На потоке по таро этому учат подробно: как ставить вопрос, чтобы колода могла ответить, '
      'и как читать связку карт, а не одну картинку.')}</p>
</div>
<aside class="side"><h4>Хотите глубже</h4>
<p>{T('В справочнике собраны все двадцать два аркана с прямым и перевёрнутым значением.')}</p>
<div class="plashki" style="margin-top:14px">
<a class="plashka" href="{u('karty/')}">{ico('karta')} Значения карт</a></div>
</aside></div>
</div></section>

{finalny('Научиться читать самому',
         'Ответ вопросника это одна карта. На потоке учат складывать их в расклад и понимать, '
         'что говорит вся картина целиком.',
         vtoraya=('taro/', 'Курс по таро'), knopka='Спросить про набор',
         side=('22 аркана', 'Столько старших карт в колоде, и каждая отвечает за свой отрезок.'))}
"""
    page('kviz/', 'Какой аркан ведёт вас сейчас: короткий вопросник',
         'Шесть вопросов и старший аркан таро, который описывает нынешний отрезок дороги. '
         'С разбором значения карты.',
         body, active='', og='images/og/vopros.jpg', crumbs=[HOME, ('Вопросник', None)])
