# Revisão interna · Capítulo 29, *Dē participiīs* (Os particípios)

- Data: 2026-10-15 · Tipo: **revisão interna do autor**, feita contra gramáticas de referência. **Não é revisão externa independente**; `creditos.revisao_gramatical` continua `None` e o capítulo fica em `status='rascunho'`.
- Fontes conferidas (abertas e lidas, não citadas de memória):
  - Bennett, *New Latin Grammar* (`referencias/bennett.txt`): § 70 (paradigma de *prūdēns*), § 70.3 (particípios em *-āns, -ēns*: ablativo em *-e* como particípio ou substantivo, em *-ī* como adjetivo), § 70.7 (genitivo plural em *-um* só na poesia), §§ 101, 103, 105, 107, 110 (particípios de *amō, moneō, regō, audiō, capiō*), § 112.a–b (depoentes), § 119.1–4 (formação do particípio perfeito; futuro ativo do mesmo tema; *moritūrus*), § 132 (*iēns, euntis*), § 336.1–5 (tempo relativo; perfeitos de depoentes com valor de presente: *ratus, veritus, ūsus, gāvīsus*), § 337.1–5 (usos atributivo e predicativo; *videō, audiō* + particípio; particípio perfeito equivalente a coordenada), § 356.2 (falta do perfeito ativo).
  - Allen & Greenough, edição DCC (páginas `3rd-declension-adjectives-classification-and-paradigms`, `3rd-declension-adjectives-case-forms-consonant-stems`, `forms-participle`, `deponent-verbs`, `tense-participles`, `uses-participles`, `future-participle`): § 117.b, § 121.a–b, § 158, § 190.a–b, §§ 488–493, §§ 494–497, §§ 498–499.
  - Kennedy, *Revised Latin Primer* (OCR): § 72, nota 2 (ablativo *-ī/-e*; no ablativo absoluto sempre *-e*), § 107 (os três particípios e os três que faltam), §§ 389–393.
  - Ravizza, *Gramática Latina* (OCR): nº 53, d (adjetivos e particípios em *-ns*; *amans*; obs. 1 sobre o ablativo), nºs 388–397, nºs 399–400.
  - Vulgata Clementina na Wikisource latina (wikitexto bruto): Mt 2,10–11; 9,9; Lc 2,16; 2,20.
  - Suetônio, *Cláudio* 21, na Latin Library: "Have imperator, morituri te salutant!".

## Morfologia

| Item | Resultado |
|---|---|
| Particípios dos cinco verbos-modelo, de *sum* (*futūrus*) e de *eō* (*iēns, euntis*; *itūrus*) | Conferidos em Bennett §§ 100–110, 132. |
| Paradigma de *amāns* (m./f. e n., sing. e pl.; ac. pl. *-ēs/-īs*; abl. *-e/-ī*) | Conforme Bennett § 70 (modelo *prūdēns*) e § 70.3; A&G §§ 117–118, 121. Vogal longa antes de *-ns*, breve antes de *-nt-*. |
| Particípio futuro: tema do perfeito + *-ūrus*; exceções *futūrus, moritūrus, itūrus*; intransitivos (*ventūrus*) | Bennett § 119.4 (inclusive *moritūrus*); *veniō* sem particípio perfeito pessoal. |
| Depoentes: três particípios ativos; perfeito ativo; gerundivo passivo (só mencionado) | Bennett § 112; A&G § 190. |
| Formas do exercício 1 (*amantem, audītīs, ventūrī, capientibus, secūtae, euntēs, regente, monitūrum*) | Todas as possibilidades de caso conferidas. |

## Sintaxe, traduções e gabarito

- Tempo relativo (presente simultâneo, perfeito anterior, futuro posterior): Bennett § 336; A&G § 489. Traduções das tabelas ajustadas ao tempo do verbo principal.
- Usos e repertório de traduções (tempo, causa, concessão, condição, modo, coordenação): Bennett § 337.2, 5; A&G § 496 e notas. Toda relação lógica proposta no gabarito é justificada pelo contexto ou por *tamen*.
- Mt 2,11: *intrantēs* conjunto ao sujeito implícito; *domum* objeto do particípio. Mt 9,9: *sedentem* com *vīdit* (Bennett § 337.3). Lc 2,16: *positum* concordando com *īnfantem*; Lc 2,20: *reversī sunt* depoente + dois particípios presentes.
- Exemplos e exercícios originais; vocabulário fora dos capítulos anteriores glosado no enunciado.

## Correções feitas durante a revisão

1. Exemplo *Caesar mīlitēs hortātus castra mōvit* (que Kennedy § 391 atribui a César, sem possibilidade de conferir a passagem) trocado por frase original com *dux*.
2. Gabarito de *veniō*: "o supino *ventum* só serve à passiva impessoal" corrigido para "a forma neutra *ventum* só aparece na passiva impessoal (*ventum est*)".
3. Etimologia duvidosa (*vindouro* < *ventūrus*) retirada; mantidos *futuro* e *nascituro*.
4. "Nomes hebraicos neste livro" restringido a "neste capítulo" (não há norma do livro sobre isso).
5. Erro de digitação na referência de A&G ("participios").

## Pendências para a auditoria final

- Ravizza, nº 53, obs. 2, dá genitivo plural em *-um* para particípios substantivados; Bennett § 70.7 e A&G § 121.b dão *-ium* como regular e *-um* como poético. O capítulo segue Bennett/A&G e não menciona *-um*.
- *Maria* e *Ioseph* ficaram sem macron. Convém uma norma do livro para nomes hebraicos.
- Os pré-requisitos 10, 13, 24, 25 e 27 eram marcadores `planejada` quando o capítulo foi escrito. As remissões a eles (adjetivos de segunda classe no 10; *amātus est* no 24; semidepoentes e *gaudeō* no 25; *eō* no 26; infinitivo futuro *amātūrus esse* no 27; oração infinitiva no 28) foram inferidas dos títulos e devem ser conferidas quando esses capítulos existirem. O build completo falha hoje por causa desses marcadores; o capítulo foi validado por import e numa cópia do repositório com a checagem de pré-requisitos desligada (gera `docs/aprenda/29-os-participios.html` como rascunho, com `id="erros"`, `id="pratica"`, `class="analise"`, tabelas `paradigma` e o SVG).
- Suetônio, *Cláudio* 21: a subdivisão (21.6) não aparece na Latin Library; a referência dá só o capítulo. A grafia *have* (por *avē*) é a do texto.
- A afirmação de que o particípio futuro substantivado é "raro em prosa clássica" apoia-se em A&G § 498 (raro em simples concordância, salvo *futūrus, ventūrus*); conferir se a formulação está adequada.
- Revisão externa por latinista independente.

## Auditoria geral (2026-10-15)

Auditoria interna assistida por IA (lote E). **Não é revisão humana**; `revisao_gramatical` continua `None` e o status não muda. Tabela completa: relatório do lote E da coordenação.

Correções:
- Genitivo plural dos particípios: nota acrescentada com a variante (Ravizza n. 53 obs. 2: *-um* no particípio substantivado; Bennett § 70.7 e A&G § 121.b: *-ium* regular, *-um* poético). O livro segue Bennett/A&G.
- Particípio futuro: "raro na prosa clássica, salvo *futūrus, ventūrus* (A&G § 498); mais livre em poetas e autores posteriores (§ 499)".
- Suetônio, *Cláudio* 21.6 (edição de Ihm, Perseus TEI; grafa *haue imperator*).
- *eius* sem mácron (§7.1); Mt/Lc abreviados; Ravizza "n./nn.".

Verificado sem mudança: Bennett §§ 70.3, 119, 336.5, 356.2; Kennedy § 72 n. 2; Mt 2,10–11; 9,9; Lc 2,16.20 na Clementina; *Maria, Ioseph* sem mácron conforme §7.4.

Pendências: remissões aos caps. 10, 24, 31, 34; revisão externa.
