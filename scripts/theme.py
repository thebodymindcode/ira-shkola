# -*- coding: utf-8 -*-
"""Тёмный мистический премиум. Вся палитра в токенах :root."""

CSS = r"""
:root{
  --noch:#0E0C11; --sloy:#16131C; --sloy2:#1D1926; --line:rgba(232,226,217,.13);
  --tekst:#E9E3DA; --tihiy:#A79E93; --zoloto:#C9A227; --zoloto-svet:#E3C15B;
  --bordo:#7A2033; --wrap:1180px; --uzko:720px; --r:12px;
  --sans:'Montserrat',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  --serif:'Prata',Georgia,'Times New Roman',serif;
  --anons:'Forum',Georgia,serif;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--noch);color:var(--tekst);font-family:var(--sans);
  font-size:17px;line-height:1.68;font-weight:400;-webkit-font-smoothing:antialiased;
  overflow-x:clip}
html{overflow-x:clip}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
a,button,summary,.plashka{touch-action:manipulation;-webkit-tap-highlight-color:transparent}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 24px}
h1,h2,h3,h4{font-family:var(--serif);font-weight:400;letter-spacing:.2px;margin:0 0 14px;
  line-height:1.14;color:#F3EDE3}
h3{margin-bottom:10px}
h1,h2,h3,h4,.zag,.kicker{hyphens:none!important;-webkit-hyphens:none!important}
h1{font-size:clamp(30px,5.4vw,64px);overflow-wrap:normal;word-break:normal;text-wrap:balance}
h2{font-size:clamp(25px,3.6vw,44px);overflow-wrap:normal;word-break:normal;text-wrap:balance}
h3{font-size:clamp(21px,2.2vw,27px);line-height:1.24;text-wrap:balance}
h1 em,h2 em{font-style:normal;color:var(--zoloto-svet)}
p{margin:0 0 18px;text-wrap:pretty}
section{padding:78px 0;border-top:1px solid var(--line)}
section:first-of-type{border-top:0}
.uzko>*{max-width:var(--uzko)}
.eyebrow{font-family:var(--anons);font-size:14px;letter-spacing:3.2px;text-transform:uppercase;
  color:var(--zoloto);margin:0 0 14px}
.lid{font-size:19.5px;line-height:1.62;color:#D9D2C8;max-width:var(--uzko);text-wrap:pretty}
.tihiy{color:var(--tihiy)}
svg.ic{width:22px;height:22px;flex:none}
li svg,p svg,span svg{width:18px;height:18px;flex:none}
svg.big{width:34px;height:34px}

/* ---------- шапка ---------- */
.shapka{position:sticky;top:0;z-index:60;background:rgba(14,12,17,.93);
  backdrop-filter:saturate(150%) blur(12px);border-bottom:1px solid var(--line)}
.shapka .in{max-width:var(--wrap);margin:0 auto;padding:0 24px;height:86px;
  display:flex;align-items:center;gap:26px}
.znak{display:flex;align-items:center;gap:12px;font-family:var(--anons);font-size:24px;
  color:#F3EDE3;letter-spacing:.6px;white-space:nowrap}
.znak svg{width:29px;height:29px;color:var(--zoloto)}
.nav{display:flex;gap:26px;margin-left:auto;align-items:center}
.nav a{font-family:var(--anons);font-size:19px;letter-spacing:.6px;color:#D8D0C5;
  padding:6px 0;position:relative}
.nav a.on{color:var(--zoloto-svet)}
.nav a.on::after{content:"";position:absolute;left:0;right:0;bottom:2px;height:1px;background:var(--zoloto)}
.burger{display:none;margin-left:auto;background:none;border:1px solid var(--line);
  border-radius:10px;width:44px;height:44px;color:var(--tekst);align-items:center;justify-content:center}
.burger svg{width:20px;height:20px}
/* ---------- мобильное меню: панель поверх страницы ---------- */
.mfon{position:fixed;top:var(--shapka-m,58px);left:0;right:0;bottom:0;z-index:88;background:rgba(8,7,10,.66);backdrop-filter:blur(3px);
  opacity:0;transition:opacity .24s ease}
.mfon.vidno{opacity:1}
.mob{position:fixed;top:var(--shapka-m,58px);right:0;bottom:0;z-index:90;width:min(94vw,430px);
  background:linear-gradient(180deg,#171320 0%,#12101a 100%);border-left:1px solid var(--line);
  box-shadow:-24px 0 60px rgba(0,0,0,.6);display:flex;flex-direction:column;
  transform:translateX(102%);visibility:hidden;
  transition:transform .28s cubic-bezier(.22,.7,.2,1),visibility .28s;
  overscroll-behavior:contain}
.mob.open{transform:translateX(0);visibility:visible}
.mverh{display:flex;align-items:center;justify-content:space-between;padding:20px 22px 16px;
  border-bottom:1px solid var(--line);flex:0 0 auto}
.mverh span{font-family:var(--zag);font-size:20px;color:#F3EDE3;letter-spacing:.4px}
.mzakryt{width:42px;height:42px;display:grid;place-items:center;border-radius:12px;
  border:1px solid var(--line);background:rgba(255,255,255,.03);color:#E9E3DA}
.mzakryt svg{width:20px;height:20px}
.mspisok{flex:1 1 auto;overflow-y:auto;-webkit-overflow-scrolling:touch;padding:8px 0 6px}
.mgruppa{border-bottom:1px solid rgba(232,226,217,.08)}
.mstroka{display:flex;align-items:center;justify-content:space-between;gap:6px}
.mstroka>a{flex:1 1 auto;display:block;padding:16px 10px 16px 22px;
  font-family:var(--anons);font-size:19.5px;letter-spacing:.4px;color:#EDE6DC}
.mstroka.on>a{color:var(--zoloto-svet)}
.mrask{flex:0 0 auto;width:54px;height:54px;display:grid;place-items:center;margin-right:8px;
  border-radius:12px;border:1px solid rgba(201,162,39,.28);background:rgba(201,162,39,.07);
  color:var(--zoloto)}
.mrask svg{width:20px;height:20px;transition:transform .24s ease}
.mgruppa.raskryt .mrask svg{transform:rotate(180deg)}
.mpod{display:grid;grid-template-rows:0fr;transition:grid-template-rows .26s ease}
.mgruppa.raskryt .mpod{grid-template-rows:1fr}
.mpod-in{overflow:hidden;min-height:0}
.mniz{flex:0 0 auto;padding:16px 22px calc(18px + env(safe-area-inset-bottom));
  border-top:1px solid var(--line)}
.mniz .btn{width:100%;justify-content:center;padding:16px 20px;font-size:16px}
.burger{position:relative}
.burger .bl{position:absolute;left:11px;width:20px;height:1.7px;border-radius:2px;background:currentColor;
  transition:transform .24s ease,opacity .18s ease}
.burger .bl:nth-child(1){top:14px}
.burger .bl:nth-child(2){top:20px}
.burger .bl:nth-child(3){top:26px}
.burger.krest .bl:nth-child(1){transform:translateY(6px) rotate(45deg)}
.burger.krest .bl:nth-child(2){opacity:0}
.burger.krest .bl:nth-child(3){transform:translateY(-6px) rotate(-45deg)}
@media(max-width:1120px){
  .nav{display:none}.burger{display:flex}
  /* шапка липнет к самому верху и не съедает экран.
     Размытие убрано намеренно: оно делает шапку точкой отсчёта и схлопывает панель меню. */
  .shapka{background:#100E15;backdrop-filter:none;-webkit-backdrop-filter:none}
  .shapka .in{height:var(--shapka-m,58px);padding:0 14px;gap:12px}
  .znak{font-size:18.5px;gap:9px}
  .znak svg{width:22px;height:22px}
  .burger{width:42px;height:42px;margin-left:auto}
}
@media(hover:hover){.nav a:hover{color:var(--zoloto-svet)}}

/* ---------- выпадающее подменю ---------- */
.hasmega{position:relative}
.hasmega>a{display:inline-flex;align-items:center;gap:6px}
.hasmega>a svg{width:12px;height:12px;opacity:.55;transition:transform .18s;flex:none}
.pod{position:absolute;left:-14px;top:100%;padding-top:12px;display:none;z-index:70}
.pod-in{background:#181420;border:1px solid var(--line);border-top:2px solid var(--zoloto);
  border-radius:0 0 14px 14px;padding:8px;min-width:236px;
  box-shadow:0 22px 50px rgba(0,0,0,.55)}
.pod-in{min-width:268px}
.pod-in a{display:flex;align-items:center;gap:12px;padding:10px 14px;border-radius:10px;
  font-family:var(--sans);font-size:15px;letter-spacing:0;color:#CFC7BC;white-space:nowrap;
  transition:background .18s ease,color .18s ease}
.pod-in a svg.mi{flex:0 0 34px;width:34px;height:34px;padding:6px;border-radius:9px;
  color:var(--zoloto);background:rgba(201,162,39,.07);border:1px solid rgba(201,162,39,.22);
  transition:background .2s ease,border-color .2s ease,transform .2s ease}
@media(hover:hover){
  .hasmega:hover .pod,.hasmega:focus-within .pod{display:block}
  .hasmega:hover>a svg{transform:rotate(180deg)}
  .pod-in a:hover{background:rgba(201,162,39,.1);color:var(--zoloto-svet)}
  .pod-in a:hover svg.mi{background:rgba(201,162,39,.18);border-color:rgba(201,162,39,.5);
    transform:translateY(-1px)}
}
@media(max-width:1120px){.pod{display:none!important}}
.mob a.sub{display:flex;align-items:center;gap:13px;padding:13px 22px 13px 22px;font-size:16.5px;
  color:#C3BBAF;background:rgba(255,255,255,.02);
  border-top:1px solid rgba(232,226,217,.06)}
.mob a.sub svg.mi{flex:0 0 32px;width:32px;height:32px;padding:6px;border-radius:9px;
  color:var(--zoloto);background:rgba(201,162,39,.07);border:1px solid rgba(201,162,39,.22)}

/* ---------- кнопки ---------- */
.btn{display:inline-flex;align-items:center;gap:9px;position:relative;text-wrap:balance;
  overflow-wrap:break-word;
  padding:14px 24px;border-radius:var(--r);font-size:15px;font-weight:600;
  border:1px solid transparent;min-height:48px;transition:transform .12s,background .18s}
.btn::after{content:"";position:absolute;top:7px;right:7px;width:9px;height:9px;
  border-top:1.5px solid currentColor;border-right:1.5px solid currentColor;opacity:.5}
.btn-gold{background:var(--zoloto);color:#151009}
.btn-gold::after{display:none}
.btn-ghost{border-color:rgba(232,226,217,.28);color:var(--tekst)}
.btn:active{transform:scale(.985)}
@media(hover:hover){.btn-gold:hover{background:var(--zoloto-svet)}
  .btn-ghost:hover{border-color:var(--zoloto);color:var(--zoloto-svet)}}
.knopki{display:flex;flex-wrap:wrap;gap:14px;margin-top:30px}

/* ---------- герой: текст слева, портрет справа ---------- */
.hero{position:relative;padding:0;border:0;overflow:clip;min-height:clamp(480px,64vh,660px);
  display:flex;align-items:center}
.hero .fon{position:absolute;inset:0;overflow:hidden;contain:paint}
.hero .fon picture{display:block;width:100%;height:100%}
.hero .fon img{width:100%;height:100%;object-fit:cover;object-position:50% 50%;opacity:.95}
.hero .fon::after{content:"";position:absolute;inset:0;background:
  linear-gradient(90deg,rgba(14,12,17,.92) 0%,rgba(14,12,17,.78) 34%,rgba(14,12,17,.2) 58%,rgba(14,12,17,0) 74%),
  linear-gradient(180deg,rgba(14,12,17,.35) 0%,rgba(14,12,17,0) 30%,rgba(14,12,17,.55) 88%,var(--noch) 100%)}
.hero .in{position:relative;z-index:5;width:100%;padding:60px 0 64px}
.hero .ryad{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.72fr);gap:56px;align-items:center}
.hero .in>.wrap>*{max-width:620px}
.hero h1{max-width:780px}
.hero p.lid{color:#DCD5CA}
.hero .eyebrow{text-shadow:0 2px 10px rgba(10,8,12,.85),0 0 26px rgba(10,8,12,.7)}
.hero .portret{position:relative;border-radius:20px;overflow:hidden;border:1px solid rgba(201,162,39,.35);
  aspect-ratio:4/5;box-shadow:0 30px 70px rgba(0,0,0,.55)}
.hero .portret img{width:100%;height:100%;object-fit:cover;object-position:50% 22%;display:block}
.hero .portret::after{content:"";position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(14,12,17,0) 55%,rgba(14,12,17,.55) 100%)}
@media(max-width:1000px){
  .hero .ryad{grid-template-columns:1fr!important;gap:26px}
  .hero .portret{aspect-ratio:5/4;max-height:420px;order:-1}
  .hero .portret img{object-position:50% 18%}
  .hero{display:block;min-height:0}
  .hero .fon{position:relative;height:clamp(230px,42vh,340px);border-radius:0}
  .hero .fon img{object-position:50% 32%;opacity:1}
  .hero .in{padding:24px 0 34px}
  .hero .fon::after{background:
    linear-gradient(180deg,rgba(14,12,17,.1) 0%,rgba(14,12,17,0) 42%,rgba(14,12,17,.72) 86%,var(--noch) 100%)}

}

/* ---------- лента шагов ---------- */
.stepline{margin:34px 0 0;padding:0;list-style:none;border-top:1px solid var(--line)}
.stepline li{display:flex;gap:20px;align-items:flex-start;padding:22px 0;border-bottom:1px solid var(--line)}

.stepline .nom{width:60px;flex:none;display:flex;align-items:center;justify-content:center;
  margin-top:2px}
.stepline .nom svg.rn{display:block}
.stepline .txt{max-width:760px}
.stepline h3{margin:0 0 6px}
.stepline p{margin:0;color:var(--tihiy);font-size:16px;text-wrap:pretty}
.stepline svg{color:var(--zoloto);margin-top:4px}

/* ---------- сетки карточек ---------- */
.grid2,.grid3{display:grid;gap:20px;margin-top:34px}
.grid2{grid-template-columns:repeat(2,minmax(0,1fr))}
.grid3{grid-template-columns:repeat(3,minmax(0,1fr))}
.card{background:var(--sloy);border:1px solid var(--line);border-radius:18px;padding:26px;
  display:flex;flex-direction:column;transition:border-color .18s,transform .18s}
.card>svg{color:var(--zoloto);margin-bottom:14px}
.card p.more svg{margin:0;vertical-align:-3px;color:var(--zoloto-svet)}
.card h3{margin:0 0 10px}
.card p{color:var(--tihiy);font-size:16px;margin:0 0 14px;text-wrap:pretty}
.card p.more{margin-top:auto;margin-bottom:0;font-size:14.5px;color:var(--zoloto-svet);font-weight:600}
@media(hover:hover){a.card:hover{border-color:rgba(201,162,39,.55);transform:translateY(-2px)}}

/* ---------- карточка с кадром ---------- */
.kadr{border-radius:18px;overflow:hidden;border:1px solid var(--line);background:var(--sloy)}
.kadr .ph{aspect-ratio:16/9;overflow:hidden}
.kadr .ph[style*='aspect-ratio']{aspect-ratio:unset}
.kadr.art-kadr{border-radius:18px}
.kadr .ph img{width:100%;height:100%;object-fit:cover}
.kadr .body{padding:22px 24px 26px}
.kadr h3{margin:0 0 9px}
.kadr p{color:var(--tihiy);font-size:15.5px;margin:0}
.metka{display:inline-block;font-family:var(--anons);font-size:13px;letter-spacing:2px;text-transform:uppercase;
  color:var(--zoloto);border:1px solid rgba(201,162,39,.4);border-radius:999px;padding:4px 11px;margin-bottom:12px}

/* ---------- карточка-приглашение в сетке ---------- */
.zov{border:1px solid rgba(201,162,39,.42);background:linear-gradient(160deg,rgba(201,162,39,.09),rgba(22,19,28,.9));
  border-radius:18px;padding:26px;display:flex;flex-direction:column;justify-content:center;gap:2px;min-height:220px}
.zov>svg{color:var(--zoloto);margin-bottom:14px}
.zov span.more svg{margin:0;vertical-align:-3px}
.zov h3{margin:0 0 8px}
.zov p{color:var(--tihiy);font-size:15.5px;margin:0 0 14px;text-wrap:pretty}
.zov span.more{margin-top:14px;font-size:14.5px;color:var(--zoloto-svet);font-weight:600}
@media(hover:hover){a.zov:hover{border-color:var(--zoloto)}}

/* ---------- сплит ---------- */
.split{display:flex;gap:52px;align-items:stretch;margin-top:36px;max-width:100%}
.split>*:first-child{flex:1 1 auto;min-width:0;display:flex;flex-direction:column}
.split>*:first-child>*:last-child{margin-bottom:0}
/* Ширину кадра считает site.js по высоте текста рядом: кадр держит свою пропорцию,
   стоит целиком и низом сходится с текстом. До счёта работает запасная доля. */
.split .ph{flex:0 0 auto;position:relative;width:var(--shirina,42%);height:auto;
  min-width:300px;max-width:min(56%,640px);
  border-radius:18px;overflow:hidden;border:1px solid var(--line);background:#0E0C11}
.split .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  object-position:50% 50%;display:block}
.split .ph.shirokij{width:var(--shirina,52%)}
.split .ph.plyvet{position:sticky;top:96px}
.split .dlist{margin-top:0}
.stolb{flex:0 0 auto;align-self:stretch;display:flex;flex-direction:column;gap:16px;
  width:var(--shirina,42%);min-width:300px;max-width:min(56%,640px)}
.stolb .ph{width:100%;max-width:100%;min-width:0}
.dobivka{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:6px;
  border:1px solid rgba(201,162,39,.34);border-radius:18px;padding:22px 24px;min-height:132px;
  background:linear-gradient(158deg,rgba(201,162,39,.1),rgba(22,19,28,.92))}
.dobivka>svg{color:var(--zoloto);width:30px;height:30px;margin-bottom:6px}
.dobivka b{font-family:var(--zag);font-size:clamp(30px,3.2vw,42px);color:var(--zoloto-svet);line-height:1}
.dobivka p{margin:2px 0 0;color:var(--tihiy);font-size:15.5px;text-wrap:pretty}
.dobivka .dob-link{margin-top:12px;display:inline-flex;align-items:center;gap:8px;
  font-size:14.5px;font-weight:600;color:var(--zoloto-svet)}
.dobivka .dob-link svg{width:18px;height:18px}
@media(hover:hover){.dobivka .dob-link:hover{gap:12px}}
@media(max-width:860px){.stolb{width:100%!important;max-width:100%}}
.split>*:first-child{display:flex;flex-direction:column}
.split>*:first-child>*:last-child{margin-bottom:0}
.split.shir .ph{aspect-ratio:auto}

/* ---------- цифры ---------- */
.nails{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;margin-top:34px}
.nail{border-left:2px solid var(--zoloto);padding:4px 0 4px 18px}
.nail b{display:block;font-family:var(--serif);font-size:40px;color:#F3EDE3;line-height:1;font-weight:400}
.nail span{display:block;margin-top:9px;color:var(--tihiy);font-size:15px}

/* ---------- тёмная лента пунктов ---------- */
.dlist{background:var(--sloy2);border:1px solid var(--line);border-radius:20px;padding:34px;margin-top:34px}
.dlist ul{list-style:none;margin:0;padding:0;display:grid;gap:16px}
.dlist li{display:flex;gap:14px;align-items:flex-start;font-size:16.5px;text-wrap:pretty}
.dlist svg{color:var(--zoloto);margin-top:3px}

/* ---------- текст с врезкой ---------- */
.tside{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:56px;align-items:start;margin-top:30px}
.tside>.col>*{max-width:680px}
.side{position:sticky;top:96px;background:var(--sloy);border:1px solid var(--line);
  border-radius:16px;padding:24px}
.side .cifra{font-family:var(--serif);font-size:34px;color:var(--zoloto-svet);line-height:1;text-wrap:balance}
.side p{font-size:15px;color:var(--tihiy);margin:12px 0 0}
.side h4{font-size:19px;margin:0 0 10px}

/* ---------- статья ---------- */
.art h2{margin:44px 0 14px}
.art h2:first-of-type{margin-top:30px}
.art p{max-width:var(--uzko)}
.art .vrez{border-left:2px solid var(--zoloto);padding:2px 0 2px 20px;margin:26px 0;
  font-family:var(--serif);font-size:23px;line-height:1.34;color:#F0E9DE;max-width:640px;
  text-wrap:balance}

/* ---------- журнальная статья ---------- */
.podzag{font-size:21px;line-height:1.5;color:var(--tihiy);max-width:640px;margin:14px 0 0;
  font-family:var(--anons)}
.art-kadr .ph{width:100%;height:auto;max-height:min(72vh,620px)}
.art-kadr .ph img{object-fit:cover}
.art .lead{font-size:20.5px;line-height:1.6;color:#DCD5CA;max-width:var(--uzko);text-wrap:pretty}
.art .lead.drop::first-letter{float:left;font-family:var(--serif);font-weight:400;font-size:78px;
  line-height:.76;padding:10px 16px 0 0;color:var(--zoloto)}
.byline{display:flex;flex-wrap:wrap;align-items:center;gap:6px 18px;margin:24px 0 32px;padding:13px 0;
  border-top:1px solid var(--line);border-bottom:1px solid var(--line);font-size:12px;font-weight:600;
  letter-spacing:.11em;text-transform:uppercase;color:var(--tihiy);max-width:var(--uzko)}
.byline b{color:#F0E9DE;text-transform:none;letter-spacing:.2px;font-size:16px;
  font-family:var(--anons);font-weight:400}
.byline .dot{width:4px;height:4px;border-radius:50%;background:rgba(201,162,39,.65);flex:none}
.byline .tag{color:var(--zoloto)}
.korotko{background:var(--sloy);border:1px solid var(--line);border-left:3px solid var(--zoloto);
  border-radius:14px;padding:24px 26px;margin:0 0 28px;max-width:var(--uzko)}
.korotko b{display:block;font-family:var(--anons);font-size:14px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--zoloto);margin-bottom:14px;font-weight:400}
.korotko ul{list-style:none;margin:0;padding:0}
.korotko li{position:relative;padding-left:24px;margin-bottom:11px;font-size:16.5px;line-height:1.55;
  color:#D6CFC5;text-wrap:pretty}
.korotko li:last-child{margin-bottom:0}
.korotko li::before{content:"";position:absolute;left:2px;top:9px;width:7px;height:7px;
  border-radius:50%;background:var(--zoloto)}
.toc{border:1px solid var(--line);border-radius:14px;padding:0;margin:0 0 34px;background:var(--sloy);
  max-width:var(--uzko);overflow:hidden}
.toc summary{cursor:pointer;list-style:none;padding:17px 24px;font-family:var(--anons);font-size:14px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--tihiy);display:flex;justify-content:space-between;
  align-items:center;gap:14px}
.toc summary::-webkit-details-marker{display:none}
.toc summary::after{content:"+";color:var(--zoloto);font-size:22px;line-height:1;font-weight:400}
.toc[open] summary::after{content:"–"}
.toc ol{margin:0;padding:0 24px 20px 42px;color:var(--tihiy)}
.toc li{margin-bottom:9px;font-size:16px;line-height:1.45}
.toc a{color:#CFC7BC;border-bottom:1px solid transparent}
@media(hover:hover){.toc a:hover{color:var(--zoloto-svet);border-bottom-color:rgba(201,162,39,.45)}}
.istok{border-top:1px solid var(--line);margin:44px 0 0;padding-top:24px;max-width:var(--uzko)}
.istok b{display:block;font-family:var(--anons);font-size:14px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--tihiy);margin-bottom:12px;font-weight:400}
.istok p{font-size:15px;line-height:1.6;color:var(--tihiy);margin:0}
.sosedi{display:flex;flex-wrap:wrap;gap:14px;margin-top:34px;max-width:var(--uzko)}
.sosedi a{flex:1 1 260px;border:1px solid var(--line);border-radius:14px;padding:18px 20px;
  background:var(--sloy)}
.sosedi span{display:block;font-family:var(--anons);font-size:13.5px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--zoloto);margin-bottom:7px}
.sosedi b{font-family:var(--serif);font-size:19px;color:#F0E9DE;font-weight:400}
@media(hover:hover){.sosedi a:hover{border-color:rgba(201,162,39,.5)}}
@media(max-width:640px){
  .art .lead.drop::first-letter{font-size:58px;padding:6px 12px 0 0}
  .byline{gap:5px 13px;font-size:11px;letter-spacing:.09em;margin:18px 0 24px}
  .byline b{font-size:13.5px}
  .korotko,.toc summary{padding-left:20px;padding-right:20px}
}

/* ---------- живые искры в шапке ---------- */
.hero .fon{overflow:hidden}
canvas.iskry{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:4;
  mix-blend-mode:screen}
.hero .fon::after{z-index:2}
.hero .fon img{will-change:transform;transform:scale(1.06)}

/* ---------- переворот карты в вопроснике ---------- */
@media (prefers-reduced-motion: no-preference){
  .kviz-karta.perevorot{animation:perevorot .9s cubic-bezier(.2,.7,.2,1) both;
    transform-style:preserve-3d;perspective:900px}
  @keyframes perevorot{
    0%{transform:rotateY(96deg) scale(.9);opacity:0;filter:brightness(.4)}
    60%{filter:brightness(1.25)}
    100%{transform:none;opacity:1;filter:none}
  }
  .kviz-otvet{transition:border-color .16s,transform .12s,background .2s}
}

/* ---------- золото дышит ---------- */
@media (prefers-reduced-motion: no-preference){
  .znak svg{animation:teplo 5.5s ease-in-out infinite}
  @keyframes teplo{0%,100%{opacity:1}50%{opacity:.72}}
}

/* ---------- мягкое появление ---------- */
@media (prefers-reduced-motion: no-preference){
  .poyav{opacity:0;transform:translateY(14px);transition:opacity .5s ease,transform .5s ease}
  .poyav.vidno{opacity:1;transform:none}
  .hero .poyav{opacity:1!important;transform:none!important}
}

/* ---------- разделитель секций ---------- */
section + section > .wrap::before{content:"✦";position:absolute;left:50%;transform:translateX(-50%);
  margin-top:-52px;color:rgba(201,162,39,.5);font-size:13px;letter-spacing:6px}
section > .wrap{position:relative}

/* ---------- галерея карт колоды ---------- */
.galereya{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:30px}
.gk{margin:0;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:var(--sloy)}
.gk img{width:100%;height:auto;display:block}
@media(max-width:640px){.galereya{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:10px}}

/* ---------- словарь ---------- */
.slovar{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:34px}
.slovo{background:var(--sloy);border:1px solid var(--line);border-left:2px solid var(--zoloto);
  border-radius:14px;padding:20px 22px}
.slovo b{display:block;font-family:var(--serif);font-weight:400;font-size:22px;color:#F0E9DE;
  margin-bottom:8px}
.slovo p{margin:0;color:var(--tihiy);font-size:15.5px;line-height:1.6;text-wrap:pretty}
@media(max-width:900px){.slovar{grid-template-columns:1fr!important}}

/* ---------- вопросник: вопросы слева, живой веер карт справа ---------- */
.kviz{--kw:140px;--veer-h:400px;--ugol:1;
  background:linear-gradient(150deg,rgba(30,26,40,.92),rgba(21,18,27,.94));
  border:1px solid var(--line);border-radius:22px;padding:34px 36px;position:relative;
  overflow:hidden}
.kviz::before{content:"";position:absolute;right:-120px;top:-140px;width:460px;height:460px;
  background:radial-gradient(circle,rgba(201,162,39,.13),transparent 66%);pointer-events:none}
.kviz-telo{display:grid;grid-template-columns:minmax(0,1fr) minmax(300px,392px);gap:36px;
  align-items:center;position:relative;z-index:2}
.kviz-telo[hidden]{display:none}
.kviz-levo{min-width:0}
.kviz-shag{display:flex;align-items:center;gap:18px;margin-bottom:20px;flex-wrap:wrap}
.kviz-nomer{font-family:var(--anons);font-size:13.5px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--zoloto);white-space:nowrap}
.kviz-luny{display:flex;gap:10px;align-items:center}
.kviz-luny i{width:14px;height:14px;border-radius:50%;position:relative;overflow:hidden;
  border:1px solid rgba(201,162,39,.4);background:rgba(232,226,217,.05);flex:none}
.kviz-luny i::after{content:"";position:absolute;inset:-1px;border-radius:50%;
  background:var(--zoloto);transform:translateX(-102%);transition:transform .45s ease}
.kviz-luny i.est::after{transform:none}
.kviz-luny i.tut{border-color:var(--zoloto-svet);box-shadow:0 0 0 3px rgba(201,162,39,.14)}
.kviz-luny i.tut::after{transform:translateX(-56%)}
.kviz-vopros{font-size:clamp(23px,2.7vw,32px);margin:0 0 20px;min-height:2.3em;
  display:flex;align-items:flex-end}
.kviz-otvety{display:grid;gap:12px}
.kviz-otvet{text-align:left;font:inherit;font-size:16.5px;color:#DCD5CA;background:var(--sloy2);
  border:1px solid var(--line);border-radius:14px;padding:16px 20px;cursor:pointer;
  transition:border-color .16s,transform .12s,background .2s;min-height:52px}
.kviz-otvet:active{transform:scale(.995)}
@media(hover:hover){.kviz-otvet:hover{border-color:rgba(201,162,39,.55);color:#F0E9DE;
  background:rgba(201,162,39,.06)}}
.kviz.zhdyom .kviz-otvety{pointer-events:none;opacity:.5;transition:opacity .2s}
.kviz-snoska{margin:18px 0 0;font-size:13.5px;color:var(--tihiy);line-height:1.55}
.kviz button.btn-ghost{background:transparent}

/* веер: шесть рубашек, каждая переворачивается на своём ответе */
.kviz-veer{position:relative;height:var(--veer-h);min-width:0}
.kviz-veer::before{content:"";position:absolute;left:50%;top:50%;width:320px;height:320px;
  margin:-160px 0 0 -160px;border-radius:50%;pointer-events:none;
  background:radial-gradient(circle,rgba(201,162,39,.15),transparent 68%)}
.veer-k{position:absolute;left:50%;top:50%;width:var(--kw);
  margin-left:calc(var(--kw) / -2);margin-top:calc(var(--kw) * -0.8);
  transform-origin:50% 132%;transform:rotate(calc(var(--rot) * var(--ugol)));
  transition:transform .45s cubic-bezier(.2,.7,.2,1),filter .3s ease;
  perspective:900px}
.veer-in{position:relative;width:100%;aspect-ratio:184/268;transform-style:preserve-3d;
  transition:transform .85s cubic-bezier(.2,.7,.2,1)}
.veer-k.otkryta .veer-in{transform:rotateY(180deg)}
.veer-storona{position:absolute;inset:0;border-radius:12px;overflow:hidden;
  backface-visibility:hidden;-webkit-backface-visibility:hidden;
  box-shadow:0 16px 34px rgba(0,0,0,.5)}
.veer-bok{background:linear-gradient(140deg,rgba(201,162,39,.1),transparent 58%)}
.veer-lico{transform:rotateY(180deg)}
.veer-storona svg{width:100%;height:100%;display:block}
.veer-k.tut{transform:rotate(calc(var(--rot) * var(--ugol))) translateY(-14px);
  filter:drop-shadow(0 0 16px rgba(201,162,39,.4))}
/* открытая карта выходит из веера вперёд, чтобы её было видно целиком */
.veer-k.vpered{z-index:30;transform:rotate(0deg) translateY(-10px) scale(1.07);
  filter:drop-shadow(0 20px 38px rgba(0,0,0,.6)) drop-shadow(0 0 24px rgba(201,162,39,.28))}
.veer-k.vpered .veer-storona{box-shadow:0 18px 40px rgba(0,0,0,.55)}

/* результат: разворот с крупной картой */
.kviz-itog{display:grid;grid-template-columns:278px minmax(0,1fr);gap:44px;align-items:center;
  position:relative;z-index:2;max-width:1000px;margin:0 auto}
.kviz-itog[hidden]{display:none}
.itog-karta{filter:drop-shadow(0 24px 48px rgba(0,0,0,.6))}
.itog-karta svg.ark{width:100%;height:auto;display:block}
.itog-txt{min-width:0}
.itog-txt h3{font-size:clamp(30px,4vw,46px);margin:2px 0 14px}
.itog-smysl{color:var(--tihiy);font-size:17.5px;margin:0 0 20px;max-width:58ch}
.itog-klyuchi{list-style:none;display:flex;flex-wrap:wrap;gap:8px;padding:0;margin:0}
.itog-klyuchi li{font-family:var(--anons);font-size:15px;letter-spacing:.03em;
  color:var(--zoloto-svet);border:1px solid rgba(201,162,39,.32);
  background:rgba(201,162,39,.07);border-radius:999px;padding:5px 14px}
.itog-ryad{grid-column:1 / -1;border-top:1px solid var(--line);padding-top:20px;margin-top:4px}
.itog-podpis{font-family:var(--anons);font-size:12.5px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--tihiy);margin:0 0 12px}
.itog-mini{display:flex;gap:12px;flex-wrap:wrap}
.itog-mini .mini{width:62px;display:block;border-radius:8px;overflow:hidden;opacity:.85}
.itog-mini svg.ark{width:100%;height:auto;display:block}
.itog-mini svg.ark text{display:none}

@media (prefers-reduced-motion: reduce){
  .veer-k,.veer-in,.kviz-luny i::after,.kviz-otvet{transition:none}
}
@media(max-width:980px){
  .kviz{--kw:118px;--veer-h:250px;--ugol:.86}
  .kviz-telo{grid-template-columns:1fr!important;gap:26px}
  .kviz-veer{order:-1}
  .kviz-vopros{min-height:0;display:block}
  .kviz-itog{grid-template-columns:1fr!important;gap:24px;justify-items:start}
  .itog-karta{max-width:210px;margin:0 auto}
}
@media(max-width:640px){
  .kviz{padding:24px 18px;border-radius:18px;--kw:100px;--veer-h:218px}
  .kviz-veer::before{width:230px;height:230px;margin:-115px 0 0 -115px}
  .kviz-otvet{font-size:16px;padding:15px 17px}
  .itog-karta{max-width:180px}
  .itog-mini .mini{width:48px}
  .kviz-itog .knopki{width:100%}
}

/* ---------- справочник арканов ---------- */
.ark-grid{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:20px;margin-top:34px}
.ark-k{display:block;transition:transform .18s}
.ark-k .ph{position:relative;border-radius:14px;overflow:hidden;border:1px solid var(--line);
  background:#0E0C11;box-shadow:0 14px 30px rgba(0,0,0,.42);transition:border-color .18s}
.ark-k .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.ark-p{display:flex;flex-direction:column;align-items:center;gap:3px;margin-top:11px;
  font-size:15px;line-height:1.3;color:#E4DDD2;text-align:center;text-wrap:balance}
.ark-p b{font-family:var(--anons);font-weight:400;font-size:12.5px;letter-spacing:.2em;
  color:var(--zoloto)}
@media(hover:hover){.ark-k:hover{transform:translateY(-4px)}
  .ark-k:hover .ph{border-color:rgba(201,162,39,.62)}}
.ark-istochnik{margin:26px 0 0;color:var(--tihiy);font-size:14.5px;text-wrap:pretty}
/* Разворот аркана: слева карта, справа значения. Ширину карты подбирает site.js
   по высоте соседней колонки, поэтому низ разворота сходится.
   На узком экране .split встаёт колонкой, и order поднимает карту наверх. */
.ark-verh{margin-top:30px;align-items:flex-start}
.ark-verh .ph{order:-1;border-color:rgba(201,162,39,.3);box-shadow:0 34px 72px rgba(0,0,0,.55)}
.ark-znach>.lid{margin-top:0}
.ark-blok{margin-top:32px}
.ark-blok h3{margin:0;color:var(--zoloto-svet)}
.ark-blok .dlist{margin-top:16px}
.ark-sovet{margin:14px 0 0;color:var(--tihiy);font-size:16.5px}
@media(max-width:1000px){.ark-grid{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media(max-width:640px){.ark-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:14px}
  .ark-p{font-size:14px}.ark-verh{margin-top:24px}.ark-blok{margin-top:26px}}

/* ---------- инфографика ---------- */
.shema{margin:36px 0 0;padding:26px 24px 20px;background:var(--sloy);border:1px solid var(--line);
  border-radius:20px;overflow-x:auto}
.shema svg{width:100%;height:auto;min-width:640px;display:block}
.shema-podpis{margin:18px 0 0;color:var(--tihiy);font-size:15px;line-height:1.6;max-width:720px;
  text-wrap:pretty}
@media(max-width:640px){.shema{padding:18px 14px 14px;border-radius:16px}
  .shema svg{min-width:560px}.shema-podpis{font-size:14px}}

/* ---------- плашки-ссылки ---------- */
.razdely{margin-top:40px;padding-top:32px;border-top:1px solid var(--line)}
.plashki{display:grid;grid-template-columns:repeat(auto-fill,minmax(252px,1fr));
  gap:12px;margin-top:18px}
/* Разделы стоят ровной сеткой: одинаковая высота, кадр слева, подпись под именем.
   Раньше это была россыпь плашек разной ширины и рваными рядами. */
.razdel{display:grid;grid-template-columns:56px minmax(0,1fr);align-items:center;gap:13px;
  padding:10px 14px 10px 10px;border:1px solid var(--line);border-radius:14px;
  background:var(--sloy);height:80px;transition:border-color .18s ease,transform .18s ease}
.razdel .rk{width:56px;height:56px;border-radius:10px;overflow:hidden;position:relative;
  border:1px solid rgba(201,162,39,.22);flex:0 0 56px}
.razdel .rk img{width:100%;height:100%;object-fit:cover;display:block}
.razdel .rt{display:flex;flex-direction:column;gap:3px;min-width:0}
.razdel .rt b{font-family:var(--anons);font-size:16.5px;font-weight:400;color:#EDE6DC;
  letter-spacing:.3px;line-height:1.2;overflow-wrap:normal;white-space:nowrap;
  overflow:hidden;text-overflow:ellipsis}
.razdel .rt i{font-style:normal;font-size:13px;color:#918878;line-height:1.3;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
@media(hover:hover){.razdel:hover{border-color:rgba(201,162,39,.5);transform:translateY(-2px)}
  .razdel:hover .rt b{color:var(--zoloto-svet)}}
@media(max-width:560px){.plashki{grid-template-columns:1fr}}
.plashka{display:inline-flex;align-items:center;gap:8px;padding:10px 16px;border:1px solid var(--line);
  border-radius:11px;background:var(--sloy);font-size:14.5px;color:#CFC7BC}
@media(hover:hover){.plashka:hover{border-color:rgba(201,162,39,.5);color:var(--zoloto-svet)}}

/* ---------- финал ---------- */
.final{background:var(--sloy2);border:1px solid var(--line);border-radius:22px;padding:44px;
  display:grid;grid-template-columns:minmax(0,1fr) 280px;gap:48px;align-items:start}
.final .fside{border-left:2px solid var(--zoloto);padding:2px 0 2px 18px}
.final .fside b{display:block;font-family:var(--serif);font-size:25px;color:#F3EDE3;line-height:1.15;
  font-weight:400;text-wrap:balance}
.final .fside span{display:block;margin-top:10px;color:var(--tihiy);font-size:15px}
.final h2{margin:0 0 14px}
.final p{color:#D2CAC0;max-width:640px}

/* ---------- вопросы ---------- */
.vopros{border-bottom:1px solid var(--line)}
.vopros summary{cursor:pointer;list-style:none;padding:20px 0;display:flex;gap:16px;
  align-items:flex-start;font-family:var(--serif);font-size:21px;color:#F0E9DE;
  max-width:760px;justify-content:space-between}
.vopros summary>span{flex:1}
.vopros summary::-webkit-details-marker{display:none}
.vopros summary svg{color:var(--zoloto);margin-top:6px;transition:transform .2s;flex:none}
.vopros[open] summary svg{transform:rotate(90deg)}
.vopros .otvet{padding:0 0 22px 38px;max-width:720px}
.vopros .otvet p{margin:0 0 12px;color:var(--tihiy);font-size:16.5px}
.vopros .otvet p:first-child strong{color:var(--tekst)}

/* ---------- подвал ---------- */
.podval{border-top:1px solid var(--line);background:#0B0910;padding:56px 0 40px;margin-top:20px}
.podval .kol{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1.4fr);gap:44px}
.podval h4{font-family:var(--anons);font-size:14.5px;letter-spacing:3px;text-transform:uppercase;
  color:var(--zoloto);margin:0 0 16px}
.podval p{color:var(--tihiy);font-size:15px}
.niz{margin-top:38px;padding-top:22px;border-top:1px solid var(--line);
  display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between;color:#7E7669;font-size:13.5px}
.niz a{color:#7E7669}
.soc{display:flex;gap:10px;margin-top:18px}

/* ---------- хлебные крошки ---------- */
.kroshki{font-size:13.5px;color:#7E7669;padding:22px 0 0}
.kroshki a{color:#9A9184}
.kroshki span{margin:0 7px}
.kroshki>span:last-child{white-space:nowrap;margin-right:0}

/* ---------- плавающая связь ---------- */
.plyv{position:fixed;right:20px;bottom:20px;z-index:70;display:inline-flex;align-items:center;gap:9px;
  padding:13px 18px;border-radius:14px;background:var(--zoloto);color:#151009;font-size:14.5px;
  font-weight:600;box-shadow:0 10px 30px rgba(0,0,0,.5);min-height:48px}
.plyv svg{width:19px;height:19px}
.plyv:active{transform:scale(.97)}
@media(hover:hover){.plyv:hover{background:var(--zoloto-svet)}}
@media(max-width:640px){
  .plyv{right:14px;bottom:14px;width:54px;height:54px;padding:0;border-radius:50%;
    justify-content:center;box-shadow:0 8px 24px rgba(0,0,0,.55)}
  .plyv span{display:none}
  .plyv svg{width:23px;height:23px}
}

/* ---------- мобильное ---------- */
@media(max-width:1000px){
  .split{flex-direction:column;gap:26px}
  /* на телефоне кадр идёт первым: иначе человек листает экран текста, прежде чем увидит фото */
  .split>.stolb,.split>.ph{order:-1}
  .split .ph,.split .stolb{width:100%!important;max-width:100%!important;min-width:0}
  .split .ph.plyvet{position:static}
  .split .ph{height:auto!important;min-height:0;position:relative}
  .split .ph img{position:absolute;inset:0}
  .dobivka{min-height:0}
  .final{grid-template-columns:1fr!important;gap:30px}
  .tside{grid-template-columns:1fr!important;gap:30px}
  .side{position:static}
  .nails{grid-template-columns:repeat(2,minmax(0,1fr))!important}
  .podval .kol{grid-template-columns:1fr!important;gap:32px}
}
@media(max-width:400px){h1{font-size:27px}h2{font-size:23px}.podzag{font-size:18px}}
@media(max-width:360px){.znak{font-size:17px;gap:8px}.znak svg{width:22px;height:22px}.shapka .in{gap:12px;padding:0 14px}.wrap{padding:0 14px}}
@media(max-width:640px){
  body{font-size:16.5px}
  .vopros summary{font-size:17.5px;padding-right:6px}
  .final{grid-template-columns:1fr!important;gap:26px}
  section{padding:54px 0}
  .grid2,.grid3{grid-template-columns:1fr!important;gap:16px}
  .nails{grid-template-columns:1fr!important}
  .final,.dlist{padding:26px 22px}
  .hero .in{padding:44px 0 46px}
  .wrap,.shapka .in{padding:0 18px}
  .stepline li{gap:14px}
  .knopki{gap:10px}
  .knopki .btn{flex:1 1 100%;justify-content:center}
  .knopki .btn::after{right:9px}
  .art .vrez{font-size:20px}
}
/* ---------- разрядка у крупных чисел ---------- */
/* В Prata пробел узкий, поэтому «6 направлений» читается как «6направлений». */
.nail b,.side .cifra,.dobivka b,.fside b,.cifra-big,.stat b,.kviz-nomer{word-spacing:.2em}

/* ---------- сетка без дыр ---------- */
/* Одинокая карточка в последнем ряду разворачивается лентой во всю ширину,
   пара занимает ряд без пустой ячейки. */
.grid3>a.kadr:last-child:nth-child(3n+1){grid-column:1 / -1;display:grid;
  grid-template-columns:minmax(0,.46fr) minmax(0,1fr);align-items:stretch}
.grid3>a.kadr:last-child:nth-child(3n+1) .ph{aspect-ratio:auto!important;height:100%}
.grid3>a.kadr:last-child:nth-child(3n+1) .body{display:flex;flex-direction:column;
  justify-content:center;padding:30px 34px}
.grid3>a.kadr:last-child:nth-child(3n+1) h3{font-size:clamp(24px,2.4vw,32px)}
.grid3>a.kadr:last-child:nth-child(3n+2){grid-column:span 2}
@media(max-width:860px){
  .grid3>a.kadr:last-child:nth-child(3n+1){grid-template-columns:1fr}
  .grid3>a.kadr:last-child:nth-child(3n+1) .ph{aspect-ratio:16/9!important;height:auto}
  .grid3>a.kadr:last-child:nth-child(3n+2){grid-column:auto}
}

/* ---------- карточка направления с кадром ---------- */
.card.s-foto{padding:0;overflow:hidden}
.card.s-foto .ph{position:relative;width:100%;aspect-ratio:16/9;overflow:hidden;border:0;border-radius:0}
.card.s-foto .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.card.s-foto .ph::after{content:"";position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(14,12,17,0) 45%,rgba(14,12,17,.78) 100%)}
.card.s-foto .tel{display:flex;flex-direction:column;flex:1 1 auto;padding:24px 26px 26px}
.card.s-foto .tel>svg{color:var(--zoloto);margin:-46px 0 14px;position:relative;z-index:2}
@media(hover:hover){.card.s-foto:hover .ph img{transform:scale(1.04);transition:transform .5s ease}}
.card.s-foto .ph img{transition:transform .5s ease}

/* ---------- схемы на телефоне: масштаб один к одному ---------- */
/* Схема шириной 1000 единиц ужималась до 560px, и подпись в 12,5px */
/* превращалась в 7px. Держим схему в натуральную величину: она листается */
/* вбок, зато читается без увеличения. */
@media(max-width:640px){
  .shema{position:relative}
  /* видно, что схема продолжается вправо, иначе человек думает, что она обрезана */
  .shema::after{content:"Схему можно листать\00a0вбок";display:block;margin:12px 0 0;
    font-size:13px;color:var(--zoloto-svet);letter-spacing:.04em;position:sticky;left:0;max-width:100%}
  .shema svg{min-width:820px}
  .shema{scroll-snap-type:x proximity;-webkit-overflow-scrolling:touch}
  /* подпись держится на месте, пока схему листают вбок */
  .shema-podpis{position:sticky;left:0;max-width:min(100%,720px)}
}


/* ---------- плавающая кнопка не спорит с открытым меню ---------- */
body:has(.mob.open) .plyv{opacity:0;pointer-events:none;transform:translateY(12px)}
.plyv{transition:opacity .2s ease,transform .2s ease}

/* ---------- лента шагов не растягивает страницу ---------- */
/* Без min-width:0 длинный заголовок с неразрывным пробелом распирает колонку,
   и на 360px последняя буква уезжает за край экрана. */
.stepline .txt,.stepline li>div{min-width:0}
.stepline h3{overflow-wrap:normal;word-break:normal;hyphens:none}
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Prata&family=Forum&family=Montserrat:wght@400;500;600&display=swap">')