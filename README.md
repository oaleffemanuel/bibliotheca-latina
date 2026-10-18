# Bibliotheca Latina

*Ab initiis ad fontes.* Uma biblioteca digital gratuita e curada para quem estuda latim: 145 recursos verificados, 56 deles com o texto latino integral para ler no próprio site, organizados em sete etapas de leitura, das primeiras palavras aos autores romanos, aos Padres da Igreja e à escolástica medieval. Inclui um guia de leitura em PDF e uma planilha de acompanhamento.

🌐 **Site (quando publicado):** https://oaleffemanuel.github.io/bibliotheca-latina/

Para quem só quer ler, basta o site. Não precisa de conta nem de saber usar o GitHub.

## O que tem aqui

| | |
|---|---|
| [Aprenda Latim](docs/aprenda/index.html) | *Elementa Linguae Latinae*: livro digital original em português, em quatro partes (Fundamenta, Grammatica, Lectio, Auctores). Lições com objetivos, exemplos em latim, tabelas, diagramas, exercícios com resposta e leituras do catálogo. 54 capítulos em três níveis (essencial, intermediário, avançado), todos disponíveis, com botão "Reportar problema" por e-mail em cada capítulo. A situação editorial interna e as pendências de revisão ficam em `conteudo/` (ver `FLUXO-EDITORIAL.md` §8 e `AUDITORIA-GERAL.md`); o site mostra uma nota editorial única na página Sobre; capítulo-modelo: 3, *Dē cāsibus*. |
| [Catálogo](docs/catalogo.html) | 145 recursos com busca e filtros por etapa, período histórico, gênero, dificuldade, áudio, formato, fonte, gratuito/comercial e "Ler aqui". No celular, os filtros ficam recolhidos atrás do botão "Filtros"; a busca fica sempre visível. Marcação de "Quero ler", "Lendo" e "Lido" salva no navegador. |
| [Ler aqui](docs/leituras/index.html) | Textos latinos integrais para ler no próprio site (56 obras: César, Cícero, Salústio, Tito Lívio, Tácito, Suetônio, Virgílio, Horácio, Ovídio, Catulo, Plauto, Terêncio, Sêneca, Juvenal, Petrônio, Apuleio e outros), com ajuste de letra, largura e aparência, ponto de leitura salvo no navegador, fonte e licença visíveis, e PDF e EPUB gerados. Obras longas têm uma página por livro. |
| [Percurso de leitura](docs/percurso.html) | As sete etapas, o teste "onde começar", o método e dicas para quem fala português. |
| [Recursos de estudo](docs/recursos.html) | Métodos, gramáticas, dicionários e ferramentas, com notas sobre pronúncia. |
| [Guia de leitura (PDF)](docs/downloads/guia-de-leitura-bibliotheca-latina.pdf) | O percurso completo em PDF. |
| [Diário de leitura (XLSX)](docs/downloads/diario-de-leitura-bibliotheca-latina.xlsx) | Planilha com o catálogo, painel de progresso, sessões, vocabulário com revisão espaçada e *summaria*. |
| [Dados abertos](docs/dados/) | Catálogo em JSON e CSV e o registro de auditoria de direitos. |

### As sete etapas

| Etapa | Nome | O que é |
|---|---|---|
| I | *Prima Verba* | Palavras e frases elementares; primeiros capítulos de um método |
| II | *Primae Fabulae* | Narrativas curtas graduadas, escritas para estudantes |
| III | *Fundamenta* | Leituras longas com gramática progressivamente mais complexa |
| IV | *Ad Fontes* | Primeiros textos latinos autênticos, com comentário |
| V | *Auctores Romani* | Literatura clássica romana |
| VI | *Latinitas Christiana* | Vulgata, Padres da Igreja, liturgia e espiritualidade |
| VII | *Sapientia Mediaevalis* | Latim medieval e escolástico |

As etapas são caminhos sugeridos, não uma escala universal de dificuldade: VI e VII são percursos paralelos que podem começar a partir da etapa III. Cada recurso recebe uma nota de dificuldade independente (1 a 5) e é identificado como original, adaptado, simplificado ou didático. Não usamos níveis A1–C2.

## Direitos autorais

Acesso gratuito não é permissão para redistribuir. Por isso:

- **Só textos auditados são hospedados.** A seção *Ler aqui* (`docs/leituras/`) traz o texto latino integral de obras cuja edição e transcrição permitem redistribuir e adaptar (56 obras da Perseus Digital Library, CC BY-SA 4.0), com PDF e EPUB. Cada obra tem `textos/<id>/texto.txt` e `metadata.json` com a auditoria de direitos. Todos os demais recursos são links para a página oficial da fonte (Perseus, Dickinson College Commentaries, Open Book Publishers, Project Gutenberg, Internet Archive, Latin Wikisource, Corpus Corporum, LibriVox e outras). Nenhum áudio é hospedado.
- Cada recurso registra licença, endereço da declaração de direitos, situação (domínio público, Creative Commons, acesso aberto limitado, comercial, não verificado) e data da última verificação.
- Os livros do método *Lingua Latina per se Illustrata* aparecem como referência comercial, com link para a Hackett Publishing, sem reprodução de conteúdo.
- A política completa está em [`LICENCAS.md`](LICENCAS.md); o registro recurso a recurso, em [`data/auditoria-direitos.csv`](data/auditoria-direitos.csv); os candidatos ainda não verificados, em [`data/candidatos.json`](data/candidatos.json).

É titular de direitos e quer corrigir ou retirar algo? Abra uma issue.

## Licenças deste projeto

- **Código** (HTML, CSS, JS, scripts): [MIT](LICENSE).
- **Textos do site, guia, planilha e dados do catálogo:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt_BR).
- **Recursos listados:** seguem a licença de cada fonte.

## Para quem mantém o projeto

O site é HTML, CSS e JavaScript puro, sem framework e sem build no servidor, publicado pelo GitHub Pages a partir da pasta `docs/`.

```
data/catalogo.json            fonte única de verdade do catálogo
data/candidatos.json          recursos conhecidos mas ainda não verificados (aparecem na página "Sobre")
data/auditoria-direitos.csv   registro de direitos (gerado)
ferramentas/construir.py      gera as páginas, o livro Aprenda Latim, o leitor, o PDF, a planilha, o CSV/JSON, a auditoria e o sitemap
ferramentas/leituras.py       leitor interno: lê textos/, gera as páginas de leitura, os PDF e os EPUB
ferramentas/importar_perseus.py importa textos da Perseus (TEI, commit fixo) para textos/<id>/ com metadata.json
textos/<id>/                  texto.txt (só o texto latino) e metadata.json (edição, licença, auditoria, alterações)
conteudo/livro.py             estrutura do livro Elementa Linguae Latinae (partes e lições planejadas)
conteudo/licoes/lNN_*.py      uma lição por módulo (dicionário LICAO); conteudo/util.py tem os construtores de tabela, paradigma, exemplos, diagrama, observação e exercício
conteudo/FLUXO-EDITORIAL.md   estados das lições, tipos de conteúdo, permissões, créditos e o padrão de capítulo
conteudo/SUMARIO-EDITORIAL.md sumário definitivo (54 capítulos), cobertura e progressão de pré-requisitos
conteudo/revisoes/            relatórios de revisão gramatical dos capítulos
conteudo/permissoes.json      registro de permissões de material de terceiros (nenhuma concedida até agora)
ferramentas/pesquisa/         pesquisa de fontes (JSON verificados por fonte), camada editorial (ed_*.py) e merge.py, que regenera data/catalogo.json
docs/                         o site publicado
  assets/                     style.css, app.js, favicon.svg
  aprenda/                    índice do livro e uma página por lição
  downloads/                  guia (PDF) e planilha (XLSX); textos/ tem os PDF e EPUB de Ler aqui e o manifesto
  leituras/                   páginas de leitura (geradas por inteiro a cada build)
  dados/                      catálogo em CSV e JSON + auditoria
LICENCAS.md                   política de direitos e histórico de decisões
```

### Rodar localmente

```bash
python3 -m http.server 8000 --directory docs
# abra http://localhost:8000/
```

### Editar o catálogo

Há dois caminhos. Para um ajuste pontual, edite `data/catalogo.json` diretamente. Para incluir recursos novos de forma auditável, acrescente o registro verificado (URL, licença, `license_url`, data) ao JSON da fonte em `ferramentas/pesquisa/` e a classificação editorial (etapa, dificuldade, descrição) ao `ed_*.py` correspondente; depois rode `python3 ferramentas/pesquisa/merge.py`, que reescreve `data/catalogo.json`. Em qualquer caso, edite `data/catalogo.json`. Cada recurso é um objeto com os campos listados em `docs/dados/catalogo.json` (os mesmos nomes). Campos obrigatórios e valores permitidos são validados pelo script:

- `reading_stage`: 1 a 7 · `difficulty`, `vocabulary_difficulty`, `morphology_difficulty`, `syntax_difficulty`: 1 a 5 ou `null`
- `historical_period`: Clássico · Pós-clássico · Tardio e patrístico · Medieval · Renascentista e neolatino · Moderno (material didático)
- `category`: Leitura · Gramática e referência · Método e curso · Ferramenta · Referência comercial
- `original_or_adapted`: original · adaptado · simplificado · didatico
- `rights_status`: public_domain · creative_commons · open_access_limited · commercial · unverified
- `formats_available`: html, pdf, epub, txt, xml, audio, print
- `hosting_allowed` só pode ser `true` com `rights_status` public_domain ou creative_commons; `free: false` exige `rights_status: commercial`; `audio_available: true` exige `audio_url`.

Regras editoriais: nunca inventar URL, licença ou áudio; registrar `license_url` e `last_verified`; descrever em `description_pt_br` o que realmente está no link; dizer se o texto é original, adaptado, simplificado ou didático.

### Escrever uma lição do Aprenda Latim

O fluxo completo (estados `planejada` → `rascunho` → `revisada` → `publicada`, tipos de conteúdo, permissões de terceiros, componente de créditos) está em [`conteudo/FLUXO-EDITORIAL.md`](conteudo/FLUXO-EDITORIAL.md). Resumo:

1. Em `conteudo/livro.py`, localize a lição planejada e acrescente `modulo='lNN_slug'` ao seu dicionário.
2. Crie `conteudo/licoes/lNN_slug.py` com um dicionário `LICAO` (use os capítulos 3, 5 e 9 como modelo): `slug`, `titulo`, `tempo`, `resumo`, `status`, `objetivos`, `topicos`, `prerequisitos`, `secoes` (lista de pares título/HTML, com os construtores de `conteudo/util.py`: `tabela`, `tabela_declinacao`, `tabela_conjugacao`, `comparacao`, `exemplos`, `observacao`, `dica`, `diagrama_frase`), `exercicios` (`util.exercicio`, sempre com resposta), `leituras` (ids do catálogo; o build falha se um id não existir), `leituras_nota`, `referencias` (`util.referencia`), `aulas_complementares` (opcional; `util.aula_complementar`, só com URL oficial verificada), `creditos` e `direitos`.
3. Regras: conteúdo original em português, exemplos latinos corretos (com macrons), nada copiado de cursos de terceiros; citações antigas só de obras em domínio público, com a fonte.
4. Rode o script de build. A lição ganha número, navegação anterior/próxima, bloco de créditos e entra no sitemap e no índice de tópicos automaticamente. A situação editorial interna (`rascunho`, `publicada` etc.) não aparece no site.

Materiais privados de pesquisa (cursos de terceiros estudados para planejar o livro) ficam fora deste repositório, e nunca são publicados.

### Acrescentar uma obra ao *Ler aqui*

1. Faça a auditoria de oito pontos descrita em [`LICENCAS.md`](LICENCAS.md#textos-hospedados-ler-aqui): edição exata, editor e ano de morte (com fonte), licença da transcrição, permissão de redistribuir e de gerar PDF/EPUB, atribuição. Na dúvida, a obra fica só como link.
2. Para a Perseus: acrescente a obra a `OBRAS` e `EDICOES` em `ferramentas/importar_perseus.py` (o `id` é o do catálogo) e rode `python3 ferramentas/importar_perseus.py <id>`. Para outra fonte, crie `textos/<id>/texto.txt` no mesmo formato (descrito no início do importador) e um `metadata.json` com os mesmos campos.
3. Rode o build: a página de leitura, o EPUB, o PDF (sem `--sem-pdf`) e as ações "Ler aqui", "Baixar PDF" e "Baixar EPUB" do card aparecem sozinhos. O build recusa obra sem auditoria completa, e um botão de download só aparece se o arquivo existir e corresponder à versão atual do texto (`docs/downloads/textos/manifesto.json`).

### Regenerar o site, o PDF e a planilha

```bash
pip install -r ferramentas/requirements.txt    # weasyprint e openpyxl
python3 ferramentas/construir.py               # --sem-pdf ou --sem-xlsx para pular; --so-publicadas exclui rascunhos do livro
```

No macOS com Homebrew, se o WeasyPrint não encontrar `libgobject`:

```bash
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 ferramentas/construir.py
```

O script valida o catálogo, gera as sete páginas, `docs/dados/`, o sitemap, a planilha e o PDF.

### Publicar no GitHub Pages

1. Crie o repositório público `bibliotheca-latina` na conta `oaleffemanuel` e envie o conteúdo (`main`).
2. Em *Settings → Pages*, escolha *Deploy from a branch*, branch `main`, pasta `/docs`.
3. Aguarde o deploy; o site fica em https://oaleffemanuel.github.io/bibliotheca-latina/ . O arquivo `docs/.nojekyll` já está incluído e todos os links são relativos (a 404 usa `<base href="/bibliotheca-latina/">`).
4. Depois de cada alteração: edite `data/catalogo.json`, rode o script e faça o commit da pasta `docs/` junto.

---

Projeto pessoal e sem fins lucrativos. Não é afiliado a nenhuma das fontes citadas. Irmão da [Biblioteca Italiana](https://github.com/oaleffemanuel/biblioteca-italiana). *Tolle, lege!*
