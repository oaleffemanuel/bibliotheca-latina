# Revisão interna · Capítulo 42, *Phaedrus* (Fedro: uma fábula)

- Data: 2026-10-15 · Tipo: **revisão interna do autor**, feita contra a edição do texto e as gramáticas de referência. **Não é revisão externa independente**; `creditos.revisao_gramatical` continua `None` e o capítulo fica em `status='rascunho'`.
- Fontes abertas nesta revisão (não citadas de memória):
  - Texto latino: Fedro, *Fabulae Aesopiae* I, 1 (*Lupus et agnus*) e I, 4, v. 1, no Perseus (`Perseus:text:1999.02.0118`), que reproduz L. Mueller, Leipzig, Teubner, 1876 (rodapé da página conferido); I, 1 e o prólogo do livro I (vv. 1–2) na The Latin Library (`phaedr1.html`). I, 1: mesmas palavras nas duas fontes (só pontuação diferente).
  - Bennett (`referencias/bennett.txt`): §§ 59.2 b (*famē*), 102, 113, 188.1, 219, 250.1, 251.4 a, 259.3, 263, 348–349, 350.11 a, 366.2 e 366.8, 370.1–2.
  - Allen & Greenough, DCC (páginas `relative-pronouns`, `dative-reference`, `ablative-cause`, `present-tense`, `pluperfect-and-future-perfect-tenses`, `order-words`): §§ 305, 307 b, 376–377, 404, 469, 477, 597–598, 599 c.
  - Kennedy (OCR local): § 195 (relativo), § 479 (trímetro iâmbico/senário).
  - Ravizza (OCR local): nº 175, nº 408, nº 536 (senário; cita Fedro, prólogo I).

## Verificações

| Item | Resultado |
|---|---|
| Texto de I, 1 (15 versos) | Conferido palavra a palavra com Mueller/Perseus e Latin Library. Macrons acrescentados pelo autor do capítulo; aspas modernas. |
| Macrons do texto (*rīvum, vēnerant, sitī, compulsī, īnferior, improbā, latrō, iūrgiī, fēcistī, bibentī, lāniger, contrā, timēns, quī, quaesō, quereris, dēcurrit, haustūs, vēritātis vīribus, mēnsēs, dīxistī, nātus, nōn, iniūstā, scrīpta, fābula, fictīs, innocentēs*) | Conferidos pela morfologia (partes principais, declinação: *sitis* abl. *sitī*; *haustus* 4ª decl.; *nex, necis*). |
| Partes principais citadas (*compellō … compulsum; repellō, reppulī, repulsum; corripiō … correptum; fingō, fīnxī, fictum; īnferō, intulī, illātum; nāscor, nātus sum; queror, questus sum*) | Corretas. |
| Sintaxe: *mihi bibentī* (dativo de referência), *sitī* e *fauce improbā* (causa), *vēritātis vīribus* (meio), *quī* adverbial, *quod quereris* (relativa sem antecedente), *correptum* com objeto subentendido, *lacerat* (presente histórico), *quī* do v. 15 (nom. pl., antecedente *hominēs*) | Conferidas com Bennett §§ 188.1, 219, 250.1, 259.3 e A&G §§ 305, 404, 469. |
| Prólogo I, 1–2 (*quam māteriam … hanc*) | Relativa com antecedente incorporado: Bennett § 251.4 a; A&G § 307 b. |
| Finais de verso iâmbicos citados (*…ne-rant*, *…pro-bā*, *…pri-munt*) | Quantidades conferidas; a escansão completa foi deliberadamente deixada para o capítulo 40. |
| Gabarito | Exercícios 1–6 e práticas guiadas conferidos; transformações para a passiva com concordância e ablativo sem *ā* para coisas. |
| Tradução portuguesa | Própria; não consultada nenhuma tradução publicada protegida. |

## Correções feitas durante a revisão

1. Exercício 6, item 2: *fame* corrigido para *famē* (ablativo de *famēs* pela 5ª declinação; Bennett § 59.2 b).

## Pendências para a auditoria final

- O prólogo do livro I (vv. 1–2) foi conferido só na The Latin Library (o Perseus não respondeu para essa seção); conferir em Mueller.
- Dados biográficos de Fedro (datas aproximadas, "de origem grega", liberto de Augusto pelo título dos manuscritos, cinco livros incompletos) escritos de forma cautelosa, sem fonte aberta nesta revisão; conferir numa introdução de edição.
- A forma grega *promȳthion* (quantidade do *y*) não foi conferida em dicionário.
- O build completo falha hoje por causa de outros capítulos (ex.: 53 aponta para 51 ainda marcador); o capítulo 42 aponta para 24, também marcador. Numa cópia do repositório com a checagem de pré-requisitos desligada, o capítulo gerou `docs/aprenda/42-fedro.html` como rascunho, com `id="erros"`, `id="pratica"`, `class="analise"` e o SVG do diagrama.


## Auditoria geral (2026-10-15)

Auditoria interna **assistida por IA** (lote H, caps. 42–49). **Não é revisão humana**: `revisao_gramatical` continua `None` e o status não muda. Fontes abertas nesta auditoria: TEI do PerseusDL (canonical-latinLit), Perseus (L&S), The Latin Library, scans do archive.org indicados abaixo, Bennett/Kennedy/Ravizza locais. Convenções aplicadas: §7.2 corrigido (*hīc, haec, hōc*), citação "Bennett § 21.2.e", "Ravizza n.".

**Correções**
- Exercício 1, item 2 (gabarito): a explicação dizia que a água passava pelo cordeiro antes de chegar ao lobo (o inverso do texto). Corrigido: a água passa primeiro pelo lobo e só depois chega ao cordeiro.
- Prólogo do livro I (vv. 1–2) e prólogo III, v. 17 (*Pierio … iugo*) conferidos no TEI de Mueller (phi0975.phi001): mesmas palavras. Nota da referência atualizada.
- Texto de 1.1: palavras = Mueller; a pontuação do livro difere em três pontos (ponto e vírgula depois de *compulsī*, ponto depois de *intulit* e do v. 12). O capítulo agora o diz, em vez de afirmar que só macrons e aspas foram acrescentados.
- *hic, haec, hoc* → *hīc, haec, hōc* (§7.2 corrigido) em duas glosas.

**Verificado sem mudança**: Bennett §§ 59.2.b, 251.4.a, 370.1–2; Kennedy § 479; Ravizza n. 536 (senário de Fedro); *promȳthion* (de μῦθος, com ῦ longo).

**Pendente (revisão humana)**: dados biográficos de Fedro (formulados com cautela; o título *Augustī lībertus* vem dos manuscritos).
