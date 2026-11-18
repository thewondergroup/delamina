# Delamina — website

Static site, no build step needed to deploy. Upload the folder to a GitHub repo and turn on GitHub Pages.

## Pages
- `index.html` — homepage
- `marylebone.html`, `east.html`, `townhouse.html` — one per restaurant (menus, hours, private rooms, map)
- `private-dining.html` — all nine rooms, enquiry form, brochure request
- `our-story.html` — Limor & Amir, the cookbook, Join us
- `whats-on.html` — Christmas 2026, Pour & Plate, Founders' Dinners, brunch
- `gift-cards.html` — Toast gift card links + cookbook
- `privacy.html` — stub; paste the current policy in

`css/style.css` and `js/main.js` are shared. `build.py` regenerates the pages from one template if you want to change the header/footer everywhere at once (`python3 build.py`) — otherwise just edit the HTML directly.

## Before launch
1. **Images** — `/images` are web-sized (2000px) versions of the shoot photos, plus a few earlier shots from the current site (venue heroes, private rooms). `/video/hero.mp4` (desktop, 1280×720) and `hero-mobile.mp4` (phone, vertical) are the 20s homepage loop cut from the Instagram reels.
2. **Forms** — the enquiry and brochure forms have a placeholder handler (`data-demo`). Point them at Formspree / a Google Sheets script / SevenRooms as preferred.
3. **Menus** — `/menus` holds the 15 current menu PDFs from the live site (à la carte, brunch, wine, sharing and Christmas for each restaurant). The homepage shows real dishes and prices taken from them. When a menu changes, replace the PDF with the same filename and update the dish lines in the homepage Menus section. The dish lists on the three restaurant pages are still samples.
4. **Pre-theatre / group menu prices** — marked "set price"; add the numbers.
5. **Privacy page** — copy from the old site.
6. **Logo** — `images/delamina-logo.svg` is traced from the logo on their menu PDFs (no vector file was available). Swap in the designer's original vector when you have it; it is inlined by `build.py`.

Fonts (Inconsolata, Open Sans) load from Google Fonts. Brand colours are in `:root` at the top of `style.css`.
