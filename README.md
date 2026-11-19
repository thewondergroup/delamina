# Delamina — website

Static site, no build step needed to deploy. Upload the folder to a GitHub repo and turn on GitHub Pages.

## Pages
- `index.html` — homepage
- `marylebone.html`, `east.html`, `townhouse.html` — one per restaurant (menus, hours, private rooms, map)
- `private-dining.html` — all nine rooms, enquiry form, brochure request
- `our-story.html` — Limor & Amir, the cookbook, Join us
- `whats-on.html` — index of everything on, linking to the pages below
- `christmas.html` — the Christmas Feast: dates, prices per restaurant, menu links, email to book
- `brunch.html` — weekend brunch at Marylebone and EAST: times, dishes, booking
- `pour-and-plate.html` — the wine dinner series (next date still to be added)
- `restaurants.html` — the three restaurants
- `gift-cards.html` — Toast gift card links + cookbook
- `menus.html`, `menu-marylebone.html`, `menu-east.html`, `menu-townhouse.html` — full menus with prices
- `privacy.html` — stub; paste the current policy in

`css/style.css` and `js/main.js` are shared. `build.py` regenerates the pages from one template if you want to change the header/footer everywhere at once (`python3 build.py`) — otherwise just edit the HTML directly.

## Before launch
1. **Images and video** — `/images` are web-sized (2000px) versions of the shoot photos, plus a few shots from the old site (private rooms, venue interiors). `/video` holds the looping clips cut from the Instagram reels: `hero*.mp4` are the full-width page heroes (each has a `-mobile` vertical version for phones) and `reel-*.mp4` are the short vertical clips, which only load when scrolled into view.
2. **Forms** — the enquiry and brochure forms have a placeholder handler (`data-demo`). Point them at Formspree / a Google Sheets script / SevenRooms as preferred.
3. **Menus** — the menus are proper pages (`menu-marylebone.html`, `menu-east.html`, `menu-townhouse.html`, plus the `menus.html` hub), built from `data/menus.json`. That file holds every dish, price and wine taken from the restaurants' current menus. To change a menu, edit the JSON and run `python3 build.py`. The homepage Menus section has its own short selection of dishes in `build.py`.
4. **Pre-theatre / group menu prices** — marked "set price"; add the numbers.
5. **Privacy page** — copy from the old site.
6. **Logo** — `images/delamina-logo.svg` is traced from the logo on their menu PDFs (no vector file was available). Swap in the designer's original vector when you have it; it is inlined by `build.py`.

Fonts (Inconsolata, Open Sans) load from Google Fonts. Brand colours are in `:root` at the top of `style.css`.
