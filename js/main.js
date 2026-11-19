// Delamina — site JS (no dependencies)
(function () {
  // Mobile nav: animated full-screen panel
  var toggle = document.querySelector('.nav-toggle');
  var mobile = document.querySelector('.mobile-nav');
  var siteHeader = document.querySelector('.site-header');
  if (toggle && mobile && siteHeader) {
    var setMenu = function (open) {
      if (open) mobile.style.height = Math.max(0, window.innerHeight - siteHeader.getBoundingClientRect().bottom) + 'px';
      mobile.classList.toggle('open', open);
      siteHeader.classList.toggle('menu-open', open);
      document.body.classList.toggle('menu-lock', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Menu');
    };
    toggle.addEventListener('click', function () { setMenu(!mobile.classList.contains('open')); });
    mobile.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
    window.addEventListener('resize', function () { if (window.innerWidth > 960) setMenu(false); });
  }

  // Scroll reveal
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }
  // Safety net: never leave content hidden
  setTimeout(function () { els.forEach(function (el) { el.classList.add('in'); }); }, 1500);

  // Background videos: phones get the vertical cut; reduced motion shows the still
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var mqv = window.matchMedia('(max-width: 760px)');
  document.querySelectorAll('video[data-desktop]').forEach(function (v) {
    var pick = function () {
      var want = mqv.matches ? v.dataset.mobile : v.dataset.desktop;
      if (mqv.matches && v.dataset.posterMobile) v.poster = v.dataset.posterMobile;
      if (v.getAttribute('data-current') !== want) {
        v.setAttribute('data-current', want);
        v.src = want;
        if (!reduce) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
      }
    };
    pick();
    if (mqv.addEventListener) mqv.addEventListener('change', pick);
    if (reduce) { v.removeAttribute('autoplay'); v.pause(); }
  });
  if (reduce) document.querySelectorAll('video[autoplay]').forEach(function (v) { v.removeAttribute('autoplay'); v.pause(); });

  // Reels: load and play only while on screen
  var lazyVids = document.querySelectorAll('video[data-lazy]');
  if (lazyVids.length && 'IntersectionObserver' in window && !reduce) {
    var vio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting) {
          if (!v.src) v.src = v.dataset.lazy;
          var p = v.play(); if (p && p.catch) p.catch(function () {});
        } else if (v.src) { v.pause(); }
      });
    }, { rootMargin: '150px 0px', threshold: 0.15 });
    lazyVids.forEach(function (v) { vio.observe(v); });
  }

  // Restaurants page: play that restaurant's video while its panel is hovered
  if (!reduce && window.matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('.rpanel').forEach(function (p) {
      var pv = p.querySelector('video[data-hover]');
      if (!pv) return;
      p.addEventListener('mouseenter', function () {
        if (!pv.src) pv.src = pv.dataset.hover;
        var pr = pv.play(); if (pr && pr.catch) pr.catch(function () {});
        p.classList.add('playing');
      });
      p.addEventListener('mouseleave', function () { p.classList.remove('playing'); pv.pause(); });
    });
  }

  // Restaurant pages: show today's booking times (London time)
  document.querySelectorAll('[data-today]').forEach(function (el) {
    try {
      var hrs = JSON.parse(el.getAttribute('data-today'));
      var day = new Date().toLocaleDateString('en-GB', { weekday: 'short', timeZone: 'Europe/London' });
      var i = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(day);
      if (i > -1 && hrs[i]) el.textContent = hrs[i];
    } catch (err) {}
  });

  // Homepage: header turns olive after the hero
  if (document.body.classList.contains('home')) {
    var hdr = document.querySelector('.site-header');
    var onScroll = function () { hdr.classList.toggle('scrolled', window.scrollY > window.innerHeight * 0.75); };
    window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  }

  // Drag to scroll the rooms rail
  var rail = document.querySelector('.rooms-rail');
  if (rail) {
    var down = false, sx = 0, sl = 0;
    rail.addEventListener('mousedown', function (e) { down = true; sx = e.pageX; sl = rail.scrollLeft; rail.style.scrollSnapType = 'none'; });
    window.addEventListener('mouseup', function () { if (down) { down = false; rail.style.scrollSnapType = ''; } });
    rail.addEventListener('mousemove', function (e) { if (!down) return; e.preventDefault(); rail.scrollLeft = sl - (e.pageX - sx); });
  }

  // Menu tabs (venue pages)
  var tabs = document.querySelectorAll('[data-menu-tab]');
  var panes = document.querySelectorAll('[data-menu-pane]');
  var activate = function (t, fromClick) {
      var id = t.getAttribute('data-menu-tab');
      if (t.hasAttribute('data-hash') && fromClick && history.replaceState) history.replaceState(null, '', '#' + id);
      tabs.forEach(function (x) { x.removeAttribute('aria-current'); });
      t.setAttribute('aria-current', 'true');
      panes.forEach(function (p) { p.hidden = p.getAttribute('data-menu-pane') !== id; });
      var photo = document.getElementById('menu-photo'), src = t.getAttribute('data-img');
      if (photo && src && photo.getAttribute('src') !== src) {
        photo.classList.add('swap');
        setTimeout(function () { photo.src = src; photo.onload = function () { photo.classList.remove('swap'); }; }, 200);
      }
    };
  tabs.forEach(function (t) {
    t.addEventListener('click', function (ev) { ev.preventDefault(); activate(t, true); });
  });
  // Open the menu named in the address (menu-marylebone.html#brunch)
  var openFromHash = function () {
    var h = location.hash.slice(1);
    if (!h) return;
    tabs.forEach(function (t) {
      if (t.hasAttribute('data-hash') && t.getAttribute('data-menu-tab') === h) {
        activate(t, false);
        var bar = document.querySelector('.mp-head');
        if (bar) window.scrollTo(0, bar.offsetTop + bar.offsetHeight - 80);
      }
    });
  };
  openFromHash();
  window.addEventListener('hashchange', openFromHash);

  // Forms: placeholder handler until a form endpoint is wired up
  document.querySelectorAll('form[data-demo]').forEach(function (f) {
    f.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var msg = f.querySelector('.form-msg');
      if (msg) { msg.textContent = 'Thank you — we’ll be in touch shortly.'; }
      f.reset();
    });
  });
})();
