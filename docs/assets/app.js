// Menu em telas estreitas: o botão só aparece com JS; sem JS a lista de links fica visível.
(function () {
  const btn = document.getElementById('nav-toggle'), nav = document.getElementById('menu');
  if (!btn || !nav) return;
  btn.hidden = false; nav.classList.add('closed');
  const set = open => { nav.classList.toggle('closed', !open); btn.setAttribute('aria-expanded', String(open)); };
  btn.addEventListener('click', () => set(nav.classList.contains('closed')));
  document.addEventListener('keydown', ev => { if (ev.key === 'Escape' && !nav.classList.contains('closed')) { set(false); btn.focus(); } });
})();

// A linha do portal (.eco) rola com a página; só a faixa da marca e do menu fica presa no topo.
(function () {
  const eco = document.querySelector('.site-header .eco');
  if (!eco) return;
  const set = () => document.documentElement.style.setProperty('--eco', eco.offsetHeight + 'px');
  set(); window.addEventListener('resize', set);
})();

// Bibliotheca Latina — filtros do catálogo e progresso de leitura (salvo só no navegador do leitor).
(function () {
  const KEY = 'bibliotheca-latina:v1';
  const STATES = ['quero', 'lendo', 'lido'];
  let store = { quero: {}, lendo: {}, lido: {} };
  try { const s = JSON.parse(localStorage.getItem(KEY)); if (s) STATES.forEach(k => { if (s[k]) store[k] = s[k]; }); } catch (e) {}
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(store)); } catch (e) {} };
  const stateOf = id => STATES.find(k => store[k][id]) || '';

  // marcações: um estado por obra (quero ler → lendo → lido), em qualquer página com cards
  document.querySelectorAll('.obra').forEach(card => {
    const id = card.id;
    const refresh = () => card.querySelectorAll('.mark').forEach(b => b.setAttribute('aria-pressed', store[b.dataset.kind][id] ? 'true' : 'false'));
    refresh();
    card.querySelectorAll('.mark').forEach(b => b.addEventListener('click', () => {
      const k = b.dataset.kind, on = !!store[k][id];
      STATES.forEach(s => delete store[s][id]);
      if (!on) store[k][id] = Date.now();
      refresh(); save(); if (window.applyFilters) window.applyFilters(false);
    }));
  });

  const grid = document.getElementById('grid');
  if (!grid) return;
  const cards = Array.from(grid.querySelectorAll('.obra'));
  const $ = id => document.getElementById(id);
  const q = $('q'), periodo = $('periodo'), genero = $('genero'), dificuldade = $('dificuldade'), formato = $('formato'),
        fonte = $('fonte'), lista = $('lista'), ordem = $('ordem'), audio = $('f-audio'), gratis = $('f-gratis'),
        count = $('count'), empty = $('empty'), interno = $('f-interno');
  const chipGroups = { etapa: new Set(), categoria: new Set(), tipo: new Set() };
  const norm = s => (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');

  document.querySelectorAll('.chip-btn').forEach(b => b.addEventListener('click', () => {
    const g = chipGroups[b.dataset.group], v = b.dataset.value;
    if (g.has(v)) g.delete(v); else g.add(v);
    b.setAttribute('aria-pressed', g.has(v) ? 'true' : 'false');
    apply(true);
  }));
  [q, periodo, genero, dificuldade, formato, fonte, lista, ordem, audio, gratis, interno].forEach(el => el && el.addEventListener(el === q ? 'input' : 'change', () => apply(true)));

  function visible(c) {
    const d = c.dataset;
    if (chipGroups.etapa.size && !chipGroups.etapa.has(d.etapa)) return false;
    if (chipGroups.categoria.size && !chipGroups.categoria.has(d.categoria)) return false;
    if (chipGroups.tipo.size && !chipGroups.tipo.has(d.tipo)) return false;
    if (periodo.value && d.periodo !== periodo.value) return false;
    if (genero.value && d.genero !== genero.value) return false;
    if (dificuldade.value && d.dif !== dificuldade.value) return false;
    if (formato.value && !(' ' + d.formatos + ' ').includes(' ' + formato.value + ' ')) return false;
    if (fonte.value && d.fonte !== fonte.value) return false;
    if (audio.checked && d.audio !== '1') return false;
    if (gratis.checked && d.gratis !== '1') return false;
    if (interno && interno.checked && d.interno !== '1') return false;
    const st = stateOf(c.id);
    if (lista.value === 'nao-lido' ? st === 'lido' : (lista.value && st !== lista.value)) return false;
    const t = norm(q.value.trim());
    return !t || t.split(/\s+/).every(w => d.q.includes(w));
  }
  const sorters = {
    sugerida: (a, b) => a.dataset.i - b.dataset.i,
    facil: (a, b) => (a.dataset.dif || 9) - (b.dataset.dif || 9) || a.dataset.i - b.dataset.i,
    dificil: (a, b) => (b.dataset.dif || 0) - (a.dataset.dif || 0) || a.dataset.i - b.dataset.i,
    titulo: (a, b) => a.dataset.t.localeCompare(b.dataset.t, 'la'),
    autor: (a, b) => a.dataset.a.localeCompare(b.dataset.a, 'la') || a.dataset.i - b.dataset.i,
  };
  function apply(push) {
    const shown = cards.filter(visible).sort(sorters[ordem.value] || sorters.sugerida);
    // Só mexe no que mudou. Esconder todos os cards e reinseri-los encolhia a página por um instante, e o
    // navegador levava a rolagem para o topo (ex.: ao marcar "Lido" no fim do catálogo).
    const on = new Set(shown);
    cards.forEach(c => { const h = !on.has(c); if (c.hidden !== h) c.hidden = h; });
    const atual = Array.from(grid.children).filter(c => !c.hidden);
    if (atual.some((c, i) => c !== shown[i])) {
      const y = window.scrollY, frag = document.createDocumentFragment();
      shown.forEach(c => frag.appendChild(c)); grid.appendChild(frag);
      if (!push) window.scrollTo({ top: y, behavior: 'instant' });
    }
    count.textContent = shown.length === 1 ? '1 recurso' : shown.length + ' recursos';
    empty.hidden = shown.length > 0;
    if (push) {
      const p = new URLSearchParams();
      Object.entries(chipGroups).forEach(([g, s]) => { if (s.size) p.set(g, [...s].join(',')); });
      [['periodo', periodo], ['genero', genero], ['dificuldade', dificuldade], ['formato', formato], ['fonte', fonte], ['lista', lista]].forEach(([k, el]) => { if (el.value) p.set(k, el.value); });
      if (audio.checked) p.set('audio', '1');
      if (gratis.checked) p.set('gratis', '1');
      if (interno && interno.checked) p.set('aqui', '1');
      if (ordem.value !== 'sugerida') p.set('ordem', ordem.value);
      if (q.value.trim()) p.set('q', q.value.trim());
      history.replaceState(null, '', (p.toString() ? '?' + p : location.pathname));
    }
    setMore(!more.classList.contains('closed'));
    return shown;
  }
  window.applyFilters = apply;

  // "Filtros": a busca fica sempre visível; etapas, tipos e menus podem ser recolhidos (recolhidos de início em telas estreitas)
  const fBtn = $('filtros-botao'), more = $('filtros-mais');
  const extras = () => Object.values(chipGroups).reduce((n, s) => n + s.size, 0) + [periodo, genero, dificuldade, formato, fonte, lista].filter(el => el.value).length + (audio.checked ? 1 : 0) + (gratis.checked ? 1 : 0) + (interno && interno.checked ? 1 : 0);
  function setMore(open) {
    more.classList.toggle('closed', !open); fBtn.setAttribute('aria-expanded', String(open));
    const n = extras(); fBtn.textContent = (open ? 'Ocultar filtros' : 'Filtros') + (n ? ' (' + n + ')' : '');
  }
  fBtn.hidden = false;
  fBtn.addEventListener('click', () => setMore(more.classList.contains('closed')));

  // atalho discreto de volta à busca, só depois que o painel de filtros saiu da tela
  const back = document.querySelector('.voltar-busca'), panel = $('filtros');
  if (back && 'IntersectionObserver' in window) {
    new IntersectionObserver(([en]) => { back.hidden = en.isIntersecting || en.boundingClientRect.top > 0; }).observe(panel);
    back.addEventListener('click', ev => { ev.preventDefault(); panel.scrollIntoView({ block: 'start', behavior: 'instant' }); q.focus({ preventScroll: true }); });
  }

  // estado inicial a partir da URL (links compartilháveis, ex.: catalogo.html?etapa=1&audio=1)
  const p = new URLSearchParams(location.search);
  Object.keys(chipGroups).forEach(g => (p.get(g) || '').split(',').filter(Boolean).forEach(v => {
    chipGroups[g].add(v);
    const b = document.querySelector(`.chip-btn[data-group="${g}"][data-value="${CSS.escape(v)}"]`);
    if (b) b.setAttribute('aria-pressed', 'true');
  }));
  [['periodo', periodo], ['genero', genero], ['dificuldade', dificuldade], ['formato', formato], ['fonte', fonte], ['lista', lista], ['ordem', ordem]].forEach(([k, el]) => { if (p.get(k)) el.value = p.get(k); });
  if (p.get('audio')) audio.checked = true;
  if (p.get('gratis')) gratis.checked = true;
  if (p.get('aqui') && interno) interno.checked = true;
  if (p.get('q')) q.value = p.get('q');
  more.classList.toggle('closed', window.matchMedia('(max-width: 700px)').matches && extras() === 0);
  apply(false);

  $('limpar').addEventListener('click', () => {
    Object.values(chipGroups).forEach(s => s.clear());
    document.querySelectorAll('.chip-btn').forEach(b => b.setAttribute('aria-pressed', 'false'));
    q.value = ''; [periodo, genero, dificuldade, formato, fonte, lista].forEach(el => { el.value = ''; }); ordem.value = 'sugerida';
    audio.checked = false; gratis.checked = false; if (interno) interno.checked = false;
    apply(true);
  });
  $('sorteio').addEventListener('click', () => {
    const pool = apply(false).filter(c => !store.lido[c.id]);
    if (!pool.length) return;
    const c = pool[Math.floor(Math.random() * pool.length)];
    c.scrollIntoView({ behavior: 'smooth', block: 'center' });
    c.classList.add('flash'); setTimeout(() => c.classList.remove('flash'), 2200);
    const h = c.querySelector('h3'); if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); }
  });
})();

// Aprenda Latim — progresso das lições (salvo só no navegador do leitor)
(function () {
  const KEY = 'bibliotheca-latina:licoes';
  let done = {};
  try { done = JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) {}
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(done)); } catch (e) {} };
  document.querySelectorAll('[data-licao-concluir]').forEach(b => {
    const id = b.dataset.licaoConcluir;
    const refresh = () => { b.setAttribute('aria-pressed', done[id] ? 'true' : 'false'); b.textContent = done[id] ? '✓ Capítulo concluído' : 'Marcar capítulo como concluído'; };
    refresh();
    b.addEventListener('click', () => { if (done[id]) delete done[id]; else done[id] = Date.now(); save(); refresh(); });
  });
  const lista = document.querySelectorAll('.licoes li[data-licao]');
  if (lista.length) {
    let n = 0;
    lista.forEach(li => { const ok = !!done[li.dataset.licao]; const f = li.querySelector('.feita'); if (f) f.hidden = !ok; if (ok) n++; });
    const bar = document.querySelector('.progresso-livro');
    if (bar) {
      const total = Number(bar.dataset.total || lista.length);
      bar.querySelector('.txt').textContent = n ? `${n} de ${total} capítulos disponíveis concluídos neste navegador.` : 'Nenhum capítulo concluído ainda. O progresso fica salvo neste navegador.';
      bar.querySelector('.barra div').style.width = (total ? Math.round(100 * n / total) : 0) + '%';
    }
  }
})();

// Aprenda Latim: "Reportar problema" (sem servidor). Com formulário externo configurado no build, abre o
// formulário pré-preenchido; sem ele, monta o relatório para o leitor copiar. Não coleta dados pessoais.
(function () {
  const box = document.getElementById('reportar'), form = box && box.querySelector('.form-reportar');
  if (!form) return;
  const sel = form.elements.secao;
  // cada título de seção tem uma marca discreta (⚑) que abre o painel com a seção já escolhida
  document.querySelectorAll('a[href="#reportar"]').forEach(a => a.addEventListener('click', () => {
    box.open = true; sel.value = a.dataset.secao || 'geral';
  }));
  const out = form.querySelector('.relatorio');
  form.addEventListener('submit', ev => {
    ev.preventDefault();
    const d = form.dataset, secao = sel.options[sel.selectedIndex].text;
    const vals = { capitulo: d.capitulo, secao: secao, categoria: form.elements.categoria.value, descricao: form.elements.descricao.value.trim(), sugestao: form.elements.sugestao.value.trim() };
    if (!vals.descricao) { form.elements.descricao.focus(); return; }
    if (d.url) {
      const p = new URLSearchParams({ usp: 'pp_url' });
      Object.keys(vals).forEach(k => { const campo = d['campo' + k.charAt(0).toUpperCase() + k.slice(1)]; if (campo) p.set(campo, vals[k]); });
      window.open(d.url + (d.url.includes('?') ? '&' : '?') + p.toString(), '_blank', 'noopener');
      return;
    }
    const txt = `Elementa Linguae Latinae · relatório de problema\n${vals.capitulo}\nSeção: ${vals.secao}\nTipo: ${vals.categoria}\nProblema: ${vals.descricao}\nSugestão: ${vals.sugestao || '—'}\nPágina: ${location.href.split('#')[0]}`;
    out.hidden = false; out.querySelector('textarea').value = txt;
    if (d.email) {
      const assunto = `[Elementa] ${vals.capitulo.replace(/ \(.*\)$/, '')} · ${vals.categoria}`;
      location.href = `mailto:${d.email}?subject=${encodeURIComponent(assunto)}&body=${encodeURIComponent(txt)}`;
    }
  });
  const copiar = form.querySelector('.copiar');

  copiar.addEventListener('click', () => {
    const t = out.querySelector('textarea');
    const ok = () => { copiar.textContent = '✓ Copiado'; setTimeout(() => { copiar.textContent = 'Copiar relatório'; }, 2000); };
    if (navigator.clipboard) navigator.clipboard.writeText(t.value).then(ok, () => { t.select(); document.execCommand('copy'); ok(); });
    else { t.select(); document.execCommand('copy'); ok(); }
  });
})();

// "Apoie este projeto": copiar a chave PIX (só existe na página quando a chave foi confirmada)
document.querySelectorAll('.copiar-pix').forEach(b => b.addEventListener('click', () => {
  const v = b.dataset.copiar, ok = () => { b.textContent = '✓ Chave copiada'; setTimeout(() => { b.textContent = 'Copiar chave PIX'; }, 2000); };
  if (navigator.clipboard) navigator.clipboard.writeText(v).then(ok, () => prompt('Chave PIX:', v)); else prompt('Chave PIX:', v);
}));

// Leitor interno: letra, largura e aparência, e o ponto de leitura de cada obra (salvos só neste navegador).
(function () {
  const d = document.documentElement, KP = 'bibliotheca-latina:leitor', KT = 'bibliotheca-latina:tema', KL = 'bibliotheca-latina:leituras';
  const get = (k, def) => { try { return JSON.parse(localStorage.getItem(k)) || def; } catch (e) { return def; } };
  const put = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} };
  const FS = [0.85, 0.93, 1, 1.1, 1.22, 1.36, 1.5];

  document.querySelectorAll('.controles').forEach(ctr => {
    const prefs = get(KP, {});
    let tema = ''; try { tema = localStorage.getItem(KT) || ''; } catch (e) {}
    const idx = () => { const i = FS.indexOf(Number(prefs.fs || 1)); return i < 0 ? 2 : i; };
    const refresh = () => {
      ctr.querySelectorAll('[data-leitor="larg"]').forEach(b => b.setAttribute('aria-pressed', String((prefs.larg || '') === b.dataset.v)));
      ctr.querySelectorAll('[data-leitor="tema"]').forEach(b => b.setAttribute('aria-pressed', String(tema === b.dataset.v)));
      ctr.querySelector('[data-leitor="fs-"]').disabled = idx() === 0;
      ctr.querySelector('[data-leitor="fs+"]').disabled = idx() === FS.length - 1;
    };
    ctr.addEventListener('click', ev => {
      const b = ev.target.closest('button'); if (!b) return;
      const a = b.dataset.leitor;
      if (a === 'fs+' || a === 'fs-') {
        // mantém na tela o trecho que estava sendo lido
        const alvo = atual(); const y0 = alvo ? alvo.getBoundingClientRect().top : 0;
        prefs.fs = FS[Math.max(0, Math.min(FS.length - 1, idx() + (a === 'fs+' ? 1 : -1)))];
        d.style.setProperty('--leitor-fs', prefs.fs); put(KP, prefs);
        if (alvo) window.scrollBy({ top: alvo.getBoundingClientRect().top - y0, behavior: 'instant' });
      } else if (a === 'larg') {
        prefs.larg = prefs.larg === b.dataset.v ? '' : b.dataset.v;
        if (prefs.larg) d.dataset.largura = prefs.larg; else delete d.dataset.largura;
        put(KP, prefs);
      } else if (a === 'tema') {
        tema = b.dataset.v;
        if (tema) d.dataset.tema = tema; else delete d.dataset.tema;
        try { if (tema) localStorage.setItem(KT, tema); else localStorage.removeItem(KT); } catch (e) {}
      }
      refresh();
    });
    refresh();
  });

  const art = document.querySelector('.texto-latino');
  const marks = art ? Array.from(art.querySelectorAll('.par, .l, h2, h3')) : [];
  function atual() {   // primeiro trecho cujo fim ainda está abaixo do cabeçalho fixo
    if (!marks.length) return null;
    const topo = (document.querySelector('.site-header') || {}).offsetHeight || 0;
    let lo = 0, hi = marks.length - 1;
    while (lo < hi) { const m = (lo + hi) >> 1; if (marks[m].getBoundingClientRect().bottom > topo + 4) hi = m; else lo = m + 1; }
    return marks[lo];
  }
  const rotulo = el => {
    if (/^H[23]$/.test(el.tagName)) return el.textContent;
    const ref = el.id.replace(/^p-/, '§ ').replace(/^v-\d+-/, 'verso ');
    let h = el; while (h && !/^H[23]$/.test(h.tagName)) h = h.previousElementSibling || (h.parentElement !== art ? h.parentElement : null);
    const sec = h ? h.textContent : (art.dataset.tituloParte || '');
    return (sec ? sec + ', ' : '') + ref;
  };
  const todos = get(KL, {});

  if (art) {
    const obra = art.dataset.obra, parte = Number(art.dataset.parte || 1), partes = Number(art.dataset.partes || 1);
    const pt = document.querySelector('.progresso-txt');
    const pct = el => Math.round(100 * ((parte - 1) + marks.indexOf(el) / Math.max(1, marks.length - 1)) / partes);
    let timer = 0, mexeu = false;
    function salvar() {
      const el = atual(); if (!el) return;
      const p = pct(el); if (pt) pt.textContent = p + '% lido';
      if (!mexeu) return;
      todos[obra] = { url: location.pathname, ancora: el.id, pct: p, rotulo: rotulo(el), t: Date.now() };
      put(KL, todos);
    }
    window.addEventListener('scroll', () => { mexeu = true; clearTimeout(timer); timer = setTimeout(salvar, 300); }, { passive: true });
    salvar();
    const sv = todos[obra], box = document.querySelector('.retomar');
    if (sv && sv.ancora && box && !location.hash && !(sv.url === location.pathname && sv.pct === 0)) {
      const href = (sv.url === location.pathname ? '' : sv.url) + '#' + sv.ancora;
      box.innerHTML = 'Continuar de onde parou: <a></a>'; const a = box.querySelector('a');
      a.href = href; a.textContent = sv.rotulo + ' (' + sv.pct + '%)';
      box.hidden = false;
    }
  }
  // página de apresentação de uma obra longa (sem texto): link para o ponto salvo
  document.querySelectorAll('.retomar[data-obra]').forEach(box => {
    const sv = todos[box.dataset.obra]; if (!sv || !sv.ancora) return;
    box.innerHTML = 'Continuar de onde parou: <a></a>'; const a = box.querySelector('a');
    a.href = sv.url + '#' + sv.ancora; a.textContent = sv.rotulo + ' (' + sv.pct + '%)'; box.hidden = false;
  });
  // "Ler aqui": obras começadas neste navegador, da mais recente para a mais antiga
  const cont = document.querySelector('.continuar');
  if (cont) {
    const itens = Object.entries(todos).filter(([id]) => document.getElementById(id)).sort((a, b) => b[1].t - a[1].t);
    if (itens.length) {
      const ul = cont.querySelector('ul');
      itens.forEach(([id, sv]) => {
        const li = document.createElement('li'), a = document.createElement('a');
        a.href = sv.url + '#' + sv.ancora; a.textContent = document.getElementById(id).querySelector('h3').textContent;
        li.append(a, ' · ' + sv.rotulo + ' · ' + sv.pct + '%'); ul.append(li);
      });
      cont.hidden = false;
    }
  }
})();
