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
        count = $('count'), empty = $('empty');
  const chipGroups = { etapa: new Set(), categoria: new Set(), tipo: new Set() };
  const norm = s => (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');

  document.querySelectorAll('.chip-btn').forEach(b => b.addEventListener('click', () => {
    const g = chipGroups[b.dataset.group], v = b.dataset.value;
    if (g.has(v)) g.delete(v); else g.add(v);
    b.setAttribute('aria-pressed', g.has(v) ? 'true' : 'false');
    apply(true);
  }));
  [q, periodo, genero, dificuldade, formato, fonte, lista, ordem, audio, gratis].forEach(el => el && el.addEventListener(el === q ? 'input' : 'change', () => apply(true)));

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
    cards.forEach(c => { c.hidden = true; });
    shown.forEach(c => { c.hidden = false; grid.appendChild(c); });
    count.textContent = shown.length === 1 ? '1 recurso' : shown.length + ' recursos';
    empty.hidden = shown.length > 0;
    if (push) {
      const p = new URLSearchParams();
      Object.entries(chipGroups).forEach(([g, s]) => { if (s.size) p.set(g, [...s].join(',')); });
      [['periodo', periodo], ['genero', genero], ['dificuldade', dificuldade], ['formato', formato], ['fonte', fonte], ['lista', lista]].forEach(([k, el]) => { if (el.value) p.set(k, el.value); });
      if (audio.checked) p.set('audio', '1');
      if (gratis.checked) p.set('gratis', '1');
      if (ordem.value !== 'sugerida') p.set('ordem', ordem.value);
      if (q.value.trim()) p.set('q', q.value.trim());
      history.replaceState(null, '', (p.toString() ? '?' + p : location.pathname));
    }
    return shown;
  }
  window.applyFilters = apply;

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
  if (p.get('q')) q.value = p.get('q');
  apply(false);

  $('limpar').addEventListener('click', () => {
    Object.values(chipGroups).forEach(s => s.clear());
    document.querySelectorAll('.chip-btn').forEach(b => b.setAttribute('aria-pressed', 'false'));
    q.value = ''; [periodo, genero, dificuldade, formato, fonte, lista].forEach(el => { el.value = ''; }); ordem.value = 'sugerida';
    audio.checked = false; gratis.checked = false;
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
    const txt = `Elementa Linguae Latinae (beta) · relatório de problema\n${vals.capitulo}\nSeção: ${vals.secao}\nTipo: ${vals.categoria}\nProblema: ${vals.descricao}\nSugestão: ${vals.sugestao || '—'}\nPágina: ${location.href.split('#')[0]}`;
    out.hidden = false; out.querySelector('textarea').value = txt;
    if (d.email) {
      const assunto = `[Elementa beta] ${vals.capitulo.replace(/ \(.*\)$/, '')} · ${vals.categoria}`;
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
