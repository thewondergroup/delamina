# Generates the static pages. Run: python3 build.py
# Edit copy here (or in the generated HTML directly — both are fine).
import os

U = "https://www.delaminakitchen.co.uk/wp-content/uploads/"
IMG = {
    "hero": "images/hero.jpg",
    "mask": "images/mask.jpg",
    "logo": "images/logo.png",
    "mary_hero": "images/mary_hero.jpg",
    "east_hero": "images/east_hero.jpg",
    "town_hero": "images/town_hero.jpg",
    "mary_1": "images/mary_1.jpg",
    "mary_2": "images/mary_2.jpg",
    "brunch": "images/brunch.jpg",
    "group": "images/group.jpg",
    "east_1": "images/east_1.jpg",
    "east_2": "images/east_2.jpg",
    "green": "images/green.jpg",
    "family": "images/family.jpg",
    "garden": "images/garden.jpg",
    "town_1": "images/town_1.jpg",
    "town_2": "images/town_2.jpg",
    "town_3": "images/town_3.jpg",
    "drawing": "images/drawing.jpg",
    "snug": "images/snug.jpg",
    "arts": "images/arts.jpg",
    "spread": "images/spread.jpg",
    "xmas_table": "images/xmas-table.jpg",
    "xmas_cheers": "images/xmas-cheers.jpg",
    "mary_exterior": "images/mary-exterior.jpg",
    "mary_interior": "images/mary-interior.jpg",
    "wine": "images/wine.jpg",
    "cauliflower": "images/cauliflower.jpg",
    "limor": "images/limor.jpg",
    "founders": "images/founders.jpg",
    "cheers": "images/cheers.jpg",
    "prawns_spread": "images/prawns-spread.jpg",
    "table_overhead": "images/table-overhead.jpg",
    "lamb": "images/lamb.jpg",
    "beef": "images/beef.jpg",
    "burrata": "images/burrata.jpg",
    "window_table": "images/window-table.jpg",
    "pour": "images/pour.jpg",
    "limor_townhouse": "images/limor-townhouse.jpg",
    "dips": "images/dips.jpg",
    "prawns": "images/prawns.jpg",
    "fish_table": "images/fish-table.jpg",
    "prawns_blue": "images/prawns-blue.jpg",
    "wine_glass": "images/wine-glass.jpg",
    "tuna": "images/tuna.jpg",
    "xmas_dish": "images/xmas-dish.jpg",
}

BOOK = {
    "mary": "https://www.sevenrooms.com/explore/delaminamarylebone/reservations/create/search/?venues=delaminamarylebone,delaminatownhouse,delaminaeast",
    "east": "https://www.sevenrooms.com/explore/delaminaeast/reservations/create/search/?venues=delaminaeast,delaminatownhouse,delaminamarylebone",
    "town": "https://www.sevenrooms.com/explore/delaminatownhouse/reservations/create/search/?venues=delaminatownhouse,delaminamarylebone,delaminaeast",
}
GIFT = {
    "mary": "https://order.toasttab.com/egiftcards/delamina-marylebone",
    "east": "https://order.toasttab.com/egiftcards/delamina-east",
    "town": "https://order.toasttab.com/egiftcards/delamina-townhouse",
}
NEWSLETTER = "https://www.sevenrooms.com/explore/delaminagroup/subscription"
INSTAGRAM = "https://www.instagram.com/delaminakitchen/"

LOGO = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "delamina-logo.svg")).read().replace("<svg ", '<svg class="logo" ')

NAV = [
    ("restaurants", "index.html#restaurants", "Restaurants"),
    ("private-dining", "private-dining.html", "Private Dining"),
    ("whats-on", "whats-on.html", "What's On"),
    ("story", "our-story.html", "Our Story"),
    ("gifts", "gift-cards.html", "Gift Cards"),
]


def head(title, desc, body_class=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{IMG['logo']}">
<link rel="preload" href="fonts/inconsolata.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/style.css">
</head>
<body{(' class="' + body_class + '"') if body_class else ''}>
"""


def header(current="", book=BOOK["mary"], announce=True):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if k == current else ""}>{t}</a>' for k, h, t in NAV
    )
    mlinks = "".join(f'<a href="{h}">{t}</a>' for k, h, t in NAV)
    ann = '<div class="announce">Christmas 2026 at Delamina — festive menus and parties for 8 to 120 now booking <a href="whats-on.html#christmas">See the menus</a></div>\n' if announce else ''
    return ann + f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Delamina home">{LOGO}</a>
    <nav class="nav" aria-label="Main">{links}</nav>
    <a class="btn btn-dark btn-sm hdr-cta" href="{book}" target="_blank" rel="noopener">Book a table</a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
  <nav class="mobile-nav" aria-label="Mobile">{mlinks}<a href="{book}" target="_blank" rel="noopener">Book a table</a></nav>
</header>
"""


FOOTER = f"""<footer class="site-footer" id="contact">
  <div class="wrap">
    <div class="foot-grid">
      <div class="col">
        <p style="font-weight:300;max-width:300px">Seasonal dishes inspired by our Eastern Mediterranean home cooking. Family run, three London restaurants.</p>
        <div class="foot-links" style="margin-top:10px"><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a><a href="our-story.html#join">Join the team</a><a href="{NEWSLETTER}" target="_blank" rel="noopener">Newsletter</a></div>
      </div>
      <div class="col">
        <h4>Marylebone</h4>
        <span>56–58 Marylebone Lane<br>London W1U 2NX</span>
        <a href="tel:+442030266810">020 3026 6810</a>
        <span class="hrs">Mon–Fri 12–3.30pm, 5–9.30pm<br>Sat 10.30am–3.15pm, 5–9.30pm<br>Sun 10.30am–3.15pm, 5–9pm</span>
        <a href="marylebone.html" class="small" style="text-decoration:underline;text-underline-offset:4px">Restaurant page</a>
      </div>
      <div class="col">
        <h4>EAST</h4>
        <span>151–153 Commercial Street<br>London E1 6BJ</span>
        <a href="tel:+442070780770">020 7078 0770</a>
        <span class="hrs">Mon–Fri 12–9.30pm<br>Sat 11am–9.30pm<br>Sun 11am–8.30pm</span>
        <a href="east.html" class="small" style="text-decoration:underline;text-underline-offset:4px">Restaurant page</a>
      </div>
      <div class="col">
        <h4>Townhouse</h4>
        <span>13–15 Tavistock Street<br>London WC2E 7PS</span>
        <a href="tel:+442045865555">020 4586 5555</a>
        <span class="hrs">Mon–Sat 12–9.30pm<br>Sun 12–4pm</span>
        <a href="townhouse.html" class="small" style="text-decoration:underline;text-underline-offset:4px">Restaurant page</a>
      </div>
    </div>
    <div class="foot-mark" aria-hidden="true">{LOGO}</div>
    <div class="foot-bottom">
      <span>© 2026 Delamina Kitchen. Times shown are booking times — we stay open two hours after the last booking.</span>
      <span><a href="privacy.html">Privacy</a><a href="index.html#contact">Contact</a></span>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""


def venue_card(key, area, name, blurb, addr, hrs, img, page):
    return f"""<article class="card reveal">
  <a class="img" href="{page}"><img src="{img}" alt="{name}" loading="lazy"></a>
  <div class="body">
    <span class="eyebrow">{area}</span>
    <h3 style="font-size:26px">{name}</h3>
    <p style="font-weight:300">{blurb}</p>
    <p class="small muted">{addr}<br>{hrs}</p>
    <div class="btn-row" style="padding-top:4px">
      <a class="btn btn-solid btn-sm" href="{BOOK[key]}" target="_blank" rel="noopener">Book</a>
      <a class="btn btn-sm" href="{page}">Menus &amp; more</a>
    </div>
  </div>
</article>"""


# ---------------------------------------------------------------- HOME (v3)
# Flow: hero -> what's on -> menus -> founders -> private dining -> restaurants
def wcard(cls, href, img, when, title, text, cta, pos="center"):
    return f"""<a class="wcard {cls}" href="{href}">
      <img src="{img}" alt="" loading="lazy" style="object-position:{pos}">
      <div class="wcard-text">
        <span class="wcard-when">{when}</span>
        <h3>{title}</h3>
        <p>{text}</p>
        <span class="go">{cta} <b aria-hidden="true">&rarr;</b></span>
      </div>
    </a>"""


def mitems(rows):
    out = ""
    for name, desc, price in rows:
        d = f"<small>{desc}</small>" if desc else ""
        out += f'<div class="mi"><div class="mi-n"><span>{name}</span>{d}</div><div class="mi-p">{price}</div></div>'
    return out


def mpane(pid, hidden, blocks, note, links):
    secs = "".join(f'<div class="mblock"><h4>{t}</h4>{mitems(rows)}</div>' for t, rows in blocks)
    lk = "".join(f'<a class="mlink" href="menus/{f}" target="_blank" rel="noopener">{label}</a>' for label, f in links)
    return f"""<div class="mpane" data-menu-pane="{pid}"{' hidden' if hidden else ''}>
      {secs}
      <p class="mnote">{note}</p>
      <div class="mlinks"><span>Full menu (PDF)</span>{lk}</div>
    </div>"""


def room(img, venue, name, cap):
    return f"""<figure class="room-card">
      <div class="room-img"><img src="{img}" alt="{name}, Delamina {venue}" loading="lazy"></div>
      <figcaption><span class="room-venue">{venue}</span><span class="room-name">{name}</span><span class="room-cap">{cap}</span></figcaption>
    </figure>"""


def find_card(key, area, name, img, addr, hrs, phone, page, pos="center"):
    return f"""<article class="fcard reveal">
      <a class="fcard-img" href="{page}"><img src="{img}" alt="{name}" loading="lazy" style="object-position:{pos}"></a>
      <span class="eyebrow">{area}</span>
      <h3>{name}</h3>
      <p>{addr}</p>
      <p class="fcard-hrs">{hrs}</p>
      <a class="fcard-tel" href="tel:{phone[1]}">{phone[0]}</a>
      <div class="btn-row"><a class="btn btn-solid btn-sm" href="{BOOK[key]}" target="_blank" rel="noopener">Book a table</a><a class="btn btn-sm" href="{page}">Menus &amp; details</a></div>
    </article>"""


home = head("Delamina — Eastern Mediterranean restaurants in Marylebone, Shoreditch & Covent Garden",
            "Seasonal Eastern Mediterranean home cooking from Limor and Amir, at three London restaurants: Delamina Marylebone, Delamina EAST in Shoreditch and Delamina Townhouse in Covent Garden.",
            body_class="home")
home += header("", announce=False)
home += f"""
<main>
<section class="hx">
  <video class="hero-video" autoplay muted loop playsinline preload="auto" poster="images/hero-poster.jpg" aria-hidden="true"
    data-desktop="video/hero.mp4" data-mobile="video/hero-mobile.mp4" data-poster-mobile="images/hero-poster-mobile.jpg">
    <source src="video/hero.mp4" type="video/mp4">
  </video>
  <div class="hx-shade"></div>
  <div class="hx-center">
    <h1 class="hx-logo"><span class="sr-only">Delamina</span>{LOGO}</h1>
    <p class="hx-tag">Seasonal dishes inspired by our Eastern Mediterranean home cooking</p>
    <p class="hx-sub">Limor &amp; Amir's family kitchen, in three London neighbourhoods</p>
  </div>
  <nav class="bookbar" aria-label="Book a table">
    <a href="{BOOK['mary']}" target="_blank" rel="noopener"><span class="bb-k">Book a table</span><span class="bb-v">Marylebone</span><span class="bb-a">56–58 Marylebone Lane, W1</span><b aria-hidden="true">&rarr;</b></a>
    <a href="{BOOK['east']}" target="_blank" rel="noopener"><span class="bb-k">Book a table</span><span class="bb-v">Shoreditch</span><span class="bb-a">Delamina EAST, Commercial Street, E1</span><b aria-hidden="true">&rarr;</b></a>
    <a href="{BOOK['town']}" target="_blank" rel="noopener"><span class="bb-k">Book a table</span><span class="bb-v">Covent Garden</span><span class="bb-a">Delamina Townhouse, Tavistock Street, WC2</span><b aria-hidden="true">&rarr;</b></a>
  </nav>
  <button class="hero-pause" type="button" aria-label="Pause background video"><span></span></button>
</section>

<section id="whats-on" class="won">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">What's on</span><h2>This season at Delamina</h2></div>
      <a class="link" href="whats-on.html">Everything that's on</a>
    </div>
    <div class="won-grid">
      {wcard('wcard-feature','whats-on.html#christmas',IMG['xmas_table'],'Now booking','Christmas at Delamina','Feast sharing menus from £64 per guest, for tables of eight up to the whole restaurant.','Festive menus &amp; parties')}
      {wcard('','marylebone.html#menus',IMG['brunch'],'Weekends &amp; bank holidays','Weekend brunch','Shakshuka, the Jaffa–Tel Aviv breakfast and halva French toast, at Marylebone and EAST.','Brunch menu')}
      {wcard('','townhouse.html#menus',IMG['fish_table'],'Before the show','Pre-theatre, £27.5','Two courses before the curtain at the Townhouse, moments from the Royal Opera House.','Pre-theatre menu')}
      {wcard('','whats-on.html#pour-and-plate',IMG['wine'],'Wine dinners','Pour &amp; Plate','One producer, one long table, and a menu to match the bottles.','Next edition')}
      {wcard('','whats-on.html#founders',IMG['limor_townhouse'],'With Limor &amp; Amir','Founders’ Dinners','An evening at the table with the two people behind Delamina.','Dates &amp; tickets','center 30%')}
    </div>
  </div>
</section>

<section id="menus" class="menus">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Menus</span><h2>Grilled over charcoal, fragrant with herbs and spice, made to share</h2></div>
      <p>Limor's menus change with the seasons. The charred cauliflower, the shawarma and the dips never leave.</p>
    </div>
    <div class="menus-grid">
      <div class="menus-img"><img id="menu-photo" src="{IMG['cauliflower']}" alt="A dish from the Delamina menu"></div>
      <div class="menus-body">
        <div class="mtabs" role="tablist">
          <a href="#menus" class="mtab" data-menu-tab="alc" data-img="{IMG['cauliflower']}" aria-current="true">À la carte</a>
          <a href="#menus" class="mtab" data-menu-tab="brunch" data-img="{IMG['brunch']}">Brunch</a>
          <a href="#menus" class="mtab" data-menu-tab="pre" data-img="{IMG['fish_table']}">Pre-theatre</a>
          <a href="#menus" class="mtab" data-menu-tab="share" data-img="{IMG['spread']}">Sharing menus</a>
          <a href="#menus" class="mtab" data-menu-tab="wine" data-img="{IMG['pour']}">Wine</a>
        </div>
        {mpane('alc', False, [
            ("Snacks &amp; dips", [
                ("Hummus", "slow-roasted spiced tomatoes, crispy onions, pita", "10.5"),
                ("Smokey aubergine", "tahini &amp; zhoug, fluffy pita", "12"),
                ("Crispy oyster mushrooms", "truffled artichoke mousse, za’atar", "12.5"),
            ]),
            ("Mix &amp; match", [
                ("Charred cauliflower", "lemon-infused crème fraîche, pomegranate molasses &amp; seeds", "9 / 14 / 19"),
                ("Grilled courgette two-ways", "crispy onions, pine kernels, labneh drizzle", "13.5"),
            ]),
            ("Mains", [
                ("House beef shawarma", "dates &amp; pine nuts on grilled pita, house pickles, tahini", "24.5"),
                ("Lamb baharat on the grill", "charred hispi cabbage, lentils, barberries &amp; mint", "26"),
                ("Seabass chermoula", "butterflied and charcoal roasted, shoestring fries, herby yoghurt", "25"),
                ("Grilled tiger prawns", "za’atar focaccia, vine leaf &amp; roasted pepper chimichurri", "26"),
            ]),
        ], "A selection from the Marylebone menu. Each restaurant's menu is a little different.",
        [("Marylebone", "delamina-mary-alc.pdf"), ("EAST", "delamina-east-alc.pdf"), ("Townhouse", "delamina-town-alc.pdf")])}
        {mpane('brunch', True, [
            ("Weekends &amp; bank holidays, from 10.30am", [
                ("Jaffa–Tel Aviv style", "two eggs, a spread of mazetim, pita &amp; mixed bread", "17.5"),
                ("Shakshuka classic", "eggs cooked in tomatoes, peppers &amp; onions, a touch of chilli, pita", "15.5"),
                ("Green shakshuka", "feta, spinach, leeks, peas, caramelised onions, pita", "16"),
                ("Focaccia Benedict", "poached eggs, avocado with sumac, harissa hollandaise", "16"),
                ("Egg shawarma", "fried egg on beef shawarma with dates &amp; pine nuts, tahini", "23.5"),
                ("Cherry, halva &amp; pistachio French toast", "whipped labneh &amp; halva cream, cherry compote", "16"),
            ]),
        ], "A selection from the Marylebone brunch menu. Brunch is served at Marylebone and EAST.",
        [("Marylebone", "delamina-mary-brunch.pdf"), ("EAST weekend", "delamina-east-weekend.pdf")])}
        {mpane('pre', True, [
            ("Pre-theatre at the Townhouse · £27.5 per person", [
                ("Crispy oyster mushrooms", "truffled artichoke purée", "to start"),
                ("Kohlrabi carpaccio", "goats cheese, pistachios", "or"),
                ("Grilled chicken ras-el-hanout", "roasted sweet potato purée", "to follow"),
                ("Roasted seabass", "cavolo nero, giant couscous with roasted artichoke", "or"),
                ("Kubaneh to share", "tahini &amp; zhoug, smokey aubergine, salsa", "+13"),
            ]),
        ], "Served at Delamina Townhouse, Covent Garden. Tell us your curtain time when you book.",
        [("Townhouse pre-theatre", "delamina-town-pretheatre.pdf")])}
        {mpane('share', True, [
            ("For the whole table", [
                ("3-course sharing menu", "EAST £48 · Marylebone £54", "from 48"),
                ("Classics 4-course sharing menu", "EAST £57 · Marylebone £59 · Townhouse £59", "from 57"),
                ("Fish 4-course sharing menu", "Marylebone", "64"),
                ("Brunch classics sharing menu", "Marylebone", "33"),
                ("Christmas feast sharing menu", "EAST £64 · Marylebone £67 · Townhouse £69", "from 64"),
            ]),
        ], "Prices are per guest. Sharing menus are for groups and private dining.",
        [("Marylebone", "delamina-mary-group.pdf"), ("EAST", "delamina-east-sharing.pdf"), ("Townhouse", "delamina-town-sharing.pdf")])}
        {mpane('wine', True, [
            ("The list", [
                ("Small producers", "wines chosen from around the eastern Mediterranean and beyond", ""),
                ("House cocktails", "made with the same herbs and spices as the kitchen", ""),
                ("Drinks by mood at brunch", "mimosa blossom, limonana, fresh mint tea", ""),
            ]),
        ], "Each restaurant keeps its own list.",
        [("Marylebone", "delamina-mary-wine.pdf"), ("EAST", "delamina-east-wine.pdf"), ("Townhouse", "delamina-town-drinks.pdf")])}
      </div>
    </div>
  </div>
</section>

<section id="story" class="storyx">
  <div class="storyx-img"><img src="{IMG['founders']}" alt="Limor and Amir, founders of Delamina" loading="lazy"></div>
  <div class="storyx-text">
    <span class="eyebrow">Our story</span>
    <h2 class="reveal">Delamina is Limor and Amir: a husband and wife cooking the food they grew up on.</h2>
    <p class="reveal">Limor is self-taught. Her cooking comes from her father's kitchen and her family's Middle Eastern and European roots: plenty of vegetables, a charcoal grill, herbs and spices used generously. It started with a residency at Shoreditch House. Ten years and three restaurants later, she still writes every menu, and they still run it together as a family.</p>
    <p class="reveal">Her cookbook, <em>My Tel Aviv Table</em>, brings the same recipes home.</p>
    <div class="btn-row reveal"><a class="btn btn-light" href="our-story.html">Read our story</a><a class="btn btn-light" href="gift-cards.html#book">The cookbook</a></div>
  </div>
</section>

<section id="private-dining" class="pdx">
  <div class="wrap pdx-head">
    <span class="eyebrow">Private dining &amp; events</span>
    <h2 class="pdx-big reveal">A room of your own, and a table to share</h2>
    <div class="pdx-sub reveal">
      <p>Birthdays, launches, Christmas parties and long family lunches. Private rooms for eight guests up to a hundred and twenty, in Marylebone, Shoreditch and Covent Garden, with sharing menus from £48 per guest.</p>
      <div class="btn-row"><a class="btn btn-dark" href="private-dining.html#enquire">Make an enquiry</a><a class="btn" href="private-dining.html">See every room</a></div>
    </div>
  </div>
  <div class="rooms-rail" tabindex="0" aria-label="Private rooms, scroll sideways">
    {room(IMG['drawing'],'Townhouse','The Drawing Room','up to 50')}
    {room(IMG['garden'],'EAST','The Garden Room','up to 30')}
    {room(IMG['snug'],'Townhouse','The Big Snug','up to 20')}
    {room(IMG['mary_interior'],'Marylebone','Exclusive hire','75 seated · 120 standing')}
    {room(IMG['green'],'EAST','The Green Room','up to 10')}
    {room(IMG['arts'],'Townhouse','The Arts Room','up to 50')}
    {room(IMG['family'],'EAST','The Family Room','up to 14')}
  </div>
</section>

<section id="restaurants" class="find">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Our restaurants</span><h2>Find your Delamina</h2></div>
      <p>Three neighbourhoods, each with its own character. The cooking and the welcome are the same.</p>
    </div>
    <div class="find-grid">
      {find_card('mary','Marylebone','Delamina Marylebone',IMG['mary_exterior'],'56–58 Marylebone Lane, London W1U 2NX','Mon–Fri 12–3.30pm &amp; 5–9.30pm<br>Sat &amp; Sun brunch from 10.30am, dinner from 5pm',('020 3026 6810','+442030266810'),'marylebone.html')}
      {find_card('east','Shoreditch','Delamina EAST',IMG['east_2'],'151–153 Commercial Street, London E1 6BJ','Mon–Fri 12–9.30pm<br>Sat 11am–9.30pm · Sun 11am–8.30pm',('020 7078 0770','+442070780770'),'east.html','center 40%')}
      {find_card('town','Covent Garden','Delamina Townhouse',IMG['drawing'],'13–15 Tavistock Street, London WC2E 7PS','Mon–Sat 12–9.30pm<br>Sun 12–4pm',('020 4586 5555','+442045865555'),'townhouse.html')}
    </div>
  </div>
</section>

<section class="newsx">
  <div class="wrap newsx-inner">
    <div><h2>Hear it first</h2><p>New menus, Pour &amp; Plate dates and Founders' Dinners, once or twice a month.</p></div>
    <a class="btn btn-dark" href="{NEWSLETTER}" target="_blank" rel="noopener">Join the mailing list</a>
  </div>
</section>
</main>
"""
home += FOOTER


# ---------------------------------------------------------------- VENUE PAGES
def menu_pane(pid, hidden, sections, note):
    secs = ""
    for title, items in sections:
        rows = "".join(f'<div class="item"><span>{n}</span><span>{d}</span></div>' for n, d in items)
        secs += f"<div><h4>{title}</h4>{rows}</div>"
    return f'<div class="menu-list" data-menu-pane="{pid}"{" hidden" if hidden else ""}>{secs}<p class="note">{note}</p></div>'


def venue_page(key, slug, area, name, title, desc, intro, hero, addr, hours, phone, menus, menu_pdf, gallery, rooms_intro, rooms, rooms_img, band, map_q, alt_imgs):
    sw = ""
    for k, s, label in (("mary", "marylebone.html", "Marylebone"), ("east", "east.html", "EAST · Shoreditch"), ("town", "townhouse.html", "Townhouse · Covent Garden")):
        cur = ' aria-current="page"' if k == key else ""
        sw += f'<a class="tab" href="{s}"{cur}>{label}</a>'
    tabs = "".join(f'<a class="tab" href="#menus" data-menu-tab="m{i}"{" aria-current=\"true\"" if i == 0 else ""}>{m[0]}</a>' for i, m in enumerate(menus))
    panes = "".join(menu_pane(f"m{i}", i != 0, m[1], m[2]) for i, m in enumerate(menus))
    gal = "".join(f'<img src="{g}" alt="{name}" loading="lazy">' for g in gallery)
    rm = "".join(f'<div class="card card-plain reveal"><div class="img"><img src="{im}" alt="{rn}, {name}" loading="lazy"></div><div class="body"><div style="display:flex;justify-content:space-between;align-items:baseline;gap:16px"><h3 style="font-size:24px">{rn}</h3><span class="muted small">{cap}</span></div><p style="font-weight:300;font-size:15px">{rd}</p></div></div>' for rn, cap, rd, im in rooms)
    h = head(title, desc)
    h += header("restaurants", BOOK[key])
    h += f"""
<main>
<section class="venue-hero">
  <img src="{hero}" alt="{name}" fetchpriority="high">
  <div class="wrap">
    <span class="eyebrow">{area}</span>
    <h1>{name}</h1>
    <p class="lede" style="max-width:640px">{intro}</p>
    <div class="btn-row" style="margin-top:8px"><a class="btn btn-solid" href="{BOOK[key]}" target="_blank" rel="noopener">Book a table</a><a class="btn btn-light" href="#menus">Menus</a><a class="btn btn-light" href="#rooms">Private rooms</a></div>
  </div>
</section>
<div class="wrap"><div class="switcher"><span class="lbl">Our restaurants</span>{sw}</div></div>

<section class="section-tight">
  <div class="wrap split" style="grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);align-items:start">
    <div class="gallery">{gal}</div>
    <div class="info">
      <div class="k"><span class="eyebrow">Address</span><span>{addr}</span></div>
      <div class="k"><span class="eyebrow">Booking times</span><span>{hours}</span><span class="small muted">We stay open two hours after the last booking. Last orders 15 minutes after.</span></div>
      <div class="k"><span class="eyebrow">Contact</span><a href="tel:{phone[1]}">{phone[0]}</a><a href="private-dining.html#enquire">Private dining enquiries</a></div>
      <div class="btn-row" style="padding-top:8px"><a class="btn btn-solid btn-sm" href="{BOOK[key]}" target="_blank" rel="noopener">Book a table</a><a class="btn btn-sm" href="#map">Directions</a><a class="btn btn-sm" href="{GIFT[key]}" target="_blank" rel="noopener">Gift card</a></div>
    </div>
  </div>
</section>

<section id="menus" class="section">
  <div class="wrap">
    <div class="section-head">
      <div class="stack"><span class="eyebrow">Menus</span><h2>What's cooking at {area.split(' ·')[0] if key!='east' else 'EAST'}.</h2></div>
      <p class="lede" style="font-size:17px">Menus change with the seasons. The cauliflower and the dips never leave. The full current menus, with prices, are in the PDFs below.</p>
    </div>
    <div class="menu-tabs">{tabs}</div>
    {panes}
    <div class="btn-row" style="margin-top:32px"><span class="mlinks-label">Full menus (PDF)</span>{"".join(f'<a class="btn btn-sm" href="menus/{f}" target="_blank" rel="noopener">{l}</a>' for l, f in menu_pdf)}</div>
  </div>
</section>

<section class="section-tight band {'band-img' if band[5] else 'bg-olive'}"{(' style="background-image:linear-gradient(rgba(33,37,41,.74),rgba(33,37,41,.74)),url(' + band[5] + ');background-size:cover;background-position:center"') if band[5] else ''}>
  <div class="wrap">
    <div class="stack" style="display:flex;flex-direction:column;gap:10px"><span class="eyebrow">{band[0]}</span><h2>{band[1]}</h2><p style="max-width:560px;font-weight:300">{band[2]}</p></div>
    <a class="btn {'btn-light' if band[5] else 'btn-dark'}" href="{band[3]}" target="_blank" rel="noopener">{band[4]}</a>
  </div>
</section>

<section id="rooms" class="section">
  <div class="wrap">
    <div class="section-head">
      <div class="stack"><span class="eyebrow">Private dining at {name.replace('Delamina ','')}</span><h2>{rooms_intro[0]}</h2></div>
      <div style="display:flex;flex-direction:column;gap:20px"><p class="lede" style="font-size:17px">{rooms_intro[1]}</p><div class="btn-row"><a class="btn btn-solid" href="private-dining.html#enquire">Enquire</a><a class="btn" href="private-dining.html">Brochure &amp; all venues</a></div></div>
    </div>
    <div class="grid-3">{rm}</div>
  </div>
</section>

<section id="map" class="section bg-light">
  <div class="wrap map">
    <div class="stack" style="display:flex;flex-direction:column;gap:20px;justify-content:center">
      <span class="eyebrow">Find us</span>
      <h2>{map_q[0]}</h2>
      <p style="font-weight:300">{map_q[1]}</p>
      <div class="btn-row"><a class="btn btn-solid btn-sm" href="https://www.google.com/maps/search/?api=1&query={map_q[2]}" target="_blank" rel="noopener">Open in Maps</a><a class="btn btn-sm" href="tel:{phone[1]}">{phone[0]}</a></div>
    </div>
    <iframe title="Map — {name}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={map_q[2]}&output=embed"></iframe>
  </div>
</section>
</main>
"""
    h += FOOTER
    return h


ALC_NOTE = "Sample dishes shown — the full seasonal menu with prices is in the PDF. Dishes marked (v) are vegetarian; most of the menu can be made vegan or gluten-free, just ask."

marylebone = venue_page(
    "mary", "marylebone", "Marylebone", "Delamina Marylebone",
    "Delamina Marylebone — Eastern Mediterranean restaurant, Marylebone Lane",
    "Delamina Marylebone: seasonal Eastern Mediterranean brunch, lunch and dinner on Marylebone Lane, with private dining for 8 to 120.",
    "The original Delamina, a step off Marylebone High Street. Weekend brunch, long lunches and candlelit dinners over two floors — and the Family Room downstairs for parties.",
    IMG["mary_interior"], "56–58 Marylebone Lane<br>London W1U 2NX",
    "Mon – Fri 12 – 3.30pm &amp; 5 – 9.30pm<br>Sat 10.30am – 3.15pm &amp; 5 – 9.30pm<br>Sun 10.30am – 3.15pm &amp; 5 – 9pm",
    ("020 3026 6810", "+442030266810"),
    [
        ("À la carte", [("To start & share", [("The dips, warm pitta (v)", "all day"), ("Whole roasted cauliflower, tahini, pomegranate (v)", "signature"), ("Seasonal salads from the counter (v)", "")]), ("From the grill", [("Shawarma, carved to share", "signature"), ("Whole sea bass, herbs, lemon", ""), ("Lamb, chicken and vegetable skewers", "")])], ALC_NOTE),
        ("Brunch", [("Saturday, Sunday & bank holidays, 10.30am – 3.15pm", [("Shakshuka, green or red (v)", ""), ("Sabich, eggs and aubergine (v)", ""), ("Brunch dips board for the table (v)", ""), ("Fresh juices, house cocktails and mocktails", "")])], "Brunch is served Saturdays, Sundays and bank holidays. Booking recommended."),
        ("Wine list", [("Eastern Mediterranean & small producers", [("Wines from Greece, Lebanon, Israel, Turkey and Cyprus", ""), ("House cocktails made with the kitchen's own herbs and spices", ""), ("Mocktails and soft drinks", "")])], "Ask the team for what's open by the glass."),
    ],
    [("À la carte","delamina-mary-alc.pdf"),("Brunch","delamina-mary-brunch.pdf"),("Wine list","delamina-mary-wine.pdf"),("Group menus","delamina-mary-group.pdf")],
    [IMG["mary_exterior"], IMG["burrata"], IMG["pour"], IMG["window_table"]],
    ("One room for the family. Both floors for everyone.", "The Family Room downstairs seats 25 to 35 around long tables. Take both floors and it's 75 seated or 120 standing — the largest space in the group."),
    [("The Green Room", "8 – 10 guests", "A snug corner for a small dinner: one table, the door closed.", IMG["green"]),
     ("The Family Room", "25 – 35 guests", "Downstairs, long tables, sharing menus. Birthdays, team dinners, the family.", IMG["family"]),
     ("Exclusive hire", "75 seated · 120 standing", "Both floors, the bar and the kitchen, all yours.", IMG["mary_interior"])],
    IMG["family"],
    ("Weekend brunch", "Saturdays, Sundays and bank holidays from 10.30am.", "Shakshuka, dips, warm bread and fresh juices — the full spread until 3.15pm, then dinner from 5.", BOOK["mary"], "Book brunch", ""),
    ("A step off Marylebone High Street.", "56–58 Marylebone Lane, W1U 2NX. Bond Street (Elizabeth, Central, Jubilee) and Baker Street are both a few minutes' walk. Step-free access to the ground floor; please call ahead for the lower floor.", "Delamina+Marylebone+56-58+Marylebone+Lane+London+W1U+2NX"),
    [],
)

east = venue_page(
    "east", "east", "Shoreditch", "Delamina EAST",
    "Delamina EAST — Eastern Mediterranean restaurant, Shoreditch",
    "Delamina EAST on Commercial Street, Shoreditch: Eastern Mediterranean brunch, sharing plates and dinner, with three private rooms and exclusive hire.",
    "Big, bright and lively on Commercial Street, by Spitalfields. Brunch every weekend, sharing plates all day, and three private rooms including the Garden Room for thirty.",
    IMG["east_hero"], "151–153 Commercial Street<br>Shoreditch, London E1 6BJ",
    "Mon – Fri 12 – 9.30pm<br>Sat 11am – 9.30pm<br>Sun 11am – 8.30pm",
    ("020 7078 0770", "+442070780770"),
    [
        ("À la carte", [("To start & share", [("The dips, warm pitta (v)", "all day"), ("Whole roasted cauliflower, tahini, pomegranate (v)", "signature"), ("Seasonal salads from the counter (v)", "")]), ("From the grill", [("Shawarma, carved to share", "signature"), ("Whole sea bass, herbs, lemon", ""), ("Lamb, chicken and vegetable skewers", "")])], ALC_NOTE),
        ("Weekend menu", [("Saturday & Sunday from 11am, bank holidays too", [("Shakshuka, green or red (v)", ""), ("Sabich, eggs and aubergine (v)", ""), ("Brunch dips board for the table (v)", ""), ("Fresh juices, house cocktails and mocktails", "")])], "The weekend à la carte runs all day Saturday and Sunday."),
        ("Wine list", [("Small producers", [("A list built around small producers across the eastern Mediterranean", ""), ("House cocktails made with the kitchen's own aromatics", ""), ("Mocktails and soft drinks", "")])], "Ask the team for what's open by the glass."),
    ],
    [("À la carte","delamina-east-alc.pdf"),("Weekend","delamina-east-weekend.pdf"),("Wine list","delamina-east-wine.pdf"),("Sharing menus","delamina-east-sharing.pdf")],
    [IMG["east_1"], IMG["prawns_blue"], IMG["east_2"], IMG["table_overhead"]],
    ("Three rooms, or the whole restaurant.", "The Green Room for ten, the semi-private Family Room for fourteen, and the Garden Room for thirty. Or take the whole of EAST for a launch or a Christmas party."),
    [("The Green Room", "up to 10 guests", "One table, tucked away. Dinners, meetings, small birthdays.", IMG["green"]),
     ("The Family Room", "up to 14 guests", "Semi-private, in the thick of it. Long-table lunches and dinners.", IMG["family"]),
     ("The Garden Room", "up to 30 guests", "The big one. Seated dinners for thirty, or drinks and canapés standing.", IMG["garden"])],
    IMG["garden"],
    ("Weekend brunch", "Saturdays and Sundays from 11am. Bank holidays too.", "The full brunch spread until mid-afternoon, then straight into the evening menu — no gap, no rush.", BOOK["east"], "Book brunch", ""),
    ("Between Spitalfields and Shoreditch High Street.", "151–153 Commercial Street, E1 6BJ. Liverpool Street (Elizabeth, Central, Circle, Met, National Rail) is five minutes on foot; Shoreditch High Street Overground is three. Step-free access to the ground floor.", "Delamina+EAST+151-153+Commercial+Street+London+E1+6BJ"),
    [],
)

townhouse = venue_page(
    "town", "townhouse", "Covent Garden", "Delamina Townhouse",
    "Delamina Townhouse — Eastern Mediterranean restaurant, Covent Garden",
    "Delamina Townhouse: a restored Georgian townhouse on Tavistock Street, Covent Garden. Pre-theatre menus, à la carte dinner and private rooms for up to 50.",
    "A restored Georgian townhouse on Tavistock Street, two minutes from the Royal Opera House. Pre-theatre suppers and long lunches downstairs; drawing rooms for parties of fifty upstairs.",
    IMG["town_hero"], "13–15 Tavistock Street<br>Covent Garden, London WC2E 7PS",
    "Mon – Sat 12 – 9.30pm<br>Sun 12 – 4pm",
    ("020 4586 5555", "+442045865555"),
    [
        ("À la carte", [("To start & share", [("The dips, warm pitta (v)", "all day"), ("Whole roasted cauliflower, tahini, pomegranate (v)", "signature"), ("Seasonal salads from the counter (v)", "")]), ("From the grill", [("Whole sea bass, herbs, lemon", "signature"), ("Lamb, chicken and vegetable skewers", ""), ("Slow-roast lamb shoulder, for two", "")])], ALC_NOTE),
        ("Lunch & pre-theatre", [("Set menu, served until 6.30pm Monday – Saturday", [("Two courses", "set price"), ("Three courses", "set price"), ("A glass of wine or a house cocktail to go with it", "")])], "Tell us your curtain time when you book and we'll have you out in good time."),
        ("Drinks", [("Wines & cocktails", [("Wines from the eastern Mediterranean and small producers", ""), ("House cocktails made with the kitchen's own aromatics", ""), ("Mocktails and soft drinks", "")])], "Ask the team for what's open by the glass."),
    ],
    [("À la carte","delamina-town-alc.pdf"),("Lunch &amp; pre-theatre","delamina-town-pretheatre.pdf"),("Drinks","delamina-town-drinks.pdf"),("Sharing menu","delamina-town-sharing.pdf")],
    [IMG["wine"], IMG["town_1"], IMG["limor_townhouse"], IMG["town_2"]],
    ("Three rooms upstairs, and the whole house if you want it.", "One of the few proper Georgian townhouses left in Covent Garden. The Big Snug for twenty, the Drawing Room and the Arts Room for fifty each — or exclusive hire of the whole house."),
    [("The Big Snug", "up to 20 guests", "Low light, one long table, the door closed. Birthdays and board dinners.", IMG["snug"]),
     ("The Drawing Room", "up to 50 guests", "Tall windows over Tavistock Street. Seated dinners, or standing with drinks and canapés.", IMG["drawing"]),
     ("The Arts Room", "up to 50 guests", "The top floor. Launches, Christmas parties, wedding breakfasts.", IMG["arts"])],
    IMG["drawing"],
    ("Theatre district", "Curtain up at 7.30? Sit down at 5.30.", "A set pre-theatre menu served from midday to 6.30pm, Monday to Saturday — and we'll have you out in time.", BOOK["town"], "Book pre-theatre", IMG["town_3"]),
    ("Two minutes from Covent Garden tube.", "13–15 Tavistock Street, WC2E 7PS. Covent Garden (Piccadilly) and Charing Cross (Northern, Bakerloo, National Rail) are both a short walk. Step-free access to the ground floor; please call ahead for the upstairs rooms.", "Delamina+Townhouse+13-15+Tavistock+Street+London+WC2E+7PS"),
    [],
)


# ---------------------------------------------------------------- PRIVATE DINING
def room_block(anchor, area, name, page, intro, rooms, phone, img):
    rm = "".join(f'<div class="card card-plain reveal"><div class="img"><img src="{im}" alt="{rn}, {name}" loading="lazy"></div><div class="body"><div style="display:flex;justify-content:space-between;align-items:baseline;gap:16px"><h3 style="font-size:24px">{rn}</h3><span class="muted small">{cap}</span></div><p style="font-weight:300;font-size:15px">{rd}</p></div></div>' for rn, cap, rd, im in rooms)
    return f"""
<section id="{anchor}" class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head" style="align-items:end">
      <div class="stack"><span class="eyebrow">{area}</span><h2>{name}</h2></div>
      <div style="display:flex;flex-direction:column;gap:16px"><p class="lede" style="font-size:17px">{intro}</p><div class="btn-row"><a class="btn btn-solid btn-sm" href="#enquire">Enquire</a><a class="btn btn-sm" href="tel:{phone[1]}">{phone[0]}</a><a class="btn btn-sm" href="{page}">Restaurant page</a></div></div>
    </div>
    <div class="grid-3">{rm}</div>
  </div>
</section>"""


pd = head("Private Dining & Events — Delamina, London",
          "Private dining rooms and exclusive hire at Delamina Marylebone, Delamina EAST (Shoreditch) and Delamina Townhouse (Covent Garden). Nine rooms, 8 to 120 guests, sharing menus built for a crowd.")
pd += header("private-dining")
pd += f"""
<main>
<section class="venue-hero" style="min-height:56vh">
  <img src="{IMG['xmas_cheers']}" alt="A private dining party raising a toast" fetchpriority="high">
  <div class="wrap">
    <span class="eyebrow">Private dining &amp; events</span>
    <h1>Three private dining destinations, one warm Eastern Mediterranean table.</h1>
    <p class="lede" style="max-width:640px">Nine private rooms across Marylebone, Shoreditch and Covent Garden. Eight guests or a hundred and twenty, seated or standing, with sharing menus built for a crowd and a team who'll tailor the details.</p>
    <div class="btn-row" style="margin-top:8px"><a class="btn btn-solid" href="#enquire">Make an enquiry</a><a class="btn btn-light" href="#brochure">Download the brochure</a></div>
  </div>
</section>

<section class="section-tight bg-light">
  <div class="wrap" style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px" id="occasions">
    <div class="stat"><b>9</b><span>Private rooms</span></div>
    <div class="stat"><b>8 – 120</b><span>Guests</span></div>
    <div class="stat"><b>3</b><span>Neighbourhoods</span></div>
    <div class="stat"><b>1</b><span>Enquiry form for all of them</span></div>
  </div>
</section>

<section class="section" style="padding-bottom:40px">
  <div class="wrap">
    <div class="section-head">
      <div class="stack"><span class="eyebrow">Occasions</span><h2>Birthdays, launches, Christmas, the whole family.</h2></div>
      <p class="lede" style="font-size:17px">Seated dinners, drinks receptions, team lunches, engagement parties, wedding breakfasts and exclusive hires. Sharing menus from a set price per guest, with vegetarian, vegan and gluten-free covered as standard. Tell us the occasion and the number and we'll suggest the room.</p>
    </div>
  </div>
</section>

{room_block('marylebone','Marylebone · 56–58 Marylebone Lane','Delamina Marylebone','marylebone.html','The Family Room downstairs seats 25 to 35. Take both floors and it is 75 seated or 120 standing — the largest space in the group.',
  [("The Green Room","8 – 10 guests","A snug corner for a small dinner: one table, the door closed.",IMG['green']),("The Family Room","25 – 35 guests","Downstairs, long tables, sharing menus. Birthdays, team dinners, the family.",IMG['family']),("Exclusive hire","75 seated · 120 standing","Both floors, the bar and the kitchen, all yours.",IMG['mary_interior'])],("020 3026 6810","+442030266810"),IMG['family'])}

{room_block('shoreditch','Shoreditch · 151–153 Commercial Street','Delamina EAST','east.html','Three rooms — the Green Room for ten, the semi-private Family Room for fourteen, the Garden Room for thirty — or the whole restaurant for a launch or a Christmas party.',
  [("The Green Room","up to 10 guests","One table, tucked away. Dinners, meetings, small birthdays.",IMG['green']),("The Family Room","up to 14 guests","Semi-private, in the thick of it. Long-table lunches and dinners.",IMG['family']),("The Garden Room","up to 30 guests","The big one. Seated dinners for thirty, or drinks and canapés standing.",IMG['garden'])],("020 3026 6810","+442030266810"),IMG['garden'])}

{room_block('covent-garden','Covent Garden · 13–15 Tavistock Street','Delamina Townhouse','townhouse.html','One of the few proper Georgian townhouses left in Covent Garden. The Big Snug for twenty, the Drawing Room and the Arts Room for fifty each, or exclusive hire of the house. Video tours available on request.',
  [("The Big Snug","up to 20 guests","Low light, one long table, the door closed. Birthdays and board dinners.",IMG['snug']),("The Drawing Room","up to 50 guests","Tall windows over Tavistock Street. Seated dinners, or standing with drinks and canapés.",IMG['drawing']),("The Arts Room","up to 50 guests","The top floor. Launches, Christmas parties, wedding breakfasts.",IMG['arts'])],("020 4586 5555","+442045865555"),IMG['drawing'])}

<section id="menus" class="section-tight bg-olive band">
  <div class="wrap">
    <div class="stack" style="display:flex;flex-direction:column;gap:10px"><span class="eyebrow">Group menus</span><h2 style="color:var(--charcoal)">Sharing menus built for a crowd.</h2><p style="max-width:600px;font-weight:300">Everything comes to the middle of the table: dips and warm bread, the cauliflower, salads, grills and desserts. Set price per guest, menus for every diet, and a drinks package if you'd like one.</p></div>
    <a class="btn btn-dark" href="#enquire">Ask for the menus</a>
  </div>
</section>

<section id="enquire" class="section">
  <div class="wrap grid-2" style="align-items:start">
    <div class="stack" style="display:flex;flex-direction:column;gap:20px">
      <span class="eyebrow">Enquire</span>
      <h2>Tell us about the occasion.</h2>
      <p class="lede" style="font-size:17px">One form for all three restaurants. We'll come back within one working day with availability, the right room and the menus.</p>
      <div class="info" style="margin-top:8px">
        <div class="k"><span class="eyebrow">Marylebone &amp; EAST events</span><a href="tel:+442030266810">020 3026 6810</a></div>
        <div class="k"><span class="eyebrow">Townhouse events</span><a href="tel:+442045865555">020 4586 5555</a></div>
      </div>
      <div id="brochure" class="panel panel-dark" style="margin-top:8px">
        <span class="eyebrow">Brochure</span>
        <h3 style="font-size:24px">The private dining brochure</h3>
        <p style="font-weight:300;font-size:15px">Every room, capacity, floor plan and sample menu in one PDF. Leave your details and it's yours.</p>
        <form data-demo class="form-row" style="margin-top:4px">
          <label class="sr-only" for="b-name">Name</label><input id="b-name" type="text" placeholder="Name" required>
          <label class="sr-only" for="b-email">Email</label><input id="b-email" type="email" placeholder="Email" required>
          <button class="btn btn-light" type="submit">Send me the brochure</button>
          <p class="form-msg small" style="width:100%"></p>
        </form>
      </div>
    </div>
    <form data-demo class="form-grid panel panel-light" style="gap:16px">
      <div class="field"><label for="e-name">Your name</label><input id="e-name" type="text" required></div>
      <div class="field"><label for="e-email">Email</label><input id="e-email" type="email" required></div>
      <div class="field"><label for="e-phone">Phone</label><input id="e-phone" type="tel"></div>
      <div class="field"><label for="e-venue">Restaurant</label><select id="e-venue"><option>No preference — suggest one</option><option>Delamina Marylebone</option><option>Delamina EAST (Shoreditch)</option><option>Delamina Townhouse (Covent Garden)</option></select></div>
      <div class="field"><label for="e-date">Date</label><input id="e-date" type="date"></div>
      <div class="field"><label for="e-guests">Number of guests</label><input id="e-guests" type="number" min="8" max="120" placeholder="8 – 120"></div>
      <div class="field full"><label for="e-occ">Occasion</label><select id="e-occ"><option>Birthday</option><option>Corporate / team event</option><option>Christmas party</option><option>Engagement or wedding</option><option>Family gathering</option><option>Drinks reception</option><option>Exclusive hire</option><option>Something else</option></select></div>
      <div class="field full"><label for="e-notes">Anything else</label><textarea id="e-notes" placeholder="Timings, dietary needs, budget, the vibe…"></textarea></div>
      <div class="full btn-row" style="align-items:center;gap:20px"><button class="btn btn-solid" type="submit">Send enquiry</button><span class="form-msg small muted"></span></div>
    </form>
  </div>
</section>
</main>
"""
pd += FOOTER


# ---------------------------------------------------------------- OUR STORY
story = head("Our Story — Limor & Amir, Delamina", "Delamina is run by husband and wife Limor and Amir. Limor's self-taught Eastern Mediterranean cooking, a residency at Shoreditch House, three restaurants and a cookbook, My Tel Aviv Table.")
story += header("story")
story += f"""
<main>
<section class="wrap hero" style="padding-bottom:40px">
  <div class="stack">
    <span class="eyebrow">Our story</span>
    <h1>Home cooking, taken out to dinner.</h1>
    <p class="lede" style="max-width:540px">Delamina is Limor and Amir — a husband and wife who started with a residency at Shoreditch House and a menu of the dishes Limor grew up eating.</p>
  </div>
  <img class="hero-img" src="{IMG['limor']}" alt="Limor bringing dishes out from the kitchen" fetchpriority="high">
</section>

<section class="section-tight">
  <div class="wrap" style="max-width:820px;display:flex;flex-direction:column;gap:24px">
    <p class="lede">Limor's cooking is self-taught and intuitive. It comes from her father's kitchen — Middle Eastern and European heritage, a lot of vegetables, grilling and roasting, herbs and spices used generously — and from the simple idea that food should be wholesome, nutritious and full of flavour at the same time.</p>
    <p style="font-weight:300;font-size:17px">The first Delamina opened in Marylebone. Shoreditch followed — Delamina EAST, big and bright on Commercial Street — and then the Townhouse in Covent Garden, a restored Georgian house with drawing rooms upstairs. Ten years on, Limor still writes every menu, the restaurants are still family run, and the welcome is still the point.</p>
    <p style="font-weight:300;font-size:17px">The drinks follow the same logic: wines from small producers around the eastern Mediterranean, and house cocktails made with the same herbs and spices as the kitchen.</p>
  </div>
</section>

<section class="section bg-dark">
  <div class="wrap split">
    <img src="{IMG['founders']}" alt="Limor and Amir at the table" loading="lazy">
    <div class="stack">
      <span class="eyebrow">The cookbook</span>
      <h2>My Tel Aviv Table</h2>
      <p class="lede" style="font-size:17px;max-width:520px">Limor's debut cookbook: the recipes behind the restaurants, written for home kitchens. On the shelf at all three Delaminas, and the right present for anyone who's ever asked how we make the cauliflower.</p>
      <div class="btn-row"><a class="btn btn-light" href="gift-cards.html#book">Buy the book</a></div>
    </div>
  </div>
</section>

<section id="join" class="section">
  <div class="wrap grid-2" style="align-items:center">
    <div class="stack" style="display:flex;flex-direction:column;gap:20px">
      <span class="eyebrow">Join us</span>
      <h2>Come and work with us.</h2>
      <p class="lede" style="font-size:17px">Front of house, kitchen, management — across three restaurants we're nearly always looking for good people who like looking after other people. Send us a note and a CV.</p>
      <div class="btn-row"><a class="btn btn-solid" href="https://www.delaminakitchen.co.uk/join-us/" target="_blank" rel="noopener">Current roles</a></div>
    </div>
    <img src="{IMG['limor_townhouse']}" alt="Limor setting the table at Delamina Townhouse" loading="lazy" style="aspect-ratio:4/5;object-fit:cover;width:100%">
  </div>
</section>
</main>
"""
story += FOOTER


# ---------------------------------------------------------------- WHAT'S ON
won = head("What's On — Delamina", "Christmas 2026 at Delamina, Pour & Plate wine dinners, Founders' Dinners with Limor and Amir, and weekend brunch in Marylebone and Shoreditch.")
won += header("whats-on")
won += f"""
<main>
<section class="wrap hero" style="padding-bottom:40px">
  <div class="stack">
    <span class="eyebrow">What's on</span>
    <h1>Reasons to come back.</h1>
    <p class="lede" style="max-width:540px">Festive menus, wine dinners, evenings with the founders and the weekend brunch that never stops.</p>
  </div>
  <img class="hero-img" src="{IMG['xmas_dish']}" alt="A festive dish at Delamina" fetchpriority="high">
</section>

<section id="christmas" class="section bg-olive">
  <div class="wrap split" style="grid-template-columns:minmax(0,1.1fr) minmax(0,1fr)">
    <div class="stack">
      <span class="eyebrow">Now booking</span>
      <h2 style="color:var(--charcoal)">Christmas 2026</h2>
      <p style="font-weight:300;font-size:17px;max-width:560px">Festive sharing menus across all three restaurants from late November to Christmas Eve, parties from 8 to 120, and exclusive hires of the Garden Room, the Drawing Room, the Arts Room and both floors at Marylebone. Menus for every diet, drinks packages if you want them.</p>
      <div class="btn-row"><a class="btn btn-dark" href="private-dining.html#enquire">Book a party</a><a class="btn" href="menus/delamina-mary-xmas.pdf" target="_blank" rel="noopener">Marylebone menu · £67</a><a class="btn" href="menus/delamina-east-xmas.pdf" target="_blank" rel="noopener">EAST menu · £64</a><a class="btn" href="menus/delamina-town-xmas.pdf" target="_blank" rel="noopener">Townhouse menu · £69</a></div>
    </div>
    <img src="{IMG['xmas_table']}" alt="A Christmas table at Delamina" loading="lazy">
  </div>
</section>

<section id="pour-and-plate" class="section">
  <div class="wrap grid-3">
    <div class="tile reveal"><span class="eyebrow">Wine dinners</span><h3>Pour &amp; Plate</h3><p>Our numbered wine dinner series — one producer from around the eastern Mediterranean, one long table, a menu Limor builds around their bottles. Tickets go to the mailing list first.</p><a class="link" href="{NEWSLETTER}" target="_blank" rel="noopener">Get the next date</a></div>
    <div id="founders" class="tile reveal"><span class="eyebrow">With Limor &amp; Amir</span><h3>Founders' Dinners</h3><p>An evening at the table with the two people behind Delamina, cooking the dishes that started it all and telling the stories behind them.</p><a class="link" href="{NEWSLETTER}" target="_blank" rel="noopener">Dates &amp; tickets</a></div>
    <div id="brunch" class="tile reveal"><span class="eyebrow">Every weekend</span><h3>Weekend brunch</h3><p>Shakshuka, sabich, the dips board and fresh juices. Saturdays, Sundays and bank holidays at Marylebone (from 10.30am) and EAST (from 11am).</p><a class="link" href="marylebone.html#menus">Brunch menu</a></div>
  </div>
</section>

<section class="section-tight bg-light">
  <div class="wrap panel" style="padding:0;flex-direction:row;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:24px">
    <div class="stack" style="display:flex;flex-direction:column;gap:8px"><span class="eyebrow">Newsletter</span><h3 style="font-size:26px">Hear about it first.</h3><p style="font-weight:300">One or two emails a month: new menus, Pour &amp; Plate dates and the odd table-only offer.</p></div>
    <a class="btn btn-dark" href="{NEWSLETTER}" target="_blank" rel="noopener">Join the mailing list</a>
  </div>
</section>
</main>
"""
won += FOOTER


# ---------------------------------------------------------------- GIFT CARDS
gifts = head("Gift Cards — Delamina", "Delamina e-gift cards for Marylebone, EAST (Shoreditch) and the Townhouse (Covent Garden), plus Limor's cookbook My Tel Aviv Table.")
gifts += header("gifts")
gifts += f"""
<main>
<section class="wrap hero" style="padding-bottom:40px">
  <div class="stack">
    <span class="eyebrow">Gift cards</span>
    <h1>Give someone the table.</h1>
    <p class="lede" style="max-width:540px">E-gift cards for any Delamina, sent by email instantly or on the day you choose. Pick the restaurant they'd love.</p>
  </div>
  <img class="hero-img" src="{IMG['cheers']}" alt="Two glasses raised at Delamina" fetchpriority="high">
</section>
<section class="section-tight">
  <div class="wrap grid-3">
    <a class="card reveal" href="{GIFT['mary']}" target="_blank" rel="noopener" style="background:var(--light)"><div class="img"><img src="{IMG['mary_interior']}" alt="Delamina Marylebone" loading="lazy"></div><div class="body"><span class="eyebrow">Marylebone</span><h3>Delamina Marylebone</h3><span class="link">Buy a gift card</span></div></a>
    <a class="card reveal" href="{GIFT['east']}" target="_blank" rel="noopener" style="background:var(--light)"><div class="img"><img src="{IMG['east_hero']}" alt="Delamina EAST" loading="lazy"></div><div class="body"><span class="eyebrow">Shoreditch</span><h3>Delamina EAST</h3><span class="link">Buy a gift card</span></div></a>
    <a class="card reveal" href="{GIFT['town']}" target="_blank" rel="noopener" style="background:var(--light)"><div class="img"><img src="{IMG['town_hero']}" alt="Delamina Townhouse" loading="lazy"></div><div class="body"><span class="eyebrow">Covent Garden</span><h3>Delamina Townhouse</h3><span class="link">Buy a gift card</span></div></a>
  </div>
</section>
<section id="book" class="section bg-dark">
  <div class="wrap split">
    <img src="{IMG['cauliflower']}" alt="Whole roasted cauliflower" loading="lazy">
    <div class="stack">
      <span class="eyebrow">The cookbook</span>
      <h2>My Tel Aviv Table</h2>
      <p class="lede" style="font-size:17px;max-width:520px">Limor's debut cookbook — the recipes behind the restaurants, written for home kitchens. Available at all three Delaminas, or order a copy below.</p>
      <div class="btn-row"><a class="btn btn-light" href="https://www.delaminakitchen.co.uk/my-tel-aviv-table-book" target="_blank" rel="noopener">Order the book</a></div>
    </div>
  </div>
</section>
</main>
"""
gifts += FOOTER


# ---------------------------------------------------------------- PRIVACY (stub)
privacy = head("Privacy Policy — Delamina", "Delamina Kitchen privacy policy.")
privacy += header("")
privacy += """
<main><section class="section"><div class="wrap" style="max-width:820px;display:flex;flex-direction:column;gap:20px">
<span class="eyebrow">Privacy</span><h1>Privacy policy</h1>
<p class="lede">Copy the current policy from <a href="https://www.delaminakitchen.co.uk/privacy-policy/" style="text-decoration:underline">delaminakitchen.co.uk/privacy-policy</a> into this page before launch.</p>
</div></section></main>
"""
privacy += FOOTER

pages = {
    "index.html": home, "marylebone.html": marylebone, "east.html": east, "townhouse.html": townhouse,
    "private-dining.html": pd, "our-story.html": story, "whats-on.html": won, "gift-cards.html": gifts, "privacy.html": privacy,
}
here = os.path.dirname(os.path.abspath(__file__))
for name, html in pages.items():
    with open(os.path.join(here, name), "w") as f:
        f.write(html)
    print("wrote", name, len(html))
