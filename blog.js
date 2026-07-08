(function () {

  /* ── THEME TOGGLE (shared) ── */
  const themeRoot   = document.documentElement;
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    const stored       = localStorage.getItem('si-theme');
    const prefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
    const initial      = stored || (prefersLight ? 'light' : 'dark');
    themeRoot.setAttribute('data-theme', initial);
    themeToggle.textContent = initial === 'light' ? '☀' : '☾';
    themeToggle.addEventListener('click', () => {
      const next = themeRoot.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      themeRoot.setAttribute('data-theme', next);
      localStorage.setItem('si-theme', next);
      themeToggle.textContent = next === 'light' ? '☀' : '☾';
    });
  }

  /* ── CURSOR ── */
  const cursor = document.getElementById('cursor');
  const ring   = document.getElementById('cursor-ring');
  let mx = -100, my = -100, rx = -100, ry = -100;
  if (cursor) cursor.style.opacity = '0';
  if (ring)   ring.style.opacity   = '0';

  document.addEventListener('mousemove', e => {
    mx = e.clientX; my = e.clientY;
    if (cursor) {
      cursor.style.opacity = '1';
      cursor.style.transform = `translate(${mx - 2}px, ${my - 2}px)`;
    }
    if (ring) ring.style.opacity = '1';
  });

  function animateRing() {
    rx += (mx - rx) * 0.12;
    ry += (my - ry) * 0.12;
    if (ring) ring.style.transform = `translate(${rx - 12}px, ${ry - 12}px)`;
    requestAnimationFrame(animateRing);
  }
  animateRing();

  /* ── TOC ACTIVE STATE ── */
  const sections = document.querySelectorAll('.content-section[id]');
  const tocItems = document.querySelectorAll('.toc-item[href]');

  if (sections.length && tocItems.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          tocItems.forEach(item => {
            item.classList.toggle('active', item.getAttribute('href') === '#' + id);
          });
        }
      });
    }, { rootMargin: '-20% 0px -60% 0px', threshold: 0 });

    sections.forEach(s => io.observe(s));
  }

})();
