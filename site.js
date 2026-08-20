document.addEventListener('DOMContentLoaded',function(){
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
  elItog.innerHTML='<div class="kviz-karta perevorot">'+(tpl?tpl.innerHTML:'')+'</div>'+
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
   var el=e.target, m=(el.textContent||'').trim().match(/^(\D*)(\d[\d\s]*)(.*)$/);
   if(!m) return;
   var do_=m[1], chislo=parseInt(m[2].replace(/\s/g,''),10), posle=m[3];
   if(!isFinite(chislo) || chislo>100000) return;
   var t0=null;
   function tik(t){ if(!t0) t0=t;
    var k=Math.min(1,(t-t0)/900), e2=1-Math.pow(1-k,3);
    el.textContent=do_+Math.round(chislo*e2).toLocaleString('ru-RU')+posle;
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
});