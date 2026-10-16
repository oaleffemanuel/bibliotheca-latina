# Revisão interna · Capítulo 1, *Dē linguā Latīnā* (O que é o latim?)

- Data: 2026-10-14 · Tipo: **revisão interna do autor**, feita contra gramáticas de referência. **Não é revisão externa independente**; por isso `creditos.revisao_gramatical` continua vazio e a página mostra "revisão gramatical: pendente".
- Escopo: atualização do capítulo ao padrão de 16 elementos (FLUXO-EDITORIAL.md § 6). Status mantido: `publicada`.
- Fontes conferidas nesta revisão (abertas e lidas, não citadas de memória):
  - Bennett, *New Latin Grammar* (texto local): Introdução § 3 (períodos; arcaico de 240 a 81 a.C.); § 1 (alfabeto; *K*, *Y*, *Z*; *I* e *V* vogais e consoantes); § 3 (pronúncia "romana"); § 4 (divisão silábica; oclusiva + *l/r*; *x* com a vogal anterior); § 5 (quantidade da vogal e da sílaba; sílabas "comuns", breves na prosa); § 6 (acento; enclíticas; *illīc*, *tantōn*).
  - Allen & Greenough, edição DCC: § 1 (alfabeto: sem *J, U, W*), §§ 2–5 (sons; *i/u* consoantes), § 7 (sílabas; *dīx-it*, *sax-um*), § 8 (pronúncia restaurada), §§ 9–11 (quantidade; vogal antes de vogal é breve; § 11.b–c posição e oclusiva + líquida), § 12 (acento e exceções), § 13 (conferido só para delimitar a referência).
  - Kennedy, *Revised Latin Primer* (OCR local): § 4 (quantidade), § 9 (acento).
  - Ravizza, *Gramática Latina* (OCR local): cap. 1, § 1 (alfabeto "de 24 letras", incluindo *U*), pronúncia de *ti* + vogal, § 5 (quantidade), § 6 (acento).
  - Lewis & Short (Perseus), verbete *philosophia*: *phĭlŏsŏphĭa*, com *i* breve.
  - DCC Latin Core Vocabulary: macrons de *sānctus*, *nōmen*, *quī*, *noster*, *tuus*.
  - Vulgata Clementina, Mt 6,9 (Wikisource latina, Evangelium secundum Matthaeum, caput 6): *Pater noster, qui es in cælis, sanctificetur nomen tuum.*
  - César, *BG* 1.1 (edição DCC), para a prática guiada 2.

## Acréscimos

| Elemento | O que foi acrescentado |
|---|---|
| 1 Título latino | `titulo_latim='Dē linguā Latīnā'` (igual a `livro.py`). |
| 3 Objetivos | 5º objetivo (ler em voz alta frase autêntica); 4º reformulado para incluir divisão silábica. |
| 5 Explicação | Subseção "Primeiro passo: dividir em sílabas"; observação "O macron não é acento"; nova seção 5, "Lendo em voz alta: uma frase autêntica". |
| 8 Análise | `analise()` de Mt 6,9 voltada à pronúncia (sílabas, quantidade, acento, as duas pronúncias), como admitido para este capítulo. |
| 10 Diagrama | `diagrama_frase()` com o acento palavra a palavra de Mt 6,9 (além da linha do tempo já existente). |
| 11 Erros comuns | 6 itens. |
| 12 Prática guiada | 2: acento de *Ītalia* e *senātor*; leitura em voz alta de *Gallia est omnis dīvīsa in partēs trēs*. |
| 13–14 Exercícios | Exercícios 4 (longa ou breve? reconhecimento com justificativa) e 5 (transformação: da grafia em maiúsculas para a edição moderna, *i/u/v*). Total: 5 conjuntos, todas as respostas explicadas. |
| 15 Leituras | Vulgata acrescentada; nota indica o Pai-Nosso inteiro (Mt 6,9–13) e Ravizza cap. 1. |
| 16 Referências | Parágrafos conferidos para A&G, Bennett, Kennedy e Ravizza; Vulgata Mt 6,9 acrescentada. |

## Correções feitas

| Antes | Problema | Depois |
|---|---|---|
| *philosophia*: "phi-lo-so-**phī**-a: o *ī* da penúltima é longo (como no grego)" | **Erro factual.** O *i* é breve (L&S *phĭlŏsŏphĭa*; vogal antes de vogal é breve, A&G § 10.a, Bennett § 5.A.2.b). | phi-lo-**so**-phi-a, com explicação; virou também o erro comum 2. |
| "Uma sílaba é longa ... quando termina em consoante, isto é, quando a vogal é seguida de duas consoantes" | **Incompleto e enganoso**: falta a exceção oclusiva + *l/r* (Bennett § 5.B.1.c e 3; A&G § 11.b–c) e o *x* duplo. | Regra completa, com *agricola*, *tenebrae* e *saxum*. |
| "O acento latino nunca cai na última sílaba" | Absoluto demais (A&G § 12 e Bennett § 6.4: *illīc*, *tantōn*). | "Em palavras de mais de uma sílaba, ... (as raríssimas exceções, como *illīc*, vêm da perda de uma sílaba final)." |
| "Cerca de nove em cada dez palavras latinas têm um parente direto em português" | Estatística não verificável. | "Boa parte das palavras mais frequentes do latim tem um parente direto em português". |
| Referência A&G "§§ 1–13 (alfabeto, sons, quantidade e acento)" | O § 13 trata de palavras combinadas (*Combinations*), não de acento. | § 1, §§ 2–5, § 7, § 8, §§ 9–11, § 12, com o assunto de cada um. |
| Referência Bennett "§§ 1–6 (alfabeto e pronúncia)" | Correta nos números, vaga no conteúdo. | §§ 1–3, 4, 5, 6 com assunto; acrescentada Introdução § 3 (períodos). |
| Ravizza "capítulo introdutório sobre pronúncia" | Sem parágrafos. | cap. 1, §§ 1–6. |
| Tabela do acento: "longa (termina em consoante)" para *puella*, *magister* | Formulação imprecisa. | "longa (vogal seguida de duas consoantes)". Acrescentado *fīlius* (vogal antes de vogal). |
| "lição", "próximas lições" | Terminologia do livro é "capítulo". | "capítulo(s)". |

## Verificações

- **Alfabeto**: 23 letras clássicas confirmado (A&G § 1; Bennett § 1). Acrescentada nota de que Ravizza conta 24 porque inclui o *U* moderno (verificado no OCR).
- **Pronúncia** (tabela restaurada × eclesiástica): coerente com Bennett § 3 e A&G § 8 para a restaurada; para *ti* + vogal na eclesiástica, coerente com Ravizza (*ti* conserva o som após *s, t, x*).
- **Acentos conferidos** (todas as palavras do capítulo): *amīcus, dominus, puella, fēmina, nātūra, magister, fīlius, Rōmānus, oculus, Caesar, agricola, Minerva, philosophia, fenestra, tenebrae, mīlitēs, Athēnae, saxum, Ītalia, senātor, Gallia, dīvīsa, sānctificētur, caelīs, nōmen, tuum*.
- **Macrons**: *sānctificētur* (DCC: *sānctus*), *nōmen*, *quī*, *caelīs* (abl. pl.), *Ītalia*, *senātor*, *Athēnae*, *mīlitēs*, *dīvīsa*. Formas sem macron conferidas como breves: *pater*, *noster*, *es*, *tuum*, *oculus*, *philosophia*.
- **Divisão silábica**: *sax-um* segue A&G § 7 nota 1 e Bennett § 4.5; *a-gri-co-la* e *te-ne-brae* seguem Bennett § 4.4.
- **Texto autêntico**: Mt 6,9 conferido palavra por palavra na Vulgata Clementina; César *BG* 1.1 conferido na DCC.
- **Exercício 5**: leitura de *I/V* conferida com Bennett § 1.2 e A&G § 1.b, § 5.

## Pendências

- Revisão externa por um latinista independente.
- *sānctificētur*: a divisão *sānc-ti-* (adotada) e *sān-cti-* (regra estrita de Bennett § 4.3) não mudam o acento; manter ou uniformizar com o resto do livro.
- O direito do capítulo continua `tipo='original'` (como no capítulo 3), embora cite dois versos curtos de textos em domínio público; decidir editorialmente se o padrão deve ser `dominio_publico` quando há citação.
- Opcional: gravar a leitura de Mt 6,9 nas duas pronúncias.

## Auditoria geral (2026-10-15)

- Tipo: **auditoria interna assistida por IA** (lote A, caps. 1–6), feita contra as fontes abertas nesta sessão. **Não é revisão humana nem revisão externa**: `creditos.revisao_gramatical` continua vazio e o status não mudou.
- Convenções aplicadas: FLUXO-EDITORIAL.md § 7 (inclusive § 7.2 corrigido: *hīc, haec, hōc*; não há formas desse pronome neste capítulo).

**Fontes abertas:** *Liber Usualis* (Desclée, 1949), archive.org `liber-usualis-1949-digital`, texto djvu da introdução, cap. IX ("The reading and pronunciation of liturgical Latin"): "H is pronounced K in the two words nihil (nee-keel) and mihi (mee-kee) and their compounds. In ancient books these words are often written nichil and michi. In all other cases H is mute."; C. Rossini, *Proper of the Mass* (media.musicasacra.com/pdf/rossini.pdf): "H is mute, except in the words Mihi and Nihil where it is pronounced like K (mi-ki, nikil)"; Bennett § 4.3 (*mōn-strum*); L&S s.v. *sanctifico*, *sanctus* (sem mácron); A&G (DCC) *sānctīs, sāncte*; Holmes (Oxford, 1914; Perseus/PerseusDL) *BG* 1.1.1; Vulgata Clementina (la.wikisource) Mt 6,9.

**Correções:**
- Referência acrescentada para César, *BG* 1.1.1 (prática guiada 2), com edição identificada (T. Rice Holmes, 1914), conforme § 7.8.3.
- Ravizza citado por "nn." (§ 7.7): "cap. 1, nn. 1–6".
- `tempo`: 35 → 45 min (§ 7.9).

**Verificado sem mudança:**
- Exceção *mihi/nihil* ("míki", "níkil") na pronúncia eclesiástica: já presente no texto e na referência ao *Liber Usualis*; conferida nas duas fontes acima (§ 7.5). Não duplicada.
- ~~Divisão de *sānctificētur*~~ **Resolvido**: o texto e o diagrama usam *sān-cti-fi-cē-tur* (Bennett § 4.3, *mōn-strum*), registrando que *sānc-ti-* dá o mesmo acento.
- Mácron de *sānct-*: L&S não marca a quantidade oculta; A&G (*sānctīs*) e Bennett (*sānctus*) a marcam; mantido (§ 7.1).
- ~~`direitos.tipo`~~ **Resolvido** por § 7.8: `dominio_publico` (o capítulo contém trechos antigos de edições em domínio público).

**Pendências:** revisão externa; gravação opcional de Mt 6,9.
