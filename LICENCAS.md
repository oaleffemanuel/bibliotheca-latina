# Política de licenças e direitos autorais

Este documento é a política oficial do projeto Bibliotheca Latina e o registro das decisões de direitos. O registro recurso a recurso está em `data/auditoria-direitos.csv`, gerado automaticamente a partir de `data/catalogo.json` (campos `license`, `license_url`, `rights_status`, `hosting_allowed`, `rights_note`, `last_verified`).

## Princípios

1. **Acesso gratuito não é permissão de redistribuição.** Um arquivo que se pode baixar de graça continua protegido se a fonte não declarar uma licença.
2. **O domínio público do autor antigo não cobre a versão moderna.** Edições críticas, comentários, vocabulários, traduções, adaptações e gravações têm direitos próprios. A avaliação é feita para a versão específica indicada pelo `source_url`.
3. **Dois regimes de prazo.** Brasil (Lei 9.610/1998, art. 41): 70 anos contados de 1º de janeiro do ano seguinte à morte do autor; para obras em coautoria, da morte do último coautor. Estados Unidos (onde estão Project Gutenberg, Internet Archive, Perseus e LibriVox): em geral, obras publicadas há mais de 95 anos (hoje, antes de 1931) ou com declaração expressa de domínio público. Quando os regimes divergem, o catálogo registra a divergência em `rights_note` e o recurso aparece só como link.
4. **Na dúvida, link.** Recursos sem declaração de direitos localizável recebem `rights_status = unverified` e `hosting_allowed = false`.
5. **Nesta versão não hospedamos nenhum texto nem áudio.** Mesmo onde a licença permitiria (domínio público, CC BY, CC BY-SA), preferimos o link: a fonte mantém o texto corrigido e merece a visita. O campo `hosting_allowed` registra a avaliação para uso futuro, mas não é exercido.
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
| Perseus Digital Library | Textos sob CC BY-SA (versão registrada por recurso) | Link |
| Corpus Corporum | Textos de edições antigas (Patrologia Latina etc.); termos registrados por recurso | Link |
| Corpus Thomisticum | Termos próprios registrados por recurso | Link |
| LibriVox | Gravações em domínio público (declaração do projeto) | Link para a página do projeto; nenhum áudio hospedado |
| Hackett Publishing (LLPSI) | Obras comerciais | Referência com link oficial; nenhum conteúdo reproduzido |

## Licenças do próprio projeto

- Código (HTML, CSS, JS, scripts Python): MIT (`LICENSE`).
- Livro digital *Elementa Linguae Latinae* (`conteudo/`, publicado em `docs/aprenda/`): texto original do projeto, CC BY 4.0. Regra editorial: explicações, exemplos e exercícios são redigidos para o livro; não se copia, transcreve, parafraseia nem adapta cursos de terceiros (incluindo materiais comerciais em português). Fatos gramaticais são de domínio comum e podem ser conferidos nas gramáticas de referência do catálogo; citações de textos antigos são sempre de obras em domínio público, com a fonte indicada. Cada lição declara `direitos.tipo` (`original`, `dominio_publico` ou `adaptacao_autorizada`) e traz um bloco de créditos (autoria, fontes consultadas, educadores externos, adaptações autorizadas, leituras). Referências a aulas públicas de outros educadores ("Aulas complementares") são links com atribuição, sem reprodução de conteúdo e sem implicar endosso ou coautoria. Adaptações de terceiros só entram com permissão registrada em `conteudo/permissoes.json` (status `concedida`); o build recusa o contrário. Detalhes em `conteudo/FLUXO-EDITORIAL.md`.
- Textos do site, guia de leitura em PDF, planilha e dados do catálogo (`data/`, `docs/dados/`): CC BY 4.0.
- Classificações de etapa e dificuldade são estimativas editoriais, não medidas científicas, e são distribuídas sob a mesma licença CC BY 4.0.

## Pedidos de correção ou retirada

Titulares de direitos podem abrir uma issue no repositório ou escrever ao mantenedor. O recurso é retirado ou corrigido com prioridade; a decisão fica registrada neste documento e no CSV de auditoria.

## Histórico de decisões

- 2026-10-13 — Seção Aprenda Latim: livro original *Elementa Linguae Latinae* sob CC BY 4.0, três lições iniciais.
- 2026-10-13 — Versão inicial. Nenhum texto ou áudio hospedado; 100% do catálogo em modo link. Materiais LLPSI (Hackett) incluídos como referência comercial.
