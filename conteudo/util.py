"""Pequenos construtores de HTML para as lições (tabelas, exemplos, diagramas). Sem dependências."""
import html as _h

def e(s): return _h.escape(str(s), quote=True)

def tabela(cabecalho, linhas, legenda=None, latim_cols=()):
    """cabecalho: lista de strings; linhas: lista de listas; latim_cols: índices das colunas em latim (itálico)."""
    cap = f'<caption>{e(legenda)}</caption>' if legenda else ''
    th = ''.join(f'<th{" class=la" if i in latim_cols else ""}>{c}</th>' for i, c in enumerate(cabecalho))
    rows = ''.join('<tr>' + ''.join(f'<td{" class=la" if i in latim_cols else ""}>{c}</td>' for i, c in enumerate(l)) + '</tr>' for l in linhas)
    return f'<div class="table-scroll"><table>{cap}<thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>'

def exemplos(pares):
    """pares: lista de (latim, português). O latim pode conter <b> para destacar terminações."""
    return '<div class="ex">' + ''.join(f'<div class="la" lang="la">{la}</div><div class="pt">{pt}</div>' for la, pt in pares) + '</div>'

def dica(texto): return f'<div class="dica">{texto}</div>'

def diagrama(svg, legenda=None):
    return f'<figure class="diagrama">{svg}{f"<figcaption>{legenda}</figcaption>" if legenda else ""}</figure>'

def exercicio(titulo, enunciado, itens):
    """itens: lista de (pergunta, resposta). A resposta fica num <details>."""
    li = ''.join(f'<li>{p}<details><summary>Ver resposta</summary><p>{r}</p></details></li>' for p, r in itens)
    return f'<div class="exercicio"><h3>{titulo}</h3><p>{enunciado}</p><ol>{li}</ol></div>'

# ─── diagramas reutilizáveis (SVG inline, cores do tema) ───
def svg_caixas(itens, largura=None, cor='#8a2b1d', seta=True):
    """Fluxo horizontal de caixas com texto (palavra em cima, função embaixo; a função quebra em duas linhas no ' · ')."""
    n = len(itens); bw, gap, h = 172, 18, 118
    w = largura or (n * bw + (n - 1) * gap + 16)
    out = [f'<svg viewBox="0 0 {w} {h}" width="{w}" role="img" aria-label="{e(" → ".join(i[0] for i in itens))}">']
    x = (w - (bw * n + gap * (n - 1))) // 2
    for k, (t, sub) in enumerate(itens):
        parts = [p.strip() for p in sub.split(' · ')] if ' · ' in sub else ([sub] if len(sub) <= 24 else [sub[:sub.rfind(' ', 0, 24)], sub[sub.rfind(' ', 0, 24) + 1:]])
        out.append(f'<rect x="{x}" y="14" width="{bw}" height="{76 if len(parts) > 1 else 62}" rx="6" fill="#fbf8f1" stroke="{cor}" stroke-width="1.5"/>')
        out.append(f'<text x="{x + bw/2}" y="40" text-anchor="middle" font-size="20" font-style="italic" fill="#211c17">{e(t)}</text>')
        for j, p in enumerate(parts[:2]):
            out.append(f'<text x="{x + bw/2}" y="{60 + 15 * j}" text-anchor="middle" font-size="12" font-family="system-ui, sans-serif" fill="#6e665b">{e(p)}</text>')
        if seta and k < n - 1:
            out.append(f'<path d="M{x + bw + 3} 45 h11" stroke="{cor}" stroke-width="2"/><path d="M{x + bw + 9} 39 l6 6 -6 6" fill="none" stroke="{cor}" stroke-width="2"/>')
        x += bw + gap
    out.append('</svg>'); return ''.join(out)

# ─── componentes didáticos (acrescentados na 2ª fase) ───
def observacao(titulo, texto):
    """Caixa 'Observação gramatical' (nuance, exceção, comparação com o português)."""
    return f'<aside class="obs"><b>{e(titulo)}</b><p>{texto}</p></aside>'

def tabela_declinacao(legenda, linhas, casos=('Nominativo', 'Genitivo', 'Dativo', 'Acusativo', 'Vocativo', 'Ablativo'), colunas=('Singular', 'Plural')):
    """Paradigma de declinação. linhas: lista de tuplas (singular, plural[, ...]) na ordem dos casos; use <b> para destacar a terminação."""
    rows = ''.join('<tr>' + f'<th scope="row">{e(c)}</th>' + ''.join(f'<td class="la">{f}</td>' for f in fs) + '</tr>' for c, fs in zip(casos, linhas))
    return f'<div class="table-scroll"><table class="paradigma"><caption>{e(legenda)}</caption><thead><tr><th>Caso</th>{"".join(f"<th>{e(c)}</th>" for c in colunas)}</tr></thead><tbody>{rows}</tbody></table></div>'

def tabela_conjugacao(legenda, formas, pessoas=('1ª sing.', '2ª sing.', '3ª sing.', '1ª pl.', '2ª pl.', '3ª pl.'), colunas=('Latim', 'Português')):
    """Paradigma de conjugação. formas: lista de tuplas na ordem das pessoas, ex. ('am<b>ō</b>', 'eu amo')."""
    rows = ''.join('<tr>' + f'<th scope="row">{e(p)}</th>' + ''.join(f'<td class="{"la" if i == 0 else ""}">{f}</td>' for i, f in enumerate(fs)) + '</tr>' for p, fs in zip(pessoas, formas))
    return f'<div class="table-scroll"><table class="paradigma"><caption>{e(legenda)}</caption><thead><tr><th>Pessoa</th>{"".join(f"<th>{e(c)}</th>" for c in colunas)}</tr></thead><tbody>{rows}</tbody></table></div>'

def comparacao(legenda, cabecalho, linhas):
    """Tabela de comparação (ex.: latim × português, restaurada × eclesiástica). Primeira coluna em latim."""
    return tabela(cabecalho, linhas, legenda, latim_cols=(0,))

def diagrama_frase(palavras, legenda=None):
    """Diagrama de estrutura de frase: lista de (palavra, função). Alias de svg_caixas com legenda."""
    return diagrama(svg_caixas(palavras), legenda)

def aula_complementar(educador, titulo, url, descricao, verificado, atribuicao=None):
    """Referência a uma aula externa pública. Todos os campos são obrigatórios; o build recusa referências sem URL verificada."""
    return dict(educador=educador, titulo=titulo, url=url, descricao=descricao, verificado=verificado, atribuicao=atribuicao)

def referencia(titulo, autor=None, url=None, catalogo=None, nota=None, tipo='obra'):
    """Fonte consultada. tipo: 'dominio_publico' | 'obra' | 'artigo' | 'site'. catalogo = id do catálogo, quando a obra está nele."""
    return dict(titulo=titulo, autor=autor, url=url, catalogo=catalogo, nota=nota, tipo=tipo)

def pratica_guiada(titulo, enunciado, passos, fecho=None):
    """Exercício resolvido passo a passo. passos: lista de (pergunta, resposta); cada resposta fica num <details>."""
    li = ''.join(f'<li>{p}<details><summary>Ver o passo</summary><p>{r}</p></details></li>' for p, r in passos)
    return f'<div class="exercicio guiada"><h3>{titulo}</h3><p>{enunciado}</p><ol class="passos">{li}</ol>{f"<p>{fecho}</p>" if fecho else ""}</div>'

def analise(legenda, linhas):
    """Tabela de análise gramatical palavra a palavra: linhas = (palavra, forma de dicionário, análise, função)."""
    rows = ''.join(f'<tr><td lang="la">{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in linhas)
    return f'<div class="table-scroll"><table class="analise"><caption>{e(legenda)}</caption><thead><tr><th>Palavra</th><th>Dicionário</th><th>Análise</th><th>Função</th></tr></thead><tbody>{rows}</tbody></table></div>'
