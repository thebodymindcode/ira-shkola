# -*- coding: utf-8 -*-
"""Стили раздела «Библиотека»: конструкция статьи взята с базы знаний
thebodymindcode.ru и переложена на тёмную палитру школы Ирины."""

CSS_BAZA = """
/* ================= БИБЛИОТЕКА: лонгриды ================= */
.artgero{padding-top:22px;padding-bottom:0}
.artgero + section{padding-top:26px}
.article h1{margin-top:0}
.artgero .ph16{position:relative;width:100%;aspect-ratio:16/9;max-height:460px;overflow:hidden;
  border:1px solid var(--line);border-radius:20px}
.artgero .ph16 img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.artgero .ph16::after{content:"";position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(14,12,17,.2) 0%,rgba(14,12,17,0) 45%,rgba(14,12,17,.55) 100%)}
.article{max-width:820px;margin:0 auto;padding:0 24px}
.article p{font-size:17.5px;line-height:1.75;margin:0 0 18px;text-wrap:pretty}
.article h2{font-size:clamp(24px,3vw,34px);margin:44px 0 16px;scroll-margin-top:80px}
.article h3{font-size:clamp(19px,2.2vw,23px);margin:30px 0 12px}
.article ul,.article ol{margin:0 0 20px;padding-left:22px}
.article li{margin:0 0 10px;font-size:17px;line-height:1.7}
.article a{color:var(--zoloto-svet);text-decoration:underline;text-underline-offset:3px;
  text-decoration-color:rgba(201,162,39,.4)}

/* быстрый ответ */
.kb-tldr{border:1px solid rgba(201,162,39,.36);border-radius:18px;padding:24px 26px;margin:26px 0 30px;
  background:linear-gradient(158deg,rgba(201,162,39,.09),rgba(22,19,28,.9))}
.kb-tldr>b{display:block;font-family:var(--anons);font-size:14px;letter-spacing:3px;
  text-transform:uppercase;color:var(--zoloto);margin-bottom:14px}
.kb-tldr ul{margin:0;padding-left:20px}
.kb-tldr li{margin-bottom:9px;color:#DCD5CA}

/* оглавление */
.kb-toc{border:1px solid var(--line);border-radius:16px;padding:18px 22px;margin:0 0 30px;
  background:var(--sloy)}
.kb-toc>summary{cursor:pointer;font-family:var(--anons);font-size:17px;color:#F0E9DF;
  letter-spacing:.4px;list-style:none}
.kb-toc>summary::-webkit-details-marker{display:none}
.kb-toc>summary::after{content:"⌄";float:right;color:var(--zoloto);transition:transform .2s}
.kb-toc[open]>summary::after{transform:rotate(180deg);display:inline-block}
.kb-toc ol{margin:14px 0 0;padding-left:22px}
.kb-toc li{margin-bottom:7px;font-size:16px}
.kb-toc a{color:#CFC7BC;text-decoration:none}
@media(hover:hover){.kb-toc a:hover{color:var(--zoloto-svet)}}

/* три цифры */
.artstats{margin:26px 0 32px}
.artstats .stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.artstats .stat{border:1px solid var(--line);border-left:2px solid var(--zoloto);border-radius:12px;
  padding:16px 18px;background:var(--sloy)}
.artstats .stat b{display:block;font-family:var(--zag);font-size:clamp(24px,2.6vw,32px);
  color:var(--zoloto-svet);line-height:1;margin-bottom:8px;word-spacing:.2em}
.artstats .stat span{font-size:14px;color:var(--tihiy);line-height:1.45}
@media(max-width:760px){.artstats .stats{grid-template-columns:1fr}}

/* таблица */
.kb-tbl{width:100%;overflow-x:auto;margin:24px 0 28px;border:1px solid var(--line);border-radius:14px}
.kb-tbl table{width:100%;border-collapse:collapse;min-width:520px}
.kb-tbl th,.kb-tbl td{padding:13px 16px;text-align:left;font-size:15.5px;
  border-bottom:1px solid rgba(232,226,217,.08)}
.kb-tbl th{font-family:var(--anons);font-size:14px;letter-spacing:1.2px;text-transform:uppercase;
  color:var(--zoloto);background:rgba(201,162,39,.06)}
.kb-tbl tr:last-child td{border-bottom:0}
.kb-tbl td:first-child{color:#EDE6DC}

/* врезка */
.kb-call{border-left:2px solid var(--zoloto);border-radius:0 14px 14px 0;padding:18px 22px;
  margin:24px 0;background:rgba(201,162,39,.07);font-size:16.5px;color:#DCD5CA}
.kb-call b{color:var(--zoloto-svet)}

/* цитата */
.kb-pull{margin:30px 0;padding:22px 26px;border-top:1px solid rgba(201,162,39,.3);
  border-bottom:1px solid rgba(201,162,39,.3);font-family:var(--zag);
  font-size:clamp(20px,2.4vw,26px);line-height:1.45;color:#F3EDE3;text-align:center}

/* практика */
.kb-practice{border:1px solid rgba(201,162,39,.4);border-radius:18px;padding:26px;margin:30px 0;
  background:linear-gradient(160deg,rgba(201,162,39,.1),rgba(22,19,28,.92))}
.kb-practice>b{display:block;font-family:var(--anons);font-size:14px;letter-spacing:3px;
  text-transform:uppercase;color:var(--zoloto);margin-bottom:12px}
.kb-practice ol{margin:14px 0 0;padding-left:22px}

/* мостик к курсу */
.kb-bridge{margin:30px 0;padding:22px 24px;border:1px dashed rgba(201,162,39,.42);border-radius:16px;
  background:rgba(201,162,39,.05)}
.kb-bridge p{margin:0;color:#DCD5CA}

/* вопросы */
.kb-faq{display:grid;gap:10px;margin:20px 0 30px}
.kb-faq details{border:1px solid var(--line);border-radius:14px;background:var(--sloy);overflow:hidden}
.kb-faq summary{cursor:pointer;padding:16px 20px;font-family:var(--anons);font-size:17px;
  color:#F0E9DF;list-style:none}
.kb-faq summary::-webkit-details-marker{display:none}
.kb-faq summary::after{content:"+";float:right;color:var(--zoloto);font-size:20px;line-height:1}
.kb-faq details[open] summary::after{content:"−"}
.kb-faq .fa{padding:0 20px 18px}
.kb-faq .fa p{margin:0 0 12px;font-size:16.5px;color:#CFC7BC}

/* источники */
.kb-src{border:1px solid var(--line);border-radius:14px;padding:16px 20px;margin:28px 0;
  background:var(--sloy)}
.kb-src summary{cursor:pointer;font-family:var(--anons);font-size:16px;color:#CFC7BC;list-style:none}
.kb-src summary::-webkit-details-marker{display:none}
.kb-src ol{margin:14px 0 0;padding-left:22px}
.kb-src li{font-size:14.5px;color:var(--tihiy);margin-bottom:8px}

/* автор */
.kb-author{display:flex;gap:16px;align-items:center;border:1px solid var(--line);border-radius:16px;
  padding:18px 20px;margin:30px 0;background:var(--sloy)}
.kb-author img{width:64px;height:64px;border-radius:50%;object-fit:cover;flex:0 0 64px}
.kb-author b{display:block;font-family:var(--anons);font-size:17px;color:#F0E9DF;margin-bottom:4px}
.kb-author span{font-size:14.5px;color:var(--tihiy);line-height:1.5}

/* крошки и шапка статьи */
.kb-crumbs{font-size:13.5px;color:#7E7669;padding:22px 0 0}
.kb-crumbs a{color:#9A9184;text-decoration:none}
.artmeta{display:flex;flex-wrap:wrap;gap:10px 18px;margin:14px 0 0;font-size:14px;color:var(--tihiy)}
.artmeta span{display:inline-flex;align-items:center;gap:7px}
.artmeta b{color:var(--zoloto);font-weight:600}

/* хаб раздела */
.kb-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px;margin-top:26px}
.kb-card{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:18px;
  overflow:hidden;background:var(--sloy);transition:border-color .18s ease,transform .18s ease}
.kb-card .ph{position:relative;width:100%;aspect-ratio:16/9;overflow:hidden;border:0;border-radius:0}
.kb-card .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.kb-card .body{padding:20px 22px 24px;display:flex;flex-direction:column;flex:1 1 auto}
.kb-card .metka{font-family:var(--anons);font-size:12.5px;letter-spacing:2.4px;text-transform:uppercase;
  color:var(--zoloto);margin-bottom:10px}
.kb-card h3{margin:0 0 10px;font-size:21px}
.kb-card p{margin:0;color:var(--tihiy);font-size:15.5px;text-wrap:pretty}
.kb-card .chit{margin-top:auto;padding-top:16px;font-size:14.5px;color:var(--zoloto-svet);font-weight:600}
@media(hover:hover){.kb-card:hover{border-color:rgba(201,162,39,.5);transform:translateY(-2px)}}
/* ---------- хаб библиотеки ---------- */
.hb{padding-top:34px}
.hb-hero{max-width:820px;margin:0 0 34px}
.hb-hero .eb{display:inline-block;font-family:var(--anons);font-size:13px;letter-spacing:3.4px;
  text-transform:uppercase;color:var(--zoloto);margin-bottom:14px}
.hb-hero h1{margin:0 0 16px}
.hb-hero p{color:var(--tihiy);font-size:17.5px;line-height:1.7;margin:0 0 22px;text-wrap:pretty}
.hb-count{display:inline-flex;align-items:center;gap:10px;padding:12px 20px;border-radius:999px;
  border:1px solid rgba(201,162,39,.42);background:rgba(201,162,39,.08);
  font-size:15.5px;color:#F0E7D2;word-spacing:.2em}
.hb-count b{font-family:var(--zag);font-size:22px;color:var(--zoloto-svet)}
.hb-count svg{width:17px;height:17px;color:var(--zoloto)}
.hb-feat{display:flex;flex-wrap:wrap;gap:12px 26px;margin-top:20px;color:var(--tihiy);font-size:14.5px}
.hb-feat span{display:inline-flex;align-items:center;gap:9px}
.hb-feat svg{width:18px;height:18px;color:var(--zoloto)}
/* поиск */
.kb-poisk{display:flex;gap:10px;align-items:center;margin:0 0 30px}
.kb-pole{flex:1 1 auto;display:flex;align-items:center;gap:12px;padding:14px 18px;
  border:1px solid var(--line);border-radius:14px;background:var(--sloy)}
.kb-pole svg{width:20px;height:20px;color:var(--zoloto);flex:0 0 20px}
.kb-pole input{flex:1 1 auto;background:none;border:0;outline:none;color:#EDE6DC;font-size:16px;
  font-family:var(--sans)}
.kb-pole input::placeholder{color:#7E7669}
.kb-clr{padding:14px 18px;border:1px solid var(--line);border-radius:14px;background:var(--sloy);
  color:#CFC7BC;font-size:15px;font-family:var(--sans)}
/* группы-рубрики */
.kb-group{margin:0 0 42px}
.kb-group .gh{display:flex;align-items:center;gap:14px;padding:0 0 16px;margin-bottom:18px;
  border-bottom:1px solid var(--line)}
.kb-group .gh .ic{width:44px;height:44px;flex:0 0 44px;display:grid;place-items:center;border-radius:12px;
  border:1px solid rgba(201,162,39,.28);background:rgba(201,162,39,.07);color:var(--zoloto)}
.kb-group .gh .ic svg{width:22px;height:22px}
.kb-group .gh b{display:block;font-family:var(--zag);font-size:23px;color:#F3EDE3;font-weight:400}
.kb-group .gh span{display:block;font-size:14.5px;color:var(--tihiy);margin-top:3px}
.kb-group .gh .gn{margin-left:auto;font-style:normal;font-family:var(--zag);font-size:20px;
  color:var(--zoloto-svet)}
.kb-itog{margin:20px 0 40px;color:var(--tihiy)}
.kb-card .chit svg{width:16px;height:16px;vertical-align:-2px;margin-left:5px}
@media(max-width:640px){.kb-group .gh span{display:none}}
.kb-rows{display:block}
"""