# Revisão interna · Capítulo 4, *Dē prīmā dēclīnātiōne* (A primeira declinação)

- Data: 2026-10-14 · Tipo: **revisão interna do autor**, feita contra gramáticas de referência. **Não é revisão externa independente**; por isso `creditos.revisao_gramatical` continua vazio e a página mostra "revisão gramatical: pendente".
- Escopo: atualização do capítulo ao padrão de 16 elementos (FLUXO-EDITORIAL.md § 6). Status mantido: `rascunho`.
- Fontes conferidas nesta revisão (abertas e lidas, não citadas de memória):
  - Bennett, *New Latin Grammar* (texto local): § 20 (paradigma de *porta*; § 20.1 sem artigo), § 21.1 (masculinos *nauta, agricola*), § 21.2.c (locativo), § 21.2.e (*-ābus* "usually" em *dea, fīlia*; às vezes *lībertābus, equābus*), § 22 (nomes gregos: *Archiās*, ac. *Archiam* ou *-ān*; *epitomē*, ac. *epitomēn*; latinizados como *grammatica, mūsica*), § 56.3 (*tenebrae* só no plural), § 141 (preposições com acusativo), § 142 (com ablativo; § 142.1: *ab* obrigatório antes de vogal ou *h*, em geral **não** antes de *b, p, f, v, m, c, g, q, t*; § 142.2: *ē/ex*), § 143 (*in* e *sub*: acusativo = movimento, ablativo = repouso).
  - Allen & Greenough, edição DCC: §§ 40–42 (tema, paradigma, gênero; masculinos pelo significado), § 43 (formas especiais; § 43.e *deābus, fīliābus*, "rarely" *līberta, mūla, equa*, e *-īs* preferido fora de *dea, fīlia* exceto quando os dois sexos aparecem juntos), § 44 (nomes gregos), § 219 (origem das preposições), § 220 (listas com acusativo e com ablativo), § 221 (usos; *ā/ab*).
  - Kennedy, *Revised Latin Primer* (OCR local): § 34 (*mensa*; nota 4: *dea* e *fīlia* com *-ābus*).
  - Ravizza, *Gramática Latina* (OCR local): § 18 (1ª declinação: *poeta*, *rosa*; masculinos *agricola, nauta, scriba*), § 19 (*-ābus* só quando unidos ou contrapostos aos masculinos: *dīs deābusque*, *fīliīs et fīliābus*), § 146 (preposições com acusativo), § 147 (com ablativo; *ab* antes de vogal ou *h*, *ā* antes de consoante).
  - DCC Latin Core Vocabulary (página da lista, conferida palavra por palavra).
  - Vulgata Clementina, Jo 1,5 (Wikisource latina, Evangelium secundum Joannem, caput 1): *et lux in tenebris lucet, et tenebræ eam non comprehenderunt.*
- Referências pedidas pelo editor (Bennett §§ 20–22 e 141–143; A&G §§ 40–44 e 219–221): **reconferidas e confirmadas**; acrescentados Bennett § 56.3, Kennedy § 34 e Ravizza §§ 18–19, 146–147.

## Acréscimos

| Elemento | O que foi acrescentado |
|---|---|
| 1 Título latino | `titulo_latim='Dē prīmā dēclīnātiōne'` (igual a `livro.py`). |
| 3 Objetivos | Novo objetivo: analisar palavra a palavra uma frase autêntica. |
| 4 Pré-requisitos | Texto atualizado ("Capítulo 3: os seis casos, o paradigma de *rosa* e as formas que coincidem"). |
| 5 Explicação | A seção "Uma frase longa, caso a caso" virou "Frases caso a caso: uma construída, uma autêntica", com a subseção de análise (mantém 6 seções). |
| 8 Análise | `analise()` de Jo 1,5: *in tenebrīs* (abl. pl. com *in*), *tenebrae* (nom. pl., nome só de plural), *eam* (ac. em *-am*). |
| 11 Erros comuns | 6 itens. |
| 12 Prática guiada | 2: *Rēgīna cum fīliābus ā villā in silvam ambulat*; *Poētae fābulās nautīs in īnsulā nārrant*. |
| 13–14 Exercícios | Novo Exercício 5 (transformação singular ↔ plural); a leitura passou a Exercício 6. Total: 6 conjuntos (reconhecimento, preposição e caso, declinação, retroversão, transformação, leitura), respostas explicadas. |
| 16 Referências | Kennedy e Vulgata Jo 1,5 acrescentados; parágrafos detalhados. |

## Correções feitas

| Antes | Problema | Depois |
|---|---|---|
| "Não há erro em usar *ab* e *ex* sempre." | **Erro factual** para *ab*: Bennett § 142.1 e Ravizza § 147 dão *ā* antes de consoante e *ab* em geral não antes de *b, p, f, v, m, c, g, q, t*. | *ex* serve sempre; *ab* só antes de vogal ou *h*; antes de consoante, *ā*. Virou também o erro comum 6. |
| "Três nomes têm ... *-ābus* em vez de *-īs*: *fīlia*, *dea* e, às vezes, *līberta*" | Impreciso: as gramáticas falam de *dea* e *fīlia* (usualmente) e só raramente de outros; Ravizza restringe a forma aos contextos com masculino ao lado. | Texto reescrito com a nuance e a divergência entre as gramáticas. |
| Gabarito de *fīlia*: só *fīliābus* | Excluía a forma regular *fīliīs*, que existe. | Gabarito admite *fīliīs* e explica por que *fīliābus* é a preferida. |
| "*Aenēās* (...), *poēsis* não, mas *epitomē*" | Frase truncada, com um contraexemplo (*poēsis*, 3ª declinação) sem explicação. | "*Aenēās* (...) e *epitomē* (...). Muitos outros se latinizaram (*grammatica*, *mūsica*)" (Bennett § 22.1). |
| "quase todos entre as mil palavras mais frequentes do latim" | **Não confere**: na lista do DCC estão 17 dos 24 nomes e 8 dos 10 verbos (faltam *rosa, domina, rēgīna, villa, amīca, nauta, agricola*; *habitō, nāvigō*). | "A maioria está na lista ...: 17 dos 24 nomes e 8 dos 10 verbos". |
| Exercício de leitura sem glosa de *nōn*, *Iūlia*, *Ītalia* | Vocabulário fora da lista. | Glosas acrescentadas no enunciado. |
| "Os três primeiros capítulos de Ora Maritima" | Número de capítulos não conferido. | "Os primeiros capítulos". |
| Referência Ravizza "1ª declinação e preposições" | Sem parágrafos. | §§ 18–19, 146–147. |

## Verificações

- **Morfologia**: paradigmas de *puella* e *nauta* (Bennett § 20; A&G § 41; Kennedy § 34; Ravizza § 18); *fīliābus, deābus* (fontes acima); declinações pedidas de *fīlia* e *poēta*; formas da transformação (*habitant, fīliābus, īnsulīs, laudat, epistulam*).
- **Gênero**: masculinos *nauta, agricola, poēta, pīrāta, scrība*; *incola* e *convīva* com gênero conforme a pessoa (comum de dois); A&G § 42.
- **Preposições**: a tabela confere com Bennett §§ 141–143 e A&G § 220; *in* + ac./abl. (Bennett § 143).
- **Sintaxe**: todos os itens com *dat/nārrat/portat* + dativo conferidos; ablativo de meio sem preposição no erro comum 3 coerente com o capítulo 3.
- **Jo 1,5**: texto conferido; *lūx* nom., *in tenebrīs* abl. pl., *tenebrae* nom. pl. (Bennett § 56.3), *eam* ac. sing. fem. retomando *lūx* (f.), *comprehendērunt* perfeito 3ª pl. A ambiguidade lexical de *comprehendere* ("compreender"/"dominar") está registrada no texto.
- **Concordância**: verbo–sujeito em todas as frases, inclusive no texto do Exercício 6 e nas práticas guiadas.
- **Macrons**: *dēclīnātiōne, fīliābus, deābus, īnsula, rēgīna, poēta, pīrāta, scrība, convīva, epitomē, Aenēās, lūx, lūcet, tenebrīs, nōn, comprehendērunt, nāvigant, nārrant*.
- **Remissões a capítulos futuros**: 5 (adjetivos, 2ª declinação), 9 (*lūx*, 3ª declinação), 13 (perfeito), 15 (pronome *is, ea, id*), conferidas em `livro.py`.

## Pendências

- Revisão externa por um latinista independente.
- ~~*Aenēās*, acusativo *Aenēān*~~ **Resolvido em 2026-10-15**: Lewis & Short s.v. *Aenēas* ("acc. Aenean often") e o quadro em PDF de A&G § 44 (*Aenēān (-am)*) confirmam a forma. Sem mudança no texto (ver `questoes-editoriais-2026-10-15.md`).
- ~~Posição do livro sobre *-ābus*~~ **Resolvido em 2026-10-15**: o livro segue A&G § 43.e, Bennett § 21.2.e e Kennedy § 34 n. 4 (*deābus, fīliābus* são as formas usuais de *dea, fīlia*, sobretudo quando é preciso distinguir do masculino; outros nomes, como *līberta, equa*, só raramente e quase só com os dois sexos juntos); Ravizza § 19 fica registrado como posição mais restritiva. Parágrafo da seção 2 reescrito e item do resumo atenuado ("indispensáveis" → "sobretudo"); exemplos e exercícios com *fīliābus* sem masculino mantidos, agora justificados no texto (ver `questoes-editoriais-2026-10-15.md`).

## Auditoria geral (2026-10-15)

- Tipo: **auditoria interna assistida por IA** (lote A, caps. 1–6), feita contra as fontes abertas nesta sessão. **Não é revisão humana nem revisão externa**: `creditos.revisao_gramatical` continua vazio e o status não mudou.
- Convenções aplicadas: FLUXO-EDITORIAL.md § 7 (inclusive § 7.2 corrigido: *hīc, haec, hōc*; não há formas desse pronome neste capítulo).

**Fontes abertas:** A&G §§ 40–44 e 219–221 (DCC); Bennett §§ 20–22, 56.3 (*tenebrae*), 142.1–2; Kennedy § 34 n. 4; Ravizza nn. 18, 19, 146–147; DCC Latin Core Vocabulary (17 dos 24 nomes e 8 dos 10 verbos conferidos); Vulgata Clementina Jo 1,5.

**Correções:**
- Mácron em falta: *in vill<b>am</b> / in vill<b>ā</b>* → *vīllam / vīllā* (dois exemplos da seção 3).
- *ab* antes de consoante: o texto dizia que é "raro"; Bennett § 142.1 diz que antes de consoante ocorre ora *ā*, ora *ab*, este normalmente não antes de *b, p, f, v, m, c, g, q, t*. Dica e resumo ajustados; a "regra prática" de produção (*ab* só antes de vogal ou *h*) foi mantida.
- "João 1,5" → "Jo 1,5"; Ravizza citado por "n."/"nn." (§ 7.7).

**Verificado sem mudança:** *-ābus* e *Aenēān* (já resolvidos em `questoes-editoriais-2026-10-15.md`; A&G § 43.e e Bennett § 21.2.e reconferidos).

**Pendências:** revisão externa.
