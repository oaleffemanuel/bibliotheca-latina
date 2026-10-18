#!/usr/bin/env python3
"""Importa para textos/<id>/ obras de outras fontes além da Perseus: eBooks do Project Gutenberg (texto puro)
e páginas do Wikisource latino (Vicifons), numa versão fixa (número do eBook; revisão da página).
O formato de texto.txt e as regras gerais estão em ferramentas/importar_perseus.py; aqui cada obra declara
onde o texto latino começa e termina e o que é omitido (prefácios modernos, notas, legendas), tudo registrado
em metadata.json. Uso: python3 ferramentas/importar_fontes.py [id ...]"""
import html, json, os, re, subprocess, sys, unicodedata
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(os.environ.get('TMPDIR', '/tmp'), 'bibliotheca-latina-fontes')
VERIFICADO = '2026-10-18'
WD = 'https://www.wikidata.org/wiki/'
UA = 'BibliothecaLatina/1.0 (aleffoemanuel@gmail.com)'
ROMANOS = r'[IVXLC]+'

def baixar(url, nome):
    os.makedirs(CACHE, exist_ok=True)
    dest = os.path.join(CACHE, nome)
    if not os.path.exists(dest):
        subprocess.run(['curl', '-sfL', '-A', UA, '-o', dest, url], check=True)
    return open(dest, encoding='utf-8').read()

def ws(s): return re.sub(r'\s+', ' ', s or '').strip()

def palavras(t): return Counter(re.findall(r"[^\W\d_]+", t))

# ───── Project Gutenberg ─────
def pg_corpo(n):
    t = baixar(f'https://www.gutenberg.org/cache/epub/{n}/pg{n}.txt', f'pg{n}.txt').replace('\r\n', '\n')
    a = t.index('\n', t.index('*** START OF')) + 1; b = t.index('*** END OF')
    return t[a:b]

def blocos_pg(trecho):
    """Parágrafos separados por linha em branco; linhas unidas com espaço."""
    return [ws(b) for b in re.split(r'\n\s*\n', trecho) if ws(b)]

def appleton(cfg):
    corpo = pg_corpo(57615)
    ini = corpo.index('\nDĒ SĀGĪS\n'); fim = corpo.index('\nINDEX VERBŌRUM')
    trecho = corpo[ini:fim]
    omit = re.findall(r'\[[^\]]*\]', trecho)                 # [Image: legenda] e quadros com glosas em inglês
    trecho = re.sub(r'\[[^\]]*\]', '\n\n', trecho)
    out, cap, k = [], '', 0
    for b in blocos_pg(trecho):
        if re.fullmatch(r'[A-ZĀĒĪŌŪȲ][A-ZĀĒĪŌŪȲ .,\'’-]+', b) and len(b) < 60:   # título de fábula em maiúsculas
            out += ['', '## ' + b.title() if False else '## ' + b]; cap = b; k = 0; continue
        if re.fullmatch(ROMANOS, b):                            # divisão interna da fábula (I, II, ...)
            out.append(f'\t{b}'); continue
        k += 1; out.append(f'{len([x for x in out if x.startswith("## ")])}.{k}\t{b.replace("_", "")}')
    return out, trecho, omit

def insula(cfg):
    corpo = pg_corpo(68935)
    ini = corpo.index('\nPars prima\n'); fim = corpo.index('\n    Caput XIV\n') if False else None
    # fim do romance: antes da lista de correções do transcritor, que começa com recuo e "Caput I"
    m = re.search(r'\n {4}Caput I\n', corpo); fim = m.start() if m else len(corpo)
    trecho = corpo[ini:fim]
    notas = re.findall(r'\n\s*\[\d+\][^\n]*(?:\n(?!\s*\n)[^\n]*)*', trecho)   # notas de rodapé no fim dos capítulos
    for nt in notas: trecho = trecho.replace(nt, '\n')
    trecho = re.sub(r'\[\d+\]', '', trecho)
    out, cap, k = [], 0, 0
    for b in blocos_pg(trecho):
        if re.match(r'Pars (prima|secunda|tertia|quarta|quinta|sexta)\b', b, re.I) and len(b) < 70: out += ['', '# ' + b]; continue
        if re.match(r'Caput ' + ROMANOS + r'\.', b) and len(b) < 90: out += ['', '## ' + b]; cap += 1; k = 0; continue
        k += 1; out.append(f'{cap}.{k}\t{b.replace("_", "")}')
    return out, trecho, notas

def descartes(cfg):
    corpo = pg_corpo(23306)
    ini = corpo.index('SAPIENTISSIMIS'); fim = re.search(r'\n\s*\(1\) Descartes schreibt', corpo).start()
    trecho = corpo[ini:fim]
    limpo = re.sub(r'\s+\[\d+\][ \t]*$', '', trecho, flags=re.M)        # número de página da 1ª ed. na margem
    limpo = re.sub(r'(\w)\|(\w)', r'\1\2', limpo); limpo = re.sub(r'[ \t]*\|[ \t]*', ' ', limpo)   # quebra de página
    limpo = re.sub(r'\((\d+)\)', '', limpo)                              # chamadas das notas alemãs de Buchenau
    out, cap, k = [], 0, 0
    secoes = [('SAPIENTISSIMIS', 'Epistola dedicatoria'), ('Praefatio ad lectorem.', 'Praefatio ad lectorem'), ('Synopsis sex sequentium meditationum.', 'Synopsis sex sequentium meditationum')]
    for b in blocos_pg(limpo):
        tit = next((t for s, t in secoes if b.startswith(s)), None)
        m = re.match(r'(Meditatio ' + ROMANOS + r'\.)\s*(.*)$', b)
        if tit and (tit != 'Epistola dedicatoria' or cap == 0):
            out += ['', '# ' + tit]; cap += 1; k = 0
            resto = b[len(next(s for s, t in secoes if t == tit)):].strip()
            if tit == 'Epistola dedicatoria': resto = b   # o cabeçalho da dedicatória faz parte do texto
            if resto: k += 1; out.append(f'{cap}.{k}\t{resto.replace("_", "")}')
            continue
        if m:
            out += ['', '# ' + ws(m.group(0))]; cap += 1; k = 0; continue
        k += 1; out.append(f'{cap}.{k}\t{b.replace("_", "")}')
    return out, trecho, ['notas e variantes de Buchenau, em alemão']

# ───── Wikisource ─────
def wikisource(titulo, nome):
    import urllib.parse
    if titulo.startswith('http'): titulo = urllib.parse.unquote(titulo.split('/wiki/', 1)[1]).replace('_', ' ')
    q = json.loads(baixar('https://la.wikisource.org/w/api.php?' + urllib.parse.urlencode(dict(action='query', prop='revisions', rvprop='ids|timestamp', titles=titulo, format='json', formatversion=2)), nome + '-rev.json'))
    rev = q['query']['pages'][0]['revisions'][0]
    p = json.loads(baixar('https://la.wikisource.org/w/api.php?' + urllib.parse.urlencode(dict(action='parse', oldid=rev['revid'], prop='text', format='json', formatversion=2, disablelimitreport=1)), nome + f'-{rev["revid"]}.json'))
    return p['parse']['text'], rev

def html_texto(h):
    h = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', '', h)
    h = re.sub(r'(?is)<span[^>]*class="dropinitial"[^>]*>\s*(\w)\s*</span>', r'\1', h)   # letra capitular colada à palavra
    h = re.sub(r'(?is)<(div|span|table)[^>]*class="[^"]*(?:pagenum|ws-noexport|headertemplate|mw-editsection|noprint|reference|navbox|Liber|ws-pagenum)[^"]*"[^>]*>.*?</\1>', '', h)
    h = re.sub(r'(?is)<sup[^>]*class="[^"]*reference[^"]*"[^>]*>.*?</sup>', '', h)
    h = re.sub(r'(?i)<br\s*/?>', '\n', h)
    h = re.sub(r'(?i)</(p|div|h[1-6]|li|tr|dd|dt)>', '\n\n', h)
    h = re.sub(r'(?i)<h([1-6])[^>]*>', lambda m: '\n\n@@H' + m.group(1) + ' ', h)
    t = html.unescape(re.sub(r'<[^>]+>', '', h))
    return t

def lhomond(cfg):
    h, rev = wikisource(cfg['pagina'], 'lhomond')
    cfg['_rev'] = rev
    t = html_texto(h)
    out, cap, k, ini, latim, omit = [], 0, 0, False, [], []
    INGLES = re.compile(r"\b(the|of|and|his|her|their|to|is|are|by|from|with|for|God|he|they|was|which)\b|'s\b")
    blocos = []
    for b in [ws(x) for x in re.split(r'\n\s*\n', t) if ws(x)]:
        b = re.sub(r'@@H\d ', '', b)
        b = re.sub(r'\{\{c\|([^{}]*?)\}\}?', r'\1', b).strip()   # predefinição {{c|...}} com chave faltando na fonte, exibida literalmente
        b2 = re.sub(r'\{\{hws\|[^|{}]*\|([^|{})]*)[)}]{2}\s*\1', r'\1', b)   # {{hws|de|delapsus)) delapsus → delapsus (predefinição de hifenização quebrada)
        if b2 != b: cfg['normalizacao'] = cfg['normalizacao'] + ['Resto de predefinição de hifenização quebrada na fonte corrigido: “{{hws|de|delapsus)) delapsus” → “delapsus”.']; b = b2
        # sumário em inglês grudado no fim do parágrafo latino anterior (falta de quebra na transcrição)
        m = re.search(r'(?<=[.;:!?\w])\s+(\d{1,3})\.\s+([A-Z][^\n]*)$', b)
        if m and not re.match(r'\d+\.', b) and len(INGLES.findall(m.group(2))) >= 2:
            blocos += [b[:m.start()].strip(), f'{m.group(1)}. {m.group(2)}']
        else: blocos.append(b)
    # números impressos dos capítulos (sumários em inglês); corrige só o que quebra a sequência e cujo número esperado não aparece em lugar nenhum
    nums = [int(re.match(r'(\d+)\. ', b).group(1)) for b in blocos if re.match(r'\d{1,3}\. \S', b)]
    presentes = set(nums)
    renum, anterior, fila = [], 0, iter(nums)
    for b in blocos:
        if b == 'HISTORIÆ SACRÆ.': ini = True; continue
        if not ini: continue
        m = re.match(r'(\d{1,3})\. (.+)$', b)
        if m:   # sumário do capítulo, em inglês, do editor de 1856: fica só o número
            n = int(m.group(1)); esp = anterior + 1
            if n != esp and esp not in presentes:
                renum.append(f'{n}→{esp}'); n = esp
            anterior = n
            out += ['', f'## {n}']; cap = n; k = 0; omit.append(m.group(2)); continue
        k += 1; out.append(f'{cap}.{k}\t{b}'); latim.append(b)
        if b.startswith('Finis Historiæ Sacræ'): break
    if renum:
        cfg['normalizacao'] = cfg['normalizacao'] + ['Números de capítulo lidos errado na transcrição corrigidos pela sequência da edição (só quando o número esperado não aparece em outro lugar): ' + ', '.join(renum) + '.']
    print('   capítulos:', len([x for x in out if x.startswith('## ')]), '| corrigidos:', ', '.join(renum) or 'nenhum')
    return out, '\n\n'.join(latim), omit

def dies_irae(cfg):
    h, rev = wikisource(cfg['pagina'], 'diesirae')
    cfg['_rev'] = rev
    t = html_texto(h)
    linhas = [ws(x) for x in t.split('\n')]
    out, n, latim, ini = [], 0, [], False
    for l in linhas:
        if not l or l.startswith('@@H'): continue
        if l.startswith('Dies Iræ, dies illa, dies tribulationis'):   # epígrafe (Sofonias 1,15-16) impressa pela antologia
            out.append(f'\t{l}'); latim.append(l); ini = True; continue
        if not ini: continue
        if re.fullmatch(ROMANOS + r'\.', l): out.append(''); continue   # número da estrofe
        n += 1; out.append(f'{n}\t{l}'); latim.append(l)
    return out, '\n'.join(latim), []

OBRAS = {
    'appleton-fabulae-virginibus-puerisque-aut-narrandae-aut-recitandae': dict(fonte='pg', ebook=57615, forma='prosa', f=appleton, titulo_latino='Fabulae virginibus puerisque aut narrandae aut recitandae',
        edicoes=[dict(editor='R. B. Appleton (autor)', edicao='Fabulae virginibus puerisque aut narrandae aut recitandae', local='Londres', editora='G. Bell and Sons', ano='1914', morte=1938, fonte_morte=WD + 'Q106695381')],
        obra_nota='Obra moderna em latim de R. B. Appleton (†1938), em domínio público no Brasil desde 2009 e nos EUA (publicada em 1914).',
        omitido=['prefácio em inglês do autor', 'legendas das ilustrações e quadros com glosas em inglês', 'índice de palavras (Index verbōrum)'],
        normalizacao=['Texto do eBook #57615 do Project Gutenberg, sem o cabeçalho e a licença do projeto; quantidades vocálicas (mácrons) como na edição de 1914, inclusive as que o transcritor aponta como divergentes do Oxford Latin Dictionary.',
                      'Parágrafos numerados pela Bibliotheca Latina (fábula.parágrafo) para navegação; não é a numeração da edição.', 'Marcas de itálico do texto puro (_..._) retiradas.']),
    'stevenson-insula-thesauraria': dict(fonte='pg', ebook=68935, forma='prosa', f=insula, titulo_latino='Insula Thesauraria',
        edicoes=[dict(editor='Arcadius Avellanus (tradutor)', edicao='Insula Thesauraria (Mount Hope Classics, vol. V)', local='Nova York', editora='E. Parmalee Prentice', ano='1922', morte=1935, fonte_morte=WD + 'Q4785199')],
        obra_nota='Tradução latina (1922) do romance de R. L. Stevenson (†1894) por Arcadius Avellanus (†1935); obra original e tradução em domínio público no Brasil e nos EUA.',
        omitido=['prefácio da série Mount Hope Classics', 'notas de rodapé da edição (glosas dos neologismos)', 'lista de correções do transcritor (as correções já estão aplicadas no texto)'],
        normalizacao=['Texto do eBook #68935 do Project Gutenberg, sem o cabeçalho e a licença do projeto; inclui as correções tipográficas do transcritor listadas no fim do eBook.',
                      'Parágrafos numerados pela Bibliotheca Latina (capítulo.parágrafo) para navegação.', 'Chamadas de nota [n] retiradas; marcas de itálico (_..._) retiradas.']),
    'descartes-meditationes-de-prima-philosophia': dict(fonte='pg', ebook=23306, forma='prosa', f=descartes, titulo_latino='Meditationes de prima philosophia',
        edicoes=[dict(editor='Artur Buchenau', edicao='Descartes, Meditationes de prima philosophia (Bibliotheca Philosophorum, vol. I)', local='Leipzig', editora='Felix Meiner', ano='1913', morte=1946, fonte_morte=WD + 'Q18616420')],
        obra_nota='Obra de René Descartes (†1650), em domínio público.',
        omitido=['prefácio em alemão de Buchenau', 'notas e variantes de Buchenau, em alemão', 'notas do transcritor'],
        normalizacao=['Texto do eBook #23306 do Project Gutenberg, sem o cabeçalho e a licença do projeto.',
                      'Números de página da 1ª edição na margem ([n]) e barras de quebra de página (|) retirados; palavras partidas pela barra reunidas.',
                      'Chamadas das notas de Buchenau ((n)) retiradas.', 'O título “Epistola dedicatoria” foi acrescentado para a navegação; a edição abre a carta direto com o endereçamento (SAPIENTISSIMIS...).', 'Parágrafos numerados pela Bibliotheca Latina (seção.parágrafo) para navegação.']),
    'lhomond-epitome-historiae-sacrae': dict(fonte='ws', pagina='https://la.wikisource.org/wiki/Epitome_histori%C3%A6_sacr%C3%A6', forma='prosa', f=lhomond, titulo_latino='Epitome historiae sacrae',
        edicoes=[dict(editor='George Ironside e Thomas S. Joy', edicao='Epitome historiae sacrae (Lhomond)', local='Filadélfia', editora='E. H. Butler & Co.', ano='1856', morte=None,
                      fonte_morte='sem registro no Wikidata; editores de livro publicado em 1856, portanto necessariamente falecidos muito antes de 1956')],
        obra_nota='Obra de Charles-François Lhomond (†1794), em domínio público.',
        omitido=['sumários dos capítulos em inglês, do editor de 1856 (fica só o número do capítulo)', 'página de rosto, advertência em inglês e vocabulário da edição de 1856', 'elementos de navegação do Wikisource'],
        normalizacao=['Texto da página do Wikisource latino transcrita e revisada a partir do fac-símile da edição de 1856 (Internet Archive), na revisão indicada.',
                      'Parágrafos numerados pela Bibliotheca Latina (capítulo.parágrafo) para navegação.']),
    'celano-dies-irae': dict(fonte='ws', pagina='https://la.wikisource.org/wiki/The_seven_great_hymns_of_the_mediaeval_church/Dies_Ir%C3%A6/Tommaso', forma='verso', f=dies_irae, titulo_latino='Dies irae',
        edicoes=[dict(editor='Charles Cooper Nott', edicao='The Seven Great Hymns of the Mediaeval Church (ed. revista)', local='Nova York', editora='Anson D. F. Randolph', ano='1902', morte=1916, fonte_morte=WD + 'Q5076009')],
        obra_nota='Sequência medieval atribuída a Tomás de Celano (séc. XIII), em domínio público.',
        omitido=['tradução inglesa e comentário da antologia'],
        normalizacao=['Texto da página do Wikisource latino, na revisão indicada; versos numerados pela Bibliotheca Latina.']),
}

def metadados(id_, cfg, omit_achados):
    eds = cfg['edicoes']
    if cfg['fonte'] == 'pg':
        land = f'https://www.gutenberg.org/ebooks/{cfg["ebook"]}'
        tr = dict(nome=f'Project Gutenberg, eBook #{cfg["ebook"]}', arquivos=[land], versao=f'eBook #{cfg["ebook"]}', commit='', acessado_em=VERIFICADO)
        lic = dict(nome='Domínio público', url='https://creativecommons.org/publicdomain/mark/1.0/deed.pt-br',
                   declaracao='O Project Gutenberg declara que os eBooks em domínio público nos EUA podem ser redistribuídos “with or without the Project Gutenberg trademark” e que não é preciso permissão para citá-lo como fonte (gutenberg.org/policy/permission.html). No Brasil, a obra e a edição estão em domínio público (ver auditoria).')
        atr = f'Texto latino: {eds[0]["edicao"]}, {eds[0]["editor"]} ({eds[0]["local"]}: {eds[0]["editora"]}, {eds[0]["ano"]}). Transcrição: Project Gutenberg, eBook #{cfg["ebook"]} ({land}). Formatação (página, PDF, EPUB): Bibliotheca Latina. Texto em domínio público.'
        a5 = 'Transcrição do Project Gutenberg de obra em domínio público; o projeto permite redistribuir sem a marca e citar a fonte sem permissão.'
        a6 = a7 = 'Sim: obra em domínio público no Brasil e nos EUA; o Project Gutenberg não impõe restrição ao uso não comercial sem a marca.'
        a8 = 'Nenhuma exigida; citamos a edição impressa e o eBook do Project Gutenberg por transparência.'
    else:
        rev = cfg['_rev']; url = f'https://la.wikisource.org/w/index.php?oldid={rev["revid"]}'
        import urllib.parse
        tr = dict(nome='Wikisource latino (Vicifons), página “' + urllib.parse.unquote(cfg['pagina'].split('/wiki/', 1)[-1]).replace('_', ' ') + '”', arquivos=[url], versao=f'revisão {rev["revid"]} ({rev["timestamp"][:10]})', commit='', acessado_em=VERIFICADO)
        lic = dict(nome='CC BY-SA 4.0', url='https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br',
                   declaracao='Wikisource: texto disponível sob a licença Creative Commons Atribuição-CompartilhaIgual (rodapé de cada página); a obra e a edição estão em domínio público.')
        atr = f'Texto latino: {eds[0]["edicao"]}, ed. {eds[0]["editor"]} ({eds[0]["local"]}: {eds[0]["editora"]}, {eds[0]["ano"]}). Transcrição: colaboradores do Wikisource latino ({url}; histórico na própria página), CC BY-SA 4.0. Formatação (página, PDF, EPUB): Bibliotheca Latina, sob a mesma licença.'
        a5 = 'CC BY-SA 4.0 (Wikisource).'
        a6 = 'Sim: CC BY-SA 4.0 permite copiar e redistribuir.'
        a7 = 'Sim: CC BY-SA 4.0 permite adaptar (PDF, EPUB), com atribuição e mesma licença.'
        a8 = 'Créditos aos colaboradores do Wikisource (link da revisão e do histórico), à edição-fonte e à licença; derivados sob CC BY-SA 4.0.'
    m_txt = lambda x: f'†{x["morte"]}' if x.get('morte') else 'data de morte não localizada'
    dirbr = ('Domínio público no Brasil (' + (f'falecido em {eds[0]["morte"]}' if eds[0].get('morte') else eds[0]['fonte_morte']) + '; Lei 9.610/98, art. 41) e nos EUA (publicada antes de 1931).')
    return {
        'id': id_, 'titulo_latino': cfg['titulo_latino'], 'forma': cfg['forma'],
        'edicoes': [{k: x[k] for k in ('editor', 'edicao', 'local', 'editora', 'ano')} for x in eds],
        'transcricao': tr, 'licenca': lic, 'atribuicao': atr,
        'auditoria': {'1_autor_e_obra': cfg['obra_nota'], '2_edicao_fonte': f'{eds[0]["edicao"]}, {eds[0]["editor"]} ({eds[0]["local"]}: {eds[0]["editora"]}, {eds[0]["ano"]}), conforme a própria fonte digital.',
                      '3_data_e_editor': f'{eds[0]["ano"]}; {eds[0]["editor"]} ({m_txt(eds[0])}; fonte: {eds[0]["fonte_morte"]}).', '4_direitos_da_edicao': dirbr,
                      '5_licenca_da_transcricao': a5, '6_permissao_de_reproduzir': a6, '7_permissao_de_derivados': a7, '8_atribuicao_exigida': a8},
        'decisao': 'hospedar', 'downloads': True, 'omitido': cfg['omitido'], 'normalizacao': cfg['normalizacao'], 'verificado_em': VERIFICADO}

def main():
    for id_ in (sys.argv[1:] or list(OBRAS)):
        cfg = OBRAS[id_]
        out, fonte_txt, omit = cfg['f'](cfg)
        txt = re.sub(r'\n{3,}', '\n\n', '\n'.join(out).strip('\n') + '\n')
        d = os.path.join(ROOT, 'textos', id_); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'texto.txt'), 'w', encoding='utf-8').write(txt)
        json.dump(metadados(id_, cfg, omit), open(os.path.join(d, 'metadata.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        corpo = '\n'.join(l.split('\t', 1)[1] if '\t' in l else l.lstrip('# ') for l in txt.splitlines() if '\t' in l or (l.startswith('#') and cfg['f'] is not lhomond))
        esperado = palavras(fonte_txt.replace('_', ' ')); obtido = palavras(corpo)
        if cfg['f'] is descartes:
            esperado = palavras(re.sub(r'\((\d+)\)', '', re.sub(r'(\w)\|(\w)', r'\1\2', fonte_txt)))
        falta, sobra = esperado - obtido, obtido - esperado
        print(f'   conferência: {sum(esperado.values())} palavras na fonte, {sum(falta.values())} ausentes, {sum(sobra.values())} a mais', falta.most_common(5) if falta else '', sobra.most_common(5) if sobra else '')
        print(f'{id_}: {sum(1 for l in txt.splitlines() if chr(9) in l)} linhas/parágrafos, {len(corpo.split())} palavras, {sum(1 for l in txt.splitlines() if l.startswith("#"))} títulos')

if __name__ == '__main__': main()
