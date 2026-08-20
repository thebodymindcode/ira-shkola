# -*- coding: utf-8 -*-
import sys, os, json, html, re


def sklonenie(n, odin, dva, mnogo):
    n = abs(n) % 100
    if 11 <= n <= 14:
        return mnogo
    n %= 10
    if n == 1:
        return odin
    if 2 <= n <= 4:
        return dva
    return mnogo
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
      'В потоке обереги идут подробнее, вместе с тем, откуда они пришли и против чего ставились.',
      'kursy/besy/', 'Курс по демонологии'),
  zov('kniga', 'Как здесь учат',
      'Закрытый канал, задание после каждой темы и разбор работы вслух.',
      'shkola/', 'Устройство обучения'),
 ],
 'nechist': [
  zov('ogon', 'Пройти это курсом',
      'В потоке по демонологии существ проходят по одному, от имени и места до оберегов против него.',
      'kursy/besy/', 'Смотреть курс'),
  zov('dom', 'Обереги дома',
      'Вторая половина журнала: чем деревня закрывала порог, окно и красный угол.',
      'oberegi/', 'Читать разборы'),
 ],
}


ISTOKI = {
 'nechist': [
  ('Откуда это известно', 'Разбор собран по деревенским быличкам, записанным собирателями в девятнадцатом и двадцатом веке. Приметы приводятся так, как их услышали на местах.'),
  ('Кто это записал', 'В основе полевые записи этнографов, то есть рассказы деревенских жителей о том, что они считали правдой своего двора и своего леса.'),
  ('На чём стоит текст', 'Всё, что здесь названо, взято из собранных быличек. Где в разных губерниях говорили по-разному, это сказано прямо в тексте.'),
  ('Источник', 'Материал взят из словарей народной веры и полевых записей, без поздних пересказов.'),
 ],
 'oberegi': [
  ('Откуда это известно', 'Обряд разобран по записям этнографов и деревенским быличкам. Что именно делали и в какие дни, приводится так, как записано у собирателей.'),
  ('Кто это записал', 'В основе полевые записи о домашних обычаях, о том, как закрывали порог, окно и красный угол.'),
  ('На чём стоит текст', 'Всё названное здесь взято из собранных записей о крестьянском быте. Где обычай отличался по губерниям, об этом сказано в тексте.'),
  ('Источник', 'Материал собран по словарям народной веры и записям о домашней обрядности, без поздних дополнений.'),
 ],
}

FINALY_STATEJ = [
 ('Читать дальше в канале', 'Каждый новый разбор Ирина сначала выкладывает в телеграм-канал школы.',
  ('kursy/besy/', 'Курс по демонологии'), 'Открыть канал',
  ('27 разборов', 'Семь про домашние обереги и двадцать про нечистую силу.')),
 ('Такие разборы выходят раз в несколько дней', 'В канале школы они появляются раньше, чем здесь, и там же их обсуждают.',
  ('nechist/', 'Вся нечистая сила'), 'Читать канал',
  ('С именем собирателя', 'У каждой приметы назван тот, кто её записал, и губерния.')),
 ('Это только часть темы', 'На курсе существо проходят целиком, от места и часа до спорных мест в записях.',
  ('kursy/besy/', 'Смотреть курс'), 'Спросить про набор',
  ('5 частей', 'Столько занимает одно существо в потоке.')),
 ('Дальше начинается практика', 'В школе то же самое делают руками. Обряд складывают, показывают и обсуждают вслух.',
  ('shkola/', 'Как устроено обучение'), 'Написать Ирине',
  ('Разбор при всех', 'Чужие работы в потоке видно, и на них учатся не меньше, чем на своих.')),
 ('Где искать продолжение', 'Свежие разборы и объявления о наборах Ирина публикует в канале школы.',
  ('oberegi/', 'Обереги дома'), 'Открыть канал школы',
  ('С 2014 года', 'Год первого авторского курса Ирины.')),
]


def kadr(a, metka=True):
    m = f'<span class="metka">{RAZDEL[a["kind"]][0]}</span>' if metka else ''
    return f"""<a class="kadr" href="{u('zhurnal/' + a['url'] + '/')}">
<div class="ph"><img src="{u('images/zhurnal/' + a['slug'] + '.jpg')}" alt="{a['name']}" loading="lazy"></div>
<div class="body">{m}<h3>{a['name']}</h3><p>{T(a['anons'])}</p></div></a>"""


def statya(a, sosedi, sosed_prev, sosed_next):
    razdel_name, razdel_path = RAZDEL[a['kind']]
    # выноска: короткое сильное предложение, вынесенное из текста (в тексте его не остаётся)
    vrez, vrez_posle, vrez_iz = '', -1, None
    kandidaty = []
    for i, sec in enumerate(a['sections']):
        if i == 0 or not sec['p']:
            continue
        for pi, p in enumerate(sec['p']):
            frazy = re.split(r'(?<=[.!?])\s+', p)
            if len(frazy) < 2:
                continue
            for fi, fr in enumerate(frazy):
                if fi == 0:
                    continue
                dl = len(fr)
                if 55 <= dl <= 135 and not fr.startswith(('Но ', 'И ', 'А ', 'То ', 'Это ')):
                    ves = (1 if '«' in fr else 0) + (1 if re.search(r'\d', fr) else 0)
                    kandidaty.append((ves, -abs(dl - 95), i, pi, fi, fr))
    if kandidaty:
        kandidaty.sort(reverse=True)
        _, _, si, pi, fi, fr = kandidaty[0]
        vrez, vrez_posle, vrez_iz = fr.strip(), si, (si, pi, fi)
    secs, toc = '', []
    for i, sec in enumerate(a['sections']):
        aid = f'r{i + 1}'
        toc.append(f'<li><a href="#{aid}">{html.escape(sec["h"])}</a></li>')
        abzacy = []
        for pi, p in enumerate(sec['p']):
            if vrez_iz and vrez_iz[0] == i and vrez_iz[1] == pi:
                frazy = re.split(r'(?<=[.!?])\s+', p)
                p = ' '.join(f for k, f in enumerate(frazy) if k != vrez_iz[2]).strip()
            if p:
                abzacy.append(f'<p>{T(html.escape(p))}</p>')
        ps = ''.join(abzacy)
        secs += f'<h2 id="{aid}">{T(html.escape(sec["h"]))}</h2>{ps}'
        if i == vrez_posle and vrez:
            secs += f'<div class="vrez">{T(html.escape(vrez))}</div>'
    # «Коротко»: первое предложение каждого раздела, то есть суть словами самой Ирины
    korotko = ''
    for x in a['sections']:
        if not x['p']:
            continue
        fraza = re.split(r'(?<=[.!?])\s+', x['p'][0])[0].strip()
        if len(fraza) > 150:
            fraza = fraza[:147].rsplit(' ', 1)[0] + '…'
        korotko += f'<li>{T(html.escape(fraza))}</li>'
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
    pervoe = re.match(r'[А-Яа-яЁёA-Za-z]+', a['lead'].strip())
    drop = 'drop' if pervoe and len(pervoe.group(0)) >= 3 else ''
    nomer = int(a['slug'].split('-')[0])
    ist_zag, ist_txt = ISTOKI[a['kind']][nomer % len(ISTOKI[a['kind']])]
    fz, ft, fv, fk, fs = FINALY_STATEJ[nomer % len(FINALY_STATEJ)]
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
<p class="lead {drop}">{T(html.escape(a['lead']))}</p>
<div class="byline"><b>Ирина Волкова</b><span class="dot"></span>
<span class="tag">{razdel_name}</span><span class="dot"></span>
<span>{len(a['sections'])} {sklonenie(len(a['sections']), 'раздел', 'раздела', 'разделов')}</span></div>
<div class="korotko"><b>Коротко</b><ul>{korotko}</ul></div>
<details class="toc"><summary>Что внутри</summary><ol>{''.join(toc)}</ol></details>
{secs}
<div class="istok"><b>{ist_zag}</b><p>{T(ist_txt)}</p></div>
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

{finalny(fz, ft, vtoraya=fv, knopka=fk, side=fs)}
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
{hero('images/obrazy/h-zhurnal.jpg', 'Журнал', 'Разборы Ирины Волковой',
      'Двадцать семь разборов о домашних оберегах и о нечистой силе славянской деревни. '
      'Всё собрано по записям этнографов и деревенским быличкам.', KNOPKI_TG)}

<section><div class="wrap">
<p class="eyebrow">Два раздела</p>
<h2>Куда смотреть</h2>
<div class="grid2">
<a class="kadr" href="{u('oberegi/')}">
<div class="ph"><img src="{u('images/obrazy/z-oberegi.jpg')}" alt="Обереги дома" loading="lazy"></div>
<div class="body"><h3>Обереги дома</h3><p>{T('Нож на ночь, красный угол, крапива у порога, громничная свеча, '
 'отливка воском, выкатать яйцом, оберег в люльку.')}</p></div></a>
<a class="kadr" href="{u('nechist/')}">
<div class="ph"><img src="{u('images/obrazy/z-nechist.jpg')}" alt="Нечисть" loading="lazy"></div>
<div class="body"><h3>Нечисть</h3><p>{T('Домовой, леший, водяной, банник, полудница, мара, упырь '
 'и другие жители народной веры.')}</p></div></a>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Обереги дома</p>
<h2>Чем закрывали порог и окно</h2>
<div class="grid3">{''.join(kadr(a, metka=False) for a in ob[:6])}</div>
<div class="knopki"><a class="btn btn-ghost" href="{u('oberegi/')}">Все {len(ob)} разборов про обереги</a></div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Нечисть</p>
<h2>Кто жил рядом с человеком</h2>
<div class="grid3">{''.join(kadr(a, metka=False) for a in ne[:6])}</div>
<div class="knopki"><a class="btn btn-ghost" href="{u('nechist/')}">Вся нечистая сила, {len(ne)} текстов</a></div>
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


FINAL_RAZDELA = {
 'oberegi': ('Что стоит за этими правилами',
   'На курсе обереги идут от границы дома, от порога и окна до красного угла. Становится видно, '
   'почему предмет ставили именно туда и почему запрет держался веками.',
   ('kursy/', 'Все курсы'), 'Читать канал школы',
   ('7 оберегов', 'Столько домашних оберегов уже описано в журнале.')),
 'nechist': ('Куда идут разборы дальше',
   'В потоке существо берут целиком, вместе с местом, часом, приметами и оберегами против него.',
   ('kursy/besy/', 'Курс по демонологии'), 'Спросить про набор',
   ('20 существ', 'Столько описано в журнале. В потоке список складывается под группу.')),
}


def razdel(kind, articles):
    arts = [a for a in articles if a['kind'] == kind]
    if kind == 'oberegi':
        title, h1 = 'Обереги дома', 'Обереги славянского дома'
        eyebrow, img = 'Раздел журнала', 'h-oberegi'
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
        eyebrow, img = 'Раздел журнала', 'h-nechist'
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

{finalny(*FINAL_RAZDELA[kind])}
"""
    page(f'{kind}/' if kind == 'oberegi' else 'nechist/',
         title + ': разборы по источникам', lid[:180], body, active='zhurnal/',
         og=f'images/og/{"oberegi" if kind == "oberegi" else "nechist"}.jpg', crumbs=[HOME, ('Журнал', 'zhurnal/'), (title, None)])
