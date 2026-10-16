# Revisão interna · Capítulo 46, *Ovidius* (Ovídio: a criação do mundo, Metamorfoses I)

- Data: 2026-10-15 · Tipo: **revisão interna do autor**, feita contra gramáticas de referência e contra a edição do texto. **Não é revisão externa independente**; `creditos.revisao_gramatical` continua `None` e o capítulo fica em `status='rascunho'`.
- Fontes abertas e lidas nesta revisão (não citadas de memória):
  - Texto: *Metamorfoses* 1,1–32 no TEI da Perseus (canonical-latinLit `phi0959.phi006.perseus-lat2`, edição Hugo Magnus, Gotha, F. A. Perthes, 1892), lido no repositório PerseusDL do GitHub porque o servidor da Perseus estava fora do ar; comparado com The Latin Library (`ovid/ovid.met1.shtml`).
  - Vulgata Clementina, Gênesis 1,1–4 (wikitexto da Wikisource latina, `action=raw`).
  - Bennett, *New Latin Grammar* (`referencias/bennett.txt`): §§ 5, 101, 116.1, 189.1, 218, 227, 338.4.a, 350.11, 362–369, 375.
  - Allen & Greenough, edição DCC: §§ 181, 603, 604 (sem parte de versificação na edição DCC).
  - Kennedy (OCR local): §§ 474, 476, 477. Ravizza (OCR local): nºs 533–536.
  - Capítulos lidos para terminologia: 29 (particípios), 40 (notação, hexâmetro, figuras), 45 (este mesmo autor).

## Texto e tradução

| Item | Resultado |
|---|---|
| Proêmio 1,1–4; Caos 1,5–20; separação 1,21–31 | Conferidos palavra a palavra com Magnus. Macrons acrescentados e conferidos com a escansão de todos os versos (feita na revisão). |
| v. 2 *illās* (Magnus) × *illa* (outras edições) | Registrado numa observação; tradução segue Magnus. |
| v. 15 *utque āēr, tellūs illīc et pontus et aethēr.* (Magnus) × *utque erat et tellūs illīc et pontus et āēr,* (Latin Library) | Seguida a edição de Magnus; variante explicada numa observação; o verso de Magnus escande (4 espondeus, dáctilo, espondeu). |
| v. 32 *quisquis fuit ille deōrum* (citado na prosa) | Conferido em Magnus. |
| Gênesis 1,1–3 | Conferido; *æ* → *ae*; macrons acrescentados. |
| Traduções | Próprias, literais. |

## Morfologia, sintaxe e métrica

| Item | Resultado |
|---|---|
| *dīxēre* = *dīxērunt* | Bennett § 101. |
| *mūtāstis* = *mūtāvistis* | Bennett § 116.1; A&G § 181.a. |
| *abscidit* de *abscindō* (i breve) | Confirmado pelo 5º pé do v. 22. |
| *nātūra* nominativo no v. 21 | Confirmado pelo 5º pé (dáctilo *tū-ra-di*); Bennett § 363.1.a para o ablativo em *-ā*. |
| *āēr / āĕris*, *aethēr*, *tellūs* | Bennett §§ 362.1.d, 364.6.b, 365; A&G §§ 603.a.4, 604.j; escansão dos vv. 12, 17, 28. |
| Gerúndio *crēscendō* | Bennett § 338.4.a. |
| Particípio conjunto × ablativo absoluto (*circumfūsō in āere*) | Bennett § 227 (o ablativo absoluto é independente); remissão aos capítulos 29 e 30. |
| Ablativos de separação, comparação, limitação e meio | Identificados verso a verso; Bennett § 218 para o meio; comparação remetida ao capítulo 18. |
| Hexâmetro e cesuras | Bennett § 368; Kennedy § 477; Ravizza nº 536. Escansões dos vv. 5, 6, 7, 19, 21, 22 e 28 conferidas sílaba a sílaba. |
| Lítotes (*nōn bene iūnctārum*), hipérbato | Bennett §§ 375.1, 350.11.a. |

## Correções feitas durante a revisão

1. Tabela do esquema do hexâmetro com sete colunas trocada por tabela de três colunas (celular).
2. Notação "— ∪" trocada por "– ˘", a do capítulo 40.
3. Prática guiada 2: contagem de sílabas do v. 19 corrigida (quinze, não catorze).
4. Erro comum 6: o exemplo *tōtō nātūrae* estava apresentado como par correto; corrigido (*tōtō* concorda com *orbe*).
5. Diagrama: rótulo longo dividido em duas caixas para caber no SVG.
6. Acrescentados às referências Bennett §§ 227, 363.1.a, 364.5.a, 364.6.b, usados no texto.

## Pendências para a auditoria final

- Verificar quais edições modernas leem *illa* no v. 2 e qual leitura do v. 15 a coordenação prefere expor (a observação não cita editores modernos pelo nome).
- *pugnābant calidīs* (v. 19): dativo com *pugnāre* tratado como uso poético, sem parágrafo conferido; procurar a referência (A&G, dativo com verbos de luta na poesia).
- *deus et melior nātūra*: a hesitação dos comentadores (dois sujeitos × hendíadis) é mencionada sem citar comentário específico.
- Afirmações gerais sobre Ovídio (preferência por dáctilos, poucas elisões; "um poema e um erro"; ≈ 12 000 versos, ≈ 250 histórias) não foram conferidas numa fonte específica nesta revisão.
- Prerrequisitos listam também 18, 29, 31 e 45, além de 30 e 40 de `livro.py`.
- Kennedy e Ravizza citados por números lidos em OCR.


## Auditoria geral (2026-10-15)

Auditoria interna **assistida por IA** (lote H, caps. 42–49). **Não é revisão humana**: `revisao_gramatical` continua `None` e o status não muda. Fontes abertas nesta auditoria: TEI do PerseusDL (canonical-latinLit), Perseus (L&S), The Latin Library, scans do archive.org indicados abaixo, Bennett/Kennedy/Ravizza locais. Convenções aplicadas: §7.2 corrigido (*hīc, haec, hōc*), citação "Bennett § 21.2.e", "Ravizza n.".

**Correções**
- Variante do v. 2 (*illās*): conferidas Magnus 1892 (TEI phi0959.phi006), Magnus, edição escolar de 1885 (archive.org `bub_gb_ycgzAQAAMAAJ`), Merkel–Ehwald, Teubner *editio minor* (archive.org `operadivo02ovid`), Miller, Loeb 1916 (archive.org `metamorphoses01ovid`) e The Latin Library: todas *illās*. A observação deixou de atribuir *illa* a "muitas edições modernas" sem conferência; agora diz que a leitura *illa* (proposta por P. Lejay em 1894) aparece em edições mais recentes, não usadas aqui.
- Variante do v. 15: Magnus (1885 e 1892) *utque aer, tellus illic et pontus et aether.*; Merkel–Ehwald, Miller e Latin Library *utque erat et tellus illic et pontus et aer, / sic erat…*. A observação agora nomeia essas edições e registra a glosa de Magnus (1885), *ut* = "onde".
- *pugnābant calidīs*: referência encontrada, Bennett § 358.3 (dativo com verbos de luta nos poetas, *contendis Homērō*); acrescentada à nota e às referências.
- Retirado "os comentadores se dividem" (não conferido) sobre *deus et melior nātūra*.
- *hic, haec, hoc* → *hīc, haec, hōc* na análise; "nº" → "n.".

**Verificado sem mudança**: escansões dos vv. 5, 6, 7, 19, 21, 22, 28; Bennett § 365 (*āēr, aethēr*), § 368.1–3.

**Pendente (revisão humana)**: a origem da conjectura *illa* (Lejay 1894; defendida por Kenney) foi vista só num resumo de artigo da *Classical Quarterly* (busca na web), não no artigo; afirmações gerais sobre o estilo de Ovídio e números redondos (≈12 000 versos, ≈250 histórias).
