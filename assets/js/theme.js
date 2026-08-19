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

  function mount() {
    if (document.querySelector(".theme-toggle")) {
      apply(current());
      return;
    }
    var toggle = document.createElement("div");
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
    var lang = document.querySelector(".lang-toggle");
    if (lang) {
      lang.classList.add("site-controls");
      lang.appendChild(toggle);
    } else {
      document.body.insertBefore(toggle, document.body.firstChild);
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
})();
