# -*- coding: utf-8 -*-
"""Тёмный мистический премиум. Вся палитра в токенах :root."""

CSS = r"""
:root{
  --noch:#0E0C11; --sloy:#16131C; --sloy2:#1D1926; --line:rgba(232,226,217,.13);
  --tekst:#E9E3DA; --tihiy:#A79E93; --zoloto:#C9A227; --zoloto-svet:#E3C15B;
  --bordo:#7A2033; --wrap:1180px; --uzko:720px; --r:12px;
  --sans:'Montserrat',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  --serif:'Cormorant Garamond',Georgia,'Times New Roman',serif;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--noch);color:var(--tekst);font-family:var(--sans);
  font-size:17px;line-height:1.68;font-weight:400;-webkit-font-smoothing:antialiased;
  overflow-x:hidden}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
a,button,summary,.plashka{touch-action:manipulation;-webkit-tap-highlight-color:transparent}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 24px}
h1,h2,h3,h4{font-family:var(--serif);font-weight:600;letter-spacing:.2px;margin:0;
  line-height:1.14;color:#F3EDE3}
h1{font-size:clamp(38px,5.6vw,68px)}
h2{font-size:clamp(30px,3.8vw,46px)}
h3{font-size:clamp(21px,2.2vw,27px);line-height:1.24}
h1 em,h2 em{font-style:normal;color:var(--zoloto-svet)}
p{margin:0 0 18px;text-wrap:pretty}
section{padding:78px 0;border-top:1px solid var(--line)}
section:first-of-type{border-top:0}
.uzko>*{max-width:var(--uzko)}
.eyebrow{font-family:var(--sans);font-size:12.5px;letter-spacing:2.4px;text-transform:uppercase;
  color:var(--zoloto);margin:0 0 14px;font-weight:600}
.lid{font-size:19.5px;line-height:1.62;color:#D9D2C8;max-width:var(--uzko);text-wrap:pretty}
.tihiy{color:var(--tihiy)}
svg.ic{width:22px;height:22px;flex:none}
li svg,p svg,span svg{width:18px;height:18px;flex:none}
svg.big{width:34px;height:34px}

/* ---------- шапка ---------- */
.shapka{position:sticky;top:0;z-index:60;background:rgba(14,12,17,.93);
  backdrop-filter:saturate(150%) blur(12px);border-bottom:1px solid var(--line)}
.shapka .in{max-width:var(--wrap);margin:0 auto;padding:0 24px;height:72px;
  display:flex;align-items:center;gap:26px}
.znak{display:flex;align-items:center;gap:11px;font-family:var(--serif);font-size:20px;
  color:#F3EDE3;font-weight:600;white-space:nowrap}
.znak svg{width:26px;height:26px;color:var(--zoloto)}
.nav{display:flex;gap:22px;margin-left:auto;align-items:center}
.nav a{font-size:14.5px;font-weight:500;color:#CFC7BC;padding:6px 0;position:relative}
.nav a.on{color:var(--zoloto-svet)}
.nav a.on::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:var(--zoloto)}
.burger{display:none;margin-left:auto;background:none;border:1px solid var(--line);
  border-radius:10px;width:44px;height:44px;color:var(--tekst);align-items:center;justify-content:center}
.burger svg{width:20px;height:20px}
.mob{display:none;border-top:1px solid var(--line);background:var(--sloy)}
.mob.open{display:block}
.mob a{display:block;padding:14px 24px;border-bottom:1px solid var(--line);font-size:16px}
@media(max-width:980px){.nav{display:none}.burger{display:flex}}
@media(hover:hover){.nav a:hover{color:var(--zoloto-svet)}}

/* ---------- кнопки ---------- */
.btn{display:inline-flex;align-items:center;gap:9px;position:relative;
  padding:14px 24px;border-radius:var(--r);font-size:15px;font-weight:600;
  border:1px solid transparent;min-height:48px;transition:transform .12s,background .18s}
.btn::after{content:"";position:absolute;top:7px;right:7px;width:9px;height:9px;
  border-top:1.5px solid currentColor;border-right:1.5px solid currentColor;opacity:.5}
.btn-gold{background:var(--zoloto);color:#151009}
.btn-ghost{border-color:rgba(232,226,217,.28);color:var(--tekst)}
.btn:active{transform:scale(.985)}
@media(hover:hover){.btn-gold:hover{background:var(--zoloto-svet)}
  .btn-ghost:hover{border-color:var(--zoloto);color:var(--zoloto-svet)}}
.knopki{display:flex;flex-wrap:wrap;gap:14px;margin-top:30px}

/* ---------- герой ---------- */
.hero{position:relative;padding:0;border:0;min-height:clamp(460px,62vh,640px);display:flex;align-items:flex-end}
.hero .fon{position:absolute;inset:0;overflow:hidden}
.hero .fon img{width:100%;height:100%;object-fit:cover;opacity:.55}
.hero .fon::after{content:"";position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(14,12,17,.5) 0%,rgba(14,12,17,.72) 46%,var(--noch) 100%)}
.hero .in{position:relative;width:100%;padding:64px 0 66px}
.hero p.lid{color:#DCD5CA}

/* ---------- лента шагов ---------- */
.stepline{margin:34px 0 0;padding:0;list-style:none;border-top:1px solid var(--line)}
.stepline li{display:flex;gap:20px;align-items:flex-start;padding:22px 0;border-bottom:1px solid var(--line)}
.stepline .nom{font-family:var(--serif);font-size:26px;color:var(--zoloto);width:38px;flex:none;line-height:1}
.stepline .txt{max-width:760px}
.stepline h3{margin:0 0 6px}
.stepline p{margin:0;color:var(--tihiy);font-size:16px}
.stepline svg{color:var(--zoloto);margin-top:4px}

/* ---------- сетки карточек ---------- */
.grid2,.grid3{display:grid;gap:20px;margin-top:34px}
.grid2{grid-template-columns:repeat(2,minmax(0,1fr))}
.grid3{grid-template-columns:repeat(3,minmax(0,1fr))}
.card{background:var(--sloy);border:1px solid var(--line);border-radius:18px;padding:26px;
  display:flex;flex-direction:column;transition:border-color .18s,transform .18s}
.card svg{color:var(--zoloto);margin-bottom:14px}
.card h3{margin:0 0 10px}
.card p{color:var(--tihiy);font-size:16px;margin:0 0 14px}
.card p.more{margin-top:auto;margin-bottom:0;font-size:14.5px;color:var(--zoloto-svet);font-weight:600}
@media(hover:hover){a.card:hover{border-color:rgba(201,162,39,.55);transform:translateY(-2px)}}

/* ---------- карточка с кадром ---------- */
.kadr{border-radius:18px;overflow:hidden;border:1px solid var(--line);background:var(--sloy)}
.kadr .ph{aspect-ratio:16/9;overflow:hidden}
.kadr .ph img{width:100%;height:100%;object-fit:cover}
.kadr .body{padding:22px 24px 26px}
.kadr h3{margin:0 0 9px}
.kadr p{color:var(--tihiy);font-size:15.5px;margin:0}
.metka{display:inline-block;font-size:11.5px;letter-spacing:1.6px;text-transform:uppercase;
  color:var(--zoloto);border:1px solid rgba(201,162,39,.4);border-radius:999px;padding:4px 11px;margin-bottom:12px}

/* ---------- сплит ---------- */
.split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.85fr);gap:52px;align-items:center;margin-top:36px}
.split .ph{aspect-ratio:3/4;border-radius:18px;overflow:hidden;border:1px solid var(--line)}
.split .ph img{width:100%;height:100%;object-fit:cover}
.split.shir .ph{aspect-ratio:16/9}

/* ---------- цифры ---------- */
.nails{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;margin-top:34px}
.nail{border-left:2px solid var(--zoloto);padding:4px 0 4px 18px}
.nail b{display:block;font-family:var(--serif);font-size:40px;color:#F3EDE3;line-height:1;font-weight:600}
.nail span{display:block;margin-top:9px;color:var(--tihiy);font-size:15px}

/* ---------- тёмная лента пунктов ---------- */
.dlist{background:var(--sloy2);border:1px solid var(--line);border-radius:20px;padding:34px;margin-top:34px}
.dlist ul{list-style:none;margin:0;padding:0;display:grid;gap:16px}
.dlist li{display:flex;gap:14px;align-items:flex-start;font-size:16.5px}
.dlist svg{color:var(--zoloto);margin-top:3px}

/* ---------- текст с врезкой ---------- */
.tside{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:56px;align-items:start;margin-top:30px}
.tside>.col>*{max-width:680px}
.side{position:sticky;top:96px;background:var(--sloy);border:1px solid var(--line);
  border-radius:16px;padding:24px}
.side .cifra{font-family:var(--serif);font-size:34px;color:var(--zoloto-svet);line-height:1}
.side p{font-size:15px;color:var(--tihiy);margin:12px 0 0}
.side h4{font-size:19px;margin:0 0 10px}

/* ---------- статья ---------- */
.art h2{margin:44px 0 14px}
.art h2:first-of-type{margin-top:30px}
.art p{max-width:var(--uzko)}
.art .vrez{border-left:2px solid var(--zoloto);padding:2px 0 2px 20px;margin:26px 0;
  font-family:var(--serif);font-size:23px;line-height:1.34;color:#F0E9DE;max-width:640px}

/* ---------- плашки-ссылки ---------- */
.plashki{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}
.plashka{display:inline-flex;align-items:center;gap:8px;padding:10px 16px;border:1px solid var(--line);
  border-radius:11px;background:var(--sloy);font-size:14.5px;color:#CFC7BC}
@media(hover:hover){.plashka:hover{border-color:rgba(201,162,39,.5);color:var(--zoloto-svet)}}

/* ---------- финал ---------- */
.final{background:var(--sloy2);border:1px solid var(--line);border-radius:22px;padding:44px}
.final h2{margin:0 0 14px}
.final p{color:#D2CAC0;max-width:640px}

/* ---------- вопросы ---------- */
.vopros{border-bottom:1px solid var(--line)}
.vopros summary{cursor:pointer;list-style:none;padding:20px 0;display:flex;gap:16px;
  align-items:flex-start;font-family:var(--serif);font-size:21px;color:#F0E9DE}
.vopros summary::-webkit-details-marker{display:none}
.vopros summary svg{color:var(--zoloto);margin-top:5px;transition:transform .2s}
.vopros[open] summary svg{transform:rotate(90deg)}
.vopros .otvet{padding:0 0 22px 38px;max-width:720px}
.vopros .otvet p{margin:0 0 12px;color:var(--tihiy);font-size:16.5px}
.vopros .otvet p:first-child strong{color:var(--tekst)}

/* ---------- подвал ---------- */
.podval{border-top:1px solid var(--line);background:#0B0910;padding:56px 0 40px;margin-top:20px}
.podval .kol{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1.4fr);gap:44px}
.podval h4{font-family:var(--sans);font-size:12.5px;letter-spacing:2px;text-transform:uppercase;
  color:var(--zoloto);margin:0 0 16px;font-weight:600}
.podval p{color:var(--tihiy);font-size:15px}
.niz{margin-top:38px;padding-top:22px;border-top:1px solid var(--line);
  display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between;color:#7E7669;font-size:13.5px}
.niz a{color:#7E7669}
.soc{display:flex;gap:10px;margin-top:18px}

/* ---------- хлебные крошки ---------- */
.kroshki{font-size:13.5px;color:#7E7669;padding:22px 0 0}
.kroshki a{color:#9A9184}
.kroshki span{margin:0 7px}

/* ---------- мобильное ---------- */
@media(max-width:1000px){
  .split{grid-template-columns:1fr!important;gap:30px}
  .tside{grid-template-columns:1fr!important;gap:30px}
  .side{position:static}
  .nails{grid-template-columns:repeat(2,minmax(0,1fr))!important}
  .podval .kol{grid-template-columns:1fr!important;gap:32px}
}
@media(max-width:640px){
  body{font-size:16.5px}
  section{padding:54px 0}
  .grid2,.grid3{grid-template-columns:1fr!important;gap:16px}
  .nails{grid-template-columns:1fr!important}
  .final,.dlist{padding:26px 22px}
  .hero .in{padding:44px 0 46px}
  .wrap,.shapka .in{padding:0 18px}
  .stepline li{gap:14px}
  .art .vrez{font-size:20px}
}
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Cormorant+Garamond:wght@500;600;700&family=Montserrat:wght@400;500;600&display=swap">')
