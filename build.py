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
    ("menus", "menus.html", "Menus"),
    ("private-dining", "private-dining.html", "Private Dining"),
    ("whats-on", "whats-on.html", "What's On"),
    ("story", "our-story.html", "Our Story"),
    ("gifts", "gift-cards.html", "Gift Cards"),
]

T = "images/thumb/"


def mcard(href, img, eyebrow, title, text):
    return f'''<a class="mega-card" href="{href}"><span class="mega-img"><img src="{T}{img}.jpg" alt="" loading="lazy"></span><span class="mega-eyebrow">{eyebrow}</span><span class="mega-title">{title}</span><span class="mega-text">{text}</span></a>'''


def mcol(img, eyebrow, title, page, links):
    lk = "".join(f'<a href="{page}#{h}">{l}</a>' for l, h in links)
    return f'''<div class="mega-col"><a class="mega-img" href="{page}"><img src="{T}{img}.jpg" alt="" loading="lazy"></a><span class="mega-eyebrow">{eyebrow}</span><a class="mega-title" href="{page}">{title}</a><div class="mega-links">{lk}</div></div>'''


MEGA = {
    "restaurants": '<div class="mega-grid mega-3">' + mcard("marylebone.html", "mary-exterior", "Marylebone", "Delamina Marylebone", "56–58 Marylebone Lane, W1") + mcard("east.html", "east_2", "Shoreditch", "Delamina EAST", "151–153 Commercial Street, E1") + mcard("townhouse.html", "drawing", "Covent Garden", "Delamina Townhouse", "13–15 Tavistock Street, WC2") + "</div>",
    "menus": '<div class="mega-grid mega-3">' + mcol("burrata", "Marylebone", "Delamina Marylebone", "menu-marylebone.html", [("À la carte", "a-la-carte"), ("Brunch", "brunch"), ("Sharing menus", "sharing"), ("Christmas", "christmas"), ("Wine", "wine")]) + mcol("prawns-blue", "Shoreditch", "Delamina EAST", "menu-east.html", [("À la carte", "a-la-carte"), ("Weekend brunch", "weekend"), ("Sharing menus", "sharing"), ("Christmas", "christmas"), ("Wine", "wine")]) + mcol("fish-table", "Covent Garden", "Delamina Townhouse", "menu-townhouse.html", [("À la carte", "a-la-carte"), ("Pre-theatre", "pre-theatre"), ("Sharing menu", "sharing"), ("Christmas", "christmas"), ("Cocktails &amp; wine", "drinks")]) + "</div>",
    "private-dining": '<div class="mega-grid mega-4">' + mcard("private-dining.html#marylebone", "mary-interior", "Marylebone", "Up to 120 guests", "The Family Room, or both floors") + mcard("private-dining.html#shoreditch", "garden", "Shoreditch", "Up to 30 guests", "Green Room, Family Room, Garden Room") + mcard("private-dining.html#covent-garden", "snug", "Covent Garden", "Up to 50 guests", "Big Snug, Drawing Room, Arts Room") + '<div class="mega-cta"><span class="mega-title">Planning something?</span><span class="mega-text">Tell us the occasion and the numbers and we\'ll suggest the room.</span><a class="btn btn-solid btn-sm" href="private-dining.html#enquire">Make an enquiry</a><a class="btn btn-sm" href="private-dining.html#brochure">Get the brochure</a></div></div>',
    "whats-on": '<div class="mega-grid mega-4">' + mcard("whats-on.html#christmas", "xmas-table", "Now booking", "Christmas at Delamina", "Feast menus from £64 per guest") + mcard("whats-on.html#new-year", "cheers", "31 December", "New Year\'s Eve", "See the year out at the table") + mcard("whats-on.html#brunch", "brunch", "Every weekend", "Weekend brunch", "Marylebone and EAST") + mcard("whats-on.html#pour-and-plate", "wine", "Wine dinners", "Pour &amp; Plate", "One producer, one long table") + "</div>",
}


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
    links = ""
    for k, h, t in NAV:
        cur = ' aria-current="page"' if k == current else ""
        if k in MEGA:
            links += f'<div class="nav-item has-mega"><a class="nav-link" href="{h}"{cur} aria-haspopup="true">{t}</a><div class="mega"><div class="wrap">{MEGA[k]}</div></div></div>'
        else:
            links += f'<div class="nav-item"><a class="nav-link" href="{h}"{cur}>{t}</a></div>'
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
    lk = "".join(f'<a class="mlink" href="{f}">{label}</a>' for label, f in links)
    return f"""<div class="mpane" data-menu-pane="{pid}"{' hidden' if hidden else ''}>
      {secs}
      <p class="mnote">{note}</p>
      <div class="mlinks"><span>Full menu</span>{lk}</div>
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
</section>

<section id="whats-on" class="won">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">What's on</span><h2>This season at Delamina</h2></div>
      <a class="link" href="whats-on.html">Everything that's on</a>
    </div>
    <div class="won-grid">
      {wcard('wcard-feature','whats-on.html#christmas',IMG['xmas_table'],'Now booking','Christmas at Delamina','Feast sharing menus from £64 per guest, for tables of eight up to the whole restaurant.','Festive menus &amp; parties')}
      {wcard('','menu-marylebone.html#brunch',IMG['brunch'],'Weekends &amp; bank holidays','Weekend brunch','Shakshuka, the Jaffa–Tel Aviv breakfast and halva French toast, at Marylebone and EAST.','Brunch menu')}
      {wcard('','menu-townhouse.html#pre-theatre',IMG['fish_table'],'Before the show','Pre-theatre, £27.5','Two courses before the curtain at the Townhouse, moments from the Royal Opera House.','Pre-theatre menu')}
      {wcard('','whats-on.html#pour-and-plate',IMG['wine'],'Wine dinners','Pour &amp; Plate','One producer, one long table, and a menu to match the bottles.','Next edition')}
      {wcard('','whats-on.html#new-year',IMG['cheers'],'31 December','New Year\u2019s Eve','See the year out around the table, with a feast menu made for sharing and a glass raised at midnight.','Details &amp; booking','center 60%')}
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
        [("Marylebone", "menu-marylebone.html#a-la-carte"), ("EAST", "menu-east.html#a-la-carte"), ("Townhouse", "menu-townhouse.html#a-la-carte")])}
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
        [("Marylebone", "menu-marylebone.html#brunch"), ("EAST", "menu-east.html#weekend")])}
        {mpane('pre', True, [
            ("Pre-theatre at the Townhouse · £27.5 per person", [
                ("Crispy oyster mushrooms", "truffled artichoke purée", "to start"),
                ("Kohlrabi carpaccio", "goats cheese, pistachios", "or"),
                ("Grilled chicken ras-el-hanout", "roasted sweet potato purée", "to follow"),
                ("Roasted seabass", "cavolo nero, giant couscous with roasted artichoke", "or"),
                ("Kubaneh to share", "tahini &amp; zhoug, smokey aubergine, salsa", "+13"),
            ]),
        ], "Served at Delamina Townhouse, Covent Garden. Tell us your curtain time when you book.",
        [("Townhouse pre-theatre", "menu-townhouse.html#pre-theatre")])}
        {mpane('share', True, [
            ("For the whole table", [
                ("3-course sharing menu", "EAST £48 · Marylebone £54", "from 48"),
                ("Classics 4-course sharing menu", "EAST £57 · Marylebone £59 · Townhouse £59", "from 57"),
                ("Fish 4-course sharing menu", "Marylebone", "64"),
                ("Brunch classics sharing menus", "Marylebone £33 and £39", "from 33"),
                ("Christmas feast sharing menu", "EAST £64 · Marylebone £67 · Townhouse £69", "from 64"),
            ]),
        ], "Prices are per guest. Sharing menus are for groups and private dining.",
        [("Marylebone", "menu-marylebone.html#sharing"), ("EAST", "menu-east.html#sharing"), ("Townhouse", "menu-townhouse.html#sharing")])}
        {mpane('wine', True, [
            ("The list", [
                ("Small producers", "wines chosen from around the eastern Mediterranean and beyond", ""),
                ("House cocktails", "made with the same herbs and spices as the kitchen", ""),
                ("Drinks by mood at brunch", "mimosa blossom, limonana, fresh mint tea", ""),
            ]),
        ], "Each restaurant keeps its own list.",
        [("Marylebone", "menu-marylebone.html#wine"), ("EAST", "menu-east.html#wine"), ("Townhouse", "menu-townhouse.html#drinks")])}
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
    <div><h2>Hear it first</h2><p>New menus, Pour &amp; Plate dates and first word on Christmas and New Year, once or twice a month.</p></div>
    <a class="btn btn-dark" href="{NEWSLETTER}" target="_blank" rel="noopener">Join the mailing list</a>
  </div>
</section>
</main>
"""
home += FOOTER


# ---------------------------------------------------------------- VENUE PAGES
import json as _json
_MENUS = _json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "menus.json"), encoding="utf-8"))
_TAGNAME = {"VG": "Vegan and dairy free", "V": "Vegetarian", "GF": "Gluten free", "DF": "Dairy free"}


def bgvideo(name, cls="hero-video"):
    """Looping background video: wide cut on desktop, vertical cut on phones."""
    return (f'<video class="{cls}" autoplay muted loop playsinline preload="auto" poster="video/{name}.jpg" aria-hidden="true" '
            f'data-desktop="video/{name}.mp4" data-mobile="video/{name}-mobile.mp4" data-poster-mobile="video/{name}-mobile.jpg"></video>')


def reel(name, caption):
    """Vertical clip that loads and plays only when scrolled into view."""
    return (f'<figure class="reel"><video muted loop playsinline preload="none" poster="video/reel-{name}.jpg" data-lazy="video/reel-{name}.mp4" aria-hidden="true"></video>'
            f'<figcaption>{caption}</figcaption></figure>')


def reels(items, eyebrow="", title=""):
    head_ = f'<div class="wrap reels-head"><span class="eyebrow">{eyebrow}</span><h2>{title}</h2></div>' if title else ""
    return f'<section class="reels">{head_}<div class="reels-row">{"".join(reel(n, c) for n, c in items)}</div></section>'


def pick_dishes(venue, wanted):
    out = ""
    for sec in _MENUS[venue]["alc"]:
        for it in sec["items"]:
            if any(it["text"].startswith(w) for w in wanted):
                tg = "".join(f'<abbr class="tg" title="{_TAGNAME[t]}">{t}</abbr>' for t in it.get("tags", []))
                out += f'<div class="ml-item"><div class="ml-text"><span>{it["text"]} {tg}</span></div><div class="ml-price">{it.get("price", "")}</div></div>'
    return out


VENUES = {
    "mary": dict(
        slug="marylebone.html", menu="menu-marylebone.html", data="marylebone", video="hero-marylebone",
        area="Marylebone", name="Delamina Marylebone",
        title="Delamina Marylebone — Eastern Mediterranean restaurant, Marylebone Lane",
        desc="Delamina Marylebone: Eastern Mediterranean brunch, lunch and dinner on Marylebone Lane, with private dining for 8 to 120.",
        tag="The original Delamina, a step off Marylebone High Street",
        statement="Where Delamina started: two floors on Marylebone Lane, a charcoal grill, and a table that fills up with plates.",
        about="Come for a long lunch, a candlelit dinner or brunch at the weekend, when the shakshuka and the Jaffa–Tel Aviv breakfast take over until mid-afternoon. Downstairs, the Family Room seats up to 35 for parties.",
        facts=["Lunch &amp; dinner daily", "Brunch at weekends &amp; bank holidays", "Private rooms for 8 to 120", "Card payments only"],
        addr="56–58 Marylebone Lane", post="London W1U 2NX", phone=("020 3026 6810", "+442030266810"),
        hours=[("Monday – Friday", "12 – 3.30pm · 5 – 9.30pm"), ("Saturday", "Brunch 10.30am – 3.15pm · 5 – 9.30pm"), ("Sunday", "Brunch 10.30am – 3.15pm · 5 – 9pm")],
        today=["10.30am – 3.15pm and 5 – 9pm", "12 – 3.30pm and 5 – 9.30pm", "12 – 3.30pm and 5 – 9.30pm", "12 – 3.30pm and 5 – 9.30pm", "12 – 3.30pm and 5 – 9.30pm", "12 – 3.30pm and 5 – 9.30pm", "10.30am – 3.15pm and 5 – 9.30pm"],
        dishes=["Smokey aubergine", "Charred cauliflower", "House beef shawarma", "Lamb baharat", "Seabass chermoula", "Grilled tiger prawns"],
        menu_reel=("lamb", "Lamb, off the grill"),
        menus=[("À la carte", "a-la-carte"), ("Brunch", "brunch"), ("Sharing menus", "sharing"), ("Christmas", "christmas"), ("Wine", "wine")],
        reels=[("egg", "Egg shawarma, weekend brunch"), ("fish", "Seabass on the charcoal grill"), ("cocktail", "Something to start"), ("dessert", "Save room")],
        won=[("menu-marylebone.html#brunch", "brunch", "Weekends &amp; bank holidays", "Weekend brunch", "From 10.30am: shakshuka, the Jaffa–Tel Aviv breakfast and halva French toast.", "Brunch menu", "center"),
             ("menu-marylebone.html#christmas", "xmas_table", "Now booking", "Christmas feast", "A feast sharing menu at £67 per guest, for tables and private parties.", "Christmas menu", "center"),
             ("whats-on.html#new-year", "cheers", "31 December", "New Year’s Eve", "See the year out around the table.", "Details", "center 60%")],
        pd_title="The Family Room downstairs, or both floors to yourselves",
        pd_text="Sharing menus from £54 per guest, with brunch sharing menus from £33.",
        rooms=[("The Green Room", "8 – 10 guests", "One table and a closed door, for a small dinner."),
               ("The Family Room", "25 – 35 guests", "Downstairs, at long tables. Birthdays, team dinners, the whole family."),
               ("Exclusive hire", "75 seated · 120 standing", "Both floors, the bar and the kitchen.")],
        pd_img="mary_interior", pd_anchor="marylebone",
        find="A step off Marylebone High Street",
        travel="Bond Street station (Elizabeth, Central and Jubilee lines) is about five minutes' walk.",
        mapq="Delamina+Marylebone+56-58+Marylebone+Lane+London+W1U+2NX",
    ),
    "east": dict(
        slug="east.html", menu="menu-east.html", data="east", video="hero-east",
        area="Shoreditch", name="Delamina EAST",
        title="Delamina EAST — Eastern Mediterranean restaurant, Shoreditch",
        desc="Delamina EAST on Commercial Street, Shoreditch: Eastern Mediterranean sharing plates, weekend brunch and three private rooms.",
        tag="Big, bright and lively on Commercial Street",
        statement="Delamina's home in the east: a big, bright room on Commercial Street, between Spitalfields and Shoreditch High Street.",
        about="Open all day from noon, with brunch specials at the weekend and the charcoal grill going through to dinner. Three private rooms sit off the main restaurant, the largest seating thirty.",
        facts=["Open all day from noon", "Brunch specials at weekends", "Three private rooms", "Card payments only"],
        addr="151–153 Commercial Street", post="London E1 6BJ", phone=("020 7078 0770", "+442070780770"),
        hours=[("Monday – Friday", "12 – 9.30pm"), ("Saturday", "11am – 9.30pm"), ("Sunday", "11am – 8.30pm")],
        today=["11am – 8.30pm", "12 – 9.30pm", "12 – 9.30pm", "12 – 9.30pm", "12 – 9.30pm", "12 – 9.30pm", "11am – 9.30pm"],
        dishes=["Carpaccio of golden beetroot", "Lettuce cups", "Charred cauliflower", "Angus beef koftas", "House beef rump shawarma", "Whole crispy seabass"],
        menu_reel=("fish", "Seabass on the charcoal grill"),
        menus=[("À la carte", "a-la-carte"), ("Weekend brunch", "weekend"), ("Sharing menus", "sharing"), ("Christmas", "christmas"), ("Wine", "wine")],
        reels=[("coffee", "Behind the bar"), ("lamb", "Lamb, off the grill"), ("mazetim", "Dinner at EAST"), ("dessert", "Save room")],
        won=[("menu-east.html#weekend", "brunch", "Saturdays &amp; Sundays", "Weekend brunch", "Brunch specials until 3.30pm, alongside the full menu.", "Weekend menu", "center"),
             ("menu-east.html#christmas", "xmas_table", "Now booking", "Christmas feast", "A feast sharing menu at £64 per guest, for tables and private parties.", "Christmas menu", "center"),
             ("whats-on.html#new-year", "cheers", "31 December", "New Year’s Eve", "See the year out around the table.", "Details", "center 60%")],
        pd_title="Three private rooms, or the whole restaurant",
        pd_text="Sharing menus from £48 per guest.",
        rooms=[("The Green Room", "up to 10 guests", "One table, tucked away. Dinners, meetings, small birthdays."),
               ("The Family Room", "up to 14 guests", "Semi-private, for long-table lunches and dinners."),
               ("The Garden Room", "up to 30 guests", "Seated dinners for thirty, or drinks and canapés standing."),
               ("Exclusive hire", "the whole restaurant", "For launches and Christmas parties.")],
        pd_img="garden", pd_anchor="shoreditch",
        find="Between Spitalfields and Shoreditch High Street",
        travel="Shoreditch High Street (Overground) and Liverpool Street (Elizabeth, Central, Circle and Metropolitan lines, National Rail) are both a short walk.",
        mapq="Delamina+EAST+151-153+Commercial+Street+London+E1+6BJ",
    ),
    "town": dict(
        slug="townhouse.html", menu="menu-townhouse.html", data="townhouse", video="hero-townhouse",
        area="Covent Garden", name="Delamina Townhouse",
        title="Delamina Townhouse — Eastern Mediterranean restaurant, Covent Garden",
        desc="Delamina Townhouse: a restored Georgian townhouse on Tavistock Street, Covent Garden. Pre-theatre menu, cocktails and private rooms for up to 50.",
        tag="A Georgian townhouse in the heart of theatreland",
        statement="A restored Georgian townhouse on Tavistock Street, moments from the Royal Opera House.",
        about="Lunch, dinner and a pre-theatre menu at £27.5, with house cocktails made from the same herbs and spices as the kitchen. The private rooms, the Big Snug, the Drawing Room and the Arts Room, host dinners and parties for up to fifty.",
        facts=["Pre-theatre menu, £27.5", "House cocktails", "Private rooms for up to 50", "Open Monday to Sunday"],
        addr="13–15 Tavistock Street", post="London WC2E 7PS", phone=("020 4586 5555", "+442045865555"),
        hours=[("Monday – Saturday", "12 – 9.30pm"), ("Sunday", "12 – 4pm")],
        today=["12 – 4pm", "12 – 9.30pm", "12 – 9.30pm", "12 – 9.30pm", "12 – 9.30pm", "12 – 9.30pm", "12 – 9.30pm"],
        dishes=["Kubaneh", "Roasted cauliflower", "Beef & lamb koftas", "Beef shawarma", "Whole crispy seabass", "Za’atar giant prawns"],
        menu_reel=("champagne", "House cocktails at the bar"),
        menus=[("À la carte", "a-la-carte"), ("Pre-theatre", "pre-theatre"), ("Sharing menu", "sharing"), ("Christmas", "christmas"), ("Cocktails &amp; wine", "drinks")],
        reels=[("fish", "Seabass on the charcoal grill"), ("cheers", "To a good evening"), ("lamb", "Lamb, off the grill"), ("dessert", "Save room")],
        won=[("menu-townhouse.html#pre-theatre", "fish_table", "Before the show", "Pre-theatre, £27.5", "Two courses before the curtain. Tell us your show time when you book.", "Pre-theatre menu", "center"),
             ("menu-townhouse.html#christmas", "xmas_table", "Now booking", "Christmas feast", "A feast sharing menu at £69 per guest, for tables and private parties.", "Christmas menu", "center"),
             ("whats-on.html#new-year", "cheers", "31 December", "New Year’s Eve", "See the year out around the table.", "Details", "center 60%")],
        pd_title="Three private rooms, or the whole house",
        pd_text="The Classics sharing menu is £59 per guest.",
        rooms=[("The Big Snug", "up to 20 guests", "One long table and a closed door. Birthdays and board dinners."),
               ("The Drawing Room", "up to 50 guests", "Tall windows over Tavistock Street. Seated, or standing with drinks."),
               ("The Arts Room", "up to 50 guests", "Launches, Christmas parties, wedding breakfasts."),
               ("Exclusive hire", "the whole house", "Every room, for your party.")],
        pd_img="drawing", pd_anchor="covent-garden",
        find="Two minutes from the Royal Opera House",
        travel="Covent Garden station (Piccadilly line) is a few minutes' walk. Charing Cross and Temple are also close.",
        mapq="Delamina+Townhouse+13-15+Tavistock+Street+London+WC2E+7PS",
    ),
}


def venue_page(key):
    v = VENUES[key]
    hours_rows = "".join(f'<div class="hr-row"><span>{d}</span><span>{t}</span></div>' for d, t in v["hours"])
    today = _json.dumps(v["today"]).replace('"', "&quot;")
    facts = "".join(f"<li>{f}</li>" for f in v["facts"])
    mlinks = "".join(f'<a class="mlink" href="{v["menu"]}#{h}">{l}</a>' for l, h in v["menus"])
    cards = "".join(wcard("", href, IMG[img], when, ttl, txt, cta, pos) for href, img, when, ttl, txt, cta, pos in v["won"])
    rooms_ = "".join(f'<div class="rr"><div class="rr-top"><h3>{n}</h3><span>{c}</span></div><p>{d}</p></div>' for n, c, d in v["rooms"])
    others = "".join(find_card(k, o["area"], o["name"], IMG[{"mary": "mary_exterior", "east": "east_2", "town": "drawing"}[k]], o["addr"] + ", " + o["post"], "<br>".join(f"{d}: {t}" for d, t in o["hours"]), o["phone"], o["slug"]) for k, o in VENUES.items() if k != key)
    short = "EAST" if key == "east" else ("the Townhouse" if key == "town" else "Marylebone")
    h = head(v["title"], v["desc"])
    h += header("restaurants", BOOK[key])
    h += f"""
<main class="vp">
<section class="hx vp-hero">
  {bgvideo(v["video"])}
  <div class="hx-shade"></div>
  <div class="hx-center">
    <span class="vp-area">{v["area"]}</span>
    <h1 class="vp-name">{v["name"]}</h1>
    <p class="hx-sub">{v["tag"]}</p>
  </div>
  <nav class="bookbar infobar" aria-label="{v["name"]} essentials">
    <a href="{BOOK[key]}" target="_blank" rel="noopener"><span class="bb-k">Reserve</span><span class="bb-v">Book a table</span><b aria-hidden="true">&rarr;</b></a>
    <a href="#hours"><span class="bb-k">Bookings today</span><span class="bb-v bb-s" data-today="{today}">See opening hours</span><b aria-hidden="true">&rarr;</b></a>
    <a href="#find"><span class="bb-k">Find us</span><span class="bb-v bb-s">{v["addr"]}</span><b aria-hidden="true">&rarr;</b></a>
    <a href="tel:{v["phone"][1]}"><span class="bb-k">Call</span><span class="bb-v bb-s">{v["phone"][0]}</span><b aria-hidden="true">&rarr;</b></a>
  </nav>
</section>

<section class="vp-intro">
  <div class="wrap vp-intro-grid">
    <div class="vp-about">
      <span class="eyebrow">The restaurant</span>
      <h2 class="reveal">{v["statement"]}</h2>
      <p class="reveal">{v["about"]}</p>
      <ul class="vp-facts reveal">{facts}</ul>
    </div>
    <aside class="vp-hours reveal" id="hours">
      <span class="eyebrow">Booking times</span>
      {hours_rows}
      <p class="vp-hours-note">We stay open for two hours after the last booking.</p>
      <div class="btn-row"><a class="btn btn-dark" href="{BOOK[key]}" target="_blank" rel="noopener">Book a table</a><a class="btn" href="tel:{v["phone"][1]}">{v["phone"][0]}</a></div>
    </aside>
  </div>
</section>

<section id="menus" class="vp-menu">
  <div class="wrap vp-menu-grid">
    {reel(*v["menu_reel"])}
    <div class="vp-menu-body">
      <span class="eyebrow">On the menu</span>
      <h2>A taste of {short}</h2>
      <div class="ml vp-dishes">{pick_dishes(v["data"], v["dishes"])}</div>
      <p class="mnote">A few dishes from the à la carte. Menus change with the seasons.</p>
      <div class="mlinks"><span>Full menus</span>{mlinks}</div>
    </div>
  </div>
</section>

{reels(v["reels"])}

<section class="won vp-won">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">What's on</span><h2>Happening at {short}</h2></div><a class="link" href="whats-on.html">Everything that's on</a></div>
    <div class="won-grid won-3">{cards}</div>
  </div>
</section>

<section id="rooms" class="pdx vp-pd">
  <div class="wrap vp-pd-grid">
    <div>
      <span class="eyebrow">Private dining at {short}</span>
      <h2 class="pdx-big reveal">{v["pd_title"]}</h2>
      <p class="vp-pd-text">{v["pd_text"]}</p>
      <div class="rrs">{rooms_}</div>
      <div class="btn-row"><a class="btn btn-dark" href="private-dining.html#enquire">Make an enquiry</a><a class="btn" href="private-dining.html#{v["pd_anchor"]}">See the rooms</a><a class="btn" href="{v["menu"]}#sharing">Sharing menus</a></div>
    </div>
    <div class="vp-pd-img"><img src="{IMG[v["pd_img"]]}" alt="Private dining at {v["name"]}" loading="lazy"></div>
  </div>
</section>

<section id="find" class="vp-find">
  <div class="wrap map">
    <div class="vp-find-text">
      <span class="eyebrow">Find us</span>
      <h2>{v["find"]}</h2>
      <p class="vp-addr">{v["addr"]}<br>{v["post"]}</p>
      <p>{v["travel"]}</p>
      <div class="btn-row"><a class="btn btn-solid btn-sm" href="https://www.google.com/maps/search/?api=1&query={v["mapq"]}" target="_blank" rel="noopener">Open in Maps</a><a class="btn btn-sm" href="tel:{v["phone"][1]}">{v["phone"][0]}</a></div>
    </div>
    <iframe title="Map — {v["name"]}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={v["mapq"]}&output=embed"></iframe>
  </div>
</section>

<section class="find vp-others">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">Our other restaurants</span><h2>Same kitchen, two more neighbourhoods</h2></div></div>
    <div class="find-grid find-2">{others}</div>
  </div>
</section>
</main>
"""
    return h + FOOTER


marylebone = venue_page("mary")
east = venue_page("east")
townhouse = venue_page("town")


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
  {bgvideo("hero-private")}
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

{reels([("fish", "Seabass on the charcoal grill"), ("lamb", "Lamb, off the grill"), ("egg", "Egg shawarma, weekend brunch"), ("dessert", "Save room")], "From the kitchen", "Cooked over charcoal, every day")}

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
won = head("What's On — Delamina", "Christmas 2026 and New Year's Eve at Delamina, Pour & Plate wine dinners, and weekend brunch in Marylebone and Shoreditch.")
won += header("whats-on")
won += f"""
<main>
<section class="wrap hero" style="padding-bottom:40px">
  <div class="stack">
    <span class="eyebrow">What's on</span>
    <h1>Reasons to come back.</h1>
    <p class="lede" style="max-width:540px">Festive menus, New Year's Eve, wine dinners and the weekend brunch that never stops.</p>
  </div>
  <video class="hero-img" autoplay muted loop playsinline preload="auto" poster="video/reel-xmas.jpg" src="video/reel-xmas.mp4" aria-label="Christmas at Delamina"></video>
</section>

<section id="christmas" class="section bg-olive">
  <div class="wrap split" style="grid-template-columns:minmax(0,1.1fr) minmax(0,1fr)">
    <div class="stack">
      <span class="eyebrow">Now booking</span>
      <h2 style="color:var(--charcoal)">Christmas 2026</h2>
      <p style="font-weight:300;font-size:17px;max-width:560px">Festive sharing menus across all three restaurants from late November to Christmas Eve, parties from 8 to 120, and exclusive hires of the Garden Room, the Drawing Room, the Arts Room and both floors at Marylebone. Menus for every diet, drinks packages if you want them.</p>
      <div class="btn-row"><a class="btn btn-dark" href="private-dining.html#enquire">Book a party</a><a class="btn" href="menu-marylebone.html#christmas">Marylebone menu · £67</a><a class="btn" href="menu-east.html#christmas">EAST menu · £64</a><a class="btn" href="menu-townhouse.html#christmas">Townhouse menu · £69</a></div>
    </div>
    <img src="{IMG['xmas_table']}" alt="A Christmas table at Delamina" loading="lazy">
  </div>
</section>

{reels([("cheers", "To a good evening"), ("xmas", "Christmas in Covent Garden"), ("champagne", "House cocktails"), ("mazetim", "The whole table")])}

<section id="pour-and-plate" class="section">
  <div class="wrap grid-3">
    <div class="tile reveal"><span class="eyebrow">Wine dinners</span><h3>Pour &amp; Plate</h3><p>Our numbered wine dinner series — one producer from around the eastern Mediterranean, one long table, a menu Limor builds around their bottles. Tickets go to the mailing list first.</p><a class="link" href="{NEWSLETTER}" target="_blank" rel="noopener">Get the next date</a></div>
    <div id="new-year" class="tile reveal"><span class="eyebrow">31 December</span><h3>New Year's Eve</h3><p>See the year out around the table, with a feast menu made for sharing and a glass raised at midnight. Details go to the mailing list first.</p><a class="link" href="{NEWSLETTER}" target="_blank" rel="noopener">Details &amp; booking</a></div>
    <div id="brunch" class="tile reveal"><span class="eyebrow">Every weekend</span><h3>Weekend brunch</h3><p>Shakshuka, sabich, the dips board and fresh juices. Saturdays, Sundays and bank holidays at Marylebone (from 10.30am) and EAST (from 11am).</p><a class="link" href="menu-marylebone.html#brunch">Brunch menu</a></div>
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
  <video class="hero-img" autoplay muted loop playsinline preload="auto" poster="video/reel-cheers.jpg" src="video/reel-cheers.mp4" aria-label="Glasses raised at Delamina"></video>
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

# ---------------------------------------------------------------- MENU PAGES
# Menu content lives in data/menus.json (taken from the restaurants' current menus).
import json
MENUS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "menus.json"), encoding="utf-8"))


def tags_html(tags):
    return "".join(f'<abbr class="tg" title="{TAGNAME[t]}">{t}</abbr>' for t in tags)


TAGNAME = {"VG": "Vegan and dairy free", "V": "Vegetarian", "GF": "Gluten free", "DF": "Dairy free"}


def r_list(secs):
    out = ""
    for sec in secs:
        sub = f'<span>{sec["sub"]}</span>' if sec.get("sub") else ""
        rows = ""
        for it in sec["items"]:
            name = f'<b class="ml-name">{it["name"]}</b>' if it.get("name") else ""
            extra = f'<small>{it["extra"]}</small>' if it.get("extra") else ""
            tg = tags_html(it.get("tags", []))
            rows += f'<div class="ml-item"><div class="ml-text">{name}<span>{it["text"]} {tg}</span>{extra}</div><div class="ml-price">{it.get("price", "")}</div></div>'
        out += f'<section class="ml-sec"><h3>{sec["title"]}{sub}</h3>{rows}</section>'
    return f'<div class="ml">{out}</div>'


def r_set_one(m):
    body = ""
    for b in m["blocks"]:
        k = b["k"]
        if k == "head":
            body += f'<h4>{b["text"]}</h4>'
        elif k == "sep":
            body += '<hr>'
        elif k == "or":
            body += f'<p class="setm-or">{"and" if b["text"] == "&" else b["text"]}</p>'
        elif k == "label":
            body += f'<p class="setm-label">{b["text"]}</p>'
        else:
            extra = f' <small>({b["extra"]})</small>' if b.get("extra") else ""
            body += f'<p class="setm-item">{b["text"]} {tags_html(b.get("tags", []))}{extra}</p>'
    notes = "".join(f'<p class="setm-note">{n}</p>' for n in m.get("notes", []))
    return body + notes


def r_sets(menus):
    if len(menus) == 1:
        m = menus[0]
        sub = f'<p class="setm-sub">{m["sub"]}</p>' if m.get("sub") else ""
        price = f'<p class="setm-price">{m["price"]}</p>' if m.get("price") else ""
        return f'<article class="setm"><h3>{m["title"]}</h3>{price}{sub}{r_set_one(m)}</article>'
    out = ""
    for i, m in enumerate(menus):
        out += f'<details class="setm setm-acc"{" open" if i == 0 else ""}><summary><span>{m["title"]}</span><b>{m.get("price", "")}</b></summary><div class="setm-body">{r_set_one(m)}</div></details>'
    return out


def r_wine(cats, note=""):
    out = ""
    for c in cats:
        rows = ""
        for st in c["styles"]:
            if st["title"]:
                rows += f'<h4>{st["title"]}</h4>'
            for w in st["wines"]:
                rows += f'<div class="wl-row"><div class="wl-name"><span>{w["name"]}</span><small>{w["note"]}</small></div><div class="wl-p">{w["g"]}</div><div class="wl-p">{w["c"]}</div><div class="wl-p">{w["b"]}</div></div>'
        out += f'<section class="wl-sec"><div class="wl-head"><h3>{c["title"]}</h3><span>Glass</span><span>Carafe</span><span>Bottle</span></div>{rows}</section>'
    n = f'<p class="mp-note">{note}</p>' if note else ""
    return f'<div class="wl">{out}{n}<p class="mp-note">V vegetarian · VG vegan · O organic · S sustainable · CS certified sustainable</p></div>'


FOOD_NOTE = '<p class="mp-note">VG vegan and dairy free · V vegetarian · GF gluten free · DF dairy free</p><p class="mp-note">Our food is prepared in a kitchen where there are nuts and other allergens. Please let your server know if you have a food allergy or intolerance. A discretionary service charge is added to your bill and is fully shared between the team.</p>'


def menu_page(key, slug, name, area, tabs, extra_note=""):
    """tabs: list of (id, label, intro, html)"""
    sw = ""
    for k, pg, label in (("mary", "menu-marylebone.html", "Marylebone"), ("east", "menu-east.html", "EAST · Shoreditch"), ("town", "menu-townhouse.html", "Townhouse · Covent Garden")):
        cur = ' aria-current="page"' if k == key else ""
        sw += f'<a class="tab" href="{pg}"{cur}>{label}</a>'
    tb = "".join(f'<a class="mtab" href="#{tid}" data-menu-tab="{tid}" data-hash="1"{" aria-current=\"true\"" if i == 0 else ""}>{label}</a>' for i, (tid, label, intro, html) in enumerate(tabs))
    panes = ""
    for i, (tid, label, intro, html) in enumerate(tabs):
        it = f'<p class="mp-intro">{intro}</p>' if intro else ""
        panes += f'<div class="mp-pane" id="{tid}" data-menu-pane="{tid}"{" hidden" if i else ""}><h2>{label}</h2>{it}{html}</div>'
    h = head(f"Menus — {name}", f"The current menus at {name}, {area}: à la carte, sharing menus, Christmas and the wine list, with prices.")
    h += header("menus", BOOK[key])
    h += f"""
<main class="mp">
<section class="mp-head">
  <div class="wrap">
    <span class="eyebrow">Menus · {area}</span>
    <h1>{name}</h1>
    <div class="mp-switch"><span class="lbl">Menus for</span>{sw}</div>
  </div>
</section>
<div class="mp-tabs"><div class="wrap"><div class="mtabs">{tb}</div><a class="btn btn-solid btn-sm" href="{BOOK[key]}" target="_blank" rel="noopener">Book a table</a></div></div>
<section class="wrap mp-body">
  {panes}
  <div class="mp-foot">{FOOD_NOTE}{extra_note}<p class="mp-note">Menus change with the seasons, so dishes and prices may differ slightly on the day.</p></div>
</section>
</main>
"""
    return h + FOOTER


M = MENUS["marylebone"]
menu_marylebone = menu_page("mary", "marylebone", "Delamina Marylebone", "Marylebone", [
    ("a-la-carte", "À la carte", "", r_list(M["alc"])),
    ("brunch", "Brunch", M.get("brunch_sub", ""), r_list(M["brunch"])),
    ("sharing", "Sharing menus", "For groups and private dining. Prices are per guest.", r_sets(M["sharing"])),
    ("christmas", "Christmas", "", r_sets(M["xmas"])),
    ("wine", "Wine", "", r_wine(M["wine"])),
], '<p class="mp-note">We do not accept cash payment.</p>')

M = MENUS["east"]
menu_east = menu_page("east", "east", "Delamina EAST", "Shoreditch", [
    ("a-la-carte", "À la carte", "", r_list(M["alc"])),
    ("weekend", "Weekend brunch", "Saturdays and Sundays, served alongside the à la carte.", r_list(M["weekend"])),
    ("sharing", "Sharing menus", "For groups and private dining. Prices are per guest.", r_sets(M["sharing"])),
    ("christmas", "Christmas", "", r_sets(M["xmas"])),
    ("wine", "Wine", "", r_wine(M["wine"])),
], '<p class="mp-note">We do not accept cash payment.</p>')

M = MENUS["townhouse"]
menu_townhouse = menu_page("town", "townhouse", "Delamina Townhouse", "Covent Garden", [
    ("a-la-carte", "À la carte", "", r_list(M["alc"])),
    ("pre-theatre", "Pre-theatre", "", r_sets(M["pretheatre"])),
    ("sharing", "Sharing menu", "For groups and private dining.", r_sets(M["sharing"])),
    ("christmas", "Christmas", "", r_sets(M["xmas"])),
    ("drinks", "Cocktails &amp; wine", "", r_list(M["cocktails"]) + '<p class="mp-note">Classic cocktails and a large selection of spirits (50ml) are also available.</p>' + r_wine(M["wine"], "Glass 125ml, carafe 375ml. Dessert wines by the 75ml glass.")),
])


def hub_col(img, area, name, page, links, book):
    lk = "".join(f'<a class="menu-row" href="{page}#{h}"><span>{l}</span><b aria-hidden="true">&rarr;</b></a>' for l, h in links)
    return f"""<article class="fcard reveal">
      <a class="fcard-img" href="{page}"><img src="{img}" alt="{name}" loading="lazy"></a>
      <span class="eyebrow">{area}</span>
      <h3>{name}</h3>
      <div class="menu-rows">{lk}</div>
    </article>"""


menus_hub = head("Menus — Delamina", "The current menus at Delamina Marylebone, Delamina EAST and Delamina Townhouse: à la carte, brunch, pre-theatre, sharing menus, Christmas and wine.")
menus_hub += header("menus")
menus_hub += f"""
<main>
<section class="mp-head">
  <div class="wrap">
    <span class="eyebrow">Menus</span>
    <h1>Choose your Delamina</h1>
    <p class="lede" style="max-width:620px;margin-top:18px">The cooking is the same family kitchen at all three. Each restaurant's menu is a little different.</p>
  </div>
</section>
<section class="find">
  <div class="wrap find-grid">
    {hub_col(IMG['burrata'], 'Marylebone', 'Delamina Marylebone', 'menu-marylebone.html', [("À la carte", "a-la-carte"), ("Brunch", "brunch"), ("Sharing menus", "sharing"), ("Christmas", "christmas"), ("Wine", "wine")], BOOK['mary'])}
    {hub_col(IMG['prawns_blue'], 'Shoreditch', 'Delamina EAST', 'menu-east.html', [("À la carte", "a-la-carte"), ("Weekend brunch", "weekend"), ("Sharing menus", "sharing"), ("Christmas", "christmas"), ("Wine", "wine")], BOOK['east'])}
    {hub_col(IMG['fish_table'], 'Covent Garden', 'Delamina Townhouse', 'menu-townhouse.html', [("À la carte", "a-la-carte"), ("Pre-theatre", "pre-theatre"), ("Sharing menu", "sharing"), ("Christmas", "christmas"), ("Cocktails &amp; wine", "drinks")], BOOK['town'])}
  </div>
</section>
</main>
"""
menus_hub += FOOTER

pages = {
    "index.html": home, "marylebone.html": marylebone, "east.html": east, "townhouse.html": townhouse,
    "private-dining.html": pd, "our-story.html": story, "whats-on.html": won, "gift-cards.html": gifts, "privacy.html": privacy,
    "menus.html": menus_hub, "menu-marylebone.html": menu_marylebone, "menu-east.html": menu_east, "menu-townhouse.html": menu_townhouse,
}
here = os.path.dirname(os.path.abspath(__file__))
for name, html in pages.items():
    with open(os.path.join(here, name), "w") as f:
        f.write(html)
    print("wrote", name, len(html))
