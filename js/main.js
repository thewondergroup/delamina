// Delamina — site JS (no dependencies)
(function () {
  // Mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var mobile = document.querySelector('.mobile-nav');
  if (toggle && mobile) {
    toggle.addEventListener('click', function () {
      var open = mobile.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
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

  // Hero video: phone gets the vertical cut; respect reduced motion; pause control
  var v = document.querySelector('.hero-video');
  if (v) {
    var mq = window.matchMedia('(max-width: 760px)');
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var pick = function () {
      var want = mq.matches ? v.dataset.mobile : v.dataset.desktop;
      if (mq.matches && v.dataset.posterMobile) v.poster = v.dataset.posterMobile;
      if (v.getAttribute('data-current') !== want) {
        v.setAttribute('data-current', want);
        v.src = want;
        if (!reduce) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
      }
    };
    pick();
    if (mq.addEventListener) mq.addEventListener('change', pick);
    var btn = document.querySelector('.hero-pause');
    var setBtn = function () {
      if (!btn) return;
      btn.classList.toggle('paused', v.paused);
      btn.setAttribute('aria-label', v.paused ? 'Play background video' : 'Pause background video');
    };
    if (reduce) { v.removeAttribute('autoplay'); v.pause(); }
    if (btn) btn.addEventListener('click', function () { if (v.paused) { v.play(); } else { v.pause(); } });
    v.addEventListener('play', setBtn); v.addEventListener('pause', setBtn); setBtn();
  }

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
  tabs.forEach(function (t) {
    t.addEventListener('click', function (ev) {
      ev.preventDefault();
      var id = t.getAttribute('data-menu-tab');
      tabs.forEach(function (x) { x.removeAttribute('aria-current'); });
      t.setAttribute('aria-current', 'true');
      panes.forEach(function (p) { p.hidden = p.getAttribute('data-menu-pane') !== id; });
      var photo = document.getElementById('menu-photo'), src = t.getAttribute('data-img');
      if (photo && src && photo.getAttribute('src') !== src) {
        photo.classList.add('swap');
        setTimeout(function () { photo.src = src; photo.onload = function () { photo.classList.remove('swap'); }; }, 200);
      }
    });
  });

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
