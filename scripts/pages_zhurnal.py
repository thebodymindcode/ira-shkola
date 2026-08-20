# -*- coding: utf-8 -*-
import sys, os, json, html, re
sys.path.insert(0, os.path.dirname(__file__))
from engine import ico, typo, TG, DOMAIN
from layout import page, u
from pages_main import hero, KNOPKI_TG
from pages_kursy import finalny

T = typo
HOME = ('Главная', '')

RAZDEL = {'oberegi': ('Обереги дома', 'oberegi/'), 'nechist': ('Нечисть', 'nechist/')}


def zov(icon, zag, txt, href, podpis):
    return (f'<a class="zov" href="{u(href)}">{ico(icon, "ic big")}<h3>{T(zag)}</h3>'
            f'<p>{T(txt)}</p><span class="more">{podpis} {ico("strela")}</span></a>')


def dobit(cards_html, n, dobavki):
    """Добивает сетку до кратности трём карточками-приглашениями."""
    nado = (-n) % 3
    return cards_html + ''.join(dobavki[:nado])


DOBAVKI = {
 'oberegi': [
  zov('ogon', 'Разобрать это на курсе',
      'Обереги в потоке разбирают подробнее: откуда пришли, против чего ставились, что изменилось за век.',
      'kursy/besy/', 'Курс по демонологии'),
  zov('kniga', 'Как здесь учат',
      'Закрытый канал, задание после каждой темы и разбор работы вслух.',
      'shkola/', 'Устройство обучения'),
 ],
 'nechist': [
  zov('ogon', 'Пройти это курсом',
      'В потоке по демонологии существ разбирают по одному: имя, место, приметы, обереги и источник записи.',
      'kursy/besy/', 'Смотреть курс'),
  zov('dom', 'Обереги дома',
      'Вторая половина журнала: чем деревня закрывала порог, окно и красный угол.',
      'oberegi/', 'Читать разборы'),
 ],
}


def kadr(a, metka=True):
    m = f'<span class="metka">{RAZDEL[a["kind"]][0]}</span>' if metka else ''
    return f"""<a class="kadr" href="{u('zhurnal/' + a['url'] + '/')}">
<div class="ph"><img src="{u('images/zhurnal/' + a['slug'] + '.jpg')}" alt="{a['name']}" loading="lazy"></div>
<div class="body">{m}<h3>{a['name']}</h3><p>{T(a['anons'])}</p></div></a>"""


def statya(a, sosedi, sosed_prev, sosed_next):
    razdel_name, razdel_path = RAZDEL[a['kind']]
    # врезка: живая присказка в кавычках, если она в статье есть
    vrez, vrez_posle = '', -1
    for i, sec in enumerate(a['sections']):
        for p in sec['p']:
            m = re.search(r'«([^»]{18,150})»', p)
            if m and not vrez:
                vrez, vrez_posle = m.group(1).strip(), i
    secs, toc = '', []
    for i, sec in enumerate(a['sections']):
        aid = f'r{i + 1}'
        toc.append(f'<li><a href="#{aid}">{html.escape(sec["h"])}</a></li>')
        ps = ''.join(f'<p>{T(html.escape(p))}</p>' for p in sec['p'])
        secs += f'<h2 id="{aid}">{T(html.escape(sec["h"]))}</h2>{ps}'
        if i == vrez_posle and vrez:
            secs += f'<div class="vrez">{T(html.escape(vrez))}</div>'
    # «Коротко»: заголовки разделов, то есть карта статьи, ничего не выдумано
    korotko = ''.join(f'<li>{T(html.escape(x["h"]))}</li>' for x in a['sections'])
    dalshe = ''.join(kadr(x, metka=False) for x in sosedi[:3])
    kurs = ('kursy/besy/', 'Курс по славянской демонологии') if a['kind'] == 'nechist' \
        else ('oberegi/', 'Все обереги дома')
    sosedi_bl = ''
    if sosed_prev:
        sosedi_bl += (f'<a href="{u("zhurnal/" + sosed_prev["url"] + "/")}">'
                      f'<span>Предыдущий разбор</span><b>{sosed_prev["name"]}</b></a>')
    if sosed_next:
        sosedi_bl += (f'<a href="{u("zhurnal/" + sosed_next["url"] + "/")}">'
                      f'<span>Следующий разбор</span><b>{sosed_next["name"]}</b></a>')
    istochnik = ('Разбор собран по записям этнографов и деревенским быличкам. Народные приметы '
                 'приводятся так, как они записаны собирателями, без позднейших дополнений.')
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "Article",
        "headline": a['name'], "description": a['deck'][:180],
        "image": f"{DOMAIN}/images/zhurnal/{a['slug']}.jpg",
        "author": {"@type": "Person", "name": "Ирина Волкова"},
        "publisher": {"@type": "Organization", "name": "Школа Ирины Волковой"},
        "mainEntityOfPage": f"{DOMAIN}/zhurnal/{a['url']}/",
    }, ensure_ascii=False)
    body = f"""
<section style="padding-top:34px"><div class="wrap uzko">
<p class="eyebrow">{razdel_name}</p>
<h1>{T(html.escape(a['name']))}</h1>
<p class="podzag">{T(html.escape(a['anons']))}</p>
</div>
<div class="wrap" style="margin-top:26px">
<div class="kadr art-kadr"><div class="ph"><img src="{u('images/zhurnal/' + a['slug'] + '.jpg')}"
 alt="{html.escape(a['name'])}"></div></div>
</div>
<div class="wrap"><div class="art" style="margin-top:30px">
<p class="lead drop">{T(html.escape(a['lead']))}</p>
<div class="byline"><b>Ирина Волкова</b><span class="dot"></span>
<span class="tag">{razdel_name}</span><span class="dot"></span>
<span>{len(a['sections'])} раздела</span></div>
<div class="korotko"><b>Коротко</b><ul>{korotko}</ul></div>
<details class="toc"><summary>Что внутри разбора</summary><ol>{''.join(toc)}</ol></details>
{secs}
<div class="istok"><b>Откуда это известно</b><p>{T(istochnik)}</p></div>
<div class="sosedi">{sosedi_bl}</div>
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

{finalny('Читать дальше в канале',
         'Каждый новый разбор Ирина сначала выкладывает в телеграм-канал школы.',
         vtoraya=('kursy/besy/', 'Курс по демонологии'), knopka='Открыть канал',
         side=('27 разборов', 'Семь про домашние обереги и двадцать про нечистую силу.'))}
"""
    page(f'zhurnal/{a["url"]}/', f'{a["name"]}: {a["deck"][:70].rstrip(",. ")}',
         a['deck'][:180], body, active='zhurnal/',
         og=f'images/og/st-{a["slug"]}.jpg',
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
<div class="grid3">{dobit(''.join(kadr(a, metka=False) for a in ob), len(ob), DOBAVKI['oberegi'])}</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Нечисть</p>
<h2>Кто жил рядом с человеком</h2>
<div class="grid3">{dobit(''.join(kadr(a, metka=False) for a in ne), len(ne), DOBAVKI['nechist'])}</div>
</div></section>

{finalny('Что выходит дальше',
         'Свежие разборы и объявления о наборах появляются в телеграм-канале школы раньше, '
         'чем где-либо ещё.',
         vtoraya=('shkola/', 'Как учат в школе'), knopka='Читать канал',
         side=('По источникам', 'У каждой приметы назван собиратель, который её записал.'))}
"""
    page('zhurnal/', 'Журнал: разборы про обереги и нечистую силу',
         'Двадцать семь разборов Ирины Волковой о домашних оберегах и нечистой силе славянской '
         'деревни, собранных по источникам.', body, active='zhurnal/',
         og='images/og/zhurnal.jpg', crumbs=[HOME, ('Журнал', None)])


def razdel(kind, articles):
    arts = [a for a in articles if a['kind'] == kind]
    if kind == 'oberegi':
        title, h1 = 'Обереги дома', 'Обереги славянского дома'
        eyebrow, img = 'Раздел журнала', 'oberegi'
        lid = ('Нож на ночь, красный угол, крапива у порога, громничная свеча. Семь разборов '
               'о том, чем деревня держала дом и откуда эти правила взялись.')
        vvod = [
            'Домашний оберег в деревне был работой с границей: где вход, где порог, где угол, где окно. '
            'У каждой границы свой предмет и своё правило. Знали их все, от хозяйки до ребёнка.',
            'Логика везде одна. Опасность приходит снаружи и заходит через щель, поэтому щель '
            'закрывают: солью, ножом, крапивой, огнём освящённой свечи, красным углом с рушником. '
            'Отсюда и запреты, которые сегодня выглядят суеверием, а на деле были частью порядка.',
            'В разборах ниже собрано, что именно делали, в какие дни и почему. Источник называется '
            'прямо в тексте.',
        ]
        kurs = ('kursy/besy/', 'Курс по славянской демонологии')
    else:
        title, h1 = 'Нечисть', 'Нечистая сила славянской деревни'
        eyebrow, img = 'Раздел журнала', 'nechist'
        lid = ('Домовой, леший, водяной, банник, полудница, мара, упырь. Двадцать разборов '
               'о тех, кого деревня считала соседями по двору, лесу и воде.')
        vvod = [
            'Народная вера различала нечисть очень подробно. У каждого своё место, свой час и свои правила: '
            'домовой держится печи, банник остаётся в бане после третьего пара, полудница выходит '
            'в полдень над полем, водяной сидит в омуте.',
            'Отсюда и разные обереги. Того, кто живёт в доме, задабривали угощением и поклоном. '
            'От пришедшего с погоста закрывались осиной и рассыпанным зерном. Общего средства '
            'не было: против каждого работало своё, и в каждой местности набор отличался.',
            'В разборах собрано, кто есть кто, по каким приметам его узнавали и как с ним обходились. '
            'У каждой приметы назван собиратель, который её записал.',
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
<p>{T('разборов в этом разделе, у каждого назван источник записи.')}</p></aside></div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Разборы</p>
<h2>{'Чем держали дом' if kind == 'oberegi' else 'Кто есть кто'}</h2>
<div class="grid3">{dobit(''.join(kadr(a, metka=False) for a in arts), len(arts), DOBAVKI[kind])}</div>
</div></section>

{finalny('Куда идут разборы дальше',
         'Разобранное здесь на курсах разворачивается подробнее: с источниками, спорными местами '
         'и практикой.',
         vtoraya=('kursy/', 'Все курсы'), knopka='Читать канал школы',
         side=('Из деревни', 'Материал взят из быличек и записей этнографов, а не из современных подборок.'))}
"""
    page(f'{kind}/' if kind == 'oberegi' else 'nechist/',
         title + ': разборы по источникам', lid[:180], body, active='zhurnal/',
         og=f'images/og/{img}.jpg', crumbs=[HOME, ('Журнал', 'zhurnal/'), (title, None)])
