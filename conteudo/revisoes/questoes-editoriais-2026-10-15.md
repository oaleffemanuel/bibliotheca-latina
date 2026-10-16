# Questões editoriais resolvidas · 2026-10-15

- Tipo: **revisão interna do autor** (não é revisão externa). Escopo: pendências abertas nas revisões dos capítulos 4, 6, 7, 8 e 9. Os capítulos 10–14 não foram tocados.
- Regra seguida: só se cita o que foi aberto e lido nesta sessão; quando a evidência não basta, isso fica dito.

## 1. *-ābus* (capítulo 4) e o acusativo *Aenēān*

**Fontes abertas (texto lido na íntegra):**

| Fonte | Onde | O que diz (citação curta) |
|---|---|---|
| Bennett, *New Latin Grammar* (texto local) | § 21.2.e | "Instead of the regular ending -īs, we usually find -ābus in the Dative and Ablative Plural of dea [...] and fīlia [...], especially when it is important to distinguish these nouns from the corresponding forms of deus [...] and fīlius". Às vezes também *lībertābus, equābus*. |
| Allen & Greenough, ed. DCC (`1st-declension-case-forms`) | § 43.e | "The dative and ablative plural of dea [...] and fīlia [...] end in an older form -ābus [...] to distinguish them from [...] deus [...] and fīlius". Raramente *līberta, mūla, equa*; "except when the two sexes are mentioned together [...] the form in -īs is preferred in all but dea and fīlia." |
| Kennedy, *Revised Latin Primer* (OCR local) | § 34, nota 4 | "Dea and filia have dat. and abl. plural -abus, in order to distinguish them from the dat. and abl. plural of deus and filius." |
| Ravizza, *Gramática Latina* (OCR local) | § 19 | *dea, filia, liberta* têm, "alem da forma regular em īs", uma em *ābus* "quando estão unidos ou contrapostos" aos masculinos; "Estas formas em âbus não se usam quando não estão contrapostas ou unidas". |

**Conclusão.** Três das quatro gramáticas (A&G, Bennett, Kennedy) tratam *deābus, fīliābus* como as formas normais de *dea, fīlia*, motivadas pela distinção com o masculino; Bennett diz "usually" (logo, *-īs* também ocorre) e "especially" quando a distinção importa. Só Ravizza restringe a forma aos contextos com masculino ao lado. Para os outros nomes (*līberta, equa, mūla*), todas convergem: raro, e quase só com os dois sexos juntos (A&G). **Posição do livro**: a de A&G/Bennett/Kennedy, com a restrição de Ravizza registrada como posição mais estrita.

**Mudanças em `l04_a_primeira_declinacao.py`:** parágrafo "Duas formas especiais" reescrito com essa posição (incluindo *equa* ao lado de *līberta*, A&G e Bennett); tirada a expressão "quase obrigatória", que nenhuma das fontes sustenta; o texto diz agora explicitamente por que os exemplos e exercícios usam *fīliābus* sem masculino ao lado (*Agricola fīliābus fābulās nārrat*, *Nautae cum fīliābus...*, *Rēgīna cum fīliābus...*). No resumo, "indispensáveis quando os dois sexos aparecem juntos" virou "sobretudo quando os dois sexos aparecem juntos; *fīliīs* também ocorre". Exemplos e gabaritos não mudaram: são coerentes com a posição adotada.

**Aenēān.** Lewis & Short (Perseus) s.v. *Aenēas*: "acc. Aenean often, after the Gr." (com remissão a Ovídio). O quadro em PDF de A&G § 44 (DCC, `1st_decl_Greek_Nouns_0.pdf`) dá *Aenēās*, ac. *Aenēān (-am)*. Bennett § 22 traz o mesmo padrão em *Archiās* (ac. *Archiam* ou *-ān*). Forma confirmada; texto mantido.

**Em aberto:** nada além da revisão externa.

## 2. Originalidade do texto do capítulo 8

**Acesso.** O texto de *Lingua Latina per se illustrata: Familia Romana* (Ørberg) é protegido e não foi consultado nem reproduzido. A comparação se baseia só no que é descrito publicamente: a folha de exercícios "Lingua Latina, Capitulum XVI, Pensum C" de um professor (users.pfw.edu/dfleming/LatinExer/Cap16_PensumC.pdf), cujas perguntas indicam os assuntos do cap. 16: que navios podem chegar a Roma, o que é a foz (*ōstium*) de um rio e se o Tibre deságua no mar Superior, quando os navios saem do porto, onde fica o *gubernātor* e o que faz, as quatro partes do céu, o que Medo e Lídia levam consigo, para onde Medo quer ir com a amiga, por que Lídia está triste, que deus os marinheiros invocam, por que a carga é lançada ao mar e se o navio afunda. As respostas não foram consultadas.

**Comparação com o texto do capítulo 8** (frases 1–18): personagens diferentes (Flávia, Tito, avô e avó; nenhum casal fugitivo, nenhum piloto, nenhuma tripulação); cenário diferente (costa da Campânia e um barquinho a remo até uma ilha próxima, não um navio mercante saindo de Óstia); trama diferente (passeio em família; o avô pressente o vento; a água entra e Tito a tira com um balde; chegada, jantar, histórias, sono); nada de carga lançada ao mar, oração a um deus, pontos cardeais ou navio em perigo de naufrágio. O que se repete é só o *tópos* (vento, ondas, medo, calmaria) e vocabulário básico inevitável (*ventus, unda, nauta, aqua*), presente em qualquer texto latino sobre o mar.

**Conclusão.** Risco desprezível. Não há personagem, nome, sequência de frases nem expressão característica em comum que se possa identificar com a informação pública. Uma ressalva: como o texto de Ørberg não foi lido, não se pode excluir que alguma frase curta e banal (por exemplo, sobre vento e ondas) coincida por acaso. Isso não muda a avaliação, porque essas frases seriam lugar-comum de vocabulário mínimo. **Nenhuma mudança** no capítulo; as remissões internas às frases 1–18 (análise, prática guiada, exercícios) ficam intactas.

**Em aberto:** conferência opcional por alguém com o livro em mãos.

## 3. Kennedy, temas nasais (capítulo 9)

**Fonte:** Kennedy, *Revised Latin Primer*, OCR local (`kennedy.txt`). Os números de parágrafo em sequência no OCR são § 40 (labiais), § 41 (*s*), § 42 (líquidas), depois o título "Stems in Nasals: n, m" (*leō, virgō, nōmen*; "Decline also: [...] homo [...]"; "only one Stem in m: hiemps"), depois § 44 (temas em *-i*). O número que falta no OCR é, pela sequência, o 43. O **índice do próprio livro** confirma: "Nasals, 6, 36, 37, 43"; *leo*, *nomen*, *homo*, *hiemps* remetem a "37, 43". Não foi preciso outro scan.

**Mudança:** a nota de Kennedy em `l09_a_terceira_declinacao_consonantal.py` passou de "e a seção seguinte, de temas nasais" para "§ 43 (temas nasais: *leō, virgō, nōmen*; *homō, homin-*)".

**Em aberto:** nada.

## 4. Tabelas e abreviaturas não conferidas

### 4a. Abreviaturas do Lewis & Short (capítulo 7)

**Fontes:** Lewis & Short, *A Latin Dictionary* (1879), scan do archive.org `latindictionaryf00andr`, texto OCR (`_djvu.txt`), lista "Other abbreviations, signs, etc." da introdução; Lewis, *An Elementary Latin Dictionary*, scan `elementarylatind00lewi`, lista "Other abbreviations".

Conferido no L&S: "comm. or c., common gender" e também "c., cum (with)"; "a. or act., active"; "n. or neutr., neuter"; "v., verb, vide, or vox"; "intr., intransitive"; "trans., translated, -tion" (**não** "transitivo"); "dep., deponent"; "freq. or fr., frequentative"; "impers., impersonal"; "indecl., indeclinable"; "comp., compare or comparative"; "sup., superlative or supine"; "lit."; "trop., in a tropical or figurative sense"; "fig."; "syn."; "cf., confer". Não há *tr.* na lista. No *Elementary*: "act., active", "intrans., intransitive", "dep., deponent", "v., vide"; também sem *tr.*

**Mudanças em `l07_como_usar_o_dicionario.py`** (tabela "Abreviaturas frequentes"): a linha *tr. · intr.* ("equivalem a *v. a.* e *v. n.* em outros dicionários", afirmação não conferida) virou *intr. · intrans.*, com as fontes e o aviso sobre *trans.* = "traduzido" no L&S; *c. ou comm.* virou *comm. ou c.*, com a nota de que *c.* também é *cum*; *v. a. · v. n.* agora explica as abreviaturas como na lista do L&S (*verb, active, neuter*), em vez de expandi-las como *verbum activum/neutrum*, forma que a lista não dá; *comp. · sup.* e *cf. · v. · syn.* receberam os sentidos alternativos registrados no L&S.

### 4b. A&G § 39 (quadro das terminações das cinco declinações)

**Fonte:** página DCC `case-endings-five-declensions` e os PDFs `Case_endings_5_decl_1_1.pdf` e `Case_endings_5_decl_2.pdf`. Genitivo singular: *-ae, -ī, -is, -ūs, -ēī (-e)*. A&G § 37 (página `rules-noun-declension`) dá a mesma lista (*ēī* na 5ª); Bennett § 18 dá *-ēī / -ĕī*; Ravizza n. 17, *ei*.

Nenhum capítulo de 1 a 9 cita A&G § 39. O capítulo 7 cita A&G § 37 para os genitivos e escrevia *-eī*. **Mudança:** "*-ēī* ou *-eī*; Bennett § 18; A&G §§ 37 e 39", e § 39 acrescentado à nota de referência de A&G. Na mesma frase, a remissão a A&G § 37.a foi precisada: A&G dá a regra "tire a terminação do genitivo e sobra o tema" para os temas em consoante; nos temas em vogal, o tema inclui a vogal característica (*rosā-*). A regra didática do capítulo vem de Ravizza n. 17 ("Eliminando-se ae [...] terei o tema ros"), que agora aparece primeiro.

### 4c. Outros itens "não conferido / pendente" nas revisões

Busca por "não conferid", "não verificad", "pendente", "não foi aberta" em `conteudo/revisoes/*.md`:

- **l06, A&G § 163 (tabela só em PDF)**: conferido no PDF DCC `verb_personal_endings_pres.pdf`: ativo *-m (-ō), -s, -t, -mus, -tis, -nt*. Coincide com o capítulo 6 (*-ō* na maioria; *-m* em *sum*). Sem mudança no capítulo; pendência marcada como resolvida em `l06-revisao-interna.md`.
- **l04, Ora Maritima "três primeiros capítulos"**: já corrigido antes ("os primeiros capítulos"); nada a fazer.
- **l01, divisão silábica de *sānctificētur*; l06, `direitos.tipo` com citações da Vulgata**: decisões editoriais, não tabelas nem abreviaturas; fora do escopo e continuam em aberto.
- As menções a "revisão gramatical: pendente" referem-se à revisão externa, que continua em aberto em todos os capítulos.

## Arquivos alterados

- `conteudo/licoes/l04_a_primeira_declinacao.py`: parágrafo sobre *-ābus* e item do resumo.
- `conteudo/licoes/l07_como_usar_o_dicionario.py`: tabela de abreviaturas, genitivo da 5ª, remissão a A&G § 37.a, nota de referência (A&G § 39).
- `conteudo/licoes/l09_a_terceira_declinacao_consonantal.py`: nota de referência de Kennedy (§ 43).
- `conteudo/licoes/l08_da_frase_ao_paragrafo.py`: sem alteração.
- Revisões: pendências atualizadas em `l04`, `l06`, `l07`, `l08` e `l09-revisao-interna.md`.
