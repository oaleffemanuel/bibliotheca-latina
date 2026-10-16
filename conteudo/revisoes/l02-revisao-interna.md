# Revisão interna · Capítulo 2, *Dē sententiā Latīnā* (Como funciona uma frase latina?)

- Data: 2026-10-14 · Tipo: **revisão interna do autor**, feita contra gramáticas de referência. **Não é revisão externa independente**; por isso `creditos.revisao_gramatical` continua vazio e a página mostra "revisão gramatical: pendente".
- Escopo: atualização do capítulo ao padrão de 16 elementos (FLUXO-EDITORIAL.md § 6). Status mantido: `publicada`.
- Fontes conferidas nesta revisão (abertas e lidas, não citadas de memória):
  - Bennett, *New Latin Grammar* (texto local): § 20.1 (o latim não tem artigo), § 166 (sujeito no nominativo), § 172 (objeto direto no acusativo), § 234 (concordância do adjetivo), § 254 (concordância do verbo em número e pessoa), § 348 (ordem normal: sujeito no início, predicado no fim), § 349 (ênfase: no início, "less frequently at the end"), § 350.1 (o genitivo segue o nome de que depende), § 67.a e § 69 (*fortis*: acusativo plural *fortēs* ou *fortīs*).
  - Allen & Greenough, edição DCC: § 21 (língua flexional), §§ 269–274 (oração, sujeito, objeto), § 280 (concordância em geral), § 286 (concordância do adjetivo), § 316 (concordância do verbo), § 339 (sujeito no nominativo), § 387 (objeto direto no acusativo), §§ 595–599 (ordem das palavras; § 596.a verbo no fim; § 597 ênfase, com a análise de *Gallia est omnis dīvīsa*; § 597.b), § 600 (relações expressas pela flexão).
  - Ravizza, *Gramática Latina* (OCR local): § 14 (proposição: sujeito, predicado, complementos).
  - Terêncio, *Phormio* 203, no texto de The Latin Library (*fortis fortuna adiuvat*, numeração de verso conferida na página). O Perseus 1999.02.0117 traz só a tradução inglesa; não serviu para conferir o latim.
  - César, *BG* 1.1 (edição DCC): *Gallia est omnis dīvīsa in partēs trēs*.
  - Vulgata Clementina, Jo 1,1 (Wikisource latina): *In principio erat Verbum, et Verbum erat apud Deum*.
  - L&S (Perseus) não foi necessário; DCC Core Vocabulary conferido para *fortūna* e *fortis*.

## Acréscimos

| Elemento | O que foi acrescentado |
|---|---|
| 1 Título latino | `titulo_latim='Dē sententiā Latīnā'` (igual a `livro.py`). |
| 3 Objetivos | 5º objetivo: número do verbo e raciocínio por exclusão numa frase autêntica. |
| 5 Explicação | Observação "Combinar não é rimar" (concordância pelo gênero; *nauta bonus*); seção 6, "Análise gramatical: uma frase autêntica". |
| 8 Análise | `analise()` de Terêncio, *Phormio* 203: *fortīs fortūna adiuvat* (objeto, sujeito, verbo; decisão por exclusão). |
| 10 Diagrama | O diagrama existente passou de `diagrama(svg_caixas(...))` para `diagrama_frase()` (mesma saída; componente padrão). |
| 11 Erros comuns | 5 itens. |
| 12 Prática guiada | 2: *Fīliam agricola laudat* (objeto na frente); *Magistrum puerī audiunt* (função de forma desconhecida por exclusão). |
| 13–14 Exercícios | Exercício 4 (transformação: ordem e número) e Exercício 5 (retroversão). Total: 5 conjuntos, respostas explicadas. |
| 16 Referências | Bennett e Ravizza acrescentados; A&G com parágrafos conferidos; Terêncio acrescentado (sem id de catálogo; não há Terêncio no catálogo). |

## Correções feitas

| Antes | Problema | Depois |
|---|---|---|
| A&G "§ 280 (concordância do verbo)" | **Número errado**: § 280 é a concordância em geral; a do verbo é § 316. | § 316 (verbo), § 286 (adjetivo), além de §§ 21, 339, 387, 595–599, 600. |
| A&G "§§ 595–601 (ordem das palavras)" | §§ 600–601 tratam da estrutura do período. | §§ 595–599 (ordem) e § 600 (flexão). |
| "Mudar a ordem serve para dar ênfase: o que vem primeiro ou por último chama atenção." | Impreciso: Bennett § 349 põe a ênfase sobretudo no início e "less frequently" no fim; A&G § 597.b é ainda mais restritivo. | "O lugar de maior destaque é o começo ...; o fim também pode receber ênfase, mas com bem menos frequência." |
| "a poesia latina consegue separar adjetivo e substantivo por versos inteiros" | Exagero. | "afastar o adjetivo do seu substantivo, às vezes com várias palavras no meio". |
| "*magistrī*: ... o genitivo, que você verá na próxima lição" | O capítulo 3 apresenta o genitivo, mas a terminação *-ī* é do capítulo 5. | Remete ao capítulo 3 (caso) e ao capítulo 5 (terminação). |
| "algumas palavras em *-us* têm essa forma [*puer*], e você as verá na lição sobre a segunda declinação" | Formulação confusa (*puer* não termina em *-us*) e sem o número do capítulo. | "algumas palavras do grupo de *Marcus* têm o nominativo em *-er*, ... capítulo 5". |
| Prévia de *amāre* sem remissão | Faltava o número do capítulo. | "o capítulo 6 apresenta o presente de todos os verbos". |
| "Lição 1", "próxima lição", "desta lição" | Terminologia e numeração de `livro.py`. | "Capítulo 1", "próximo capítulo", "deste capítulo". |

Numeração conferida em `conteudo/livro.py`: casos = 3, primeira declinação = 4, segunda declinação = 5, presente = 6, terceira declinação, adjetivos de segunda classe = 10.

## Verificações

- **Morfologia**: *Marcus/Marcum*, *Iūlia/Iūliam*, *puella/puellae*, *rosās*, *servus/servum*, *magister/magistrum*, *puer/puerum*, *agricola/agricolam*, presente de *amāre* (Bennett, A&G); *fortīs* acusativo plural (Bennett §§ 67.a, 69; A&G § 597 imprime *partīs trīs* em César).
- **Sintaxe**: sujeito no nominativo e objeto no acusativo (Bennett §§ 166, 172; A&G §§ 339, 387); concordância verbo–sujeito em número em todas as frases (*-t*/*-nt*), conferida item a item, inclusive nas transformações do Exercício 4.
- **Ordem das palavras**: tendência S–O–V e verbo no fim (Bennett § 348; A&G § 596.a); genitivo depois do nome (Bennett § 350.1), coerente com *fīliam magistrī*, *villam dominae*.
- **Terêncio**: leitura "a sorte ajuda os corajosos" (objeto *fortīs*, sujeito *fortūna*) é a tradicional; a alternativa "a sorte corajosa ajuda" é excluída porque deixaria *adiuvat* sem objeto e *fortīs* não concorda em número com *fortūna*.
- **Traduções**: artigos escolhidos pelo português; a ênfase indicada quando a ordem latina a sugere.
- **Macrons**: *Iūlia, amās, amāmus, amātis, dīvīsa, partēs, trēs, prīncipiō, fīlia, magistrī, dēlectant, ōrnant, lūna, fortīs, fortūna*.

## Pendências

- Revisão externa por um latinista independente.
- O Exercício 1 e o 3 usam *puerī* e *servī* (nominativo plural da 2ª declinação) antes do capítulo 5; o enunciado e as respostas explicam pelo verbo plural, e a prática guiada 2 transforma essa antecipação em exercício de exclusão. Avaliar se convém trocar por nomes da 1ª declinação.
- `direitos.tipo` mantido como `original` (padrão do capítulo 3), apesar das citações curtas em domínio público.

## Auditoria geral (2026-10-15)

- Tipo: **auditoria interna assistida por IA** (lote A, caps. 1–6), feita contra as fontes abertas nesta sessão. **Não é revisão humana nem revisão externa**: `creditos.revisao_gramatical` continua vazio e o status não mudou.
- Convenções aplicadas: FLUXO-EDITORIAL.md § 7 (inclusive § 7.2 corrigido: *hīc, haec, hōc*; não há formas desse pronome neste capítulo).

**Fontes abertas:** A&G § 597 (DCC, `order-words`: a frase de César está no § 597, com a nota "Divided: opposed to the false conception..." e o texto *partīs trīs*); Bennett §§ 20.1, 67.a, 69, 166, 172, 234, 254, 348–350; Ravizza n. 14; Terêncio, *Phormio* 203 na The Latin Library (*fortis fortuna adiuvat*, verso 203 conferido pela numeração) e na ed. E. St. J. Parry (Londres, 1857; PerseusDL `phi0134.phi004.perseus-lat2`: *Fortes fortuna adiuvat*); César, *BG* 1.1.1, ed. Holmes 1914 (*partes tres*); Vulgata Clementina Jo 1,1.

**Correções:**
- *Marcus/Marcum/Marce* → *Mārcus/Mārcum/Mārce* (A&G, Bennett e Georges marcam *Mārcus*; L&S cita a grafia epigráfica MAARCVS). Uniformiza com os caps. 5 e 6.
- Variante de Terêncio documentada (texto da The Latin Library *fortīs*; Parry *fortes*) na análise e na referência; edição de César identificada (Holmes) em vez de "edição DCC".
- Formato de citação (§ 7.7): "César, *BG* 1.1.1"; "Jo 1,1, Vulgata" (com reticências, porque a frase do versículo continua); "Terêncio, *Phormio* 203"; "Ravizza n. 14".

**Verificado sem mudança:** *puerī/servī* antes do cap. 5 (o verbo em *-nt* e a prática guiada 2 tornam o exercício resolúvel). ~~`direitos.tipo`~~ **Resolvido** por § 7.8 (`dominio_publico`).

**Pendências:** revisão externa.
