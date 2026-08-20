document.addEventListener('DOMContentLoaded',function(){
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
   if(zapas>20){ sh.scrollLeft=sh.dataset.nachalo? 0 : Math.round(zapas/2);
    sh.dataset.navedena='1'; }
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

/* ---- мобильное меню: панель, замок прокрутки, разделы гармошкой ---- */
(function(){
 var b=document.getElementById('burger'), m=document.getElementById('mobmenu'),
     fon=document.getElementById('mobfon');
 if(!b||!m) return;
 var otkryto=false, sdvig=0;
 function pokazat(){
  if(otkryto) return;
  otkryto=true; sdvig=window.scrollY;
  m.classList.add('open'); if(fon){fon.hidden=false; requestAnimationFrame(function(){fon.classList.add('vidno');});}
  b.classList.add('krest'); b.setAttribute('aria-expanded','true');
  document.body.style.position='fixed'; document.body.style.top=(-sdvig)+'px';
  document.body.style.left='0'; document.body.style.right='0';
 }
 function spryatat(){
  if(!otkryto) return;
  otkryto=false;
  m.classList.remove('open'); if(fon){fon.classList.remove('vidno');
   setTimeout(function(){ if(!otkryto) fon.hidden=true; },260);}
  b.classList.remove('krest'); b.setAttribute('aria-expanded','false');
  document.body.style.position=''; document.body.style.top='';
  document.body.style.left=''; document.body.style.right='';
  window.scrollTo(0, sdvig);
 }
 b.addEventListener('click', function(){ otkryto? spryatat() : pokazat(); });
 if(fon) fon.addEventListener('click', spryatat);
 addEventListener('keydown', function(e){ if(e.key==='Escape') spryatat(); });
 m.addEventListener('click', function(e){ if(e.target.closest('a')) spryatat(); });
 /* разделы раскрываются на месте, страница под ними не прыгает */
 [].forEach.call(m.querySelectorAll('.mrask'), function(kn){
  kn.addEventListener('click', function(){
   var gr=kn.closest('.mgruppa'), otkryt=gr.classList.toggle('raskryt');
   kn.setAttribute('aria-expanded', otkryt?'true':'false');
  });
 });
 /* раздел текущей страницы открыт сразу */
 var tek=m.querySelector('.mstroka.on');
 if(tek){ var gr=tek.closest('.mgruppa');
  if(gr && gr.querySelector('.mpod')){ gr.classList.add('raskryt');
   var kn=gr.querySelector('.mrask'); if(kn) kn.setAttribute('aria-expanded','true'); } }
 addEventListener('resize', function(){ if(window.innerWidth>1120) spryatat(); });
})();
});