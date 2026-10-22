#!/usr/bin/env python3
"""Gera index.html da Cabana Bela Sardenha. Edite os dados aqui e rode: python3 build.py"""
import json, html

SITE = "https://cabanabelasardenha.com.br"

# ---------- Links de reserva (preencher quando a Camila enviar) ----------
LINKS = {
    "whatsapp": "https://wa.me/message/4OM2FDCG3OLWH1",   # ex.: https://wa.me/5554999999999?text=...
    "airbnb": "https://airbnb.com/h/cabanabelasardenha",
    "booking": "https://www.booking.com/Share-lCEy6C",
    "holmy": "https://www.holmy.com.br/hospedagem/cabana-elegante-na-serra-gaucha/",
    "instagram": "https://www.instagram.com/cabanabelasardenha/",
    "tiktok": "https://www.tiktok.com/@cabanabelasardenha",
    "maps": "https://maps.app.goo.gl/5ovxAbf6YuYhzmAE8",
}

def pic(name, alt, cls="", sizes="(min-width: 900px) 50vw, 100vw", eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img class="{cls}" src="img/{name}-1200.webp" '
            f'srcset="img/{name}-640.webp 640w, img/{name}-1200.webp 1200w" sizes="{sizes}" '
            f'alt="{html.escape(alt)}" width="1200" height="1600" decoding="async" {load}>')

def link(key, label, cls):
    url = LINKS[key]
    if url:
        return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener">{label}</a>'
    return f'<a class="{cls} pendente" href="#reservar" aria-disabled="true">{label}<small>link a configurar</small></a>'

GALERIA = [
    ("06-externa-dia-aframe-jacuzzi", "Cabana A-frame preta com deck, jacuzzi privativa e espreguiçadeiras de madeira, cercada de mata na Serra Gaúcha"),
    ("20-arco-iris-deck-jacuzzi", "Arco-íris sobre o vale visto do deck da cabana, com a jacuzzi e a mesa externa"),
    ("14-sala-janelao-aframe-simetrica", "Sala com janelão triangular do A-frame, sofá de couro, lustre pendente e vista para o deck e a mata"),
    ("07-sala-vista-mezanino-deck", "Vista do mezanino para a sala de pé-direito alto, com o deck e a jacuzzi do lado de fora"),
    ("08-sala-janelao-vista-flores", "Sala integrada com portas de vidro abertas para o deck e o jardim"),
    ("01-sala-golden-lareira-mezanino", "Sala com TV, lareira a lenha e escada para o mezanino; golden retriever em primeiro plano"),
    ("04-sala-chuva-janela-golden", "Dia de chuva visto da sala, com cachorro deitado no sofá junto ao janelão"),
    ("15-sala-vista-mezanino-golden", "Sala vista de cima, com tapete de couro, mesa de centro e o deck ao fundo"),
    ("09-quarto-mezanino-poltrona", "Quarto no mezanino sob as vigas do telhado A-frame, com cama king, poltrona e janela para a mata"),
    ("03-quarto-mezanino-ar-condicionado", "Quarto com cama king, forro de madeira, iluminação indireta e ar-condicionado"),
    ("21-cozinha-cafe-coado", "Cozinha equipada com fogão de indução, forno elétrico, micro-ondas, geladeira com freezer e café coado no balcão de granito"),
    ("25-banheiro-espelho-chuveiro", "Banheiro com espelho iluminado, cuba sobre bancada e box de vidro com chuveiro aquecido a boiler"),
    ("24-banheiro-maquina-lavaseca", "Banheiro com máquina lava e seca disponível para o hóspede"),
    ("10-jacuzzi-dia-drink", "Jacuzzi aquecida com hidromassagem em frente à cabana, em dia de sol"),
    ("12-jacuzzi-noite-cromoterapia", "Jacuzzi à noite com luz de cromoterapia vermelha e a cabana iluminada"),
    ("02-externa-noite-jacuzzi-vinho", "Cabana iluminada ao entardecer, jacuzzi acesa e taça de vinho junto às espreguiçadeiras"),
    ("18-fogueira-noite-marshmallow", "Fogueira acesa à noite com marshmallows, e a cabana iluminada no alto do gramado"),
    ("23-fogueira-araucarias-luzes", "Área da fogueira com cadeiras de madeira, varal de luzes e araucárias ao fundo"),
    ("17-fogueira-entardecer-pessoa-golden", "Hóspede junto à fogueira ao entardecer, com golden retriever deitado no gramado"),
    ("11-fogueira-varal-luzes-aframe", "Fogueira com varal de luzes no gramado e a cabana A-frame ao fundo"),
    ("13-deck-chimarrao-vista", "Chimarrão no deck com vista para o vale, araucárias e campos da Serra Gaúcha"),
    ("05-deck-vista-vale-drink", "Drink no deck com vista para o vale verde e céu azul"),
    ("16-espreguicadeiras-vista-golden", "Espreguiçadeiras de madeira de frente para o vale, com a jacuzzi e o deck ao lado"),
    ("22-deck-golden-churrasqueira-entardecer", "Golden retriever no deck ao entardecer, com churrasqueira americana e jacuzzi"),
]

FAQ = [
    ("Quantas pessoas a cabana acomoda?",
     "Até 4 pessoas. São dois ambientes de dormir com cama king: um no mezanino e outro no piso inferior. Os quartos não têm portas; a privacidade é feita por cortinas blackout, que fecham totalmente o ambiente e bloqueiam a luz."),
    ("A cabana tem piso aquecido?",
     "Sim. Todo o interior da cabana tem piso aquecido. A construção também tem isolamento térmico e acústico, e há ar-condicionado nos dois quartos e na sala, então a cabana fica confortável no inverno e no verão da Serra."),
    ("Tem internet? Dá para trabalhar de lá?",
     "Sim. A internet é Starlink, via satélite, pensada para quem precisa trabalhar remotamente ou fazer videochamadas mesmo na zona rural."),
    ("Qual é o horário de check-in e check-out?",
     "O check-in é a partir das 15h e o check-out é até as 11h."),
    ("Existem outras cabanas na propriedade?",
     "Não. A Cabana Bela Sardenha é a única cabana da propriedade. O hóspede tem acesso exclusivo a todo o terreno de 6.000 m², que é totalmente cercado e privado."),
    ("A cabana aceita pets?",
     "Sim. Pets são bem-vindos sem taxa e sem limite de porte. Como a propriedade é toda cercada, o cachorro pode circular com segurança pelo gramado."),
    ("Crianças podem se hospedar?",
     "Sim, crianças são bem-vindas."),
    ("A jacuzzi é aquecida e privativa?",
     "Sim. A jacuzzi fica no deck, é de uso exclusivo do hóspede e tem hidromassagem, cromoterapia e aquecimento que chega a 40 °C, o que permite usar no inverno da Serra."),
    ("Tem lareira e fogueira?",
     "Sim. Há uma lareira a lenha na sala e uma área de fogueira ao ar livre, de uso exclusivo, com cadeiras de madeira e varal de luzes. Fornecemos um pacote de lenha por hospedagem."),
    ("A cabana tem gás?",
     "Não. O fogão é de indução e o chuveiro é aquecido por boiler, então não há gás na cabana."),
    ("O que tem na cozinha?",
     "Fogão de indução, forno elétrico, micro-ondas, geladeira com freezer, utensílios e louças. Há também churrasqueira americana no deck e máquina lava e seca à disposição."),
    ("Qual é a estadia mínima?",
     "Duas noites durante todo o ano. No Réveillon (noites de 30/12, 31/12 e 01/01) e no feriado de Carnaval, a estadia mínima é de três noites."),
    ("Dá para caminhar na natureza?",
     "Sim. Parte da propriedade é mata nativa preservada, com caminho para caminhar dentro da própria área cercada."),
    ("Onde fica a cabana?",
     "Na zona rural de Farroupilha, no coração da região vinícola da Serra Gaúcha (RS). De carro, fica a cerca de 10 minutos do centro de Farroupilha, 5 minutos da cervejaria Blauth Bier, 8 minutos do Salto Ventoso, 15 minutos de Garibaldi e dos Caminhos de Pedra e 20 minutos do Vale dos Vinhedos."),
    ("Como faço para reservar?",
     "Você pode reservar pelo Airbnb, pelo Booking.com ou pelo Holmy, ou falar direto com a gente pelo WhatsApp. Na reserva direta pelo WhatsApp é possível parcelar no cartão de crédito."),
]

REVIEWS = [
    ("Maria Eduarda", "julho de 2026", "Estadia maravilhosa! A casa é impecável, com aquecimento de todo o piso, fomos em dias bem frios e não sentimentos frio em momento nenhum! A anfitriã foi super prestativa e atenciosa!"),
    ("Rafael", "agosto de 2026", "Foi fácil de encontrar e fazer o checkin. Tudo na acomodação é de muito boa qualidade. Tudo funcionando perfeitamente: os eletrodomésticos, instalações...\nO piso aquecido é um diferencial muito legal.\nVoltaremos em uma próxima oportunidade!"),
    ("Jader", "julho de 2026", "Nossa estadia foi excelente! O lugar é exatamente como mostrado nas fotos: muito bonito, limpo, organizado e confortável. É um ambiente tranquilo, perfeito para descansar e aproveitar momentos de paz.\nOs anfitriões foram muito atenciosos, receptivos e sempre disponíveis quando precisamos. Tudo funcionou muito bem durante a estadia.\nCom certeza voltaria a me hospedar aqui e recomendo para quem procura um lugar agradável, confortável e fiel ao anúncio. Excelente experiência!"),
    ("Jéssica", "abril de 2026", "Excepcional é a definição deste lugar!\nA cabana estava impecável! Parecia que nós éramos as primeiras pessoas a entrar ali de tão perfeita que estava!\nCheirosa, limpa, organizada, bem equipada...perfeita!!!\nNota milllll\nVoltaremos 💖"),
]

SCHEMA = {
    "@context": "https://schema.org",
    "@type": "VacationRental",
    "name": "Cabana Bela Sardenha",
    "description": "Cabana A-frame única em propriedade privada e cercada de 6.000 m² em Farroupilha, Serra Gaúcha (RS), a 20 minutos do Vale dos Vinhedos e 15 minutos de Garibaldi e dos Caminhos de Pedra. Piso aquecido em todo o interior, isolamento térmico e acústico, internet Starlink, jacuzzi aquecida privativa, lareira a lenha, fogueira exclusiva, mata nativa, dois quartos com cama king, até 4 hóspedes, pet friendly sem taxa.",
    "address": {"@type": "PostalAddress", "addressLocality": "Farroupilha", "addressRegion": "RS", "addressCountry": "BR"},
    "containedInPlace": {"@type": "Place", "name": "Serra Gaúcha"},
    "url": SITE + "/",
    "image": [f"{SITE}/img/{n}-1200.webp" for n, _ in GALERIA[:6]],
    "petsAllowed": True,
    "occupancy": {"@type": "QuantitativeValue", "maxValue": 4},
    "numberOfRooms": 2,
    "numberOfBedrooms": 2,
    "numberOfBathroomsTotal": 1,
    "floorSize": {"@type": "QuantitativeValue", "value": 6000, "unitCode": "MTK", "description": "área total da propriedade"},
    "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": a, "value": True} for a in [
        "Jacuzzi aquecida privativa (até 40 °C) com hidromassagem e cromoterapia", "Lareira a lenha", "Fogueira externa exclusiva",
        "Churrasqueira americana", "Fogão de indução", "Chuveiro aquecido a boiler", "Máquina lava e seca",
        "Piso aquecido em todo o interior", "Isolamento térmico e acústico", "Internet Starlink", "Ar-condicionado nos quartos e na sala", "Cortinas blackout", "Propriedade totalmente cercada", "Mata nativa com trilha", "Aceita pets sem taxa", "Aceita crianças"]],
    "foundingDate": "2022",
    "checkinTime": "15:00",
    "checkoutTime": "11:00",
    "sameAs": [LINKS["instagram"], LINKS["tiktok"], LINKS["airbnb"], LINKS["holmy"]],
    "hasMap": "https://maps.app.goo.gl/5ovxAbf6YuYhzmAE8",
}
FAQ_SCHEMA = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}

g = {n: a for n, a in GALERIA}

out = f'''<title>Cabana Bela Sardenha</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="Cabana A-frame única em propriedade privada de 6.000 m² em Farroupilha, Serra Gaúcha. Piso aquecido, internet Starlink, jacuzzi aquecida privativa, lareira, fogueira, mata nativa, até 4 hóspedes, pet friendly.">
<link rel="icon" href="img/favicon.png">
<link rel="canonical" href="{SITE}/">
<meta property="og:type" content="website">
<meta property="og:title" content="Cabana Bela Sardenha · Farroupilha, Serra Gaúcha">
<meta property="og:description" content="Cabana A-frame única em propriedade privada de 6.000 m². Piso aquecido, Starlink, jacuzzi aquecida privativa, lareira, fogueira. Até 4 hóspedes, pet friendly.">
<meta property="og:image" content="{SITE}/img/06-externa-dia-aframe-jacuzzi-1200.webp">
<meta property="og:locale" content="pt_BR">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Montserrat:wght@400;500;600&display=swap">
<script type="application/ld+json">{json.dumps(SCHEMA, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(FAQ_SCHEMA, ensure_ascii=False)}</script>
<style>
/* Layout: ficha de hospedagem — hero dividido (texto | foto vertical), seções alternando bege e verde, fotos verticais em pares. */
:root {{
  --bg: #f4efe4; --band: #eae1ce; --fg: #243d43; --muted: #536569; --line: #d6cbb3;
  --accent: #bf4d28; --accent-ink: #ffffff; --gold: #a59463; --sage: #71816d;
  --deep: #243d43; --deep-fg: #eae1ce; --deep-muted: #b9b4a3;
  --serif: "Cormorant Garamond", "Iowan Old Style", Georgia, serif;
  --sans: "Montserrat", "Segoe UI", system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #17292e; --band: #1e353b; --fg: #eae1ce; --muted: #b3ae9e; --line: #34504f;
  --accent: #c9552e; --deep: #0f1f23; --deep-fg: #eae1ce; --deep-muted: #a9a593; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #17292e; --band: #1e353b; --fg: #eae1ce; --muted: #b3ae9e; --line: #34504f;
  --accent: #c9552e; --deep: #0f1f23; --deep-fg: #eae1ce; --deep-muted: #a9a593; color-scheme: dark }}

* {{ box-sizing: border-box }}
html {{ scroll-behavior: smooth }}
@media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto }} }}
body {{ background: var(--bg); color: var(--fg); font: 400 1rem/1.7 var(--sans); }}
body::before {{ content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 30; background: var(--bg) }}
img {{ display: block; max-width: 100%; height: auto }}
a {{ color: inherit }}
:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 3px }}
.wrap {{ max-width: 1180px; margin-inline: auto; padding-left: max(20px, env(safe-area-inset-left, 0px)); padding-right: max(20px, env(safe-area-inset-right, 0px)) }}
h1, h2, h3 {{ font-family: var(--serif); font-weight: 500; line-height: 1.08; text-wrap: balance; margin: 0 }}
h1 {{ font-size: clamp(2.4rem, 5.4vw, 4.4rem) }}
h2 {{ font-size: clamp(2rem, 3.8vw, 3rem) }}
h3 {{ font-size: 1.6rem }}
p {{ margin: 0; max-width: 62ch }}
.eyebrow {{ font: 600 .72rem/1 var(--sans); letter-spacing: .22em; text-transform: uppercase; color: var(--gold) }}
.lead {{ font-size: 1.08rem; color: var(--muted) }}

/* header */
.top {{ position: sticky; top: env(safe-area-inset-top, 0px); z-index: 20; background: color-mix(in srgb, var(--bg) 92%, transparent); backdrop-filter: blur(8px); border-bottom: 1px solid var(--line) }}
.top .wrap {{ display: flex; align-items: center; gap: 24px; padding-block: 12px }}
.top .logo img {{ height: 40px; width: auto }}
.logo .dark {{ display: none }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) .logo .light {{ display: none }} :root:not([data-theme="light"]) .logo .dark {{ display: block }} }}
:root[data-theme="dark"] .logo .light {{ display: none }} :root[data-theme="dark"] .logo .dark {{ display: block }}
.top nav {{ display: flex; gap: 22px; margin-left: auto; font-size: .82rem; font-weight: 500; letter-spacing: .04em }}
.top nav a {{ text-decoration: none; color: var(--muted) }}
.top nav a:hover {{ color: var(--fg) }}
@media (max-width: 760px) {{ .top nav {{ display: none }} .top .btn {{ margin-left: auto }} }}

.btn {{ display: inline-flex; align-items: center; justify-content: center; gap: 10px; padding: 14px 24px; border-radius: 2px; font: 600 .82rem/1 var(--sans); letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border: 1px solid var(--accent); background: var(--accent); color: var(--accent-ink); transition: filter .2s }}
.btn:hover {{ filter: brightness(1.08) }}
.btn.ghost {{ background: transparent; color: var(--fg); border-color: var(--fg) }}
.btn.small {{ padding: 10px 16px; font-size: .74rem }}
.btn svg {{ width: 18px; height: 18px; flex: none }}
.pendente {{ position: relative; flex-direction: column; gap: 6px }}
.pendente small {{ font-size: .62rem; letter-spacing: .1em; opacity: .75; font-weight: 500 }}

/* hero */
.hero .wrap {{ display: grid; grid-template-columns: 1.05fr .95fr; gap: clamp(28px, 5vw, 72px); align-items: center; padding-block: clamp(36px, 6vw, 80px) }}
.hero-text {{ display: grid; gap: 22px; min-width: 0 }}
.hero-actions {{ display: flex; flex-wrap: wrap; gap: 12px; margin-top: 6px }}
.hero-photo {{ position: relative }}
.hero-photo img {{ aspect-ratio: 4/5; object-fit: cover; width: 100% }}
.hero-photo figcaption {{ position: absolute; left: 0; bottom: 0; background: var(--bg); padding: 10px 16px 0 0; font-size: .74rem; color: var(--muted); letter-spacing: .06em }}
@media (max-width: 860px) {{ .hero .wrap {{ grid-template-columns: 1fr }} .hero-photo {{ order: -1 }} .hero-photo img {{ aspect-ratio: 4/4.4 }} }}

/* ficha */
.ficha {{ background: var(--deep); color: var(--deep-fg) }}
.ficha dl {{ display: grid; grid-template-columns: repeat(6, 1fr); margin-block: 0; padding-block: 34px }}
.ficha div {{ padding: 4px 18px; border-left: 1px solid color-mix(in srgb, var(--deep-fg) 22%, transparent); min-width: 0 }}
.ficha div:first-child {{ border-left: 0; padding-left: 0 }}
.ficha dt {{ font: 600 .66rem/1.3 var(--sans); letter-spacing: .18em; text-transform: uppercase; color: var(--deep-muted) }}
.ficha dd {{ margin: 8px 0 0; font: 500 1.7rem/1.1 var(--serif) }}
@media (max-width: 960px) {{ .ficha dl {{ grid-template-columns: repeat(3, 1fr); row-gap: 26px }} .ficha div:nth-child(4) {{ border-left: 0; padding-left: 0 }} }}
@media (max-width: 520px) {{ .ficha dl {{ grid-template-columns: repeat(2, 1fr) }} .ficha div {{ border-left: 0; padding-left: 0 }} }}

section {{ padding-block: clamp(56px, 8vw, 110px) }}
.band {{ background: var(--band) }}
.split {{ display: grid; grid-template-columns: 1fr 1fr; gap: clamp(28px, 5vw, 72px); align-items: center }}
.split > * {{ min-width: 0 }}
.split.rev .copy {{ order: 2 }}
.copy {{ display: grid; gap: 18px }}
.pair {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px }}
.pair img, .one img {{ aspect-ratio: 3/4; object-fit: cover; width: 100% }}
.pair img:nth-child(2) {{ margin-top: 48px }}
@media (max-width: 860px) {{ .split {{ grid-template-columns: 1fr }} .split.rev .copy {{ order: 0 }} }}

.conforto {{ background: var(--band) }}
h2.big {{ font-size: clamp(2.6rem, 5.6vw, 4.6rem) }}
.feats {{ list-style: none; padding: 0; margin: 8px 0 0; display: grid; grid-template-columns: 1fr 1fr; gap: 0; border-top: 1px solid var(--line) }}
.feats li {{ padding: 16px 16px 16px 0; border-bottom: 1px solid var(--line); min-width: 0; display: grid; gap: 2px }}
.feats b {{ font: 500 1.35rem/1.2 var(--serif) }}
.feats span {{ font-size: .86rem; color: var(--muted) }}
.ticks {{ list-style: none; padding: 0; margin: 4px 0 0; display: grid; gap: 10px }}
.ticks li {{ padding-left: 26px; position: relative }}
.ticks li::before {{ content: ""; position: absolute; left: 0; top: .72em; width: 14px; height: 1px; background: var(--gold) }}

/* interiores */
.rooms {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 44px }}
.room {{ display: grid; gap: 14px; align-content: start; min-width: 0 }}
.room img {{ aspect-ratio: 3/4; object-fit: cover; width: 100% }}
.room h3 {{ font-size: 1.45rem }}
.room p {{ font-size: .92rem; color: var(--muted) }}
@media (max-width: 960px) {{ .rooms {{ grid-template-columns: repeat(2, 1fr) }} }}
@media (max-width: 520px) {{ .rooms {{ grid-template-columns: 1fr }} }}
.section-head {{ display: grid; gap: 16px; max-width: 760px }}

/* noite */
.noite {{ background: var(--deep); color: var(--deep-fg) }}
.noite .lead {{ color: var(--deep-muted) }}
.noite-grid {{ display: grid; grid-template-columns: 1.2fr 1fr 1fr; gap: 12px; margin-top: 44px }}
.noite-grid img {{ width: 100%; height: 100%; object-fit: cover; aspect-ratio: 3/4 }}
.noite-grid figure:first-child {{ grid-row: span 2 }}
.noite-grid figure:first-child img {{ aspect-ratio: auto; height: 100% }}
.noite-grid figure {{ margin: 0; position: relative; min-width: 0 }}
.noite-grid figcaption {{ position: absolute; inset: auto 0 0; padding: 30px 16px 14px; font-size: .82rem; background: linear-gradient(transparent, rgba(10,22,25,.8)); color: #eae1ce }}
@media (max-width: 760px) {{ .noite-grid {{ grid-template-columns: 1fr 1fr }} .noite-grid figure:first-child {{ grid-column: span 2; grid-row: auto }} .noite-grid figure:first-child img {{ aspect-ratio: 4/5 }} }}

/* avaliações */
.revs {{ columns: 3 300px; column-gap: 20px; margin-top: 40px }}
.rev {{ break-inside: avoid; margin: 0 0 20px; padding: 26px; background: var(--bg); border: 1px solid var(--line); display: grid; gap: 14px }}
.rev .stars {{ color: var(--accent); letter-spacing: .2em; font-size: .9rem }}
.rev blockquote {{ margin: 0; display: grid; gap: 8px; font-size: .95rem }}
.rev figcaption {{ display: grid; gap: 2px; border-top: 1px solid var(--line); padding-top: 12px }}
.rev figcaption b {{ font: 500 1.2rem/1.2 var(--serif) }}
.rev figcaption span {{ font-size: .78rem; color: var(--muted); letter-spacing: .04em }}

/* galeria */
.gal {{ columns: 4 220px; column-gap: 12px; margin-top: 40px }}
.gal button {{ all: unset; display: block; margin-bottom: 12px; cursor: zoom-in; break-inside: avoid; width: 100% }}
.gal button:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px }}
.gal img {{ width: 100%; transition: opacity .2s }}
.gal button:hover img {{ opacity: .88 }}
dialog {{ border: 0; padding: 0; background: transparent; max-width: min(96vw, 900px); max-height: 94vh }}
dialog::backdrop {{ background: rgba(10, 20, 23, .92) }}
dialog img {{ max-height: 82vh; width: auto; margin-inline: auto }}
dialog p {{ color: #eae1ce; font-size: .85rem; text-align: center; margin: 12px auto 0; max-width: 70ch }}
.lb-nav {{ display: flex; justify-content: center; gap: 10px; margin-top: 12px }}
.lb-nav button {{ background: transparent; border: 1px solid #eae1ce; color: #eae1ce; font: 600 .74rem/1 var(--sans); letter-spacing: .1em; text-transform: uppercase; padding: 10px 16px; cursor: pointer }}

/* comodidades */
.amen {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 32px; margin-top: 44px }}
.amen > div {{ min-width: 0; border-top: 1px solid var(--line); padding-top: 18px }}
.amen h3 {{ font-size: 1.35rem; margin-bottom: 10px }}
.amen ul {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 8px; font-size: .92rem; color: var(--muted) }}
@media (max-width: 960px) {{ .amen {{ grid-template-columns: 1fr 1fr }} }}
@media (max-width: 520px) {{ .amen {{ grid-template-columns: 1fr }} }}

/* regras */
.rules {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; margin-top: 36px; border-top: 1px solid var(--line) }}
.rules div {{ padding: 22px 22px 22px 0; border-bottom: 1px solid var(--line); min-width: 0 }}
.rules strong {{ display: block; font: 500 1.45rem/1.2 var(--serif); margin-bottom: 4px }}
.rules span {{ font-size: .9rem; color: var(--muted) }}
@media (max-width: 960px) {{ .rules {{ grid-template-columns: 1fr 1fr }} }}
@media (max-width: 520px) {{ .rules {{ grid-template-columns: 1fr }} }}

/* faq */
.faq {{ display: grid; grid-template-columns: .8fr 1.2fr; gap: clamp(28px, 5vw, 72px) }}
.faq > * {{ min-width: 0 }}
details {{ border-bottom: 1px solid var(--line) }}
summary {{ cursor: pointer; list-style: none; padding: 20px 36px 20px 0; position: relative; font: 500 1.3rem/1.3 var(--serif) }}
summary::-webkit-details-marker {{ display: none }}
summary::after {{ content: "+"; position: absolute; right: 4px; top: 18px; font: 400 1.4rem var(--sans); color: var(--gold) }}
details[open] summary::after {{ content: "–" }}
details p {{ padding: 0 0 22px; color: var(--muted) }}
@media (max-width: 860px) {{ .faq {{ grid-template-columns: 1fr }} }}

/* localização */
.dist {{ list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--line) }}
.dist li {{ display: flex; justify-content: space-between; align-items: baseline; gap: 16px; padding: 16px 0; border-bottom: 1px solid var(--line) }}
.dist span {{ font: 500 1.35rem/1.2 var(--serif) }}
.dist b {{ font-weight: 600; font-size: .82rem; letter-spacing: .12em; text-transform: uppercase; color: var(--accent); font-variant-numeric: tabular-nums; white-space: nowrap }}
.dist li.foot {{ border: 0; font-size: .8rem; color: var(--muted); justify-content: flex-start }}

/* reservar */
.reserve {{ background: var(--deep); color: var(--deep-fg); text-align: left }}
.reserve .lead {{ color: var(--deep-muted) }}
.channels {{ display: grid; grid-template-columns: 1.4fr 1fr 1fr 1fr; gap: 12px; margin-top: 40px }}
.channels .btn {{ padding: 22px 18px; min-height: 84px }}
.channels .btn.ghost {{ color: var(--deep-fg); border-color: color-mix(in srgb, var(--deep-fg) 55%, transparent) }}
.reserve .note {{ margin-top: 22px; font-size: .86rem; color: var(--deep-muted) }}
@media (max-width: 860px) {{ .channels {{ grid-template-columns: 1fr 1fr }} .channels .btn:first-child {{ grid-column: span 2 }} }}

footer {{ background: var(--deep); color: var(--deep-muted); border-top: 1px solid color-mix(in srgb, var(--deep-fg) 14%, transparent) }}
footer .wrap {{ display: flex; flex-wrap: wrap; gap: 28px; align-items: center; padding-block: 40px; font-size: .84rem }}
footer img {{ width: 84px; height: auto }}
footer .tag {{ font-family: var(--serif); font-size: 1.2rem; color: var(--deep-fg) }}
footer .end {{ margin-left: auto; text-align: right }}
@media (max-width: 600px) {{ footer .end {{ margin-left: 0; text-align: left }} }}
</style>

<header class="top">
  <div class="wrap">
    <a class="logo" href="#inicio" aria-label="Cabana Bela Sardenha, início">
      <img class="light" src="img/logo-h-verde.png" alt="Cabana Bela Sardenha" width="900" height="270">
      <img class="dark" src="img/logo-h-bege.png" alt="Cabana Bela Sardenha" width="900" height="270">
    </a>
    <nav aria-label="Seções">
      <a href="#cabana">A cabana</a><a href="#ao-ar-livre">Ao ar livre</a><a href="#galeria">Fotos</a><a href="#avaliacoes">Avaliações</a><a href="#localizacao">Localização</a><a href="#perguntas">Perguntas</a>
    </nav>
    <a class="btn small" href="#reservar">Reservar</a>
  </div>
</header>

<main id="inicio">
<section class="hero" style="padding:0">
  <div class="wrap">
    <div class="hero-text">
      <span class="eyebrow">Farroupilha · Serra Gaúcha · RS</span>
      <h1>Uma cabana A-frame, uma propriedade inteira só para vocês.</h1>
      <p class="lead">A Cabana Bela Sardenha é a única cabana em um terreno de 6.000 m², todo cercado e privado, com mata nativa, piso aquecido em toda a cabana, jacuzzi aquecida, lareira e fogueira. Recebe até 4 pessoas, crianças e pets de qualquer porte.</p>
      <div class="hero-actions">
        {link("whatsapp", "Reservar pelo WhatsApp", "btn")}
        <a class="btn ghost" href="#reservar">Ver Airbnb, Booking e Holmy</a>
      </div>
    </div>
    <figure class="hero-photo" style="margin:0">
      {pic("06-externa-dia-aframe-jacuzzi", g["06-externa-dia-aframe-jacuzzi"], eager=True)}
      <figcaption>Deck com jacuzzi privativa, de frente para o vale</figcaption>
    </figure>
  </div>
</section>

<div class="ficha" aria-label="Ficha da cabana">
  <dl class="wrap">
    <div><dt>Hóspedes</dt><dd>até 4</dd></div>
    <div><dt>Piso</dt><dd>aquecido</dd></div>
    <div><dt>Internet</dt><dd>Starlink</dd></div>
    <div><dt>Jacuzzi</dt><dd>até 40 °C</dd></div>
    <div><dt>Propriedade</dt><dd>6.000 m²</dd></div>
    <div><dt>Pets</dt><dd>sem taxa</dd></div>
  </dl>
</div>

<section class="conforto" id="conforto">
  <div class="wrap split rev">
    <div class="copy">
      <span class="eyebrow">Conforto térmico</span>
      <h2 class="big">Piso aquecido em toda a cabana.</h2>
      <p class="lead">Do banheiro ao quarto, todo o interior tem piso aquecido. A cabana foi construída com isolamento térmico e acústico, e há ar-condicionado nos dois quartos e na sala.</p>
      <p>Na prática, isso quer dizer pé descalço no chão quente em julho e sala fresca em janeiro, com a lareira acesa só pelo prazer de acender.</p>
      <ul class="feats">
        <li><b>Piso aquecido</b><span>em todo o interior</span></li>
        <li><b>Isolamento</b><span>térmico e acústico</span></li>
        <li><b>Ar-condicionado</b><span>quartos e sala</span></li>
        <li><b>Internet Starlink</b><span>para home office e videochamadas</span></li>
      </ul>
    </div>
    <div class="one">
      {pic("04-sala-chuva-janela-golden", g["04-sala-chuva-janela-golden"])}
    </div>
  </div>
</section>

<section id="cabana">
  <div class="wrap split">
    <div class="copy">
      <span class="eyebrow">Privacidade total</span>
      <h2>Sem vizinhos de cabana, sem áreas compartilhadas.</h2>
      <p>Não existe outra hospedagem no terreno. Durante a estadia, os 6.000 m² são só seus: o gramado, o deck, a jacuzzi, a fogueira e a trilha na mata nativa preservada.</p>
      <p>A propriedade é totalmente cercada. Quem viaja com cachorro solta o pet no gramado sem preocupação, e quem viaja com criança tem a mesma tranquilidade.</p>
      <ul class="ticks">
        <li>Única cabana da propriedade, com acesso exclusivo</li>
        <li>Terreno todo cercado</li>
        <li>Mata nativa com caminho para caminhar</li>
      </ul>
    </div>
    <div class="pair">
      {pic("11-fogueira-varal-luzes-aframe", g["11-fogueira-varal-luzes-aframe"], sizes="(min-width: 900px) 25vw, 50vw")}
      {pic("16-espreguicadeiras-vista-golden", g["16-espreguicadeiras-vista-golden"], sizes="(min-width: 900px) 25vw, 50vw")}
    </div>
  </div>
</section>

<section class="band" id="por-dentro">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Por dentro</span>
      <h2>Pé-direito de A-frame, madeira e janelão para a mata.</h2>
      <p class="lead">A sala ocupa toda a altura do telhado triangular. O janelão de vidro abre direto para o deck, então a vista acompanha você do sofá à jacuzzi.</p>
    </div>
    <div class="rooms">
      <article class="room">
        {pic("14-sala-janelao-aframe-simetrica", g["14-sala-janelao-aframe-simetrica"], sizes="(min-width: 960px) 25vw, (min-width: 520px) 50vw, 100vw")}
        <h3>Sala com lareira</h3>
        <p>Lareira a lenha, ar-condicionado, sofá de couro e portas de vidro para o deck.</p>
      </article>
      <article class="room">
        {pic("09-quarto-mezanino-poltrona", g["09-quarto-mezanino-poltrona"], sizes="(min-width: 960px) 25vw, (min-width: 520px) 50vw, 100vw")}
        <h3>Dois quartos king</h3>
        <p>Um no mezanino, sob as vigas do telhado, e outro no piso inferior. Ambos com cama king, ar-condicionado e cortinas blackout no lugar de portas.</p>
      </article>
      <article class="room">
        {pic("21-cozinha-cafe-coado", g["21-cozinha-cafe-coado"], sizes="(min-width: 960px) 25vw, (min-width: 520px) 50vw, 100vw")}
        <h3>Cozinha sem gás</h3>
        <p>Fogão de indução, forno elétrico, micro-ondas e geladeira com freezer. Não há gás na cabana.</p>
      </article>
      <article class="room">
        {pic("25-banheiro-espelho-chuveiro", g["25-banheiro-espelho-chuveiro"], sizes="(min-width: 960px) 25vw, (min-width: 520px) 50vw, 100vw")}
        <h3>Banheiro e lavanderia</h3>
        <p>Chuveiro aquecido a boiler e máquina lava e seca disponível para o hóspede.</p>
      </article>
    </div>
  </div>
</section>

<section id="ao-ar-livre">
  <div class="wrap split rev">
    <div class="copy">
      <span class="eyebrow">Ao ar livre</span>
      <h2>Jacuzzi aquecida a 40 °C, de frente para o vale.</h2>
      <p>A jacuzzi fica no deck, é privativa e tem hidromassagem e cromoterapia. O aquecimento chega a 40 °C, então ela funciona também nas noites frias da Serra.</p>
      <p>No mesmo deck ficam a mesa externa, os bancos de madeira e a churrasqueira americana, liberada para o hóspede. Do outro lado, as espreguiçadeiras olham para os campos e as araucárias.</p>
    </div>
    <div class="pair">
      {pic("10-jacuzzi-dia-drink", g["10-jacuzzi-dia-drink"], sizes="(min-width: 900px) 25vw, 50vw")}
      {pic("13-deck-chimarrao-vista", g["13-deck-chimarrao-vista"], sizes="(min-width: 900px) 25vw, 50vw")}
    </div>
  </div>
</section>

<section class="noite" id="noite">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Quando escurece</span>
      <h2>Fogueira exclusiva, varal de luzes e a cabana acesa no alto do gramado.</h2>
      <p class="lead">A área da fogueira é de uso exclusivo, com cadeiras de madeira em volta. Cada hospedagem inclui um pacote de lenha, que serve para a fogueira e para a lareira.</p>
    </div>
    <div class="noite-grid">
      <figure>{pic("18-fogueira-noite-marshmallow", g["18-fogueira-noite-marshmallow"], sizes="(min-width: 760px) 40vw, 100vw")}<figcaption>Fogueira com marshmallow</figcaption></figure>
      <figure>{pic("12-jacuzzi-noite-cromoterapia", g["12-jacuzzi-noite-cromoterapia"], sizes="(min-width: 760px) 30vw, 50vw")}<figcaption>Jacuzzi com cromoterapia</figcaption></figure>
      <figure>{pic("23-fogueira-araucarias-luzes", g["23-fogueira-araucarias-luzes"], sizes="(min-width: 760px) 30vw, 50vw")}<figcaption>Varal de luzes e araucárias</figcaption></figure>
      <figure>{pic("02-externa-noite-jacuzzi-vinho", g["02-externa-noite-jacuzzi-vinho"], sizes="(min-width: 760px) 30vw, 50vw")}<figcaption>Vinho da Serra no deck</figcaption></figure>
      <figure>{pic("17-fogueira-entardecer-pessoa-golden", g["17-fogueira-entardecer-pessoa-golden"], sizes="(min-width: 760px) 30vw, 50vw")}<figcaption>Pets são bem-vindos</figcaption></figure>
    </div>
  </div>
</section>

<section class="band" id="avaliacoes">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Avaliações no Airbnb</span>
      <h2>O que os hóspedes escreveram</h2>
      <p class="lead">Avaliações reais, copiadas como foram publicadas no Airbnb.</p>
    </div>
    <div class="revs">
      {"".join(f'<figure class="rev"><div class="stars" aria-label="5 de 5 estrelas">★★★★★</div><blockquote>{"".join(f"<p>{html.escape(l)}</p>" for l in t.split(chr(10)))}</blockquote><figcaption><b>{html.escape(n)}</b><span>{d} · Airbnb</span></figcaption></figure>' for n, d, t in REVIEWS)}
    </div>
    <div style="margin-top:32px">{link("airbnb", "Ver todas as avaliações no Airbnb", "btn ghost")}</div>
  </div>
</section>

<section id="comodidades">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Comodidades</span>
      <h2>O que você encontra na cabana</h2>
    </div>
    <div class="amen">
      <div><h3>Conforto</h3><ul><li>Piso aquecido em todo o interior</li><li>Isolamento térmico e acústico</li><li>Ar-condicionado nos quartos e na sala</li><li>Lareira a lenha</li><li>Dois quartos com cama king e cortinas blackout</li><li>Chuveiro aquecido a boiler</li></ul></div>
      <div><h3>Cozinha</h3><ul><li>Fogão de indução</li><li>Forno elétrico</li><li>Micro-ondas</li><li>Geladeira com freezer</li><li>Utensílios e louças</li><li>Churrasqueira americana</li></ul></div>
      <div><h3>Lazer</h3><ul><li>Jacuzzi privativa até 40 °C</li><li>Hidromassagem e cromoterapia</li><li>Fogueira exclusiva com lenha inclusa</li><li>Deck com vista para o vale</li><li>Trilha na mata nativa</li></ul></div>
      <div><h3>Praticidade</h3><ul><li>Internet Starlink</li><li>TV na sala</li><li>Máquina lava e seca</li><li>Sem gás na cabana</li><li>Propriedade toda cercada</li><li>Pets sem taxa</li><li>Crianças bem-vindas</li></ul></div>
    </div>
  </div>
</section>

<section class="band" id="galeria">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Fotos</span>
      <h2>A cabana em cada estação e em cada hora do dia</h2>
    </div>
    <div class="gal" id="gal">
      {"".join(f'<button type="button" data-i="{i}" aria-label="Ampliar: {html.escape(a)}">{pic(n, a, sizes="(min-width: 900px) 25vw, 50vw")}</button>' for i, (n, a) in enumerate(GALERIA))}
    </div>
  </div>
</section>

<section id="regras">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Antes de reservar</span>
      <h2>Condições da hospedagem</h2>
    </div>
    <div class="rules">
      <div><strong>Check-in 15h</strong><span>Entrada a partir das 15h</span></div>
      <div><strong>Check-out 11h</strong><span>Saída até as 11h</span></div>
      <div><strong>2 noites</strong><span>Estadia mínima durante todo o ano</span></div>
      <div><strong>3 noites em feriados</strong><span>Réveillon (30/12, 31/12 e 01/01) e Carnaval</span></div>
      <div><strong>Até 4 hóspedes</strong><span>Crianças são bem-vindas</span></div>
      <div><strong>Pets de qualquer porte</strong><span>Sem taxa adicional</span></div>
      <div><strong>Lenha inclusa</strong><span>Um pacote por hospedagem</span></div>
      <div><strong>Sem gás</strong><span>Indução na cozinha e boiler no chuveiro</span></div>
    </div>
  </div>
</section>

<section class="band" id="perguntas">
  <div class="wrap faq">
    <div class="section-head">
      <span class="eyebrow">Perguntas frequentes</span>
      <h2>O que os hóspedes costumam perguntar</h2>
      <p class="lead">Não encontrou sua dúvida? Fale com a gente no WhatsApp.</p>
    </div>
    <div>
      {"".join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in FAQ)}
    </div>
  </div>
</section>

<section id="localizacao">
  <div class="wrap split">
    <div class="copy">
      <span class="eyebrow">Localização</span>
      <h2>No coração da região vinícola da Serra Gaúcha.</h2>
      <p>A cabana fica na zona rural de Farroupilha, cercada de campos e araucárias, e perto das vinícolas, cervejarias e roteiros mais procurados da Serra.</p>
      <div><a class="btn ghost" href="{LINKS["maps"]}" target="_blank" rel="noopener">Abrir no Google Maps</a></div>
    </div>
    <ol class="dist" aria-label="Tempo de carro até os principais pontos">
      <li><span>Blauth Bier</span><b>5 min</b></li>
      <li><span>Salto Ventoso</span><b>8 min</b></li>
      <li><span>Centro de Farroupilha</span><b>10 min</b></li>
      <li><span>Garibaldi</span><b>15 min</b></li>
      <li><span>Caminhos de Pedra</span><b>15 min</b></li>
      <li><span>Vale dos Vinhedos</span><b>20 min</b></li>
      <li class="foot">Tempos médios de carro a partir da cabana</li>
    </ol>
  </div>
</section>

<section class="reserve" id="reservar">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Reservas</span>
      <h2>Escolha como prefere reservar</h2>
      <p class="lead">A agenda é a mesma em todas as plataformas. Pelo WhatsApp você fala direto com a gente e pode parcelar no cartão de crédito.</p>
    </div>
    <div class="channels">
      {link("whatsapp", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19l-4 1z"/></svg> WhatsApp', "btn")}
      {link("airbnb", "Airbnb", "btn ghost")}
      {link("booking", "Booking.com", "btn ghost")}
      {link("holmy", "Holmy", "btn ghost")}
    </div>
    <p class="note">Zona rural de Farroupilha, Serra Gaúcha, Rio Grande do Sul.</p>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <img src="img/selo-bege.png" alt="Selo Cabana Bela Sardenha, Farroupilha, Brasil, desde 2022" width="400" height="472">
    <div>
      <div class="tag">Construindo memórias, despertando sentimentos.</div>
      <div>Cabana Bela Sardenha · Farroupilha · Serra Gaúcha · RS · desde 2022</div>
    </div>
    <div class="end"><a href="{LINKS["instagram"]}" target="_blank" rel="noopener">Instagram</a> · <a href="{LINKS["tiktok"]}" target="_blank" rel="noopener">TikTok</a><br>@cabanabelasardenha</div>
  </div>
</footer>

<dialog id="lb" aria-label="Foto ampliada">
  <img id="lb-img" alt="">
  <p id="lb-cap"></p>
  <div class="lb-nav"><button type="button" id="lb-prev">Anterior</button><button type="button" id="lb-close">Fechar</button><button type="button" id="lb-next">Próxima</button></div>
</dialog>

<script>
(() => {{
  const items = [...document.querySelectorAll('#gal button')];
  const lb = document.getElementById('lb'), im = document.getElementById('lb-img'), cap = document.getElementById('lb-cap');
  let cur = 0;
  const show = i => {{
    cur = (i + items.length) % items.length;
    const src = items[cur].querySelector('img');
    im.src = src.currentSrc.replace('-640.webp', '-1200.webp') || src.src; im.alt = src.alt; cap.textContent = src.alt;
  }};
  items.forEach((b, i) => b.addEventListener('click', () => {{ show(i); lb.showModal(); }}));
  document.getElementById('lb-prev').onclick = () => show(cur - 1);
  document.getElementById('lb-next').onclick = () => show(cur + 1);
  document.getElementById('lb-close').onclick = () => lb.close();
  lb.addEventListener('click', e => {{ if (e.target === lb) lb.close(); }});
  lb.addEventListener('keydown', e => {{ if (e.key === 'ArrowLeft') show(cur - 1); if (e.key === 'ArrowRight') show(cur + 1); }});
  document.querySelectorAll('.pendente').forEach(a => a.addEventListener('click', e => e.preventDefault()));
}})();
</script>
'''
open("index.html", "w", encoding="utf-8").write(out)
print("ok", len(out))

# ---------- versão para publicar (GitHub Pages) ----------
import os, shutil, datetime
cut = out.index('<header class="top">')
head, body = out[:cut], out[cut:]
doc = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
             .replace('<style>', '<style>\nbody {{ margin: 0 }}\n[hidden] {{ display: none !important }}'.replace('{{','{').replace('}}','}'), 1)
       + '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
os.makedirs("dist", exist_ok=True)
open("dist/index.html", "w", encoding="utf-8").write(doc)
if os.path.exists("dist/img"): shutil.rmtree("dist/img")
shutil.copytree("img", "dist/img", ignore=shutil.ignore_patterns("selo-terracota.png"))
open("dist/CNAME", "w").write("cabanabelasardenha.com.br\n")
open("dist/.nojekyll", "w").write("")
open("dist/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
today = datetime.date.today().isoformat()
open("dist/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE}/</loc><lastmod>{today}</lastmod></url></urlset>\n')
llms = ["# Cabana Bela Sardenha", "",
        "> Cabana A-frame única em propriedade privada e totalmente cercada de 6.000 m² na zona rural de Farroupilha, Serra Gaúcha (RS, Brasil). Piso aquecido em todo o interior, internet Starlink, jacuzzi aquecida privativa, lareira a lenha e fogueira exclusiva. Até 4 hóspedes, aceita pets sem taxa e crianças.", "",
        "## Perguntas frequentes", ""]
llms += [f"- **{q}** {a}" for q, a in FAQ]
llms += ["", "## Reservas", "",
         f"- WhatsApp (reserva direta, parcelamento no cartão): {LINKS['whatsapp']}",
         f"- Airbnb: {LINKS['airbnb']}", f"- Booking.com: {LINKS['booking']}", f"- Holmy: {LINKS['holmy']}",
         f"- Google Maps: {LINKS['maps']}", f"- Instagram e TikTok: @cabanabelasardenha", ""]
open("dist/llms.txt", "w", encoding="utf-8").write("\n".join(llms))
print("dist ok")
