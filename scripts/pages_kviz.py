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


def kviz():
    po_slug = {a['slug']: a for a in ARKANY}
    dannye = json.dumps({
        'voprosy': [{'q': q, 'o': [{'t': t, 's': sl} for t, sl in oo]} for q, oo in VOPROSY],
        'karty': {a['slug']: {'name': a['name'], 'n': a['n'],
                              'smysl': a['smysl'], 'pryamo': a['pryamo'][:3]}
                  for a in ARKANY},
    }, ensure_ascii=False)
    kartinki = ''.join(f'<template data-slug="{a["slug"]}">{karta(a["slug"], a["n"], a["name"])}</template>'
                       for a in ARKANY)
    body = f"""
{hero('images/obrazy/h-vopros.jpg', 'Короткий вопросник', 'Какой аркан ведёт вас сейчас',
      'Шесть вопросов о том, как вы решаете и чего ждёте. В ответе будет старший аркан, '
      'который отвечает за этот отрезок дороги, и его разбор.')}

<section><div class="wrap uzko">
<div id="kviz" class="kviz" data-kviz='{dannye}'>
<div class="kviz-shag"><span class="kviz-nomer">Вопрос 1 из {len(VOPROSY)}</span>
<div class="kviz-polosa"><i style="width:0%"></i></div></div>
<h2 class="kviz-vopros">Загрузка</h2>
<div class="kviz-otvety"></div>
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
