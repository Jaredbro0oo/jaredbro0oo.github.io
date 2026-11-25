/* Portafolio de Jared Andrade · Jaredbro0o */
(function(){
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Menú móvil
  var m = document.querySelector('.menu');
  m.addEventListener('click', function(){ var o = document.body.classList.toggle('abierto'); m.setAttribute('aria-expanded', o); });
  document.querySelectorAll('nav a').forEach(function(a){ a.addEventListener('click', function(){ document.body.classList.remove('abierto'); m.setAttribute('aria-expanded', 'false'); }); });

  // Borde de la cabecera al bajar
  var top = document.querySelector('.top');
  addEventListener('scroll', function(){ top.classList.toggle('scroll', scrollY > 10); }, { passive:true });

  // Aparición al hacer scroll
  var rv = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && !reduce){
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold:.12 });
    rv.forEach(function(el){ io.observe(el); });
  } else rv.forEach(function(el){ el.classList.add('in'); });

  // Contadores
  document.querySelectorAll('[data-n]').forEach(function(el){
    var fin = +el.dataset.n;
    if (reduce){ el.textContent = fin; return; }
    var t0 = null;
    setTimeout(function(){ requestAnimationFrame(function f(t){ if (!t0) t0 = t; var p = Math.min(1, (t - t0) / 1300); el.textContent = Math.round(fin * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(f); }); }, 300);
  });

  // Filtro por rubro
  var bs = document.querySelectorAll('.filtros button');
  bs.forEach(function(b){ b.addEventListener('click', function(){
    var f = b.dataset.f;
    bs.forEach(function(x){ x.setAttribute('aria-pressed', x === b); });
    document.querySelectorAll('.web, .destacado').forEach(function(w){ w.classList.toggle('oculto', f !== 'todos' && w.dataset.r !== f); });
  }); });
})();
