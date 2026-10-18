# Política de licenças e direitos autorais

Este documento é a política oficial do projeto Bibliotheca Latina e o registro das decisões de direitos. O registro recurso a recurso está em `data/auditoria-direitos.csv`, gerado automaticamente a partir de `data/catalogo.json` (campos `license`, `license_url`, `rights_status`, `hosting_allowed`, `rights_note`, `last_verified`).

## Princípios

1. **Acesso gratuito não é permissão de redistribuição.** Um arquivo que se pode baixar de graça continua protegido se a fonte não declarar uma licença.
2. **O domínio público do autor antigo não cobre a versão moderna.** Edições críticas, comentários, vocabulários, traduções, adaptações e gravações têm direitos próprios. A avaliação é feita para a versão específica indicada pelo `source_url`.
3. **Dois regimes de prazo.** Brasil (Lei 9.610/1998, art. 41): 70 anos contados de 1º de janeiro do ano seguinte à morte do autor; para obras em coautoria, da morte do último coautor. Estados Unidos (onde estão Project Gutenberg, Internet Archive, Perseus e LibriVox): em geral, obras publicadas há mais de 95 anos (hoje, antes de 1931) ou com declaração expressa de domínio público. Quando os regimes divergem, o catálogo registra a divergência em `rights_note` e o recurso aparece só como link.
4. **Na dúvida, link.** Recursos sem declaração de direitos localizável recebem `rights_status = unverified` e `hosting_allowed = false`.
5. **Só hospedamos texto auditado, obra a obra.** A seção *Ler aqui* (`docs/leituras/`) traz o texto latino de obras cuja edição exata e cuja transcrição digital foram verificadas como livres para redistribuir e adaptar (ver "Textos hospedados", abaixo). Tudo o mais continua como link. Nenhum áudio é hospedado. O campo `hosting_allowed` do catálogo registra a avaliação da fonte indicada no catálogo; a decisão de hospedar é registrada em `textos/<id>/metadata.json`.
6. **Materiais comerciais só como referência**, com link para a página oficial da editora e sem reprodução de conteúdo.

## Categorias de situação (`rights_status`)

| Valor | Critério | Pode hospedar? |
|---|---|---|
| `public_domain` | Texto e edição em domínio público nos dois regimes, ou declaração expressa de domínio público pela fonte (ex.: LibriVox) | Sim, em tese |
| `creative_commons` | Licença CC declarada na fonte; a versão exata é registrada em `license` | Só CC BY, BY-SA e CC0 |
| `open_access_limited` | Leitura gratuita, mas sem licença de redistribuição ou com cláusula NC/ND | Não |
| `commercial` | Obra à venda | Não |
| `unverified` | Sem declaração de direitos localizável | Não |

## Fontes e decisões por fonte

| Fonte | O que diz a fonte | Decisão |
|---|---|---|
| Dickinson College Commentaries | Conteúdo sob Creative Commons (versão registrada por recurso) | Link. Cópia seria permitida nos termos da licença; não exercida |
| Open Book Publishers | Cada livro traz sua licença CC (BY, BY-NC-ND etc.) | Link para a página do livro; PDF só quando a própria editora o oferece gratuitamente |
| Project Gutenberg | Domínio público nos EUA + Project Gutenberg License | Link. Para cada obra registramos o ano de morte do autor/editor para o regime brasileiro |
| Internet Archive | Fac-símiles de livros antigos; o campo de direitos varia por item | Link. Só incluímos itens cujo autor/editor morreu há mais de 70 anos ou publicados antes de 1931 com indicação de domínio público; os demais ficam em `data/candidatos.json` |
| Latin Wikisource | Transcrições de obras em domínio público; contribuições CC BY-SA 4.0 | Link |
| Perseus Digital Library | Site: CC BY-SA 3.0 US no rodapé de cada texto. Repositório PerseusDL/canonical-latinLit (GitHub): CC BY-SA 4.0 ("Unless otherwise indicated", README e LICENSE), com declaração no próprio arquivo TEI em parte dos textos | Link; e fonte das transcrições de *Ler aqui* (arquivos TEI fixados num commit) |
| Corpus Corporum | Textos de edições antigas (Patrologia Latina etc.); termos registrados por recurso | Link |
| Corpus Thomisticum | Termos próprios registrados por recurso | Link |
| LibriVox | Gravações em domínio público (declaração do projeto) | Link para a página do projeto; nenhum áudio hospedado |
| Hackett Publishing (LLPSI) | Obras comerciais | Referência com link oficial; nenhum conteúdo reproduzido |

## Textos hospedados (*Ler aqui*)

Cada obra hospedada tem uma pasta `textos/<id>/` (o `id` é o do catálogo) com `texto.txt` (só o texto latino) e `metadata.json` (edição, transcrição, licença, atribuição, alterações e auditoria). O build recusa uma obra sem os oito pontos da auditoria ou sem `decisao = "hospedar"`.

Auditoria obrigatória antes de importar:

1. Autor e obra originais.
2. Edição exata usada pela transcrição (lida no próprio arquivo, não suposta).
3. Data da edição e editor, com o ano de morte do editor e a fonte dessa informação.
4. Situação da edição: domínio público no Brasil (editor falecido há mais de 70 anos, Lei 9.610/98, art. 41) e nos EUA (publicada antes de 1931).
5. Licença da transcrição digital (o autor antigo em domínio público não basta: a transcrição precisa de licença que permita redistribuir).
6. Permissão de reproduzir o texto.
7. Permissão de gerar formatos derivados (página, PDF, EPUB).
8. Atribuição exigida.

Regras de importação: só o texto latino; notas, aparato crítico, introduções, comentários e traduções da edição não são reproduzidos. A grafia, a pontuação e a ordem são as da edição; os sinais editoriais da própria edição (⟨ ⟩ acréscimos, [ ] supressões, * * * lacunas) são mantidos; toda normalização fica listada em `metadata.json → normalizacao` e aparece na página de leitura, no PDF e no EPUB. Se a reutilização não for clara, a obra fica só como link.

Primeiro lote (2026-10-18): dez obras da Perseus Digital Library (repositório `PerseusDL/canonical-latinLit`, commit `128a05a`, CC BY-SA 4.0), importadas por `ferramentas/importar_perseus.py`. Edições e editores (ano de morte conferido no Wikidata/Wikipédia): Fedro, ed. L. Mueller, Teubner 1876 (†1898); César, ed. T. Rice Holmes, Oxford 1914 (†1933); Cícero, *In Catilinam*, ed. A. C. Clark, Oxford 1908 (†1937); Cícero, *De amicitia* e *De senectute*, ed. W. A. Falconer, Loeb 1923 (†1927); Salústio, *Catilina*, ed. A. W. Ahlberg, Teubner 1919 (†1951); Tito Lívio, livro I, ed. W. Weissenborn e H. J. Müller, Teubner 1884–1911 (†1878, †1912); Virgílio, *Bucolica* e *Aeneis*, ed. J. B. Greenough, Ginn 1881 (†1901); Ovídio, *Metamorphoses*, ed. H. Magnus, Perthes 1892 (†1924). As páginas de leitura, os PDF e os EPUB dessas obras são distribuídos sob CC BY-SA 4.0, com atribuição à Perseus e à edição-fonte.

Segundo lote (2026-10-18): mais 46 obras do mesmo repositório e commit (56 no total), sete delas já no catálogo (Catulo, Horácio *Carmina* e *Epodi*, Nepos, *Agricola*, *Amores* I, *De officiis*, *Somnium Scipionis*) e 39 novas no catálogo, cada uma com ficha no Perseus Catalog como fonte. Editores e anos de morte: Merrill (†1936), Shorey (†1934) e Laing (†1945), Vollmer (†1923), Fleckeisen (†1899) e Halm (†1882), Furneaux (†1900), Ehwald (†1927), W. Miller (†1949), C. F. W. Müller (†1903), du Pontet (†1948), Fisher (†1916), Ihm (†1909), Clark (†1937), Plasberg (†1924), Wilkins (†1905), Schiche (†1950), Purser (†1932), Leo (†1914), Postgate (†1926), Ramsay (†1921), Heseltine (†1952), Rouse (†1950), Gaselee (†1943), Peiper (†1898), Rolfe (†1943), Kempf (†1894), Forster (†1950), Krohn (†1941), Fairclough (†1938), Evelyn-White (†1924), C. Smart (†1771). Sem data de morte registrada, mas necessariamente falecidos muito antes de 1956: E. St. J. Parry (Terêncio, edição de 1857), K. H. Weise (Lucano, nascido em 1787), E. Hedicke (Cúrcio, nascido em 1840) e G. Richter (Sêneca, coeditor desde 1867); a auditoria de cada obra diz isso em vez de inventar um ano.

Excluídas por direitos ou por fonte incerta, mesmo estando no repositório da Perseus: edições de editores falecidos depois de 1955 (Apuleio, *Apologia* e *Florida*, ed. Helm †1966; Cícero, *Tusculanae*, ed. Pohlenz †1962; Sêneca, *De clementia*, ed. Basore †1959, e *Epistulae*, ed. Gummere †1969; *Historia Augusta*, ed. Magie †1960; Agostinho, cartas, ed. Baxter †1973), Estácio (data de morte do editor Mozley não confirmada), Propércio (transcrição de origem sem licença, The Latin Library) e as cartas de Plínio e as *Historiae* de Tácito (arquivos sem edição identificada).

Conferência de integridade: o importador compara as palavras do corpo de cada TEI (menos o que as regras omitem) com as do `texto.txt`. Nas 56 obras não há palavra perdida nem acrescentada; as diferenças restantes são uniões corretas de palavras partidas por quebra de página ou por marcação (ex.: *memi|nisti*, *uter|que*), as 31 passagens em grego convertidas de Beta Code para letras gregas e as correções documentadas em cada obra (13 casos de letra duplicada em Gélio; duas saudações de carta em Cícero).

## Licenças do próprio projeto

- Código (HTML, CSS, JS, scripts Python): MIT (`LICENSE`).
- Livro digital *Elementa Linguae Latinae* (`conteudo/`, publicado em `docs/aprenda/`): texto original do projeto, CC BY 4.0. Regra editorial: explicações, exemplos e exercícios são redigidos para o livro; não se copia, transcreve, parafraseia nem adapta cursos de terceiros (incluindo materiais comerciais em português). Fatos gramaticais são de domínio comum e podem ser conferidos nas gramáticas de referência do catálogo; citações de textos antigos são sempre de obras em domínio público, com a fonte indicada. Cada lição declara `direitos.tipo` (`original`, `dominio_publico` ou `adaptacao_autorizada`) e traz um bloco de créditos (autoria, fontes consultadas, educadores externos, adaptações autorizadas, leituras). Referências a aulas públicas de outros educadores ("Aulas complementares") são links com atribuição, sem reprodução de conteúdo e sem implicar endosso ou coautoria. Adaptações de terceiros só entram com permissão registrada em `conteudo/permissoes.json` (status `concedida`); o build recusa o contrário. Detalhes em `conteudo/FLUXO-EDITORIAL.md`.
- Textos do site, guia de leitura em PDF, planilha e dados do catálogo (`data/`, `docs/dados/`): CC BY 4.0.
- Textos latinos de *Ler aqui* (`textos/`, `docs/leituras/`, `docs/downloads/textos/`): a licença da transcrição de origem (no primeiro lote, CC BY-SA 4.0), indicada em cada obra.
- Classificações de etapa e dificuldade são estimativas editoriais, não medidas científicas, e são distribuídas sob a mesma licença CC BY 4.0.

## Pedidos de correção ou retirada

Titulares de direitos podem abrir uma issue no repositório ou escrever ao mantenedor. O recurso é retirado ou corrigido com prioridade; a decisão fica registrada neste documento e no CSV de auditoria.

## Histórico de decisões

- 2026-10-18 — *Ler aqui*: primeiras dez obras hospedadas (Perseus, CC BY-SA 4.0), com PDF e EPUB, após auditoria de oito pontos por obra. O princípio 5 deixa de ser "nenhum texto hospedado".
- 2026-10-13 — Seção Aprenda Latim: livro original *Elementa Linguae Latinae* sob CC BY 4.0, três lições iniciais.
- 2026-10-13 — Versão inicial. Nenhum texto ou áudio hospedado; 100% do catálogo em modo link. Materiais LLPSI (Hackett) incluídos como referência comercial.
