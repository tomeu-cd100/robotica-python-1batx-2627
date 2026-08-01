/* Robòtica · 1r Batx — interacció del web (sense dependències) */
(function () {
  "use strict";
  var doc = document.documentElement;

  /* ---------- Tema clar / fosc ---------- */
  var temaBtn = document.querySelector(".tema-btn");
  if (temaBtn) {
    temaBtn.addEventListener("click", function () {
      var fosc = doc.getAttribute("data-tema") === "fosc";
      if (fosc) { doc.removeAttribute("data-tema"); }
      else { doc.setAttribute("data-tema", "fosc"); }
      try { localStorage.setItem("tema", fosc ? "clar" : "fosc"); } catch (e) {}
    });
  }

  /* ---------- Menú lateral (mòbil) ---------- */
  var menuBtn = document.querySelector(".menu-btn");
  if (menuBtn) {
    menuBtn.addEventListener("click", function () {
      var obert = document.body.classList.toggle("menu-obert");
      menuBtn.setAttribute("aria-expanded", obert ? "true" : "false");
    });
  }

  /* ---------- Regió aria-live per als lectors de pantalla ----------
     Es crea en carregar (no sota demanda): els lectors només anuncien
     de forma fiable les regions que ja existien al DOM abans del canvi. */
  var avisA11y = document.createElement("div");
  avisA11y.id = "a11y-avis";
  avisA11y.className = "vo";
  avisA11y.setAttribute("aria-live", "polite");
  document.body.appendChild(avisA11y);
  function anuncia(msg) {
    avisA11y.textContent = "";
    setTimeout(function () { avisA11y.textContent = msg; }, 30);
  }

  /* ---------- Ajustos de lectura: mida de text i tipografia ---------- */
  var MIDES = [90, 100, 110, 120, 130];
  function midaActual() {
    var m = parseInt(localStorage.getItem("mida"), 10);
    return MIDES.indexOf(m) !== -1 ? m : 100;
  }
  function aplicaMida(m) {
    if (m === 100) { doc.removeAttribute("data-mida"); }
    else { doc.setAttribute("data-mida", String(m)); }
    try { localStorage.setItem("mida", String(m)); } catch (e) {}
    anuncia("Mida del text: " + m + " per cent.");
  }
  function canviaMida(pas) {
    var i = MIDES.indexOf(midaActual());
    var nou = MIDES[Math.min(MIDES.length - 1, Math.max(0, i + pas))];
    if (nou !== midaActual()) aplicaMida(nou);
  }
  var btnMenys = document.querySelector(".mida-menys");
  var btnMes = document.querySelector(".mida-mes");
  if (btnMenys) btnMenys.addEventListener("click", function () { canviaMida(-1); });
  if (btnMes) btnMes.addEventListener("click", function () { canviaMida(1); });

  var btnFont = document.querySelector(".font-toggle");
  if (btnFont) {
    var fontOn = doc.getAttribute("data-font") === "llegible";
    btnFont.setAttribute("aria-pressed", fontOn ? "true" : "false");
    btnFont.addEventListener("click", function () {
      fontOn = doc.getAttribute("data-font") === "llegible";
      if (fontOn) { doc.removeAttribute("data-font"); }
      else { doc.setAttribute("data-font", "llegible"); }
      try { localStorage.setItem("font", fontOn ? "estandard" : "llegible"); } catch (e) {}
      btnFont.setAttribute("aria-pressed", fontOn ? "false" : "true");
      anuncia(fontOn ? "Tipografia estàndard." : "Tipografia de lectura fàcil activada.");
    });
  }

  /* ---------- Vista docent / alumnat (amb porta de contrasenya) ---------- */
  /* FRICCIÓ, no seguretat: tot el material és públic al repositori (CC BY-SA).
     La porta només evita que l'alumnat entri a la vista docent per curiositat.
     Per canviar la contrasenya: py tools/canvia_contrasenya_docent.py */
  var DOCENT_HASH = "10d9c1b3";

  function clauDocent(text) {
    var h = 5381;
    for (var i = 0; i < text.length; i++) { h = ((h << 5) + h + text.charCodeAt(i)) >>> 0; }
    return h.toString(16);
  }
  function docentDesbloquejat() {
    try { return localStorage.getItem("docentClau") === DOCENT_HASH; } catch (e) { return false; }
  }
  function provaContrasenya(text) {
    if (text === null || clauDocent(text) !== DOCENT_HASH) return false;
    try { localStorage.setItem("docentClau", DOCENT_HASH); } catch (e) {}
    return true;
  }
  function posaVista(nova) {
    doc.setAttribute("data-vista", nova);
    try { localStorage.setItem("vista", nova); } catch (e) {}
  }

  /* Si la vista docent ve recordada d'abans però la clau no hi és (o ha
     canviat), torna a l'alumnat: la porta es passa un cop per navegador. */
  if (doc.getAttribute("data-vista") === "docent" && !docentDesbloquejat()) {
    posaVista("alumnat");
  }

  var vistaBtn = document.querySelector(".vista-btn");
  if (vistaBtn) {
    var vAra = doc.getAttribute("data-vista") || "alumnat";
    vistaBtn.setAttribute("aria-pressed", vAra === "docent" ? "true" : "false");
    vistaBtn.addEventListener("click", function () {
      var nova = doc.getAttribute("data-vista") === "docent" ? "alumnat" : "docent";
      if (nova === "docent" && !docentDesbloquejat()) {
        var t = window.prompt("Contrasenya de la vista docent:");
        if (!provaContrasenya(t)) {
          if (t !== null) { window.alert("Contrasenya incorrecta."); }
          anuncia("Contrasenya incorrecta.");
          return;
        }
      }
      posaVista(nova);
      vistaBtn.setAttribute("aria-pressed", nova === "docent" ? "true" : "false");
      anuncia(nova === "docent" ? "Vista docent activada." : "Vista alumnat activada.");
    });
  }

  /* Porta a les pàgines de material docent obertes per URL directa */
  if (document.body.getAttribute("data-public") === "docent" && !docentDesbloquejat()) {
    var contingut = document.getElementById("contingut") || document.querySelector("main");
    if (contingut) {
      contingut.setAttribute("data-ocult-docent", "");
      var porta = document.createElement("div");
      porta.className = "porta-docent";
      porta.innerHTML =
        '<div class="porta-docent-caixa" role="dialog" aria-labelledby="porta-docent-tit">' +
        '<p id="porta-docent-tit"><strong>🔒 Material del docent.</strong> Aquesta pàgina és per al professorat.</p>' +
        '<p class="porta-docent-nota">Ets alumne? Torna enrere: tot el que necessites és a la teva vista.</p>' +
        '<label>Contrasenya: <input type="password" class="porta-docent-input" autocomplete="off"></label>' +
        '<div class="porta-docent-botons">' +
        '<button type="button" class="porta-docent-entra">Entra</button>' +
        '<button type="button" class="porta-docent-enrere">← Enrere</button></div>' +
        '<p class="porta-docent-err" hidden>Contrasenya incorrecta.</p></div>';
      contingut.parentNode.insertBefore(porta, contingut);
      var input = porta.querySelector(".porta-docent-input");
      var err = porta.querySelector(".porta-docent-err");
      function entra() {
        if (provaContrasenya(input.value)) {
          porta.remove();
          contingut.removeAttribute("data-ocult-docent");
          anuncia("Vista docent desbloquejada.");
        } else {
          err.hidden = false;
          input.select();
        }
      }
      porta.querySelector(".porta-docent-entra").addEventListener("click", entra);
      input.addEventListener("keydown", function (e) { if (e.key === "Enter") entra(); });
      porta.querySelector(".porta-docent-enrere").addEventListener("click", function () {
        if (history.length > 1) { history.back(); } else { location.href = "./"; }
      });
      input.focus();
    }
  }

  /* ---------- Blocs de codi plegats: obre el bloc destí d'un enllaç #ancora ---------- */
  function obreBlocDesti() {
    var id = location.hash && decodeURIComponent(location.hash.slice(1));
    if (!id) return;
    var el = document.getElementById(id);
    if (el && el.tagName === "DETAILS" && !el.open) {
      el.open = true;
      el.scrollIntoView();
    }
  }
  obreBlocDesti();
  window.addEventListener("hashchange", obreBlocDesti);

  /* ---------- Botons de copiar codi ---------- */
  document.querySelectorAll(".copia-btn").forEach(function (btn) {
    btn.addEventListener("click", function (ev) {
      ev.preventDefault();
      ev.stopPropagation();
      var bloc = btn.closest(".codi-bloc");
      var pre = bloc ? bloc.querySelector("pre") : null;
      if (!pre) return;
      var text = pre.innerText;
      var ok = function () {
        var orig = btn.textContent;
        btn.textContent = "Copiat ✓";
        btn.classList.add("fet");
        anuncia("Codi copiat al porta-retalls.");
        setTimeout(function () { btn.textContent = orig; btn.classList.remove("fet"); }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(ok, fallback);
      } else { fallback(); }
      function fallback() {
        var ta = document.createElement("textarea");
        ta.value = text; document.body.appendChild(ta); ta.select();
        try { document.execCommand("copy"); ok(); } catch (e) {}
        document.body.removeChild(ta);
      }
    });
  });

  /* ---------- Cercador ---------- */
  var input = document.getElementById("cerca");
  var caixa = document.getElementById("cerca-resultats");
  var index = window.INDEX_CERCA || [];
  if (input && caixa) {
    var prefix = (function () {
      // calcula el prefix relatiu a l'arrel a partir de la URL de full.css
      var l = document.querySelector('link[href*="assets/css/estil.css"]');
      if (!l) return "";
      var h = l.getAttribute("href");
      return h.slice(0, h.indexOf("assets/css/estil.css"));
    })();

    function normalitza(s) {
      return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
    }

    var resultats = [], selIdx = -1;

    function cerca(q) {
      q = normalitza(q.trim());
      if (!q) { tanca(); return; }
      var vista = doc.getAttribute("data-vista") || "alumnat";
      var termes = q.split(/\s+/);
      // Dues passades: primer títol+secció (més rellevant), després el cos.
      var alTitol = [], alCos = [];
      index.forEach(function (it) {
        if (vista === "alumnat" && it.p === "docent") return;
        var heu = normalitza(it.t + " " + it.s);
        if (termes.every(function (t) { return heu.indexOf(t) !== -1; })) {
          alTitol.push(it);
          return;
        }
        if (!it.b) return;
        var tot = heu + " " + normalitza(it.b);
        if (termes.every(function (t) { return tot.indexOf(t) !== -1; })) {
          alCos.push(it);
        }
      });
      resultats = alTitol.concat(alCos).slice(0, 12);
      pinta();
    }

    function pinta() {
      selIdx = -1;
      if (!resultats.length) {
        caixa.innerHTML = '<div class="cerca-buit">Cap resultat.</div>';
        caixa.hidden = false; return;
      }
      caixa.innerHTML = resultats.map(function (it) {
        return '<a href="' + prefix + it.u + '"><strong>' +
          escapa(it.t) + '</strong><span class="r-sec">' + escapa(it.s) + '</span></a>';
      }).join("");
      caixa.hidden = false;
    }

    function tanca() { caixa.hidden = true; caixa.innerHTML = ""; resultats = []; selIdx = -1; }
    function escapa(s) { return s.replace(/[&<>]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]; }); }

    input.addEventListener("input", function () { cerca(input.value); });
    input.addEventListener("focus", function () { if (input.value) cerca(input.value); });
    input.addEventListener("keydown", function (e) {
      var enllacos = caixa.querySelectorAll("a");
      if (e.key === "ArrowDown") { e.preventDefault(); selIdx = Math.min(selIdx + 1, enllacos.length - 1); marca(enllacos); }
      else if (e.key === "ArrowUp") { e.preventDefault(); selIdx = Math.max(selIdx - 1, 0); marca(enllacos); }
      else if (e.key === "Enter") { if (enllacos[selIdx]) { e.preventDefault(); window.location.href = enllacos[selIdx].href; } }
      else if (e.key === "Escape") { tanca(); input.blur(); }
    });
    function marca(enllacos) {
      enllacos.forEach(function (a, i) { a.classList.toggle("sel", i === selIdx); });
      if (enllacos[selIdx]) enllacos[selIdx].scrollIntoView({ block: "nearest" });
    }
    document.addEventListener("click", function (e) {
      if (!input.contains(e.target) && !caixa.contains(e.target)) tanca();
    });
  }
})();
