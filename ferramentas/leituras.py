"""Leitor interno da Bibliotheca Latina: textos/<id>/{texto.txt, metadata.json} → páginas em docs/leituras/,
PDF e EPUB em docs/downloads/textos/. Chamado por construir.py; o formato de texto.txt está descrito em
ferramentas/importar_perseus.py. Só entram obras com metadata.decisao == 'hospedar' (auditoria de direitos feita)."""
import hashlib, html, json, os, re, uuid, zipfile
from datetime import datetime, timezone

e = lambda s: html.escape(str(s), quote=True)
AUDITORIA = ['1_autor_e_obra', '2_edicao_fonte', '3_data_e_editor', '4_direitos_da_edicao', '5_licenca_da_transcricao',
             '6_permissao_de_reproduzir', '7_permissao_de_derivados', '8_atribuicao_exigida']
DIVIDIR_ACIMA = 25000
# o código deste módulo entra no hash dos downloads: mudar a forma de gerar PDF/EPUB regenera todos os arquivos
GERADOR = hashlib.sha1(open(__file__, 'rb').read()).hexdigest()   # palavras: obras maiores e com vários livros ganham uma página por livro

def carregar(root, catalogo):
    """Lê e valida textos/. catalogo: dict id → obra do catálogo. Sai com erro se algo não confere."""
    base, out, errs = os.path.join(root, 'textos'), {}, []
    if not os.path.isdir(base): return out
    for id_ in sorted(os.listdir(base)):
        d = os.path.join(base, id_)
        if not os.path.isdir(d): continue
        try:
            m = json.load(open(os.path.join(d, 'metadata.json'), encoding='utf-8'))
            txt = open(os.path.join(d, 'texto.txt'), encoding='utf-8').read()
        except FileNotFoundError as ex:
            errs.append(f'{id_}: falta {os.path.basename(ex.filename)}'); continue
        if m.get('id') != id_: errs.append(f'{id_}: metadata.id diferente da pasta')
        if id_ not in catalogo: errs.append(f'{id_}: não está em data/catalogo.json')
        if m.get('decisao') != 'hospedar': errs.append(f'{id_}: decisao != hospedar')
        for k in ('titulo_latino', 'forma', 'edicoes', 'transcricao', 'licenca', 'atribuicao', 'auditoria', 'normalizacao', 'verificado_em'):
            if not m.get(k): errs.append(f'{id_}: falta {k}')
        for k in AUDITORIA:
            if not (m.get('auditoria') or {}).get(k): errs.append(f'{id_}: auditoria sem {k}')
        if m.get('forma') not in ('prosa', 'verso'): errs.append(f'{id_}: forma inválida')
        eds = m.get('edicoes') or []
        m['ed_curta'] = '; '.join(f'{x["editor"]} ({x["ano"]})' for x in eds)
        m['ed_longa'] = '; '.join(f'<i>{e(x["edicao"])}</i>, ed. {e(x["editor"])} ({e(x["local"])}: {e(x["editora"])}, {e(x["ano"])})' + (f' [{e(x["partes"])}]' if x.get('partes') else '') for x in eds)
        m['ed_texto'] = '; '.join(f'{x["edicao"]}, ed. {x["editor"]} ({x["local"]}: {x["editora"]}, {x["ano"]})' + (f' [{x["partes"]}]' if x.get('partes') else '') for x in eds)
        m['arquivos'] = (m.get('transcricao') or {}).get('arquivos') or []
        if not m['arquivos']: errs.append(f'{id_}: transcricao.arquivos vazio')
        m['blocos'] = parse(txt)
        m['palavras'] = sum(len(b[2].split()) for b in m['blocos'] if b[0] == 'x')
        m['hash'] = hashlib.sha1((GERADOR + txt + json.dumps({k: v for k, v in m.items() if k not in ('blocos', 'palavras')}, sort_keys=True, ensure_ascii=False)).encode()).hexdigest()[:12]
        m['partes'] = partes(m)
        out[id_] = m
    if errs: raise SystemExit('textos/ inválido:\n  ' + '\n  '.join(errs))
    return out

def parse(txt):
    """Blocos: ('h', nível, título) · ('fala', nome) · ('p'|'v', ref, texto) · ('sep',)."""
    bl = []
    for linha in txt.splitlines():
        if not linha.strip(): bl.append(('sep',)); continue
        m = re.match(r'^(#{1,2}) (.*)$', linha)
        if m: bl.append(('h', len(m.group(1)), m.group(2).strip())); continue
        if linha.startswith('> '): bl.append(('fala', linha[2:].strip())); continue
        ref, _, t = linha.partition('\t')
        bl.append(('x', ref.strip(), t.strip()))
    return bl

def partes(m):
    """Divide em livros (cabeçalhos de 1º nível) quando a obra é longa; senão, uma parte só."""
    tipo = 'p' if m['forma'] == 'prosa' else 'v'
    bl = [(b[0] if b[0] != 'x' else tipo,) + b[1:] for b in m['blocos']]
    m['blocos'] = bl
    h1 = [i for i, b in enumerate(bl) if b[0] == 'h' and b[1] == 1]
    if m['palavras'] <= DIVIDIR_ACIMA or len(h1) < 2:
        return [dict(n=1, titulo='', blocos=bl)]
    ps = []
    for k, i in enumerate(h1):
        fim = h1[k + 1] if k + 1 < len(h1) else len(bl)
        ps.append(dict(n=k + 1, titulo=bl[i][2], blocos=bl[i + 1:fim]))
    return ps

def _inline(t):
    return re.sub(r'\{(\w+)\}', r'<sup class="sec">\1</sup>', e(t))

def corpo_html(blocos, forma, xhtml=False, pdf=False):
    """HTML do texto latino. Ids estáveis por página (s-k para seções, p-ref para parágrafos, v-k-n para versos)."""
    out, verso_aberto, sec, toc, primeiro = [], False, 0, [], True
    vistos = set()
    def uid(base):   # ids únicos na página (refs repetidas ou vazias no texto-fonte não podem gerar ids iguais)
        i, k = base, 2
        while i in vistos: i = f'{base}~{k}'; k += 1
        vistos.add(i); return i
    def fecha():
        nonlocal verso_aberto
        if verso_aberto: out.append('</div>'); verso_aberto = False
    for b in blocos:
        if b[0] == 'h':
            fecha(); sec += 1; primeiro = True
            tag = 'h2' if b[1] == 1 else 'h3'
            out.append(f'<{tag} id="s-{sec}">{e(b[2])}</{tag}>'); toc.append((b[1], b[2], f's-{sec}'))
        elif b[0] == 'sep':
            fecha()
        elif b[0] == 'fala':
            fecha(); out.append(f'<p class="fala">{e(b[1])}</p>')
        elif b[0] == 'p':
            fecha()
            ref = b[1]
            if not ref:   # linha sem número (saudação de carta, rubrica): sem âncora
                out.append(f'<p class="par sem-ref">{_inline(b[2])}</p>'); continue
            rid = uid('p-' + re.sub(r'[^\w.-]', '_', ref))
            mostra = ref.split('.')[-1] if '.' in ref else ref
            out.append(f'<p class="par" id="{rid}"><span class="ref">{e(mostra)}</span> {_inline(b[2])}</p>')
        elif b[0] == 'v':
            if not verso_aberto: out.append('<div class="versos">'); verso_aberto = True
            n = b[1]
            idattr = f' id="{uid(f"v-{sec}-" + re.sub(r"[^\w-]", "_", n))}"' if n else ''
            num = e(n) if (n and (primeiro or (n.isdigit() and int(n) % 5 == 0))) else ''
            cls = 'l' if n else 'l sem-ref'
            out.append(f'<p class="{cls}"{idattr}><span class="n">{num}</span>{_inline(b[2])}</p>' if xhtml or pdf else
                       f'<span class="{cls}"{idattr}><span class="n">{num}</span>{_inline(b[2])}</span>')
            primeiro = False
    fecha()
    return '\n'.join(out), toc

def ficha(w, m, DIF, GRADUS, ROMAN):
    g, d = w['reading_stage'], w.get('difficulty')
    itens = [('Autor', w.get('author') or '—'), ('Obra', m['titulo_latino']), ('Período', w['historical_period']), ('Gênero', w['genre']),
             ('Dificuldade', f'{d} · {DIF[d]}' if d else '—'), ('Etapa do percurso', f'{ROMAN[g]} · {GRADUS[g]["nome"]}'),
             ('Extensão', f'{m["palavras"]:,} palavras'.replace(',', '.') + (f' · {w["estimated_reading_time"]}' if w.get('estimated_reading_time') else ''))]
    return '<dl class="ficha">' + ''.join(f'<div><dt>{k}</dt><dd>{e(v)}</dd></div>' for k, v in itens) + '</dl>'

def fonte_html(m, w):
    tr, li = m['transcricao'], m['licenca']
    arqs = m['arquivos']
    arq_html = (f'<a href="{e(arqs[0])}" target="_blank" rel="noopener">{e(tr["nome"])}</a>' if len(arqs) == 1 else
                f'{e(tr["nome"])}: ' + ', '.join(f'<a href="{e(a)}" target="_blank" rel="noopener">{e(a.rsplit("/", 1)[1].split(".perseus")[0])}</a>' for a in arqs))
    norm = ''.join(f'<li>{e(x)}</li>' for x in m['normalizacao'])
    aud = ''.join(f'<li><b>{e(k.split("_", 1)[1].replace("_", " ").capitalize())}:</b> {e(m["auditoria"][k])}</li>' for k in AUDITORIA)
    return f'''<section class="fonte-direitos" id="fonte"><h2>Fonte, edição e direitos</h2>
<dl class="ficha">
<div><dt>Edição impressa</dt><dd>{m["ed_longa"]}</dd></div>
<div><dt>Transcrição digital</dt><dd>{arq_html} (versão {e(tr["commit"][:7])}, consultada em {e(tr["acessado_em"])})</dd></div>
<div><dt>Licença</dt><dd><a href="{e(li["url"])}" target="_blank" rel="license noopener">{e(li["nome"])}</a>. {e(li["declaracao"])}</dd></div>
<div><dt>No catálogo</dt><dd><a href="{e(w["source_url"])}" target="_blank" rel="noopener">{e(w["source_name"])} ↗</a></dd></div>
</dl>
<p class="atribuicao">{e(m["atribuicao"])}</p>
<details><summary>O que foi alterado em relação à fonte</summary><ul>{norm}</ul><p>Omitido: {e("; ".join(m["omitido"]))}.</p></details>
<details><summary>Auditoria de direitos ({e(m["verificado_em"])})</summary><ul>{aud}</ul></details>
</section>'''

CONTROLES = '''<div class="controles" role="group" aria-label="Ajustes de leitura">
<span class="grupo"><span class="rot">Letra</span><button type="button" data-leitor="fs-" aria-label="Diminuir a letra">A−</button><button type="button" data-leitor="fs+" aria-label="Aumentar a letra">A+</button></span>
<span class="grupo"><span class="rot">Largura</span><button type="button" data-leitor="larg" data-v="estreita" aria-pressed="false">Estreita</button><button type="button" data-leitor="larg" data-v="larga" aria-pressed="false">Larga</button></span>
<span class="grupo"><span class="rot">Aparência</span><button type="button" data-leitor="tema" data-v="" aria-pressed="false">Automática</button><button type="button" data-leitor="tema" data-v="claro" aria-pressed="false">Clara</button><button type="button" data-leitor="tema" data-v="escuro" aria-pressed="false">Escura</button></span>
<span class="grupo progresso-txt" aria-live="polite"></span>
</div>'''

# ───────────── PDF ─────────────
PDF_CSS = '''
@page { size: A5; margin: 16mm 14mm 18mm 16mm; @bottom-center { content: counter(page); font: 8pt Georgia, serif; color: #6e665b; } }
@page :first { @bottom-center { content: none; } }
body { font: 10.5pt/1.5 Georgia, "Times New Roman", serif; color: #211c17; hyphens: auto; }
.capa { page-break-after: always; text-align: center; padding-top: 30mm; }
.capa .k { font: 8pt Helvetica, Arial, sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #8a2b1d; }
.capa h1 { font-size: 24pt; line-height: 1.15; margin: 10mm 0 4mm; } .capa .autor { font-size: 14pt; font-style: italic; margin: 0 0 18mm; }
.capa .ed { font-size: 9pt; color: #4b443b; } .capa .fio { width: 30mm; height: 1px; background: #a98434; margin: 8mm auto; }
.direitos { page-break-after: always; font-size: 8.6pt; color: #4b443b; } .direitos h2 { font-size: 11pt; color: #211c17; margin-top: 0; }
.direitos li { margin: 0 0 3pt; } a { color: #27496e; text-decoration: none; }
h2 { font-size: 14pt; text-align: center; margin: 0 0 6mm; page-break-before: always; page-break-after: avoid; color: #8a2b1d; }
h2:first-child { page-break-before: avoid; }
h3 { font-size: 11pt; margin: 6mm 0 2.5mm; page-break-after: avoid; font-style: italic; }
.par { margin: 0 0 2.4mm; text-align: justify; } .par .ref { font: bold 7.5pt Helvetica, Arial, sans-serif; color: #8a2b1d; margin-right: 1.5mm; }
.sec { font: 6.5pt Helvetica, Arial, sans-serif; color: #6e665b; vertical-align: super; line-height: 0; }
.versos { margin: 0 0 3mm; } .l { margin: 0; padding-left: 9mm; position: relative; text-indent: -2mm; page-break-inside: avoid; }
.l .n { position: absolute; left: -2mm; width: 8mm; text-align: right; font: 7pt Helvetica, Arial, sans-serif; color: #6e665b; top: .25em; text-indent: 0; }
.fala { font-variant: small-caps; letter-spacing: .04em; margin: 3mm 0 1mm; color: #8a2b1d; page-break-after: avoid; }
'''

def pdf_html(w, m, SITE, ROMAN):
    corpo, _ = corpo_html(m['blocos'], m['forma'], pdf=True)
    li = m['licenca']
    norm = ''.join(f'<li>{e(x)}</li>' for x in m['normalizacao'])
    return f'''<!doctype html><html lang="la"><head><meta charset="utf-8"><title>{e(w["title"])}</title>
<meta name="author" content="{e(w.get("author") or "")}"><meta name="description" content="{e(m["atribuicao"])}">
<style>{PDF_CSS}</style></head><body>
<section class="capa"><p class="k">Bibliotheca Latina · textus Latinus</p><h1>{e(m["titulo_latino"])}</h1><p class="autor">{e(w.get("author") or "")}</p>
<div class="fio"></div><p class="ed">Texto latino: {m["ed_longa"]}</p>
<p class="ed">{e(SITE)}leituras/{e(w["id"])}.html</p></section>
<section class="direitos" lang="pt-BR"><h2>Fonte e licença</h2><p>{e(m["atribuicao"])}</p>
<p>Licença: <a href="{e(li["url"])}">{e(li["nome"])}</a> ({e(li["url"])}). Você pode copiar, redistribuir e adaptar este arquivo, dando o crédito acima e mantendo a mesma licença.</p>
<p>Transcrição: {"; ".join(e(a) for a in m["arquivos"])}</p>
<p><b>Alterações em relação à fonte</b></p><ul>{norm}</ul><p>Omitido: {e("; ".join(m["omitido"]))}.</p>
<p>Gerado em {datetime.now(timezone.utc).date().isoformat()} pela Bibliotheca Latina. O texto latino não foi modernizado nem resumido.</p></section>
<main lang="la">{corpo}</main></body></html>'''

# ───────────── EPUB 3 ─────────────
EPUB_CSS = '''body { font-family: serif; line-height: 1.5; margin: 0 4%; }
h1, h2, h3 { font-weight: normal; } h1 { text-align: center; margin-top: 20%; } h2 { text-align: center; color: #8a2b1d; margin: 1.5em 0 1em; }
h3 { font-style: italic; margin: 1.4em 0 .5em; } .autor { text-align: center; font-style: italic; } .ed { text-align: center; font-size: .85em; color: #4b443b; }
.par { margin: 0 0 .6em; text-align: justify; } .ref { font-family: sans-serif; font-size: .7em; font-weight: bold; color: #8a2b1d; }
.sec { font-family: sans-serif; font-size: .6em; color: #6e665b; } .versos { margin: 0 0 1em; }
.l { margin: 0; padding-left: 2.6em; text-indent: -2.6em; } .l .n { display: inline-block; width: 2.2em; margin-right: .4em; text-align: right; font-family: sans-serif; font-size: .7em; color: #6e665b; text-indent: 0; }
.fala { font-variant: small-caps; color: #8a2b1d; margin: 1em 0 .2em; } .direitos { font-size: .85em; }'''

def _xhtml(titulo, corpo, lang='la'):
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang}" lang="{lang}">
<head><meta charset="utf-8"/><title>{e(titulo)}</title><link rel="stylesheet" type="text/css" href="estilo.css"/></head>
<body>{corpo}</body></html>'''

def build_epub(w, m, destino, SITE):
    li = m['licenca']
    uid = 'urn:uuid:' + str(uuid.uuid5(uuid.NAMESPACE_URL, SITE + 'leituras/' + w['id']))
    caps = []
    for p in m['partes']:
        bl = p['blocos'] if not p['titulo'] else [('h', 1, p['titulo'])] + p['blocos']
        corpo, toc = corpo_html(bl, m['forma'], xhtml=True)
        caps.append((f'parte{p["n"]:02d}.xhtml', p['titulo'] or m['titulo_latino'], corpo, toc))
    capa = f'''<section epub:type="titlepage"><h1>{e(m["titulo_latino"])}</h1><p class="autor">{e(w.get("author") or "")}</p>
<p class="ed">Texto latino: {m["ed_longa"]}.</p><p class="ed">Bibliotheca Latina · {e(SITE)}</p></section>'''
    norm = ''.join(f'<li>{e(x)}</li>' for x in m['normalizacao'])
    direitos = f'''<section class="direitos" epub:type="copyright-page"><h2>Fonte e licença</h2><p>{e(m["atribuicao"])}</p>
<p>Licença: <a href="{e(li["url"])}">{e(li["nome"])}</a>. Você pode copiar, redistribuir e adaptar este arquivo, dando o crédito acima e mantendo a mesma licença.</p>
<p>Transcrição: {e(m["transcricao"]["nome"])}{"".join(f' <a href="{e(a)}">[{k}]</a>' for k, a in enumerate(m["arquivos"], 1))}</p><p>Alterações em relação à fonte:</p><ul>{norm}</ul></section>'''
    nav_items = ''
    for f, t, _, toc in caps:
        subs = ''.join(f'<li><a href="{f}#{a}">{e(tt)}</a></li>' for lv, tt, a in toc if lv == 2)
        nav_items += f'<li><a href="{f}">{e(t)}</a>' + (f'<ol>{subs}</ol>' if subs and len(caps) > 1 else '') + '</li>'
    if len(caps) == 1 and caps[0][3]:
        nav_items = ''.join(f'<li><a href="{caps[0][0]}#{a}">{e(tt)}</a></li>' for lv, tt, a in caps[0][3] if lv == 1) or \
                    ''.join(f'<li><a href="{caps[0][0]}#{a}">{e(tt)}</a></li>' for lv, tt, a in caps[0][3])
    if not nav_items: nav_items = f'<li><a href="{caps[0][0]}">{e(m["titulo_latino"])}</a></li>'
    nav = f'''<nav epub:type="toc" id="toc"><h2>Index</h2><ol><li><a href="capa.xhtml">{e(m["titulo_latino"])}</a></li><li><a href="direitos.xhtml">Fonte e licença</a></li>{nav_items}</ol></nav>'''
    mod = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    itens = ''.join(f'<item id="c{k}" href="{f}" media-type="application/xhtml+xml"/>' for k, (f, *_) in enumerate(caps))
    spine = ''.join(f'<itemref idref="c{k}"/>' for k in range(len(caps)))
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid" xml:lang="la">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">{uid}</dc:identifier><dc:title>{e(m["titulo_latino"])}</dc:title><dc:creator>{e(w.get("author") or "")}</dc:creator>
<dc:language>la</dc:language><dc:publisher>Bibliotheca Latina</dc:publisher><dc:source>{e(m["ed_texto"])}; {e(m["transcricao"]["nome"])}</dc:source>
<dc:rights>{e(li["nome"])} · {e(m["atribuicao"])}</dc:rights><meta property="dcterms:modified">{mod}</meta>
</metadata>
<manifest><item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/><item id="css" href="estilo.css" media-type="text/css"/>
<item id="capa" href="capa.xhtml" media-type="application/xhtml+xml"/><item id="direitos" href="direitos.xhtml" media-type="application/xhtml+xml"/>{itens}</manifest>
<spine><itemref idref="capa"/><itemref idref="direitos"/>{spine}</spine>
</package>'''
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with zipfile.ZipFile(destino, 'w') as z:
        z.writestr(zipfile.ZipInfo('mimetype'), 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        def put(n, s): z.writestr(n, s, compress_type=zipfile.ZIP_DEFLATED)
        put('META-INF/container.xml', '<?xml version="1.0" encoding="utf-8"?>\n<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>')
        put('OEBPS/content.opf', opf); put('OEBPS/estilo.css', EPUB_CSS)
        put('OEBPS/nav.xhtml', _xhtml('Index', nav)); put('OEBPS/capa.xhtml', _xhtml(m['titulo_latino'], capa))
        put('OEBPS/direitos.xhtml', _xhtml('Fonte e licença', direitos, 'pt-BR'))
        for f, t, corpo, _ in caps: put('OEBPS/' + f, _xhtml(t, corpo))
