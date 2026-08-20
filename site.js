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
});