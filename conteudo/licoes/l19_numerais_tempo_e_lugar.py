from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='19-numerais-tempo-e-lugar', titulo='Numerais; expressões de tempo e de lugar',
    titulo_latim='Dē numerīs, tempore et locō', tempo='70 min',
    resumo='Os numerais latinos (cardinais, ordinais, distributivos e advérbios numerais), a declinação de ūnus, duo, trēs e mīlia, os algarismos romanos, e as construções que respondem a "quando?", "em quanto tempo?" e "por quanto tempo?", e a "onde?", "para onde?" e "de onde?", com a regra especial dos nomes de cidade, de domus e de rūs e o caso locativo (Rōmae, domī).',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['cardinais', 'ordinais', 'declinação de ūnus, duo, trēs', 'mīlle e mīlia', 'distributivos', 'advérbios numerais', 'algarismos romanos', 'ablativo de tempo (quando?)', 'ablativo de tempo (em quanto tempo?)', 'acusativo de duração', 'post e ante com acusativo', 'lugar onde, para onde, de onde', 'nomes de cidade e ilhas pequenas', 'domus e rūs', 'locativo', 'datas romanas (nota)', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 4 (as preposições <i>in</i>, <i>ad</i>, <i>ab</i>, <i>ex</i>, <i>dē</i> e os casos que regem), capítulo 5 (adjetivos como <i>bonus</i>, modelo dos ordinais) e capítulo 11 (quarta e quinta declinações: <i>domus</i>, <i>diēs</i>). O capítulo 18 (superlativos) ajuda a entender os ordinais.',
                       licoes=['04-a-primeira-declinacao', '05-a-segunda-declinacao', '11-a-quarta-e-a-quinta-declinacoes', '18-comparativos-e-superlativos']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 66 (ūnus, declinado como tōtus), §§ 78–81 (classes de numerais; tabela de cardinais, ordinais, distributivos e advérbios; declinação de duo, trēs, mīlia; usos: et nos compostos, subtração em duodēvīgintī, distributivos), § 181 (acusativo de duração e de extensão; abhinc), § 182 (acusativo de lugar para onde sem preposição: cidades, ilhas pequenas, domum, rūs; ad = "perto de"), § 228 (lugar onde; ablativo dos nomes de cidade no plural e da 3ª; rūrī), § 229 (lugar de onde: Rōmā, domō, rūre; ab com cidades), §§ 230–231 (ablativo de tempo quando e em quanto tempo; in pāce, in bellō; 231.1, ablativo de duração ocasional), § 232 (locativo: Rōmae, Corinthī, domī, humī), § 371 (calendário romano)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', url='https://dcc.dickinson.edu/grammar/latin/cardinal-and-ordinal-numbers', nota='§ 80 (locativo da 3ª: rūrī, Carthāginī ou Carthāgine), §§ 132–138 (numerais; algarismos romanos, inclusive IIII e VIIII; declinação de duo e trēs; mīlle e mīlia com genitivo; distributivos; advérbios numerais), §§ 421–424 (locativo; tempo quando, dentro do qual e duração; ablativo de duração ocasional; post e ante), § 425 (extensão), §§ 426–428 (relações de lugar; cidades, ilhas pequenas, domus, rūs; urbs e oppidum com preposição; ad = "nas proximidades"), § 631 (datas)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§§ 88–89 (classes de numerais; ūnus, duo, trēs; mīlle e mīlia), §§ 268–279 (lugar, tempo e espaço; locativo; domī com genitivo do possuidor; abhinc)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 40 (diēs masculino ou feminino), nn. 61–67 (numerais; declinação de ūnus; mīlle e mīlia), nn. 178–188 (complementos de lugar: cidades, ilhas pequenas, domus, rūs, locativo), nn. 193–195 (complementos de tempo; no OCR os números aparecem deformados)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Atos 28,11–14', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Acta_Apostolorum', nota='frases das seções 5 e 6, conferidas na Wikisource latina; macrons acrescentados', tipo='dominio_publico'),
        referencia('Eutrópio, Breviarium ab urbe condita I, 1, 3 e 7', None, catalogo='eutropius-breviarium-ab-urbe-condita', url='https://www.thelatinlibrary.com/eutropius/eutropius1.shtml', nota='frases das seções 3 e 6 e da nota sobre as datas, conferidas na The Latin Library; macrons acrescentados', tipo='dominio_publico'),
        referencia('César, De bello Gallico I, 1, 1', None, catalogo='caesar-commentarii-de-bello-gallico-texto-integral', url='https://www.thelatinlibrary.com/caesar/gall1.shtml', nota='frase da seção 2, conferida na The Latin Library; macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Contar de 1 a 20 e pelas dezenas, centenas e milhares em latim, declinando <i>ūnus</i>, <i>duo</i>, <i>trēs</i> e usando <i>mīlia</i> com genitivo.',
        'Reconhecer e formar os ordinais (declinados como <i>bonus</i>), e identificar distributivos e advérbios numerais.',
        'Ler e escrever algarismos romanos, inclusive as formas aditivas antigas (IIII, VIIII).',
        'Traduzir as expressões de tempo: ablativo para "quando?" e "em quanto tempo?", acusativo para "por quanto tempo?".',
        'Exprimir lugar onde, para onde e de onde, com preposições e, nos nomes de cidade, em <i>domus</i> e <i>rūs</i>, sem preposição e com o locativo.',
    ],
    secoes=[
        ('Os cardinais: contar em latim', f'''
<p>Os <b>numerais cardinais</b> respondem à pergunta "quantos?" (<i>quot?</i>). O português herdou quase todos, e por isso a lista é mais fácil do que parece: <i>ūnus</i> (um), <i>duo</i> (dois), <i>trēs</i> (três), <i>quattuor</i>, <i>quīnque</i>, <i>sex</i>, <i>septem</i>, <i>octō</i>, <i>novem</i>, <i>decem</i>. De 11 a 17, junta-se a unidade a <i>-decim</i> ("dez"): <i>ūndecim, duodecim, tredecim</i>… E 18 e 19 se dizem por <b>subtração</b>: <i>duodēvīgintī</i>, "dois de vinte", e <i>ūndēvīgintī</i>, "um de vinte" (Bennett § 81.2). O mesmo vale para 28 e 29, 38 e 39, e assim por diante: <i>duodētrīgintā</i>, <i>ūndēquadrāgintā</i>.</p>
{tabela(['Nº', 'Cardinal', 'Nº', 'Cardinal', 'Nº', 'Cardinal'], [
    ['1', 'ūnus, ūna, ūnum', '11', 'ūndecim', '30', 'trīgintā'],
    ['2', 'duo, duae, duo', '12', 'duodecim', '40', 'quadrāgintā'],
    ['3', 'trēs, tria', '13', 'tredecim', '50', 'quīnquāgintā'],
    ['4', 'quattuor', '14', 'quattuordecim', '60', 'sexāgintā'],
    ['5', 'quīnque', '15', 'quīndecim', '70', 'septuāgintā'],
    ['6', 'sex', '16', 'sēdecim', '80', 'octōgintā'],
    ['7', 'septem', '17', 'septendecim', '90', 'nōnāgintā'],
    ['8', 'octō', '18', 'duodēvīgintī', '100', 'centum'],
    ['9', 'novem', '19', 'ūndēvīgintī', '200', 'ducentī, -ae, -a'],
    ['10', 'decem', '20', 'vīgintī', '1000', 'mīlle'],
], 'Os cardinais (Bennett § 79; Allen e Greenough § 133)', latim_cols=(1, 3, 5))}
<p>As outras centenas seguem <i>ducentī</i>: <i>trecentī</i> (300), <i>quadringentī</i> (400), <i>quīngentī</i> (500), <i>sescentī</i> (600), <i>septingentī</i> (700), <i>octingentī</i> (800), <i>nōngentī</i> (900). Nos números compostos abaixo de 100, ou o maior vem primeiro, sem <i>et</i> (<i>vīgintī ūnus</i>), ou o menor vem primeiro, com <i>et</i> (<i>ūnus et vīgintī</i>); acima de 100, o maior vem primeiro, como em português (<i>centum vīgintī septem</i>, 127).</p>
<h3>Quais se declinam</h3>
<p>A maioria dos cardinais é <b>indeclinável</b>: <i>quattuor</i>, <i>septem</i>, <i>vīgintī</i>, <i>centum</i> ficam iguais em qualquer caso (<i>cum quattuor mīlitibus</i>, <i>quattuor mīlitum</i>). Declinam-se apenas <i>ūnus</i>, <i>duo</i>, <i>trēs</i>, as centenas de 200 a 900 (como o plural de <i>bonus</i>: <i>ducentī, ducentae, ducenta; ducentōrum…</i>) e o plural <i>mīlia</i>.</p>
<p><i>Ūnus</i> se declina como <i>bonus</i>, exceto no genitivo e no dativo singular, que são <b><i>ūnīus</i></b> e <b><i>ūnī</i></b> para os três gêneros, como <i>tōtus</i> e <i>sōlus</i> (Bennett § 66). <i>Duo</i> conserva uma terminação antiga em <i>-o</i> e tem dativo e ablativo em <i>-ōbus</i>, <i>-ābus</i>; <i>trēs</i> se declina como o plural de um adjetivo de segunda classe.</p>
{tabela_declinacao('ūnus, duo, trēs', [
    ('ūnus · ūna · ūnum', 'duo · duae · duo', 'trēs · tria'), ('ūn<b>īus</b> (3 gêneros)', 'du<b>ōrum</b> · du<b>ārum</b> · du<b>ōrum</b>', 'tr<b>ium</b>'),
    ('ūn<b>ī</b> (3 gêneros)', 'du<b>ōbus</b> · du<b>ābus</b> · du<b>ōbus</b>', 'tr<b>ibus</b>'), ('ūnum · ūnam · ūnum', 'du<b>ōs</b> (<i>ou</i> duo) · du<b>ās</b> · duo', 'trēs · tria'),
    ('ūn<b>ō</b> · ūn<b>ā</b> · ūn<b>ō</b>', 'du<b>ōbus</b> · du<b>ābus</b> · du<b>ōbus</b>', 'tr<b>ibus</b>')],
    casos=('Nominativo', 'Genitivo', 'Dativo', 'Acusativo', 'Ablativo'), colunas=('ūnus (m. · f. · n.)', 'duo (m. · f. · n.)', 'trēs (m./f. · n.)'))}
<h3>Mīlle e mīlia</h3>
<p>"Mil" tem duas construções, e a diferença importa para a leitura. No singular, <b><i>mīlle</i></b> é um <b>adjetivo indeclinável</b>, como <i>centum</i>: <i>mīlle mīlitēs</i>, "mil soldados"; <i>cum mīlle mīlitibus</i>, "com mil soldados". No plural, <b><i>mīlia</i></b> é um <b>substantivo neutro</b> ("milhares"), declinado como um neutro de tema em <i>-i</i> (<i>mīlia, mīlium, mīlibus</i>), e a coisa contada vai para o <b>genitivo</b>: <i>duo mīlia mīlitum</i>, literalmente "dois milhares de soldados" (Bennett § 80.5; Allen e Greenough § 135.c). O português diz "dois mil soldados", sem preposição, e por isso o aluno tende a escrever *<i>duo mīlle mīlitēs</i>, que não existe.</p>
{tabela_declinacao('mīlia, "milhares" (substantivo neutro plural)', [('mīli<b>a</b>',), ('mīli<b>um</b>',), ('mīli<b>bus</b>',), ('mīli<b>a</b>',), ('mīli<b>a</b>',), ('mīli<b>bus</b>',)], colunas=('Plural',))}
{exemplos([('Mārcus <b>ūnum</b> fīlium et <b>duās</b> fīliās habet.', 'Marcos tem um filho e duas filhas. (<i>ūnum</i>, ac. m.; <i>duās</i>, ac. f.)'),
           ('Agricola cum <b>tribus</b> servīs in agrō labōrat.', 'O agricultor trabalha no campo com três escravos. (<i>tribus</i>, abl. depois de <i>cum</i>)'),
           ('In oppidō sunt <b>mīlle</b> hominēs.', 'Na cidade há mil pessoas. (<i>mīlle</i>, adjetivo indeclinável)'),
           ('In oppidō sunt <b>tria mīlia</b> hominum.', 'Na cidade há três mil pessoas. (<i>tria</i>, neutro, concorda com <i>mīlia</i>; <i>hominum</i>, genitivo)')])}
'''),
        ('Ordinais, distributivos e advérbios numerais', f'''
<p>Os <b>ordinais</b> respondem a "qual na ordem?" e são adjetivos de primeira classe, declinados como <i>bonus</i>: <i>prīmus, -a, -um</i>. Você já conhece <i>prīmus</i> do capítulo 18, como superlativo sem positivo; de fato, a maioria dos ordinais tem forma de superlativo (<i>decimus</i>, <i>centēsimus</i>), o que faz sentido: o décimo é o último de uma série de dez. <i>Secundus</i> vem de "seguir" (o que segue o primeiro); para "o segundo de dois", o latim usa também <i>alter</i>.</p>
{tabela(['Nº', 'Ordinal', 'Nº', 'Ordinal', 'Nº', 'Ordinal'], [
    ['1º', 'prīmus', '8º', 'octāvus', '15º', 'quīntus decimus'],
    ['2º', 'secundus (alter)', '9º', 'nōnus', '18º', 'duodēvīcēsimus'],
    ['3º', 'tertius', '10º', 'decimus', '20º', 'vīcēsimus'],
    ['4º', 'quārtus', '11º', 'ūndecimus', '30º', 'trīcēsimus'],
    ['5º', 'quīntus', '12º', 'duodecimus', '40º', 'quadrāgēsimus'],
    ['6º', 'sextus', '13º', 'tertius decimus', '100º', 'centēsimus'],
    ['7º', 'septimus', '14º', 'quārtus decimus', '1000º', 'mīllēsimus'],
], 'Os ordinais (todos declinados como bonus, -a, -um)', latim_cols=(1, 3, 5))}
<p>Nos ordinais compostos, as duas partes se declinam: "no décimo terceiro ano" é <i>tertiō decimō annō</i>. As gramáticas registram também a grafia <i>-ēnsimus</i> (<i>vīcēnsimus</i>), equivalente a <i>-ēsimus</i>. Os ordinais servem para tudo o que o português conta em ordem, e sobretudo para o tempo, como você verá na seção 4: "no terceiro ano", "na quarta hora". Os nomes de reis e papas também usam ordinais: <i>Pius Nōnus</i>, Pio IX.</p>
<p>César abre a <i>Guerra da Gália</i> com um cardinal e um ordinal na mesma frase:</p>
{exemplos([('Gallia est omnis dīvīsa in partēs <b>trēs</b>, quārum <b>ūnam</b> incolunt Belgae, aliam Aquītānī, <b>tertiam</b> quī ipsōrum linguā Celtae, nostrā Gallī appellantur.', 'A Gália, em seu conjunto, está dividida em três partes, das quais uma é habitada pelos belgas, outra pelos aquitanos, a terceira pelos que na língua deles se chamam celtas e na nossa, gauleses. (César, <i>BG</i> 1.1.1; <i>dīvīsa</i>, dividida; <i>incolunt</i>, habitam; <i>quārum</i>, das quais, capítulo 16)')])}
<p>Note a sequência <i>ūnam … aliam … tertiam</i>: o cardinal <i>ūnus</i> no feminino acusativo, concordando com <i>partem</i> subentendido, e depois o ordinal <i>tertius</i>, também no acusativo feminino.</p>
<h3>Distributivos e advérbios numerais</h3>
<p>Dois outros grupos de numerais aparecem com menos frequência, e basta reconhecê-los. Os <b>distributivos</b> respondem a "quantos de cada vez? quantos para cada um?" e se declinam como o plural de <i>bonus</i>: <i>singulī</i> (um a um, um para cada), <i>bīnī</i> (dois a dois, dois para cada), <i>ternī</i> (ou <i>trīnī</i>), <i>quaternī</i>, <i>quīnī</i>, … <i>dēnī</i> (dez para cada). Eles também substituem o cardinal com nomes que só existem no plural, mas significam uma coisa só: <i>castra</i>, "acampamento", é plural, e "dois acampamentos" se diz <i>bīna castra</i> (Bennett § 81.4; Allen e Greenough § 137.b). Os <b>advérbios numerais</b> respondem a "quantas vezes?": <i>semel</i> (uma vez), <i>bis</i> (duas vezes), <i>ter</i> (três vezes), <i>quater</i> (quatro vezes), <i>quīnquiēs</i>, … <i>deciēs</i>, <i>centiēs</i>, <i>mīliēs</i>. O português guarda <i>bis</i> no grito "bis!" e em compostos como "bisavô".</p>
{exemplos([('Magister puerīs <b>bīna</b> māla dat.', 'O mestre dá duas maçãs a cada menino. (<i>bīna</i>: distributivo, neutro plural; <i>mālum, -ī</i>, maçã)'),
           ('Nauta <b>ter</b> in annō nāvigat.', 'O marinheiro navega três vezes por ano. (<i>ter</i>: advérbio numeral; <i>in annō</i>, "no espaço de um ano")')])}
'''),
        ('Os algarismos romanos', f'''
<p>Os romanos escreviam os números com sete letras: <b>I</b> = 1, <b>V</b> = 5, <b>X</b> = 10, <b>L</b> = 50, <b>C</b> = 100, <b>D</b> = 500, <b>M</b> = 1000. A regra básica é a <b>adição</b>: os sinais se somam da esquerda para a direita, do maior para o menor (<i>XVI</i> = 10 + 5 + 1 = 16; <i>MDCLX</i> = 1660). Usa-se também a <b>subtração</b>: um sinal menor antes de um maior se subtrai dele (<i>IV</i> = 4, <i>IX</i> = 9, <i>XL</i> = 40, <i>XC</i> = 90). Para 400 e 900, a convenção atual escreve <i>CD</i> e <i>CM</i>; Allen e Greenough (§ 133) só registram <i>CCCC</i> e <i>DCCCC</i>.</p>
<p>As formas <b>aditivas</b> <i>IIII</i> e <i>VIIII</i>, porém, também são antigas, e Allen e Greenough (§ 133) registram as duas grafias lado a lado (<i>IIII</i> ou <i>IV</i>, <i>VIIII</i> ou <i>IX</i>, <i>XXXX</i> ou <i>XL</i>, <i>LXXXX</i> ou <i>XC</i>, <i>CCCC</i>, <i>DCCCC</i>). Não as tome por erros: são tão romanas quanto as outras. Na convenção que se usa hoje, a subtração só se faz com sinais vizinhos (I antes de V e X, X antes de L e C, C antes de D e M); por isso 99 se escreve <i>XCIX</i>, e não *<i>IC</i>.</p>
{tabela(['Algarismo', 'Leitura', 'Valor', 'Em latim'], [
    ['XIV', 'X + IV', '14', 'quattuordecim · quārtus decimus'],
    ['XIX', 'X + IX', '19', 'ūndēvīgintī · ūndēvīcēsimus'],
    ['XL', 'L − X', '40', 'quadrāgintā'],
    ['LXXXIII', 'L + XXX + III', '83', 'octōgintā trēs <i>ou</i> trēs et octōgintā'],
    ['XCIX', 'XC + IX', '99', 'nōnāgintā novem'],
    ['CDXLIV', 'CD + XL + IV', '444', 'quadringentī quadrāgintā quattuor'],
    ['MDCCLIII', 'M + DCC + L + III', '1753', 'mīlle septingentī quīnquāgintā trēs'],
    ['MMXXVI', 'MM + XX + VI', '2026', 'duo mīlia vīgintī sex'],
], 'Lendo algarismos romanos', latim_cols=(0, 3))}
<p>Nos textos, o algarismo romano se lê com a palavra latina no caso que a frase pede. Eutrópio, contando o recenseamento feito pelo rei Sérvio Túlio, escreve com algarismos:</p>
{exemplos([('Sub eō Rōma … habuit capita LXXXIII mīlia cīvium Rōmānōrum.', 'Sob ele, Roma teve oitenta e três mil cabeças [= pessoas recenseadas] de cidadãos romanos. (Eutrópio 1.7; leia <i>octōgintā tria mīlia</i>, com <i>tria</i> neutro concordando com <i>mīlia</i>, e o genitivo <i>cīvium Rōmānōrum</i>)')])}
<p>Repare que o genitivo depois de <i>mīlia</i> é exatamente a regra da seção 1, agora num texto autêntico. A frase completa tem ainda um ablativo absoluto (<i>omnibus in cēnsum dēlātīs</i>, "registrados todos no censo"), que o capítulo 30 explica.</p>
'''),
        ('Expressões de tempo', f'''
<p>O português usa preposições para o tempo ("em 1500", "durante três anos", "em três dias"). O latim, quase sempre, usa só o <b>caso</b>, e escolhe o caso pela pergunta a que a expressão responde. São três perguntas.</p>
<h3>1. Quando? Ablativo</h3>
<p>O momento em que algo acontece vai para o <b>ablativo sem preposição</b> (Bennett § 230; Allen e Greenough § 423): <i>hieme</i>, "no inverno"; <i>aestāte</i>, "no verão"; <i>nocte</i>, "de noite"; <i>prīmā lūce</i>, "ao raiar do dia"; <i>tertiā hōrā</i>, "na terceira hora"; <i>eō annō</i>, "naquele ano". Com números, usa-se o <b>ordinal</b>: "no ano 1500" é <i>annō mīllēsimō quīngentēsimō</i>, "no milésimo quingentésimo ano". A regra vale para palavras que já significam tempo (<i>annus, hōra, diēs, nox, hiems, aestās, vēr</i>); palavras que não indicam tempo pedem <i>in</i>: <i>in bellō</i>, "na guerra"; <i>in pāce</i>, "na paz". Mas, se vierem com um adjetivo que marque a época, dispensam a preposição: <i>bellō Pūnicō secundō</i>, "na segunda guerra púnica" (Bennett § 230.2).</p>
<h3>2. Em quanto tempo? Ablativo</h3>
<p>O prazo dentro do qual algo acontece também vai para o <b>ablativo</b>, com ou sem <i>in</i>: <i>tribus diēbus</i>, "em três dias, dentro de três dias"; <i>paucīs hōrīs</i>, "em poucas horas"; <i>ter in annō</i>, "três vezes no ano" (Bennett § 231).</p>
<h3>3. Por quanto tempo? Acusativo</h3>
<p>A <b>duração</b>, o tempo ao longo do qual algo se estende, vai para o <b>acusativo sem preposição</b> (Bennett § 181; Allen e Greenough § 423): <i>trēs annōs</i>, "durante três anos"; <i>multōs diēs</i>, "por muitos dias"; <i>tōtam noctem</i>, "a noite inteira". A preposição <i>per</i> reforça a ideia de continuidade: <i>per decem diēs</i>, "ao longo de dez dias". É a mesma lógica do acusativo de extensão no espaço (<i>mīlia passuum tria</i>, "três milhas"): o acusativo mede o que é percorrido.</p>
{tabela(['Pergunta', 'Caso', 'Exemplo', 'Tradução'], [
    ['quando?', 'ablativo', '<i>hieme · tertiā hōrā · annō prīmō</i>', 'no inverno · na terceira hora · no primeiro ano'],
    ['em quanto tempo?', 'ablativo (às vezes <i>in</i> + abl.)', '<i>tribus diēbus · paucīs annīs</i>', 'em três dias · em poucos anos'],
    ['por quanto tempo?', 'acusativo (ou <i>per</i> + ac.)', '<i>trēs annōs · per decem diēs</i>', 'durante três anos · ao longo de dez dias'],
    ['depois de / antes de quanto?', '<i>post</i> / <i>ante</i> + ac.', '<i>post trēs annōs · ante paucōs diēs</i>', 'três anos depois · poucos dias antes'],
    ['há quanto tempo?', '<i>abhinc</i> + ac.', '<i>abhinc septem annōs</i>', 'há sete anos, sete anos atrás'],
], 'O tempo em latim: a pergunta decide o caso', latim_cols=())}
{exemplos([('Agricolae <b>aestāte</b> in agrīs labōrant, <b>hieme</b> domī manent.', 'Os agricultores trabalham nos campos no verão; no inverno, ficam em casa. (ablativos de tempo; <i>domī</i>, seção 5)'),
           ('Nautae <b>decem diēbus</b> ad īnsulam nāvigant.', 'Os marinheiros navegam até a ilha em dez dias. (ablativo: o prazo)'),
           ('Poēta <b>multōs annōs</b> in vīllā vīvit.', 'O poeta vive muitos anos na casa de campo. (acusativo: a duração)'),
           ('Morbō dēcessit <b>quadrāgēsimō et tertiō</b> imperiī <b>annō</b>.', 'Morreu de doença no quadragésimo terceiro ano do seu reinado. (Eutrópio 1.3, sobre o rei Numa; ordinal no ablativo: "quando?")')])}
{observacao('O latim bíblico às vezes mede a duração com o ablativo', 'A regra clássica é acusativo para a duração, mas o próprio Bennett (§ 231.1) e Allen e Greenough (§ 424.b) registram, ocasionalmente, o ablativo com esse sentido, e a Vulgata o usa muito: <i>cum iēiūnāsset quadrāgintā diēbus et quadrāgintā noctibus</i>, "depois de jejuar quarenta dias e quarenta noites" (Mt 4,2), e <i>mānsimus ibi trīduō</i>, "ficamos ali três dias" (At 28,12). Ao ler, deixe o sentido do verbo decidir; ao escrever, use o acusativo.')}
<p>Uma palavra sobre <i>diēs</i> (capítulo 11): no singular ela é normalmente masculina, mas pode ser feminina quando designa um dia marcado, uma data (Ravizza, n. 40). Por isso você encontrará tanto <i>eō diē</i> quanto <i>certā diē</i>, "no dia fixado"; a Vulgata, nas frases de Atos que você vai analisar, diz <i>secundā diē</i>.</p>
'''),
        ('Expressões de lugar e o locativo', f'''
<p>No capítulo 4 você aprendeu a regra geral, que continua valendo para a grande maioria dos nomes: <b>lugar onde</b> = <i>in</i> + ablativo (<i>in silvā</i>); <b>lugar para onde</b> = <i>in</i> ou <i>ad</i> + acusativo (<i>in silvam</i>, "para dentro da floresta"; <i>ad silvam</i>, "até a floresta"); <b>lugar de onde</b> = <i>ab</i>, <i>ex</i>, <i>dē</i> + ablativo (<i>ex silvā</i>, "de dentro da floresta"; <i>ā silvā</i>, "da floresta, a partir dela"). Os nomes de países e de ilhas grandes seguem essa regra: <i>in Italiā</i>, <i>in Graeciam</i>, <i>ex Siciliā</i>.</p>
<h3>A exceção: cidades, ilhas pequenas, domus e rūs</h3>
<p>Com os <b>nomes de cidades</b> e de <b>ilhas pequenas</b> (que em geral se confundem com a sua cidade) e com as palavras <b><i>domus</i></b> (casa) e <b><i>rūs</i></b> (campo, zona rural), o latim <b>não usa preposição</b> (Bennett §§ 182, 228–229, 232; Allen e Greenough § 427):</p>
<ul>
<li><b>para onde</b>: acusativo puro: <i>Rōmam</i>, "para Roma"; <i>Athēnās</i>, "para Atenas"; <i>domum</i>, "para casa"; <i>rūs</i>, "para o campo".</li>
<li><b>de onde</b>: ablativo puro: <i>Rōmā</i>, "de Roma"; <i>Athēnīs</i>, "de Atenas"; <i>domō</i>, "de casa"; <i>rūre</i>, "do campo".</li>
<li><b>onde</b>: o <b>locativo</b>, um antigo caso de lugar que sobreviveu nessas palavras: <i>Rōmae</i>, "em Roma"; <i>Corinthī</i>, "em Corinto"; <i>domī</i>, "em casa"; <i>rūrī</i>, "no campo".</li>
</ul>
<p>Qual é a forma do locativo? Nos nomes <b>singulares da 1ª e da 2ª declinações</b>, ele se parece com o genitivo: <i>Rōmae</i> (de <i>Rōma, -ae</i>), <i>Corinthī</i> (de <i>Corinthus, -ī</i>), <i>Brundisiī</i> (de <i>Brundisium, -ī</i>). Nos nomes <b>plurais</b> e nos da <b>3ª declinação</b>, tem a forma do ablativo: <i>Athēnīs</i> (de <i>Athēnae, -ārum</i>, que só existe no plural), <i>Puteolīs</i> (de <i>Puteolī, -ōrum</i>), <i>Carthāgine</i> ou <i>Carthāginī</i> (de <i>Carthāgō, -inis</i>). As gramáticas divergem só no nome: Bennett (§ 228.1) chama essas formas de ablativo; Allen e Greenough (§§ 80 e 427) as tratam como locativo. Para o leitor, o importante é que, com um nome de cidade, a forma sem preposição pode significar "em".</p>
{tabela(['', 'Onde? (locativo)', 'Para onde? (acusativo)', 'De onde? (ablativo)'], [
    ['<i>Rōma, -ae</i> (f.)', 'Rōm<b>ae</b>, em Roma', 'Rōm<b>am</b>, para Roma', 'Rōm<b>ā</b>, de Roma'],
    ['<i>Corinthus, -ī</i> (f.)', 'Corinth<b>ī</b>, em Corinto', 'Corinth<b>um</b>, para Corinto', 'Corinth<b>ō</b>, de Corinto'],
    ['<i>Athēnae, -ārum</i> (f. pl.)', 'Athēn<b>īs</b>, em Atenas', 'Athēn<b>ās</b>, para Atenas', 'Athēn<b>īs</b>, de Atenas'],
    ['<i>Carthāgō, -inis</i> (f.)', 'Carthāgin<b>e</b> / -<b>ī</b>, em Cartago', 'Carthāgin<b>em</b>, para Cartago', 'Carthāgin<b>e</b>, de Cartago'],
    ['<i>domus, -ūs</i> (f.)', 'dom<b>ī</b>, em casa', 'dom<b>um</b>, para casa', 'dom<b>ō</b>, de casa'],
    ['<i>rūs, rūris</i> (n.)', 'rūr<b>ī</b>, no campo', 'rūs, para o campo', 'rūr<b>e</b>, do campo'],
    ['<i>Italia, -ae</i> (país: regra geral)', 'in Italiā', 'in Italiam', 'ex Italiā'],
], 'Nomes de cidade, domus e rūs: sem preposição', latim_cols=(1, 2, 3))}
<p>Por que essa exceção? O locativo e o acusativo de direção sem preposição são usos muito antigos dos casos; a língua os conservou justamente nas palavras de lugar que se usavam a toda hora (o nome da cidade, "em casa", "no campo"), enquanto, no resto, as preposições foram tornando a relação mais clara (Allen e Greenough § 421). O português tem algo parecido em "ir a Roma", "estar em casa", sem artigo.</p>
<p>Três detalhes completam a regra. Primeiro, <i>ad</i> com nome de cidade significa "para perto de, nas imediações de": <i>ad Rōmam</i>, "para as proximidades de Roma", e <i>ab</i> pode indicar "dos arredores de" (Bennett §§ 182.3 e 229.2; Allen e Greenough § 428.a). Segundo, as palavras <i>urbs</i> e <i>oppidum</i> sempre pedem preposição, mesmo ao lado do nome da cidade: <i>Rōmae in urbe</i>, "em Roma, na cidade"; <i>ad urbem Rōmam</i> ou <i>Rōmam ad urbem</i>, "para a cidade de Roma" (Allen e Greenough § 428.b). Terceiro, <i>humī</i>, "no chão", é outro locativo de uso corrente (Bennett § 232.2).</p>
{exemplos([('Mārcus <b>Rōmae</b> habitat, sed frāter eius <b>Athēnīs</b>.', 'Marcos mora em Roma, mas o irmão dele, em Atenas. (locativos)'),
           ('Nauta <b>Corinthō</b> <b>Athēnās</b> nāvigat.', 'O marinheiro navega de Corinto para Atenas. (ablativo de origem e acusativo de direção, sem preposições)'),
           ('Puerī <b>domum</b> veniunt; pater <b>rūrī</b> labōrat.', 'Os meninos vêm para casa; o pai trabalha no campo.'),
           ('Agricola <b>rūre</b> <b>in urbem</b> venit.', 'O agricultor vem do campo para a cidade. (<i>rūre</i> sem preposição; <i>urbem</i>, nome comum, com <i>in</i>)')])}
{dica('<b>Como ler.</b> Diante de um nome de cidade sem preposição, pergunte: há verbo de movimento? Se há, o acusativo é "para" (<i>Rōmam venit</i>) e o ablativo é "de" (<i>Rōmā venit</i>). Se não há, a forma em <i>-ae</i>, <i>-ī</i> ou <i>-īs</i> é quase sempre "em" (<i>Rōmae est</i>). E não leia <i>Rōmae</i> como genitivo só porque a forma é igual: "de Roma", como origem, seria <i>Rōmā</i>.')}
<h3>Nota: as datas romanas</h3>
<p>Os romanos não numeravam os dias do mês de 1 a 31. Contavam para trás a partir de três dias fixos: as <b>Calendas</b> (<i>Kalendae</i>), dia 1; as <b>Nonas</b> (<i>Nōnae</i>), dia 5 (dia 7 em março, maio, julho e outubro); e os <b>Idos</b> (<i>Īdūs</i>), dia 13 (dia 15 nesses quatro meses). O nome do mês é um adjetivo que concorda com esses nomes: <i>Īdibus Mārtiīs</i>, "nos Idos de março", 15 de março, com o ablativo de tempo da seção 4. Os outros dias se diziam "tantos dias antes" do próximo ponto fixo, contando os dois extremos (Bennett § 371; Allen e Greenough § 631). Assim, Eutrópio (1.1) diz que Rômulo fundou a cidade <i>XI Kal. Maiās</i>, isto é, no décimo primeiro dia antes das Calendas de maio, contando o próprio 1º de maio: 21 de abril, a data tradicional da fundação de Roma.</p>
'''),
        ('Análise gramatical: uma viagem a Roma', f'''
<p>O fim dos Atos dos Apóstolos narra, na primeira pessoa do plural, a viagem de Paulo e dos seus companheiros de Malta até Roma. Em poucas linhas, o texto reúne numerais e quase todas as construções de tempo e de lugar deste capítulo. Os verbos estão no perfeito (capítulo 13): <i>nāvigāvimus</i>, "navegamos"; <i>vēnimus</i>, "chegamos".</p>
{exemplos([('Post mēnsēs autem trēs nāvigāvimus in nāvī Alexandrīnā.', 'Três meses depois, navegamos num navio de Alexandria. (At 28,11)'),
           ('… secundā diē vēnimus Puteolōs: ubi inventīs frātribus rogātī sumus manēre apud eōs diēs septem: et sīc vēnimus Rōmam.', '… no segundo dia chegamos a Putéolos, onde, tendo encontrado irmãos, fomos convidados a ficar com eles sete dias; e assim chegamos a Roma. (At 28,13–14)')])}
{analise('Atos 28,11, palavra a palavra', [
    ('Post', 'post (preposição)', 'rege acusativo', 'introduz a distância no tempo: "depois de"'),
    ('mēnsēs', 'mēnsis, -is (m.), mês', 'acusativo plural, 3ª declinação', 'regido por <i>post</i>'),
    ('autem', 'autem (conjunção)', 'invariável; vem em segundo lugar', '"e, então": liga ao que precede'),
    ('trēs', 'trēs, tria, três', 'acusativo plural masculino', 'concorda com <i>mēnsēs</i>: <i>post mēnsēs trēs</i>, "três meses depois"'),
    ('nāvigāvimus', 'nāvigō, -āre, navegar', 'perfeito, 1ª pessoa do plural', 'verbo: "navegamos"'),
    ('in', 'in (preposição)', 'aqui com ablativo', 'lugar onde: "num"'),
    ('nāvī', 'nāvis, -is (f.), navio', 'ablativo singular, tema em <i>-i</i> (capítulo 10)', 'lugar onde, com <i>in</i>'),
    ('Alexandrīnā', 'Alexandrīnus, -a, -um, de Alexandria', 'ablativo singular feminino', 'concorda com <i>nāvī</i>'),
])}
{analise('Atos 28,13–14 (trechos), palavra a palavra', [
    ('secundā', 'secundus, -a, -um, segundo', 'ordinal, ablativo singular feminino', 'concorda com <i>diē</i>'),
    ('diē', 'diēs, -ēī, dia (aqui feminino)', 'ablativo singular, 5ª declinação', 'tempo: "quando?" = "no segundo dia"'),
    ('vēnimus', 'veniō, -īre, vir, chegar', 'perfeito, 1ª pessoa do plural', 'verbo de movimento'),
    ('Puteolōs', 'Puteolī, -ōrum (m. pl.), Putéolos (cidade)', 'acusativo plural', 'lugar para onde, sem preposição: nome de cidade'),
    ('diēs', 'diēs, -ēī (m.), dia', 'acusativo plural', 'duração: "por quanto tempo?"'),
    ('septem', 'septem, sete', 'cardinal indeclinável', 'concorda com <i>diēs</i>: "sete dias"'),
    ('Rōmam', 'Rōma, -ae (f.), Roma', 'acusativo singular', 'lugar para onde, sem preposição'),
])}
{diagrama_frase([('Secundā diē', 'ablativo · quando?'), ('vēnimus', 'verbo · "chegamos"'), ('Puteolōs', 'ac. sem prep. · para onde?')],
    'Lendo em ordem: <i>secundā diē vēnimus Puteolōs</i> = "no segundo dia chegamos a Putéolos". Ablativo de tempo, verbo de movimento, acusativo de cidade sem preposição.')}
<p>O trecho é um pequeno manual do capítulo. <i>Post mēnsēs trēs</i>: <i>post</i> com acusativo para "depois de quanto tempo", e <i>trēs</i> declinado (acusativo masculino) para concordar com <i>mēnsēs</i>. <i>In nāvī</i>: um nome comum, com a regra geral de lugar onde. <i>Secundā diē</i>: ordinal no ablativo, para "quando?" (e <i>diēs</i> no feminino, como Ravizza permite para um dia determinado). <i>Diēs septem</i>: acusativo de duração, aqui na forma clássica, com o cardinal indeclinável. E <i>Puteolōs</i>, <i>Rōmam</i>: nomes de cidade no acusativo sem preposição depois de um verbo de movimento. Compare com o capítulo 4: lá, "para a floresta" pedia <i>in silvam</i>; aqui, "para Roma" é só <i>Rōmam</i>.</p>
<p>O mesmo livro mostra as outras duas direções: <i>Paulus autem cum Athēnīs eōs exspectāret</i>, "enquanto Paulo os esperava em Atenas" (At 17,16, com <i>Athēnīs</i> no sentido de "onde?"), e <i>Post haec ēgressus ab Athēnīs, vēnit Corinthum</i>, "depois disso, saindo de Atenas, foi para Corinto" (At 18,1). Neste último, a Vulgata põe <i>ab</i> diante do nome da cidade no sentido simples de "de"; na prosa clássica, <i>ab</i> com nome de cidade indica em geral "dos arredores de" ou o ponto de onde se mede uma distância (Bennett § 229.2; Allen e Greenough § 428.a), e "de Atenas" seria só <i>Athēnīs</i>. <i>Corinthum</i> segue a regra.</p>
<h3>Resumo</h3>
<ul>
<li>Cardinais: declinam-se só <i>ūnus</i> (gen. <i>ūnīus</i>, dat. <i>ūnī</i>), <i>duo</i>, <i>trēs</i>, as centenas de 200 a 900 e <i>mīlia</i>; <i>mīlle</i> é adjetivo indeclinável, <i>mīlia</i> é substantivo com genitivo (<i>duo mīlia mīlitum</i>).</li>
<li>Ordinais: como <i>bonus</i> (<i>prīmus, secundus, tertius…</i>); distributivos (<i>singulī, bīnī</i>) = "tantos para cada um"; advérbios (<i>semel, bis, ter</i>) = "tantas vezes".</li>
<li>Algarismos: I V X L C D M; adição e subtração; IIII e VIIII também são romanos.</li>
<li>Tempo: quando? e em quanto tempo? = ablativo (<i>tertiā hōrā, tribus diēbus</i>); por quanto tempo? = acusativo (<i>trēs annōs</i>, <i>per decem diēs</i>).</li>
<li>Lugar: regra geral com preposições; cidades, ilhas pequenas, <i>domus</i>, <i>rūs</i> sem preposição: <i>Rōmam</i> (para), <i>Rōmā</i> (de), <i>Rōmae</i> (em); <i>domum, domō, domī</i>; <i>rūs, rūre, rūrī</i>; <i>Athēnīs</i> = em ou de Atenas.</li>
</ul>
<p>Nos capítulos 20 e 21, os usos do genitivo, do dativo, do acusativo e do ablativo são reunidos e completados, entre eles o genitivo que você viu com <i>mīlia</i> e com os superlativos.</p>
'''),
    ],
    erros_comuns=[
        ('Usar preposição com nome de cidade: *<i>in Rōmā habitat</i>, *<i>in Rōmam venit</i>, *<i>ex Rōmā venit</i>.', 'Com nomes de cidade e de ilhas pequenas, e com <i>domus</i> e <i>rūs</i>, o latim dispensa a preposição: <i>Rōmae habitat</i>, <i>Rōmam venit</i>, <i>Rōmā venit</i>. <i>Ad Rōmam</i> existe, mas significa "para as proximidades de Roma".'),
        ('Ler o locativo <i>Rōmae</i> como genitivo ("de Roma") ou dativo.', 'Sem um nome do qual dependa e sem verbo que peça dativo, <i>Rōmae</i> é "em Roma". "De Roma" como origem é <i>Rōmā</i>; como posse ("o povo de Roma"), aí sim é genitivo, e o contexto mostra a diferença.'),
        ('Pôr a duração no ablativo e o "quando" no acusativo: *<i>tribus annīs rēgnat</i> por "reina há/durante três anos", *<i>tertiam hōram venit</i>.', 'Na prosa clássica, a duração vai para o acusativo (<i>trēs annōs</i>), e o momento ou o prazo para o ablativo (<i>tertiā hōrā</i>; <i>tribus annīs</i> = "em três anos"). Se encontrar ablativo de duração na Vulgata, entenda-o, mas não o imite.'),
        ('Escrever *<i>duo mīlle mīlitēs</i> ou *<i>tria mīlia mīlitēs</i>.', '<i>Mīlle</i> (singular) é adjetivo indeclinável; para dois mil ou mais, use o substantivo <i>mīlia</i> com o genitivo da coisa contada: <i>duo mīlia mīlitum</i>, <i>tria mīlia hominum</i>. E <i>tria</i>, não <i>trēs</i>, porque <i>mīlia</i> é neutro.'),
        ('Não declinar <i>duo</i> e <i>trēs</i>, ou declinar os indeclináveis: *<i>cum duo puellīs</i>, *<i>quattuōrum</i>.', '<i>Duo</i> e <i>trēs</i> se declinam (<i>cum duābus puellīs</i>, <i>cum tribus puerīs</i>); de <i>quattuor</i> a <i>centum</i>, os cardinais não se declinam (<i>quattuor puellārum</i>).'),
        ('Usar o cardinal para indicar a ordem ou a hora: *<i>annō mīlle quīngentī</i>, *<i>tribus hōrīs</i> por "na terceira hora".', 'Para "o ano 1500", "a terceira hora", "o capítulo décimo", o latim usa o <b>ordinal</b>, declinado: <i>annō mīllēsimō quīngentēsimō</i>, <i>tertiā hōrā</i>, <i>capite decimō</i>. <i>Tribus hōrīs</i> significa "em três horas".'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Tempo e lugar na mesma frase',
            'Analise e traduza: <i lang="la">Tertiō annō Mārcus Athēnīs Rōmam venit et ibi decem annōs habitat.</i> Vocabulário: <i>ibi</i>, ali; <i>habitō, -āre</i>, morar.', [
            ('Que caso é <i>tertiō annō</i>, e a que pergunta responde?', 'Ablativo singular masculino (ordinal + <i>annus</i>), sem preposição: responde a "quando?": "no terceiro ano".'),
            ('<i>Athēnīs</i> é "em Atenas" ou "de Atenas"?', 'A forma serve para os dois (locativo e ablativo coincidem nos plurais). O verbo é de movimento (<i>venit</i>) e há um <i>Rōmam</i> de destino: aqui é ponto de partida, "de Atenas".'),
            ('E <i>Rōmam</i>?', 'Acusativo sem preposição de um nome de cidade, com verbo de movimento: "para Roma".'),
            ('Que caso é <i>decem annōs</i>?', '<i>Annōs</i> é acusativo plural; <i>decem</i> é indeclinável. Acusativo de duração: "durante dez anos".'),
            ('Monte a tradução.', '"No terceiro ano, Marcos vem de Atenas para Roma e ali mora dez anos." (Em português corrente, com tempos do passado: "No terceiro ano, Marcos foi de Atenas para Roma e morou ali dez anos.")'),
        ]),
        pratica_guiada('Prática guiada 2 · Numerais que concordam',
            'Traduza para o latim: "Duas meninas e três meninos caminham com mil soldados; dois mil soldados ficam em casa." Vocabulário: <i>ambulō, -āre</i>, caminhar; <i>maneō, -ēre</i>, ficar.', [
            ('Como fica "duas meninas"?', '<i>duae puellae</i>: nominativo plural feminino de <i>duo</i>, porque é sujeito.'),
            ('E "três meninos"?', '<i>trēs puerī</i>: <i>trēs</i> serve ao masculino e ao feminino no nominativo.'),
            ('"Com mil soldados"?', '<i>cum mīlle mīlitibus</i>: <i>mīlle</i> não se declina; <i>mīlitibus</i> está no ablativo pedido por <i>cum</i>.'),
            ('"Dois mil soldados", sujeito?', '<i>duo mīlia mīlitum</i>: <i>mīlia</i> é o sujeito (neutro plural, nominativo), <i>duo</i> concorda com ele no neutro, e <i>mīlitum</i> vai para o genitivo. O verbo fica no plural.'),
            ('"Em casa"?', '<i>domī</i>, locativo, sem preposição.'),
            ('Monte a frase.', '<i>Duae puellae et trēs puerī cum mīlle mīlitibus ambulant; duo mīlia mīlitum domī manent.</i>'),
        ], 'Conclusão: antes de escrever um numeral, pergunte se ele se declina e, no caso de "mil", se é <i>mīlle</i> (adjetivo) ou <i>mīlia</i> (substantivo com genitivo).'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Algarismos romanos', 'Dê o valor e o cardinal latino (nominativo).', [
            ('<i>XVII</i>', '17: <i>septendecim</i>. X + V + II.'),
            ('<i>XXVIII</i>', '28: <i>duodētrīgintā</i> (ou <i>vīgintī octō</i>, <i>octō et vīgintī</i>). Os números terminados em 8 e 9 costumam se dizer por subtração.'),
            ('<i>XLIV</i>', '44: <i>quadrāgintā quattuor</i> (ou <i>quattuor et quadrāgintā</i>). XL = 40 (L − X), IV = 4.'),
            ('<i>LXXXX</i>', '90: <i>nōnāgintā</i>. Forma aditiva antiga, equivalente a XC.'),
            ('<i>CCCLX</i>', '360: <i>trecentī sexāgintā</i>.'),
            ('<i>MDCCC</i>', '1800: <i>mīlle octingentī</i>.'),
        ]),
        exercicio('Exercício 2 · Faça concordar o numeral', 'Complete com a forma correta do numeral entre parênteses e explique.', [
            ('<i>cum ___ fīliābus</i> (duo)', '<i>duābus</i>: ablativo feminino, depois de <i>cum</i>.'),
            ('<i>___ puerōrum</i> (trēs)', '<i>trium</i>: genitivo plural, igual nos três gêneros.'),
            ('<i>___ templa</i> (trēs), como objeto', '<i>tria</i>: acusativo plural neutro.'),
            ('<i>nōmen ___ rēgis</i> (ūnus)', '<i>ūnīus</i>: genitivo singular, "de um só rei"; o genitivo de <i>ūnus</i> é <i>ūnīus</i> em todos os gêneros.'),
            ('<i>quīnque ___ hominum</i> (mīlle)', '<i>mīlia</i>: para "cinco mil", o plural substantivo, com <i>hominum</i> no genitivo.'),
            ('<i>cum ___ equitibus</i> (mīlle)', '<i>mīlle</i>: no singular é adjetivo indeclinável; <i>equitibus</i> leva o caso.'),
        ]),
        exercicio('Exercício 3 · Que pergunta? Que caso?', 'Diga a que pergunta responde a expressão destacada (quando?, em quanto tempo?, por quanto tempo?) e traduza.', [
            ('<i>Puer <b>tōtam noctem</b> dormit.</i>', 'Por quanto tempo? Acusativo de duração: "O menino dorme a noite inteira."'),
            ('<i>Nūntius <b>quārtā hōrā</b> venit.</i>', 'Quando? Ablativo com ordinal: "O mensageiro chega na quarta hora."'),
            ('<i>Mīlitēs <b>paucīs diēbus</b> oppidum capiunt.</i>', 'Em quanto tempo? Ablativo: "Os soldados tomam a cidade em poucos dias."'),
            ('<i>Rēx <b>trīgintā annōs</b> rēgnat.</i>', 'Por quanto tempo? Acusativo: "O rei reina trinta anos."'),
            ('<i><b>Post trēs diēs</b> nautae redeunt.</i> (<i>redeunt</i>, voltam)', 'Depois de quanto tempo? <i>Post</i> + acusativo: "Três dias depois, os marinheiros voltam."'),
            ('<i><b>In bellō</b> fortēs sunt, <b>in pāce</b> iūstī.</i>', 'Quando, com nomes que não indicam tempo por si: <i>in</i> + ablativo. "Na guerra são valentes; na paz, justos."'),
        ]),
        exercicio('Exercício 4 · Onde, para onde, de onde', 'Escreva a expressão latina pedida e explique se leva preposição.', [
            ('em Corinto (<i>Corinthus, -ī</i>, f.)', '<i>Corinthī</i>: locativo de um singular da 2ª declinação, sem preposição.'),
            ('para Atenas (<i>Athēnae, -ārum</i>)', '<i>Athēnās</i>: acusativo sem preposição.'),
            ('de casa', '<i>domō</i>: ablativo sem preposição.'),
            ('no campo', '<i>rūrī</i>: locativo de <i>rūs</i>.'),
            ('para a Itália', '<i>in Italiam</i>: nome de país, regra geral com preposição.'),
            ('em Cartago (<i>Carthāgō, -inis</i>)', '<i>Carthāgine</i> (ou <i>Carthāginī</i>): na 3ª declinação, o locativo tem forma de ablativo (ou em <i>-ī</i>).'),
            ('para a cidade', '<i>in urbem</i> (ou <i>ad urbem</i>): <i>urbs</i> é nome comum e sempre pede preposição.'),
            ('perto de Roma, nas proximidades', '<i>ad Rōmam</i>: com nome de cidade, <i>ad</i> indica a vizinhança, não a entrada na cidade.'),
        ]),
        exercicio('Exercício 5 · Leia e traduza', 'Traduza, indicando cada expressão de número, tempo e lugar. Vocabulário: <i>Brundisium, -ī</i> (n.), Brundísio (cidade); <i>proficīscitur</i>, parte; <i>manet</i>, fica.', [
            ('<i>Cicerō Rōmā Brundisium proficīscitur.</i>', '"Cícero parte de Roma para Brundísio." <i>Rōmā</i>, ablativo de origem; <i>Brundisium</i>, acusativo de direção; ambos sem preposição (nomes de cidade).'),
            ('<i>Brundisiī decem diēs manet.</i>', '"Fica em Brundísio dez dias." <i>Brundisiī</i>, locativo (singular da 2ª); <i>decem diēs</i>, acusativo de duração.'),
            ('<i>Tertiō diē nāvem cōnscendit et in Graeciam nāvigat.</i> (<i>cōnscendit</i>, embarca em)', '"No terceiro dia embarca num navio e navega para a Grécia." <i>Tertiō diē</i>, ablativo de tempo com ordinal; <i>in Graeciam</i>, país, com preposição.'),
            ('<i>Athēnīs duo mīlia cīvium eum exspectant.</i> (<i>eum</i>, o; <i>exspectant</i>, esperam)', '"Em Atenas, dois mil cidadãos o esperam." <i>Athēnīs</i>, sem verbo de movimento: "em Atenas"; <i>duo mīlia cīvium</i>, sujeito, com genitivo.'),
        ]),
        exercicio('Exercício 6 · Retroversão', 'Passe para o latim. Vocabulário: <i>maneō, -ēre</i>, ficar; <i>habitō, -āre</i>, morar; <i>veniō, -īre</i>, vir; <i>hōra, -ae</i>, hora.', [
            ('O poeta mora em Roma há muitos anos (= mora muitos anos em Roma).', '<i>Poēta multōs annōs Rōmae habitat.</i> Acusativo de duração; locativo <i>Rōmae</i>.'),
            ('Na primeira hora as meninas vêm para casa.', '<i>Prīmā hōrā puellae domum veniunt.</i> Ablativo com ordinal; <i>domum</i> sem preposição.'),
            ('Os marinheiros navegam de Corinto para Atenas em três dias.', '<i>Nautae tribus diēbus Corinthō Athēnās nāvigant.</i> <i>Tribus diēbus</i>, prazo (ablativo); cidades sem preposição.'),
            ('Três mil soldados ficam no campo.', '<i>Tria mīlia mīlitum rūrī manent.</i> <i>Mīlia</i> neutro com genitivo; <i>rūrī</i>, locativo.'),
        ]),
    ],
    leituras=['eutropius-breviarium-ab-urbe-condita', 'lhomond-urbis-romae-viri-illustres-selecoes', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'caesar-commentarii-de-bello-gallico-selecoes', 'd-ooge-latin-for-beginners', 'bennett-new-latin-grammar'],
    leituras_nota='O primeiro livro do Breviarium de Eutrópio é o melhor exercício para este capítulo: datas, anos de reinado com ordinais (I, 3–6), distâncias em milhas e números escritos com algarismos romanos (I, 7 e 16). O De viris illustribus de Lhomond conta a mesma história em latim mais simples. Na Vulgata, leia Atos 27–28, a viagem de Paulo a Roma, procurando os nomes de cidade sem preposição. No início da Guerra da Gália (I, 1), veja os numerais e as expressões de lugar. D\'Ooge traz exercícios graduados sobre numerais e sobre expressões de tempo e de lugar; Bennett (§§ 78–81, 181–182, 228–232) serve para consulta.',
)
