/**
 * ===================================================================
 * HETXA BOS - ERP Module Section JavaScript (Performance Optimized)
 * Handles smooth debounced ScrollTrigger synchronization without
 * freezing or locking the main browser thread on refresh.
 * ===================================================================
 */

(function () {
  "use strict";

  let refreshTimer = null;
  function debouncedRefresh(delay) {
    if (typeof ScrollTrigger === "undefined") return;
    if (refreshTimer) clearTimeout(refreshTimer);
    refreshTimer = setTimeout(function () {
      ScrollTrigger.refresh();
    }, delay || 100);
  }

  // 1. Initial DOM Ready sync
  document.addEventListener("DOMContentLoaded", function () {
    debouncedRefresh(150);

    // 2. Track images loading via imagesLoaded plugin
    if (typeof imagesLoaded !== "undefined") {
      imagesLoaded(document.body, function () {
        debouncedRefresh(100);
      });
    }

    // 3. Track web fonts ready
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(function () {
        debouncedRefresh(80);
      });
    }
  });

  // 4. Window load event sync
  window.addEventListener("load", function () {
    debouncedRefresh(100);
  });

  // 5. Debounced window resize handler
  window.addEventListener("resize", function () {
    debouncedRefresh(150);
  }, { passive: true });
})();
