"""Genera el portafolio de Jared Andrade (Jaredbro0o). Ejecuta: python3 build.py"""
import os, html
OUT = os.path.dirname(os.path.abspath(__file__))
DEMO = "https://jaredbro0o.netlify.app/"
WA = "593979589676"
IRKANO_URL = ""  # pega aquí el link de Irkano Suites cuando esté publicado

# (archivo de captura, nombre, rubro, ruta en Netlify, lo que tiene)
WEBS = [
    ("rukito", "Rukito Grill & Drink", "comida", "rukito/", "Parrilla con 7 locales: menú con filtros, promo del día, horarios en vivo y reservas por WhatsApp."),
    ("prego", "Prego", "comida", "prego/", "Sandwichería: el sánduche se arma capa por capa y el carrito envía el pedido a WhatsApp."),
    ("fibydog", "FibyDog", "comida", "fibydog/", "Hot dogs: lluvia de cebolla animada y un armador de hot dog personalizado."),
    ("carbonrojo", "Carbón Rojo", "comida", "carbonrojo/", "Asados al carbón: el pedido llega al WhatsApp del local que elija el cliente."),
    ("pepezu", "Pepezu Donuts & Rolls", "comida", "pepezu/", "Donas y rollos de canela: sabores, pedidos para eventos y ubicación."),
    ("suculento", "Suculento", "comida", "suculento/", "Piqueos y cócteles: carta, cócteles y contacto con identidad nocturna."),
    ("donkeyswings", "Donkey's Wings", "comida", "donkeyswings/", "Alitas: burrito volador animado y un picómetro para escoger la salsa."),
    ("manaba", "El Manaba Jr", "comida", "manaba-jr.html", "Comida manaba: bolones, tigrillos y pedidos en Mucho Lote 2."),
    ("midoc", "Centro Médico Mi Doc", "salud", "midoc.html", "Centro médico: agenda de citas, horarios en vivo y recordatorio para el calendario."),
    ("rehi", "Consultorios REHI", "salud", "rehi/", "Consultorios médicos: especialidades, ecografías y citas por WhatsApp."),
    ("medesthetique", "Medesthetique", "salud", "medesthetique/", "Medicina estética: rediseño con tratamientos, 3 sedes y agenda de valoración."),
    ("makami", "Makami Medi-Spa", "salud", "makami/", "Podología y spa: servicios y agenda de citas en un minuto."),
    ("centerfit", "Center-Fit", "salud", "centerfit/", "Gimnasio: horario por día, test de membresía y agenda de visita."),
    ("vetzoo", "VetZooaquarium", "mascotas", "vetzooaquarium.html", "Acuario y veterinaria: pecera animada y mascotas no tradicionales."),
    ("pietrain", "Veterinaria Pietrain", "mascotas", "pietrain/", "Veterinaria: peluquería por tamaño de mascota y calendario de vacunas."),
    ("zhuangmonar", "Importadora Zhuang Monar", "comercio", "zhuangmonar/", "Importadora: catálogo con lista de pedido y precio de mayorista desde 3 productos."),
    ("alphapeople", "Alpha People", "comercio", "alphapeople/", "Computadoras semi nuevas: rediseño con catálogo filtrable y cotización para empresas."),
    ("jaes", "JAES Comercio Exterior", "comercio", "jaes/", "Asesoría aduanera: calculadora de tributos de importación."),
    ("giftlab", "Gift Lab", "comercio", "giftlab/", "Tienda de regalos: arma tu regalo y el pedido llega listo a WhatsApp."),
    ("mirasol", "Hotel Mirasol", "hospedaje", "hotel-mirasol.html", "Hotel: saludo según la hora del día y consulta de disponibilidad."),
]
RUBROS = [("todos", "Todos"), ("comida", "Comida"), ("salud", "Salud y bienestar"), ("mascotas", "Mascotas"), ("comercio", "Comercio y servicios"), ("hospedaje", "Hospedaje")]

PANDA = ["......hhhh......", "....hhhhhhhh....", "..HHHHHHHHHHHH..", "..kwwwwwwwwwwk..", "..wkkwwwwwwkkw..", "..wkrwwwwwwrkw..",
         "..wwwwwkkwwwww..", "...wwwwwwwwww...", "...rrrrrrrrrrrr.", "..kkkwwwwwwkkk.r", "..kkwwwwwwwwkk.r", "..kkwwwwwwwwkk..",
         "...wwwwwwwwww...", "...kkk....kkk..."]
COL = {"h": "#E2B04A", "H": "#A8742A", "k": "#1B1B1F", "w": "#F4F1EA", "r": "#D8342B"}
panda_svg = '<svg class="panda" viewBox="0 0 16 14" shape-rendering="crispEdges" role="img" aria-label="Pandy, el panda ninja de Panda Dash">' + "".join(
    f'<rect x="{x}" y="{y}" width="1" height="1" fill="{COL[c]}"/>' for y, row in enumerate(PANDA) for x, c in enumerate(row) if c != ".") + "</svg>"

def card(w):
    k, n, r, ruta, d = w
    return f'''<article class="web" data-r="{r}"><a class="shot" href="{DEMO}{ruta}" target="_blank" rel="noopener"><span class="barra" aria-hidden="true"><i></i><i></i><i></i><em>jaredbro0o.netlify.app/{ruta}</em></span><img src="assets/shots/{k}.webp" alt="Página de {html.escape(n)}" loading="lazy" width="800" height="500"></a>
<div class="info"><h3>{html.escape(n)}</h3><p>{d}</p><a class="lnk" href="{DEMO}{ruta}" target="_blank" rel="noopener">Abrir la demo<span class="sr"> de {html.escape(n)}</span></a></div></article>'''

col = lambda ks: "".join(f'<img src="assets/shots/{k}.webp" alt="" loading="eager" width="800" height="500">' for k in ks)
muro = f'''<div class="muro" aria-hidden="true">
<div class="c c1">{col(["rukito","giftlab","midoc","zhuangmonar","pietrain"]*2)}</div>
<div class="c c2">{col(["prego","centerfit","donkeyswings","alphapeople","mirasol"]*2)}</div>
<div class="c c3">{col(["fibydog","medesthetique","jaes","pepezu","rehi"]*2)}</div></div>'''

irk_btn = (f'<a class="btn luz" href="{IRKANO_URL}" target="_blank" rel="noopener">Ver Irkano Suites</a>' if IRKANO_URL
           else f'<a class="btn luz" href="https://wa.me/{WA}?text=Hola%20Jared%2C%20quiero%20ver%20la%20demo%20de%20Irkano%20Suites" target="_blank" rel="noopener">Pedir el recorrido de la demo</a>')

doc = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Jared Andrade · Jaredbro0o — Páginas web, soporte IT y contenido</title>
<meta name="description" content="Portafolio de Jared Andrade (Jaredbro0o): páginas web para negocios de Guayaquil, soporte técnico IT y creación de contenido.">
<meta property="og:title" content="Jared Andrade · Jaredbro0o">
<meta property="og:description" content="Páginas web para negocios, soporte técnico IT y creación de contenido. Durán – Guayaquil, Ecuador.">
<meta property="og:image" content="assets/shots/rukito.webp">
<meta name="theme-color" content="#14161B">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700;800&family=Figtree:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="saltar" href="#trabajos">Saltar a los trabajos</a>
<header class="top"><div class="wrap bar">
<a class="marca" href="#inicio" aria-label="Jaredbro0o, inicio"><b>J</b><span>Jaredbro0o</span></a>
<button class="menu" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav"><span></span><span></span></button>
<nav id="nav" aria-label="Secciones"><ul>
<li><a href="#servicios">Servicios</a></li><li><a href="#trabajos">Páginas web</a></li><li><a href="#contenido">Contenido</a></li><li><a href="#juegos">Juegos</a></li><li><a href="#experiencia">Experiencia</a></li><li class="cta"><a href="#contacto">Contacto</a></li></ul></nav>
</div></header>

<main>
<section class="hero" id="inicio"><div class="wrap hgrid">
<div class="htxt">
<p class="hola"><span class="punto" aria-hidden="true"></span>Disponible para nuevos proyectos</p>
<h1>Páginas web que hacen que tu negocio <span class="sub">reciba pedidos.</span></h1>
<p class="lead">Soy Jared Andrade. Diseño páginas web para negocios de Guayaquil, doy soporte técnico IT y creo contenido digital. Cada página tiene su propia identidad y lleva al cliente directo a tu WhatsApp.</p>
<div class="btns"><a class="btn azul" href="#trabajos">Ver mis páginas</a><a class="btn borde" href="https://wa.me/{WA}?text=Hola%20Jared%2C%20quiero%20una%20p%C3%A1gina%20web%20para%20mi%20negocio" target="_blank" rel="noopener">Escribirme por WhatsApp</a></div>
<dl class="cifras"><div><dt>Páginas de muestra</dt><dd><span data-n="{len(WEBS)+1}">0</span></dd></div><div><dt>Rubros distintos</dt><dd><span data-n="5">0</span></dd></div><div><dt>Responsive</dt><dd>100%</dd></div></dl>
</div>
{muro}
</div></section>

<section id="servicios" class="servicios"><div class="wrap">
<h2 class="tit rv">Lo que hago</h2>
<div class="tres">
<article class="srv rv"><span class="num">01</span><h3>Páginas web para negocios</h3><p>Sitios con varias páginas, animaciones, menú o catálogo, formularios que arman el pedido en WhatsApp y horarios con "abierto ahora". Se ven bien en celular, tablet y computadora.</p><ul><li>Diseño con la identidad de tu marca</li><li>Pedidos, reservas y citas por WhatsApp</li><li>Publicación en internet con tu dominio</li></ul></article>
<article class="srv rv d1"><span class="num">02</span><h3>Soporte técnico IT</h3><p>Diagnóstico y solución de problemas de PC, presencial y remoto. Redes, cableado y cámaras para oficinas y negocios.</p><ul><li>Hardware, software y Windows</li><li>Ponchado de cable UTP y racks</li><li>DVR, cámaras y access points</li></ul></article>
<article class="srv rv d2"><span class="num">03</span><h3>Contenido digital</h3><p>Guiones, videos cortos y largos para redes sociales, con edición, miniaturas y una publicación constante.</p><ul><li>Videos para TikTok y YouTube</li><li>Guiones y calendario de publicación</li><li>Animación y pixel art</li></ul></article>
</div></div></section>

<section id="trabajos" class="trabajos"><div class="wrap">
<div class="cab"><div><h2 class="tit rv">Páginas web</h2><p class="intro rv">Propuestas de diseño que preparé para negocios reales de Guayaquil. Cada una es una demo funcionando: ábrela y pruébala.</p></div>
<div class="filtros rv" role="group" aria-label="Filtrar por rubro">{"".join(f'<button type="button" data-f="{k}" aria-pressed="{"true" if k=="todos" else "false"}">{l}</button>' for k, l in RUBROS)}</div></div>

<article class="destacado rv" data-r="hospedaje">
<div class="dimg"><img src="assets/shots/irkano.webp" alt="Página de Irkano Suites" loading="lazy" width="800" height="500"><img class="foto" src="assets/shots/irkano-foto.webp" alt="Suite de Irkano Suites" loading="lazy"></div>
<div class="dtxt"><p class="etq">Proyecto destacado · 2026</p><h3>Irkano Suites</h3><p>Sitio de 7 páginas para un edificio de 26 suites. Lo más llamativo es el plano interactivo del edificio, donde el cliente toca una puerta, ve si la suite está libre y la reserva.</p>
<ul class="lista"><li>Plano interactivo de 3 pisos y 26 suites</li><li>Recorridos en video con capítulos</li><li>Galería con visor y comparador de suites</li><li>Panel para que el dueño actualice la disponibilidad</li></ul>{irk_btn}</div>
</article>

<div class="webs">{"".join(card(w) for w in WEBS)}</div>
<p class="aviso rv">Son propuestas de diseño: cada demo indica que no es la página oficial del negocio. Todas están publicadas en <a href="{DEMO}" target="_blank" rel="noopener">jaredbro0o.netlify.app</a>.</p>
</div></section>

<section class="proceso"><div class="wrap">
<h2 class="tit rv">Cómo trabajo</h2>
<ol class="pasos">
<li class="rv"><h3>Investigo tu negocio</h3><p>Reviso tus redes, tu menú o catálogo y lo que te hace distinto.</p></li>
<li class="rv d1"><h3>Te muestro una demo</h3><p>Antes de cobrarte nada, ves tu página funcionando con un link.</p></li>
<li class="rv d2"><h3>La ajustamos juntos</h3><p>Cambiamos textos, fotos y precios hasta que quede como la quieres.</p></li>
<li class="rv d3"><h3>La publicamos</h3><p>Queda en internet con tu dominio y te ayudo a mantenerla al día.</p></li>
</ol></div></section>

<section id="contenido" class="contenido"><div class="wrap cgrid">
<div class="rv"><p class="etq">Creación de contenido</p><h2 class="tit">Cosmobro</h2>
<p class="intro">Mi canal sobre los misterios del universo y la programación. Publico videos cortos todos los días en TikTok y videos largos cada semana en YouTube: guion, narración, edición y miniaturas.</p>
<div class="btns"><a class="btn luz" href="https://www.tiktok.com/@cosmobro0o" target="_blank" rel="noopener">TikTok @cosmobro0o</a><a class="btn borde claro" href="https://www.youtube.com/@Cosmobro0o" target="_blank" rel="noopener">YouTube @Cosmobro0o</a></div></div>
<div class="cosmo rv d1" aria-hidden="true"><div class="orbita"><span class="pl p1"></span><span class="pl p2"></span><span class="pl p3"></span></div><div class="casco"><i></i></div>
<div class="tags"><span>Universo</span><span>Programación</span><span>Curiosidades</span></div></div>
</div></section>

<section id="juegos" class="juegos"><div class="wrap jgrid">
<div class="pixel rv">{panda_svg}<div class="suelo" aria-hidden="true"></div></div>
<div class="rv d1"><p class="etq">Videojuegos y herramientas</p><h2 class="tit">Panda Dash</h2>
<p class="intro">Mi propio juego de carreras en pixel art, hecho en Godot. Pandy, un panda ninja con sombrero de paja, corre por un bosque de bambú, la Gran Muralla y una aldea antigua.</p>
<ul class="lista"><li>Animaciones completas en pixel art: correr, saltar, deslizarse, lanzar y más</li><li>Modo berserker y 7 osos jugables, cada uno con su arma y su región</li><li>Fondos con parallax y efectos de viento, niebla y luciérnagas</li><li>Tienda de ropa y accesorios para personalizar al personaje</li></ul>
<p class="nota">También creé un limpiador de sprites para dejar las imágenes listas para el juego, y un video animado en pixel art que explica las funciones de JavaScript.</p></div>
</div></section>

<section id="experiencia" class="experiencia"><div class="wrap egrid">
<div><h2 class="tit rv">Experiencia</h2>
<ol class="linea">
<li class="rv"><span class="fecha">2026 – Actualidad</span><h3>Asistente del Área de Sistemas</h3><p class="emp">Tractodiesel</p><ul><li>Diagnóstico y solución de problemas de PC en hardware y software, presencial y remoto.</li><li>Ponchado y tendido de cable de red UTP y organización de racks de comunicaciones.</li><li>Instalación y configuración de DVR, cámaras de seguridad y access points.</li><li>Soporte a usuarios en incidencias de equipos, programas y conectividad.</li></ul></li>
<li class="rv"><span class="fecha">2026 – Actualidad</span><h3>Diseño web freelance</h3><p class="emp">Jaredbro0o</p><ul><li>Más de 20 páginas de muestra para negocios de comida, salud, mascotas, comercio y hospedaje.</li><li>Contacto directo con los negocios y presentación de propuestas.</li></ul></li>
<li class="rv"><span class="fecha">2025 – 2026</span><h3>Soporte de Ventas FVD</h3><p class="emp">CANTEC</p><ul><li>Ingreso y registro de información de clientes en el sistema.</li><li>Gestión de solicitudes de clientes y seguimiento hasta su cierre.</li></ul></li>
<li class="rv"><span class="fecha">2025</span><h3>Asesor de Ventas</h3><p class="emp">CANTEC</p><ul><li>Asesoría a clientes y venta de equipos electrónicos y servicios de telecomunicaciones.</li></ul></li>
<li class="rv"><span class="fecha">2019 – 2025</span><h3>Bachiller Técnico en Informática</h3><p class="emp">Unidad Educativa Fiscal Durán</p></li>
</ol></div>
<aside class="habil rv d1"><h3>Habilidades</h3>
<div class="grupo"><h4>Soporte técnico IT</h4><p><span>Hardware y software</span><span>Soporte presencial y remoto</span><span>Instalación de programas</span><span>Windows y mantenimiento</span><span>Impresoras e inventarios</span></p></div>
<div class="grupo"><h4>Redes y telemática</h4><p><span>Cable UTP</span><span>Racks</span><span>DVR y cámaras</span><span>Access points</span></p></div>
<div class="grupo"><h4>Desarrollo y diseño</h4><p><span>HTML</span><span>CSS</span><span>JavaScript</span><span>C++</span><span>Godot</span><span>Netlify</span><span>Pixel art</span></p></div>
<div class="grupo"><h4>Ofimática</h4><p><span>Excel</span><span>Word</span><span>PowerPoint</span><span>Organización documental</span></p></div>
<div class="grupo"><h4>Idiomas</h4><p><span>Español nativo</span><span>Inglés básico</span></p></div>
</aside>
</div></section>

<section id="contacto" class="contacto"><div class="wrap">
<h2 class="tit grande rv">¿Tu negocio necesita su página?</h2>
<p class="intro rv">Te preparo una demo de tu página para que la veas funcionando antes de decidir. Trabajo presencial, híbrido o remoto desde Durán – Guayaquil.</p>
<div class="btns rv"><a class="btn luz" href="https://wa.me/{WA}?text=Hola%20Jared%2C%20quiero%20una%20p%C3%A1gina%20web%20para%20mi%20negocio" target="_blank" rel="noopener">WhatsApp +593 97 958 9676</a><a class="btn borde claro" href="mailto:jaredelsalto@gmail.com">jaredelsalto@gmail.com</a></div>
</div></section>
</main>

<footer class="pie"><div class="wrap"><span>© 2026 Jared Andrade · Jaredbro0o</span><span>Hecho a mano con HTML, CSS y JavaScript</span></div></footer>
<script src="assets/main.js"></script>
</body>
</html>'''
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(doc)
open(os.path.join(OUT, "assets", "favicon.svg"), "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#2D4BFF"/><text x="16" y="23" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="20" fill="#fff">J</text></svg>')
print("ok portafolio")
