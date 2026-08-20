# -*- coding: utf-8 -*-
import sys, os, json, html
sys.path.insert(0, os.path.dirname(__file__))
from engine import ico, typo, TG, DOMAIN
from layout import page, u
from pages_main import hero, KNOPKI_TG
from pages_kursy import finalny

T = typo
HOME = ('Главная', '')

RAZDEL = {'oberegi': ('Обереги дома', 'oberegi/'), 'nechist': ('Нечисть', 'nechist/')}


def kadr(a, metka=True):
    m = f'<span class="metka">{RAZDEL[a["kind"]][0]}</span>' if metka else ''
    return f"""<a class="kadr" href="{u('zhurnal/' + a['slug'] + '/')}">
<div class="ph"><img src="{u('images/zhurnal/' + a['slug'] + '.jpg')}" alt="{a['name']}" loading="lazy"></div>
<div class="body">{m}<h3>{a['name']}</h3><p>{T(a['deck'][:110])}</p></div></a>"""


def statya(a, sosedi):
    razdel_name, razdel_path = RAZDEL[a['kind']]
    secs = ''
    for i, s in enumerate(a['sections']):
        ps = ''.join(f'<p>{T(html.escape(p))}</p>' for p in s['p'])
        secs += f'<h2>{T(html.escape(s["h"]))}</h2>{ps}'
        if i == 1 and a['deck']:
            secs += f'<div class="vrez">{T(html.escape(a["deck"]))}</div>'
    dalshe = ''.join(kadr(x, metka=False) for x in sosedi[:3])
    kurs = ('kursy/besy/', 'Курс по славянской демонологии') if a['kind'] == 'nechist' \
        else ('oberegi/', 'Все обереги дома')
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "Article",
        "headline": a['name'], "description": a['deck'][:180],
        "image": f"{DOMAIN}/images/zhurnal/{a['slug']}.jpg",
        "author": {"@type": "Person", "name": "Ирина Волкова"},
        "publisher": {"@type": "Organization", "name": "Школа Ирины Волковой"},
        "mainEntityOfPage": f"{DOMAIN}/zhurnal/{a['slug']}/",
    }, ensure_ascii=False)
    body = f"""
<section style="padding-top:34px"><div class="wrap uzko">
<p class="eyebrow">{razdel_name}</p>
<h1>{T(html.escape(a['name']))}</h1>
<p class="lid">{T(html.escape(a['deck']))}</p>
</div>
<div class="wrap" style="margin-top:30px">
<div class="kadr"><div class="ph"><img src="{u('images/zhurnal/' + a['slug'] + '.jpg')}"
 alt="{html.escape(a['name'])}"></div></div>
</div>
<div class="wrap"><div class="art" style="margin-top:34px">
<p class="lid">{T(html.escape(a['lead']))}</p>
{secs}
</div></div></section>

<section><div class="wrap">
<p class="eyebrow">Дальше</p>
<h2>Читать по этой теме</h2>
<div class="grid3">{dalshe}</div>
<div class="plashki" style="margin-top:24px">
<a class="plashka" href="{u(kurs[0])}">{ico('strela')} {kurs[1]}</a>
<a class="plashka" href="{u('zhurnal/')}">{ico('kniga')} Весь журнал</a>
</div>
</div></section>

{finalny('Разборы выходят в канале',
         'Новые разборы про обереги и нечистую силу Ирина выкладывает в телеграм-канале школы. '
         'Там же выходят объявления о наборах на курсы.')}
"""
    page(f'zhurnal/{a["slug"]}/', f'{a["name"]}: {a["deck"][:70].rstrip(",. ")}',
         a['deck'][:180], body, active='zhurnal/',
         og=f'images/zhurnal/{a["slug"]}.jpg',
         crumbs=[HOME, ('Журнал', 'zhurnal/'), (razdel_name, razdel_path), (a['name'], None)],
         schema=f'<script type="application/ld+json">{schema}</script>')


def zhurnal(articles):
    ob = [a for a in articles if a['kind'] == 'oberegi']
    ne = [a for a in articles if a['kind'] == 'nechist']
    body = f"""
{hero('images/obrazy/zhurnal.jpg', 'Журнал', 'Разборы Ирины Волковой',
      'Двадцать семь разборов о домашних оберегах и о нечистой силе славянской деревни. '
      'Всё собрано по записям этнографов и деревенским быличкам.', KNOPKI_TG)}

<section><div class="wrap">
<p class="eyebrow">Два раздела</p>
<h2>Куда смотреть</h2>
<div class="grid2">
<a class="kadr" href="{u('oberegi/')}">
<div class="ph"><img src="{u('images/obrazy/oberegi.jpg')}" alt="Обереги дома" loading="lazy"></div>
<div class="body"><h3>Обереги дома</h3><p>{T('Семь разборов: соль, нож, красный угол, крапива '
 'у порога, громничная свеча, отливка воском, оберег в люльку.')}</p></div></a>
<a class="kadr" href="{u('nechist/')}">
<div class="ph"><img src="{u('images/obrazy/nechist.jpg')}" alt="Нечисть" loading="lazy"></div>
<div class="body"><h3>Нечисть</h3><p>{T('Двадцать разборов: домовой, леший, водяной, банник, '
 'полудница, мара, упырь и другие жители народной веры.')}</p></div></a>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Обереги дома</p>
<h2>Домашняя защита деревни</h2>
<div class="grid3">{''.join(kadr(a, metka=False) for a in ob)}</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Нечисть</p>
<h2>Кто жил рядом с человеком</h2>
<div class="grid3">{''.join(kadr(a, metka=False) for a in ne)}</div>
</div></section>

{finalny('Новые разборы выходят в канале',
         'Ирина выкладывает разборы в телеграм-канале школы. Там же объявляются наборы на курсы.')}
"""
    page('zhurnal/', 'Журнал: разборы про обереги и нечистую силу',
         'Двадцать семь разборов Ирины Волковой о домашних оберегах и нечистой силе славянской '
         'деревни, собранных по источникам.', body, active='zhurnal/',
         og='images/obrazy/zhurnal.jpg', crumbs=[HOME, ('Журнал', None)])


def razdel(kind, articles):
    arts = [a for a in articles if a['kind'] == kind]
    if kind == 'oberegi':
        title, h1 = 'Обереги дома', 'Обереги славянского дома'
        eyebrow, img = 'Раздел журнала', 'oberegi'
        lid = ('Соль, нож, красный угол, крапива у порога, громничная свеча. Семь разборов '
               'о том, чем деревня держала дом и откуда эти правила взялись.')
        vvod = [
            'Домашний оберег в деревне был работой с границей: где вход, '
            'где порог, где угол, где окно. У каждой границы находился свой предмет и своё правило, '
            'и правило это знали все, от хозяйки до ребёнка.',
            'Логика везде одна. Опасность приходит снаружи и заходит через щель, поэтому щель '
            'закрывают: солью, ножом, крапивой, огнём освящённой свечи, красным углом с рушником. '
            'Отсюда и запреты, которые сегодня выглядят суеверием, а на деле были частью порядка.',
            'В разборах ниже собрано, что именно делали, в какие дни и почему. Источники называются '
            'прямо в тексте, догадки от записанного отделены.',
        ]
        kurs = ('kursy/besy/', 'Курс по славянской демонологии')
    else:
        title, h1 = 'Нечисть', 'Нечистая сила славянской деревни'
        eyebrow, img = 'Раздел журнала', 'nechist'
        lid = ('Домовой, леший, водяной, банник, полудница, мара, упырь. Двадцать разборов '
               'о тех, кого деревня считала соседями по двору, лесу и воде.')
        vvod = [
            'В народной вере нечисть не была одной серой массой. У каждого существа своё место, '
            'свой час и свои правила: домовой держится печи, банник приходит в четвёртый пар, '
            'полудница выходит в полдень над полем, водяной сидит в омуте.',
            'Отсюда и разные обереги. Против того, кто живёт в доме, работает угощение и поклон. '
            'Против того, кто пришёл с погоста, работает счёт зёрен и осина. Одинаковых средств '
            'не было, потому что и беды считались разными.',
            'В разборах собрано, кто есть кто, по каким приметам его узнавали и как с ним '
            'обходились. Всё, что записано у собирателей, отделено от позднейших выдумок.',
        ]
        kurs = ('kursy/besy/', 'Курс по славянской демонологии')

    body = f"""
{hero(f'images/obrazy/{img}.jpg', eyebrow, h1, lid, KNOPKI_TG)}

<section><div class="wrap">
<p class="eyebrow">О разделе</p>
<h2>Как это устроено</h2>
<div class="tside"><div class="col">
{''.join(f'<p>{T(p)}</p>' for p in vvod)}
<div class="plashki"><a class="plashka" href="{u(kurs[0])}">{ico('strela')} {kurs[1]}</a></div>
</div>
<aside class="side"><div class="cifra">{len(arts)}</div>
<p>{T('разборов в этом разделе, каждый с источниками и без страшилок.')}</p></aside></div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Разборы</p>
<h2>{'Чем держали дом' if kind == 'oberegi' else 'Кто есть кто'}</h2>
<div class="grid3">{''.join(kadr(a, metka=False) for a in arts)}</div>
</div></section>

{finalny('Новые разборы в канале',
         'Ирина выкладывает разборы в телеграм-канале школы, там же объявляются наборы на курсы.')}
"""
    page(f'{kind}/' if kind == 'oberegi' else 'nechist/',
         title + ': разборы по источникам', lid[:180], body, active='zhurnal/',
         og=f'images/obrazy/{img}.jpg', crumbs=[HOME, ('Журнал', 'zhurnal/'), (title, None)])
