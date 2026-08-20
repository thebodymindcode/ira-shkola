# -*- coding: utf-8 -*-
"""Каркас страницы: head, шапка, подвал, крошки."""
import os, sys, json, re, html as _html
sys.path.insert(0, os.path.dirname(__file__))
from engine import BASE, VERSION, DOMAIN, TITLE_SITE, TG, IG, MENU, FOOTER_LINKS, ico, typo, mico
from theme import CSS, FONTS

INDEXING = True   # единственный выключатель индексации на весь сайт

def u(path=''):
    # Картинку правят под тем же именем, поэтому браузер держит старую.
    # Метка версии заставляет его забрать свежую, чистить кеш руками не нужно.
    if path.rsplit('.', 1)[-1].lower() in ('jpg', 'jpeg', 'png', 'webp', 'svg', 'avif'):
        return f'{BASE}{path}?v={VERSION}'
    return BASE + path

# У каждой строки свой знак: по нему видно, куда провалится человек.
PODMENU = {
    'kursy/': [('kursy/grimuar/', 'Чёрный Гримуар', 'grimuar'), ('kursy/besy/', 'Бесы', 'besy'),
               ('kursy/gekata/', 'Геката', 'gekata'), ('kursy/runy/', 'Руны', 'runy_kurs'),
               ('kursy/nastavnichestvo/', 'Личная работа', 'nastav'),
               ('shkola/', 'Как проходит обучение', 'stupeni')],
    'taro/': [('taro/', 'Курс по таро', 'taro_kurs'), ('karty/', 'Значения 22 арканов', 'veer'),
              ('kviz/', 'Вопросник: ваш аркан', 'vopros'), ('luna/', 'Лунный круг', 'lunnyj_krug')],
    'zhurnal/': [('oberegi/', 'Обереги дома', 'obereg_dom'), ('nechist/', 'Нечистая сила', 'nechist_les'),
                 ('zhurnal/', 'Все разборы', 'razbory'), ('slovar/', 'Словарь', 'slovar_ikona')],
}


def podpanel(punkty):
    ssylki = ''.join(f'<a href="{u(p)}">{mico(i)}<span>{n}</span></a>' for p, n, i in punkty)
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
            mob += ''.join(f'<a class="sub" href="{u(pp)}">{mico(ii)}<span>{nn}</span></a>'
                           for pp, nn, ii in PODMENU[p])
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
 var d=JSON.parse(k.dataset.kviz), baza=k.dataset.karty||'', shag=0, schet={}, vybor=[];
 var elNomer=k.querySelector('.kviz-nomer'), elLuny=k.querySelector('.kviz-luny'),
     elVopros=k.querySelector('.kviz-vopros'), elOtvety=k.querySelector('.kviz-otvety'),
     elTelo=k.querySelector('.kviz-telo'), elItog=k.querySelector('.kviz-itog'),
     veer=[].slice.call(k.querySelectorAll('.veer-k'));
 function lico(slug){
  var t=document.querySelector('template[data-slug="'+slug+'"]');
  return t?t.innerHTML:'';
 }
 function luny(){
  [].forEach.call(elLuny.children,function(el,i){
   el.className = i<shag ? 'est' : (i===shag ? 'tut' : '');
  });
 }
 function podsvet(){
  veer.forEach(function(el,i){
   if(i===shag && shag<d.voprosy.length){el.classList.add('tut');} else {el.classList.remove('tut');}
  });
 }
 function otvet(o){
  if(k.classList.contains('zhdyom')) return;
  vybor[shag]=o.s; schet[o.s]=(schet[o.s]||0)+1;
  var kv=veer[shag];
  if(kv){
   veer.forEach(function(el){ el.classList.remove('vpered'); });
   kv.querySelector('.veer-lico').innerHTML=lico(o.s);
   kv.classList.add('otkryta'); kv.classList.add('vpered');
  }
  shag++; luny(); podsvet();
  elNomer.textContent = shag<d.voprosy.length ? 'Вопрос '+(shag+1)+' из '+d.voprosy.length : 'Ваш аркан';
  k.classList.add('zhdyom');
  setTimeout(function(){
   k.classList.remove('zhdyom');
   if(shag<d.voprosy.length){risuj();} else {itog();}
  },320);
 }
 function risuj(){
  var v=d.voprosy[shag];
  elNomer.textContent='Вопрос '+(shag+1)+' из '+d.voprosy.length;
  elVopros.textContent=v.q;
  elOtvety.innerHTML='';
  v.o.forEach(function(o){
   var b=document.createElement('button');
   b.className='kviz-otvet'; b.type='button'; b.textContent=o.t;
   b.addEventListener('click',function(){ otvet(o); });
   elOtvety.appendChild(b);
  });
  luny(); podsvet();
 }
 function itog(){
  var luchshiy=null,max=0;
  for(var s in schet){ if(schet[s]>max){max=schet[s];luchshiy=s;} }
  var karta=d.karty[luchshiy]||d.karty['durak'];
  var klyuchi=karta.pryamo.map(function(x){return '<li>'+x+'</li>';}).join('');
  var mini=vybor.map(function(s){return '<span class="mini">'+lico(s)+'</span>';}).join('');
  elTelo.hidden=true;
  elItog.hidden=false;
  elItog.innerHTML='<div class="itog-karta kviz-karta perevorot">'+lico(luchshiy)+'</div>'+
   '<div class="itog-txt"><p class="eyebrow">Старший аркан '+karta.n+'</p>'+
   '<h3>'+karta.name+'</h3><p class="itog-smysl">'+karta.smysl+'</p>'+
   '<ul class="itog-klyuchi">'+klyuchi+'</ul>'+
   '<div class="knopki"><a class="btn btn-gold" href="'+baza+luchshiy+'/">Открыть значение</a>'+
   '<button class="btn btn-ghost" type="button" id="kviz-snova">Пройти заново</button></div></div>'+
   '<div class="itog-ryad"><p class="itog-podpis">Что выпало по ответам</p>'+
   '<div class="itog-mini">'+mini+'</div></div>';
  document.getElementById('kviz-snova').addEventListener('click',function(){
   shag=0; schet={}; vybor=[];
   veer.forEach(function(el){ el.classList.remove('otkryta'); el.classList.remove('vpered');
    el.querySelector('.veer-lico').innerHTML=''; });
   elItog.hidden=true; elItog.innerHTML=''; elTelo.hidden=false; risuj();
   k.scrollIntoView({block:'center'});
  });
  var r=k.getBoundingClientRect();
  if(r.top<0 || r.top>window.innerHeight*0.55){
   window.scrollTo({top:window.pageYOffset+r.top-96,behavior:'smooth'});
  }
 }
 risuj();
}
/* ---- кадр ростом с текст ---- */
/* Ширина кадра подбирается под высоту соседней колонки: шире кадр, уже текст,
   выше текст, поэтому идём бинарным поиском. Где текста слишком много,
   кадр плывёт вместе с чтением, и низ блока не зияет дырой. */
(function(){
 var bloki=[].slice.call(document.querySelectorAll('.split'));
 if(!bloki.length) return;
 function proporciya(ph){
  var st=(getComputedStyle(ph).aspectRatio||'').split('/');
  var k=(st.length===2)? parseFloat(st[0])/parseFloat(st[1]) : 0.75;
  return (isFinite(k)&&k>0)? k : 0.75;
 }
 function schitat(){
  var uzko=window.matchMedia('(max-width:860px)').matches;
  bloki.forEach(function(b){
   var ph=b.querySelector('.stolb')||b.querySelector('.ph'), tx=b.firstElementChild;
   if(!ph||!tx||ph===tx) return;
   var kadr=ph.classList.contains('stolb')? ph.querySelector('.ph') : ph;
   if(!kadr) return;
   if(uzko){ ph.style.removeProperty('--shirina'); ph.classList.remove('plyvet'); return; }
   var k=proporciya(kadr);
   var zazor=parseFloat(getComputedStyle(b).columnGap)||52;
   var vsego=b.getBoundingClientRect().width;
   var lo=300, hi=Math.min(vsego*0.56, 640, vsego-zazor-360);
   if(hi<lo){ ph.style.setProperty('--shirina', Math.round(Math.max(260,hi))+'px'); return; }
   b.style.alignItems='flex-start';          // иначе меряем растянутую колонку, а не текст
   var luchshaya=hi, luchshee=Infinity;
   for(var i=0;i<=9;i++){                                   // ширина влияет на высоту текста
    var w=lo+(hi-lo)*i/9;                                   // немонотонно, поэтому скан
    ph.style.setProperty('--shirina', Math.round(w)+'px');
    var vysota=tx.scrollHeight;
    var mesto=(ph===kadr)? 0 : 150;                       // место под плашку с фактом
    var raznica=Math.abs(vysota - (w/k + mesto));
    if(raznica<luchshee){ luchshee=raznica; luchshaya=w; }
   }
   ph.style.setProperty('--shirina', Math.round(luchshaya)+'px');
   b.style.removeProperty('align-items');
   var ostatok=tx.scrollHeight - ph.getBoundingClientRect().height;
   ph.classList.toggle('plyvet', ostatok>160 && ph===kadr);
   // текст короче колонки с кадром: разводим абзацы по высоте, верх остаётся вровень
   var pervyj=tx.firstElementChild, posl=tx.lastElementChild;
   if(pervyj && posl){
    tx.style.justifyContent='';
    var vysota_teksta=posl.getBoundingClientRect().bottom - pervyj.getBoundingClientRect().top;
    var dyra=ph.getBoundingClientRect().height - vysota_teksta;
    tx.style.justifyContent = (dyra>34 && dyra<240) ? 'space-between' : '';
   }
  });
 }
 schitat();
 addEventListener('load', schitat);
 if(document.fonts && document.fonts.ready) document.fonts.ready.then(schitat);
 var t=null;
 addEventListener('resize', function(){ clearTimeout(t); t=setTimeout(schitat,160); });
 if('ResizeObserver' in window){
  var ro=new ResizeObserver(function(){ clearTimeout(t); t=setTimeout(schitat,80); });
  bloki.forEach(function(b){ if(b.firstElementChild) ro.observe(b.firstElementChild); });
 }
})();

/* ---- схема на узком экране открывается на рисунке, а не на пустом поле ---- */
(function(){
 var shemy=[].slice.call(document.querySelectorAll('.shema'));
 if(!shemy.length) return;
 function navesti(){
  if(!window.matchMedia('(max-width:640px)').matches) return;
  shemy.forEach(function(sh){
   if(sh.dataset.navedena) return;
   var zapas=sh.scrollWidth-sh.clientWidth;
   if(zapas>20){ sh.scrollLeft=Math.round(zapas/2); sh.dataset.navedena='1'; }
  });
 }
 navesti();
 addEventListener('load', navesti);
 addEventListener('resize', navesti);
})();

/* ---- живые искры в шапке ---- */
(function(){
 var hero=document.querySelector('.hero .fon');
 if(!hero || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
 var c=document.createElement('canvas'); c.className='iskry'; hero.appendChild(c);
 var x=c.getContext('2d'), W=0,H=0, chastic=[], zhivo=true, kadr=null;
 function razmer(){ var r=hero.getBoundingClientRect(); W=c.width=r.width; H=c.height=r.height; }
 function novaya(gde){ return {x:Math.random()*W, y:gde?Math.random()*H:H+10,
   r:Math.random()*2.4+0.8, v:Math.random()*0.42+0.12, drift:(Math.random()-0.5)*0.3,
   a:Math.random()*0.75+0.35, faza:Math.random()*6.28}; }
 function sozdat(n){ chastic=[]; for(var i=0;i<n;i++) chastic.push(novaya(true)); }
 function shag(){
  if(!zhivo){kadr=null;return;}
  x.clearRect(0,0,W,H);
  for(var i=0;i<chastic.length;i++){
   var p=chastic[i];
   p.y-=p.v; p.x+=p.drift+Math.sin((p.faza+=0.012))*0.16;
   if(p.y< -12) chastic[i]=novaya(false);
   var a=p.a*(0.55+0.45*Math.sin(p.faza*1.7));
   var R=p.r*4.6;
   var g=x.createRadialGradient(p.x,p.y,0,p.x,p.y,R);
   g.addColorStop(0,'rgba(255,222,140,'+a+')');
   g.addColorStop(0.35,'rgba(227,193,91,'+(a*0.55)+')');
   g.addColorStop(1,'rgba(227,193,91,0)');
   x.fillStyle=g; x.beginPath(); x.arc(p.x,p.y,R,0,6.283); x.fill();
  }
  kadr=requestAnimationFrame(shag);
 }
 razmer(); sozdat(W<640?38:86); shag();
 var t=null;
 addEventListener('resize',function(){ clearTimeout(t); t=setTimeout(function(){
   razmer(); sozdat(W<640?38:86); },220); });
 if('IntersectionObserver' in window){
  new IntersectionObserver(function(z){ z.forEach(function(e){
    zhivo=e.isIntersecting; if(zhivo && !kadr) shag(); }); },{threshold:0.02}).observe(hero);
 }
})();

/* ---- параллакс шапки ---- */
(function(){
 var im=document.querySelector('.hero .fon img');
 if(!im || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
 var tik=false;
 addEventListener('scroll',function(){
  if(tik) return; tik=true;
  requestAnimationFrame(function(){
   var y=Math.min(scrollY,700);
   im.style.transform='translate3d(0,'+(y*0.16).toFixed(1)+'px,0) scale(1.06)';
   tik=false;
  });
 },{passive:true});
})();

/* ---- цифры набегают ---- */
(function(){
 if(!('IntersectionObserver' in window)) return;
 if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
 var nabl=new IntersectionObserver(function(z){
  z.forEach(function(e){
   if(!e.isIntersecting) return;
   nabl.unobserve(e.target);
   var el=e.target, ish=(el.textContent||'');
   // \u00a0 после числа не трогаем: иначе «6 направлений» слипается в «6направлений»
   var m=ish.match(/^(\D*?)(\d+)([\s\S]*)$/);
   if(!m) return;
   var do_=m[1], chislo=parseInt(m[2],10), posle=m[3];
   if(!isFinite(chislo) || chislo>100000) return;
   var razryady = (m[2].length>4);        // год пишем как есть, без разбивки на разряды
   var t0=null;
   function tik(t){ if(!t0) t0=t;
    var k=Math.min(1,(t-t0)/900), e2=1-Math.pow(1-k,3);
    var v=Math.round(chislo*e2);
    el.textContent=do_+(razryady? v.toLocaleString('ru-RU') : String(v))+posle;
    if(k<1) requestAnimationFrame(tik); }
   el.textContent=do_+'0'+posle; requestAnimationFrame(tik);
  });
 },{threshold:0.6});
 document.querySelectorAll('.side .cifra, .final .fside b, .nail b')
  .forEach(function(el){ nabl.observe(el); });
})();

(function(){
 var mozhno = !window.matchMedia('(prefers-reduced-motion: reduce)').matches
              && 'IntersectionObserver' in window;
 if(!mozhno) return;
 var celi=[];
 document.querySelectorAll('main section > .wrap > *, main .shema, main .card, main .kadr, main .zov')
  .forEach(function(el){
   if(el.closest('.hero')) return;                 /* первый экран виден сразу */
   var b=el.getBoundingClientRect();
   if(b.top < innerHeight*1.05) return;            /* то, что уже в кадре, не прячем */
   celi.push(el);
  });
 celi.forEach(function(el){ el.classList.add('poyav'); });
 var nabl=new IntersectionObserver(function(zapisi){
  zapisi.forEach(function(z){ if(z.isIntersecting){ z.target.classList.add('vidno'); nabl.unobserve(z.target); } });
 },{rootMargin:'0px 0px -6% 0px',threshold:0.04});
 celi.forEach(function(el){ nabl.observe(el); });
 /* страховка: через 2.5 секунды показываем всё, что почему-то не проявилось */
 setTimeout(function(){ celi.forEach(function(el){ el.classList.add('vidno'); }); }, 2500);
})();

var b=document.getElementById('burger'),m=document.getElementById('mobmenu');
if(b&&m){b.addEventListener('click',function(){var o=m.classList.toggle('open');
b.setAttribute('aria-expanded',o?'true':'false');});
m.addEventListener('click',function(e){if(e.target.tagName==='A'){m.classList.remove('open');
b.setAttribute('aria-expanded','false');}});}
});"""


_RAZMERY = {}


def ph(img, alt=''):
    """Кадр в колонке: рамка берёт пропорцию самого файла, поэтому снимок стоит
    в ней целиком. Ни пустых полей вокруг, ни среза по голове и по нижней кромке."""
    if img not in _RAZMERY:
        try:
            from PIL import Image
            _RAZMERY[img] = Image.open(img).size
        except Exception:
            _RAZMERY[img] = (1045, 1400)
    w, h = _RAZMERY[img]
    a = u(img)
    shir = ' shirokij' if w > h * 1.15 else ''
    return (f'<div class="ph{shir}" style="aspect-ratio:{w}/{h}">'
            f'<img src="{a}" alt="{alt}" loading="lazy"></div>')


def stolb(img, alt, ikona, chislo, podpis, ssylka='', ssylka_text=''):
    """Колонка рядом с текстом: кадр целиком, под ним плашка с фактом.
    Плашка тянется и добирает остаток высоты, поэтому низ блока сходится."""
    from engine import ico
    niz = (f'<a class="dob-link" href="{u(ssylka)}">{ssylka_text}'
           f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
           f'stroke-linecap="round"><path d="M5 12h13M13 7l5 5-5 5"/></svg></a>') if ssylka else ''
    return (f'<div class="stolb">{ph(img, alt)}'
            f'<aside class="dobivka">{ico(ikona)}'
            f'<b>{chislo}</b><p>{podpis}</p>{niz}</aside></div>')
