# Revisão interna · Capítulo 54, *Thomās Aquīnās* (Tomás de Aquino: um artigo da Summa)

- Data: 2026-10-15 · Tipo: **revisão interna do autor**, feita contra as fontes e as gramáticas de referência. **Não é revisão externa independente**; `creditos.revisao_gramatical` continua `None` e o capítulo fica em `status='rascunho'`.
- Leitura comentada (Parte IV): artigo integral *Summa theologiae* I, q. 2, a. 1 (três objeções, *sed contra*, corpo, três respostas). Último capítulo do livro; termina com a seção "E agora?".

## Fontes efetivamente abertas
- **Texto-base**: digitalização do tomo IV da edição Leonina (Romae, ex typographia polyglotta S. C. de Propaganda Fide, **1888**), archive.org `operaomniaiussui04thom`, texto OCR (`_djvu.txt`) lido nas pp. 27–28 (folha de rosto conferida: "Tomus quartus · Pars prima Summae theologiae a quaestione I ad quaestionem XLIX · MDCCCLXXXVIII"). Conferidos na mesma digitalização: I, q. 1, a. 1, arg. 2 (*doctrina non potest esse nisi de ente…*); I, q. 2, a. 3 (início da primeira via: *Certum est enim…*, *Movere enim nihil aliud est quam educere aliquid de potentia in actum*); I, q. 3, a. 4 (*Sua igitur essentia est suum esse*).
- **Texto corrente**: Wikisource latina, *Summa Theologiae/Prima pars/Quaestio II*; comparação automática palavra a palavra com o texto do capítulo (sem macrons): nenhuma diferença.
- **Corpus Thomisticum** (`sth1001.html`, `sth1002.html`): o rodapé declara "© 2019 Fundación Tomás de Aquino quoad hanc editionem · Iura omnia asservantur". Por isso **não** foi usado como fonte do texto; só consultado. O capítulo diz isso em `referencias` e na observação sobre a edição.
- **Anselmo, Proslogion** cap. 2 (The Latin Library, `anselmproslogion.html`): *credimus te esse aliquid quo nihil maius cogitari possit… "dixit insipiens in corde suo: non est Deus"*.
- **Vulgata Clementina** (Wikisource): Salmo 52,1 (*Dixit insipiens in corde suo: Non est Deus*); João 14,6 (por meio da margem da Leonina, "Vers. 6").
- **Bennett**: § 115, § 138 III–IV, § 297.2, § 299.1.a, § 300.1 e 300.6, § 330, § 337.8.b.1.
- **Allen & Greenough** (DCC): `periphrastic-conjugations` (§§ 193–194), `impersonal-verbs` (§§ 207–208, 208.d), `ablative-absolute` (§ 419), `infinitive-noun` (§ 452), `infinitive-subject-impersonal` (§ 454), `gerund-and-gerundive` (§ 500), `indicative-quod` (§ 572), `indirect-questions` (§ 574).
- **Kennedy** (OCR): §§ 299–301, §§ 381–383. **Ravizza** (OCR): nº 140, IV.

## Verificações
| Item | Resultado |
|---|---|
| Texto do artigo | Idêntico (palavras) à Leonina e à Wikisource; pontuação da Leonina (dois-pontos); grafia *intelligit/intelligat*, *existendi*, *Boetius* (com macron: *Boētius*) mantida. |
| Macrons | Acrescentados; conferidos *intellēctō/intellēctūs*, *scītō*, *arguī* (inf. pres. passivo, *u* breve), *āctus*, *ēdūcere*, *exīstimant*, *quoad* sem macron. |
| Estrutura do artigo | Fórmulas (*Ad primum sic proceditur; Videtur quod; Praeterea; Sed contra; Respondeo dicendum quod; Ad primum ergo dicendum quod*) conferidas no próprio texto. |
| Gramática | *Deum esse* sujeito (Bennett § 330; A&G § 452); *dīcendum* gerundivo impessoal (Bennett § 337.8.b.1; Kennedy § 382); *prōcēditur* passiva impessoal (Bennett § 138 IV; A&G § 208.d; Ravizza nº 140 IV); *sequitur/contingit quod* comparado com o clássico *ut* + subj. (Bennett § 297.2); *ex hōc… quod* (Bennett § 299.1.a; A&G § 572); interrogativa indireta no indicativo (Bennett § 300.6; capítulo 50). |
| Traduções | Próprias, feitas para este capítulo. |
| Gabarito | Respostas conferidas; retroversões para latim clássico revistas (ver correções). |
| Catálogo | Leituras e referências com ids existentes; o roteiro "E agora?" cita apenas obras presentes no catálogo. |
| Validação | Import ok; build completo concluído sem erro; HTML com `id="erros"`, `id="pratica"`, `class="analise"`, diagrama SVG e cinco exercícios. |

## Correções feitas durante a revisão
1. Exercício 3: a retroversão de *sequitur quod sit in rē* por oração infinitiva foi substituída por *sequitur ut… sit* (Bennett § 297.2); o item sobre *Vidētur quod…* (retroversão discutível) foi trocado por *contingit… quod* → *contingit ut*.
2. Seção 5: a afirmação de que Cícero usaria sempre a infinitiva onde Tomás usa *quod* foi precisada (infinitiva com *oportet*; *ut* com *sequitur, contingit*). Retirada a remissão a A&G § 454 para *contingit* + infinitivo (o parágrafo não lista *contingit*).
3. Exercício 4, *existendī*: reescrito o comentário (gerúndio com *Deum* no acusativo).
4. Retiradas afirmações não verificadas: o conteúdo do capítulo 1 ("pronúncia de *Magister*"), *Fābulae* fora do catálogo, "três mil páginas", "*ēns* não existe em Cícero" (agora "praticamente ausente da prosa clássica").

## Pendências para a auditoria final
- *cognitiō existendī Deum*: a análise (gerúndio com sujeito no acusativo) é uma interpretação; um revisor pode preferir ler *Deum* como objeto de *cognitiō* em construção livre. Conferir com um comentário escolástico ou gramática do latim medieval.
- A observação de que, em Tomás, *quod* leva subjuntivo "sobretudo depois de verbos de aparência, necessidade ou consequência e em contexto hipotético" é uma tendência observada neste artigo, não regra tirada de gramática citada.
- *quoad* como preposição com acusativo (latim escolástico): sem parágrafo de gramática clássica que o cubra; conferir em léxico de latim medieval.
- Dados biográficos (c. 1225, Roccasecca, 1274, início da *Summa* c. 1265–1266, *Tertia pars* até a q. 90) sem fonte bibliográfica citada.
- Remissão de Damasceno (*De fide orthodoxa* I, 1 e 3) tomada da margem da Leonina, não conferida no texto grego/latim de Damasceno.
- O roteiro "E agora?" cita capítulos 42–49 e 52 pelo sumário; o 52 ainda era marcador quando este capítulo foi escrito.
- Revisão externa por latinista independente.

## Auditoria geral (2026-10-15)

Auditoria interna assistida por IA (lote I), **não é revisão humana**; `revisao_gramatical` continua `None`. Tabela completa: relatório do lote I da auditoria.

Correções: (1) *cognitiō existendī Deum*: texto conferido na Leonina (p. 27) e paralelo do próprio Tomás no mesmo tomo (I, q. 8, a. 3: *modi existendi Deum in rebus*) acrescentado ao gabarito do exercício 4; (2) *quoad* = *quod attinet ad* com fonte (Du Cange, *Glossarium*, t. 6, col. 617c); (3) pronome *hoc* → *hōc* em 11 lugares (§7.2 revisto).
Verificados: artigo inteiro idêntico à Leonina t. IV (1888), pp. 27–28; margem "De Fide Orth., cap. I, III" (Damasceno); biografia (CE, *St. Thomas Aquinas*: 1225 ou 1227; *Summa* desde 1265; *Tertia pars* até a q. 90); Bennett §§ 138, 297.2, 299.1.a, 300.6, 330, 337.8.b.1; Kennedy § 382.
Pendente: texto de Damasceno não aberto; a tendência de *quod* + subjuntivo continua observação do artigo, não regra de gramática.
