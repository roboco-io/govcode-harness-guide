// Apply before the stylesheet loads to avoid flashing the wrong theme.
(() => {
  const key = 'govcode-guide-theme';
  const media = window.matchMedia('(prefers-color-scheme: dark)');
  let preference = null;
  try {
    const saved = localStorage.getItem(key);
    if (saved === 'light' || saved === 'dark') preference = saved;
  } catch { /* Private browsing or storage restrictions: use this visit only. */ }
  function apply() {
    const theme = preference || (media.matches ? 'dark' : 'light');
    document.documentElement.dataset.theme = theme;
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', theme === 'dark' ? '#101923' : '#142943');
    const toggle = document.querySelector('[data-theme-toggle]');
    if (toggle) {
      const label = theme === 'dark' ? '라이트 모드로 전환' : '다크 모드로 전환';
      toggle.setAttribute('aria-label', label);
      toggle.setAttribute('title', label);
      toggle.querySelector('[data-theme-label]').textContent = theme === 'dark' ? '라이트' : '다크';
    }
    const reset = document.querySelector('[data-theme-system]');
    if (reset) reset.hidden = !preference;
  }
  function save(value) {
    preference = value;
    try { if (value) localStorage.setItem(key, value); else localStorage.removeItem(key); } catch { /* Keep the in-memory choice. */ }
    apply();
  }
  apply();
  media.addEventListener('change', () => { if (!preference) apply(); });
  window.addEventListener('storage', event => {
    if (event.key !== key && event.key !== null) return;
    preference = event.newValue === 'dark' || event.newValue === 'light' ? event.newValue : null;
    apply();
  });
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('[data-theme-toggle]')?.addEventListener('click', () => save(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'));
    document.querySelector('[data-theme-system]')?.addEventListener('click', () => save(null));
    apply();
  });
})();
