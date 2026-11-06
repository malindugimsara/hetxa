/**
 * ===================================================================
 * HETXA BOS - Business Benefits & Problems Solved Interactive JS
 * Created: 2026-11-06
 * Features:
 *  - Animated counter numbers for top ROI stat cards on scroll
 *  - Interactive 3D perspective tilt on transformation cards
 *  - Dynamic arrow flow highlight on stage hover
 * ===================================================================
 */

(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    // 1. Animated Numbers for ROI Stat Cards
    const statCards = document.querySelectorAll(".hetxa-roi-stat-card");
    if (statCards.length) {
      let statsAnimated = false;

      function animateStats() {
        const statValues = document.querySelectorAll(".hetxa-roi-stat-value");
        statValues.forEach((el) => {
          const originalText = el.innerText.trim();

          // Animate numeric values
          if (originalText.includes("%")) {
            const target = parseFloat(originalText);
            const isDecimal = originalText.includes(".");
            let current = 0;
            const step = target / 40;
            const timer = setInterval(() => {
              current += step;
              if (current >= target) {
                current = target;
                clearInterval(timer);
              }
              el.innerText = (isDecimal ? current.toFixed(1) : Math.round(current)) + "%";
            }, 30);
          } else if (originalText.includes("x")) {
            const target = parseFloat(originalText);
            let current = 0;
            const step = target / 35;
            const timer = setInterval(() => {
              current += step;
              if (current >= target) {
                current = target;
                clearInterval(timer);
              }
              el.innerText = current.toFixed(1) + "x";
            }, 35);
          }
        });
      }

      // Trigger animation using IntersectionObserver
      if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver(
          (entries, obs) => {
            entries.forEach((entry) => {
              if (entry.isIntersecting && !statsAnimated) {
                statsAnimated = true;
                animateStats();
                obs.disconnect();
              }
            });
          },
          { threshold: 0.3 }
        );

        const statsGrid = document.querySelector(".hetxa-roi-stats-grid");
        if (statsGrid) observer.observe(statsGrid);
      }
    }

    // 2. Interactive 3D Perspective Tilt on Transformation Cards (Desktop only)
    if (window.innerWidth >= 992) {
      const transformCards = document.querySelectorAll(".hetxa-transform-card");
      transformCards.forEach((card) => {
        let reqId = null;

        card.addEventListener("mousemove", function (e) {
          const rect = card.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          const centerX = rect.width / 2;
          const centerY = rect.height / 2;
          const deltaX = (x - centerX) / centerX;
          const deltaY = (y - centerY) / centerY;

          if (reqId) cancelAnimationFrame(reqId);
          reqId = requestAnimationFrame(() => {
            card.style.transform = `perspective(1200px) rotateY(${deltaX * 1.8}deg) rotateX(${-deltaY * 1.8}deg) translateY(-4px)`;
          });
        });

        card.addEventListener("mouseleave", function () {
          if (reqId) cancelAnimationFrame(reqId);
          card.style.transform = "";
        });
      });
    }

    // 3. Stage Hover Arrow Pulse Accent
    const stageBoxes = document.querySelectorAll(".hetxa-stage-box");
    stageBoxes.forEach((box) => {
      box.addEventListener("mouseenter", function () {
        const parentFlow = box.closest(".hetxa-transform-flow");
        if (parentFlow) {
          const arrows = parentFlow.querySelectorAll(".hetxa-flow-arrow");
          arrows.forEach((arr) => {
            arr.style.opacity = "1";
            arr.style.color = "#FF5E14";
            arr.style.transform = "scale(1.15)";
          });
        }
      });

      box.addEventListener("mouseleave", function () {
        const parentFlow = box.closest(".hetxa-transform-flow");
        if (parentFlow) {
          const arrows = parentFlow.querySelectorAll(".hetxa-flow-arrow");
          arrows.forEach((arr) => {
            arr.style.opacity = "";
            arr.style.color = "";
            arr.style.transform = "";
          });
        }
      });
    });
  });
})();
