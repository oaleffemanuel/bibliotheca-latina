from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='07-como-usar-o-dicionario', titulo='Como usar o dicionário; o vocabulário básico', titulo_latim='Dē lexicō', tempo='60 min',
    resumo='Como se lê um verbete latino, como se chega da forma do texto à forma do dicionário, o que fazer com homógrafos, grafias variantes, o enclítico -que e os prefixos, e como montar um vocabulário básico com a lista de frequência DCC e as ferramentas gratuitas, sem deixar o analisador automático pensar por você.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['verbete de dicionário', 'nominativo, genitivo e gênero', 'tema do nome', 'adjetivos de três terminações', 'partes principais do verbo', 'abreviaturas de dicionário', 'forma de dicionário a partir da forma flexionada', 'homógrafos', 'grafias u/v e i/j', 'enclítico -que', 'prefixos e assimilação', 'famílias de palavras', 'cognatos e falsos amigos', 'vocabulário básico e frequência', "Whitaker's Words, Logeion, Lewis & Short", 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulos 5 e 6: as duas primeiras declinações com os adjetivos de primeira classe, e o presente do indicativo de esse e das quatro conjugações (com a entrada de dicionário do verbo).', licoes=['05-a-segunda-declinacao', '06-o-presente-do-indicativo']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 1.2 (i/j e u/v), § 7.1 (mudança de vogal nos compostos), § 8.4–5 (assimilação), § 9.2–3 (grafias variáveis; compostos de jaciō), § 17.3 (tema e terminação), § 18 (as declinações pelo genitivo), §§ 63–65 (adjetivos de 1ª e 2ª declinação), § 99 (partes principais), §§ 158–159 (compostos; preposições inseparáveis), § 341.1–2 (-que)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 1.b (i e u/v nesta gramática), § 16 (assimilação nos compostos com preposição), § 37 e § 37.a (declinação pelo genitivo; como achar o tema), § 39 (quadro das terminações das cinco declinações, PDF da edição DCC), §§ 171–173 (conjugações e partes principais), § 224.a (-que), §§ 264–267 (compostos; prefixos; enfraquecimento da vogal, § 267 nota 2)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 17 (como o dicionário registra os substantivos e como achar o tema pelo genitivo), n. 84 (os "tempos primitivos" que o dicionário fornece), n. 159–160 (composição; partículas inseparáveis; in- negativo distinto da preposição in)', tipo='dominio_publico'),
        referencia('DCC Latin Core Vocabulary', 'Christopher Francese e Dickinson College', catalogo='college-dcc-latin-core-vocabulary', nota='página de apresentação (cerca de mil lemas, c. 70% das formas de um texto típico; frequência a partir dos dados LASLA) e versão em português (tradução de Vittorio Pastelli); posições de frequência citadas conferidas na lista', tipo='site'),
        referencia('A Latin Dictionary (Lewis & Short)', 'Charlton T. Lewis e Charles Short', catalogo='short-a-latin-dictionary-lewis-short', nota='verbetes conferidos na edição Perseus: amo, moneo, ambulo, porto, ap-porto, jacio, ager, arma, vir, cano, līber, civis, hortor, nequam', tipo='dominio_publico'),
        referencia("Whitaker's Words", 'William A. Whitaker', catalogo='whitakers-words', nota='respostas conferidas para portas, servo, amicae, agros, liberos, capiunt, populi, malum, arma, virumque, cano', tipo='site'),
        referencia('Aeneis I, 1 (Virgílio)', None, catalogo='maro-aeneis-selecoes', nota='frase autêntica analisada na seção 6 (texto conferido em The Latin Library e no Perseus)', tipo='dominio_publico'),
    ],
    objetivos=[
        'Ler um verbete de nome, de adjetivo e de verbo, dizendo o que cada parte informa: genitivo, gênero, terminações, partes principais e abreviaturas.',
        'Chegar à forma de dicionário a partir de uma forma flexionada: separar a terminação, testar as declinações e conjugações possíveis e conferir o tema no verbete.',
        'Resolver homógrafos pelo contexto e não perder uma palavra por causa de grafias variantes (u/v, i/j, prefixos assimilados) ou do enclítico <i>-que</i>.',
        'Reconhecer os prefixos <i>in-, ad-, con-, ex-, re-, dē-</i> e as famílias de palavras, distinguindo cognatos úteis de falsos amigos.',
        "Montar um plano de vocabulário com a lista de frequência DCC e usar Whitaker's Words, Logeion e Lewis & Short para conferir uma análise já feita, e não para substituí-la.",
    ],
    secoes=[
        ('O verbete: o que o dicionário diz em uma linha', f'''
<p>Um dicionário latino não registra as palavras na forma em que elas aparecem nos textos, e sim numa <b>forma de citação</b> (o <b>lema</b>), seguida de algumas formas-chave que permitem reconstruir todas as outras. A primeira linha de um verbete é, portanto, um pequeno resumo gramatical. Quem a lê inteira sabe declinar ou conjugar a palavra; quem lê só a primeira forma e pula para a tradução terá problemas mais adiante. Nesta seção você aprende a ler essa linha nas três classes que já conhece: nomes, adjetivos e verbos.</p>
<h3>Nomes: nominativo, genitivo, gênero</h3>
<p>Para um nome, o dicionário dá o <b>nominativo singular</b>, logo depois a terminação do <b>genitivo singular</b> e, por fim, o <b>gênero</b> abreviado. O Pe. Ravizza descreve exatamente esse formato e acrescenta que, quando o nome não tem singular, o verbete começa pelo nominativo plural (Ravizza n. 17). Cada parte responde a uma pergunta diferente. O <b>genitivo</b> diz a declinação, porque as cinco declinações se distinguem justamente pela terminação do genitivo singular (<i>-ae</i>, <i>-ī</i>, <i>-is</i>, <i>-ūs</i>, <i>-ēī</i> ou <i>-eī</i>; Bennett § 18; A&amp;G §§ 37 e 39), e mostra o <b>tema</b>: tirando a terminação do genitivo, sobra a parte da palavra a que se acrescentam as terminações de todos os casos (Ravizza n. 17; A&amp;G § 37.a dá essa regra para os temas em consoante e, nos temas em vogal, inclui no tema a vogal característica: <i>rosā-</i>). O <b>gênero</b> diz como os adjetivos vão concordar, e não se deduz da terminação: <i>nauta</i> termina em <i>-a</i> e é masculino.</p>
{tabela(['Verbete', 'Declinação (pelo genitivo)', 'Tema', 'O que mais o verbete ensina'], [
    ['rosa, -ae, f.', '1ª (<i>-ae</i>)', 'ros-', 'o caso típico: nominativo, genitivo, gênero'],
    ['nauta, -ae, m.', '1ª (<i>-ae</i>)', 'naut-', 'o gênero vem do verbete, não da terminação <i>-a</i>'],
    ['dominus, -ī, m.', '2ª (<i>-ī</i>)', 'domin-', 'masculino em <i>-us</i>'],
    ['ager, agrī, m.', '2ª (<i>-ī</i>)', 'agr-', 'o genitivo vem por extenso porque o tema perde o <i>e</i> do nominativo'],
    ['puer, -ī, m.', '2ª (<i>-ī</i>)', 'puer-', 'aqui o <i>e</i> fica: basta acrescentar <i>-ī</i>'],
    ['bellum, -ī, n.', '2ª (<i>-ī</i>)', 'bell-', 'neutro: nominativo = acusativo'],
    ['arma, -ōrum, n. pl.', '2ª (genitivo plural <i>-ōrum</i>)', 'arm-', 'só se usa no plural; o verbete começa pelo nominativo plural'],
], 'Como ler o verbete de um nome', latim_cols=(0,))}
<p>Repare em <i>ager, agrī</i> e <i>puer, puerī</i>, que você viu no capítulo 5: o nominativo é o mesmo tipo de palavra, mas os temas são diferentes, e só o genitivo mostra isso. É por isso que muitos dicionários escrevem o genitivo inteiro quando o tema muda, e só a terminação (<i>-ī</i>) quando basta acrescentá-la. A mesma lógica vai valer, com mais força, na terceira declinação (capítulo 9), em que o nominativo muitas vezes esconde o tema: só o genitivo revela, por exemplo, que o tema de <i>rēx</i> ("rei") é <i>rēg-</i> (<i>rēx, rēgis</i>).</p>
<h3>Adjetivos: as três formas do nominativo</h3>
<p>O adjetivo de primeira classe aparece com as três formas do nominativo singular, masculino, feminino e neutro, quase sempre abreviadas: <i>bonus, -a, -um</i>. Nos adjetivos em <i>-er</i>, o feminino abreviado faz o papel que o genitivo faz nos nomes, porque mostra se o <i>e</i> fica ou cai: <i>pulcher, -chra, -chrum</i> (tema <i>pulchr-</i>, como <i>ager</i>) e <i>līber, -era, -erum</i> (tema <i>līber-</i>, como <i>puer</i>). A declinação é a que o capítulo 5 apresentou: masculino e neutro na 2ª, feminino na 1ª (Bennett §§ 63–65).</p>
<h3>Verbos: as partes principais</h3>
<p>O verbo aparece pelas <b>partes principais</b>: a 1ª pessoa do singular do presente, o infinitivo presente, o perfeito e uma quarta forma ligada ao particípio (Bennett § 99; A&amp;G § 172), que Ravizza chama de "tempos primitivos" (n. 84). O capítulo 6 já mostrou por que as duas primeiras bastam por enquanto: a 1ª pessoa sozinha engana (<i>amō</i> e <i>regō</i> terminam igual), e o infinitivo decide a conjugação (<i>amāre</i>, <i>monēre</i>, <i>regere</i>, <i>audīre</i>; <i>capiō, capere</i> é a 3ª em <i>-iō</i>). O perfeito e a quarta forma serão estudados no capítulo 13; até lá, leia-os no verbete e siga adiante.</p>
<p>O que muda de um dicionário para outro é o formato, não a informação. Compare o mesmo verbo em três ferramentas que você vai usar:</p>
{comparacao('O mesmo verbo, três formatos de verbete', ['Onde', 'Como aparece', 'O que observar'], [
    ['Lista DCC', '<i>amō -āre</i>; <i>videō vidēre vīdī vīsum</i>', 'nos verbos regulares da 1ª conjugação dá só o infinitivo abreviado: o resto é previsível'],
    ['Lewis &amp; Short', '<i>ămo, āvi, ātum, 1, v. a.</i>', 'não escreve o infinitivo: o número <b>1</b> indica a conjugação; marca também as breves (ă); escreve <i>v</i> e <i>j</i> consonantais'],
    ["Whitaker's Words", '<i>porto, portare, portavi, portatus</i>', 'sem macrons; a quarta forma é o particípio em <i>-us</i>, e não a forma em <i>-um</i> dos dicionários'],
])}
{observacao('Por que a quarta forma varia?', 'As gramáticas não concordam sobre qual forma citar. Bennett (§ 99) dá o particípio perfeito; Allen &amp; Greenough (§ 172) preferem o neutro em <i>-um</i> (o "supino"), ou o particípio futuro quando o primeiro não existe; Whitaker cita o particípio masculino (<i>portatus</i>). São três maneiras de mostrar o mesmo tema (<i>portāt-</i>). Você só precisa saber que é a mesma informação, e o capítulo 13 explica o resto.')}
<h3>As abreviaturas</h3>
<p>Os dicionários economizam espaço com abreviaturas, quase sempre de palavras latinas ou inglesas. As listas completas ficam no começo de cada dicionário; as mais frequentes são estas:</p>
{tabela(['Abreviatura', 'Significa', 'Exemplo ou comentário'], [
    ['m. · f. · n.', 'masculino · feminino · neutro', '<i>nauta, -ae, m.</i>'],
    ['comm. ou c.', 'comum de dois (masculino ou feminino conforme a pessoa)', 'Lewis &amp; Short: <i>cīvis, is, comm.</i>, "cidadão, cidadã"; na lista do L&amp;S, <i>c.</i> também abrevia <i>cum</i> ("com")'],
    ['sing. · pl. (plur.)', 'singular · plural', '<i>arma, -ōrum, n. pl.</i>: só tem plural'],
    ['gen. · dat. · acc. (ac.) · abl.', 'os casos', 'aparecem na regência: "<i>cum</i> + abl."'],
    ['adj. · adv. · prep. · conj. · interj.', 'adjetivo · advérbio · preposição · conjunção · interjeição', '<i>ad</i>, prep. + acc.'],
    ['indecl.', 'indeclinável: uma só forma para todos os casos', 'Lewis &amp; Short: <i>nēquam, adj. indecl.</i>, "imprestável"'],
    ['1 · 2 · 3 · 4 (depois de um verbo)', 'a conjugação', 'Lewis &amp; Short: <i>mŏnĕo, ŭi, ĭtum, 2</i>'],
    ['v. a. · v. n.', 'verbo ativo (transitivo) · verbo neutro (intransitivo): na lista do L&amp;S, <i>v.</i> = <i>verb</i>, <i>a.</i> = <i>active</i>, <i>n.</i> = <i>neuter</i>', 'Lewis &amp; Short: <i>ămo … 1, v. a.</i>; <i>ambŭlo … 1, v. n.</i>'],
    ['intr. · intrans.', 'intransitivo', '<i>intr.</i> na lista do Lewis &amp; Short; <i>intrans.</i> na do <i>Elementary Latin Dictionary</i>. Cuidado: no Lewis &amp; Short, <i>trans.</i> quer dizer "traduzido" (<i>translated</i>), não "transitivo"'],
    ['dep.', 'depoente: forma passiva, sentido ativo', 'Lewis &amp; Short: <i>hortor, ātus, 1, v. dep.</i> (capítulo 25)'],
    ['impers.', 'impessoal: só na 3ª pessoa do singular', 'verbos como "chove"'],
    ['freq.', 'frequentativo: verbo derivado que indica ação repetida ou intensa', 'Lewis &amp; Short classifica <i>porto</i> como <i>v. freq. a.</i>'],
    ['comp. · sup.', 'comparativo · superlativo', 'formas como "melhor", "ótimo" (capítulo 18); no Lewis &amp; Short, <i>comp.</i> também é "compare" e <i>sup.</i> também é "supino"'],
    ['lit. · trop. (fig.)', 'sentido literal · sentido figurado', 'os sentidos vêm numerados: I, II, A, B, 1, 2…'],
    ['cf. · v. · syn.', '<i>cōnfer</i> (compare) · <i>vidē</i> (veja) · sinônimos', 'remetem a outro verbete; no Lewis &amp; Short, <i>v.</i> pode ser <i>vidē</i>, <i>verb</i> ou <i>vox</i>, e o contexto decide'],
    ['Cic. · Caes. · Verg. · Ov. · Vulg.', 'Cícero · César · Virgílio · Ovídio · Vulgata', 'abreviaturas de autores e obras: indicam onde o sentido está documentado'],
], 'Abreviaturas frequentes nos dicionários latinos', latim_cols=(0,))}
'''),
        ('Da forma do texto ao verbete: o caminho de volta', f'''
<p>No texto você não encontra <i>ager</i>, encontra <i>agrōs</i>; não encontra <i>capiō</i>, encontra <i>capiunt</i>. Procurar <i>agrōs</i> no dicionário não dá em nada. O trabalho é fazer de trás para frente o que a declinação e a conjugação fazem: separar a terminação, levantar hipóteses e reconstruir a forma de citação. Feito com método, ele quase nunca falha, e é ele que distingue quem lê de quem adivinha.</p>
{diagrama_frase([('agrōs', 'forma no texto'), ('agr- + -ōs', 'tema · terminação'), ('-ōs: ac. pl.', 'hipótese · 2ª declinação'), ('ager, agrī, m.', 'verbete · confere o tema agr-'), ('"os campos"', 'sentido · escolhido no contexto')], 'O caminho de volta, num exemplo: da forma <i>agrōs</i> ao verbete <i>ager, agrī</i> e ao sentido.')}
<p>Os passos, um a um:</p>
<ol>
<li><b>Classe da palavra.</b> Pela terminação e pela posição, é nome, adjetivo ou verbo? Terminações pessoais (<i>-ō, -s, -t, -mus, -tis, -nt</i>) apontam para verbo; terminações de caso, para nome ou adjetivo. Algumas formas servem para os dois, e aí entram os homógrafos (seção 3).</li>
<li><b>Separe a terminação.</b> Use as tabelas dos capítulos 3 a 6. Em <i>agrōs</i>, a terminação <i>-ōs</i> é acusativo plural da 2ª declinação; o que sobra, <i>agr-</i>, é o tema provável.</li>
<li><b>Liste as hipóteses.</b> Uma terminação raramente tem uma só leitura. <i>-ae</i> pode ser genitivo ou dativo singular ou nominativo plural da 1ª; <i>-unt</i> pode ser presente da 3ª, da 3ª em <i>-iō</i> ou da 4ª conjugação. Anote todas antes de escolher.</li>
<li><b>Reconstrua a forma de citação.</b> Para cada hipótese, monte o nominativo singular (nomes), o masculino singular (adjetivos) ou a 1ª pessoa do presente (verbos). Do tema <i>agr-</i> da 2ª declinação saem dois candidatos: <i>agrus</i> ou <i>ager</i>.</li>
<li><b>Confira no verbete.</b> Procure os candidatos. <i>Agrus</i> não existe; <i>ager, agrī</i> existe e o genitivo confirma o tema <i>agr-</i>. Se o tema do verbete não bate com o que você separou, a hipótese está errada.</li>
<li><b>Escolha o sentido pelo contexto.</b> O verbete traz vários sentidos ("campo", "território", "propriedade"); fique com o que a frase pede.</li>
</ol>
<p>O passo 5 é o que muitos pulam, e é o mais importante. Conferir o tema é o que impede, por exemplo, de achar que <i>librōs</i> vem de <i>līber</i>, "livre": o genitivo <i>librī</i> mostra que o tema de <i>liber</i>, "livro", perde o <i>e</i>, enquanto <i>līber, -era, -erum</i> o conserva (<i>līberōs</i>). As duas palavras são parecidas no nominativo e se separam no tema.</p>
{dica('<b>Os macrons do dicionário servem para conferir.</b> A maioria dos textos que você vai ler não tem macrons; o dicionário tem. Depois de achar o verbete, releia a forma do texto com as quantidades do verbete: isso confirma a pronúncia e às vezes desfaz a dúvida (<i>līberōs</i> com <i>ī</i> longo, <i>librōs</i> sem o <i>e</i>).')}
'''),
        ('Homógrafos, grafias variantes e o enclítico -que', f'''
<h3>Homógrafos: duas palavras, a mesma forma</h3>
<p><b>Homógrafos</b> são formas que se escrevem igual e pertencem a palavras diferentes. O latim tem muitos, porque as mesmas terminações servem a nomes e verbos e porque, sem macrons, vogais longas e breves se confundem. Alguns que você já pode reconhecer:</p>
{comparacao('Homógrafos com o vocabulário dos capítulos 3 a 6', ['Forma', 'Leitura 1', 'Leitura 2', 'Como decidir'], [
    ['portās', '<i>porta, -ae</i> (f.), "porta, portão": acusativo plural', '<i>portō, -āre</i>, "carregar": 2ª pessoa singular do presente', 'há outro verbo na frase? há um "tu" como sujeito?'],
    ['servō', '<i>servus, -ī</i> (m.), "escravo": dativo ou ablativo singular', '<i>servō, -āre</i>, "guardar, conservar": 1ª pessoa singular', 'o verbo da frase já existe? há um verbo de dar ou dizer?'],
    ['amīcae', '<i>amīca, -ae</i> (f.), "amiga": gen. ou dat. sing., nom. pl.', '<i>amīcus, -a, -um</i>, "amigo, amigável": feminino, mesmos casos', 'concorda com algum nome feminino?'],
    ['līberōs · librōs', '<i>līber, -era, -erum</i>, "livre"; <i>līberī</i>, "os filhos"', '<i>liber, librī</i> (m.), "livro"', 'o tema: <i>līber-</i> conserva o <i>e</i>, <i>libr-</i> não'],
    ['malum · mālum', '<i>malus, -a, -um</i>, "mau"; <i>malum, -ī</i> (n.), "o mal"', '<i>mālum, -ī</i> (n.), "maçã"', 'a quantidade (no dicionário) e o sentido da frase'],
])}
<p>O contexto decide, e decide quase sempre pelo mesmo raciocínio por exclusão que você aprendeu no capítulo 3. Em <i>Nautae portās spectant</i>, o verbo já existe (<i>spectant</i>, "olham") e o sujeito é plural; <i>portās</i> não pode ser "carregas", e é "as portas". Em <i>Aquam portās</i>, não há outro verbo; <i>portās</i> é "(tu) carregas". Os analisadores automáticos, como o Whitaker's Words, listam as duas leituras de <i>portās</i> e de <i>servō</i> sem escolher entre elas: a escolha é sua.</p>
<h3>u ou v, i ou j</h3>
<p>Os romanos escreviam com a mesma letra o <i>i</i> vogal e o <i>i</i> consoante, e com a mesma letra o <i>u</i> vogal e o <i>u</i> consoante (V). As edições modernas resolveram isso de maneiras diferentes, e o dicionário que você abrir pode seguir uma convenção diferente da do seu texto. Bennett escreve <i>j</i> e <i>v</i> para as consoantes, mas reconhece que muitos estudiosos usam <i>i</i> e <i>u</i> para tudo (§ 1.2); Allen &amp; Greenough usam <i>i</i> para os dois sons e distinguem <i>u</i> de <i>v</i> (§ 1.b); a lista DCC escreve <i>iaciō</i>; o Lewis &amp; Short escreve <i>jacio</i>, e na edição do Perseus a busca por <i>iacio</i> não encontra o verbete. Algumas edições de textos clássicos usam <i>u</i> para os dois sons e escrevem <i>uiuit</i> onde outras escrevem <i>vīvit</i>.</p>
<p>A regra prática é simples: se uma palavra começada por <i>i</i> + vogal não aparece, procure com <i>j</i> (e vice-versa); se uma palavra com <i>u</i> + vogal não aparece, procure com <i>v</i>. O mesmo vale para outras grafias que conviviam na mesma época, como <i>epistula</i> e <i>epistola</i>, <i>exspectō</i> e <i>expectō</i> (Bennett § 9.2), e para os compostos com prefixo, que você verá na seção 4.</p>
<h3>O enclítico -que</h3>
<p><i>-que</i> quer dizer "e", mas não é uma palavra separada: é um <b>enclítico</b>, que se cola ao fim da palavra seguinte à que ele liga. <i>Puerī puellaeque</i> é "os meninos e as meninas"; <i>arma virumque</i>, "as armas e o homem". Quando liga duas orações, cola-se à primeira palavra da segunda, mas, se essa palavra for uma preposição, passa para a palavra seguinte (Bennett § 341.2.a; A&amp;G § 224.a). Bennett observa ainda que <i>-que</i> une mais estreitamente que <i>et</i>, de preferência coisas que formam um par natural (§ 341.1.b), e a lista DCC põe <i>-que</i> entre as cinco palavras mais frequentes do latim (posição 4).</p>
<p>Na consulta, a regra é: <b>tire o <i>-que</i> antes de procurar</b>. <i>Agrōsque</i> se procura como <i>agrōs</i> (→ <i>ager</i>); <i>servatque</i>, como <i>servat</i> (→ <i>servō, -āre</i>). Mas cuidado com as palavras que terminam em <i>-que</i> e não têm enclítico nenhum, como <i>atque</i> ("e também"), <i>neque</i> ("e não") e <i>quoque</i> ("também"): se, tirando o <i>-que</i>, o que sobra não existe ou não faz sentido, procure a palavra inteira. Na pronúncia, o enclítico atrai o acento para a sílaba anterior quando ela é longa: <i>virúmque</i>, e em <i>puellaeque</i> o acento cai no ditongo <i>-lae-</i> (Bennett § 6.3). Os enclíticos <i>-ne</i> (pergunta) e <i>-ve</i> ("ou") funcionam do mesmo modo, e você os verá mais adiante.</p>
'''),
        ('Prefixos e famílias de palavras', f'''
<p>Boa parte do vocabulário latino é feita de peças. Um verbo simples recebe uma preposição na frente e vira um verbo novo, com sentido previsível a partir das duas partes (A&amp;G § 267.a; Bennett § 159.3.e; Ravizza n. 159). Isso tem duas consequências para quem usa o dicionário: o composto tem verbete próprio (procure <i>importō</i> em <i>i</i>, e não em <i>portō</i>), e, conhecendo o verbo simples e o prefixo, você muitas vezes adivinha o sentido do composto antes de abri-lo.</p>
{tabela(['Prefixo', 'Sentido básico', 'Família de portō, "carregar"', 'Família de vocō, "chamar"', 'Português'], [
    ['in-', 'em, para dentro; contra', '<i>importō</i>, levar para dentro', '<i>invocō</i>, chamar por, invocar', 'importar, invocar'],
    ['ad-', 'para, junto a', '<i>apportō</i>, trazer para junto', '<i>advocō</i>, chamar para junto (como auxiliar)', 'advogado'],
    ['con- (com-, co-)', 'junto; por completo', '<i>comportō</i>, levar junto, reunir', '<i>convocō</i>, chamar todos juntos', 'comportar, convocar'],
    ['ex- (ē-)', 'para fora', '<i>exportō</i>, levar para fora', '<i>ēvocō</i>, chamar para fora', 'exportar, evocar'],
    ['re- (red-)', 'para trás; de novo', '<i>reportō</i>, levar de volta', '<i>revocō</i>, chamar de volta', 'reportar, revogar'],
    ['dē-', 'de cima para baixo; para longe; por completo', '<i>dēportō</i>, levar embora', '<i>dēvocō</i>, chamar para baixo; chamar para longe, desviar', 'deportar'],
], 'Seis prefixos e duas famílias de palavras', latim_cols=(0,))}
<p>Dois avisos. Primeiro, o prefixo <i>in-</i> tem dois homônimos: diante de verbos é a preposição ("em, para dentro"); diante de adjetivos é quase sempre <b>negativo</b>, "não", como em <i>inimīcus</i> ("não amigo, inimigo"), <i>impūrus</i> ("impuro"), <i>indignus</i> ("indigno"). Ravizza alerta para não confundir os dois (n. 160c), e Allen &amp; Greenough tratam o <i>in-</i> negativo à parte (§ 267.d). Segundo, <i>re-</i> e <i>dis-</i> nunca aparecem sozinhos: são partículas <b>inseparáveis</b>, que só existem em composição (Bennett § 159, nota; A&amp;G § 267.b).</p>
<h3>Assimilação e mudança de vogal</h3>
<p>Quando o prefixo termina em consoante e o verbo começa por outra, a primeira muitas vezes se <b>assimila</b> à segunda, isto é, torna-se igual a ela ou parecida com ela, para facilitar a pronúncia (Bennett § 8.4–5; A&amp;G § 16): <i>ad</i> + <i>portō</i> dá <i>apportō</i>; <i>con</i> + <i>mittō</i>, <i>committō</i>; <i>in</i> + <i>portō</i>, <i>importō</i> (diante de <i>b, m, p</i>, o <i>n</i> vira <i>m</i>); <i>ex</i> + <i>ferō</i>, <i>efferō</i>. O português herdou o fenômeno: "acorrer" (de <i>accurrō</i>, <i>ad</i> + <i>currō</i>), "cometer", "importar". A assimilação nem sempre foi escrita: Bennett mostra que os compostos com preposição podiam ser grafados com ou sem ela, <i>ad-serō</i> ou <i>asserō</i>, <i>in-lātus</i> ou <i>illātus</i> (§ 9.2). Por isso o Lewis &amp; Short registra <i>ap-porto</i> e informa, no próprio verbete, que alguns editores escrevem <i>adp-</i>. Se você não acha uma palavra com <i>app-</i>, <i>coll-</i>, <i>imm-</i>, procure a forma sem assimilação (<i>adp-</i>, <i>conl-</i>, <i>inm-</i>), e vice-versa.</p>
<p>A vogal do verbo também pode mudar no composto: o <i>a</i> breve se enfraquece em <i>i</i> diante de uma consoante (A&amp;G § 267, nota 2; Bennett § 7.1.b). Assim, de <i>capiō</i> ("pegar") vêm <i>accipiō</i> ("receber"), <i>recipiō</i> ("retomar, receber") e <i>incipiō</i> ("começar"); de <i>faciō</i> ("fazer"), <i>cōnficiō</i> ("concluir"). Quem procura <i>accipiunt</i> e só pensa em <i>capiō</i> não acha nada; quem conhece a regra reconhece a família e procura <i>accipiō</i>.</p>
<h3>Cognatos e falsos amigos</h3>
<p>Para quem fala português, a maior parte do vocabulário latino tem parentes conhecidos, os <b>cognatos</b>: <i>aqua</i>, água; <i>terra</i>, terra; <i>vīta</i>, vida; <i>oculus</i>, olho; <i>populus</i>, povo; <i>liber</i>, livro. Use-os para lembrar, não para traduzir, porque o sentido mudou em muitas palavras ao longo de dois mil anos. Esses são os <b>falsos amigos</b>, palavras de forma parecida e sentido diferente:</p>
{comparacao('Falsos amigos frequentes', ['Latim', 'Parece', 'Quer dizer', 'Exemplo'], [
    ['studium, -ī, n.', 'estudo', 'empenho, dedicação, gosto por algo', '<i>studium agricolae</i>: a dedicação do agricultor'],
    ['cūra, -ae, f.', 'cura (de doença)', 'cuidado, preocupação', '<i>cūra puerōrum</i>: o cuidado com os meninos'],
    ['officium, -ī, n.', 'ofício, escritório', 'dever, serviço prestado', '<i>officium servī</i>: o dever do escravo'],
    ['līberī, -ōrum, m. pl.', 'livres', 'os filhos', '<i>līberī dominī</i>: os filhos do senhor'],
    ['parentēs (de parēns, -entis, c.)', 'parentes', 'os pais (pai e mãe)', 'terceira declinação: capítulo 9'],
    ['familia, -ae, f.', 'família (pais e filhos)', 'todos os da casa, inclusive os escravos', '<i>familia dominī</i>: a casa do senhor, com seus escravos'],
])}
{dica('<b>Esperar e esperar.</b> O português usa "esperar" para duas ideias que o latim separa: <i>exspectō, -āre</i>, "aguardar" (de <i>ex-</i> + <i>spectō</i>, "olhar para fora", ficar de olho em quem vem), e <i>spērō, -āre</i>, "ter esperança". O prefixo de <i>exspectō</i> explica o sentido.')}
'''),
        ('O vocabulário básico: frequência e método', f'''
<p>O latim conservado tem dezenas de milhares de palavras, mas umas poucas centenas formam a maior parte de qualquer texto. A <b>DCC Latin Core Vocabulary</b>, preparada no Dickinson College sob a coordenação de Christopher Francese, reúne cerca de mil lemas mais frequentes da língua, que, segundo a apresentação da lista, geram aproximadamente 70% das formas de um texto latino típico. A mesma página cita estudos segundo os quais cerca de 250 palavras já respondem pela metade de um texto. A ordem de frequência vem de um levantamento estatístico feito em Liège sobre cerca de 800 mil palavras de autores clássicos (os dados LASLA), e não da intuição de quem montou a lista.</p>
<p>Veja as primeiras posições, que confirmam o que você já percebeu nas frases dos capítulos anteriores:</p>
{tabela(['Posição', 'Verbete na lista DCC', 'Sentido'], [
    ['1', 'et', 'e'], ['2', 'sum esse fuī futūrum', 'ser, existir'], ['4', '-que', 'e (enclítico)'], ['5', 'in', 'em, sobre (+ abl.); para dentro de, para (+ ac.)'],
    ['6', 'nōn', 'não'], ['10', 'cum', 'com (prep. + abl.)'], ['14', 'ad', 'para, até (+ ac.)'],
], 'Algumas das palavras mais frequentes do latim, segundo a lista DCC', latim_cols=(1,))}
<p>A lista tem uma versão em português (tradução de Vittorio Pastelli), em que cada verbete traz o sentido, a classificação (por exemplo, "Substantivo: 2a Declinação" ou "Verbo: 3a Conjugação -iō"), um grupo semântico ("A Casa", "Guerra e Paz", "Movimento") e a posição de frequência. É possível filtrar por classificação e por grupo, e baixar tudo como planilha. As traduções são úteis, mas foram feitas a partir do inglês e algumas ficaram imprecisas (<i>mittō</i>, por exemplo, aparece como "remeter, livrar", quando o sentido básico é "enviar"): confira sempre no dicionário as palavras que você for decorar.</p>
<h3>Como estudar o vocabulário</h3>
<p>A experiência dos professores e o próprio formato dos verbetes sugerem um método:</p>
<ul>
<li><b>Aprenda o verbete inteiro, nunca só a palavra.</b> Para um nome, nominativo, genitivo e gênero (<i>ager, agrī, m.</i>); para um adjetivo, as três formas (<i>līber, -era, -erum</i>); para um verbo, pelo menos as duas primeiras partes (<i>capiō, capere</i>), e as quatro quando chegar ao capítulo 13. Saber só <i>ager</i> = "campo" não permite reconhecer <i>agrōs</i>.</li>
<li><b>Pela frequência, não pela ordem alfabética.</b> Comece pelas cem primeiras posições da lista e avance em blocos. Quando uma palavra do texto estiver na lista, ela merece ser decorada; quando for rara, basta entendê-la ali.</li>
<li><b>Em famílias.</b> Junte o simples e os compostos (<i>portō, importō, exportō, reportō</i>), o nome e o adjetivo (<i>amīcus, amīca, inimīcus</i>). Uma palavra aprendida assim traz outras de graça.</li>
<li><b>Com um cognato ou uma imagem.</b> "Agrário" para <i>ager</i>; "pueril" para <i>puer</i>. Mas anote ao lado os falsos amigos, para não cair neles.</li>
<li><b>Em frases, não em listas soltas.</b> Escreva cada palavra nova numa frase curta que você entenda (<i>Agricola agrōs servat</i>). Reveja em intervalos crescentes: no dia seguinte, depois de três dias, depois de uma semana.</li>
<li><b>Lendo muito.</b> A lista diz o que priorizar; quem fixa o vocabulário é a leitura. As palavras frequentes voltam sozinhas, centenas de vezes, nos textos graduados indicados ao fim de cada capítulo.</li>
</ul>
'''),
        ('As ferramentas gratuitas e uma frase autêntica', f'''
<p>O catálogo da Bibliotheca Latina reúne as ferramentas gratuitas que você vai usar daqui em diante. Cada uma faz uma coisa bem e outra mal; conhecer os limites é o que permite usá-las com proveito.</p>
{tabela(['Ferramenta', 'O que faz', 'Quando usar', 'Cuidado'], [
    ["Whitaker's Words", 'analisador morfológico: recebe uma forma flexionada, devolve todas as análises possíveis e o verbete de cada uma, em inglês', 'para conferir uma análise que você já fez, ou quando não consegue chegar ao lema (por exemplo, um tema irregular)', 'lista tudo, sem escolher; não usa macrons; inclui palavras raras e medievais'],
    ['Logeion', 'busca o lema em vários dicionários ao mesmo tempo, entre eles o Lewis &amp; Short, o <i>Elementary Latin Dictionary</i> e o Du Cange (latim medieval)', 'depois de saber o lema, para ver os sentidos, a regência e exemplos', 'você precisa chegar à forma de citação primeiro (seção 2)'],
    ['Lewis &amp; Short', 'o grande dicionário latim-inglês de 1879, com abonações dos autores', 'para sentidos raros, construções e o latim cristão', 'escreve <i>j</i> e <i>v</i>; indica a conjugação por número; separa os homógrafos em verbetes numerados (o adjetivo <i>līber</i> remete a "2. Liber", o deus Líber)'],
    ['Lista DCC', 'as mil palavras mais frequentes, com sentido em português', 'para decidir o que decorar', 'traduções a conferir'],
    ['Ravizza, <i>Gramática Latina</i>', 'gramática em português que explica como o dicionário registra nomes e verbos (n. 17 e 84)', 'para entender o verbete em português', 'não é dicionário; é o manual para lê-lo'],
], 'Ferramentas gratuitas do catálogo', latim_cols=())}
<h3>O analisador não analisa por você</h3>
<p>Ponha no Whitaker's Words a forma <i>virumque</i>. Ele separa corretamente o enclítico <i>-que</i>, e depois oferece três leituras de <i>virum</i>: acusativo singular de <i>vir, virī</i>, "homem"; nominativo ou acusativo de um <i>virum, -ī</i>, "vírus", que o próprio programa marca como latim moderno e pouco comum; e genitivo plural de <i>vīs</i>, "força", uma forma que o programa gera pela regra mas que o latim clássico não usa (o genitivo plural atestado é <i>vīrium</i>, com <i>ī</i> longo). E falta uma leitura útil: em poesia, <i>virum</i> pode ser genitivo plural de <i>vir</i>, forma antiga de <i>virōrum</i>. Para <i>canō</i>, devolve, antes do verbo "cantar", formas de dativo e ablativo de dois nomes raros e de um adjetivo <i>cānus</i>, "grisalho". Algumas dessas leituras são possíveis como morfologia, uma é teórica, e quase todas estão erradas na frase. O programa não lê a frase: ele só conhece a palavra isolada.</p>
<p>Daí a regra de ouro deste capítulo: <b>analise primeiro, consulte depois</b>. Escreva no caderno a sua hipótese (classe, caso ou pessoa, lema) e só então abra a ferramenta, para confirmar ou corrigir. Usado assim, o analisador é um professor paciente; usado antes de pensar, ele é uma muleta que impede de aprender a andar. O capítulo 8 mostra quando abrir o dicionário durante a leitura de um texto inteiro.</p>
<h3>Uma frase autêntica, verbete a verbete</h3>
<p>O primeiro verso da <i>Eneida</i> de Virgílio começa assim:</p>
{exemplos([('Arma virumque canō…', 'Canto as armas e o herói… (Virgílio, <i>En.</i> 1.1)')])}
{analise('Eneida 1.1: o que o dicionário diz de cada palavra', [
    ('Arma', 'arma, -ōrum, n. pl., armas', 'acusativo plural, 2ª declinação (neutro: igual ao nominativo)', 'objeto direto de <i>canō</i>'),
    ('virum', 'vir, virī, m., homem, herói', 'acusativo singular, 2ª declinação', 'objeto direto, coordenado a <i>arma</i>'),
    ('-que', '-que, conj. enclítica, e', 'invariável', 'liga <i>virum</i> a <i>arma</i>'),
    ('canō', 'canō, -ere (3ª), cantar, celebrar em versos', 'presente do indicativo, 1ª pessoa do singular', 'verbo da oração: "(eu) canto"'),
])}
<p>Três decisões dependem do verbete e do contexto, e não do analisador. <i>Arma</i> poderia ser nominativo ou acusativo plural (neutro), e o Whitaker's Words acrescenta ainda o imperativo de um verbo <i>armō</i>, "armar"; mas a frase já tem um verbo, <i>canō</i>, cuja 1ª pessoa diz que o sujeito é "eu": <i>arma</i> só pode ser o que se canta, o objeto. <i>Virum</i> se decide pelo <i>-que</i>, que coordena palavras no mesmo caso: ligado a <i>arma</i>, é outro objeto, e o verbete de <i>vir</i> oferece, entre os sentidos, "herói", que é o que a epopeia pede. E <i>arma</i> se procura no nominativo plural, porque o verbete, como ensina Ravizza (n. 17), começa pelo plural quando a palavra não tem singular.</p>
'''),
    ],
    erros_comuns=[
        ('Procurar no dicionário a forma exatamente como está no texto (<i>agrōs</i>, <i>capiunt</i>, <i>portās</i>).', 'O dicionário só registra o lema. Separe a terminação, reconstrua o nominativo singular ou a 1ª pessoa do presente e procure essa forma. Se não souber reconstruí-la, use o analisador para descobrir o lema, mas anote antes a sua hipótese.'),
        ('Ler só a primeira palavra do verbete e pular para a tradução.', 'O genitivo, o gênero e o infinitivo são a parte gramatical do verbete. Sem o genitivo <i>agrī</i>, você não reconhece <i>agrōs</i>; sem o gênero <i>m.</i> de <i>nauta</i>, erra a concordância; sem o infinitivo <i>capere</i>, conjuga <i>capiō</i> como <i>audiō</i>.'),
        ("Aceitar a primeira resposta do Whitaker's Words, ou o primeiro sentido do verbete.", 'O analisador lista todas as possibilidades na ordem dele, não na da frase (para <i>canō</i> ele começa por um nome que significa "cabelos brancos"). O dicionário põe primeiro o sentido etimológico, não o mais comum. Teste cada leitura na frase e fique com a que cabe na construção.'),
        ('Traduzir pelo cognato português: <i>studium</i> = "estudo", <i>cūra</i> = "cura", <i>līberī</i> = "livres".', 'Os cognatos ajudam a lembrar, mas o sentido mudou em muitas palavras. Confira no verbete: <i>studium</i> é "empenho", <i>cūra</i> é "cuidado", <i>līberī</i> (substantivo) são "os filhos". Desconfie quando a tradução pelo cognato deixa a frase estranha.'),
        ('Concluir que uma palavra "não existe" porque não está no dicionário com aquela grafia.', 'Tire o enclítico (<i>agrōsque</i> → <i>agrōs</i>), troque <i>i</i>/<i>j</i> e <i>u</i>/<i>v</i> (<i>iacit</i> → <i>jacio</i> no Lewis &amp; Short), desfaça a assimilação do prefixo (<i>apportō</i> / <i>adportō</i>) e lembre o enfraquecimento da vogal (<i>accipiō</i> é da família de <i>capiō</i>).'),
        ('Tirar o <i>-que</i> de toda palavra que termina assim.', '<i>Atque</i>, <i>neque</i> e <i>quoque</i> são palavras inteiras, com verbete próprio. Se o que sobra depois de tirar o <i>-que</i> não existe (<i>at</i> existe, mas não faz sentido ali; <i>ne</i>, <i>quo</i>…), procure a palavra inteira.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Três consultas, passo a passo',
            'Encontre o verbete de cada forma destacada e traduza a frase. Vocabulário já visto: <i>nauta</i>, marinheiro; <i>spectō, -āre</i>, olhar; <i>agricola</i>, agricultor; <i>videō, -ēre</i>, ver; <i>puer, -ī</i>, menino; <i>mālum, -ī</i> (n.), maçã. As frases: (a) <i lang="la">Nautae <b>portās</b> spectant.</i> (b) <i lang="la">Agricola <b>līberōs</b> in agrō videt.</i> (c) <i lang="la">Puerī māla <b>capiunt</b>.</i>', [
            ('(a) <i>portās</i>: que terminação se pode separar, e que hipóteses ela abre?', '<i>-ās</i>. Pode ser acusativo plural da 1ª declinação (tema <i>port-</i> → <i>porta, -ae</i>) ou 2ª pessoa do singular do presente da 1ª conjugação (<i>portō, -āre</i>, "tu carregas"). São duas palavras diferentes: um homógrafo.'),
            ('(a) Qual das duas a frase aceita?', 'A frase já tem verbo, <i>spectant</i>, com sujeito plural (<i>nautae</i>). Uma segunda forma verbal de 2ª pessoa não tem lugar; <i>portās</i> é o objeto de <i>spectant</i>: verbete <i>porta, -ae, f.</i> "Os marinheiros olham as portas (da cidade)."'),
            ('(b) <i>līberōs</i>: separe a terminação e reconstrua os candidatos.', '<i>-ōs</i>: acusativo plural masculino da 2ª declinação. Tema <i>līber-</i>. Candidatos ao nominativo: <i>līberus</i> ou <i>līber</i>. O verbete existente é <i>līber, -era, -erum</i>, "livre", que conserva o <i>e</i> (o tipo de <i>puer</i>).'),
            ('(b) Poderia ser <i>liber, librī</i>, "livro"?', 'Não: o tema de "livro" é <i>libr-</i> (acusativo plural <i>librōs</i>), sem o <i>e</i>. Conferir o tema exclui a hipótese. E o adjetivo, aqui sem nome a que se ligue, está usado como substantivo: o masculino plural <i>līberī</i> quer dizer "os filhos" (capítulo 5). "O agricultor vê os filhos no campo."'),
            ('(c) <i>capiunt</i>: que conjugações terminam em <i>-iunt</i>?', 'A 4ª (<i>audiunt</i>) e a 3ª em <i>-iō</i> (<i>capiunt</i>). Os dois candidatos ao lema são <i>capiō, capīre</i> (4ª) ou <i>capiō, capere</i> (3ª em <i>-iō</i>). A 1ª pessoa é a mesma; só o infinitivo do verbete decide.'),
            ('(c) O que diz o verbete?', '<i>capiō, capere</i>, com <i>e</i> breve: 3ª conjugação em <i>-iō</i>, "pegar, tomar". <i>Māla</i> é o acusativo plural neutro de <i>mālum</i> (o sujeito é <i>puerī</i>, nominativo plural, de acordo com <i>-unt</i>). "Os meninos pegam as maçãs."'),
        ], 'Repare que em nenhum dos três casos o dicionário sozinho resolveu: ele confirmou um tema ou uma conjugação, e a frase escolheu entre as hipóteses.'),
        pratica_guiada('Prática guiada 2 · Uma frase com -que e um homógrafo',
            'Leia, procure cada palavra e traduza: <i lang="la">Dominus servō pecūniam dat agrōsque servat.</i> Vocabulário: <i>dominus, -ī</i>, senhor; <i>servus, -ī</i>, escravo; <i>pecūnia, -ae</i>, dinheiro; <i>dat</i>, dá; <i>ager, agrī</i>, campo; <i>servō, -āre</i>, guardar, conservar.', [
            ('Quantos verbos há na frase, e quais são?', 'Dois: <i>dat</i> e <i>servat</i>, ambos na 3ª pessoa do singular. O sujeito dos dois é <i>dominus</i>, o único nominativo singular.'),
            ('<i>servō</i>: nome ou verbo?', 'As duas leituras existem: dativo/ablativo de <i>servus</i> ou 1ª pessoa de <i>servō, -āre</i> ("eu guardo"). Um verbo de 1ª pessoa não cabe numa frase cujo sujeito é <i>dominus</i>; e <i>dat</i> pede um destinatário no dativo. É o dativo de <i>servus</i>: "ao escravo".'),
            ('<i>agrōsque</i>: como procurar?', 'Tire o enclítico: <i>agrōs</i> + <i>-que</i>. <i>Agrōs</i> é acusativo plural de <i>ager, agrī</i>. O <i>-que</i> liga a segunda oração à primeira e se colou à primeira palavra dela.'),
            ('<i>servat</i>: qual o verbete, e o que significa aqui?', '<i>servō, -āre</i> (1ª conjugação), "guardar, conservar". É o mesmo verbete que se descartou para <i>servō</i>: agora a forma <i>servat</i> só pode ser verbo. O objeto é <i>agrōs</i>.'),
            ('Monte a tradução.', '"O senhor dá dinheiro ao escravo e conserva os campos." O par <i>servō</i> / <i>servat</i> mostra bem o que é um homógrafo: o mesmo verbete <i>servō, -āre</i> aparece em <i>servat</i>, mas não na forma <i>servō</i> desta frase.'),
        ]),
    ],
    exercicios=[
        exercicio('Exercício 1 · Leia o verbete', 'Para cada verbete, diga a classe, a declinação ou conjugação, o gênero (nos nomes) e o tema, e explique como o verbete mostrou isso.', [
            ('<i>silva, -ae, f.</i>, floresta', 'Nome da 1ª declinação (genitivo <i>-ae</i>), feminino, tema <i>silv-</i>.'),
            ('<i>magister, magistrī, m.</i>, professor', 'Nome da 2ª declinação (genitivo <i>-ī</i>), masculino. O genitivo por extenso mostra que o tema é <i>magistr-</i>: o <i>e</i> do nominativo cai, como em <i>ager</i>.'),
            ('<i>perīculum, -ī, n.</i>, perigo', 'Nome da 2ª declinação, neutro, tema <i>perīcul-</i>. Por ser neutro, nominativo e acusativo são iguais (<i>perīculum</i>; plural <i>perīcula</i>).'),
            ('<i>miser, -era, -erum</i>, infeliz', 'Adjetivo de primeira classe. O feminino <i>-era</i> mostra que o <i>e</i> fica: tema <i>miser-</i>, como <i>līber</i> (e não como <i>pulcher, -chra</i>).'),
            ('<i>teneō, -ēre</i>, segurar', 'Verbo da 2ª conjugação: infinitivo em <i>-ēre</i>, com <i>ē</i> longo.'),
            ('<i>mittō, -ere</i>, enviar', 'Verbo da 3ª conjugação: infinitivo em <i>-ere</i> breve, e a 1ª pessoa não tem <i>i</i> antes do <i>-ō</i>.'),
            ('<i>fugiō, -ere</i>, fugir', 'Verbo da 3ª conjugação em <i>-iō</i>: a 1ª pessoa parece de 4ª (<i>audiō</i>), mas o infinitivo em <i>-ere</i> breve decide.'),
            ('<i>veniō, -īre</i>, vir', 'Verbo da 4ª conjugação: infinitivo em <i>-īre</i>.'),
        ]),
        exercicio('Exercício 2 · Da forma ao verbete', 'Use os verbetes do exercício 1 e os dos capítulos anteriores. Para cada forma, diga a análise (caso e número, ou pessoa e número) e o verbete em que ela se procura.', [
            ('<i>magistrō</i>', 'Dativo ou ablativo singular de <i>magister, magistrī</i>. Tema <i>magistr-</i> + <i>-ō</i>.'),
            ('<i>perīcula</i>', 'Nominativo ou acusativo plural de <i>perīculum, -ī</i> (neutro plural em <i>-a</i>). Não é da 1ª declinação: não existe <i>perīcula, -ae</i>.'),
            ('<i>silvārum</i>', 'Genitivo plural de <i>silva, -ae</i>.'),
            ('<i>miserās</i>', 'Acusativo plural feminino de <i>miser, -era, -erum</i>. O tema <i>miser-</i>, com <i>e</i>, confirma o verbete.'),
            ('<i>mittunt</i>', '3ª pessoa do plural do presente de <i>mittō, -ere</i> (3ª conjugação: <i>-unt</i> sem <i>i</i>).'),
            ('<i>fugiunt</i>', '3ª pessoa do plural de <i>fugiō, -ere</i>. A terminação <i>-iunt</i> serve à 4ª e à 3ª em <i>-iō</i>; o verbete (<i>-ere</i>) mostra que é a segunda.'),
            ('<i>venīs</i>', '2ª pessoa do singular de <i>veniō, -īre</i> (4ª conjugação, <i>ī</i> longo).'),
            ('<i>tenēmus</i>', '1ª pessoa do plural de <i>teneō, -ēre</i>.'),
        ]),
        exercicio('Exercício 3 · Homógrafos: o contexto decide', 'Diga a que verbete pertence a forma destacada e por quê. Vocabulário: <i>liber, librī</i>, livro; <i>servō, -āre</i>, guardar; <i>portō, -āre</i>, carregar; <i>porta, -ae</i>, porta; <i>amant</i>, amam.', [
            ('<i>Dominus <b>servō</b> librum dat.</i>', '<i>servus, -ī</i>, dativo singular: o verbo é <i>dat</i>, que pede um destinatário, e o sujeito é <i>dominus</i>. "O senhor dá um livro ao escravo."'),
            ('<i>Librum <b>servō</b>.</i>', '<i>servō, -āre</i>, 1ª pessoa do singular: é o único verbo possível na frase. "Guardo o livro."'),
            ('<i>Aquam <b>portās</b>.</i>', '<i>portō, -āre</i>, 2ª pessoa do singular: não há outro verbo. "Carregas água."'),
            ('<i>Puellae <b>portās</b> spectant.</i>', '<i>porta, -ae</i>, acusativo plural: o verbo é <i>spectant</i>. "As meninas olham as portas."'),
            ('<i>Agricolae <b>līberōs</b> amant.</i>', '<i>līber, -era, -erum</i>, usado como nome: "os filhos". O tema <i>līber-</i> exclui <i>liber, librī</i>. "Os agricultores amam os filhos."'),
            ('<i>Puerī <b>librōs</b> amant.</i>', '<i>liber, librī</i>, acusativo plural: o tema <i>libr-</i> não tem o <i>e</i>. "Os meninos amam os livros."'),
        ]),
        exercicio('Exercício 4 · Enclíticos, grafias e prefixos', 'Diga em que verbete você procuraria cada forma e explique o que precisou desfazer.', [
            ('<i>virīque</i>', 'Tire o <i>-que</i>: <i>virī</i>, de <i>vir, virī</i> (genitivo singular ou nominativo plural). "e dos homens" ou "e os homens", conforme a frase.'),
            ('<i>terrāsque</i>', '<i>terrās</i> + <i>-que</i>: acusativo plural de <i>terra, -ae</i>. "e as terras".'),
            ('<i>neque</i>', 'Não tire nada: <i>neque</i>, "e não, nem", é uma palavra com verbete próprio. Tirando <i>-que</i>, sobraria <i>ne</i>, que não faz sentido como lema aqui.'),
            ('<i>uiuit</i> (assim, numa edição moderna)', 'Os dois <i>u</i>, cada um diante de vogal, são consoantes: <i>vīvit</i>, 3ª pessoa de <i>vīvō, -ere</i>, "viver". Procure com <i>v</i>.'),
            ('<i>iacit</i>', '3ª pessoa de <i>iaciō, -ere</i> (3ª em <i>-iō</i>), "lançar". No Lewis &amp; Short, o verbete está em <i>jacio</i>.'),
            ('<i>adportat</i>', 'É a grafia sem assimilação de <i>apportat</i>, de <i>apportō, -āre</i> (<i>ad</i> + <i>portō</i>), "trazer para junto". Se não achar uma das grafias, procure a outra.'),
            ('<i>accipiunt</i>', '<i>accipiō, -ere</i> (<i>ad</i> + <i>capiō</i>, com assimilação de <i>d</i> e enfraquecimento de <i>a</i> em <i>i</i>), "receber". Procure em <i>a</i>, não em <i>capiō</i>.'),
            ('<i>inimīcus</i> (decomponha)', '<i>in-</i> negativo + <i>amīcus</i>, com o <i>a</i> enfraquecido em <i>i</i>: "não amigo", "inimigo". Diante de adjetivo, <i>in-</i> é "não", e não "em".'),
        ]),
        exercicio('Exercício 5 · Cognatos e falsos amigos', 'Traduza, cuidando dos falsos amigos. Nas duas últimas, verta para o latim. Vocabulário: <i>studium, -ī</i>; <i>cūra, -ae</i>; <i>officium, -ī</i>; <i>magnus, -a, -um</i>, grande; <i>est</i>, é; <i>sunt</i>, estão, são.', [
            ('<i>Studium agricolae magnum est.</i>', '"A dedicação do agricultor é grande." <i>Studium</i> é empenho, não "estudo"; <i>magnum</i>, neutro, concorda com ele como predicativo.'),
            ('<i>Cūra puellārum magna est.</i>', '"A preocupação (o cuidado) das meninas é grande." <i>Cūra</i> não é "cura" de doença.'),
            ('<i>Līberī dominī in vīllā sunt.</i>', '"Os filhos do senhor estão na casa." <i>Līberī</i>, nominativo plural usado como nome, são "os filhos", e o verbo <i>sunt</i> confirma o plural.'),
            ('<i>Officium servōrum magnum est.</i>', '"O dever (o serviço) dos escravos é grande." <i>Officium</i> não é "escritório".'),
            ('Os filhos do agricultor carregam água.', '<i>Līberī agricolae aquam portant.</i> Sujeito <i>līberī</i> (nominativo plural), genitivo <i>agricolae</i>, objeto <i>aquam</i>, verbo no plural.'),
            ('Os marinheiros guardam os livros e as armas.', '<i>Nautae librōs armaque servant.</i> (ou <i>librōs et arma</i>). <i>Librōs</i> de <i>liber, librī</i>; <i>arma</i> é neutro plural, igual no nominativo e no acusativo; o <i>-que</i> se cola à segunda palavra.'),
        ]),
        exercicio('Exercício 6 · Usando as ferramentas', "Responda com base no que o capítulo mostrou sobre a lista DCC, o Whitaker's Words e o Lewis & Short.", [
            ('Qual é a palavra mais frequente do latim na lista DCC, e em que posição está <i>in</i>?', '<i>Et</i>, na posição 1; <i>in</i> está na posição 5. Por isso vale a pena dominar cedo as preposições e conjunções: elas aparecem em quase toda frase.'),
            ("O Whitaker's Words diz que <i>virum</i> pode ser \"vírus\". Por que descartar essa leitura em <i>Arma virumque canō</i>?", 'Porque o próprio programa marca essa palavra como latim moderno e pouco comum, e porque o sentido não cabe na frase de um poema antigo sobre armas e heróis. O analisador lista possibilidades da palavra isolada; a frase escolhe.'),
            ('Por que o Lewis &amp; Short registra <i>ămo, āvi, ātum, 1</i> sem o infinitivo?', 'Porque o número <b>1</b> já diz a conjugação, e o infinitivo da 1ª é previsível (<i>amāre</i>). É uma convenção do dicionário, não uma informação a menos.'),
            ('Você procurou <i>iacio</i> no Lewis &amp; Short e não achou. O que fazer?', 'Procurar <i>jacio</i>: o Lewis &amp; Short escreve <i>j</i> para o <i>i</i> consonantal. A palavra existe; só a grafia do dicionário é outra.'),
            ('Em que ordem usar o caderno e o analisador?', 'Primeiro o caderno: classe, análise e lema hipotéticos. Depois o analisador ou o dicionário, para confirmar ou corrigir. Só assim a consulta ensina alguma coisa.'),
        ]),
    ],
    leituras=['college-dcc-latin-core-vocabulary', 'logeion', 'whitakers-words', 'short-a-latin-dictionary-lewis-short', 'ravizza-gramatica-latina', 'sonnenschein-ora-maritima-a-latin-story-for-beginners'],
    leituras_nota="Comece pela lista DCC em português: filtre os nomes da 1ª e da 2ª declinação e os verbos das quatro conjugações e estude as cem primeiras posições, verbete inteiro. Use o Logeion para consultar o Lewis & Short e o Elementary Latin Dictionary pelo lema, e o Whitaker's Words só para conferir uma análise já anotada. Ravizza (n. 17 e 84) explica em português como o dicionário registra nomes e verbos. Para praticar a consulta em texto corrido, leia os primeiros capítulos de Ora Maritima procurando no dicionário só as palavras que o contexto não resolver.",
)
