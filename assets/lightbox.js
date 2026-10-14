(function () {
  "use strict";

  function init() {
    var triggers = document.querySelectorAll("a.zoomable");
    if (!triggers.length) return;

    var lastFocus = null;
    var inerted = [];
    var root = document.createElement("div");
    root.className = "lightbox";
    root.hidden = true;
    root.setAttribute("role", "dialog");
    root.setAttribute("aria-modal", "true");
    root.setAttribute("aria-label", "画像の拡大表示");
    root.innerHTML =
      '<button type="button" class="lightbox-close">閉じる</button>' +
      '<figure class="lightbox-figure">' +
        '<img class="lightbox-img" alt="" />' +
        '<figcaption id="lightbox-caption"></figcaption>' +
      "</figure>";
    document.body.appendChild(root);

    var closeBtn = root.querySelector(".lightbox-close");
    var img = root.querySelector(".lightbox-img");
    var caption = root.querySelector("#lightbox-caption");

    function open(trigger) {
      var source = trigger.querySelector("img");
      var figure = trigger.closest("figure");
      var cap = figure ? figure.querySelector("figcaption") : null;
      var alt = source && source.getAttribute("alt") ? source.getAttribute("alt") : "画像の拡大表示";
      img.src = trigger.getAttribute("href");
      img.alt = alt;
      caption.textContent = cap ? cap.textContent.replace(/\s+/g, " ").trim() : "";
      if (!caption.textContent) caption.hidden = true;
      else caption.hidden = false;
      root.setAttribute("aria-label", alt);
      lastFocus = trigger;
      Array.prototype.forEach.call(document.body.children, function (node) {
        if (node === root || node.hasAttribute("inert")) return;
        node.setAttribute("inert", "");
        inerted.push(node);
      });
      root.hidden = false;
      document.body.classList.add("lightbox-open");
      closeBtn.focus();
    }

    function close() {
      if (root.hidden) return;
      root.hidden = true;
      img.removeAttribute("src");
      img.alt = "";
      document.body.classList.remove("lightbox-open");
      inerted.forEach(function (node) { node.removeAttribute("inert"); });
      inerted = [];
      if (lastFocus && typeof lastFocus.focus === "function") lastFocus.focus();
      lastFocus = null;
    }

    Array.prototype.forEach.call(triggers, function (trigger) {
      trigger.setAttribute("aria-haspopup", "dialog");
      trigger.addEventListener("click", function (event) {
        if (event.defaultPrevented) return;
        if (event.button !== 0) return;
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        open(trigger);
      });
    });

    root.addEventListener("click", function (event) {
      if (event.target === closeBtn) return;
      close();
    });
    closeBtn.addEventListener("click", close);

    document.addEventListener("keydown", function (event) {
      if (root.hidden) return;
      if (event.key === "Escape") {
        event.preventDefault();
        close();
        return;
      }
      if (event.key !== "Tab") return;
      event.preventDefault();
      closeBtn.focus();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
