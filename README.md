# Delamina — website

Static site, no build step needed to deploy. Upload the folder to a GitHub repo and turn on GitHub Pages.

## Pages
- `index.html` — homepage
- `marylebone.html`, `east.html`, `townhouse.html` — one per restaurant (menus, hours, private rooms, map)
- `private-dining.html` — all nine rooms, enquiry form, brochure request
- `our-story.html` — Limor & Amir, the cookbook, Join us
- `whats-on.html` — Christmas 2026, Pour & Plate, Founders' Dinners, brunch
- `gift-cards.html` — Toast gift card links + cookbook
- `menus.html`, `menu-marylebone.html`, `menu-east.html`, `menu-townhouse.html` — full menus with prices
- `privacy.html` — stub; paste the current policy in

`css/style.css` and `js/main.js` are shared. `build.py` regenerates the pages from one template if you want to change the header/footer everywhere at once (`python3 build.py`) — otherwise just edit the HTML directly.

## Before launch
1. **Images** — `/images` are web-sized (2000px) versions of the shoot photos, plus a few earlier shots from the current site (venue heroes, private rooms). `/video/hero.mp4` (desktop, 1280×720) and `hero-mobile.mp4` (phone, vertical) are the 20s homepage loop cut from the Instagram reels.
2. **Forms** — the enquiry and brochure forms have a placeholder handler (`data-demo`). Point them at Formspree / a Google Sheets script / SevenRooms as preferred.
3. **Menus** — the menus are proper pages (`menu-marylebone.html`, `menu-east.html`, `menu-townhouse.html`, plus the `menus.html` hub), built from `data/menus.json`. That file holds every dish, price and wine taken from the restaurants' current menus. To change a menu, edit the JSON and run `python3 build.py`. The homepage Menus section has its own short selection of dishes in `build.py`.
4. **Pre-theatre / group menu prices** — marked "set price"; add the numbers.
5. **Privacy page** — copy from the old site.
6. **Logo** — `images/delamina-logo.svg` is traced from the logo on their menu PDFs (no vector file was available). Swap in the designer's original vector when you have it; it is inlined by `build.py`.

Fonts (Inconsolata, Open Sans) load from Google Fonts. Brand colours are in `:root` at the top of `style.css`.
