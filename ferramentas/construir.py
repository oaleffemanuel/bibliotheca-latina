"""Constrói o site (docs/), o guia de leitura em PDF e a planilha de acompanhamento a partir de data/catalogo.json.

Uso:  python3 ferramentas/construir.py [--sem-pdf] [--sem-xlsx] [--so-publicadas]
Requisitos: Python 3.10+. Para o PDF, weasyprint; para a planilha, openpyxl. O site em si é HTML/CSS/JS puro.
No macOS com Homebrew, se o weasyprint reclamar de libgobject:
    DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 ferramentas/construir.py
"""
import base64, csv, hashlib, html, json, os, re, sys, unicodedata
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'docs')
DATA = os.path.join(ROOT, 'data')
SITE = 'https://oaleffemanuel.github.io/bibliotheca-latina/'
REPO = 'https://github.com/oaleffemanuel/bibliotheca-latina'
CONTATO_EMAIL = 'aleffoemanuel@gmail.com'
# Doação voluntária por PIX: só aparece quando a chave for confirmada pelo responsável, ex.:
# PIX = dict(chave='...', tipo='e-mail', titular='...'). Nunca preencher com chave suposta.
PIX = None
PDF_NAME = 'guia-de-leitura-bibliotheca-latina.pdf'
XLSX_NAME = 'diario-de-leitura-bibliotheca-latina.xlsx'
TODAY = date.today().isoformat()
VER = hashlib.sha1(b''.join(open(os.path.join(DOCS, 'assets', f), 'rb').read() for f in ('style.css', 'app.js'))).hexdigest()[:8]

sys.path.insert(0, ROOT)
import importlib
from conteudo import livro as LIVRO

W = json.load(open(os.path.join(DATA, 'catalogo.json'), encoding='utf-8'))
CAND = json.load(open(os.path.join(DATA, 'candidatos.json'), encoding='utf-8')) if os.path.exists(os.path.join(DATA, 'candidatos.json')) else []
e = lambda s: html.escape(str(s if s is not None else ''), quote=True)

# ───────────────────────── vocabulário editorial ─────────────────────────
ROMAN = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII'}
GRADUS = {
    1: dict(nome='Prima Verba', pt='Primeiras palavras',
            curta='Palavras, frases curtas e os primeiros capítulos de um método. Para quem está começando do zero ou recomeçando.',
            perfil='Você nunca estudou latim, ou estudou há muito tempo e quer recomeçar com calma.',
            objetivo='Reconhecer as formas mais comuns (nominativo, acusativo, genitivo; presente do indicativo) e entender frases curtas sem traduzir palavra por palavra.',
            como='Siga um método do começo (Familia Romana ou Latin for Beginners) e leia cada capítulo em voz alta. Não decore tabelas antes de ver as formas em frases.',
            meta='Os 10 primeiros capítulos de um método, em 4 a 8 semanas.',
            avancar='Você lê um capítulo didático curto sem consultar nada e sabe dizer quem faz o quê em cada frase.'),
    2: dict(nome='Primae Fabulae', pt='Primeiras narrativas',
            curta='Narrativas curtas e graduadas, escritas para estudantes: fábulas, mitos e cenas da vida romana com vocabulário controlado.',
            perfil='Você conhece as três primeiras declinações, o presente, o imperfeito e o perfeito.',
            objetivo='Ler histórias inteiras com prazer, acostumar-se ao ritmo da frase latina (verbo no fim) e absorver vocabulário por repetição.',
            como='Leia muito e leia fácil: histórias curtas, uma por dia. Releia a anterior antes de começar a nova. Use as notas e o vocabulário do próprio livro.',
            meta='Duas ou três coletâneas graduadas, em 2 a 4 meses.',
            avancar='Você termina uma fábula de uma página precisando de menos de cinco palavras no dicionário.'),
    3: dict(nome='Fundamenta', pt='Fundamentos',
            curta='Leituras mais longas e de gramática progressivamente mais complexa: subjuntivo, oração infinitiva, ablativo absoluto, períodos maiores.',
            perfil='Você já leu narrativas graduadas inteiras e começa a reconhecer o subjuntivo e as orações subordinadas.',
            objetivo='Consolidar a morfologia completa e a sintaxe do período, lendo textos adaptados ou escritos em latim simples mas contínuo.',
            como='Alterne um texto longo (Epitome Historiae Sacrae, Roma Aeterna) com uma gramática de referência aberta ao lado. Anote as construções que se repetem, não só palavras.',
            meta='Um livro longo de leitura contínua, em 3 a 6 meses.',
            avancar='Você segue uma narrativa de várias páginas sem perder o fio e identifica a função de cada oração subordinada.'),
    4: dict(nome='Ad Fontes', pt='Às fontes',
            curta='Os primeiros textos latinos autênticos, com comentário e vocabulário: César, Nepos, Fedro, o Evangelho em latim, Sulpício Severo.',
            perfil='Você leu textos longos adaptados e quer, enfim, ler os próprios autores.',
            objetivo='Passar do latim escrito para estudantes ao latim escrito por romanos, com o apoio de edições comentadas.',
            como='Escolha edições com notas e vocabulário na mesma página (os comentários do DCC e da Open Book Publishers são ideais). Leia trechos curtos todos os dias, releia em voz alta e só então consulte a tradução.',
            meta='Um livro de César ou a Vida de Aníbal inteira, em 2 a 4 meses.',
            avancar='Você lê um capítulo de César com as notas e sente que a dificuldade está no conteúdo, não mais na língua.'),
    5: dict(nome='Auctores Romani', pt='Autores romanos',
            curta='A literatura clássica: Cícero, Virgílio, Ovídio, Sêneca, Salústio, Tito Lívio, Tácito, Lucrécio.',
            perfil='Você já leu um autor autêntico com comentário e quer explorar a literatura romana por conta própria.',
            objetivo='Leitura extensiva de prosa e poesia clássicas; aprender a escandir hexâmetros e a seguir os períodos de Cícero.',
            como='Comece pela prosa (Cícero, Sêneca) e vá à poesia com comentário (Eneida IV, Amores I). Varie autores e gêneros; não é preciso ler obras inteiras de uma vez.',
            meta='Sem meta fixa: esta etapa dura o tempo que você quiser.',
            avancar='Não há próxima etapa obrigatória: as etapas VI e VII são outros caminhos, não degraus mais altos.'),
    6: dict(nome='Latinitas Christiana', pt='Latinidade cristã',
            curta='A Vulgata, os Padres da Igreja, a liturgia e a espiritualidade: Jerônimo, Agostinho, Ambrósio, a Regra de São Bento, os hinos, a Imitação de Cristo.',
            perfil='Qualquer leitor a partir da etapa III. O latim cristão não é mais difícil que o clássico: muitas vezes é mais simples e mais próximo do português.',
            objetivo='Ler as Escrituras e os Padres no original, reconhecendo o vocabulário e a sintaxe próprios do latim tardio e eclesiástico.',
            como='Comece pela Vulgata (Marcos, Gênesis, Salmos), que você já conhece em português. Depois, Sulpício Severo, as Confissões e as Cartas de Jerônimo. A Imitação de Cristo é uma excelente leitura diária.',
            meta='Um Evangelho inteiro e um Padre da Igreja, no seu ritmo.',
            avancar='Você lê a Vulgata com fluência e já consegue acompanhar a argumentação de Agostinho.'),
    7: dict(nome='Sapientia Mediaevalis', pt='Sabedoria medieval',
            curta='O latim medieval e escolástico: Boécio, Beda, Eginardo, Anselmo, Tomás de Aquino, Boaventura, a Legenda Áurea, os Carmina Burana.',
            perfil='Leitores a partir da etapa IV, ou da etapa VI para os textos teológicos. A escolástica tem sintaxe simples e vocabulário técnico; as crônicas são narrativas.',
            objetivo='Ler filosofia, teologia e história medievais no original e dominar o vocabulário técnico da escolástica.',
            como='Para a escolástica, leia um artigo da Summa por vez, seguindo a estrutura (objeções, sed contra, respondeo, respostas). Para as crônicas e lendas, leia como narrativa.',
            meta='O Proslogion inteiro, ou vinte artigos da Summa, ou uma crônica.',
            avancar='Não há próxima etapa. Tolle, lege!'),
}
DIF = {1: 'Elementar', 2: 'Básico', 3: 'Intermediário', 4: 'Avançado', 5: 'Superior'}
DIF_DESC = {1: 'Frases curtas, vocabulário controlado, morfologia básica. Para quem está começando.',
            2: 'Narrativas simples e contínuas; todas as declinações, tempos principais, poucas subordinadas.',
            3: 'Latim autêntico de prosa simples ou textos adaptados longos; subjuntivo, infinitivas, ablativo absoluto.',
            4: 'Prosa clássica elaborada ou poesia com comentário; períodos longos, vocabulário amplo.',
            5: 'Poesia sem comentário, filosofia, retórica densa, latim arcaico ou muito técnico.'}
TIPO = {'original': 'Original', 'adaptado': 'Adaptado', 'simplificado': 'Simplificado', 'didatico': 'Didático'}
TIPO_DESC = {'original': 'texto antigo tal como foi escrito (em edição moderna)', 'adaptado': 'texto antigo abreviado ou reescrito',
             'simplificado': 'versão simplificada de um original', 'didatico': 'escrito do zero para estudantes'}
FMT = {'html': 'Leitura online', 'pdf': 'PDF', 'epub': 'EPUB', 'txt': 'Texto', 'xml': 'XML', 'audio': 'Áudio', 'print': 'Impresso'}
PERIODOS = ['Clássico', 'Pós-clássico', 'Tardio e patrístico', 'Medieval', 'Renascentista e neolatino', 'Moderno (material didático)']
CATEGORIAS = ['Leitura', 'Gramática e referência', 'Método e curso', 'Ferramenta', 'Referência comercial']
RIGHTS = {'public_domain': 'Domínio público', 'creative_commons': 'Creative Commons', 'open_access_limited': 'Acesso aberto (reúso limitado)',
          'commercial': 'Comercial', 'unverified': 'Não verificado'}

for i, w in enumerate(W): w['i'] = i
for g in GRADUS: GRADUS[g]['obras'] = [w for w in W if w['reading_stage'] == g]

def find(id_):
    for w in W:
        if w['id'] == id_: return w
    sys.exit(f'Obra não encontrada no catálogo: {id_}')

def norm(s):
    s = unicodedata.normalize('NFD', (s or '').lower()); return ''.join(c for c in s if unicodedata.category(c) != 'Mn')

def main_link(w):
    return w.get('online_reading_url') or w.get('pdf_url') or w['source_url']

def autor_line(w): return w['author'] or ''

ICON_AUDIO = '<svg aria-hidden="true" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M3 14v-2a9 9 0 0 1 18 0v2"/><rect x="3" y="14" width="4" height="7" rx="1.5"/><rect x="17" y="14" width="4" height="7" rx="1.5"/></svg>'
ICON_DL = '<svg aria-hidden="true" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M12 3v12m0 0-5-5m5 5 5-5M4 21h16"/></svg>'

# ───────────────────────── layout ─────────────────────────
NAV = [('./', 'Início'), ('aprenda/', 'Aprenda Latim'), ('catalogo.html', 'Catálogo'), ('percurso.html', 'Percurso'), ('recursos.html', 'Recursos de estudo'), ('guia.html', 'Como usar'), ('sobre.html', 'Sobre e direitos')]

def page(fname, title, desc, body, extra_head=''):
    base = '../' if '/' in fname else ''
    def cur(h):
        if h == './': return fname == 'index.html'
        if h == 'aprenda/': return fname.startswith('aprenda/')
        return h == fname
    nav = ''.join(f'<a href="{base}{h}"{" aria-current=\"page\"" if cur(h) else ""}>{t}</a>' for h, t in NAV)
    canon = SITE + ('' if fname == 'index.html' else fname.replace('index.html', ''))
    seo = ('<base href="/bibliotheca-latina/">\n<meta name="robots" content="noindex">' if fname == '404.html'
           else f'<link rel="canonical" href="{canon}">\n<meta property="og:url" content="{canon}">')
    full_title = title if fname == 'index.html' else f'{title} · Bibliotheca Latina'
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
{seo}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Bibliotheca Latina">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:locale" content="pt_BR">
<meta name="theme-color" content="#8a2b1d">
<link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/style.css?v={VER}">
{extra_head}</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="{base or './'}"><img src="{base}assets/favicon.svg" alt="" width="36" height="36"><span>Bibliotheca Latina<small>ab initiis ad fontes</small></span></a>
<nav class="nav" aria-label="Principal">{nav}</nav>
</div></header>
<main id="conteudo">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div><p><b>Bibliotheca Latina</b> · <i>ab initiis ad fontes</i>: leituras em latim, das primeiras palavras às fontes.</p>
<p>Projeto pessoal, gratuito e sem fins lucrativos. Não é afiliado às fontes citadas.</p></div>
<div><p>Contato: <a href="mailto:{CONTATO_EMAIL}">{CONTATO_EMAIL}</a> · <a href="{base}sobre.html#apoie">Apoie este projeto</a></p>
<p><a href="{REPO}">Código e dados no GitHub</a> · <a href="{REPO}/issues">Avisar um problema</a></p>
<p>Textos do projeto: CC BY 4.0 · Atualizado em {TODAY}</p></div>
</div></footer>
<script src="{base}assets/app.js?v={VER}" defer></script>
</body>
</html>
'''

def card(w, compact=False):
    g = w['reading_stage']; d = w.get('difficulty')
    tags = [f'<span class="tag stage">Etapa {ROMAN[g]} · {e(GRADUS[g]["nome"])}</span>']
    if d: tags.append(f'<span class="tag diff">Dificuldade {d} · {DIF[d]}</span>')
    if w.get('original_or_adapted'): tags.append(f'<span class="tag kind">{TIPO[w["original_or_adapted"]]}</span>')
    if w.get('audio_available'): tags.append(f'<span class="tag audio">{ICON_AUDIO} Áudio</span>')
    if w.get('notes_available'): tags.append('<span class="tag">Com notas</span>')
    if not w.get('free', True): tags.append('<span class="tag paid">Comercial</span>')
    acts = []
    if w.get('online_reading_url'): acts.append(f'<a class="btn small" href="{e(w["online_reading_url"])}" target="_blank" rel="noopener">Ler na fonte ↗</a>')
    if w.get('pdf_url'): acts.append(f'<a class="btn small ghost" href="{e(w["pdf_url"])}" target="_blank" rel="noopener">PDF ↗</a>')
    if w.get('epub_url'): acts.append(f'<a class="btn small ghost" href="{e(w["epub_url"])}" target="_blank" rel="noopener">EPUB ↗</a>')
    if not w.get('online_reading_url') and not w.get('pdf_url'):
        acts.append(f'<a class="btn small" href="{e(w["source_url"])}" target="_blank" rel="noopener">{"Página oficial ↗" if not w.get("free", True) else "Abrir na fonte ↗"}</a>')
    if w.get('audio_url'): acts.append(f'<a class="btn small ghost" href="{e(w["audio_url"])}" target="_blank" rel="noopener">{ICON_AUDIO} Áudio ↗</a>')
    if w.get('official_url') and w['official_url'] != w['source_url'] and w.get('free', True):
        acts.append(f'<a class="btn small ghost" href="{e(w["official_url"])}" target="_blank" rel="noopener">Editora ↗</a>')
    acts += ['<button type="button" class="mark quero" data-kind="quero" aria-pressed="false">Quero ler</button>',
             '<button type="button" class="mark lendo" data-kind="lendo" aria-pressed="false">Lendo</button>',
             '<button type="button" class="mark lido" data-kind="lido" aria-pressed="false">✓ Lido</button>']
    fmts = [FMT[f] for f in w.get('formats_available', []) if f in FMT]
    meta = ' · '.join(x for x in [w.get('genre'), w.get('historical_period'), w.get('estimated_reading_time'), w.get('source_name')] if x)
    q = norm(' '.join(str(x) for x in [w['title'], w['author'], w.get('genre'), w.get('historical_period'), w.get('source_name'), w.get('category'), GRADUS[g]['nome'], w.get('description_pt_br')] if x))
    more = (f'<details class="more"><summary>Detalhes e direitos</summary><dl>'
            f'<dt>Pré-requisitos</dt><dd>{e(w.get("recommended_prerequisites") or "—")}</dd>'
            f'<dt>Vocabulário · morfologia · sintaxe</dt><dd>{e(w.get("vocabulary_difficulty") or "–")} · {e(w.get("morphology_difficulty") or "–")} · {e(w.get("syntax_difficulty") or "–")} (escala 1–5, estimativa editorial)</dd>'
            f'<dt>Formatos</dt><dd>{e(", ".join(fmts) or "—")}</dd>'
            f'<dt>Fonte</dt><dd><a href="{e(w["source_url"])}" target="_blank" rel="noopener">{e(w["source_name"])}</a></dd>'
            f'<dt>Licença</dt><dd>{e(w.get("license") or "—")}{f" · <a href=\"{e(w['license_url'])}\" target=\"_blank\" rel=\"noopener\">declaração</a>" if w.get("license_url") else ""} · {RIGHTS.get(w.get("rights_status"), "")}</dd>'
            f'<dt>Verificado em</dt><dd>{e(w.get("last_verified") or "—")}</dd>'
            f'</dl></details>')
    return (f'<article class="obra c{g}" id="{e(w["id"])}" data-i="{w["i"]}" data-etapa="{g}" data-categoria="{e(w["category"])}" data-tipo="{e(w.get("original_or_adapted") or "")}" '
            f'data-periodo="{e(w["historical_period"])}" data-genero="{e(w["genre"])}" data-dif="{d or ""}" data-formatos="{e(" ".join(w.get("formats_available", [])))}" '
            f'data-fonte="{e(w["source_name"])}" data-audio="{int(bool(w.get("audio_available")))}" data-gratis="{int(bool(w.get("free", True)))}" '
            f'data-t="{e(w["title"])}" data-a="{e(w["author"] or "")}" data-q="{e(q)}">'
            f'<div class="top">{"".join(tags)}</div><h3>{e(w["title"])}</h3><p class="autor">{e(autor_line(w))}</p>'
            f'<p class="desc">{e(w["description_pt_br"])}</p><p class="meta">{e(meta)}</p>{more if not compact else ""}<div class="acts">{"".join(acts)}</div></article>')

def gradus_cards(link=True):
    out = []
    for g, d in GRADUS.items():
        n = len(d['obras']); a = sum(bool(w.get('audio_available')) for w in d['obras'])
        inner = (f'<span class="num">ETAPA {ROMAN[g]}</span><h3>{e(d["nome"])}</h3><span class="sub">{e(d["pt"])}</span>'
                 f'<p>{e(d["curta"])}</p><div class="count">{n} recursos{f" · {a} com áudio" if a else ""}</div>')
        out.append(f'<a class="gradus c{g}" href="catalogo.html?etapa={g}">{inner}</a>' if link else f'<div class="gradus c{g}">{inner}</div>')
    return '<div class="gradus-grid">' + ''.join(out) + '</div>'

# ───────────────────────── páginas ─────────────────────────
N = len(W); NA = sum(bool(w.get('audio_available')) for w in W); NF = sum(bool(w.get('free', True)) for w in W)
NL = sum(w['category'] == 'Leitura' for w in W); NSRC = len({w['source_name'] for w in W})

def first_reading(stage, maxdif=None):
    for w in GRADUS[stage]['obras']:
        if w['category'] == 'Leitura' and w.get('free', True) and (maxdif is None or (w.get('difficulty') or 9) <= maxdif): return w
    return None

def wlink(w, target=True):
    t = ' target="_blank" rel="noopener"' if target else ''
    return f'<a href="{e(main_link(w))}"{t}><i>{e(w["title"])}</i></a>' + (f' ({e(w["author"])})' if w['author'] else '')

def p_index():
    ld = json.dumps({'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Bibliotheca Latina', 'url': SITE, 'inLanguage': 'pt-BR',
                     'description': 'Biblioteca digital gratuita e curada para estudantes de latim: um percurso em sete etapas, das primeiras palavras às fontes clássicas, cristãs e medievais.'}, ensure_ascii=False)
    first = first_reading(1) or first_reading(2)
    body = f'''<section class="hero"><div class="wrap">
<p class="kicker">Salvete! Uma biblioteca para quem aprende latim</p>
<h1>Bibliotheca <i>Latina</i></h1>
<p class="motto">Ab initiis ad fontes — das primeiras palavras às fontes.</p>
<p class="lead">{N} recursos gratuitos ou de referência, verificados um a um e organizados em sete etapas de leitura: do latim elementar aos autores romanos, aos Padres da Igreja e à escolástica medieval. Sem cadastro, sem anúncios.</p>
<ul class="stats"><li><b>{N}</b>recursos</li><li><b>{NL}</b>leituras</li><li><b>{NA}</b>com áudio</li><li><b>{NSRC}</b>acervos de origem</li></ul>
<div class="cta"><a class="btn accent" href="catalogo.html">Explorar o catálogo</a><a class="btn ghost" href="percurso.html#onde-comecar">Não sei por onde começar</a></div>
</div></section>
<section class="wrap"><div class="callout"><div><p class="kicker">Nunca estudou latim?</p><h2>Aprenda Latim: <i>Elementa Linguae Latinae</i></h2><p>Um livro digital gratuito, em português, que ensina a gramática na ordem em que ela aparece nos textos: lições curtas, exemplos em latim, tabelas, exercícios com resposta e leituras do catálogo ao fim de cada capítulo.</p></div><div><a class="btn accent" href="aprenda/">Começar pelo capítulo 1</a></div></div></section>
<section class="wrap"><h2>O percurso, em sete etapas</h2>
<p>As etapas são caminhos de leitura sugeridos, não uma escada rígida de dificuldade. As etapas I a V seguem uma ordem natural; as etapas VI (latim cristão) e VII (latim medieval) podem começar bem antes: cada recurso traz sua própria classificação de dificuldade.</p>
{gradus_cards()}
</section>
<section class="wrap"><h2>Como funciona</h2>
<ol class="steps">
<li><b>Descubra seu ponto de partida.</b><br>Se nunca estudou latim, comece pelo <a href="aprenda/">curso Aprenda Latim</a>. Se já estudou, o <a href="percurso.html#onde-comecar">teste de cinco minutos</a> indica em qual etapa começar.{f' Se está começando do zero, a primeira leitura é {wlink(first)}.' if first else ''}</li>
<li><b>Escolha uma leitura.</b><br>Filtre o catálogo por etapa, período, gênero, dificuldade, áudio ou formato.</li>
<li><b>Leia na fonte original.</b><br>Cada recurso leva à página oficial do acervo que o publica. Não guardamos cópias; explicamos <a href="sobre.html#direitos">por quê</a>.</li>
<li><b>Marque seu progresso.</b><br>"Quero ler", "Lendo" e "Lido" ficam salvos no seu navegador. Para um registro permanente, use a planilha.</li>
</ol></section>
<section class="wrap"><h2>Para baixar</h2>
<div class="downloads">
<div class="dl"><h3>Guia de leitura (PDF)</h3><p>As sete etapas explicadas, uma metodologia prática de leitura, as leituras recomendadas de cada etapa e dicas para quem fala português.</p><a class="btn accent" href="downloads/{PDF_NAME}" download>{ICON_DL} Baixar o guia</a> <a class="btn ghost" href="percurso.html">Ler online</a></div>
<div class="dl"><h3>Diário de leitura (planilha)</h3><p>Todo o catálogo com links, status de leitura, datas, painel de progresso e caderno de vocabulário. Funciona no Excel, no LibreOffice e no Google Planilhas.</p><a class="btn accent" href="downloads/{XLSX_NAME}" download>{ICON_DL} Baixar a planilha</a> <a class="btn ghost" href="guia.html#planilha">Como usar</a></div>
</div>
<p class="note">Os textos não ficam guardados aqui: os links levam aos acervos que os publicam (Perseus, Dickinson College Commentaries, Project Gutenberg, Wikisource, Internet Archive, Open Book Publishers e outros). Só indicamos materiais comerciais como referência, com link para a editora. <a href="sobre.html#direitos">Política de direitos.</a></p>
</section>'''
    return page('index.html', 'Bibliotheca Latina — leituras em latim, das primeiras palavras às fontes',
                f'Biblioteca digital gratuita para estudantes de latim: {N} recursos verificados, organizados em sete etapas, do latim elementar a Cícero, Virgílio, Agostinho, Jerônimo e Tomás de Aquino. Com guia de leitura em PDF e planilha.',
                body, f'<script type="application/ld+json">{ld}</script>\n')

def p_catalogo():
    fontes = sorted({w['source_name'] for w in W})
    generos = sorted({w['genre'] for w in W}, key=norm)
    periodos = [p for p in PERIODOS if any(w['historical_period'] == p for w in W)]
    formatos = [f for f in FMT if any(f in w.get('formats_available', []) for w in W)]
    chips_g = ''.join(f'<button type="button" class="chip-btn c{g}" data-group="etapa" data-value="{g}" aria-pressed="false">{ROMAN[g]} · {e(d["nome"])}<small>{len(d["obras"])}</small></button>' for g, d in GRADUS.items())
    chips_c = ''.join(f'<button type="button" class="chip-btn" data-group="categoria" data-value="{e(c)}" aria-pressed="false">{e(c)}</button>' for c in CATEGORIAS if any(w['category'] == c for w in W))
    chips_t = ''.join(f'<button type="button" class="chip-btn" data-group="tipo" data-value="{k}" aria-pressed="false">{v}</button>' for k, v in TIPO.items() if any(w.get('original_or_adapted') == k for w in W))
    body = f'''<div class="wrap"><h1>Catálogo</h1>
<p>{N} recursos em ordem sugerida de leitura. Combine os filtros à vontade; o endereço da página guarda a busca para você compartilhar. Dificuldade, pré-requisitos e tempo de leitura são estimativas editoriais (<a href="sobre.html#metodo">como classificamos</a>).</p></div>
<div class="filters"><div class="wrap">
<div class="row">
<label class="sr" for="q">Buscar</label>
<input id="q" type="search" placeholder="Buscar título ou autor (ex.: Caesar, Vulgata, Ørberg, Aquino)" autocomplete="off">
<select id="ordem" aria-label="Ordenar"><option value="sugerida">Ordem sugerida</option><option value="facil">Mais fáceis primeiro</option><option value="dificil">Mais difíceis primeiro</option><option value="titulo">Título (A–Z)</option><option value="autor">Autor (A–Z)</option></select>
</div>
<div class="row"><span class="lbl">Etapa</span>{chips_g}</div>
<div class="row"><span class="lbl">Tipo</span>{chips_c}{chips_t}</div>
<div class="row"><span class="lbl">Filtros</span>
<select id="periodo" aria-label="Período histórico"><option value="">Todos os períodos</option>{"".join(f'<option>{e(p)}</option>' for p in periodos)}</select>
<select id="genero" aria-label="Gênero"><option value="">Todos os gêneros</option>{"".join(f'<option>{e(g)}</option>' for g in generos)}</select>
<select id="dificuldade" aria-label="Dificuldade"><option value="">Qualquer dificuldade</option>{"".join(f'<option value="{k}">{k} · {v}</option>' for k, v in DIF.items())}</select>
<select id="formato" aria-label="Formato"><option value="">Qualquer formato</option>{"".join(f'<option value="{f}">{FMT[f]}</option>' for f in formatos)}</select>
<select id="fonte" aria-label="Fonte"><option value="">Todas as fontes</option>{"".join(f'<option>{e(f)}</option>' for f in fontes)}</select>
<select id="lista" aria-label="Minha lista"><option value="">Minha lista: tudo</option><option value="quero">Quero ler</option><option value="lendo">Lendo</option><option value="lido">Lidos</option><option value="nao-lido">Ainda não lidos</option></select>
<label class="inline"><input id="f-audio" type="checkbox"> Com áudio</label>
<label class="inline"><input id="f-gratis" type="checkbox"> Só gratuitos</label>
</div>
</div></div>
<div class="wrap">
<div class="toolbar"><span id="count" aria-live="polite">{N} recursos</span><div class="acts"><button type="button" class="btn small ghost" id="sorteio">Sortear uma leitura</button><button type="button" class="btn small ghost" id="limpar">Limpar filtros</button></div></div>
<div class="grid" id="grid">{"".join(card(w) for w in W)}</div>
<p id="empty" hidden>Nenhum recurso com esses filtros. Tente ampliar a busca.</p>
<p class="legend" style="margin-top:1.5rem">Todos os links abrem a página oficial de cada fonte. Os recursos marcados "Comercial" são referências a livros à venda; o link leva à editora.</p>
</div>'''
    return page('catalogo.html', 'Catálogo de leituras em latim',
                f'{N} recursos para estudar latim, com filtros por etapa, período histórico, gênero, dificuldade, áudio e formato: leitores graduados, gramáticas, César, Cícero, Virgílio, Vulgata, Agostinho, Tomás de Aquino.', body)

def level_test():
    picks = [(1, 1), (2, 2), (3, 3), (4, 3)]
    items = []
    for stage, maxd in picks:
        w = first_reading(stage, maxd) or first_reading(stage)
        if w: items.append((stage, w))
    if not items: return ''
    li = ''
    for k, (stage, w) in enumerate(items):
        prev = ROMAN[max(1, stage - 1)]; cur = ROMAN[stage]
        hint = (f'Se foi difícil, comece pela <b>Etapa {prev}</b>, com um método; se foi tranquilo, pela <b>Etapa {cur}</b>.' if stage > 1 else
                f'Se foi difícil, comece pela <b>Etapa {cur}</b>.')
        li += f'<li>{wlink(w)} (etapa {cur}). {hint}</li>'
    return f'''<ol>{li}</ol>
<p>Se os quatro foram tranquilos, vá direto à <b>Etapa V</b> (ou às etapas VI e VII, conforme seu interesse). Na dúvida, comece uma etapa abaixo: ler fácil demais custa pouco; ler difícil demais faz desistir.</p>'''

def plan_body(pdf=False):
    base = SITE if pdf else ''
    def link(w):
        return f'<a href="{e(main_link(w))}">{e(w["title"])}</a>' if not pdf else f'{e(w["title"])}'
    def table(ws):
        rows = ''.join(f'<tr><td>{link(w)}{"<br><small>" + e(w["source_url"]) + "</small>" if pdf else ""}</td><td>{e(w["author"] or "")}</td>'
                       f'<td>{e(w.get("difficulty") or "–")} · {e(DIF.get(w.get("difficulty"), ""))}</td><td>{e(TIPO.get(w.get("original_or_adapted"), ""))}</td>'
                       f'<td>{"sim" if w.get("audio_available") else "—"}</td><td>{e(w["source_name"])}</td></tr>' for w in ws)
        return f'<div class="table-scroll"><table><thead><tr><th>Recurso</th><th>Autor</th><th>Dificuldade</th><th>Tipo</th><th>Áudio</th><th>Onde</th></tr></thead><tbody>{rows}</tbody></table></div>'
    secs = ''
    for g, d in GRADUS.items():
        ws = d['obras']
        more = '' if pdf else f'<p><a href="catalogo.html?etapa={g}">Ver os {len(ws)} recursos desta etapa no catálogo →</a></p>'
        secs += f'''<section class="gradus-sec c{g}" id="etapa-{g}">
<div class="gradus-head"><h2>Etapa {ROMAN[g]} · <i>{e(d["nome"])}</i></h2><span class="lvl">{e(d["pt"])}</span></div>
<p>{e(d["curta"])}</p>
<div class="two">
<div class="box"><b>Para quem</b><br>{e(d["perfil"])}<br><br><b>Objetivo</b><br>{e(d["objetivo"])}</div>
<div class="box"><b>Como ler</b><br>{e(d["como"])}<br><br><b>Meta</b><br>{e(d["meta"])}</div>
</div>
<h3>Recursos desta etapa</h3>{table(ws) if ws else '<p>Nenhum recurso verificado ainda nesta etapa.</p>'}
<p class="note"><b>Sinal para avançar:</b> {e(d["avancar"])}</p>{more}
</section>'''
    scale = ''.join(f'<div><b>{k} · {v}</b>{e(DIF_DESC[k])}</div>' for k, v in DIF.items())
    return f'''
<p class="lead">Um caminho prático para ir das primeiras frases em latim até Cícero, Agostinho e Tomás de Aquino, usando só recursos gratuitos e verificados (e, como referência, o método Ørberg). Com 20 a 30 minutos por dia, as etapas I a III levam cerca de um ano.</p>

<h2 id="onde-comecar">Onde começar?</h2>
<p>Faça este teste de cinco minutos. Abra cada texto abaixo, em ordem, leia o primeiro parágrafo (ou as dez primeiras linhas) e pare no primeiro em que precisar do dicionário mais de uma vez por frase.</p>
{level_test()}

<h2 id="metodo">O método: cinco hábitos</h2>
<div class="two">
<div class="box"><b>1. Leia muito, leia fácil, leia em ordem</b><br>Quase todo o seu tempo deve ir para textos que você entende quase inteiros. O latim se aprende pela quantidade de latim compreendido, não pela quantidade de tabelas decoradas. <b>Regra prática:</b> mais de cinco a oito palavras desconhecidas por página que atrapalham o sentido, e o texto está difícil demais: volte uma etapa, sem culpa.</div>
<div class="box"><b>2. Leia em voz alta</b><br>O latim foi feito para ser ouvido. Leia cada trecho em voz alta antes de analisar. Escolha uma pronúncia (<i>restaurada</i>, a reconstrução do latim clássico, ou <i>eclesiástica</i>, a da Igreja, muito próxima do italiano) e seja consistente. Os áudios do LibriVox ajudam a calibrar o ouvido; os leitores indicam qual pronúncia usam.</div>
<div class="box"><b>3. Entenda na ordem latina</b><br>Não "cace o verbo" nem reordene a frase para o português. Leia da primeira palavra à última, segurando as expectativas: um nominativo pede um verbo; um <i>cum</i> pede um subjuntivo; um <i>ut</i> abre uma finalidade ou consequência. As edições comentadas ensinam isso frase a frase.</div>
<div class="box"><b>4. Colete construções, não só palavras</b><br>No máximo cinco anotações por sessão, sempre com a frase inteira em que apareceram. Anote construções (ablativo absoluto, oração infinitiva, <i>cum</i> histórico) com a mesma atenção que dá ao vocabulário. Revise após 1, 3 e 7 dias; a planilha calcula as datas.</div>
<div class="box"><b>5. Escreva o <i>summarium</i></b><br>Ao terminar, escreva duas ou três frases em latim, simples, sobre o que leu: <b>Quis?</b> (quem) · <b>Quid facit?</b> (o que faz) · <b>Quomodo finitur?</b> (como termina). Exemplo: <i>Caesar in Galliam venit. Cum Helvetiis pugnat et eos vincit. Galli timent.</i> Errar faz parte; o objetivo é produzir, não ser perfeito.</div>
</div>

<h3>Uma semana típica (30 minutos por dia)</h3>
<div class="table-scroll keep"><table><thead><tr><th>Dia</th><th>O que fazer</th></tr></thead><tbody>
<tr><td>Segunda a sexta</td><td>20 min de leitura nova em voz alta + 10 min de releitura do trecho anterior ou de revisão das anotações</td></tr>
<tr><td>Sábado</td><td>Escrever os <i>summaria</i> da semana e revisar as construções anotadas</td></tr>
<tr><td>Domingo</td><td>Livre: ouvir um áudio de algo já lido, ou folhear a gramática procurando o que apareceu na semana</td></tr>
</tbody></table></div>

<h3>Como classificamos a dificuldade</h3>
<p>Cada recurso recebe uma nota de 1 a 5, independente da etapa, considerando frequência do vocabulário, complexidade morfológica e sintática, estilo, extensão, existência de notas e conhecimento gramatical exigido. É uma estimativa editorial, não uma medida científica, e não usamos os níveis do Quadro Europeu (A1–C2), que foram pensados para línguas faladas.</p>
<div class="scale">{scale}</div>

<h2 id="etapas">As sete etapas</h2>
<p>As etapas I a V formam uma sequência natural. As etapas VI e VII são caminhos paralelos: o latim cristão e o medieval não são "mais difíceis" que o clássico, e podem começar a partir da etapa III, conforme o seu interesse. Dentro de cada etapa, os recursos estão em ordem sugerida.</p>
{secs}

<h2 id="dicas">Dicas para quem fala português</h2>
<div class="two">
<div class="box"><b>Vantagem</b><br>Cerca de 90% do vocabulário latino tem parente direto em português. <i>Aqua, terra, pater, mater, amicus, bonus, magnus, dicere, facere, venire</i>: o sentido quase sempre se adivinha. A dificuldade está na morfologia (os casos) e na ordem das palavras, não no léxico.</div>
<div class="box"><b>Falsos amigos frequentes</b><br><i>Villa</i> = casa de campo (não vila); <i>officium</i> = dever (não ofício); <i>virtus</i> = coragem, valor (não só virtude); <i>familia</i> = conjunto dos escravos e da casa (não a família nuclear); <i>liber</i> = livro, mas também "livre"; <i>sinister</i> = esquerdo; <i>hostis</i> = inimigo (não hóspede: isso é <i>hospes</i>); <i>cadere</i> = cair (<i>caedere</i> = cortar, matar).</div>
<div class="box"><b>Os casos, em português</b><br>Pense nos casos como funções que o português marca com preposições e posição: nominativo = sujeito; acusativo = objeto direto (e "para" com movimento); genitivo = "de"; dativo = "a/para" alguém; ablativo = "com, por, em, de" (meio, lugar, origem). O vocativo é o chamamento. Em português ainda temos resquícios: <i>eu/me/mim</i>.</div>
<div class="box"><b>Pronúncia</b><br>Na <b>restaurada</b>: <i>c</i> sempre /k/ (<i>Cicero</i> = "Kíkero"), <i>v</i> = /w/, <i>ae</i> = "ai", vogais longas realmente longas. Na <b>eclesiástica</b>: <i>c</i> antes de <i>e/i</i> = "tch", <i>v</i> = /v/, <i>ae</i> = "é", <i>gn</i> = "nh". As duas são legítimas; a eclesiástica soa natural para brasileiros, a restaurada é padrão nas universidades. Para a liturgia e a Vulgata, a eclesiástica; para Virgílio, a restaurada.</div>
</div>
<p><b>Macrons</b> (<i>ā, ē, ī, ō, ū</i>) marcam vogais longas e ajudam a distinguir formas (<i>puella</i> nominativo, <i>puellā</i> ablativo). Os métodos e leitores modernos costumam usá-los; os textos antigos em edição corrente, não. Aprenda com eles e acostume-se a lê-los sem.</p>
'''

def p_percurso():
    body = f'''<div class="wrap narrow prose">
<h1>Percurso de leitura</h1>
<p><a class="btn accent" href="downloads/{PDF_NAME}" download>{ICON_DL} Baixar o guia em PDF</a> <a class="btn ghost" href="downloads/{XLSX_NAME}" download>{ICON_DL} Planilha de acompanhamento</a></p>
{plan_body(False)}
</div>'''
    return page('percurso.html', 'Percurso de leitura em latim, em sete etapas',
                'Guia gratuito para aprender latim lendo: método, sete etapas (Prima Verba, Primae Fabulae, Fundamenta, Ad Fontes, Auctores Romani, Latinitas Christiana, Sapientia Mediaevalis), recursos recomendados e dicas para quem fala português.', body)

def p_recursos():
    def sec(title, cat, intro):
        ws = [w for w in W if w['category'] == cat]
        if not ws: return ''
        return f'<h2 id="{norm(cat).replace(" ", "-")}">{title}</h2><p>{intro}</p><div class="resource-list">{"".join(card(w, compact=True) for w in ws)}</div>'
    body = f'''<div class="wrap prose">
<h1>Recursos de estudo</h1>
<p class="lead">Métodos, gramáticas, dicionários e ferramentas para acompanhar as leituras. Tudo o que está aqui também aparece no <a href="catalogo.html">catálogo</a>; esta página só organiza por tipo.</p>
{sec('Métodos e cursos', 'Método e curso', 'Livros que ensinam a língua do zero, capítulo a capítulo. Um método é o eixo das etapas I a III; os leitores graduados complementam.')}
{sec('Gramáticas e obras de referência', 'Gramática e referência', 'Para consultar, não para decorar: abra a gramática quando uma construção aparecer na leitura. As gramáticas históricas em inglês continuam excelentes e são de domínio público.')}
{sec('Ferramentas', 'Ferramenta', 'Dicionários e analisadores morfológicos online. Use-os para confirmar uma forma, não para traduzir palavra por palavra.')}
{sec('Referências comerciais', 'Referência comercial', 'Materiais à venda que recomendamos como referência. Não reproduzimos seu conteúdo; o link leva à página oficial da editora.')}
<h2 id="pronuncia">Pronúncia e áudio</h2>
<p>Há duas pronúncias correntes: a <b>restaurada</b> (reconstrução do latim clássico, padrão nas universidades) e a <b>eclesiástica</b> (a da Igreja, próxima do italiano). As gravações do LibriVox, em domínio público, usam uma ou outra conforme o leitor; indicamos quando a página do projeto informa. Leia em voz alta desde o primeiro dia.</p>
<h2 id="dicionarios">Como consultar um dicionário latino</h2>
<ul>
<li>Os substantivos são listados pelo <b>nominativo singular</b> seguido do <b>genitivo</b> (<i>rex, regis</i>): o genitivo revela a declinação e o radical.</li>
<li>Os verbos são listados pela <b>1ª pessoa do presente</b>, seguida do infinitivo, do perfeito e do supino (<i>amo, amare, amavi, amatum</i>).</li>
<li>Para uma forma que você não reconhece (<i>tulerunt</i>, <i>latus</i>), use um analisador morfológico (Whitaker's Words, Perseus) e depois confirme no dicionário.</li>
<li>O <b>Lewis &amp; Short</b> (1879) continua sendo o grande dicionário latino-inglês de domínio público; o <b>Logeion</b> reúne vários dicionários numa só busca.</li>
</ul>
</div>'''
    return page('recursos.html', 'Recursos de estudo: métodos, gramáticas e ferramentas',
                'Métodos, gramáticas, dicionários e ferramentas gratuitas para estudar latim, com orientações sobre pronúncia e uso do dicionário.', body)

def p_guia():
    body = f'''<div class="wrap narrow prose">
<h1>Como usar</h1>
<p class="lead">Você não precisa de conta, cadastro nem de saber o que é GitHub. Tudo funciona no navegador, inclusive no celular.</p>

<h2>Em três minutos</h2>
<ol>
<li>Nunca estudou latim? Comece pelo livro <a href="aprenda/">Aprenda Latim</a>: capítulos curtos, com exercícios e leituras indicadas. Já estudou? Descubra seu ponto de partida com o <a href="percurso.html#onde-comecar">teste rápido do percurso</a>.</li>
<li>Abra o <a href="catalogo.html">catálogo</a> e clique na sua etapa.</li>
<li>Escolha um recurso e clique em <b>Ler na fonte</b> (ou <b>PDF</b> / <b>EPUB</b>, quando houver).</li>
<li>Ao começar, marque <b>Lendo</b>; ao terminar, <b>✓ Lido</b>. O site lembra para você.</li>
</ol>

<h2>O livro Aprenda Latim</h2>
<ul>
<li><b>Quatro partes</b> (Fundamenta, Grammatica, Lectio, Auctores) e capítulos numerados. São 54 capítulos, todos disponíveis.</li>
<li><b>Cada capítulo</b> tem objetivos, explicação, exemplos em latim, tabelas, diagramas, exercícios com resposta escondida (clique em "Ver resposta") e leituras do catálogo.</li>
<li><b>Marcar capítulo como concluído</b> salva a marcação neste navegador; o índice do livro mostra o avanço.</li>
</ul>

<h2>O catálogo</h2>
<ul>
<li><b>Etapas (I a VII):</b> caminhos de leitura sugeridos. Dá para marcar várias ao mesmo tempo.</li>
<li><b>Tipo:</b> leitura, método, gramática, ferramenta ou referência comercial; e se o texto é original, adaptado, simplificado ou didático (escrito para estudantes).</li>
<li><b>Período, gênero, dificuldade, formato e fonte:</b> menus para refinar. A dificuldade vai de 1 (elementar) a 5 (superior) e é independente da etapa.</li>
<li><b>Com áudio:</b> recursos com gravação gratuita (quase sempre no LibriVox).</li>
<li><b>Só gratuitos:</b> esconde as referências comerciais (os livros do método Ørberg).</li>
<li><b>Sortear uma leitura:</b> escolhe um recurso ao acaso entre os filtrados que você ainda não leu.</li>
<li><b>Minha lista:</b> "Quero ler", "Lendo" e "Lido" ficam salvos <i>neste navegador</i>. Se limpar os dados do navegador ou trocar de aparelho, a lista some. Para um registro permanente, use a planilha.</li>
<li><b>Detalhes e direitos:</b> cada cartão tem um painel com pré-requisitos, formatos, licença e data da última verificação.</li>
<li><b>Compartilhar uma busca:</b> o endereço da página muda com os filtros. Copie e envie (ex.: <a href="catalogo.html?etapa=2&amp;audio=1">etapa II com áudio</a>).</li>
</ul>

<h2>Lendo em cada fonte</h2>
<ul>
<li><b>Dickinson College Commentaries:</b> texto latino com notas e vocabulário na mesma tela. Leia online; há também versões para imprimir.</li>
<li><b>Open Book Publishers:</b> comentários acadêmicos com texto, notas e tradução. Leia online ou baixe o PDF gratuito na página do livro.</li>
<li><b>Project Gutenberg:</b> prefira o formato <b>EPUB</b>, que abre no Apple Books, no Google Play Livros ou em leitores como o Kobo. Para o Kindle, use a opção "Kindle" da página.</li>
<li><b>Internet Archive:</b> livros antigos digitalizados. O botão "PDF" baixa o fac-símile; o leitor online permite folhear.</li>
<li><b>Wikisource:</b> leia online ou baixe EPUB/PDF pelo menu de download da página.</li>
<li><b>Perseus e Corpus Corporum:</b> textos para ler na tela; no Perseus, clicar numa palavra abre sua análise morfológica.</li>
<li><b>LibriVox:</b> áudios gratuitos; baixe os MP3 ou ouça no site.</li>
</ul>

<h2 id="planilha">A planilha de acompanhamento</h2>
<p><a class="btn accent" href="downloads/{XLSX_NAME}" download>{ICON_DL} Baixar a planilha</a></p>
<p>Abre no Excel, no LibreOffice ou no <b>Google Planilhas</b> (em <i>Arquivo → Importar → Fazer upload</i>; ou envie para o Google Drive e abra com o Planilhas). Tem seis abas:</p>
<ul>
<li><b>Comece aqui:</b> instruções curtas.</li>
<li><b>Painel:</b> seu progresso por etapa, sessões registradas, palavras anotadas. Calcula sozinho.</li>
<li><b>Catálogo:</b> os {N} recursos com link. Escolha o <b>Status</b> (Quero ler, Lendo, Lido, Abandonei) e preencha datas e nota.</li>
<li><b>Sessões:</b> anote cada sessão de leitura (data, recurso, minutos, trecho). Serve para ver sua constância.</li>
<li><b>Vocabulário:</b> palavra ou construção, forma do dicionário, tradução e a frase do texto. As datas de revisão (1, 3 e 7 dias) aparecem sozinhas.</li>
<li><b>Summaria:</b> seus resumos em latim, de duas ou três frases.</li>
</ul>

<h2>Perguntas frequentes</h2>
<details><summary>É gratuito?</summary><p>Sim. O site, o guia e a planilha são gratuitos, e todos os recursos marcados como gratuitos são de acesso livre nas fontes. Os poucos recursos comerciais estão identificados e levam à editora.</p></details>
<details><summary>Por que os textos não ficam aqui?</summary><p>Porque acesso gratuito não é o mesmo que permissão para redistribuir. Preferimos levar você à página oficial de cada acervo, que mantém o texto atualizado e merece a visita. Veja <a href="sobre.html#direitos">a política de direitos</a>.</p></details>
<details><summary>Preciso saber gramática antes de ler?</summary><p>Não toda. Comece pela etapa I com um método: a gramática vem aos poucos, pela leitura. As gramáticas de referência servem para consultar quando uma construção aparece.</p></details>
<details><summary>Qual pronúncia devo usar?</summary><p>Qualquer uma das duas (restaurada ou eclesiástica), desde que seja consistente. Veja <a href="recursos.html#pronuncia">pronúncia e áudio</a>.</p></details>
<details><summary>O latim cristão é mais fácil ou mais difícil?</summary><p>Em geral, a Vulgata e muitos textos medievais têm frases mais curtas e vocabulário mais próximo do português do que Cícero ou Virgílio. Por isso as etapas VI e VII não são "depois" da V: são caminhos paralelos, e cada recurso tem sua própria nota de dificuldade.</p></details>
<details><summary>Posso sugerir um recurso?</summary><p>Sim: abra uma <a href="{REPO}/issues">issue no GitHub</a> com o link da fonte e, se possível, a declaração de licença. Só incluímos o que conseguimos verificar.</p></details>
</div>'''
    return page('guia.html', 'Como usar a biblioteca', 'Como usar a Bibliotheca Latina: encontrar o ponto de partida, filtrar o catálogo, marcar o progresso e usar a planilha de leitura.', body)

SRC_INFO = {
 'Project Gutenberg': ('https://www.gutenberg.org/', 'Domínio público nos EUA + Project Gutenberg License. Para o Brasil, conferimos o ano de morte de autor e editor de cada obra.'),
 'Dickinson College Commentaries': ('https://dcc.dickinson.edu/', 'CC BY-SA (3.0 ou 4.0, conforme a página); comentários, vocabulários e áudios incluídos.'),
 'Vicifons (Latin Wikisource)': ('https://la.wikisource.org/', 'Textos antigos em domínio público; transcrições sob CC BY-SA 4.0.'),
 'Perseus Digital Library': ('https://www.perseus.tufts.edu/', 'CC BY-SA 3.0 US no rodapé de cada texto; Vulgata e Lewis & Short sem declaração (não verificado).'),
 'Internet Archive': ('https://archive.org/', 'Fac-símiles de livros antigos; direitos conferidos item a item pelo ano de publicação e de morte dos autores.'),
 'Corpus Corporum': ('https://mlat.uzh.ch/', 'Textos da Patrologia Latina (domínio público); o site pede uso não comercial para as suas transcrições.'),
 'Hackett Publishing': ('https://hackettpublishing.com/', 'Obras comerciais (método Ørberg).'),
 'Open Book Publishers': ('https://www.openbookpublishers.com/', 'Livros de acesso aberto; licença CC indicada em cada volume (BY 4.0; os mais antigos BY-NC ou BY-NC-ND).'),
 'Repositório UFES (EDUFES)': ('https://repositorio.ufes.br/', 'CC BY-NC-ND 4.0.'),
 'Corpus Thomisticum': ('https://www.corpusthomisticum.org/', 'Edição eletrônica com direitos reservados pela Fundación Tomás de Aquino; leitura gratuita.'),
 "Whitaker's Words": ('https://latin-words.com/', 'Licença livre do autor (programa); uso gratuito.'),
 'Logeion': ('https://logeion.uchicago.edu/', 'Serviço gratuito da Universidade de Chicago; dicionários com licenças próprias.'),
 'Latinitium': ('https://latinitium.com/', 'Conteúdo gratuito para leitura; sem licença de reúso.'),
 'The Latin Library': ('https://www.thelatinlibrary.com/', 'Sem licença explícita (não verificado).'),
 'Vicipaedia': ('https://la.wikipedia.org/', 'CC BY-SA 4.0.'),
}

def p_sobre():
    srcs = {}
    for w in W:
        s = srcs.setdefault(w['source_name'], dict(n=0, lic=set(), url=w.get('source_home') or w['source_url'], host=False))
        s['n'] += 1; s['lic'].add(w.get('license') or '—'); s['host'] = s['host'] or bool(w.get('hosting_allowed'))
    rows = ''.join(f'<tr><td><a href="{e(SRC_INFO.get(n, (s["url"],))[0])}" target="_blank" rel="noopener">{e(n)}</a><br><small>{s["n"]} recurso{"s" if s["n"] != 1 else ""}</small></td>'
                   f'<td>{e(SRC_INFO.get(n, (None, "; ".join(sorted(s["lic"]))))[1])}</td><td>{"Link para a página oficial" if not s["host"] else "Link (cópia permitida pela licença, não exercida)"}</td></tr>'
                   for n, s in sorted(srcs.items(), key=lambda x: -x[1]['n']))
    status = {}
    for w in W: status[w.get('rights_status', 'unverified')] = status.get(w.get('rights_status', 'unverified'), 0) + 1
    status_rows = ''.join(f'<tr><td>{RIGHTS[k]}</td><td>{status.get(k, 0)}</td><td>{d}</td></tr>' for k, d in [
        ('public_domain', 'Original e edição em domínio público (autor e editor mortos há mais de 70 anos, ou licença de domínio público declarada).'),
        ('creative_commons', 'Licença Creative Commons declarada na fonte. Conferimos a versão exata (BY, BY-SA, BY-NC, BY-NC-ND).'),
        ('open_access_limited', 'Leitura gratuita, mas sem licença que permita redistribuir.'),
        ('commercial', 'Obra à venda. Só referência, com link para a editora.'),
        ('unverified', 'Não conseguimos localizar uma declaração de direitos. Só link.')])
    cand = ''.join(f'<li><i>{e(c["title"])}</i>{f" ({e(c['author'])})" if c.get("author") else ""}: {e(c["reason"])}</li>' for c in CAND)
    body = f'''<div class="wrap narrow prose">
<h1>Sobre, fontes e direitos</h1>
<p class="lead">A Bibliotheca Latina nasceu de uma constatação: existe uma quantidade enorme de latim gratuito e de qualidade na internet, mas espalhada por dezenas de acervos, sem ordem e sem indicação de por onde começar. Este projeto reúne, verifica e organiza.</p>
<p>É um projeto pessoal, gratuito e sem fins lucrativos, feito por um brasileiro que estuda latim. Não tem anúncios, não coleta dados e não exige cadastro. Não é afiliado a nenhuma das fontes. É irmão da <a href="https://oaleffemanuel.github.io/biblioteca-italiana/">Biblioteca Italiana</a>, de quem herda a arquitetura e a política de direitos.</p>

<h2>As fontes</h2>
<div class="table-scroll"><table><thead><tr><th>Fonte</th><th>Licenças encontradas</th><th>Como aparece aqui</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Todo o mérito das obras é de seus autores, editores e dos acervos que as publicam. Se você gosta de uma fonte, visite-a e, se puder, apoie-a diretamente.</p>

<h2 id="direitos">Política de direitos autorais</h2>
<ul>
<li><b>Acesso gratuito não é permissão.</b> Um PDF que se baixa de graça continua protegido se a fonte não der uma licença explícita. Por isso o catálogo é formado por <b>links</b> para as páginas oficiais.</li>
<li><b>Autor antigo em domínio público não cobre a edição moderna.</b> Cícero é de todos; a edição crítica, o comentário, o vocabulário, a tradução e a gravação têm direitos próprios. Avaliamos cada versão específica no endereço indicado.</li>
<li><b>Dois regimes de prazo.</b> No Brasil, uma obra entra em domínio público 70 anos após a morte do autor (contados de 1º de janeiro do ano seguinte). Nos Estados Unidos, onde estão Project Gutenberg, Internet Archive e Perseus, valem regras próprias (em geral, publicação antes de 1931). Quando os dois regimes divergem, indicamos e preferimos o link.</li>
<li><b>Nesta versão, não hospedamos nenhum texto.</b> Mesmo onde a licença permitiria (CC BY, CC BY-SA, domínio público), optamos por link: a fonte mantém o texto atualizado e corrigido. O campo <code>hosting_allowed</code> do catálogo registra, porém, a avaliação, para uso futuro.</li>
<li><b>Materiais comerciais só como referência.</b> Os livros do método <i>Lingua Latina per se Illustrata</i> (Hackett Publishing) aparecem com link para a editora; não reproduzimos nada do seu conteúdo.</li>
<li><b>Na dúvida, link.</b> Recursos sem declaração de direitos localizável ficam marcados como "não verificado", só com link, e nunca seriam copiados.</li>
</ul>
<div class="table-scroll"><table><thead><tr><th>Situação de direitos</th><th>Recursos</th><th>Critério</th></tr></thead><tbody>{status_rows}</tbody></table></div>
<p>O registro completo, recurso a recurso (licença, endereço da declaração, situação, permissão de cópia, data de verificação), está em <a href="dados/auditoria-direitos.csv">dados/auditoria-direitos.csv</a> e no <a href="{REPO}/blob/main/LICENCAS.md">documento de política</a> do repositório.</p>
<p class="note warn">É titular de direitos e quer corrigir ou retirar algo? Abra uma <a href="{REPO}/issues">issue no GitHub</a>. A correção é feita com prioridade.</p>

<h2 id="metodo">Como classificamos</h2>
<ul>
<li><b>Etapa (I–VII):</b> caminho de leitura sugerido, por tipo de texto e momento do estudo. Não é uma escala universal de dificuldade: o latim cristão (VI) e o medieval (VII) são percursos paralelos.</li>
<li><b>Dificuldade (1–5):</b> estimativa editorial que considera vocabulário, morfologia, sintaxe, estilo, extensão, existência de notas e gramática exigida. As três subnotas (vocabulário, morfologia, sintaxe) aparecem em "Detalhes".</li>
<li><b>Original, adaptado, simplificado, didático:</b> dizemos sempre o que o texto é. Um leitor graduado moderno não é um texto antigo, e um resumo de Lhomond não é Tito Lívio.</li>
<li><b>Tempo de leitura:</b> ordem de grandeza ("algumas horas", "semanas"), nunca minutos exatos. Não inventamos métricas que não temos como medir.</li>
<li><b>Sem níveis A1–C2:</b> o Quadro Europeu foi feito para línguas faladas e não se aplica bem a textos latinos antigos.</li>
</ul>

<h2 id="candidatos">Candidatos ainda não incluídos</h2>
<p>Recursos conhecidos que ficaram de fora desta versão, com o motivo. Ajuda para verificá-los é bem-vinda.</p>
<ul>{cand or '<li>Nenhum no momento.</li>'}</ul>

<h2>Licença deste projeto</h2>
<ul>
<li><b>Textos do site, guia de leitura, planilha e dados do catálogo:</b> CC BY 4.0. Pode usar e adaptar, com crédito.</li>
<li><b>Livro <i>Elementa Linguae Latinae</i> (seção Aprenda Latim):</b> texto original deste projeto, CC BY 4.0. Explicações, exemplos e exercícios foram escritos para o livro; não reproduz cursos nem materiais de terceiros. As citações latinas antigas (César, Vulgata) estão em domínio público.</li>
<li><b>Código (HTML, CSS, JS e scripts):</b> MIT.</li>
<li><b>Os recursos listados:</b> seguem a licença de cada fonte, indicada em cada cartão.</li>
</ul>
<h2 id="nota-editorial">Nota editorial sobre o livro</h2>
<p>O <i>Elementa Linguae Latinae</i> foi desenvolvido de forma independente por este projeto. As explicações, os exemplos e os exercícios foram escritos para ele com base nas gramáticas de referência (Bennett, Allen e Greenough, Kennedy, Ravizza), no dicionário de Lewis e Short e em edições em domínio público dos textos antigos. A redação e a verificação editorial foram feitas com auxílio de ferramentas de inteligência artificial, com conferência das formas, regras, citações e edições contra essas fontes. O livro não passou por revisão por pares nem tem certificação acadêmica; correções são bem-vindas pelo botão "Reportar problema" de cada capítulo. O professor Rafael Falcão, a quem o autor agradece no <a href="aprenda/#creditos">índice do livro</a>, não participou da obra, não a revisou e não a endossa.</p>
{apoie_html()}
</div>'''
    return page('sobre.html', 'Sobre o projeto, fontes e direitos autorais', 'Sobre a Bibliotheca Latina: as fontes usadas, a política de direitos autorais, o método de classificação e as licenças do projeto.', body)

# ───────────────────────── Aprenda Latim · Elementa Linguae Latinae ─────────────────────────
SO_PUBLICADAS = '--so-publicadas' in sys.argv
STATUS = ('planejada', 'rascunho', 'revisada', 'publicada')   # situação editorial interna; não é exibida no site
TIPOS_DIREITO = {'original': 'Conteúdo original deste projeto', 'dominio_publico': 'Conteúdo original com trechos de obras em domínio público', 'adaptacao_autorizada': 'Adaptação autorizada de material de terceiros'}
PERMISSOES = json.load(open(os.path.join(ROOT, 'conteudo', 'permissoes.json'), encoding='utf-8'))['fontes']

def validar_licao(l):
    errs = []
    for k in ('slug', 'titulo', 'tempo', 'resumo', 'status', 'objetivos', 'topicos', 'prerequisitos', 'secoes', 'exercicios', 'leituras', 'creditos', 'direitos'):
        if k not in l: errs.append(f'falta o campo {k}')
    if errs: sys.exit(f'Lição {l.get("slug")}: ' + '; '.join(errs))
    if l['status'] not in STATUS: errs.append(f'status inválido: {l["status"]}')
    if not l['creditos'].get('autor'): errs.append('creditos.autor vazio')
    d = l['direitos']
    if d.get('tipo') not in TIPOS_DIREITO: errs.append(f'direitos.tipo inválido: {d.get("tipo")}')
    if d.get('tipo') == 'adaptacao_autorizada':
        if not d.get('adaptacoes'): errs.append('adaptacao_autorizada sem direitos.adaptacoes')
        for a in d.get('adaptacoes', []):
            fonte = next((f for f in PERMISSOES if f['id'] == a.get('fonte')), None)
            if not fonte: errs.append(f'adaptação cita fonte desconhecida em permissoes.json: {a.get("fonte")}')
            elif fonte.get('status_adaptacao') != 'concedida': errs.append(f'adaptação da fonte {a.get("fonte")} sem permissão concedida ({fonte.get("status_adaptacao")})')
    for a in l.get('aulas_complementares', []):
        for k in ('educador', 'titulo', 'url', 'descricao', 'verificado'):
            if not a.get(k): errs.append(f'aula complementar "{a.get("titulo")}" sem o campo {k}; referências incompletas não são publicadas')
        if a.get('url') and not a['url'].startswith('http'): errs.append(f'aula complementar com URL inválida: {a["url"]}')
    for r in l.get('referencias', []):
        if not r.get('titulo'): errs.append('referência sem título')
        if r.get('catalogo'): find(r['catalogo'])
    for i in l['leituras']: find(i)
    for pr in l['prerequisitos'].get('licoes', []):
        if not any(x.get('slug') == pr for pt in LIVRO.PARTES for x in pt['licoes']): errs.append(f'pré-requisito aponta para lição inexistente: {pr}')
    if errs: sys.exit(f'Lição {l["slug"]} inválida:\n  ' + '\n  '.join(errs))

LICOES = []   # lições com módulo, em ordem, com numeração global (inclui rascunhos, salvo --so-publicadas)
_n = 0
for _pt in LIVRO.PARTES:
    for _l in _pt['licoes']:
        _n += 1; _l['numero'] = _n; _l['parte'] = _pt['num']
        if _l.get('modulo'):
            _m = importlib.import_module(f"conteudo.licoes.{_l['modulo']}").LICAO
            _m.update(numero=_n, parte=_pt['num'], parte_nome=_pt['nome'], modulo_nome=_pt['nome']); _m.setdefault('titulo_latim', _l.get('titulo_latim')); _m.setdefault('nivel', _l.get('nivel'))
            if _m.get('status') == 'planejada' or (SO_PUBLICADAS and _m.get('status') != 'publicada'): _l['status'] = _m.get('status'); continue
            _l['slug'] = _m['slug']; _l['status'] = _m['status']; LICOES.append(_m)
for _l in LICOES: validar_licao(_l)
N_LICOES_TOTAL = _n
for _pt in LIVRO.PARTES:
    for _l in _pt['licoes']:
        if _l.get('nivel') not in LIVRO.NIVEIS: sys.exit(f'Capítulo {_l["numero"]}: nível inválido {_l.get("nivel")}')
        if any(x >= _l['numero'] for x in _l.get('pre', [])): sys.exit(f'Capítulo {_l["numero"]}: pré-requisito posterior ao capítulo')
SLUG2LICAO = {l['slug']: l for l in LICOES}

def licao_href(l): return f"{l['slug']}.html"

# A situação editorial (status) e a revisão acadêmica (creditos.revisao_gramatical) são registros internos;
# o site não exibe selos de rascunho/revisão (decisão de 2026-10-16; ver FLUXO-EDITORIAL §8).
DATA_AUDITORIA = '2026-10-15'
# Formulário externo de correções (sem backend próprio). Com url vazia, o leitor gera o relatório no navegador e o copia.
# Google Forms: url = 'https://docs.google.com/forms/d/e/<ID>/viewform'; em campos, o 'entry.NNN' de cada pergunta
# (obtido em "Gerar link pré-preenchido"). Outro serviço que aceite parâmetros na URL também serve.
FEEDBACK = dict(url='', campos=dict(capitulo='', secao='', categoria='', descricao='', sugestao=''))
CATEGORIAS_FEEDBACK = ['Forma latina, quantidade (mácron) ou ortografia', 'Tradução', 'Exercício ou resposta (gabarito)',
                       'Explicação confusa ou incompleta', 'Português: digitação ou redação', 'Referência ou citação',
                       'Exibição, link ou navegação', 'Outro']

def apoie_html():
    pix = ''
    if PIX:
        pix = (f'<div class="pix"><p><b>Doação por PIX</b> ({e(PIX.get("tipo", "chave"))}{", titular " + e(PIX["titular"]) if PIX.get("titular") else ""}):</p>'
               f'<p><code class="pix-chave">{e(PIX["chave"])}</code> <button type="button" class="btn small copiar-pix" data-copiar="{e(PIX["chave"])}">Copiar chave PIX</button></p></div>')
    return f"""<section class="apoie" id="apoie"><h2>Apoie este projeto</h2>
<p>A Bibliotheca Latina é inteiramente gratuita e aberta a todos os estudantes: o catálogo, o guia, a planilha e o livro <i>Elementa Linguae Latinae</i> não têm cadastro, anúncios nem conteúdo pago. O projeto é mantido de forma independente, por uma pessoa, no tempo livre.</p>
<p>Se ele foi útil para você, a melhor ajuda é usá-lo, indicá-lo a outros estudantes e avisar dos erros que encontrar (há um botão "Reportar problema" em cada capítulo). {"Quem quiser, pode também contribuir com uma doação voluntária; nada no site depende dela." if PIX else "Contribuições voluntárias poderão ser recebidas no futuro; por ora, um contato já ajuda."}</p>
{pix}<p>Contato: <a class="btn small ghost" href="mailto:{CONTATO_EMAIL}">{CONTATO_EMAIL}</a></p>
</section>"""

def reportar_html(l):
    secs = [(f's{i}', re.sub(r'<[^>]+>', '', t)) for i, (t, h) in enumerate(l['secoes'], 1)]
    if l.get('erros_comuns'): secs.append(('erros', 'Erros comuns'))
    if l.get('pratica_guiada'): secs.append(('pratica', 'Prática guiada'))
    secs += [('exercicios', 'Exercícios'), ('leituras', 'Leituras recomendadas'), ('creditos', 'Créditos e fontes'), ('geral', 'O capítulo em geral')]
    opts = ''.join(f'<option value="{e(i)}">{e(t)}</option>' for i, t in secs)
    cats = ''.join(f'<option>{e(c)}</option>' for c in CATEGORIAS_FEEDBACK)
    campos = ' '.join(f'data-campo-{k}="{e(v)}"' for k, v in FEEDBACK['campos'].items())
    return f"""<details class="reportar" id="reportar"><summary>Reportar problema</summary>
<form class="form-reportar" data-url="{e(FEEDBACK['url'])}" data-email="{e(CONTATO_EMAIL)}" {campos} data-capitulo="{e(f'Capítulo {l["numero"]}: {l["titulo"]} ({l["slug"]})')}">
<p class="legend">Achou um erro de latim, uma tradução duvidosa ou uma resposta errada? Conte o que viu. O botão abre o seu programa de e-mail com a mensagem pronta para <b>{e(CONTATO_EMAIL)}</b>; nada é enviado sem a sua confirmação.</p>
<label>Seção<select name="secao">{opts}</select></label>
<label>Tipo de problema<select name="categoria">{cats}</select></label>
<label>O que está errado? <small>(cite a frase ou o exercício)</small><textarea name="descricao" rows="4" required></textarea></label>
<label>Sugestão de correção <small>(opcional)</small><textarea name="sugestao" rows="2"></textarea></label>
<button type="submit" class="btn small">{"Abrir formulário de envio" if FEEDBACK['url'] else "Enviar por e-mail"}</button>
<div class="relatorio" hidden><p class="legend">Se o programa de e-mail não abriu (por exemplo, se você usa e-mail só no navegador), copie o texto abaixo e envie para <a href="mailto:{e(CONTATO_EMAIL)}">{e(CONTATO_EMAIL)}</a>.</p><textarea readonly rows="7"></textarea><button type="button" class="btn small copiar">Copiar relatório</button></div>
</form></details>"""

def p_aprenda():
    partes = ''; topicos = {}
    for pt in LIVRO.PARTES:
        li = ''
        for l in pt['licoes']:
            info = (f'<span class="lat">{e(l.get("titulo_latim", ""))}</span>' if l.get('titulo_latim') else '') + \
                   f'<span class="meta-cap">{e(l.get("nivel", ""))}' + (f' · requer {", ".join(str(x) for x in l["pre"])}' if l.get('pre') else '') + '</span>'
            if l.get('slug'):
                li += (f'<li data-licao="{e(l["slug"])}" class="nv-{norm(l.get("nivel", "")).replace("á", "a")}"><span class="n">{l["numero"]}</span><span class="cap"><a href="{licao_href(l)}">{e(l["titulo"])}</a>{info}</span>'
                       f'<span class="feita" hidden>✓ concluída</span></li>')
                for t in SLUG2LICAO[l['slug']].get('topicos', []): topicos.setdefault(t, []).append(l)
            else:
                li += f'<li class="planejada nv-{norm(l.get("nivel", ""))}"><span class="n">{l["numero"]}</span><span class="cap"><span>{e(l["titulo"])} <small>· em preparação</small></span>{info}</span></li>'
        partes += (f'<section class="parte p{pt["num"]}" id="parte-{pt["num"]}"><h2>Parte {ROMAN[pt["num"]]} · <i>{e(pt["nome"])}</i> <span class="lvl">{e(pt["pt"])}</span></h2>'
                   f'<p class="desc">{e(pt["desc"])}</p><ul class="licoes">{li}</ul></section>')
    idx = ''.join(f'<li><b>{e(t)}</b>: ' + ', '.join(f'<a href="{licao_href(l)}">capítulo {l["numero"]}</a>' for l in ls) + '</li>' for t, ls in sorted(topicos.items(), key=lambda x: norm(x[0])))
    primeira = LICOES[0]
    body = f"""<div class="wrap"><div class="livro-head">
<p class="kicker">Aprenda Latim · livro digital gratuito</p>
<h1>{e(LIVRO.TITULO)}</h1>
<p class="sub">{e(LIVRO.SUBTITULO)}</p>
<p class="lead">Um curso em português, do zero à leitura dos autores, em quatro partes e {N_LICOES_TOTAL} capítulos. Cada capítulo traz objetivos, explicações, exemplos em latim, tabelas, diagramas, exercícios com resposta e leituras do catálogo. {"Os " + str(N_LICOES_TOTAL) + " capítulos estão disponíveis, de graça, com progressão gramatical completa, das primeiras frases à leitura guiada de César, Virgílio, Cícero, Lívio, da Vulgata, de Agostinho e de Tomás de Aquino." if len(LICOES) == N_LICOES_TOTAL else f"{len(LICOES)} capítulos já estão disponíveis; os demais estão em preparação."}</p>
<div class="cta"><a class="btn accent" href="{licao_href(primeira)}">Começar pelo capítulo 1</a><a class="btn ghost" href="#como-estudar">Como estudar com o livro</a><a class="btn ghost" href="#topicos">Índice de tópicos</a></div>
<div class="progresso-livro" data-total="{len(LICOES)}"><span class="txt">O progresso fica salvo neste navegador.</span><div class="barra"><div></div></div></div>
</div></div>
<div class="wrap"><p class="legend niveis-legenda"><b>Níveis:</b> <span class="nv nv-essencial">essencial</span> o que todo iniciante precisa · <span class="nv nv-intermediario">intermediário</span> o necessário para ler prosa autêntica com apoio · <span class="nv nv-avancado">avançado</span> sintaxe do período, poesia e escrita. "Requer" indica os capítulos pré-requisitos.</p><div class="partes">{partes}</div>
<h2 id="como-estudar">Como estudar com o livro</h2>
<div class="two">
<div class="box"><b>Uma lição por vez, em voz alta.</b><br>Leia a explicação, repita os exemplos em latim em voz alta e só então faça os exercícios. Confira cada resposta antes de passar à seguinte: a explicação da resposta é parte da lição.</div>
<div class="box"><b>Combine com um método e com leituras.</b><br>O livro explica a gramática; a fluência vem das leituras indicadas ao fim de cada capítulo e, se possível, de um método completo ao lado (<i>Familia Romana</i> ou <i>Latine loqui</i>, em português).</div>
<div class="box"><b>Marque o que concluiu.</b><br>Ao fim de cada capítulo há um botão "Marcar capítulo como concluído". A marcação fica salva só no seu navegador; o índice mostra o seu avanço.</div>
<div class="box"><b>Volte quando precisar.</b><br>As tabelas das lições são para consultar sempre que uma forma aparecer na leitura. Ninguém decora as declinações de uma vez: elas se fixam vendo-as nos textos.</div>
</div>
<h2 id="topicos">Índice de tópicos gramaticais</h2>
<p>Onde cada assunto é tratado no livro.</p>
<ul class="toc topicos-idx">{idx}</ul>
<h2 id="creditos">Créditos e fontes</h2>
<p>O <i>Elementa Linguae Latinae</i> é um texto original deste projeto, escrito em português, sob licença CC BY 4.0. Explicações, exemplos e exercícios foram redigidos para este livro; os fatos gramaticais são os da tradição, conferidos nas gramáticas de referência do <a href="../recursos.html">catálogo</a>. Cada capítulo traz, ao final, seus créditos: autor, fontes consultadas, educadores externos cujas aulas públicas são indicadas como complemento, adaptações autorizadas (quando houver) e leituras. A indicação de uma aula externa é uma referência independente e não implica endosso, colaboração nem autoria por parte do educador citado.</p>
<p><b>Agradecimento.</b> O autor deste livro agradece ao professor Rafael Falcão, cujo curso gratuito de latim despertou e alimentou seu interesse pela língua. O <i>Elementa</i> é uma obra independente: não reproduz nem adapta o conteúdo daquele curso, e esta menção não implica endosso, colaboração ou coautoria do professor.</p>
</div>"""
    return page('aprenda/index.html', 'Aprenda Latim: Elementa Linguae Latinae',
                f'Curso gratuito de latim em português, em quatro partes: fundamentos, gramática, leitura e autores. Lições com explicações, exemplos, tabelas, exercícios com resposta e leituras recomendadas.', body)

def creditos_html(l):
    """Componente reutilizável de atribuição: autor, fontes consultadas, educadores externos, adaptações autorizadas, para ir além."""
    c = l['creditos']; d = l['direitos']; blocos = []
    aut = e(c['autor'])
    if c.get('colaboradores'): aut += ' · colaboração: ' + e(', '.join(c['colaboradores']))
    rev = c.get('revisao_gramatical')
    aut += f' · revisão acadêmica: {e(rev["nome"])} ({e(rev["data"])})' if rev else ''
    blocos.append(('Autoria', f'{aut}. {e(TIPOS_DIREITO[d["tipo"]])}; licença {e(d.get("licenca", "CC BY 4.0"))}.'))
    refs = l.get('referencias', [])
    if refs:
        items = []
        for r in refs:
            t = f'<i>{e(r["titulo"])}</i>' + (f', {e(r["autor"])}' if r.get('autor') else '')
            if r.get('catalogo'): w = find(r['catalogo']); t = f'<a href="{e(main_link(w))}" target="_blank" rel="noopener">{t}</a> (no catálogo)'
            elif r.get('url'): t = f'<a href="{e(r["url"])}" target="_blank" rel="noopener">{t}</a>'
            if r.get('tipo') == 'dominio_publico': t += ' · domínio público'
            if r.get('nota'): t += f' · {e(r["nota"])}'
            items.append(f'<li>{t}</li>')
        blocos.append(('Fontes consultadas', f'<ul>{"".join(items)}</ul>'))
    aulas = l.get('aulas_complementares', [])
    if aulas:
        eds = sorted({a['educador'] for a in aulas})
        blocos.append(('Educadores externos', f'As aulas públicas de {e(", ".join(eds))} são indicadas acima como complemento. São referências independentes: não implicam endosso, colaboração nem autoria do conteúdo desta lição por parte do educador.'))
    if d.get('adaptacoes'):
        items = ''.join(f'<li>{e(a.get("descricao", ""))} · fonte: {e(next(f["titular"] for f in PERMISSOES if f["id"] == a["fonte"]))} · permissão concedida em {e(a.get("data", "—"))}{f" · condições: {e(a['condicoes'])}" if a.get("condicoes") else ""}</li>' for a in d['adaptacoes'])
        blocos.append(('Adaptações autorizadas', f'<ul>{items}</ul>'))
    alem = [f'<a href="{e(main_link(find(i)))}" target="_blank" rel="noopener"><i>{e(find(i)["title"])}</i></a>' for i in l['leituras']]
    if alem: blocos.append(('Para ir além', ', '.join(alem) + ' (ver Leituras recomendadas acima).'))
    return '<section class="creditos" id="creditos"><h2>Créditos e fontes</h2><dl>' + ''.join(f'<dt>{e(t)}</dt><dd>{h}</dd>' for t, h in blocos) + '</dl></section>'

def p_licao(l, k):
    prev = LICOES[k - 1] if k > 0 else None; nxt = LICOES[k + 1] if k + 1 < len(LICOES) else None
    obj = ''.join(f'<li>{o}</li>' for o in l['objetivos'])
    flag = lambda sid: f' <a class="rep-secao" href="#reportar" data-secao="{sid}" title="Reportar problema nesta seção" aria-label="Reportar problema nesta seção">⚑</a>'
    secs = ''.join(f'<h2 id="s{i}">{t}{flag(f"s{i}")}</h2>{h}' for i, (t, h) in enumerate(l['secoes'], 1))
    aulas = l.get('aulas_complementares', [])
    toc = ''.join(f'<li><a href="#s{i}">{e(t)}</a></li>' for i, (t, h) in enumerate(l['secoes'], 1)) + ('<li><a href="#erros">Erros comuns</a></li>' if l.get('erros_comuns') else '') + ('<li><a href="#pratica">Prática guiada</a></li>' if l.get('pratica_guiada') else '') + f'<li><a href="#exercicios">{"Exercícios independentes" if l.get("pratica_guiada") else "Exercícios"}</a></li>' + ('<li><a href="#aulas">Aulas complementares</a></li>' if aulas else '') + '<li><a href="#leituras">Leituras recomendadas</a></li><li><a href="#creditos">Créditos e fontes</a></li>'
    exs = ''.join(l['exercicios'])
    guiada = ''.join(l.get('pratica_guiada', []))
    erros = ''.join(f'<li><p class="errado"><b>Erro:</b> {a}</p><p class="certo"><b>Por quê, e como evitar:</b> {b}</p></li>' for a, b in l.get('erros_comuns', []))
    erros_html = f'<h2 id="erros">Erros comuns{flag("erros")}</h2><ul class="erros">{erros}</ul>' if erros else ''
    guiada_html = f'<h2 id="pratica">Prática guiada{flag("pratica")}</h2><p class="legend">Resolvida passo a passo: leia a pergunta, tente responder e só então abra cada passo.</p>{guiada}' if guiada else ''
    leituras = ''.join(card(find(i), compact=True) for i in l['leituras'])
    topicos = ''.join(f'<span class="tag">{e(t)}</span>' for t in l['topicos'])
    pr = l['prerequisitos']; pr_links = ''.join(f' · <a href="{SLUG2LICAO[s]["slug"]}.html">capítulo {SLUG2LICAO[s]["numero"]}</a>' if s in SLUG2LICAO else '' for s in pr.get('licoes', []))
    prereq = f'<p class="prereq"><b>Antes deste capítulo:</b> {pr.get("texto") or "nenhum pré-requisito."}{pr_links}</p>'
    aulas_html = ''
    if aulas:
        cards = ''.join(f'<article class="aula-comp"><p class="kicker">{e(a["educador"])}</p><h3><a href="{e(a["url"])}" target="_blank" rel="noopener">{e(a["titulo"])} ↗</a></h3><p>{e(a["descricao"])}</p>'
                        f'<p class="legend">{e(a.get("atribuicao") or f"Aula pública de {a['educador']}, indicada como complemento independente.")} · link conferido em {e(a["verificado"])}</p></article>' for a in aulas)
        aulas_html = f'<h2 id="aulas">Aulas complementares</h2><p class="legend">Aulas públicas de outros educadores sobre o mesmo assunto. São indicações independentes, com link para a página oficial; não reproduzimos seu conteúdo.</p><div class="aulas-comp">{cards}</div>'
    nav = ''
    if prev: nav += f'<a class="ant" href="{licao_href(prev)}">← Capítulo {prev["numero"]}<b>{e(prev["titulo"])}</b></a>'
    if nxt: nav += f'<a class="prox" href="{licao_href(nxt)}">Capítulo {nxt["numero"]} →<b>{e(nxt["titulo"])}</b></a>'
    else: nav += f'<a class="prox" href="./">Voltar ao índice do livro →<b>{"Você chegou ao fim do livro" if len(LICOES) == N_LICOES_TOTAL else "Os próximos capítulos estão em preparação"}</b></a>'
    body = f"""<div class="wrap licao p{l["parte"]}">
<p class="licao-top"><a href="./">{e(LIVRO.TITULO)}</a><span class="sep">·</span><span>Parte {ROMAN[l["parte"]]} · {e(l["parte_nome"])}</span><span class="sep">·</span><span>Capítulo {l["numero"]}</span><span class="sep">·</span><span>{e(l["tempo"])}</span><a class="link-reportar" href="#reportar">Reportar problema</a></p>
<p class="titulo-latim" lang="la">{e(l.get("titulo_latim") or "")}</p>
<h1>{e(l["titulo"])}</h1>
<p class="resumo">{e(l["resumo"])}</p>
<div class="objetivos"><b>Neste capítulo você vai</b><ul>{obj}</ul><div class="topicos">{topicos}</div></div>
{prereq}
<ol class="toc">{toc}</ol>
{secs}
{erros_html}
{guiada_html}
<h2 id="exercicios">{"Exercícios independentes" if guiada else "Exercícios"}{flag("exercicios")}</h2>
<p class="legend">Faça por escrito ou em voz alta; abra "Ver resposta" só depois de tentar. A explicação da resposta faz parte da lição.</p>
{exs}
{aulas_html}
<h2 id="leituras">Leituras recomendadas</h2>
<p>{l.get("leituras_nota", "")}</p>
<div class="leituras-licao">{leituras}</div>
<div class="concluir"><button type="button" class="btn small" data-licao-concluir="{e(l["slug"])}" aria-pressed="false">Marcar capítulo como concluído</button><span>A marcação fica salva só neste navegador.</span></div>
{reportar_html(l)}
{creditos_html(l)}
<nav class="licao-nav" aria-label="Capítulos">{nav}</nav>
</div>"""
    return page(f'aprenda/{l["slug"]}.html', f'Capítulo {l["numero"]}: {l["titulo"]}', l['resumo'], body)

def p_404():
    return page('404.html', 'Página não encontrada', 'Página não encontrada.',
                '<div class="wrap narrow"><h1>Pagina non inventa</h1><p>Essa página não existe. Volte ao <a href="./">início</a> ou ao <a href="catalogo.html">catálogo</a>.</p></div>')

# ───────────────────────── PDF ─────────────────────────
PDF_CSS = '''
@page { size: A4; margin: 20mm 18mm 22mm; @bottom-center { content: "Bibliotheca Latina · Guia de leitura · página " counter(page); font: 8.5pt Helvetica, Arial, sans-serif; color: #6e665b; } }
body { font: 10.5pt/1.45 Georgia, "Times New Roman", serif; color: #211c17; }
h1 { font-size: 26pt; margin: 0 0 .3em; color: #211c17; }
h2 { font-size: 17pt; margin: 1.4em 0 .4em; color: #8a2b1d; page-break-after: avoid; }
h3 { font-size: 12.5pt; margin: 1.1em 0 .3em; page-break-after: avoid; }
p { margin: 0 0 .7em; } a { color: #27496e; text-decoration: none; }
.lead { font-size: 12pt; color: #4b443b; }
.two { display: block; } .box { border: 1px solid #d8ccb3; padding: 6pt 9pt; margin: 0 0 7pt; background: #fbf8f1; font-size: 9.8pt; }
.note { border-left: 3px solid #a98434; padding: 4pt 8pt; background: #f5efe3; font-size: 9.5pt; margin: 6pt 0; }
table { border-collapse: collapse; width: 100%; font-size: 8.8pt; margin: 6pt 0 10pt; page-break-inside: auto; }
th, td { text-align: left; padding: 3.5pt 5pt; border-bottom: 1px solid #d8ccb3; vertical-align: top; }
th { font: bold 7.5pt Helvetica, Arial, sans-serif; letter-spacing: .06em; text-transform: uppercase; color: #6e665b; }
td small { color: #6e665b; font-size: 7.5pt; word-break: break-all; }
tr { page-break-inside: avoid; }
.gradus-sec { page-break-before: always; } .gradus-head h2 { margin-top: 0; } .lvl { font: 9pt Helvetica, Arial, sans-serif; color: #6e665b; }
.scale { display: block; } .scale div { margin: 0 0 4pt; font-size: 9.5pt; } .scale b { display: inline; margin-right: 4pt; }
.cover { height: 240mm; position: relative; page-break-after: always; }
.cover .k { font: 9pt Helvetica, Arial, sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #8a2b1d; margin: 60mm 0 6mm; }
.cover h1 { font-size: 40pt; line-height: 1.05; }
.cover .sub { font-size: 14pt; color: #4b443b; max-width: 120mm; font-style: italic; }
.cover ol { font-size: 11pt; margin-top: 14mm; padding-left: 18pt; } .cover li { margin-bottom: 3pt; }
.cover .rule { height: 2px; width: 60mm; background: linear-gradient(90deg, #8a2b1d, #a98434); margin: 8mm 0; }
.cover .foot { position: absolute; bottom: 0; left: 0; right: 0; font: 8.5pt/1.5 Helvetica, Arial, sans-serif; color: #6e665b; }
.cover img { width: 18mm; }
'''

def build_pdf():
    from weasyprint import HTML
    logo = open(os.path.join(DOCS, 'assets', 'favicon.svg'), encoding='utf-8').read()
    logo_uri = 'data:image/svg+xml;base64,' + base64.b64encode(logo.encode()).decode()
    toc = ''.join(f'<li>Etapa {ROMAN[g]} · <i>{e(d["nome"])}</i> — {e(d["pt"])}</li>' for g, d in GRADUS.items())
    doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Guia de leitura · Bibliotheca Latina</title>
<style>{PDF_CSS}</style></head><body>
<section class="cover"><img src="{logo_uri}" alt=""><p class="k">Bibliotheca Latina · ab initiis ad fontes</p>
<h1>Guia de leitura</h1><div class="rule"></div><p class="sub">Das primeiras palavras às fontes: sete etapas, um método e {N} recursos verificados para aprender latim lendo.</p>
<ol>{toc}</ol>
<p class="foot">Versão de {TODAY} · {SITE}<br>Texto sob licença CC BY 4.0. Os recursos citados seguem as licenças de suas fontes; os endereços levam às páginas oficiais.</p></section>
{plan_body(True)}
</body></html>'''
    HTML(string=doc, base_url=DOCS).write_pdf(os.path.join(DOCS, 'downloads', PDF_NAME))

# ───────────────────────── planilha ─────────────────────────
def build_xlsx():
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.formatting.rule import CellIsRule, FormulaRule
    from openpyxl.worksheet.datavalidation import DataValidation
    from openpyxl.utils import get_column_letter
    INK, ACC, PAPER, LINE = '211C17', '8A2B1D', 'F5EFE3', 'D8CCB3'
    head_font = Font(bold=True, color='FFFFFF'); head_fill = PatternFill('solid', fgColor=INK)
    wb = Workbook()

    def header(ws, cols, widths):
        for i, (c, wdt) in enumerate(zip(cols, widths), 1):
            cell = ws.cell(row=1, column=i, value=c); cell.font = head_font; cell.fill = head_fill
            cell.alignment = Alignment(vertical='center', wrap_text=True); ws.column_dimensions[get_column_letter(i)].width = wdt
        ws.row_dimensions[1].height = 30; ws.freeze_panes = 'A2'

    ws = wb.active; ws.title = 'Comece aqui'; ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 3; ws.column_dimensions['B'].width = 105
    lines = [('Bibliotheca Latina · Diário de leitura', Font(size=22, bold=True, color=ACC)),
             ('ab initiis ad fontes', Font(size=12, italic=True, color='6E665B')), ('', None),
             ('Como usar, em quatro passos', Font(size=14, bold=True)),
             ('1. Na aba "Catálogo", encontre um recurso (use os filtros do cabeçalho: Etapa, Dificuldade, Tipo, Áudio...).', None),
             ('2. Clique em "abrir ↗" para ir à página oficial. Ao começar, mude o Status para "Lendo"; ao terminar, para "Lido".', None),
             ('3. Registre cada sessão na aba "Sessões" e as palavras ou construções novas na aba "Vocabulário" (no máximo 5 por sessão).', None),
             ('4. Escreva seu resumo em latim na aba "Summaria". O "Painel" mostra seu progresso automaticamente.', None), ('', None),
             ('As sete etapas', Font(size=14, bold=True))]
    lines += [(f'Etapa {ROMAN[g]} · {d["nome"]} ({d["pt"]}): {d["curta"]}', None) for g, d in GRADUS.items()]
    lines += [('', None), ('Dificuldade (1 a 5, estimativa editorial, independente da etapa)', Font(size=14, bold=True))]
    lines += [(f'{k} · {v}: {DIF_DESC[k]}', None) for k, v in DIF.items()]
    lines += [('', None), ('Dicas', Font(size=14, bold=True)),
              ('• Mais de 5 a 8 palavras desconhecidas por página que atrapalham o sentido: desça uma etapa.', None),
              ('• Leia em voz alta antes de analisar. Entenda na ordem latina, sem reordenar para o português.', None),
              ('• Anote construções (ablativo absoluto, oração infinitiva), não só palavras.', None),
              ('', None), (f'Site: {SITE}  ·  Versão de {TODAY}  ·  Licença CC BY 4.0', Font(color='6E665B'))]
    for r, (txt, f) in enumerate(lines, 2):
        c = ws.cell(row=r, column=2, value=txt); c.alignment = Alignment(wrap_text=True, vertical='top')
        if f: c.font = f

    # Catálogo
    cat = wb.create_sheet('Catálogo')
    cols = ['#', 'Etapa', 'Nome da etapa', 'Título', 'Autor', 'Categoria', 'Tipo', 'Dificuldade', 'Período', 'Gênero', 'Fonte', 'Gratuito', 'Áudio', 'Formatos', 'Link',
            'Status', 'Início', 'Fim', 'Nota (1–5)', 'Comentário']
    header(cat, cols, [5, 7, 20, 40, 26, 20, 12, 11, 22, 20, 24, 9, 7, 18, 10, 13, 12, 12, 10, 40])
    for r, w in enumerate(W, 2):
        g = w['reading_stage']
        vals = [r - 1, ROMAN[g], GRADUS[g]['nome'], w['title'], w['author'] or '', w['category'], TIPO.get(w.get('original_or_adapted'), ''), w.get('difficulty') or '',
                w['historical_period'], w['genre'], w['source_name'], 'sim' if w.get('free', True) else 'não', 'sim' if w.get('audio_available') else '',
                ', '.join(FMT.get(f, f) for f in w.get('formats_available', [])), None, '', None, None, None, '']
        for c, v in enumerate(vals, 1):
            cell = cat.cell(row=r, column=c, value=v)
            if c in (4, 9, 10, 11, 14): cell.alignment = Alignment(wrap_text=True, vertical='top')
        lk = cat.cell(row=r, column=15, value='abrir ↗'); lk.hyperlink = main_link(w); lk.font = Font(color='27496E', underline='single')
        for c in (17, 18): cat.cell(row=r, column=c).number_format = 'DD/MM/YYYY'
    last = N + 1
    dv = DataValidation(type='list', formula1='"Quero ler,Lendo,Lido,Abandonei"', allow_blank=True); cat.add_data_validation(dv); dv.add(f'P2:P{last}')
    dvn = DataValidation(type='whole', operator='between', formula1='1', formula2='5', allow_blank=True); cat.add_data_validation(dvn); dvn.add(f'S2:S{last}')
    cat.conditional_formatting.add(f'P2:P{last}', CellIsRule(operator='equal', formula=['"Lido"'], fill=PatternFill('solid', fgColor='DCE8D4')))
    cat.conditional_formatting.add(f'P2:P{last}', CellIsRule(operator='equal', formula=['"Lendo"'], fill=PatternFill('solid', fgColor='F3E6C4')))
    cat.conditional_formatting.add(f'P2:P{last}', CellIsRule(operator='equal', formula=['"Quero ler"'], fill=PatternFill('solid', fgColor='DCE3EE')))
    cat.auto_filter.ref = f'A1:T{last}'

    # Sessões
    ses = wb.create_sheet('Sessões')
    header(ses, ['Data', 'Recurso', 'Trecho (capítulo, páginas, linhas)', 'Minutos', 'Em voz alta?', 'Observações'], [12, 40, 30, 9, 12, 50])
    for r in range(2, 402):
        ses.cell(row=r, column=1).number_format = 'DD/MM/YYYY'
    dvv = DataValidation(type='list', formula1='"sim,não"', allow_blank=True); ses.add_data_validation(dvv); dvv.add('E2:E401')

    # Vocabulário
    voc = wb.create_sheet('Vocabulário')
    header(voc, ['Data', 'Palavra ou construção', 'Forma de dicionário', 'Tradução', 'Frase do texto', 'Recurso', 'Revisar em 1 dia', 'Revisar em 3 dias', 'Revisar em 7 dias', 'Aprendida?'],
           [12, 24, 26, 22, 50, 28, 14, 14, 14, 11])
    for r in range(2, 1002):
        voc.cell(row=r, column=1).number_format = 'DD/MM/YYYY'
        for c, dd in ((7, 1), (8, 3), (9, 7)):
            cell = voc.cell(row=r, column=c, value=f'=IF(A{r}="","",A{r}+{dd})'); cell.number_format = 'DD/MM/YYYY'
    dva = DataValidation(type='list', formula1='"sim,não"', allow_blank=True); voc.add_data_validation(dva); dva.add('J2:J1001')
    voc.conditional_formatting.add('G2:I1001', FormulaRule(formula=['AND(G2<>"",G2<=TODAY(),$J2<>"sim")'], fill=PatternFill('solid', fgColor='F3E6C4')))

    # Summaria
    sm = wb.create_sheet('Summaria')
    header(sm, ['Data', 'Recurso', 'Quis? (quem)', 'Quid facit? (o que acontece)', 'Quomodo finitur? (como termina)', 'Dúvidas para rever'], [12, 36, 40, 40, 40, 36])
    for r in range(2, 302): sm.cell(row=r, column=1).number_format = 'DD/MM/YYYY'

    # Painel (fórmulas sobre as outras abas)
    pn = wb.create_sheet('Painel', 1); pn.sheet_view.showGridLines = False
    pn.column_dimensions['A'].width = 3; pn.column_dimensions['B'].width = 30
    for col in 'CDEFG': pn.column_dimensions[col].width = 14
    pn.cell(row=2, column=2, value='Painel de progresso').font = Font(size=18, bold=True, color=ACC)
    pn.cell(row=3, column=2, value='Calculado a partir das outras abas. Não edite esta aba.').font = Font(italic=True, color='6E665B')
    hdr = ['Etapa', 'Recursos', 'Quero ler', 'Lendo', 'Lidos', '% lidos']
    for i, h in enumerate(hdr, 2):
        c = pn.cell(row=5, column=i, value=h); c.font = head_font; c.fill = head_fill
    for k, g in enumerate(GRADUS, 6):
        nm = f'{ROMAN[g]} · {GRADUS[g]["nome"]}'
        pn.cell(row=k, column=2, value=nm)
        pn.cell(row=k, column=3, value=f'=COUNTIF(Catálogo!$B$2:$B${last},"{ROMAN[g]}")')
        for j, st in enumerate(['Quero ler', 'Lendo', 'Lido'], 4):
            pn.cell(row=k, column=j, value=f'=COUNTIFS(Catálogo!$B$2:$B${last},"{ROMAN[g]}",Catálogo!$P$2:$P${last},"{st}")')
        pn.cell(row=k, column=7, value=f'=IF(C{k}=0,0,F{k}/C{k})').number_format = '0%'
    t = 6 + len(GRADUS)
    pn.cell(row=t, column=2, value='Total').font = Font(bold=True)
    for j in range(3, 7): pn.cell(row=t, column=j, value=f'=SUM({get_column_letter(j)}6:{get_column_letter(j)}{t-1})').font = Font(bold=True)
    pn.cell(row=t, column=7, value=f'=IF(C{t}=0,0,F{t}/C{t})').number_format = '0%'
    extra = [('Sessões registradas', '=COUNTA(Sessões!A2:A401)'), ('Minutos lidos', '=SUM(Sessões!D2:D401)'),
             ('Palavras e construções anotadas', '=COUNTA(Vocabulário!B2:B1001)'), ('Aprendidas', '=COUNTIF(Vocabulário!J2:J1001,"sim")'),
             ('Revisões pendentes hoje', '=SUMPRODUCT((Vocabulário!G2:I1001<>"")*(Vocabulário!G2:I1001<=TODAY())*(Vocabulário!J2:J1001<>"sim"))'),
             ('Summaria escritos', '=COUNTA(Summaria!A2:A301)')]
    for k, (lab, f) in enumerate(extra, t + 2):
        pn.cell(row=k, column=2, value=lab); pn.cell(row=k, column=3, value=f).font = Font(bold=True)
    for sh in wb.worksheets:
        for row in sh.iter_rows(min_row=1, max_row=1):
            for c in row: c.border = Border(bottom=Side(style='thin', color=LINE))
    wb.save(os.path.join(DOCS, 'downloads', XLSX_NAME))

# ───────────────────────── dados abertos, auditoria, sitemap ─────────────────────────
PUBLIC_FIELDS = ['id', 'title', 'author', 'original_language', 'historical_period', 'genre', 'category', 'reading_stage', 'difficulty',
                 'vocabulary_difficulty', 'morphology_difficulty', 'syntax_difficulty', 'recommended_prerequisites', 'original_or_adapted',
                 'source_name', 'source_url', 'official_url', 'license', 'license_url', 'rights_status', 'hosting_allowed', 'formats_available',
                 'pdf_url', 'epub_url', 'online_reading_url', 'audio_available', 'audio_url', 'audio_pronunciation', 'notes_available',
                 'estimated_reading_time', 'description_pt_br', 'recommended_order', 'free', 'verification_status', 'last_verified']

def build_data():
    pub = [{k: w.get(k) for k in PUBLIC_FIELDS} for w in W]
    json.dump(pub, open(os.path.join(DOCS, 'dados', 'catalogo.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(DOCS, 'dados', 'catalogo.csv'), 'w', encoding='utf-8', newline='') as f:
        wr = csv.DictWriter(f, fieldnames=PUBLIC_FIELDS); wr.writeheader()
        for w in pub: wr.writerow({k: (', '.join(v) if isinstance(v, list) else v) for k, v in w.items()})
    aud_fields = ['id', 'title', 'author', 'source_name', 'source_url', 'license', 'license_url', 'rights_status', 'hosting_allowed', 'free', 'rights_note', 'verification_status', 'last_verified']
    for path in (os.path.join(DOCS, 'dados', 'auditoria-direitos.csv'), os.path.join(DATA, 'auditoria-direitos.csv')):
        with open(path, 'w', encoding='utf-8', newline='') as f:
            wr = csv.DictWriter(f, fieldnames=aud_fields); wr.writeheader()
            for w in W: wr.writerow({k: w.get(k) for k in aud_fields})
    pages = ['', 'catalogo.html', 'percurso.html', 'recursos.html', 'guia.html', 'sobre.html', 'aprenda/'] + [f'aprenda/{l["slug"]}.html' for l in LICOES]
    sm = ''.join(f'<url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod></url>' for p in pages)
    open(os.path.join(DOCS, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    open(os.path.join(DOCS, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')

def validate():
    ids = set(); errs = []
    req = ['id', 'title', 'historical_period', 'genre', 'category', 'reading_stage', 'original_or_adapted', 'source_name', 'source_url', 'license',
           'rights_status', 'hosting_allowed', 'formats_available', 'audio_available', 'notes_available', 'description_pt_br', 'free', 'verification_status', 'last_verified']
    for w in W:
        for k in req:
            if k not in w: errs.append(f'{w.get("id")}: falta o campo {k}')
        if w['id'] in ids: errs.append(f'id duplicado: {w["id"]}')
        ids.add(w['id'])
        if w['reading_stage'] not in GRADUS: errs.append(f'{w["id"]}: reading_stage inválido')
        if w.get('difficulty') is not None and w['difficulty'] not in DIF: errs.append(f'{w["id"]}: difficulty inválida')
        if w['historical_period'] not in PERIODOS: errs.append(f'{w["id"]}: historical_period inválido: {w["historical_period"]}')
        if w['category'] not in CATEGORIAS: errs.append(f'{w["id"]}: category inválida')
        if w['original_or_adapted'] not in TIPO: errs.append(f'{w["id"]}: original_or_adapted inválido')
        if w['rights_status'] not in RIGHTS: errs.append(f'{w["id"]}: rights_status inválido')
        if w['hosting_allowed'] and w['rights_status'] not in ('public_domain', 'creative_commons'): errs.append(f'{w["id"]}: hosting_allowed sem base')
        if not w.get('free', True) and w['rights_status'] != 'commercial': errs.append(f'{w["id"]}: não gratuito deve ser commercial')
        if w.get('audio_available') and not w.get('audio_url'): errs.append(f'{w["id"]}: áudio sem URL')
        for f in w['formats_available']:
            if f not in FMT: errs.append(f'{w["id"]}: formato inválido {f}')
        if not (w.get('online_reading_url') or w.get('pdf_url') or w['source_url']): errs.append(f'{w["id"]}: sem link')
    if errs: sys.exit('Catálogo inválido:\n  ' + '\n  '.join(errs))
    print(f'Catálogo válido: {N} recursos, {NL} leituras, {NA} com áudio, {NF} gratuitos, {NSRC} fontes.')

def main():
    validate()
    for fname, fn in [('index.html', p_index), ('catalogo.html', p_catalogo), ('percurso.html', p_percurso), ('recursos.html', p_recursos),
                      ('guia.html', p_guia), ('sobre.html', p_sobre), ('404.html', p_404)]:
        open(os.path.join(DOCS, fname), 'w', encoding='utf-8').write(fn())
    os.makedirs(os.path.join(DOCS, 'aprenda'), exist_ok=True)
    open(os.path.join(DOCS, 'aprenda', 'index.html'), 'w', encoding='utf-8').write(p_aprenda())
    for k, l in enumerate(LICOES):
        open(os.path.join(DOCS, 'aprenda', f'{l["slug"]}.html'), 'w', encoding='utf-8').write(p_licao(l, k))
    for f in os.listdir(os.path.join(DOCS, 'aprenda')):   # remove páginas de lições que saíram do build (ex.: --so-publicadas)
        if f != 'index.html' and f[:-5] not in SLUG2LICAO: os.remove(os.path.join(DOCS, 'aprenda', f))
    print(f'Aprenda Latim: {len(LICOES)} lições geradas de {N_LICOES_TOTAL} planejadas' + (' (só publicadas)' if SO_PUBLICADAS else '') + '; status: ' + ', '.join(f'{l["numero"]}={l["status"]}' for l in LICOES) + '.')
    build_data()
    if '--sem-xlsx' not in sys.argv: build_xlsx(); print('Planilha gerada.')
    if '--sem-pdf' not in sys.argv:
        try: build_pdf(); print('PDF gerado.')
        except Exception as ex: print(f'AVISO: PDF não gerado ({ex}). Use --sem-pdf para silenciar.')
    print(f'Site gerado em docs/ ({TODAY}).')

if __name__ == '__main__': main()
