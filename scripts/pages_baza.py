# -*- coding: utf-8 -*-
"""Раздел «Библиотека»: лонгриды-справочники по канону базы знаний
thebodymindcode.ru, переложенному на сайт школы Ирины Волковой."""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from engine import ico, typo, TG, DOMAIN
from layout import page, u, ph

T = typo


def krohki(nazvanie):
    return (f'<div class="wrap"><div class="kb-crumbs">'
            f'<a href="{u()}">Главная</a> / <a href="{u("baza/")}">Библиотека</a> / {nazvanie}</div></div>')


def tldr(punkty):
    li = ''.join(f'<li>{T(x)}</li>' for x in punkty)
    return f'<div class="kb-tldr"><b>Коротко</b><ul>{li}</ul></div>'


def toc(razdely):
    li = ''.join(f'<li><a href="#{i}">{n}</a></li>' for i, n in razdely)
    return f'<details class="kb-toc" open><summary>Содержание</summary><ol>{li}</ol></details>'


def stats(troyka):
    d = ''.join(f'<div class="stat"><b>{b}</b><span>{T(s)}</span></div>' for b, s in troyka)
    return f'<div class="artstats"><div class="stats">{d}</div></div>'


def tablica(shapka, ryady):
    th = ''.join(f'<th>{x}</th>' for x in shapka)
    tr = ''.join('<tr>' + ''.join(f'<td>{T(str(y))}</td>' for y in r) + '</tr>' for r in ryady)
    return f'<div class="kb-tbl"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def vrezka(text):
    return f'<div class="kb-call">{T(text)}</div>'


def citata(text):
    return f'<div class="kb-pull">{T(text)}</div>'


def praktika(zagolovok, vvod, shagi):
    li = ''.join(f'<li>{T(x)}</li>' for x in shagi)
    return (f'<div class="kb-practice"><b>{zagolovok}</b><p>{T(vvod)}</p><ol>{li}</ol></div>')


def mostik(text):
    return f'<div class="kb-bridge"><p>{T(text)}</p></div>'


def faq(pary):
    d = ''.join(
        f'<details><summary>{v}</summary><div class="fa">'
        + ''.join(f'<p>{T(a)}</p>' for a in (o if isinstance(o, list) else [o]))
        + '</div></details>' for v, o in pary)
    return f'<h2 id="faq">Частые вопросы</h2><div class="kb-faq">{d}</div>'


def istochniki(spisok):
    li = ''.join(
        f'<li>{T(opis)} <a href="{ssyl}" target="_blank" rel="noopener">{ssyl.split("/")[2]}</a></li>'
        for opis, ssyl in spisok)
    return f'<details class="kb-src"><summary>Источники</summary><ol>{li}</ol></details>'


def avtor():
    return (f'<div class="kb-author"><img src="{u("images/obrazy/p-irina1.jpg")}" alt="Ирина Волкова">'
            f'<div><b>Ирина Волкова</b><span>{T("Практикует с двадцати трёх лет, первый авторский курс собрала в 2014 году. Ведёт школу таро, ритуальной магии, рун и домашних оберегов.")}</span></div></div>')


def razmetka(zag, opis, slug, data, faq_pary):
    adres = f'{DOMAIN}/baza/{slug}/'
    art = {"@context": "https://schema.org", "@type": "Article", "headline": zag,
           "description": opis, "datePublished": data, "dateModified": data,
           "author": {"@type": "Person", "name": "Ирина Волкова"},
           "publisher": {"@type": "Organization", "name": "Школа Ирины Волковой"},
           "mainEntityOfPage": adres,
           "image": f'{DOMAIN}/ira-shkola/images/baza/{slug}.jpg'}
    kroh = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Главная", "item": f'{DOMAIN}/ira-shkola/'},
        {"@type": "ListItem", "position": 2, "name": "Библиотека", "item": f'{DOMAIN}/ira-shkola/baza/'},
        {"@type": "ListItem", "position": 3, "name": zag, "item": adres}]}
    fq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": v,
         "acceptedAnswer": {"@type": "Answer",
                            "text": ' '.join(o if isinstance(o, list) else [o])}}
        for v, o in faq_pary]}
    return ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>'
                   for x in (art, kroh, fq))


def anons(text, predel=140):
    """Режем по границе слова: обрыв на полуслове читается как ошибка."""
    t = ' '.join(text.split())
    if len(t) <= predel:
        return t
    kus = t[:predel]
    kus = kus[:kus.rfind(' ')].rstrip(' ,.;:')
    return kus + '…'


def statya(d, sosedi):
    """Собирает страницу лонгрида из словаря статьи."""
    razdely_html = ''.join(
        f'<h2 id="{r["id"]}">{T(r["h2"])}</h2>{r["telo"]}' for r in d['razdely'])
    tabl = ''
    if d.get('tablica'):
        tabl = tablica(d['tablica']['shapka'], d['tablica']['ryady'])
    rel = ''
    if sosedi:
        kart = ''.join(
            f'<a class="kb-card" href="{u("baza/" + s["slug"] + "/")}">'
            f'{ph("images/baza/" + s["slug"] + ".jpg", s["h1"])}'
            f'<div class="body"><span class="metka">Библиотека</span><h3>{T(s["h1"])}</h3>'
            f'<p>{T(anons(s["lead"], 120))}</p><span class="chit">Читать разбор</span></div></a>'
            for s in sosedi[:2])
        rel = (f'<section><div class="wrap"><p class="eyebrow">Читать дальше</p>'
               f'<h2>Соседние разборы</h2><div class="kb-grid">{kart}</div></div></section>')
    telo = f"""<section class="artgero"><div class="wrap">
<div class="ph16"><img src="{u('images/baza/' + d['slug'] + '.jpg')}" alt="{T(d['h1'])}"
 width="1600" height="900" fetchpriority="high"></div></div></section>
<section><div class="wrap article">
<h1>{T(d['h1'])}</h1>
<div class="artmeta"><span>{ico('kniga')} <b>Библиотека</b></span>
<span>{ico('chas')} {d.get('chtenie', '12 минут')}</span>
<span>{ico('luna')} {d.get('data_vid', '21 августа 2026')}</span></div>
<p class="lid">{T(d['lead'])}</p>
{tldr(d['tldr'])}
{toc([(r['id'], r['h2']) for r in d['razdely']] + [('faq', 'Частые вопросы')])}
{stats(d['stats'])}
{razdely_html}
{tabl}
{praktika(d['praktika']['zag'], d['praktika']['vvod'], d['praktika']['shagi'])}
{mostik(d['mostik'])}
{faq(d['faq'])}
{istochniki(d['istochniki'])}
{avtor()}
</div></section>
{rel}
"""
    return page(f"baza/{d['slug']}/", d['title'], d['descr'], telo, active='baza/',
                og=f"images/og/baza-{d['slug']}.jpg",
                crumbs=[('Библиотека', 'baza/')],
                schema=razmetka(d['h1'], d['descr'], d['slug'],
                                d.get('data', '2026-08-21'), d['faq']))


RUBRIKI = [
    ('taro', 'Таро', 'karta', 'Колода как рабочий инструмент: чтение, позиции, разборы арканов.'),
    ('runy', 'Руны', 'runa', 'Северные знаки: история ряда, имена, поэмы, работа с поставом.'),
    ('oberegi', 'Обереги дома', 'dom', 'Домашняя защита славянской деревни, разобранная по записям собирателей.'),
    ('nechist', 'Нечистая сила', 'les', 'Кто где живёт, в какие часы встречали и как с этим обходились.'),
    ('magiya', 'Ритуальная магия', 'svecha', 'Обряд, порядок работы и правила, на которых он держится.'),
]


def kartochka(s, rubrika_imya):
    return (f'<a class="kb-card" href="{u("baza/" + s["slug"] + "/")}" '
            f'data-poisk="{(s["h1"] + " " + s["lead"]).lower()}">'
            f'{ph("images/baza/" + s["slug"] + ".jpg", s["h1"])}'
            f'<div class="body"><span class="metka">{rubrika_imya}</span>'
            f'<h3>{T(s["h1"])}</h3><p>{T(anons(s["lead"], 150))}</p>'
            f'<span class="chit">Читать разбор {ico("strela")}</span></div></a>')


def hab(statyi):
    po_rubrikam = {}
    for s in statyi:
        po_rubrikam.setdefault(s.get('rubrika_id', 'taro'), []).append(s)
    gruppy = ''
    for rid, imya, ikona, opis in RUBRIKI:
        spisok = po_rubrikam.get(rid, [])
        if not spisok:
            continue
        kart = ''.join(kartochka(x, imya) for x in spisok)
        gruppy += (f'<div class="kb-group" id="rub-{rid}" data-rub="{rid}">'
                   f'<div class="gh"><span class="ic">{ico(ikona)}</span>'
                   f'<div><b>{imya}</b><span>{T(opis)}</span></div>'
                   f'<i class="gn">{len(spisok)}</i></div>'
                   f'<div class="kb-grid">{kart}</div></div>')
    kolvo = len(statyi)
    slovo = 'разбор' if kolvo % 10 == 1 and kolvo % 100 != 11 else (
        'разбора' if kolvo % 10 in (2, 3, 4) and kolvo % 100 not in (12, 13, 14) else 'разборов')
    telo = f"""<section class="hb"><div class="wrap">
<div class="hb-hero">
<span class="eb">Библиотека</span>
<h1>Разборы, после которых не нужен третий сайт</h1>
<p>{T('Ищешь значение знака и находишь пять разных ответов, ни одного с указанием, откуда он взялся. '
      'Здесь у каждого утверждения назван источник: рукопись, находка, работа исследователя. '
      'Где они расходятся между собой, так и написано.')}</p>
<p>{T('Внутри полные разборы: старший футарк по знакам, работа с колодой, домашние обереги, '
      'нечистая сила деревни. Каждый заканчивается практикой на сегодня.')}</p>
<a class="hb-count" href="#vse"><b>{kolvo}</b> {slovo} в библиотеке {ico('strela')}</a>
<div class="hb-feat">
<span>{ico('kniga')} Источник у каждого утверждения</span>
<span>{ico('glaz')} Разбор, а не пересказ</span>
<span>{ico('ruka')} Практика в конце</span>
</div>
</div>
<div class="kb-poisk">
<label class="kb-pole"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"
 stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="6.4"/><path d="M16 16l4.4 4.4"/></svg>
<input type="search" id="kb-q" placeholder="Найти разбор: руны, карта дня, порог, домовой"
 autocomplete="off" aria-label="Поиск по библиотеке">
</label>
<button class="kb-clr" id="kb-clr" type="button" hidden>Сбросить</button>
</div>
<div id="vse" class="kb-rows">{gruppy}</div>
<p class="kb-itog" id="kb-itog" hidden>Ничего не нашлось. Попробуйте другое слово.</p>
</div></section>"""
    return page('baza/', 'Библиотека школы Ирины Волковой',
                'Длинные разборы школы: руны старшего футарка, работа с колодой таро, домашние обереги. '
                'Всё по источникам и с практикой.', telo, active='baza/')
