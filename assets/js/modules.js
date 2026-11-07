/**
 * ===================================================================
 * HETXA BOS - ERP Module Section JavaScript (Performance Optimized)
 * Rock-solid ScrollTrigger Synchronization & Layout Shift Protection
 * Prevents premature card freezing by ensuring ScrollTrigger positions
 * are accurately calculated after fonts, images and hero video initialize.
 *
 * NOTE: Never attach ResizeObserver with ScrollTrigger.refresh() on
 * smooth-content/body because ScrollTrigger unpins containers during
 * measurement, causing an infinite height-change loop with ScrollSmoother.
 * ===================================================================
 */

(function () {
  "use strict";

  let refreshTimer = null;
  function debouncedRefresh(delay) {
    if (typeof ScrollTrigger === "undefined") return;
    if (refreshTimer) clearTimeout(refreshTimer);
    refreshTimer = setTimeout(function () {
      try {
        ScrollTrigger.refresh();
      } catch (e) {
        // Silently handle if GSAP is unmounted
      }
    }, delay || 60);
  }

  // 1. Initial DOM Ready sync
  document.addEventListener("DOMContentLoaded", function () {
    debouncedRefresh(100);

    // Track web fonts ready (fires once)
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(function () {
        debouncedRefresh(50);
      });
    }

    // Attach one-time load listener to all images currently in DOM
    const imgs = document.querySelectorAll("img");
    imgs.forEach(function (img) {
      if (!img.complete) {
        img.addEventListener("load", function () {
          debouncedRefresh(60);
        }, { once: true });
        img.addEventListener("error", function () {
          debouncedRefresh(60);
        }, { once: true });
      }
    });

    // Attach ONE-TIME metadata listener to video elements (never listen to 'playing' or loops)
    const videos = document.querySelectorAll("video");
    videos.forEach(function (video) {
      if (video.readyState >= 1) {
        debouncedRefresh(50);
      } else {
        video.addEventListener("loadedmetadata", function () {
          debouncedRefresh(50);
        }, { once: true });
      }
    });
  });

  // 2. Track images loaded via imagesLoaded library if present (fires once)
  if (typeof imagesLoaded !== "undefined") {
    imagesLoaded(document.body, function () {
      debouncedRefresh(80);
    });
  }

  // 3. Window load event sync with safe one-off post-preloader sync
  window.addEventListener("load", function () {
    debouncedRefresh(50);
    setTimeout(function () {
      debouncedRefresh(100);
    }, 600);
  }, { once: true });

  // 4. Debounced window resize handler (handled natively by GSAP, but safe debounced backup)
  window.addEventListener("resize", function () {
    debouncedRefresh(150);
  }, { passive: true });

  window.addEventListener("orientationchange", function () {
    debouncedRefresh(200);
  }, { passive: true });
})();
