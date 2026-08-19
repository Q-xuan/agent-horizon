(function () {
  var KEY = "ah-theme";

  function current() {
    return document.documentElement.getAttribute("data-theme") || "light";
  }

  function apply(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    try {
      localStorage.setItem(KEY, theme);
    } catch (e) {}
    document.querySelectorAll(".theme-toggle button").forEach(function (btn) {
      btn.classList.toggle("active", btn.getAttribute("data-theme") === theme);
    });
  }

  function ensureToggle() {
    var toggle = document.querySelector(".theme-toggle");
    if (toggle) return toggle;
    toggle = document.createElement("div");
    toggle.className = "theme-toggle";
    [
      ["light", "白"],
      ["dark", "黑"],
    ].forEach(function (pair) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.setAttribute("data-theme", pair[0]);
      btn.textContent = pair[1];
      btn.addEventListener("click", function () {
        apply(pair[0]);
      });
      toggle.appendChild(btn);
    });
    document.body.appendChild(toggle);
    return toggle;
  }


  function homeUrl() {
    var css = document.querySelector('link[href*="assets/css/horizon.css"]');
    if (css && css.href) {
      return css.href.replace(/assets\/css\/horizon\.css.*$/, "");
    }
    var parts = location.pathname.split("/").filter(Boolean);
    if (parts.length && parts[0] !== "2026" && parts[0] !== "2025") {
      return "/" + parts[0] + "/";
    }
    return "/";
  }

  function ensureHome() {
    if (document.querySelector(".site-home")) return;
    var header = document.querySelector(".page-header");
    if (!header) return;
    var a = document.createElement("a");
    a.className = "site-home";
    a.href = homeUrl();
    a.textContent = "Agent Horizon";
    header.insertBefore(a, header.firstChild);
    var title = header.querySelector(".project-name");
    if (title && /^Home$/i.test(title.textContent.trim())) {
      title.style.display = "none";
    }
  }
  function mount() {
    ensureHome();
    var toggle = ensureToggle();
    var lang = document.querySelector(".lang-toggle");
    if (lang && toggle.parentNode !== lang) {
      lang.classList.add("site-controls");
      lang.appendChild(toggle);
    }
    apply(current());
  }

  var fromQuery = null;
  try {
    fromQuery = new URLSearchParams(window.location.search).get("theme");
  } catch (e) {}
  apply(
    (fromQuery === "dark" || fromQuery === "light" ? fromQuery : null) ||
      (function () {
        try {
          return localStorage.getItem(KEY);
        } catch (e) {
          return null;
        }
      })() ||
      (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light")
  );

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
  window.addEventListener("load", mount);
  setTimeout(mount, 50);
  setTimeout(mount, 300);
})();
