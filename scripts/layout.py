# -*- coding: utf-8 -*-
"""Каркас страницы: head, шапка, подвал, крошки."""
import os, sys, json, re, html as _html
sys.path.insert(0, os.path.dirname(__file__))
from engine import BASE, VERSION, DOMAIN, TITLE_SITE, TG, IG, MENU, FOOTER_LINKS, ico, typo
from theme import CSS, FONTS

INDEXING = True   # единственный выключатель индексации на весь сайт

def u(path=''):
    return BASE + path

PODMENU = {
    'kursy/': [('kursy/grimuar/', 'Чёрный Гримуар'), ('kursy/besy/', 'Бесы'),
               ('kursy/gekata/', 'Геката'), ('kursy/runy/', 'Руны'),
               ('kursy/nastavnichestvo/', 'Личная работа'), ('shkola/', 'Как проходит обучение')],
    'taro/': [('taro/', 'Курс по таро'), ('karty/', 'Значения 22 арканов'),
              ('kviz/', 'Вопросник: ваш аркан'), ('luna/', 'Лунный круг')],
    'zhurnal/': [('oberegi/', 'Обереги дома'), ('nechist/', 'Нечистая сила'),
                 ('zhurnal/', 'Все разборы'), ('slovar/', 'Словарь')],
}


def podpanel(punkty):
    ssylki = ''.join(f'<a href="{u(p)}">{n}</a>' for p, n in punkty)
    return f'<div class="pod"><div class="pod-in">{ssylki}</div></div>'


def shapka(active):
    MEGA = {p: podpanel(v) for p, v in PODMENU.items()}
    nav = ''
    for n, p in MENU:
        on = ' class="on"' if (active is not None and p == active) else ''
        if p in MEGA:
            strelka = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
                       'stroke-linecap="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>')
            nav += (f'<div class="hasmega"><a href="{u(p)}"{on}>{n}{strelka}</a>{MEGA[p]}</div>')
        else:
            nav += f'<a href="{u(p)}"{on}>{n}</a>'
    mob = ''
    for n, p in MENU:
        on = ' class="on"' if (active is not None and p == active) else ''
        mob += f'<a href="{u(p)}"{on}>{n}</a>'
        if p in PODMENU:
            mob += ''.join(f'<a class="sub" href="{u(pp)}">{nn}</a>' for pp, nn in PODMENU[p])
    return f"""<header class="shapka"><div class="in">
<a class="znak" href="{u()}">{ico('klyuch')}<span>Школа Ирины&nbsp;Волковой</span></a>
<nav class="nav">{nav}</nav>
<button class="burger" id="burger" aria-label="Меню" aria-expanded="false">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div><div class="mob" id="mobmenu">{mob}</div></header>"""


def podval():
    links = ''.join(f'<a class="plashka" href="{u(p)}">{n}</a>' for n, p in FOOTER_LINKS)
    return f"""<footer class="podval"><div class="wrap">
<div class="kol">
<div>
<h4>Школа</h4>
<p>Ирина Волкова учит таро, ритуальной магии, рунам и домашним оберегам. Обучение идёт в закрытых
телеграм-каналах, поток за потоком, с разбором работ.</p>
<div class="soc">
<a class="plashka" href="{TG}" rel="noopener" target="_blank">{ico('tg')} Telegram</a>
<a class="plashka" href="{IG}" rel="noopener" target="_blank">{ico('ig')} Instagram</a>
</div>
</div>
<div>
<h4>Разделы</h4>
<div class="plashki">{links}</div>
</div>
</div>
<div class="niz">
<span>© Ирина Волкова, {2026}. Материалы сайта носят культурно-исторический и обучающий характер.</span>
<a href="{u('politika/')}">Политика конфиденциальности</a>
</div>
</div></footer>"""

def kroshki(items):
    """items: [(name, path), ...] без последнего звена-ссылки."""
    if not items:
        return ''
    out = []
    for i, (n, p) in enumerate(items):
        if p is None:
            out.append(f'<span class="tihiy">{n}</span>')
        else:
            out.append(f'<a href="{u(p)}">{n}</a>')
    return '<div class="wrap"><div class="kroshki">' + '<span>/</span>'.join(out) + '</div></div>'

def schema_crumbs(crumbs, title):
    items, pos = [], 1
    for n, p in (crumbs or []):
        items.append({"@type": "ListItem", "position": pos, "name": n,
                      "item": DOMAIN + '/' + (p or '')})
        pos += 1
    if not items:
        return ''
    d = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
    return f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>'


def schema_faq(body):
    """Собирает FAQPage из уже готовых блоков вопросов на странице."""
    qa = re.findall(r'<summary>.*?<span>(.*?)</span></summary>\s*<div class="otvet">(.*?)</div>',
                    body, re.S)
    if len(qa) < 2:
        return ''
    items = []
    for q, a in qa:
        txt = _html.unescape(re.sub(r'<[^>]+>', ' ', a)).replace('\xa0', ' ')
        txt = re.sub(r'\s+', ' ', txt).strip()
        items.append({"@type": "Question",
                      "name": _html.unescape(re.sub(r'<[^>]+>', '', q)).replace('\xa0', ' ').strip(),
                      "acceptedAnswer": {"@type": "Answer", "text": txt}})
    d = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}
    return f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>'



SIROTA_TAGS = ('h1', 'h2', 'h3', 'h4', 'li', 'summary', 'b', 'a')


def bez_sirot(html_text):
    """Клеит последнее слово неразрывным пробелом в заголовках и пунктах."""
    NB = '\u00a0'

    def skleit(m):
        otkr, telo, zakr = m.group(1), m.group(2), m.group(3)
        if '<' in telo and '>' in telo:
            hvost = re.split(r'(<[^>]+>)', telo)
            for i in range(len(hvost) - 1, -1, -1):
                if hvost[i] and not hvost[i].startswith('<') and ' ' in hvost[i].strip():
                    sl = hvost[i].strip().split()
                    if len(sl) >= 2 and len(sl[-1]) + len(sl[-2]) <= 24:
                        nv = re.sub(r'\s+(\S+)\s*$', NB + r'\1', hvost[i])
                        if ' ' in nv.strip():
                            hvost[i] = nv
                    break
            telo = ''.join(hvost)
        else:
            slova = telo.strip().split()
            if len(slova) > 2 and len(slova[-1]) + len(slova[-2]) <= 24:
                novoe = re.sub(r'\s+(\S+)\s*$', NB + r'\1', telo)
                # строка не должна стать неразрывной целиком: ей нужен хотя бы один обычный пробел
                if ' ' in novoe.strip():
                    telo = novoe
        return otkr + telo + zakr

    for tag in SIROTA_TAGS:
        html_text = re.sub(r'(<%s(?:\s[^>]*)?>)(.*?)(</%s>)' % (tag, tag),
                           skleit, html_text, flags=re.S)
    # выноска-цитата, лид, подзаголовок и строки подвала
    for pat in (r'(<div class="vrez">)(.*?)(</div>)',
                r'(<p class="lid[^"]*">)(.*?)(</p>)',
                r'(<p class="podzag">)(.*?)(</p>)',
                r'(<span>)(© [^<]*?)(</span>)'):
        html_text = re.sub(pat, skleit, html_text, flags=re.S)
    return html_text


def page(path, title, descr, body, active=None, og='obrazy/glavnaya.jpg', crumbs=None, schema=''):
    """Собирает и пишет html. path: '' | 'kursy/' | 'zhurnal/domovoy/'."""
    canon = DOMAIN + '/' + path
    schema = schema + schema_crumbs(crumbs, title) + schema_faq(body)
    robots = '' if INDEXING else '<meta name="robots" content="noindex,nofollow">'
    full = f'{title} | {TITLE_SITE}' if path else title
    html = f"""<!doctype html><html lang="ru"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{full}</title>
<meta name="description" content="{descr}">
<link rel="canonical" href="{canon}">{robots}
<meta property="og:type" content="website">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{descr}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAIN}/{og}?v={VERSION}">
<meta property="og:site_name" content="{TITLE_SITE}">
<meta name="theme-color" content="#0E0C11">
<link rel="icon" href="{u('favicon.svg')}?v={VERSION}" type="image/svg+xml">
<link rel="icon" href="{u('favicon-32.png')}?v={VERSION}" sizes="32x32">
<link rel="apple-touch-icon" href="{u('apple-touch-icon.png')}?v={VERSION}">
{FONTS}
<link rel="stylesheet" href="{u('site.css')}?v={VERSION}">
{schema}
</head><body>
{shapka(active)}
{kroshki(crumbs) if crumbs else ''}
<main>{bez_sirot(body)}</main>
<a class="plyv" href="{TG}" target="_blank" rel="noopener" aria-label="Написать в Telegram">{ico('tg')}<span>Написать в&nbsp;Telegram</span></a>
{bez_sirot(podval())}
<script src="{u('site.js')}?v={VERSION}" defer></script>
</body></html>"""
    out = os.path.join(path, 'index.html') if path else 'index.html'
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    open(out, 'w', encoding='utf-8').write(html)
    return out

JS = r"""document.addEventListener('DOMContentLoaded',function(){
var k=document.getElementById('kviz');
if(k){
 var d=JSON.parse(k.dataset.kviz), shag=0, schet={};
 var elNomer=k.querySelector('.kviz-nomer'), elPolosa=k.querySelector('.kviz-polosa i'),
     elVopros=k.querySelector('.kviz-vopros'), elOtvety=k.querySelector('.kviz-otvety'),
     elItog=k.querySelector('.kviz-itog');
 function risuj(){
  var v=d.voprosy[shag];
  elNomer.textContent='Вопрос '+(shag+1)+' из '+d.voprosy.length;
  elPolosa.style.width=Math.round(shag/d.voprosy.length*100)+'%';
  elVopros.textContent=v.q;
  elOtvety.innerHTML='';
  v.o.forEach(function(o){
   var b=document.createElement('button');
   b.className='kviz-otvet'; b.type='button'; b.textContent=o.t;
   b.addEventListener('click',function(){ schet[o.s]=(schet[o.s]||0)+1; shag++;
    if(shag<d.voprosy.length){risuj();} else {itog();} });
   elOtvety.appendChild(b);
  });
 }
 function itog(){
  var luchshiy=null,max=0;
  for(var s in schet){ if(schet[s]>max){max=schet[s];luchshiy=s;} }
  var karta=d.karty[luchshiy]||d.karty['durak'];
  var tpl=document.querySelector('template[data-slug="'+luchshiy+'"]');
  elNomer.textContent='Готово';
  elPolosa.style.width='100%';
  elVopros.textContent='Ваш аркан сейчас';
  elOtvety.innerHTML='';
  elItog.hidden=false;
  elItog.innerHTML='<div class="kviz-karta">'+(tpl?tpl.innerHTML:'')+'</div>'+
   '<div class="kviz-txt"><p class="eyebrow">Старший аркан '+karta.n+'</p>'+
   '<h3>'+karta.name+'</h3><p>'+karta.smysl+'</p>'+
   '<p class="kviz-klyuchi">'+karta.pryamo.join(' · ')+'</p>'+
   '<div class="knopki"><a class="btn btn-ghost" href="'+location.pathname.replace(/kviz\/$/,'')+
   'karty/'+luchshiy+'/">Разбор карты</a>'+
   '<button class="btn btn-ghost" type="button" id="kviz-snova">Пройти заново</button></div></div>';
  document.getElementById('kviz-snova').addEventListener('click',function(){
   shag=0; schet={}; elItog.hidden=true; elItog.innerHTML=''; risuj(); });
 }
 risuj();
}
if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window){
 var nabl=new IntersectionObserver(function(zapisi){
  zapisi.forEach(function(z){ if(z.isIntersecting){ z.target.classList.add('vidno'); nabl.unobserve(z.target); } });
 },{rootMargin:'0px 0px -8% 0px',threshold:0.06});
 document.querySelectorAll('main section > .wrap > *, main .shema, main .card, main .kadr, main .zov')
  .forEach(function(el){ el.classList.add('poyav'); nabl.observe(el); });
}
var b=document.getElementById('burger'),m=document.getElementById('mobmenu');
if(b&&m){b.addEventListener('click',function(){var o=m.classList.toggle('open');
b.setAttribute('aria-expanded',o?'true':'false');});
m.addEventListener('click',function(e){if(e.target.tagName==='A'){m.classList.remove('open');
b.setAttribute('aria-expanded','false');}});}
});"""
