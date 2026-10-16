# Revisão interna · Capítulo 53, *Augustīnus* (Agostinho: as Confissões)

- Data: 2026-10-15 · Tipo: **revisão interna do autor**, feita contra as fontes e as gramáticas de referência. **Não é revisão externa independente**; `creditos.revisao_gramatical` continua `None` e o capítulo fica em `status='rascunho'`.
- Leitura comentada (Parte IV): dois textos autênticos, *Conf.* I,1,1 (integral) e VIII,12,29 (integral).

## Fontes efetivamente abertas
- **Texto-base**: *Confessiones (ed. Migne)/1* e */8* na Wikisource latina (edição J.-P. Migne, 1841, via Corpus Corporum; `action=raw` baixado e lido). Conferidas também as indicações bíblicas da própria edição (Psal. CXLIV, 3; CXLVI, 5; XXI, 27; VI, 4; LXXVIII, 5.8; I Petr. V, 5; Rom. X, 14; XIII, 13–14; Matth. XIX, 21).
- **Comparação**: The Latin Library, `augustine/conf1.shtml` e `conf8.shtml` (texto moderno). Variantes notadas: I,1,1 *inveniunt* (TLL) × *invenient* (Migne); VIII,12,29 *nihil aliud interpretans divinitus mihi iuberi nisi ut* (TLL) × *nihil aliud interpretans, nisi divinitus mihi juberi ut* (Migne); *audisse* × *audivisse*; *in eum locum* × *ad eum locum*. O capítulo segue Migne e registra a principal na seção 5.
- **Vulgata Clementina** (Wikisource latina): Salmos 6,4; 21,27; 78,5.8; 138,8; 144,3; 146,5; Romanos 10,14; 11,36; 13,13–14; 1 Pedro 5,5 (texto conferido versículo a versículo).
- **Cruzamentos internos das Confissões** (Migne): VI,3 (Ambrósio lê em silêncio: *vox autem et lingua quiescebant*), VIII,6 (*Pontitianus narrat Antonii vitam*), I,13–14 (estudos; *Litteras graecas oderat*).
- **Bennett** (`referencias/bennett.txt`): § 162.1–4 e 4.a, § 274, § 276, § 277, § 293 III.1–2, § 299, § 300.1 e 300.4, § 307, § 323, § 324.
- **Allen & Greenough** (DCC): `hortatory-subjunctive` (§ 439 e notas), `deliberative-subjunctive` (§ 444), `imperative` (§ 450), `infinitive-subject-impersonal` (§ 454), `clauses-comparison` (§ 524), `dum-dōnec-and-quoad` (§§ 553 e nota 1, 554), `substantive-clauses-purpose` (§ 563.a), `indirect-questions` (§ 574), `intermediate-clauses` (§§ 591–593), `causal-clauses` (§§ 539–540, consultado).
- **Kennedy** (OCR): §§ 357–361.
- **Ravizza** (OCR): nº 370, nº 371 (o OCR imprime "971"; número confirmado pelo índice: "subj. exortativo, 371"), nº 442.
- Vogais longas de palavras raras conferidas no Wiktionary (cabeçalhos `la-noun/la-verb`): *ēvangelicus, cōmissātiō, exīstimō, cognōscō, cantitō, uspiam, requiēscō, inquiētus, intellēctus, impudīcitia, superveniō, concupīscentia, contrītiō*.

## Verificações
| Item | Resultado |
|---|---|
| Transcrição dos dois textos contra Migne | Conferida palavra a palavra; ortografia normalizada (j > i; *coelis* > *caelīs*; *lacrymarum* > *lacrimārum*; *tanquam* > *tamquam*; *hujusce* > *huiusce*); *intelligere* e *comessationibus* mantidos. |
| Macrons | Acrescentados em todo o latim; formas verbais conferidas (*invocāris* ind. × *sciāris* subj.; *crēdidērunt*; *īnspīrāstī*; *invēnissem*; *diffūgērunt*). *cōmessātiōnibus*: macron do *ō* por analogia com *cōmissātiō* (ver pendências). |
| Subjuntivos do texto I | *dēlectet* (final), *requiēscat* (dōnec + expectativa, Bennett § 293 III.2; A&G § 553 n. 1), *sit* (interrog. indireta dupla, § 300.4), *sciāris* (final), *quaeram/invocem* (exortação na 1ª sing.; *quaeram* ambíguo com o futuro, resolvido pelo paralelo com *invocem*). |
| Subjuntivos do texto II | *solērent* (interrog. indireta, sequência secundária), *aperīrem/legerem* (completiva com *ut*), *invēnissem* (atração, Bennett § 324; A&G § 593), *admonitus fuerit* (quod + subj. de discurso relatado; perfeito em sequência secundária assinalado como liberdade tardia), *dīcerētur* (tamquam, § 307), *fēceritis* (proibição, § 276). |
| *quia* "que" × *quia* causal | Coerente com os capítulos 28 e 50 (seção "Dizer 'que'"). |
| Citações bíblicas e numeração dos Salmos | Vulgata 144 → 145; 146,5 → 147,5; 21,27 → 22,27 (22,26 em algumas Bíblias); 6,4; 78 → 79; 52 → 53. |
| Traduções | Próprias, feitas para este capítulo; não copiadas de tradução publicada. |
| Gabarito | Todas as respostas conferidas contra o texto e a análise; cada uma explica o porquê. |
| Catálogo | Ids de leituras e referências existentes em `data/catalogo.json`. |
| Validação | Import do módulo ok; build completo (`construir.py --sem-pdf --sem-xlsx`) concluído sem erro depois que o capítulo 51 foi escrito; HTML com `id="erros"`, `id="pratica"`, duas `class="analise"`, diagrama SVG. |

## Correções feitas durante a revisão
1. Removido um exemplo de Cícero (*quam quisque nōrit artem…*) citado de memória e não conferido.
2. Reescrita a nota sobre *iubērī ut*: a primeira versão dizia que *iubeō* + *ut* é "mais frequente no latim tardio" sem fonte; agora remete a A&G § 563.a (*iubeō* clássico com infinitiva) e descreve só o que está no texto.
3. A seção de vocabulário do texto I foi fundida à seção do texto para manter 6 seções; remissões internas ("seção 4", "seção 5") corrigidas.
4. Acrescentadas remissões aos capítulos 50 (sequência afrouxada) e 51 (*Vetus Latina*), escritos em paralelo.

## Pendências para a auditoria final
- Volume e colunas da *Patrologia Latina* (PL 32) não conferidos na digitalização impressa; o capítulo cita "Migne, 1841" conforme o cabeçalho da Wikisource.
- *praedicātor tuus* = Ambrósio: identificação usual, mas discutida; o capítulo diz "provavelmente".
- Datas biográficas (354, 384, 386, 387, 430; redação c. 397–400) dadas sem fonte bibliográfica citada; conferir com uma introdução de referência.
- A afirmação de que Agostinho cita em geral a *Vetus Latina* é corrente nos estudos, mas não está apoiada em fonte citada no capítulo.
- *cōmessātiō*: grafia bíblica com *e*; a quantidade do *o* foi posta por analogia com *cōmissātiō* (Wiktionary). Confirmar.
- O "subjuntivo exortativo na 1ª pessoa do singular" (*quaeram, invocem*): Bennett § 274 restringe o termo à 1ª do plural; o capítulo se apoia em A&G § 439 (definição geral e nota 2). Um revisor pode preferir "volitivo" ou "optativo".
- Revisão externa por latinista independente.

## Auditoria geral (2026-10-15)

Auditoria interna assistida por IA (lote I), **não é revisão humana**; `revisao_gramatical` continua `None`. Tabela completa: relatório do lote I da auditoria.

Correções: (1) regra de conversão dos Salmos (dica, resumo, erro comum): "some um" vale para Vg 10–145, exceto 113–115; Vg 9 = hebr. 9–10; Vg 146–147 = hebr. 147; (2) *praedicātor tuus*: Ambrósio, Cristo ou Paulo, segundo os comentadores (O'Donnell 1992); (3) "raro em Cícero" retirado, com remissão a Bennett § 274; (4) cena do jardim "fim do verão de 386 (agosto ou setembro)" (CE dá setembro); (5) Sl 6,4 e Sl 78,5 (79,5); (6) PL vol. 32 (folha de rosto de 1841 conferida no archive.org); (7) "*hīc* + -ce" (§7.2 revisto).
Verificados: VIII,12,29 e I,1,1 contra Migne; datas biográficas (CE; Bennett Intr. § 3.f); *cōmessātiō* (L&S *cōmissātio, cōmess-*); A&G § 439 n. 2–3 e § 553 n. 1; Bennett §§ 162, 274, 276, 293 III.
Pendente: colunas de PL 32 (OCR ilegível); "Agostinho cita em geral a *Vetus Latina*" sem fonte aberta.
