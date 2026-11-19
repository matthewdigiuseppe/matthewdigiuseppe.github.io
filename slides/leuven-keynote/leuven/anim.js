/* Shared stage controller for the animated slides in the Leuven deck.
   Each animation page has a few stages. The clicker (or the arrow keys)
   moves through the stages first, and only then on to the next slide.

   It works by listening to the deck's own key presses while this page is
   the slide on screen, so nothing has to be clicked first. */
(function () {
  const NEXT = new Set(['ArrowRight', 'PageDown', ' ', 'Spacebar', 'Enter']);
  const PREV = new Set(['ArrowLeft', 'PageUp']);

  window.Stages = {
    init(count, onChange) {
      let stage = 0;
      let stageStart = performance.now();

      const dots = document.createElement('div');
      dots.className = 'stage-dots';
      for (let i = 0; i < count; i++) dots.appendChild(document.createElement('i'));
      document.body.appendChild(dots);

      const paint = (previous) => {
        [...dots.children].forEach((d, i) => d.classList.toggle('on', i <= stage));
        document.body.dataset.stage = String(stage);
        onChange(stage, previous);
      };
      const go = (delta) => {
        const next = stage + delta;
        if (next < 0 || next >= count) return false;
        const previous = stage;
        stage = next;
        stageStart = performance.now();
        paint(previous);
        return true;
      };
      const handle = (e) => {
        if (e.ctrlKey || e.metaKey || e.altKey) return false;
        if (NEXT.has(e.key)) return go(1);
        if (PREV.has(e.key)) return go(-1);
        return false;
      };

      // The deck page, when this file is shown inside a slide.
      let deck = null;
      try { if (window.parent !== window && window.parent.document) deck = window.parent; } catch (err) { deck = null; }

      if (deck) {
        const onDeckKey = (e) => {
          // This page has left the screen: stop listening.
          if (!window.frameElement || !window.frameElement.isConnected) {
            deck.removeEventListener('keydown', onDeckKey, true);
            return;
          }
          const body = deck.document.body;
          if (body.classList.contains('edit-mode')) return;
          if (deck.document.querySelector('.modal.open')) return;
          const t = e.target;
          if (t && t.closest && t.closest('textarea,input,select')) return;
          if (handle(e)) { e.preventDefault(); e.stopImmediatePropagation(); }
        };
        deck.addEventListener('keydown', onDeckKey, true);
        window.addEventListener('pagehide', () => deck.removeEventListener('keydown', onDeckKey, true));
      }

      // Keys pressed while this page itself has focus (after a click on it).
      window.addEventListener('keydown', (e) => {
        if (handle(e)) { e.preventDefault(); return; }
        if (deck && (NEXT.has(e.key) || PREV.has(e.key))) {
          // First or last stage: hand the key back to the deck.
          deck.document.dispatchEvent(new KeyboardEvent('keydown', { key: e.key, bubbles: true }));
          try { deck.focus(); } catch (err) { /* ignore */ }
          e.preventDefault();
        }
      });

      // A click or tap also moves one stage on.
      window.addEventListener('click', () => { go(1); });

      paint(-1);
      return {
        get stage() { return stage; },
        get elapsed() { return (performance.now() - stageStart) / 1000; },
        go
      };
    }
  };

  /* Small helpers shared by the canvas pages. */
  window.Anim = {
    // Repeatable random numbers, so the picture is the same every time.
    rng(seed) {
      let a = seed >>> 0;
      return function () {
        a |= 0; a = (a + 0x6D2B79F5) | 0;
        let t = Math.imul(a ^ (a >>> 15), 1 | a);
        t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
        return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
      };
    },
    ease(x) { x = Math.max(0, Math.min(1, x)); return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; },
    clamp(x, lo, hi) { return Math.max(lo, Math.min(hi, x)); },
    lerp(a, b, t) { return a + (b - a) * t; },
    comma(n) { return Math.round(n).toLocaleString('en-GB'); },
    // A 1600 x 900 drawing surface that stays sharp on a projector.
    canvas(id) {
      const cv = document.getElementById(id);
      const scale = 2;
      cv.width = 1600 * scale; cv.height = 900 * scale;
      const ctx = cv.getContext('2d');
      ctx.scale(scale, scale);
      return ctx;
    }
  };
})();
