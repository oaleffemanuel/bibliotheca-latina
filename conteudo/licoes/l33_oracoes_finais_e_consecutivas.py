from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='33-oracoes-finais-e-consecutivas', titulo='Orações finais, consecutivas e completivas',
    titulo_latim='Ut et nē', tempo='75 min',
    resumo='O subjuntivo nas orações subordinadas com ut e nē: a finalidade (ut, nē, quō com comparativo), a consequência (tam, ita, sīc, adeō, tantus, tālis … ut; negativa ut nōn), as completivas de ordem e pedido (imperō, rogō, ōrō, moneō, persuādeō ut/nē, contra iubeō + infinitivo), as de temor (timeō nē = "que", timeō ut / nē nōn = "que não") e as de resultado (fit ut, accidit ut), com a regra simples da escolha do tempo.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['orações finais', 'ut e nē finais', 'quō com comparativo', 'nēve', 'orações consecutivas', 'tam, ita, sīc, adeō, tantus, tālis, tot … ut', 'ut nōn consecutivo',
             'nē × ut nōn', 'orações completivas', 'ordem indireta (imperō, rogō, ōrō, moneō, persuādeō)', 'iubeō e vetō com infinitivo', 'verbos de temor (timeō nē, timeō ut)',
             'completivas de resultado (fit ut, accidit ut, efficiō ut)', 'sequência dos tempos (forma simples)', 'ut com indicativo', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 32: as formas do subjuntivo (sobretudo o presente e o imperfeito) e a ideia de que nē nega a vontade e o desejo. Ajudam o capítulo 18 (comparativos, para quō) e o capítulo 28 (a oração infinitiva, que aparece em contraste com iubeō).',
                       licoes=['32-o-subjuntivo', '18-comparativos-e-superlativos', '28-a-oracao-infinitiva']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 267 (tempos principais e históricos; regra da sequência), § 268.6 (perfeito do subjuntivo nas consecutivas depois de tempo histórico), § 282 (orações finais: ut, quō, nē; 282.a quō com comparativo; 282.c ut nōn quando a negação recai numa palavra; 282.d nēve), § 284 (consecutivas: ut, ut nōn; tantus, tālis, tot, tam, ita, sīc, adeō), § 294 (orações substantivas), § 295 (completivas volitivas: ut/nē com verbos de pedir, ordenar, persuadir; 295.1.a iubeō com infinitivo; 295.8 subjuntivo sem ut), § 296.2 (verbos de temer: nē, ut, nē nōn), § 297 (completivas de resultado: faciō, efficiō; fit, accidit, ēvenit)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§§ 482–484 (sequência dos tempos), § 485.c (perfeito do subjuntivo nas consecutivas), §§ 529–533 (orações finais; 531.a quō com comparativo; 531 nota 1, Lēgum idcircō servī sumus…; 533 o latim não exprime finalidade pelo infinitivo), §§ 536–538 (consecutivas; 537.a negativa ut nōn, nunca nē; 538 finais e consecutivas iguais no afirmativo, diferentes no negativo), §§ 560–562 (orações substantivas), § 563 (completivas de finalidade; 563.a iubeō e vetō com infinitivo), § 564 (verbos de temer), §§ 567–569 (completivas de resultado)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 411 (sequência dos tempos), § 417 (ordem, pedido e proibição indiretos com ut/nē; nota 2, volō, iubeō com infinitivo; nota 4, verbos de temer), § 421 (consecutivas; ut depois de adeō, ita, tam, sīc, tantus, tot; nota 2 sobre a sequência), § 423 (finais: ut, nē, ut nē; Lēgum idcircō servī sumus…)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 416 (consecutio temporum: contemporaneidade, anterioridade e posterioridade), n. 418 (verbos de temer: ne = "que", ut / ne non = "que não"), nn. 452–455 (proposições finais: ut, quo, ne), nn. 457–462 (proposições consecutivas)', tipo='dominio_publico'),
        referencia("D'Ooge, Latin for Beginners", "Benjamin L. D'Ooge", catalogo='d-ooge-latin-for-beginners', nota='lições LXII (subjuntivo de finalidade), LXIII (sequência dos tempos), LXIV (completivas de finalidade), LXV (verbos de temer) e LXVIII (subjuntivo de resultado); conferidas no sumário da edição do Projeto Gutenberg', tipo='dominio_publico'),
        referencia('Cícero, Pro Cluentio 146', 'Mārcus Tullius Cicero', catalogo='the-latin-library', url='https://www.thelatinlibrary.com/cicero/cluentio.shtml', nota='frase analisada na seção 2, conferida no texto da Latin Library (§ 146) e na edição de A. C. Clark (Oxford, 1905; TEI da Perseus), que dá o mesmo texto e registra as variantes servimus (manuscrito P) por servī sumus e lēgibus dēnique (Baiter) por lēgum dēnique; A&G § 531 nota 1 e Kennedy § 423 citam-na abreviada (ut līberī sīmus / ut līberī esse possīmus); macrons acrescentados', tipo='dominio_publico'),
        referencia('César, De Bello Gallico 1.2.1', 'Gaius Iulius Caesar', catalogo='caesar-commentarii-de-bello-gallico-texto-integral', url='https://www.thelatinlibrary.com/caesar/gall1.shtml', nota='frase analisada na seção 5, conferida no texto da Latin Library; macrons acrescentados', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Gênesis 1,14–17; João 3,16; Mateus 2,12 e 7,1', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Joannem', nota='frases do diagrama e dos exercícios, conferidas no texto da Wikisource latina; ortografia adaptada (ae por æ, i por j) e macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Reconhecer as três famílias de orações com <i>ut</i>/<i>nē</i> + subjuntivo (finais, consecutivas e completivas) e traduzir cada uma corretamente.',
        'Distinguir finalidade de consequência pelas palavras-sinal (<i>tam, ita, sīc, adeō, tantus, tālis, tot</i>) e pela negação: <i>nē</i> na final, <i>ut nōn</i> na consecutiva.',
        'Construir ordens e pedidos indiretos com <i>imperō, rogō, ōrō, moneō, persuādeō</i> + <i>ut/nē</i>, e contrastá-los com <i>iubeō</i> e <i>vetō</i> + infinitivo.',
        'Traduzir as orações de temor sem inverter o sentido (<i>timeō nē</i> = "temo que"; <i>timeō ut</i>, <i>nē nōn</i> = "temo que não").',
        'Escolher o tempo do subjuntivo pela regra simples: presente depois de tempo presente ou futuro, imperfeito depois de tempo passado.',
    ],
    secoes=[
        ('Ut e nē: duas conjunções, muitas funções', f'''
<p>No capítulo 32 o subjuntivo apareceu sozinho, em oração principal. Na maior parte dos textos, porém, ele aparece em <b>orações subordinadas</b>, e as duas conjunções que mais o introduzem são <i>ut</i> e <i>nē</i>. Elas são pequenas e frequentes, e por isso mesmo traiçoeiras: <i>ut</i> com subjuntivo pode significar "para que", "de modo que" ou simplesmente "que"; <i>nē</i> pode significar "para que não" ou, depois de verbos de temor, "que". Este capítulo ensina a decidir entre esses sentidos.</p>
<p>As orações com <i>ut</i>/<i>nē</i> + subjuntivo formam três famílias. As <b>finais</b> dizem para que algo se faz: "estudamos <b>para que</b> aprendamos". As <b>consecutivas</b> dizem que consequência algo teve: "estudou <b>tanto que</b> aprendeu". As <b>completivas</b> (ou substantivas) completam o sentido de um verbo, como um objeto: "peço <b>que</b> venhas", "temo <b>que</b> chova", "aconteceu <b>que</b> choveu" (Bennett § 294; A&amp;G §§ 561–562). O português conserva a mesma estrutura nas três: conjunção + subjuntivo nas finais e nas completivas de pedido ("para que venhas", "peço que venhas"), e uma correlação "tão… que", "tanto… que" nas consecutivas.</p>
{tabela(['Família', 'Afirmativa', 'Negativa', 'Português', 'Exemplo'], [
    ['Final', '<i>ut</i> (ou <i>quō</i>)', '<i>nē</i>', 'para que, a fim de que', 'Labōrō <b>ut</b> vīvam.'],
    ['Consecutiva', '<i>ut</i> (depois de <i>tam, ita, sīc…</i>)', '<i>ut nōn</i>', 'de modo que, tão… que', 'Tam fessus est <b>ut</b> dormiat.'],
    ['Completiva de ordem/pedido', '<i>ut</i>', '<i>nē</i>', 'que (+ subjuntivo)', 'Rogō <b>ut</b> veniās.'],
    ['Completiva de temor', '<i>nē</i> = "que"', '<i>ut</i>, <i>nē nōn</i> = "que não"', 'que, que não', 'Timeō <b>nē</b> veniat.'],
    ['Completiva de resultado', '<i>ut</i>', '<i>ut nōn</i>', 'que (aconteceu que…)', 'Accidit <b>ut</b> pluat.'],
], 'As orações com ut e nē + subjuntivo: visão geral')}
{observacao('Ut com indicativo é outra coisa', 'Quando o verbo depois de <i>ut</i> está no <b>indicativo</b>, <i>ut</i> significa "como" (comparação) ou "quando" (tempo): <i>ut dīxī</i>, "como eu disse"; <i>ut vēnit</i>, "quando chegou". Antes de traduzir <i>ut</i>, olhe o modo do verbo da oração: só com o subjuntivo valem as regras deste capítulo.')}
<h3>Que tempo do subjuntivo? A regra simples</h3>
<p>Nas orações deste capítulo, o tempo do subjuntivo depende do tempo do verbo principal. Por ora, basta uma regra de duas linhas, que é a forma simples da <b>sequência dos tempos</b> (Bennett § 267; A&amp;G § 483; Kennedy § 411): se o verbo principal está num tempo de <b>presente ou futuro</b>, o subjuntivo vai para o <b>presente</b>; se está num tempo <b>passado</b>, vai para o <b>imperfeito</b>. É o mesmo instinto do português: "estudo para que <b>aprenda</b>" × "estudava para que <b>aprendesse</b>". A regra completa, com o perfeito e o mais-que-perfeito do subjuntivo e com a ação posterior, é o assunto do capítulo 34.</p>
{exemplos([('Labōrō ut vīv<b>am</b>.', 'Trabalho para viver (para que eu viva). (presente → presente)'), ('Labōrābō ut vīv<b>am</b>.', 'Trabalharei para viver. (futuro → presente)'), ('Labōrābam ut vīver<b>em</b>.', 'Eu trabalhava para viver (para que vivesse). (passado → imperfeito)'), ('Labōrāvī ut vīver<b>em</b>.', 'Trabalhei para viver. (perfeito narrativo → imperfeito)')])}
'''),
        ('Orações finais: ut, nē, quō', f'''
<p>A oração <b>final</b> (do latim <i>fīnis</i>, "fim, objetivo") exprime a intenção com que se pratica a ação principal. Afirmativa, começa por <i>ut</i> (às vezes <i>utī</i>); negativa, por <b><i>nē</i></b>, "para que não", e nunca por *<i>ut nōn</i> (Bennett § 282; A&amp;G § 531; Kennedy § 423; Ravizza nn. 452–455). O verbo vai sempre para o subjuntivo, porque a finalidade é uma ação querida, não um fato.</p>
{exemplos([('Edimus <b>ut</b> vīvāmus.', 'Comemos para viver. (exemplo de Bennett § 282)'), ('Puerī in scholā sedent <b>ut</b> discant.', 'Os meninos ficam sentados na escola para aprender. (<i>discō, -ere</i>, aprender)'), ('Servus fūgit <b>nē</b> caperētur.', 'O escravo fugiu para não ser capturado. (passado → imperfeito; passiva de <i>capiō</i>)'), ('Tacēmus <b>nē</b> dominum excitēmus.', 'Ficamos calados para não acordar o senhor. (<i>taceō</i>, calar; <i>excitō</i>, acordar)')])}
<p>Repare na tradução: o português prefere "para + infinitivo" quando o sujeito das duas orações é o mesmo ("comemos para viver"), e "para que + subjuntivo" quando muda ("falo alto para que todos ouçam"). O latim clássico, ao contrário, <b>não usa o infinitivo para exprimir finalidade</b> (A&amp;G § 533): "comemos para viver" é obrigatoriamente <i>edimus ut vīvāmus</i>. Na retroversão, nunca escreva *<i>edimus vīvere</i>.</p>
<h3>Detalhes da final</h3>
<p><b><i>Nēve</i> (<i>neu</i>)</b>: para acrescentar uma segunda finalidade negativa, "e para que não", o latim usa <i>nēve</i>: <i>profūgit nē caperētur nēve interficerētur</i>, "fugiu para não ser preso nem morto" (Bennett § 282.d). <b><i>Quō</i> + comparativo</b>: quando a oração final contém um comparativo (capítulo 18), a conjunção costuma ser <i>quō</i> (= <i>ut eō</i>, "para que por isso"): <i>adiūtā mē quō hōc fīat facilius</i>, "ajuda-me para que isto se faça mais facilmente" (Bennett § 282.a; A&amp;G § 531.a). <b>Correlativos</b>: a oração principal anuncia às vezes a finalidade com <i>idcircō</i>, <i>ideō</i>, <i>eō cōnsiliō</i> ("por isso, com este propósito"), que se traduzem "é para isto que…" (A&amp;G § 531, nota 1).</p>
{observacao('Também a relativa pode ser final', 'Um relativo com o verbo no subjuntivo pode exprimir finalidade: <i>Helvētiī lēgātōs mittunt quī dīcerent</i>, "os helvécios mandam embaixadores para dizer" (literalmente, "que dissessem"; Bennett § 282.2). Aqui <i>quī</i> vale <i>ut eī</i>. Basta reconhecer a construção por enquanto; as relativas com subjuntivo voltam no capítulo 39.')}
<h3>Análise gramatical: Cícero, Pro Cluentio 146</h3>
<p>Numa defesa de 66 a.C., Cícero lembra aos juízes que a liberdade dos cidadãos depende da obediência às leis, e resume a ideia numa frase que as gramáticas citam até hoje como modelo de oração final com correlativo:</p>
{exemplos([('Lēgum dēnique idcircō omnēs servī sumus ut līberī esse possīmus.', 'Enfim, é por isto que todos somos escravos das leis: para podermos ser livres. (Cícero, <i>Pro Cluentio</i> 146)')])}
{analise('Pro Cluentio 146, palavra a palavra', [
    ('Lēgum', 'lēx, lēgis (f.), lei', 'genitivo plural, 3ª declinação', 'complemento de <i>servī</i>: "escravos <b>das leis</b>"'),
    ('dēnique', 'dēnique, enfim', 'advérbio', 'fecha uma enumeração'),
    ('idcircō', 'idcircō, por isso', 'advérbio correlativo', 'anuncia a oração final: "é por isto que…"'),
    ('omnēs', 'omnis, -e, todo', 'nominativo plural masculino', 'concorda com o sujeito implícito "nós"'),
    ('servī', 'servus, -ī (m.), escravo', 'nominativo plural', 'predicativo do sujeito'),
    ('sumus', 'sum, esse, fuī, ser', '1ª pl., presente do indicativo', 'verbo principal; tempo <b>presente</b>'),
    ('ut', 'ut (conjunção)', 'com subjuntivo', 'introduz a oração <b>final</b>: "para que"'),
    ('līberī', 'līber, -era, -erum, livre', 'nominativo plural masculino', 'predicativo de <i>esse</i>, concordando com o sujeito "nós"'),
    ('esse', 'sum, esse, fuī, ser', 'infinitivo presente', 'complemento de <i>possīmus</i>'),
    ('possīmus', 'possum, posse, potuī, poder', '1ª pl., <b>presente do subjuntivo</b>', 'verbo da final; presente porque <i>sumus</i> é presente'),
])}
<p>Três pontos do capítulo estão aqui. O correlativo <i>idcircō</i> prepara a final, e por isso a tradução natural é "é por isso que… para que". A sequência é a simples: <i>sumus</i> (presente) pede <i>possīmus</i> (presente do subjuntivo). E o paradoxo retórico depende da finalidade: a escravidão às leis não é um fato isolado, é o meio para um fim, a liberdade. Allen &amp; Greenough (§ 531, nota 1) e Kennedy (§ 423) citam a frase de forma abreviada; o texto acima é o da edição da Latin Library.</p>
'''),
        ('Orações consecutivas: tam … ut', f'''
<p>A oração <b>consecutiva</b> diz qual foi (ou é) a consequência do que se afirma na principal. No afirmativo ela também começa por <i>ut</i> com subjuntivo, mas quase sempre a principal traz uma <b>palavra-sinal</b> de intensidade ou de modo, que anuncia a consequência (Bennett § 284; A&amp;G § 537, nota 2; Kennedy § 421; Ravizza nn. 457–459):</p>
{tabela(['Palavra-sinal', 'Classe', 'Sentido', 'Exemplo'], [
    ['tam', 'advérbio (com adjetivo ou advérbio)', 'tão', '<i>tam fessus ut…</i>'],
    ['ita, sīc', 'advérbios (com verbos)', 'assim, de tal modo', '<i>ita clāmāvit ut…</i>'],
    ['adeō', 'advérbio', 'a tal ponto', '<i>adeō timēbant ut…</i>'],
    ['tantus, -a, -um', 'adjetivo', 'tão grande', '<i>tanta tempestās ut…</i>'],
    ['tālis, -e', 'adjetivo', 'tal, de tal natureza', '<i>tālis vir ut…</i>'],
    ['tot (invariável)', 'adjetivo', 'tantos', '<i>tot hostēs ut…</i>'],
], 'As palavras-sinal da oração consecutiva', latim_cols=(0,))}
{exemplos([('Puer <b>tam</b> fessus erat <b>ut</b> statim dormīret.', 'O menino estava tão cansado que dormiu imediatamente.'), ('<b>Tanta</b> erat tempestās <b>ut</b> nautae nāvigāre nōn possent.', 'A tempestade era tão grande que os marinheiros não podiam navegar.'), ('<b>Ita</b> clāmāvit <b>ut</b> omnēs eum audīrent.', 'Gritou de tal modo que todos o ouviram.')])}
<p>A <b>negativa</b> é <b><i>ut nōn</i></b> (ou <i>ut nēmō</i>, <i>ut nihil</i>, <i>ut numquam</i>), e nunca <i>nē</i> (A&amp;G § 537.a). O motivo é lógico: <i>nē</i> nega uma vontade, e a consequência não é querida por ninguém; é um fato que se seguiu. Pela mesma razão, a tradução portuguesa da consecutiva usa muitas vezes o <b>indicativo</b> ("estava tão cansado que <b>dormiu</b>"), embora o latim use o subjuntivo: o latim marca a dependência da oração, o português marca a realidade do fato.</p>
<p>O versículo mais citado do Evangelho de João é uma consecutiva com <i>sīc</i>. Note que <i>dīlēxit</i> (perfeito, passado) pede o imperfeito <i>daret</i>:</p>
{diagrama_frase([('Sīc', 'advérbio · palavra-sinal'), ('dīlēxit mundum', 'principal · perfeito (passado)'), ('ut', 'conjunção · consecutiva'), ('Fīlium … daret', 'subjuntivo imperfeito · a consequência')],
    '<i>Sīc enim Deus dīlēxit mundum, ut Fīlium suum ūnigenitum daret</i> (João 3,16) = Pois Deus amou tanto o mundo, que deu o seu Filho unigênito. O <i>sīc</i> da principal anuncia a consequência; o português traduz <i>daret</i> pelo indicativo ("deu").')}
{observacao('Uma exceção de tempo nas consecutivas', 'Nas consecutivas, depois de um verbo principal no passado, os historiadores usam às vezes o <b>perfeito</b> do subjuntivo em vez do imperfeito, para apresentar a consequência como um fato pontual: <i>rēx tantum mōtus est ut Tissaphernem hostem iūdicārit</i>, "o rei ficou tão abalado que declarou Tissafernes inimigo" (Bennett § 268.6; A&amp;G § 485.c). Ao ler, aceite os dois tempos; ao escrever, use o imperfeito.')}
'''),
        ('A armadilha: nē ou ut nōn?', f'''
<p>No afirmativo, final e consecutiva são <b>idênticas na forma</b>: <i>ut</i> + subjuntivo. No negativo elas se separam: a final usa <i>nē</i>, a consecutiva usa <i>ut nōn</i> (A&amp;G § 538). Allen &amp; Greenough dão um par perfeito para fixar a diferença:</p>
{comparacao('O mesmo verbo, duas intenções (A&G § 538)', ['Latim', 'Tipo', 'Português'], [
    ['Cūstōdītus est <b>nē</b> effugeret.', 'final negativa', 'Foi vigiado para que não fugisse (era essa a intenção).'],
    ['Cūstōdītus est <b>ut nōn</b> effugeret.', 'consecutiva negativa', 'Foi vigiado de modo que não fugiu (foi esse o resultado).'],
])}
<p>Como decidir, então, diante de um <i>ut</i> afirmativo? Use três perguntas, nesta ordem. <b>1. Há palavra-sinal na principal</b> (<i>tam, ita, sīc, adeō, tantus, tālis, tot</i>)? Se há, é quase certamente consecutiva. <b>2. A oração responde a "para quê?" ou a "com que resultado?"</b>? Intenção é final; resultado é consecutiva. <b>3. Se a frase for negativa, a própria negação resolve</b>: <i>nē</i> só pode ser final (ou completiva de ordem ou temor); <i>ut nōn</i> é consecutiva (ou completiva de resultado).</p>
{tabela(['Para negar…', 'Final (intenção)', 'Consecutiva (resultado)'], [
    ['a oração toda', 'nē', 'ut nōn'],
    ['"ninguém"', 'nē quis', 'ut nēmō'],
    ['"nada"', 'nē quid', 'ut nihil'],
    ['"nunca"', 'nē umquam', 'ut numquam'],
    ['"e para que não"', 'nēve (neu)', 'et ut nōn, neque'],
], 'Negativas da final e da consecutiva (Bennett §§ 282, 284; A&G § 538)', latim_cols=(1, 2))}
<p>Duas exceções, para não ser pego de surpresa. Numa final, <i>ut nōn</i> aparece quando o <i>nōn</i> nega uma <b>só palavra</b>, e não a oração inteira (Bennett § 282.c): <i>ut plūra nōn dīcam</i>, "para não dizer mais" (A&amp;G § 531, nota 2). E o latim bíblico, que segue de perto o grego, usa às vezes <i>ut nōn</i> com valor final: <i>Nōlīte iūdicāre, ut nōn iūdicēminī</i>, "não julgueis, para não serdes julgados" (Mateus 7,1, Vulgata). Na prosa clássica, a regra é a da tabela.</p>
'''),
        ('Orações completivas: ordens, pedidos, temores e resultados', f'''
<p>Uma oração <b>completiva</b> funciona como objeto ou sujeito de um verbo, exatamente como um substantivo: em "peço <b>que venhas</b>", a oração responde a "peço o quê?" (Bennett § 294; A&amp;G § 561). Com <i>ut</i>/<i>nē</i> + subjuntivo, há três grupos.</p>
<h3>1. Ordens, pedidos e conselhos (ordem indireta)</h3>
<p>Verbos que significam <b>ordenar, pedir, aconselhar, exortar, persuadir</b> levam <i>ut</i> (afirmativo) ou <i>nē</i> (negativo) + subjuntivo: o conteúdo da ordem ou do pedido é uma ação querida, por isso a negação é <i>nē</i>, como no jussivo (Bennett § 295.1; A&amp;G § 563; Kennedy § 417). Preste atenção ao caso da pessoa a quem se ordena ou pede:</p>
{tabela(['Verbo', 'Pessoa', 'Exemplo', 'Português'], [
    ['imperō, -āre, ordenar', 'dativo', 'Mīlitibus imperat ut pugnent.', 'Ordena aos soldados que lutem.'],
    ['persuādeō, -ēre, -suāsī, persuadir', 'dativo', 'Patrī persuādeō nē abeat.', 'Persuado o pai a não partir.'],
    ['rogō, -āre, pedir', 'acusativo', 'Tē rogō ut veniās.', 'Peço-te que venhas.'],
    ['ōrō, -āre, rogar', 'acusativo', 'Ōrat nē abeās.', 'Pede que não vás embora. (Bennett § 295.1)'],
    ['moneō, -ēre, aconselhar, advertir', 'acusativo', 'Puerōs moneō ut dīligenter legant.', 'Aconselho os meninos a ler com atenção.'],
    ['hortor, -ārī (depoente), exortar', 'acusativo', 'Mīlitēs hortātur ut fortēs sint.', 'Exorta os soldados a serem valentes.'],
    ['petō, -ere, pedir', 'ā/ab + ablativo', 'Ā rēge petunt ut pācem faciat.', 'Pedem ao rei que faça a paz.'],
], 'Verbos de ordem e pedido com ut/nē + subjuntivo', latim_cols=(0, 2))}
<p><b>O contraste com <i>iubeō</i></b>. O verbo mais comum para "mandar", <i>iubeō, -ēre, iussī, iussum</i>, não segue essa regra: leva <b>acusativo + infinitivo</b> (capítulo 28), e o mesmo faz <i>vetō, -āre</i>, "proibir" (Bennett § 295.1.a; A&amp;G § 563.a). Compare: <i>mīlitibus imperat ut pugnent</i> × <i>mīlitēs pugnāre iubet</i>, as duas "ordena aos soldados que lutem". Para negar com <i>iubeō</i>, use <i>vetō</i>: <i>mīlitēs pugnāre vetat</i>, "proíbe os soldados de lutar". O português conhece as duas construções ("mandou-os sair" × "mandou que saíssem"), mas o latim as distribui por verbo, e quem decide é o dicionário.</p>
<p>A primeira frase de César sobre o helvécio Orgetórix, no começo da Guerra da Gália, é uma ordem indireta com <i>persuādeō</i>:</p>
{exemplos([('Is … cīvitātī persuāsit ut dē fīnibus suīs cum omnibus cōpiīs exīrent.', 'Ele … persuadiu o povo a sair do seu território com todos os seus recursos. (César, <i>BG</i> 1.2.1)')])}
{analise('De Bello Gallico 1.2.1 (trecho), palavra a palavra', [
    ('Is', 'is, ea, id, ele', 'nominativo singular masculino', 'sujeito: Orgetórix'),
    ('cīvitātī', 'cīvitās, -ātis (f.), cidade, povo', 'dativo singular', 'pessoa persuadida: <i>persuādeō</i> rege dativo'),
    ('persuāsit', 'persuādeō, -ēre, -suāsī, -suāsum, persuadir', '3ª sing., perfeito do indicativo', 'verbo principal; tempo <b>passado</b>'),
    ('ut', 'ut (conjunção)', 'com subjuntivo', 'introduz a completiva: o conteúdo da persuasão'),
    ('dē fīnibus suīs', 'fīnēs, -ium (m. pl.), território', '<i>dē</i> + ablativo plural', 'de onde: "do seu território"'),
    ('cum omnibus cōpiīs', 'cōpiae, -ārum (f. pl.), recursos, tropas', '<i>cum</i> + ablativo plural', 'companhia: "com todos os recursos"'),
    ('exīrent', 'exeō, -īre, -iī, -itum, sair', '3ª pl., <b>imperfeito do subjuntivo</b> (<i>exīre</i> + <i>-nt</i>)', 'verbo da completiva; imperfeito porque <i>persuāsit</i> é passado'),
])}
<p>Note três coisas. <i>Exīrent</i> é o imperfeito do subjuntivo de um composto de <i>eō</i>, formado do infinitivo <i>exīre</i>, como no capítulo 32. O verbo está no plural embora <i>cīvitās</i> seja singular: César pensa nas pessoas que formam o povo (concordância pelo sentido). E a sequência é a simples: <i>persuāsit</i>, passado, pede o imperfeito.</p>
<h3>2. Temores: timeō nē = "temo que"</h3>
<p>Depois de verbos de <b>temor</b> (<i>timeō, metuō, vereor</i>; <i>perīculum est</i>), as conjunções parecem trocar de sentido: <b><i>nē</i> significa "que"</b> e <b><i>ut</i> (ou <i>nē nōn</i>) significa "que não"</b> (Bennett § 296.2; A&amp;G § 564; Kennedy § 417, nota 4; Ravizza n. 418). A explicação está na origem optativa da construção: <i>timeō nē veniat</i> era, originalmente, "que ele não venha! (mas) tenho medo [de que venha]"; <i>timeō ut veniat</i>, "que ele venha! (mas) tenho medo [de que não venha]". Quem teme deseja o contrário do que teme, e a conjunção exprime o desejo.</p>
{tabela(['Latim', 'Literalmente (o desejo)', 'Português (o temor)'], [
    ['Timeō <b>nē</b> pater aegrōtet.', '"que não esteja doente!"', 'Temo que o pai esteja doente.'],
    ['Timeō <b>ut</b> pater redeat.', '"que volte!"', 'Temo que o pai não volte.'],
    ['Timeō <b>nē</b> pater <b>nōn</b> redeat.', '—', 'Temo que o pai não volte. (= <i>ut</i>)'],
    ['Timēbam <b>nē</b> hostēs venīrent.', '"que não viessem!"', 'Eu temia que os inimigos viessem.'],
], 'Verbos de temor: a inversão aparente (exemplos baseados em Ravizza n. 418)', latim_cols=(0,))}
{dica('Regra prática para traduzir: depois de verbo de temor, leia <i>nē</i> como "que" e <i>ut</i> / <i>nē nōn</i> como "que não". Nunca traduza <i>timeō nē veniat</i> por "temo que não venha": é exatamente o contrário.')}
<h3>3. Resultados: fit ut, accidit ut</h3>
<p>Expressões que significam <b>acontecer</b> ou <b>fazer com que</b> levam uma completiva de <b>resultado</b>, com <i>ut</i> e negativa <i>ut nōn</i>, como as consecutivas de que derivam (Bennett § 297; A&amp;G §§ 568–569): <i>fit ut</i>, "acontece que"; <i>accidit ut</i>, "aconteceu que"; <i>efficiō ut</i>, "consigo que, faço com que". A oração completiva é o sujeito de <i>fit</i> e <i>accidit</i> e o objeto de <i>efficiō</i>.</p>
{exemplos([('Saepe <b>fit ut</b> puerī dormiant.', 'Muitas vezes acontece que os meninos dormem.'), ('<b>Accidit ut</b> eō diē plueret.', 'Aconteceu que naquele dia chovia. (<i>pluit</i>, chove)'), ('Magister <b>efficit ut</b> puerī librōs ament.', 'O professor consegue que os meninos amem os livros.'), ('<b>Accidit ut</b> nēmō venīret.', 'Aconteceu que ninguém veio. (negativa de resultado: <i>ut nēmō</i>)')])}
'''),
        ('Ler um período com ut e nē', f'''
<p>Para ler sem tropeços um período com <i>ut</i> ou <i>nē</i>, siga sempre a mesma rotina. <b>1.</b> Ache o verbo da oração com <i>ut</i>/<i>nē</i> e confirme que está no subjuntivo (se estiver no indicativo, <i>ut</i> é "como" ou "quando"). <b>2.</b> Olhe o verbo principal: é de ordem ou pedido? de temor? de "acontecer"? Então é completiva. <b>3.</b> Se não for, procure uma palavra-sinal (<i>tam, ita, sīc, adeō, tantus, tālis, tot</i>): se houver, é consecutiva; se não houver, é final. <b>4.</b> Confira o tempo pela regra simples (presente depois de presente ou futuro; imperfeito depois de passado). <b>5.</b> Traduza com a fórmula portuguesa adequada: "para que", "de modo que / tão… que", "que".</p>
<p>O primeiro capítulo do Gênesis, na Vulgata, permite treinar a regra do tempo com o mesmo tipo de oração em dois momentos. Quando Deus fala (presente, ordem), a final está no presente; quando o narrador conta o que Deus fez (passado), a final passa para o imperfeito:</p>
{exemplos([('Fīant lūmināria in firmāmentō caelī … ut lūceant in firmāmentō caelī.', 'Façam-se luzeiros no firmamento do céu … para que brilhem no firmamento do céu. (Gênesis 1,14–15; jussivo <i>fīant</i>, primário → <i>lūceant</i>, presente)'), ('Et posuit eās in firmāmentō caelī, ut lūcērent super terram.', 'E colocou-as no firmamento do céu para que brilhassem sobre a terra. (Gênesis 1,17; <i>posuit</i>, perfeito → <i>lūcērent</i>, imperfeito)')])}
{observacao('O subjuntivo sem ut', 'Com alguns verbos de pedir e ordenar, e com <i>volō</i>, <i>licet</i> e <i>oportet</i>, o latim às vezes omite o <i>ut</i> e põe o subjuntivo direto: <i>velim scrībās</i>, "gostaria que escrevesses"; <i>licet redeās</i>, "podes voltar"; <i>huic imperat adeat cīvitātēs</i>, "ordena-lhe que visite as cidades" (Bennett §§ 295.6, 295.8 e 296.1.a). Se você encontrar um subjuntivo "solto" depois desses verbos, leia como se houvesse <i>ut</i>.')}
<h3>Resumo</h3>
<ul>
<li><b>Final</b>: <i>ut</i> / <i>nē</i> (+ <i>quō</i> com comparativo; <i>nēve</i> para "e para que não") = "para que", "para".</li>
<li><b>Consecutiva</b>: palavra-sinal + <i>ut</i> / <i>ut nōn</i> = "tão… que", "de modo que"; em português, muitas vezes com indicativo.</li>
<li><b>Ordem e pedido</b>: <i>imperō</i> (dat.), <i>persuādeō</i> (dat.), <i>rogō, ōrō, moneō, hortor</i> (ac.) + <i>ut</i> / <i>nē</i>; mas <i>iubeō</i> e <i>vetō</i> + acusativo e infinitivo.</li>
<li><b>Temor</b>: <i>timeō nē</i> = "temo que"; <i>timeō ut</i> / <i>nē nōn</i> = "temo que não".</li>
<li><b>Resultado</b>: <i>fit ut, accidit ut, efficiō ut</i> (negativa <i>ut nōn</i>).</li>
<li><b>Tempo</b>: principal no presente ou futuro → presente do subjuntivo; principal no passado → imperfeito.</li>
</ul>
<p>No capítulo 34 a regra do tempo se completa: o perfeito e o mais-que-perfeito do subjuntivo entram para exprimir a ação anterior, e a conjunção <i>cum</i> mostra quanto o subjuntivo é comum na narração.</p>
'''),
    ],
    erros_comuns=[
        ('Negar a final com <i>ut nōn</i>: *<i>Fūgit ut nōn caperētur</i> para "fugiu para não ser preso".', 'A finalidade é uma ação querida e se nega com <i>nē</i>: <i>Fūgit nē caperētur</i>. <i>Ut nōn</i> faria da frase uma consecutiva ("fugiu, de modo que não foi preso"). Guarde o par de A&amp;G § 538: <i>cūstōdītus est nē effugeret</i> (intenção) × <i>ut nōn effugeret</i> (resultado).'),
        ('Negar a consecutiva com <i>nē</i>: *<i>Tam fessus erat nē labōrāret</i>.', 'A consequência não é querida, é um fato: nega-se com <i>ut nōn</i> (<i>tam fessus erat ut nōn labōrāret</i>), <i>ut nēmō</i>, <i>ut nihil</i>. Se há palavra-sinal (<i>tam, ita, tantus…</i>) e uma negação, espere <i>ut nōn</i>.'),
        ('Traduzir <i>timeō nē veniat</i> por "temo que não venha".', 'Depois de verbo de temor, <i>nē</i> é "que" e <i>ut</i> / <i>nē nōn</i> é "que não": <i>timeō nē veniat</i> = "temo que venha"; <i>timeō ut veniat</i> = "temo que não venha". Pense no desejo de quem teme: quem diz <i>nē veniat</i> deseja que ele <b>não</b> venha, porque teme que venha.'),
        ('Usar <i>iubeō</i> com <i>ut</i> (*<i>iubeō ut veniās</i>) ou <i>imperō</i> com acusativo e infinitivo (*<i>imperō tē venīre</i>).', '<i>Iubeō</i> e <i>vetō</i> levam acusativo + infinitivo (<i>iubeō tē venīre</i>); <i>imperō</i> leva dativo + <i>ut</i>/<i>nē</i> (<i>imperō tibi ut veniās</i>). Confira a regência no dicionário: os dois verbos significam quase o mesmo, mas se constroem de modos diferentes.'),
        ('Exprimir finalidade com o infinitivo, como em português: *<i>Vēnī vidēre</i> para "vim ver".', 'Na prosa clássica, a finalidade não se exprime pelo infinitivo (A&amp;G § 533): <i>Vēnī ut vidērem</i>. O português "para + infinitivo" corresponde a <i>ut</i> + subjuntivo; outras construções de finalidade (gerundivo, supino; capítulo 31) existem, mas o infinitivo simples não é uma delas.'),
        ('Pôr o presente do subjuntivo depois de um verbo no passado: *<i>Persuāsit ut exeant</i>.', 'Depois de um tempo passado o subjuntivo vai, em regra, para o imperfeito: <i>persuāsit ut exīrent</i>. O português faz o mesmo ("persuadiu-os a que <b>saíssem</b>"); o erro vem de traduzir palavra por palavra a partir de "persuadiu-os a sair".'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Final, consecutiva ou completiva?',
            'Classifique cada oração com <i>ut</i>/<i>nē</i> e traduza: (a) <i lang="la">Magister puerōs monet ut taceant.</i> (b) <i lang="la">Puerī tam clāmābant ut magister nihil audīret.</i> (c) <i lang="la">Puerī tacent nē magistrum excitent.</i> Vocabulário: <i>taceō, -ēre</i>, calar-se; <i>clāmō, -āre</i>, gritar; <i>excitō, -āre</i>, acordar.', [
            ('(a) O verbo principal pede um complemento?', 'Sim: <i>moneō</i>, "aconselhar, advertir", é verbo de ordem/conselho. <i>Ut taceant</i> diz o conteúdo do conselho: completiva. <i>Monet</i> é presente, logo <i>taceant</i> está no presente. "O professor adverte os meninos que se calem" (ou "a se calarem").'),
            ('(b) Há palavra-sinal?', 'Sim: <i>tam</i>. <i>Ut … audīret</i> é consecutiva: o resultado da gritaria. <i>Clāmābant</i> é passado, logo <i>audīret</i> está no imperfeito. A negação de resultado aparece como <i>nihil</i> (<i>ut … nihil</i>, não <i>nē quid</i>). "Os meninos gritavam tanto que o professor não ouvia nada."'),
            ('(c) <i>Nē</i> depois de <i>tacent</i>: que sentido tem?', '<i>Taceō</i> não é verbo de temor nem de ordem; não há palavra-sinal. <i>Nē</i> + subjuntivo é, então, final negativa: "Os meninos ficam quietos para não acordar o professor."'),
        ], 'Conclusão: olhe primeiro o verbo principal (completiva?), depois a palavra-sinal (consecutiva?); o que sobra é final.'),
        pratica_guiada('Prática guiada 2 · Do português para o latim',
            'Traduza: "O general ordenou aos soldados que não fugissem, porque temia que os inimigos viessem." Vocabulário: <i>dux, ducis</i>, general; <i>imperō, -āre, -āvī</i> (+ dat.), ordenar; <i>fugiō, -ere</i>, fugir; <i>timeō, -ēre</i>, temer; <i>hostis, -is</i>, inimigo; <i>veniō, -īre</i>, vir; <i>quod</i>, porque.', [
            ('Como fica "ordenou aos soldados que não fugissem"?', '<i>Imperō</i> leva dativo + <i>nē</i> + subjuntivo: <i>Dux mīlitibus imperāvit nē fugerent.</i> <i>Imperāvit</i> é passado, logo o imperfeito <i>fugerent</i> (de <i>fugere</i> + <i>-nt</i>).'),
            ('E "temia que os inimigos viessem"?', 'Verbo de temor + <i>nē</i> = "que": <i>timēbat nē hostēs venīrent</i>. Não use <i>ut</i>, que significaria "temia que não viessem".'),
            ('Monte o período.', '<i>Dux mīlitibus imperāvit nē fugerent, quod timēbat nē hostēs venīrent.</i> Dois <i>nē</i> com sentidos diferentes: o primeiro nega a ordem ("que não"), o segundo é o "que" do temor.'),
        ]),
    ],
    exercicios=[
        exercicio('Exercício 1 · Classifique e traduza', 'Diga se a oração com <i>ut</i>/<i>nē</i> é final, consecutiva ou completiva (de ordem, de temor ou de resultado). Vocabulário: <i>discō, -ere</i>, aprender; <i>vereor, -ērī</i>, temer; <i>excitō</i>, acordar.', [
            ('<i>Legimus ut discāmus.</i>', 'Final: "Lemos para aprender." Presente → presente.'),
            ('<i>Tam celeriter cucurrit ut nēmō eum caperet.</i> (<i>currō, cucurrī</i>, correr)', 'Consecutiva, com <i>tam</i> e negativa <i>ut nēmō</i>: "Correu tão depressa que ninguém o apanhou."'),
            ('<i>Rogō tē nē abeās.</i> (<i>abeō</i>, ir embora)', 'Completiva de pedido, negativa com <i>nē</i>: "Peço-te que não vás embora."'),
            ('<i>Vereor nē pluat.</i>', 'Completiva de temor; <i>nē</i> = "que": "Temo que chova."'),
            ('<i>Vereor ut veniat.</i>', 'Completiva de temor; <i>ut</i> = "que não": "Temo que ele não venha."'),
            ('<i>Accidit ut amīcus abesset.</i> (<i>absum</i>, estar ausente)', 'Completiva de resultado, sujeito de <i>accidit</i>: "Aconteceu que o amigo estava ausente."'),
            ('<i>Tacuimus nē dominum excitārēmus.</i>', 'Final negativa: "Ficamos calados para não acordar o senhor." Perfeito → imperfeito.'),
            ('<i>Ut dīxī, puer abest.</i>', 'Nenhuma das três: <i>dīxī</i> está no indicativo, logo <i>ut</i> = "como". "Como eu disse, o menino está ausente."'),
        ]),
        exercicio('Exercício 2 · O tempo certo', 'Complete com o presente ou o imperfeito do subjuntivo do verbo entre parênteses, segundo a regra simples, e traduza.', [
            ('<i>Veniō ut tē ___</i> (videō)', '<i>videam</i>: principal no presente. "Venho para te ver."'),
            ('<i>Vēnī ut tē ___</i> (videō)', '<i>vidērem</i>: <i>vēnī</i> é perfeito, tempo passado. "Vim para te ver."'),
            ('<i>Imperābit mīlitibus ut ___</i> (pugnō)', '<i>pugnent</i>: principal no futuro → presente. "Ordenará aos soldados que lutem."'),
            ('<i>Timēbant nē hostēs ___</i> (veniō)', '<i>venīrent</i>: passado → imperfeito. "Temiam que os inimigos viessem."'),
            ('<i>Tanta erat tempestās ut nautae nōn ___</i> (nāvigō)', '<i>nāvigārent</i>: consecutiva depois de passado → imperfeito. "A tempestade era tão grande que os marinheiros não navegavam."'),
            ('<i>Hortātur mīlitēs ut fortēs ___</i> (sum)', '<i>sint</i>: <i>hortātur</i> é presente. "Exorta os soldados a serem valentes."'),
        ]),
        exercicio('Exercício 3 · Nē ou ut nōn?', 'Complete com <i>nē</i> ou <i>ut nōn</i> e explique.', [
            ('<i>Portās clausērunt ___ hostēs intrārent.</i> (<i>claudō, clausī</i>, fechar; <i>intrō</i>, entrar)', '<i>nē</i>: fecharam as portas com a intenção de impedir a entrada (final). "Fecharam as portas para que os inimigos não entrassem."'),
            ('<i>Tam fessī erant ___ labōrāre possent.</i>', '<i>ut nōn</i>: há <i>tam</i> e trata-se de resultado. "Estavam tão cansados que não podiam trabalhar."'),
            ('<i>Moneō tē ___ hōc faciās.</i>', '<i>nē</i>: completiva de conselho negativa. "Aconselho-te a não fazer isto."'),
            ('<i>Ita vīxit ___ quisquam eum vituperāret.</i> (<i>quisquam</i>, alguém; <i>vituperō</i>, censurar)', '<i>ut nōn</i>: <i>ita</i> anuncia uma consecutiva. "Viveu de tal modo que ninguém o censurava."'),
            ('<i>Accidit ___ litterae advenīrent.</i> (<i>litterae</i>, carta; <i>adveniō</i>, chegar)', '<i>ut nōn</i>: completiva de resultado, que se nega como a consecutiva. "Aconteceu que a carta não chegou."'),
        ]),
        exercicio('Exercício 4 · Imperō ou iubeō?', 'Reescreva a ordem com o outro verbo, mantendo o sentido.', [
            ('<i>Dux mīlitibus imperat ut castra mūniant.</i> (<i>castra mūniō</i>, fortificar o acampamento) → <i>iubeō</i>', '<i>Dux mīlitēs castra mūnīre iubet.</i> <i>Iubeō</i>: acusativo (<i>mīlitēs</i>) + infinitivo (<i>mūnīre</i>), sem <i>ut</i>.'),
            ('<i>Pater fīlium venīre iussit.</i> → <i>imperō</i>', '<i>Pater fīliō imperāvit ut venīret.</i> Dativo (<i>fīliō</i>) + <i>ut</i> + imperfeito, porque <i>imperāvit</i> é passado.'),
            ('<i>Magister puerīs imperat nē clāment.</i> → <i>vetō</i>', '<i>Magister puerōs clāmāre vetat.</i> A ordem negativa com <i>iubeō</i> se faz com <i>vetō</i> ("proibir") + acusativo e infinitivo.'),
        ]),
        exercicio('Exercício 5 · Leitura de frases autênticas', 'Classifique a oração com <i>ut</i>/<i>nē</i>, explique o tempo e traduza. Textos conferidos na fonte; macrons acrescentados.', [
            ('<i>Et respōnsō acceptō in somnīs nē redīrent ad Hērōdem, per aliam viam reversī sunt in regiōnem suam.</i> (Mateus 2,12; <i>respōnsum</i>, resposta, aviso; <i>somnus</i>, sono; <i>redeō</i>, voltar; <i>revertor, reversus</i>, regressar)', '<i>Nē redīrent</i> é completiva de ordem negativa, que depende da ideia de aviso contida em <i>respōnsō acceptō</i> (ablativo absoluto, capítulo 30): "tendo recebido em sonhos o aviso de que não voltassem a Herodes". Imperfeito porque a narração está no passado. Tradução: "E, avisados em sonho que não voltassem a Herodes, regressaram por outro caminho à sua região."'),
            ('<i>Fēcitque Deus duo lūmināria magna: lūmināre maius, ut praeesset diēī, et lūmināre minus, ut praeesset noctī.</i> (Gênesis 1,16; <i>lūmināre, -is</i>, luzeiro; <i>praesum</i> + dat., presidir a)', 'Duas finais: "para que presidisse ao dia… à noite". Imperfeito <i>praeesset</i> (de <i>praeesse</i>) porque <i>fēcit</i> é passado. "E Deus fez dois grandes luzeiros: o luzeiro maior para presidir ao dia, e o luzeiro menor para presidir à noite."'),
            ('<i>Tanta vīs probitātis est ut eam in hoste dīligāmus.</i> (Cícero, <i>Laelius</i> 29, na forma abreviada de A&amp;G § 537; o texto da Latin Library diz <i>ut eam vel in iīs quōs numquam vīdimus vel, quod maius est, in hoste etiam dīligāmus</i>; <i>probitās</i>, honestidade; <i>dīligō</i>, estimar)', 'Consecutiva com <i>tanta</i>; presente <i>dīligāmus</i> porque <i>est</i> é presente. "Tão grande é a força da honestidade que a estimamos até num inimigo."'),
            ('<i>Timeō nē Verrēs fēcerit.</i> (Cícero, <i>Verr.</i> 2.5.3, na forma abreviada de A&amp;G § 564; o texto completo, conferido na Latin Library, é <i>timeō nē C. Verrēs … omnia quae fēcit impūne fēcerit</i>)', 'Completiva de temor com <i>nē</i> = "que". O perfeito <i>fēcerit</i> indica uma ação já passada em relação ao temor presente (o capítulo 34 explica esse uso). "Temo que Verres tenha feito…" (no texto completo: "temo que Caio Verres tenha feito impunemente tudo o que fez")'),
        ]),
        exercicio('Exercício 6 · Do português para o latim', 'Traduza. Vocabulário: <i>discipulus, -ī</i>, aluno; <i>studeō, -ēre</i>, estudar; <i>ōrō, -āre</i>, rogar; <i>timeō</i>; <i>nauta, -ae</i>, marinheiro; <i>pereō, -īre</i>, morrer; <i>sīc</i>, assim; <i>cantō, -āre</i>, cantar; <i>omnēs</i>, todos; <i>lacrimō, -āre</i>, chorar.', [
            ('Os alunos estudam para aprender.', '<i>Discipulī student ut discant.</i> Final; presente → presente. Não use *<i>student discere</i>.'),
            ('Rogo-te que não partas.', '<i>Ōrō tē nē abeās.</i> Completiva de pedido negativa: <i>nē</i>; <i>ōrō</i> leva acusativo.'),
            ('Temíamos que os marinheiros morressem.', '<i>Timēbāmus nē nautae perīrent.</i> Temor: <i>nē</i> = "que"; passado → imperfeito (<i>perīre</i> + <i>-nt</i>).'),
            ('O poeta cantou de tal modo que todos choraram.', '<i>Poēta sīc cantāvit ut omnēs lacrimārent.</i> Consecutiva com <i>sīc</i>; o português usa o indicativo, o latim o subjuntivo imperfeito.'),
            ('Ordenou-lhes que saíssem.', '<i>Eīs imperāvit ut exīrent.</i> ou <i>Eōs exīre iussit.</i> As duas construções estão certas, cada uma com o seu verbo.'),
        ]),
    ],
    leituras=['caesar-commentarii-de-bello-gallico-selecoes', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'd-ooge-latin-for-beginners', 'nepos-de-viris-illustribus-vitae', 'bennett-new-latin-grammar', 'greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc'],
    leituras_nota='Os primeiros capítulos da Guerra da Gália (livro I, 2–7) estão cheios de ordens indiretas e finais com ut/nē: leia-os procurando cada subjuntivo e perguntando qual das famílias deste capítulo ele representa (o capítulo 44 lê César por inteiro). Na Vulgata, Gênesis 1 e Mateus 2 trazem finais e completivas em frases curtas. As Vidas de Cornélio Nepos são a prosa clássica mais simples para treinar finais e consecutivas. Latin for Beginners, de D\'Ooge, dedica as lições LXII, LXIV, LXV e LXVIII a estas construções. Para consulta, Bennett §§ 282–284 e 294–297, e Allen & Greenough §§ 529–538 e 560–569.',
)
