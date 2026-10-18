#!/usr/bin/env python3
"""Importa textos latinos da Perseus Digital Library (repositório PerseusDL/canonical-latinLit, CC BY-SA 4.0)
para textos/<id>/texto.txt, numa versão fixa (commit) para que a importação seja reproduzível.

Uso: python3 ferramentas/importar_perseus.py [id ...]     (sem argumentos: todas as obras de OBRAS)

Formato de texto.txt (lido por ferramentas/construir.py):
  # Título           cabeçalho de 1º nível (livro, discurso)
  ## Título          cabeçalho de 2º nível (poema, fábula, episódio)
  > Nome             personagem que fala (diálogos em verso)
  ref<TAB>texto      parágrafo (prosa) ou verso (poesia); ref = capítulo ou número do verso
  {n}                dentro de um parágrafo: início da seção n
  linha em branco    separa estrofes / grupos
Regras de conversão (iguais para todas as obras, registradas em metadata.json → normalizacao):
  - notas (<note>) e variantes do aparato (<app>/<rdg>) são omitidas: são material editorial, não texto latino;
  - acréscimos do editor (<add>) entre ⟨ ⟩; supressões propostas pelo editor (<del>) entre [ ]; lacunas (<gap>) como * * *;
  - <choice>: usa a correção marcada pela Perseus (<corr>, erros de digitalização) e a abreviatura impressa (<abbr>);
  - <q> recebe aspas “ ” apenas quando o arquivo declara que as aspas foram retiradas (<quotation marks="none">);
    <q rend="merge"> continua a citação do verso anterior: abre-se uma vez e fecha-se no último verso da fala;
  - nada mais é alterado: grafia, maiúsculas, u/v, pontuação e ordem são as da edição.
"""
import json, os, re, subprocess, sys
from xml.etree import ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMIT = '128a05afa9cc7179ab18f8d05f78a9f1dd50e415'   # PerseusDL/canonical-latinLit, master em 2026-10-18
RAW = 'https://raw.githubusercontent.com/PerseusDL/canonical-latinLit/{c}/data/{p}'
BLOB = 'https://github.com/PerseusDL/canonical-latinLit/blob/{c}/data/{p}'
CACHE = os.path.join(os.environ.get('TMPDIR', '/tmp'), 'bibliotheca-latina-perseus')
T = '{http://www.tei-c.org/ns/1.0}'

# id do catálogo → arquivo TEI, forma, e como achar livros/capítulos
OBRAS = {
    'phaedrus-fabulae-aesopiae': dict(tei='phi0975/phi001/phi0975.phi001.perseus-lat2.xml', forma='verso'),
    'caesar-commentarii-de-bello-gallico-texto-integral': dict(tei='phi0448/phi001/phi0448.phi001.perseus-lat2.xml', forma='prosa', livro='Liber'),
    'cicero-in-catilinam-i-iv': dict(tei='phi0474/phi013/phi0474.phi013.perseus-lat2.xml', forma='prosa'),
    'cicero-laelius-de-amicitia': dict(tei='phi0474/phi052/phi0474.phi052.perseus-lat2.xml', forma='prosa'),
    'cicero-cato-maior-de-senectute': dict(tei='phi0474/phi051/phi0474.phi051.perseus-lat2.xml', forma='prosa'),
    'crispus-bellum-catilinae': dict(tei='phi0631/phi001/phi0631.phi001.perseus-lat3.xml', forma='prosa'),
    'livius-ab-urbe-condita-liber-i': dict(tei='phi0914/phi001/phi0914.phi001.perseus-lat2.xml', forma='prosa', so_livro='1'),
    'maro-bucolica-eclogae': dict(tei='phi0690/phi001/phi0690.phi001.perseus-lat2.xml', forma='verso'),
    'maro-aeneis-texto-integral': dict(tei='phi0690/phi003/phi0690.phi003.perseus-lat2.xml', forma='verso', livro='Liber'),
    'naso-metamorphoses-texto-integral': dict(tei='phi0959/phi006/phi0959.phi006.perseus-lat2.xml', forma='verso', livro='Liber', episodios=True),
}
# Edição-fonte de cada arquivo TEI (lida no <sourceDesc> do próprio arquivo) e data de morte do editor,
# conferida em 2026-10-18 (Wikidata / Wikipédia). Lei 9.610/98, art. 41: domínio público no Brasil a partir de
# 1º de janeiro do ano seguinte aos 70 anos da morte; nos EUA, obras publicadas até 1930 estão em domínio público.
EDICOES = {
    'phaedrus-fabulae-aesopiae': dict(titulo_latino='Fabulae Aesopiae', editor='Lucian Mueller', edicao='Phaedri Fabulae Aesopiae', local='Leipzig', editora='B. G. Teubner', ano='1876', morte=1898, fonte_morte='https://www.wikidata.org/wiki/Q71344'),
    'caesar-commentarii-de-bello-gallico-texto-integral': dict(titulo_latino='Commentarii de bello Gallico (com o livro VIII de A. Hírcio)', editor='T. Rice Holmes', edicao='C. Iuli Commentarii Rerum in Gallia Gestarum VII, A. Hirti Commentarius VIII', local='Oxford', editora='Clarendon Press (Scriptorum Classicorum Bibliotheca Oxoniensis)', ano='1914', morte=1933, fonte_morte='https://www.wikidata.org/wiki/Q7668644'),
    'cicero-in-catilinam-i-iv': dict(titulo_latino='In L. Catilinam orationes IV', editor='Albert Curtis Clark', edicao='M. Tulli Ciceronis Orationes, vol. 1', local='Oxford', editora='Clarendon Press (Oxford Classical Texts)', ano='1908', morte=1937, fonte_morte='https://www.wikidata.org/wiki/Q2637776'),
    'cicero-laelius-de-amicitia': dict(titulo_latino='Laelius de amicitia', editor='William Armistead Falconer', edicao='Cicero, De Senectute, De Amicitia, De Divinatione (Loeb Classical Library)', local='Londres / Nova York', editora='William Heinemann / G. P. Putnam’s Sons', ano='1923', morte=1927, fonte_morte='https://www.wikidata.org/wiki/Q93268573'),
    'cicero-cato-maior-de-senectute': dict(titulo_latino='Cato Maior de senectute', editor='William Armistead Falconer', edicao='Cicero, De Senectute, De Amicitia, De Divinatione (Loeb Classical Library)', local='Londres / Nova York', editora='William Heinemann / G. P. Putnam’s Sons', ano='1923', morte=1927, fonte_morte='https://www.wikidata.org/wiki/Q93268573'),
    'crispus-bellum-catilinae': dict(titulo_latino='Bellum Catilinae (De Catilinae coniuratione)', editor='Axel W. Ahlberg', edicao='C. Sallusti Crispi Catilina, Iugurtha, Orationes et epistulae excerptae de Historiis', local='Leipzig', editora='B. G. Teubner', ano='1919', morte=1951, fonte_morte='https://www.wikidata.org/wiki/Q5543810'),
    'livius-ab-urbe-condita-liber-i': dict(titulo_latino='Ab urbe condita, liber I', editor='Wilhelm Weissenborn e Hermann Johannes Müller', edicao='Titi Livi Ab urbe condita libri', local='Leipzig', editora='B. G. Teubner', ano='1884–1911', morte=1912, fonte_morte='https://www.wikidata.org/wiki/Q18932954 (H. J. Müller, †1912); https://www.wikidata.org/wiki/Q2575612 (W. Weissenborn, †1878)'),
    'maro-bucolica-eclogae': dict(titulo_latino='Bucolica (Eclogae)', editor='J. B. Greenough', edicao='The Bucolics, Aeneid, and Georgics of Virgil', local='Boston', editora='Ginn and Company', ano='1881', morte=1901, fonte_morte='https://www.wikidata.org/wiki/Q6129112'),
    'maro-aeneis-texto-integral': dict(titulo_latino='Aeneis', editor='J. B. Greenough', edicao='The Bucolics, Aeneid, and Georgics of Virgil', local='Boston', editora='Ginn and Company', ano='1881', morte=1901, fonte_morte='https://www.wikidata.org/wiki/Q6129112'),
    'naso-metamorphoses-texto-integral': dict(titulo_latino='Metamorphoses', editor='Hugo Magnus', edicao='P. Ovidi Nasonis Metamorphoseon libri XV', local='Gotha', editora='F. A. Perthes', ano='1892', morte=1924, fonte_morte='https://de.wikipedia.org/wiki/Hugo_Magnus_(Philologe)'),
}
VERIFICADO = '2026-10-18'

def metadados(id_, cfg, raw, aspas, correcoes):
    e = EDICOES[id_]
    av = re.search(r'<availability[^>]*>(.*?)</availability>', raw, re.S)
    decl = ws(re.sub('<[^>]+>', ' ', av.group(1))) if av else ''
    norm = ['Notas do editor e variantes do aparato crítico omitidas (material editorial, não texto latino).',
            'Acréscimos do editor entre ⟨ ⟩, supressões propostas pelo editor entre [ ], lacunas como * * *, como na edição impressa.',
            'Correções de digitalização marcadas pela Perseus (<choice>/<corr>) aplicadas; abreviaturas mantidas como impressas.',
            'Grafia, maiúsculas, u/v, pontuação e ordem do texto mantidas como na edição; nenhuma modernização.',
            'Espaços e quebras de linha do arquivo XML normalizados; numeração de livros, capítulos, seções e versos preservada.']
    if aspas: norm.append('Aspas “ ” recolocadas onde a Perseus codificou citações como <q> e declarou ter retirado as aspas (<quotation marks="none">); falas de vários versos (<q rend="merge">) recebem uma só abertura e um só fechamento.')
    if cfg.get('episodios'): norm.append('Títulos de episódio: os da edição de Magnus (marcos ed="Magnus"); títulos em inglês de outra fonte omitidos.')
    if cfg.get('so_livro'): norm.append(f'Só o livro {cfg["so_livro"]} (o catálogo trata deste livro); as periochae (resumos tardios) omitidas.')
    norm += [c[0].upper() + c[1:] + '.' for c in correcoes]
    return {
        'id': id_, 'titulo_latino': e['titulo_latino'], 'forma': cfg['forma'],
        'edicao': {k: e[k] for k in ('editor', 'edicao', 'local', 'editora', 'ano')},
        'transcricao': {'nome': 'Perseus Digital Library (Tufts University), repositório PerseusDL/canonical-latinLit',
                        'arquivo': BLOB.format(c=COMMIT, p=cfg['tei']), 'commit': COMMIT, 'acessado_em': VERIFICADO},
        'licenca': {'nome': 'CC BY-SA 4.0', 'url': 'https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br',
                    'declaracao': decl or 'Sem declaração no arquivo; vale a licença geral do repositório: “Unless otherwise indicated, all contents of this repository are licensed under a Creative Commons Attribution-ShareAlike 4.0 International License” (README e LICENSE do repositório).'},
        'atribuicao': f'Texto latino: {e["edicao"]}, ed. {e["editor"]} ({e["local"]}: {e["editora"]}, {e["ano"]}). Transcrição digital: Perseus Digital Library, Tufts University (PerseusDL/canonical-latinLit), CC BY-SA 4.0. Adaptação de formato (texto, PDF, EPUB) pela Bibliotheca Latina, distribuída sob a mesma licença CC BY-SA 4.0.',
        'auditoria': {
            '1_autor_e_obra': 'Autor antigo; obra em domínio público.',
            '2_edicao_fonte': f'{e["edicao"]}, ed. {e["editor"]}, {e["local"]}, {e["ano"]} (lida no <sourceDesc> do arquivo TEI).',
            '3_data_e_editor': f'{e["ano"]}; {e["editor"]} (†{e["morte"]}; fonte: {e["fonte_morte"]}).',
            '4_direitos_da_edicao': f'Domínio público no Brasil (editor falecido em {e["morte"]}; Lei 9.610/98, art. 41) e nos EUA (publicada antes de 1931).',
            '5_licenca_da_transcricao': 'CC BY-SA 4.0 (Perseus Digital Library).',
            '6_permissao_de_reproduzir': 'Sim: CC BY-SA 4.0 permite copiar e redistribuir.',
            '7_permissao_de_derivados': 'Sim: CC BY-SA 4.0 permite adaptar (PDF, EPUB), com atribuição e mesma licença.',
            '8_atribuicao_exigida': 'Créditos à Perseus Digital Library e à edição-fonte, link da licença, indicação das mudanças; derivados sob CC BY-SA 4.0.',
        },
        'decisao': 'hospedar', 'downloads': True,
        'omitido': ['notas e aparato crítico do editor', 'introduções, comentários e traduções da edição impressa'],
        'normalizacao': norm, 'verificado_em': VERIFICADO,
    }

ROMAN = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV']

def baixar(p):
    os.makedirs(CACHE, exist_ok=True)
    dest = os.path.join(CACHE, COMMIT[:12] + '-' + os.path.basename(p))
    if not os.path.exists(dest):
        subprocess.run(['curl', '-sfL', '-A', 'BibliothecaLatina/1.0', '-o', dest, RAW.format(c=COMMIT, p=p)], check=True)
    return dest

def ws(s): return re.sub(r'\s+', ' ', s or '').strip()

class Conv:
    def __init__(self, aspas, marcos_secao):
        self.aspas = aspas; self.marcos = marcos_secao
    def inline(self, el):
        """Texto de el e descendentes (sem a cauda de el), aplicando as regras do cabeçalho do módulo."""
        tag = el.tag.replace(T, '')
        if tag in ('note', 'rdg', 'pb', 'lb', 'sic', 'expan', 'reg_skip', 'speaker', 'head', 'bibl', 'figure'):
            return ''
        if tag == 'gap': return ' * * * '
        if tag == 'milestone':
            return f' {{{el.get("n")}}} ' if (self.marcos and el.get('unit') == 'section') else ''
        if tag == 'app':
            lem = el.find(T + 'lem'); return self.inline(lem) if lem is not None else ''
        if tag == 'choice':
            for k in ('corr', 'abbr', 'orig', 'reg'):
                c = el.find(T + k)
                if c is not None: return self.inline(c)
            return ''
        s = el.text or ''
        for ch in el:
            s += self.inline(ch) + (ch.tail or '')
        if tag == 'add': return '⟨' + s.strip() + '⟩'
        if tag == 'del': return '[' + s.strip() + ']'
        if tag == 'q' and self.aspas:   # rend="merge": continuação da citação do verso anterior
            return ('\x03' if el.get('rend') == 'merge' else '\x01') + s.strip() + '\x02'
        return s

def head_of(div):
    h = div.find(T + 'head'); return ws(''.join(h.itertext())) if h is not None else ''

def converter(id_, cfg):
    path = baixar(cfg['tei'])
    raw = open(path, encoding='utf-8').read()
    root = ET.parse(path).getroot()
    aspas = '<quotation marks="none"' in raw
    ed = root.find(f'.//{T}body/{T}div')
    out = []
    marcos = cfg['forma'] == 'prosa' and not ed.findall(f'.//{T}div[@subtype="section"]')
    cv = Conv(aspas, marcos)

    def subdivs(d): return [c for c in d if c.tag == T + 'div' and c.get('type') == 'textpart']

    def prosa_paragrafo(d, ref):
        # um capítulo (ou seção sem subdivisões) vira um parágrafo; seções internas viram marcas {n}
        secs = [s for s in subdivs(d) if s.get('subtype') == 'section']
        if secs:
            partes = []
            for k, s in enumerate(secs):
                t = ws(' '.join(cv.inline(p) for p in s if p.tag in (T + 'p', T + 'l', T + 'lg', T + 'quote')))
                partes.append((f'{{{s.get("n")}}} ' if k else '') + t)
            texto = ' '.join(partes)
        else:
            texto = ws(' '.join(cv.inline(p) for p in d if p.tag in (T + 'p', T + 'lg', T + 'l', T + 'quote', T + 'sp', T + 'said')))
        texto = re.sub(r'\s+([,.;:?!])', r'\1', ws(texto))
        texto = re.sub(r'^\{1\}\s*', '', texto)
        if texto: out.append(f'{ref}\t{texto}')

    def verso(d):
        for el in d:
            tag = el.tag.replace(T, '')
            if tag == 'l':
                t = ws(cv.inline(el))
                if t: out.append(f'{el.get("n") or ""}\t{t}')
            elif tag == 'milestone' and cfg.get('episodios') and el.get('unit') == 'tale' and el.get('n') and el.get('ed') == 'Magnus':
                out.append(''); out.append('## ' + ws(el.get('n')))
            elif tag in ('lg', 'sp', 'q', 'quote', 'said', 'p'):
                if tag == 'sp':
                    sp = el.find(T + 'speaker')
                    if sp is not None: out.append(''); out.append('> ' + ws(''.join(sp.itertext())))
                elif tag == 'lg': out.append('')
                if tag == 'q' and aspas:
                    # citação que abrange vários versos: aspas no primeiro e no último
                    n0 = len(out); verso(el)
                    linhas = [i for i in range(n0, len(out)) if '\t' in out[i]]
                    if linhas:
                        a, b = linhas[0], linhas[-1]
                        r, t = out[a].split('\t', 1); out[a] = f'{r}\t“{t}'
                        r, t = out[b].split('\t', 1); out[b] = f'{r}\t{t}”'
                else:
                    verso(el)

    def walk(d, nivel, refpref):
        for c in subdivs(d):
            st, n = c.get('subtype'), c.get('n') or ''
            if st in ('index',) or (cfg.get('so_livro') and st == 'book' and n != cfg['so_livro']): continue
            if st == 'part' and cfg.get('so_livro'):
                walk(c, nivel, refpref); continue
            h = head_of(c)
            if 'periocha' in h.lower(): continue
            if st in ('book', 'speech', 'poem') or (st == 'chapter' and cfg['forma'] == 'verso'):
                if not h and st == 'book': h = f'{cfg.get("livro", "Liber")} {ROMAN[int(n)] if n.isdigit() and int(n) < len(ROMAN) else n}'
                if not h and st == 'speech': h = f'Oratio {ROMAN[int(n)] if n.isdigit() else n}'
                if not h and st == 'poem': h = n
                lvl = 1 if st in ('book', 'speech') else 2
                if out and out[-1] != '': out.append('')
                out.append('#' * lvl + ' ' + h)
                if cfg['forma'] == 'verso': verso(c)
                walk(c, nivel + 1, (refpref + n + '.') if st in ('book', 'speech') else refpref)
            elif cfg['forma'] == 'prosa' and st in ('chapter', 'section'):
                prosa_paragrafo(c, refpref + n)
            elif cfg['forma'] == 'verso' and st == 'poem':
                verso(c)
    if not subdivs(ed) and cfg['forma'] == 'verso': verso(ed)
    walk(ed, 1, '')
    # Divisão de capítulo ausente no TEI (ex.: Salústio, Cat. 54 dentro do 53): se a numeração das seções recomeça
    # em {1} no meio de um parágrafo e o capítulo seguinte não existe, separa ali. Só muda a divisão, não o texto.
    correcoes = []
    refs = {l.split('\t')[0] for l in out if '\t' in l}
    for i, l in enumerate(list(out)):
        if '\t' not in l or cfg['forma'] != 'prosa': continue
        ref, t = l.split('\t', 1)
        m = re.search(r' \{1\} ', t)
        if not m: continue
        pre, num = (ref.rsplit('.', 1) + [''])[:2] if '.' in ref else ('', ref)
        if not num.isdigit(): continue
        prox = (pre + '.' if pre else '') + str(int(num) + 1)
        if prox in refs: continue
        k = out.index(l)
        out[k:k + 1] = [f'{ref}\t{t[:m.start()]}', f'{prox}\t{t[m.end():]}']
        refs.add(prox); correcoes.append(f'capítulo {prox} separado do {ref} (divisão ausente no arquivo TEI)')
    txt = '\n'.join(out).strip() + '\n'
    # aspas: fecha só onde a citação não continua no verso seguinte (<q rend="merge">)
    txt = re.sub(r'\x02(\n[^\t\n]*\t)\x03', r'\1', txt)
    txt = txt.replace('\x01', '“').replace('\x03', '“').replace('\x02', '”')
    txt = re.sub(r'\n{3,}', '\n\n', txt)
    return txt, aspas, correcoes, raw

def main():
    ids = sys.argv[1:] or list(OBRAS)
    for id_ in ids:
        cfg = OBRAS[id_]
        txt, aspas, correcoes, raw = converter(id_, cfg)
        d = os.path.join(ROOT, 'textos', id_); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'texto.txt'), 'w', encoding='utf-8').write(txt)
        json.dump(metadados(id_, cfg, raw, aspas, correcoes), open(os.path.join(d, 'metadata.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        n_l = sum(1 for l in txt.splitlines() if '\t' in l)
        if correcoes: print('  ', '; '.join(correcoes))
        print(f'{id_}: {n_l} {"versos" if cfg["forma"] == "verso" else "parágrafos"}, {len(txt.split())} palavras, aspas={aspas}')

if __name__ == '__main__': main()
