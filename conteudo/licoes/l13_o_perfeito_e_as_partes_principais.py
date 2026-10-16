from conteudo.util import (tabela, tabela_conjugacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Texto original do capítulo (para o exercício 5): reconta no passado a travessia do capítulo 8, com o vocabulário
# dos capítulos 4–8 e 12; as palavras novas vão glosadas no enunciado. Perfeitos conferidos em Bennett/Lewis & Short.
_TEXTO_LEITURA = ('<sup>1</sup> Herī Titus et Flāvia cum avō ad īnsulam nāvigāvērunt. '
                  '<sup>2</sup> Prīmō caelum serēnum erat, et puerī cantābant. '
                  '<sup>3</sup> Subitō ventus magnus vēnit, et aqua in nāviculam intrāvit. '
                  '<sup>4</sup> Flāvia timuit, sed avus rēmōs tenuit et Titum vocāvit. '
                  '<sup>5</sup> Tandem avus nāviculam ad īnsulam dūxit. '
                  '<sup>6</sup> Avia in ōrā exspectābat; cēnam bonam iam parāverat. '
                  '<sup>7</sup> Post cēnam avus fābulās nārrāvit, et puerī mox dormīvērunt.')

LICAO = dict(
    slug='13-o-perfeito-e-as-partes-principais', titulo='O perfeito e os tempos do perfectum; as partes principais do verbo', titulo_latim='Dē perfectō', tempo='80 min',
    resumo='O segundo tema do verbo: o perfectum, que apresenta a ação concluída. As quatro partes principais e o que cada uma fornece; as terminações do perfeito (-ī, -istī, -it, -imus, -istis, -ērunt/-ēre); os cinco modos de formar o tema do perfeito e por que, na 3ª conjugação, ele se decora; fuī; o mais-que-perfeito e o futuro perfeito; perfeito × imperfeito ("fez" × "fazia"); e como chegar de rēxit a regō no dicionário.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['perfectum', 'infectum × perfectum', 'aspecto: ação concluída', 'partes principais do verbo', 'tema do perfeito', 'perfeito do indicativo ativo',
             'terminações do perfeito (-ī, -istī, -it, -imus, -istis, -ērunt/-ēre)', 'perfeito em -vī e -uī', 'perfeito em -sī', 'perfeito com reduplicação',
             'perfeito com alongamento da vogal', 'perfeito sem mudança do tema', 'fuī (perfeito de esse)', 'formas sincopadas (amāstī, amārunt)',
             'mais-que-perfeito do indicativo', 'futuro perfeito do indicativo', 'perfeito × imperfeito', 'perfeito histórico e perfeito definido',
             'do perfeito ao verbete', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 12: o infectum (presente, imperfeito em -bam e futuro em -bō/-bis ou -am/-ēs), eram e erō. Usam-se também as terminações pessoais e os verbos-modelo do capítulo 6 (amāre, monēre, regere, audīre, capere, esse) e o método de consulta ao dicionário do capítulo 7.',
                       licoes=['12-o-imperfeito-e-o-futuro']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 96 (terminações pessoais, com as próprias do perfeito: -ī, -stī, -stis, -ērunt), § 97 (os três temas do verbo e os tempos que saem de cada um), § 99 e nota 28 (partes principais), § 100 (sum, fuī; perfeito, mais-que-perfeito e futuro perfeito), §§ 101, 103, 105, 107, 110 (amō, moneō, regō, audiō, capiō: partes principais e tempos do perfeito), § 116.1 (formas sincopadas: amāstī, amārunt, audīstī), § 117.3 (n acrescentado só ao tema do presente), § 118 (formação do tema do perfeito: -v-, -u-, -s-, reduplicação, alongamento, sem mudança), §§ 120–122 (listas de verbos com as partes principais), § 127 (dō, dedī), § 257 (tempo e tipo de ação; a tabela dos seis tempos), § 260 (imperfeito, tempo da descrição), § 262 (perfeito presente e perfeito histórico, tempo da narração), § 263 (mais-que-perfeito), § 264 (futuro perfeito)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§§ 160–161 (ação contínua × concluída; perfeito definido e histórico), § 163.a e nota 3 (terminações especiais do perfeito; -ērunt e -ēre), § 169 (formação do perfeito, do mais-que-perfeito e do futuro perfeito; a influência de eram e erō), § 170 (sum), §§ 172–173 (partes principais; a quarta forma em -um), § 177 (formação do tema do perfeito), § 179.a.2, c.2 e d (o perfeito nas quatro conjugações; na 3ª, "não se forma do tema do presente"), § 181 (formas contraídas), § 470 e nota (imperfeito: rēx erat × rēx fuit), §§ 473–474 (perfeito; Habuit, nōn habet), §§ 477–478 (mais-que-perfeito e futuro perfeito), § 605 (quantidade dos perfeitos: vīdī, vēnī, fūgī; dĕdī; dĭdĭcī, cŭcurrī)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 105 (os seis tempos; o perfeito latino faz o papel de dois tempos, "I loved" e "I have loved"), § 112 (as formas que é preciso conhecer: amo, amare, amavi, amatum etc.), § 113 (formas contraídas; -ere por -erunt, "often written", sem contração), § 150 (formação do perfeito: reduplicação, vogal alongada, tema sem mudança, -si, -vi, -ui)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 80 (os seis tempos; o pretérito perfeito latino corresponde ao pretérito perfeito simples e composto do português), n. 84 (os quatro "tempos primitivos" que o dicionário fornece), n. 86 (desinências do perfeito em todas as conjugações, -ērunt ou -ēre; tempos formados do perfeito), n. 104 (formas sincopadas; -ēre por -ērunt, sem síncope)', tipo='dominio_publico'),
        referencia('Lewis & Short, A Latin Dictionary (Perseus)', 'C. T. Lewis e C. Short', url='https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.04.0059', nota='partes principais conferidas nos verbetes de amo, moneo, rego, audio, venio, video, vinco, scribo, respondeo, duco, mitto, vivo, maneo, sedeo, habeo, teneo, timeo, doceo, deleo, curro, disco, defendo, facio, fugio, ago, emo, pono, peto, laudo, specto, narro, voco, porto, canto, navigo, exspecto, dormio, scio', tipo='dominio_publico'),
        referencia('De vita Caesarum, Dīvus Iūlius 37', 'Suetônio', url='https://www.thelatinlibrary.com/suetonius/suet.caesar.html', nota='VENI · VIDI · VICI, o letreiro levado no triunfo do Ponto; texto conferido na The Latin Library e no Perseus (Suet. Iul. 37.2); Plutarco, César 50.3–4, conta que César escreveu as três palavras a um amigo em Roma', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Jo 19,22 e 1,18', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', nota='frases autênticas da seção 6 e do exercício 5 (texto conferido na Wikisource latina, "Vulgata Clementina/Evangelium Secundum Joannem")', tipo='dominio_publico'),
    ],
    objetivos=[
        'Distinguir os tempos do <i>infectum</i> e do <i>perfectum</i> e traduzir cada um com o tempo português adequado ("fazia", "fez", "tinha feito", "terá feito").',
        'Ler as quatro partes principais de um verbo (<i>amō, amāre, amāvī, amātum</i>), dizer o que cada uma fornece e recitá-las para os verbos-modelo e para <i>sum, esse, fuī</i>.',
        'Conjugar o perfeito, o mais-que-perfeito e o futuro perfeito de qualquer verbo a partir da 3ª parte principal.',
        'Reconhecer os cinco modos de formar o tema do perfeito e voltar de uma forma como <i>rēxit</i> ou <i>cucurrērunt</i> à entrada de dicionário.',
        'Analisar palavra a palavra frases autênticas com perfeitos (Suetônio; Vulgata, Jo 19,22).',
    ],
    secoes=[
        ('Infectum e perfectum: dois temas, dois aspectos', f'''
<p>No capítulo 12 você viu que o indicativo latino tem seis tempos, divididos em dois grupos de três, e estudou o primeiro grupo, o do <b><i>infectum</i></b>: presente, imperfeito e futuro, todos feitos com o tema do presente (<i>amā-</i>, <i>monē-</i>, <i>rege-</i>, <i>audī-</i>). Agora vem o segundo grupo, o do <b><i>perfectum</i></b> ("acabado", "completo"): o <b>perfeito</b>, o <b>mais-que-perfeito</b> e o <b>futuro perfeito</b>. Os três apresentam a ação como <b>concluída</b> e se constroem sobre um segundo tema, o <b>tema do perfeito</b> (Bennett § 97 lista os tempos que saem de cada tema; Allen &amp; Greenough falam em "sistema do perfeito", § 169, e opõem a ação "contínua" à ação "concluída", § 160).</p>
<p>A ideia é a mesma que distingue, em português, "eu fazia" de "eu fiz". As duas formas falam do passado; o que muda é o modo de ver a ação. "Fazia" mostra a ação em andamento ou repetida, sem dizer se terminou; "fiz" mostra a ação como um fato fechado. Essa diferença entre ação em curso e ação concluída chama-se <b>aspecto</b>, e é ela, mais do que a época, que separa o <i>infectum</i> do <i>perfectum</i>. Bennett resume tudo numa tabela (§ 257), que aqui aparece com o verbo <i>regō</i>:</p>
{tabela(['Época', 'Infectum: ação em curso', 'Perfectum: ação concluída'], [
    ['Presente', '<i>regō</i>, governo, estou governando', '<i>rēxī</i>, já governei (o fato está consumado agora)'],
    ['Passado', '<i>regēbam</i>, governava, estava governando', '<i>rēxeram</i>, tinha governado'],
    ['Futuro', '<i>regam</i>, governarei, estarei governando', '<i>rēxerō</i>, terei governado'],
], 'Os seis tempos do indicativo ativo: dois temas, três épocas')}
<p>Repare na primeira linha. O perfeito <i>rēxī</i> aparece na coluna do presente porque, num dos seus usos, ele diz que a ação está concluída <b>agora</b>: "já governei", "tenho isto feito". Mas o mesmo <i>rēxī</i> também conta um fato passado, "governei", como o pretérito perfeito do português. Kennedy explica a razão (§ 105, nota): o latim não tem formas separadas para esses dois valores, e o perfeito "faz o papel de dois tempos". Allen &amp; Greenough chamam o primeiro uso de perfeito <b>definido</b> e o segundo de perfeito <b>histórico</b> (§ 161); na prática, o português traduz os dois por "governei", acrescentando "já" quando o contexto pede o resultado presente.</p>
{observacao('"Governei" ou "tenho governado"?', 'Ravizza diz que o perfeito latino corresponde ao pretérito perfeito simples e ao composto do português, "amei" e "tenho amado" (n. 80). Cuidado com o segundo: no português do Brasil, "tenho amado", "tenho lido" quase sempre indica ação repetida que continua até hoje ("tenho lido muito ultimamente"), e não uma ação concluída. Para o perfeito latino, prefira "amei", "li", "já li". Guarde "tenho lido" para quando o contexto realmente falar de repetição.')}
<p>O tema do perfeito não se tira do infinitivo, como o do presente: ele vem pronto na terceira forma do verbete, <i>amāvī</i>, <i>rēxī</i>, <i>fuī</i>. Por isso o capítulo começa pelas partes principais.</p>
'''),
        ('As quatro partes principais', f'''
<p>Desde o capítulo 6 você lê verbetes como <i>amō, amāre</i>, e no capítulo 7 viu que eles continuam com mais duas formas: <i>amō, amāre, amāvī, amātum</i>. Essas quatro formas são as <b>partes principais</b> do verbo. Bennett as chama assim "porque contêm os diferentes temas dos quais se pode derivar a conjugação inteira" (§ 99); Allen &amp; Greenough dizem que elas mostram "os três temas que determinam a conjugação" (§ 172), e Ravizza, que as chama de "tempos primitivos", lembra que são justamente as formas que o dicionário fornece (n. 84). Cada uma tem uma função:</p>
{tabela(['Parte', 'Forma', 'O que fornece', 'Exemplo'], [
    ['1ª', 'presente do indicativo, 1ª pessoa do singular', 'a forma pela qual o verbo é procurado no dicionário', '<i>amō</i>, <i>regō</i>'],
    ['2ª', 'infinitivo presente', 'a conjugação e o tema do presente (<i>infectum</i>): presente, imperfeito, futuro', '<i>amā-re</i> → <i>amā-</i>; <i>rege-re</i> → <i>rege-</i>'],
    ['3ª', 'perfeito do indicativo, 1ª pessoa do singular', 'o tema do perfeito (<i>perfectum</i>): tire o <i>-ī</i>', '<i>amāv-ī</i> → <i>amāv-</i>; <i>rēx-ī</i> → <i>rēx-</i>'],
    ['4ª', 'supino ou particípio perfeito', 'o terceiro tema, usado na passiva do <i>perfectum</i> e nos particípios (capítulos 24 e 29)', '<i>amāt-um</i>; <i>rēct-um</i>'],
], 'As partes principais e o que cada uma fornece', latim_cols=(3,))}
<p>A quarta parte é a única que você ainda não vai usar. Ela fornece o tema de formas que só aparecem mais adiante, a voz passiva do <i>perfectum</i> (capítulo 24) e os particípios (capítulo 29). Por ora, basta <b>decorá-la junto com as outras</b>, para não ter de voltar a cada verbo quando ela for necessária. As gramáticas não citam essa forma do mesmo jeito: Allen &amp; Greenough dão o neutro em <i>-um</i>, <i>amātum</i> (§ 172), como a maioria dos dicionários; Bennett dá o particípio masculino, <i>amātus</i> (§ 99); e, quando o verbo não tem particípio perfeito, os dois põem em seu lugar o particípio futuro, como em <i>sum, esse, fuī, futūrus</i> (Bennett § 99, nota 28; § 100). Alguns verbos não têm quarta forma nenhuma, e o dicionário a omite: <i>timeō, timēre, timuī</i>. Este livro cita a forma em <i>-um</i>.</p>
{tabela(['Conjugação', '1ª parte', '2ª parte', '3ª parte', '4ª parte', 'Significado'], [
    ['1ª', 'amō', 'amāre', 'amā<b>v</b>ī', 'amātum', 'amar'],
    ['2ª', 'moneō', 'monēre', 'mon<b>u</b>ī', 'monitum', 'advertir, aconselhar'],
    ['3ª', 'regō', 'regere', 'rē<b>x</b>ī', 'rēctum', 'reger, governar'],
    ['4ª', 'audiō', 'audīre', 'audī<b>v</b>ī', 'audītum', 'ouvir'],
    ['3ª em -iō', 'capiō', 'capere', 'c<b>ē</b>pī', 'captum', 'pegar, tomar'],
    ['irregular', 'sum', 'esse', '<b>fu</b>ī', 'futūrus', 'ser, estar'],
], 'As partes principais dos verbos-modelo (Bennett §§ 100–110; A&G § 173)', latim_cols=(1, 2, 3, 4))}
<p>Recite cada linha em voz alta, como uma palavra só: <i>amō, amāre, amāvī, amātum</i>. É assim que os verbos se aprendem, e é assim que você vai encontrá-los nas listas de vocabulário, por extenso (<i>videō, vidēre, vīdī, vīsum</i>, na lista DCC) ou abreviados (o Lewis &amp; Short escreve <i>rĕgo, xi, ctum, 3</i> e <i>dūco, xi, ctum, 3</i>, isto é, <i>rēxī, rēctum</i> e <i>dūxī, ductum</i>, da 3ª conjugação; o capítulo 7 mostrou como ler essas abreviaturas).</p>
'''),
        ('O perfeito do indicativo', f'''
<p>O perfeito tem uma vantagem enorme sobre o presente: <b>as terminações são as mesmas em todas as conjugações</b> (Ravizza n. 86; A&amp;G § 169.a). Uma vez conhecido o tema, <i>amāv-</i>, <i>rēx-</i>, <i>cēp-</i>, <i>fu-</i>, basta acrescentar:</p>
{tabela(['Pessoa', 'Terminação', 'Compare com o presente', 'Exemplo', 'Português'], [
    ['1ª sing.', '<b>-ī</b>', '-ō / -m', 'rēx<b>ī</b>', 'governei'],
    ['2ª sing.', '<b>-istī</b>', '-s', 'rēx<b>istī</b>', 'governaste, você governou'],
    ['3ª sing.', '<b>-it</b>', '-t', 'rēx<b>it</b>', 'governou'],
    ['1ª pl.', '<b>-imus</b>', '-mus', 'rēx<b>imus</b>', 'governamos'],
    ['2ª pl.', '<b>-istis</b>', '-tis', 'rēx<b>istis</b>', 'governastes, vocês governaram'],
    ['3ª pl.', '<b>-ērunt</b> ou <b>-ēre</b>', '-nt', 'rēx<b>ērunt</b>, rēx<b>ēre</b>', 'governaram'],
], 'As terminações do perfeito do indicativo ativo', latim_cols=(1, 2, 3))}
<p>Três dessas terminações são exclusivas do perfeito, e por isso Bennett as lista à parte entre as terminações pessoais (§ 96): <i>-ī</i> na 1ª pessoa, <i>-stī</i> na 2ª do singular e <i>-stis</i> na 2ª do plural, além de <i>-ērunt</i> (A&amp;G § 163.a). Quem as reconhece sabe, sem olhar mais nada, que está diante de um perfeito: uma forma em <i>-istī</i> ou <i>-istis</i> não pode ser outro tempo. Já <i>-it</i> e <i>-imus</i> são enganosas, porque coincidem com o presente da 3ª conjugação (<i>regit, regimus</i>); aí quem decide é o tema, <i>rēx-</i> e não <i>reg-</i>.</p>
<p>Agora os verbos-modelo e <i>esse</i>. Leia as colunas de cima para baixo e repare que, depois do tema, tudo se repete:</p>
{tabela(['Pessoa', '1ª · amō', '2ª · moneō', '3ª · regō', '4ª · audiō', '3ª em -iō · capiō', 'sum'], [
    ['1ª sing.', 'amāv<b>ī</b>', 'monu<b>ī</b>', 'rēx<b>ī</b>', 'audīv<b>ī</b>', 'cēp<b>ī</b>', 'fu<b>ī</b>'],
    ['2ª sing.', 'amāv<b>istī</b>', 'monu<b>istī</b>', 'rēx<b>istī</b>', 'audīv<b>istī</b>', 'cēp<b>istī</b>', 'fu<b>istī</b>'],
    ['3ª sing.', 'amāv<b>it</b>', 'monu<b>it</b>', 'rēx<b>it</b>', 'audīv<b>it</b>', 'cēp<b>it</b>', 'fu<b>it</b>'],
    ['1ª pl.', 'amāv<b>imus</b>', 'monu<b>imus</b>', 'rēx<b>imus</b>', 'audīv<b>imus</b>', 'cēp<b>imus</b>', 'fu<b>imus</b>'],
    ['2ª pl.', 'amāv<b>istis</b>', 'monu<b>istis</b>', 'rēx<b>istis</b>', 'audīv<b>istis</b>', 'cēp<b>istis</b>', 'fu<b>istis</b>'],
    ['3ª pl.', 'amāv<b>ērunt</b>', 'monu<b>ērunt</b>', 'rēx<b>ērunt</b>', 'audīv<b>ērunt</b>', 'cēp<b>ērunt</b>', 'fu<b>ērunt</b>'],
], 'O perfeito do indicativo ativo (Bennett §§ 100, 101, 103, 105, 107, 110)', latim_cols=(1, 2, 3, 4, 5, 6))}
<p>O perfeito de <i>esse</i> é <i>fuī</i>, de outra raiz (a mesma do particípio <i>futūrus</i>), e conjuga-se com as terminações de sempre: "fui, estive" (Bennett § 100; A&amp;G § 170). O português aproveitou essa raiz: "fui, foste, foi" vêm dela, segundo a explicação corrente da gramática histórica.</p>
<h3>A variante -ēre</h3>
<p>Na 3ª pessoa do plural, ao lado de <i>-ērunt</i>, existe <i>-ēre</i>, com o mesmo valor: <i>amāvēre</i> = <i>amāvērunt</i>, <i>fuēre</i> = <i>fuērunt</i>, <i>rēxēre</i> = <i>rēxērunt</i>. Bennett a registra em todos os paradigmas (§§ 100–110), e Kennedy observa que ela é escrita com frequência (§ 113). Cuidado para não confundir essa forma com um infinitivo. O tema resolve quase sempre (<i>rēxēre</i> tem o tema <i>rēx-</i>, o infinitivo é <i>regere</i>), mas há casos em que só a quantidade separa as duas: <b><i>vīdēre</i></b>, "viram", e <b><i>vidēre</i></b>, "ver". Num texto sem macrons, ambos se escrevem <i>videre</i>; um sujeito no plural e a falta de um verbo que peça infinitivo indicam o perfeito.</p>
<h3>Formas sincopadas</h3>
<p>Nos perfeitos em <i>-āvī</i>, <i>-ēvī</i> e <i>-īvī</i>, o latim muitas vezes "engole" o <i>v</i> e a vogal seguinte antes de <i>r</i> ou <i>s</i> (Bennett § 116.1; A&amp;G § 181; Kennedy § 113; Ravizza n. 104). Você vai encontrar <i>amāstī</i> por <i>amāvistī</i>, <i>amārunt</i> por <i>amāvērunt</i>, <i>audīstī</i> por <i>audīvistī</i>, <i>dēlērunt</i> por <i>dēlēvērunt</i>; nos perfeitos em <i>-īvī</i> é comum também a simples queda do <i>v</i>: <i>audiērunt</i> por <i>audīvērunt</i>. Basta reconhecê-las: ao ver <i>amārunt</i>, pense "falta um <i>-vē-</i>", e você tem <i>amāvērunt</i>. A 1ª pessoa (<i>amāvī</i>) nunca se contrai (A&amp;G § 181.a, nota), e a variante em <i>-ēre</i> também não: não se diz "amāre" por <i>amāvēre</i>, observa Ravizza (n. 104.d), e de fato essa forma se confundiria com o infinitivo.</p>
{exemplos([('Agricola equōs in agrum dūx<b>it</b>.', 'O agricultor levou os cavalos para o campo. (<i>dūcō, dūcere, dūxī, ductum</i>)'),
           ('Puellae fābulam nārrāv<b>ērunt</b>.', 'As meninas contaram uma história.'),
           ('Epistulam scrīps<b>ī</b>.', 'Escrevi a carta. / Já escrevi a carta. (perfeito definido, conforme o contexto)'),
           ('Ubi fu<b>istis</b>? In īnsulā fu<b>imus</b>.', 'Onde vocês estiveram? Estivemos na ilha. (<i>ubi</i>, onde)')])}
'''),
        ('Como se forma o tema do perfeito', f'''
<p>Se as terminações do perfeito são sempre as mesmas, toda a dificuldade está no tema. Bennett (§ 118), Allen &amp; Greenough (§ 177) e Kennedy (§ 150) descrevem os mesmos processos, que podem ser agrupados em cinco tipos. Conhecê-los não serve para "fabricar" perfeitos, e sim para <b>reconhecê-los</b> num texto e, a partir deles, achar o verbo no dicionário:</p>
{tabela(['Tipo', 'O que acontece', 'Exemplos (presente → perfeito)'], [
    ['1. <b>-v-</b> ou <b>-u-</b>', 'acrescenta-se <i>v</i> ao tema vocálico, ou <i>u</i> à raiz', 'amō → amā<b>v</b>ī · audiō → audī<b>v</b>ī · dēleō → dēlē<b>v</b>ī · moneō → mon<b>u</b>ī · habeō → hab<b>u</b>ī · timeō → tim<b>u</b>ī'],
    ['2. <b>-s-</b>', 'acrescenta-se <i>s</i> à raiz; <i>c</i> ou <i>g</i> + <i>s</i> se escrevem <i>x</i>, <i>b</i> + <i>s</i> vira <i>ps</i>, e o <i>t</i> ou <i>d</i> cai', 'regō → rē<b>x</b>ī (<i>reg-s-</i>) · dūcō → dū<b>x</b>ī · scrībō → scrī<b>ps</b>ī · maneō → mān<b>s</b>ī · mittō → mī<b>s</b>ī'],
    ['3. <b>reduplicação</b>', 'repete-se a consoante inicial, com uma vogal, antes da raiz', 'dō → <b>de</b>dī · currō → <b>cu</b>currī · discō → <b>di</b>dicī · cadō → <b>ce</b>cidī · stō → <b>ste</b>tī'],
    ['4. <b>alongamento</b>', 'a vogal breve da raiz fica longa; o <i>a</i> breve vira <i>ē</i>', 'veniō → v<b>ē</b>nī · legō → l<b>ē</b>gī · videō → v<b>ī</b>dī · faciō → f<b>ē</b>cī · capiō → c<b>ē</b>pī · agō → <b>ē</b>gī · fugiō → f<b>ū</b>gī · vincō → v<b>ī</b>cī'],
    ['5. <b>sem mudança</b>', 'o perfeito usa o próprio tema do presente', 'dēfendō → dēfend<b>ī</b> · vertō → vert<b>ī</b>'],
], 'Os cinco modos de formar o tema do perfeito (Bennett § 118; A&G § 177; Kennedy § 150)', latim_cols=(2,))}
<p>Alguns detalhes que ajudam a reconhecer as formas. No tipo 2, a regra de Bennett (§ 118.3a) explica as grafias: o <i>g</i> de <i>reg-</i> e o <i>c</i> de <i>dūc-</i> se unem ao <i>s</i> e formam <i>x</i> (<i>rēxī, dūxī</i>), o <i>b</i> de <i>scrīb-</i> vira <i>p</i> (<i>scrīpsī</i>), e o <i>t</i> de <i>mitt-</i> desaparece (<i>mīsī</i>, com a vogal alongada, como nota Kennedy no § 150). No tipo 3, as vogais da reduplicação são breves: <i>dĕdī</i>, <i>cŭcurrī</i>, <i>dĭdĭcī</i> (A&amp;G § 605). No tipo 4, a regra de A&amp;G (§ 605) é que os perfeitos de duas sílabas têm a primeira longa (<i>vīdī, vēnī, fūgī</i>), com poucas exceções, como <i>dĕdī</i> e <i>stĕtī</i>. Em <i>vīcī</i>, de <i>vincō</i>, o <i>n</i> some porque pertencia só ao tema do presente (Bennett § 117.3 descreve esse <i>n</i> acrescentado ao presente). No tipo 5, o perfeito é igual ao presente em quase todas as pessoas: <i>dēfendit</i> é "defende" ou "defendeu", <i>dēfendimus</i>, "defendemos" nos dois tempos; só o contexto, ou a 3ª pessoa do plural (<i>dēfendunt</i> × <i>dēfendērunt</i>), decide.</p>
<h3>Por que o perfeito da 3ª conjugação se decora</h3>
<p>Nas outras conjugações há uma forma dominante. A 1ª faz quase sempre <i>-āvī</i>, <i>-ātum</i> (A&amp;G § 179.a.2), com poucas exceções, como <i>dō, dare, dedī, datum</i> (Bennett § 127) e <i>stō, stāre, stetī</i> (Bennett § 120); a 4ª faz em geral <i>-īvī</i>, <i>-ītum</i> (A&amp;G § 179.d), com exceções como <i>veniō, venīre, vēnī, ventum</i>; a 2ª faz sobretudo <i>-uī</i>, <i>-itum</i> como <i>moneō</i> (A&amp;G § 173), mas tem vários perfeitos de outros tipos (<i>vīdī, mānsī, sēdī, dēlēvī</i>). Na 3ª, porém, Allen &amp; Greenough avisam que aparecem "todas as variedades" de perfeito, e que ele "não se forma do tema do presente, mas da raiz" (§ 179.c.2). O presente não dá nenhuma pista segura. Compare:</p>
{comparacao('Presentes parecidos, perfeitos diferentes (3ª conjugação)', ['Partes principais', 'Tipo de perfeito', 'Português'], [
    ['regō, regere, rēxī, rēctum', '-s- (<i>g</i> + <i>s</i> = <i>x</i>)', 'reger, governar'],
    ['legō, legere, lēgī, lēctum', 'alongamento', 'ler; recolher'],
    ['currō, currere, cucurrī, cursum', 'reduplicação', 'correr'],
    ['dēfendō, dēfendere, dēfendī, dēfēnsum', 'sem mudança', 'defender'],
    ['petō, petere, petīvī, petītum', '-v-, como se fosse da 4ª', 'pedir; dirigir-se a'],
    ['pōnō, pōnere, posuī, positum', '-u-', 'pôr, colocar'],
])}
<p><i>Regō</i> e <i>legō</i> diferem numa só letra no presente e seguem caminhos diferentes no perfeito; nada no presente de <i>petō</i> anuncia <i>petīvī</i>. É por isso que os verbos se aprendem pelas quatro partes, e não só pelo infinitivo. O consolo é que os verbos mais irregulares são também os mais frequentes, e você os verá tantas vezes que acabará por saber de cor. O português, aliás, faz o mesmo com os seus: ninguém deduz "fiz", "vim", "vi", "disse" de "fazer", "vir", "ver", "dizer"; aprende-se cada um. E, segundo a explicação corrente da gramática histórica, boa parte desses perfeitos portugueses irregulares vem justamente dos latinos: <i>fēcī</i>, <i>vēnī</i>, <i>vīdī</i>, <i>dīxī</i>.</p>
{tabela(['Conjugação', 'Partes principais dos verbos usados neste capítulo', 'Significado'], [
    ['1ª', 'laudō, -āre, -āvī, -ātum · labōrō · nārrō · spectō · portō · vocō · nāvigō · exspectō · cantō · parō (todos em -āvī, -ātum) · dō, dare, dedī, datum · stō, stāre, stetī, stātūrus', 'louvar · trabalhar · contar · olhar · carregar · chamar · navegar · esperar, aguardar · cantar · preparar · dar · estar de pé'],
    ['2ª', 'habeō, -ēre, habuī, habitum · timeō, -ēre, timuī · doceō, -ēre, docuī, doctum · teneō, -ēre, tenuī, tentum · videō, -ēre, vīdī, vīsum · maneō, -ēre, mānsī, mānsum · sedeō, -ēre, sēdī, sessum · respondeō, -ēre, respondī, respōnsum · dēleō, -ēre, dēlēvī, dēlētum', 'ter · temer · ensinar · segurar · ver · ficar · estar sentado · responder · destruir'],
    ['3ª', 'dūcō, dūxī, ductum · dīcō, dīxī, dictum · scrībō, scrīpsī, scrīptum · mittō, mīsī, missum · vīvō, vīxī, vīctum · legō, lēgī, lēctum · agō, ēgī, āctum · vincō, vīcī, victum · emō, ēmī, ēmptum · currō, cucurrī, cursum · discō, didicī · cadō, cecidī, cāsūrus · dēfendō, dēfendī, dēfēnsum · vertō, vertī, versum', 'conduzir · dizer · escrever · enviar · viver · ler · conduzir, fazer · vencer · comprar · correr · aprender · cair · defender · virar'],
    ['3ª em -iō', 'capiō, cēpī, captum · faciō, fēcī, factum · fugiō, fūgī, fugitūrus', 'pegar · fazer · fugir'],
    ['4ª', 'audiō, -īre, -īvī, -ītum · dormiō, -īvī, -ītum · sciō, -īvī, -ītum · veniō, -īre, vēnī, ventum', 'ouvir · dormir · saber · vir, chegar'],
], 'Vocabulário: partes principais (conferidas em Bennett §§ 100–127 e no Lewis & Short)', latim_cols=(1,))}
'''),
        ('O mais-que-perfeito e o futuro perfeito', f'''
<p>Os outros dois tempos do <i>perfectum</i> se fazem com o mesmo tema do perfeito e com terminações que você já conhece: são, quase letra por letra, o imperfeito e o futuro de <i>esse</i> do capítulo 12, <i>eram</i> e <i>erō</i>. Allen &amp; Greenough apontam essa influência de <i>eram</i> e <i>erō</i> na formação dos dois tempos (§ 169.b–c), e Ravizza dá a regra prática: tire o <i>-ī</i> do perfeito e acrescente as terminações (n. 86).</p>
{tabela(['Pessoa', 'Mais-que-perfeito', 'Português', 'Futuro perfeito', 'Português'], [
    ['1ª sing.', 'rēx<b>eram</b>', 'tinha governado', 'rēx<b>erō</b>', 'terei governado'],
    ['2ª sing.', 'rēx<b>erās</b>', 'tinhas governado', 'rēx<b>eris</b>', 'terás governado'],
    ['3ª sing.', 'rēx<b>erat</b>', 'tinha governado', 'rēx<b>erit</b>', 'terá governado'],
    ['1ª pl.', 'rēx<b>erāmus</b>', 'tínhamos governado', 'rēx<b>erimus</b>', 'teremos governado'],
    ['2ª pl.', 'rēx<b>erātis</b>', 'tínheis governado', 'rēx<b>eritis</b>', 'tereis governado'],
    ['3ª pl.', 'rēx<b>erant</b>', 'tinham governado', 'rēx<b>erint</b>', 'terão governado'],
], 'Mais-que-perfeito e futuro perfeito: tema do perfeito + eram / erō (Bennett § 105)', latim_cols=(1, 3))}
<p>Compare com <i>esse</i>: <i>eram, erās, erat, erāmus, erātis, erant</i> é exatamente o final do mais-que-perfeito. No futuro perfeito a correspondência também é completa, <b>menos na 3ª pessoa do plural</b>: o futuro de <i>esse</i> é <i>erunt</i>, mas o futuro perfeito termina em <b><i>-erint</i></b> (<i>amāverint, rēxerint, fuerint</i>; Bennett §§ 100–101). O mesmo vale para todos os verbos: <i>amāveram</i>, <i>monueram</i>, <i>audīveram</i>, <i>cēperam</i>, <i>fueram</i>; <i>amāverō</i>, <i>monuerō</i>, <i>audīverō</i>, <i>cēperō</i>, <i>fuerō</i>.</p>
<h3>O que eles significam: anterioridade</h3>
<p>Os dois tempos situam uma ação como <b>já concluída antes de outro momento</b>. O mais-que-perfeito indica uma ação concluída antes de um momento passado (Bennett § 263; A&amp;G § 477), como o "tinha feito" do português; o futuro perfeito, uma ação concluída antes de um momento futuro (Bennett § 264; A&amp;G § 478), como o "terei feito".</p>
{exemplos([('Avus nāviculam parāverat; tum puerī vēnērunt.', 'O avô tinha preparado o barquinho; então os meninos chegaram. (<i>tum</i>, então: primeiro o preparo, depois a chegada)'),
           ('Crās epistulam scrīpserō.', 'Amanhã terei escrito a carta. (<i>crās</i>, amanhã: concluída antes de amanhã)'),
           ('Sī labōrāveris, laetus eris.', 'Se você trabalhar (literalmente "se tiver trabalhado"), ficará contente. (<i>sī</i>, se)')])}
<p>O último exemplo mostra por que o futuro perfeito é tão mais frequente em latim do que o "terei feito" em português. Quando uma ação futura precisa estar terminada antes de outra, o latim usa o futuro perfeito com rigor (Bennett § 264.a; A&amp;G § 478, nota). O português, nesse caso, usa o <b>futuro do subjuntivo</b>: "se você trabalhar", "quando você chegar". Allen &amp; Greenough dão um exemplo de Cícero que mostra bem a diferença: <i>Ut sēmentem fēceris, ita metēs</i>, "como semeares (literalmente, como tiveres semeado), assim colherás" (§ 478).</p>
{observacao('O português guardou as duas formas', 'Segundo a explicação corrente da gramática histórica do português, os dois tempos deixaram herdeiros. O mais-que-perfeito simples, hoje quase só escrito, continua o latino: <i>amāveram</i> → "amara", <i>fēceram</i> → "fizera", <i>vīderam</i> → "vira" ("ele já partira quando ela chegou"). E o futuro do subjuntivo ("quando eu fizer", "se eu vir") continua, em grande parte, o futuro perfeito latino (<i>fēcerō</i>, <i>vīderō</i>). Por isso a tradução "se você trabalhar" para <i>sī labōrāveris</i> é natural.')}
{observacao('Uma armadilha para depois: -erint', 'A forma <i>amāverint</i> pode ser futuro perfeito, "terão amado", mas também o perfeito do <b>subjuntivo</b>, que tem a mesma 3ª pessoa do plural (Bennett § 101) e que você estudará no capítulo 32. Por enquanto, quando encontrar <i>-erint</i> numa oração que não seja claramente futura, registre a dúvida em vez de forçar o "terão". E não confunda três finais parecidos: <i>-ērunt</i> (perfeito: <i>amāvērunt</i>, "amaram"), <i>-erant</i> (mais-que-perfeito: <i>amāverant</i>, "tinham amado") e <i>-erint</i> (futuro perfeito: <i>amāverint</i>, "terão amado").')}
'''),
        ('Perfeito ou imperfeito? E do texto ao dicionário', f'''
<p>Imperfeito e perfeito falam os dois do passado, e o português os distingue do mesmo modo que o latim: <b>"fazia" × "fez"</b>. O imperfeito apresenta a ação em andamento, repetida ou habitual, e por isso é o tempo da <b>descrição</b>, do pano de fundo (Bennett § 260; A&amp;G § 470). O perfeito apresenta a ação como um fato concluído, e é o tempo da <b>narração</b>, dos acontecimentos que fazem a história andar (Bennett § 262.B). Bennett ilustra a narração com uma sequência de perfeitos: <i>Rēgulus in senātum vēnit, mandāta exposuit</i>, "Régulo veio ao senado, expôs a sua missão" (§ 262.B).</p>
{diagrama_frase([('Avus', 'nominativo · sujeito'), ('fābulās', 'acusativo pl. · objeto'), ('nārrābat', 'imperfeito · cena em curso'), ('Titus', 'nominativo · sujeito'), ('vēnit', 'perfeito · fato novo, concluído')], '<i>Avus fābulās nārrābat; Titus vēnit</i> = O avô contava histórias; Tito chegou. O imperfeito monta a cena, o perfeito conta o que aconteceu nela. Em português, "contava" e "chegou" fazem a mesma divisão.')}
<p>Allen &amp; Greenough observam que, em muitos casos, a escolha depende do ponto de vista: <i>rēx erat</i> e <i>rēx fuit</i> podem referir-se ao mesmo fato, mas "o primeiro descreve a situação, o segundo apenas a constata" (§ 470, nota). Em português, "era rei" e "foi rei". Às vezes o perfeito ganha um sentido enfático: o que foi já não é. <i>Habuit, nōn habet</i>, diz Cícero, "teve, não tem mais" (citado em A&amp;G § 474).</p>
{exemplos([('Puer epistulam scrībē<b>bat</b>.', 'O menino escrevia (estava escrevendo) uma carta. (em curso: não sabemos se terminou)'),
           ('Puer epistulam scrīps<b>it</b>.', 'O menino escreveu uma carta. (fato concluído)'),
           ('Servī in agrō labōrā<b>bant</b>; subitō dominus vēn<b>it</b>.', 'Os escravos trabalhavam no campo; de repente o senhor chegou. (<i>subitō</i>, de repente)')])}
<h3>Do perfeito ao verbete: de rēxit a regō</h3>
<p>No dicionário, o verbo se procura pela 1ª pessoa do presente. Diante de um perfeito, portanto, você precisa voltar do tema do perfeito ao do presente, e o método é o do capítulo 7, com um passo a mais. Tome <i>rēxit</i>:</p>
<ol>
<li><b>Separe a terminação.</b> <i>-it</i> é 3ª pessoa do singular: do perfeito, ou do presente da 3ª conjugação. O que sobra é <i>rēx-</i>.</li>
<li><b>Teste o presente.</b> Se fosse presente, o verbete seria "rēxō", que não existe. Então <i>rēx-</i> é um tema de perfeito.</li>
<li><b>Desfaça a formação.</b> Pelos tipos da seção 4: um <i>x</i> no perfeito costuma ser <i>c</i> ou <i>g</i> + <i>s</i>, e a vogal pode ter sido alongada. Candidatos: "recō" ou <i>regō</i>.</li>
<li><b>Confira no verbete.</b> <i>regō, regere, rēxī, rēctum</i> (no Lewis &amp; Short, <i>rĕgo, xi, ctum, 3</i>): a terceira parte confirma o tema <i>rēx-</i>. <i>Rēxit</i> é "governou".</li>
</ol>
<p>Para os perfeitos com reduplicação, tire a sílaba repetida (<i>cucurr-</i> → <i>curr-</i> → <i>currō</i>; <i>didic-</i> → <i>discō</i>, que tem o <i>-sc-</i> só no presente). Para os de vogal alongada, procure a mesma consoante com vogal breve (<i>lēg-</i> → <i>legō</i>; <i>ēg-</i> → <i>agō</i>, lembrando que o <i>a</i> vira <i>ē</i>). E quando nada disso funcionar, como em <i>tulī</i> (de <i>ferō</i>, capítulo 26), o Whitaker's Words, apresentado no capítulo 7, analisa a forma e devolve o verbete.</p>
{comparacao('Presente ou perfeito? Pares que só a quantidade separa', ['Forma', 'Presente', 'Perfeito', 'Como decidir num texto sem macrons'], [
    ['legit · lēgit', '<i>legit</i>, lê', '<i>lēgit</i>, leu', 'o tempo dos outros verbos da passagem; a narração pede perfeito'],
    ['venit · vēnit', '<i>venit</i>, vem', '<i>vēnit</i>, veio, chegou', 'idem; a pronúncia distingue <u>ve</u>nit de <u>vē</u>nit só pela quantidade'],
    ['fugit · fūgit', '<i>fugit</i>, foge', '<i>fūgit</i>, fugiu', 'idem'],
    ['dēfendit', 'defende', 'defendeu', 'tipo 5: a forma é a mesma; só o contexto decide'],
    ['regit · rēxit', '<i>regit</i>, governa', '<i>rēxit</i>, governou', 'aqui o tema muda (<i>reg-</i> × <i>rēx-</i>): não há dúvida'],
])}
'''),
        ('Análise gramatical: Suetônio e a Vulgata', f'''
<p>A frase latina mais famosa no perfeito tem três palavras. Suetônio conta que, no triunfo pela vitória no Ponto, César mandou levar entre os andores do cortejo um letreiro com três palavras, <span lang="la"><i>VENI · VIDI · VICI</i></span>, que não narrava os fatos da guerra, como os outros letreiros, mas marcava a rapidez com que ela tinha sido concluída (<i>Dīvus Iūlius</i> 37). Plutarco, que escreve em grego, conta que César usou as mesmas três palavras numa carta a um amigo em Roma, e observa que, em latim, elas têm "a mesma terminação", o que dá à frase uma brevidade impressionante (<i>César</i> 50). Essa terminação comum é o <i>-ī</i> do perfeito. O texto foi conferido na The Latin Library e no Perseus; os macrons foram acrescentados.</p>
{exemplos([('Vēnī, vīdī, vīcī.', 'Vim, vi, venci. (Suetônio, <i>Dīvus Iūlius</i> 37.2)'),
           ('Respondit Pīlātus: Quod scrīpsī, scrīpsī.', 'Pilatos respondeu: O que escrevi, escrevi. (Jo 19,22)')])}
{analise('Suetônio, Dīvus Iūlius 37, e Jo 19,22, palavra a palavra', [
    ('Vēnī', 'veniō, venīre, vēnī, ventum (4ª), vir, chegar', 'perfeito do indicativo ativo, 1ª pessoa do singular; tema <i>vēn-</i> (tipo 4: <i>vĕn-</i> → <i>vēn-</i>) + <i>-ī</i>', 'verbo; sujeito "eu" na terminação'),
    ('vīdī', 'videō, vidēre, vīdī, vīsum (2ª), ver', 'perfeito, 1ª pessoa do singular; tema <i>vīd-</i> (tipo 4: <i>vĭd-</i> → <i>vīd-</i>)', 'verbo; objeto não expresso'),
    ('vīcī', 'vincō, vincere, vīcī, victum (3ª), vencer', 'perfeito, 1ª pessoa do singular; tema <i>vīc-</i>: o <i>n</i> de <i>vinc-</i> é só do presente', 'verbo'),
    ('Respondit', 'respondeō, respondēre, respondī, respōnsum (2ª), responder', 'perfeito, 3ª pessoa do singular; o presente seria <i>respondet</i>', 'verbo da oração principal; perfeito histórico (narração)'),
    ('Pīlātus', 'Pīlātus, -ī (m.), Pilatos', 'nominativo singular, 2ª declinação', 'sujeito de <i>respondit</i>'),
    ('Quod', 'pronome relativo, "o que" (capítulo 16)', 'neutro singular, acusativo', 'objeto do primeiro <i>scrīpsī</i>'),
    ('scrīpsī', 'scrībō, scrībere, scrīpsī, scrīptum (3ª), escrever', 'perfeito, 1ª pessoa do singular; tema <i>scrīps-</i> (tipo 2: <i>scrīb-</i> + <i>s</i>)', 'verbo da oração relativa ("o que escrevi")'),
    ('scrīpsī', 'scrībō, scrībere, scrīpsī, scrīptum', 'perfeito, 1ª pessoa do singular', 'verbo principal; perfeito definido: o escrito está feito e assim fica'),
])}
<p>Repare em três coisas. Em <i>Vēnī, vīdī, vīcī</i>, os três perfeitos são do tipo 4 e de três conjugações diferentes (4ª, 2ª e 3ª), mas terminam todos em <i>-ī</i>: é a "mesma terminação" de que fala Plutarco, e é ela que faz a frase soar como um golpe só. O sujeito, "eu", não aparece: está nas três terminações. Em Jo 19,22, a moldura narrativa usa o perfeito histórico, <i>respondit</i>, "respondeu"; a resposta de Pilatos usa o perfeito definido: <i>scrīpsī</i> não conta só um fato passado, afirma que o letreiro está escrito e não vai mudar. O versículo vem logo depois de <i>Scrīpsit autem et titulum Pīlātus</i>, "Pilatos escreveu também um letreiro" (Jo 19,19), e a repetição do mesmo perfeito, primeiro na relativa e depois na principal, é o que dá à frase o tom definitivo. Na pronúncia, <i>respondit</i> se acentua na penúltima, <i>res<u>pon</u>dit</i>, porque a sílaba é longa por posição.</p>
<h3>Resumo</h3>
<ul>
<li><b><i>Infectum</i> × <i>perfectum</i></b>: ação em curso (tema do presente) × ação concluída (tema do perfeito); "fazia" × "fez".</li>
<li><b>Partes principais</b>: <i>amō</i> (verbete), <i>amāre</i> (conjugação e tema do presente), <i>amāvī</i> (tema do perfeito), <i>amātum</i> (para a passiva e os particípios, mais tarde); <i>sum, esse, fuī</i>.</li>
<li><b>Perfeito</b>: tema + <i>-ī, -istī, -it, -imus, -istis, -ērunt</i> (ou <i>-ēre</i>), iguais em todas as conjugações; formas sincopadas como <i>amāstī, amārunt</i>.</li>
<li><b>Tema do perfeito</b>: <i>-v-/-u-</i>, <i>-s-</i>, reduplicação, alongamento, sem mudança; na 3ª conjugação, imprevisível: decore as quatro partes.</li>
<li><b>Mais-que-perfeito</b> (<i>-eram</i>, "tinha feito") e <b>futuro perfeito</b> (<i>-erō</i>, "terei feito"; 3ª pl. <i>-erint</i>): ação concluída antes de um momento passado ou futuro.</li>
</ul>
'''),
    ],
    erros_comuns=[
        ('Procurar <i>rēxit</i> no dicionário como "rēxō", ou <i>cēpit</i> como "cēpō".', 'O dicionário registra o verbo pela 1ª pessoa do <b>presente</b>, e o tema do perfeito muitas vezes é diferente do tema do presente. Separe a terminação, reconheça o tipo de perfeito (<i>x</i> = <i>g/c</i> + <i>s</i>; vogal alongada; reduplicação) e reconstrua o presente: <i>rēx-</i> → <i>regō</i>; <i>cēp-</i> → <i>capiō</i>. Depois confira a 3ª parte principal no verbete.'),
        ('Traduzir todo perfeito por "tenho feito": <i>Librum lēgī</i>, "tenho lido o livro".', 'No português do Brasil, "tenho lido" indica ação repetida que continua até agora. O perfeito latino, nos dois usos, traduz-se pelo pretérito perfeito: "li o livro", "já li o livro" (A&amp;G § 161; Bennett § 262).'),
        ('Usar o perfeito e o imperfeito como se fossem equivalentes: traduzir <i>scrībēbat</i> por "escreveu" e <i>scrīpsit</i> por "escrevia".', 'O imperfeito é ação em curso ou habitual ("escrevia, estava escrevendo"), o tempo da descrição; o perfeito é o fato concluído ("escreveu"), o tempo da narração (Bennett §§ 260, 262). A mesma diferença existe em português: "fazia" × "fez".'),
        ('Confundir <i>-ērunt</i>, <i>-erant</i>, <i>-erint</i> e o <i>erunt</i> de <i>esse</i>.', '<i>amāvērunt</i>, "amaram" (perfeito); <i>amāverant</i>, "tinham amado" (mais-que-perfeito, como <i>erant</i>); <i>amāverint</i>, "terão amado" (futuro perfeito; a mesma forma serve ao perfeito do subjuntivo, capítulo 32); <i>erunt</i>, "serão" (futuro de <i>esse</i>). Olhe a vogal depois do <i>r</i> e o tema antes dele.'),
        ('Ler <i>vēnit</i>, <i>lēgit</i>, <i>fūgit</i> como presente porque, sem macrons, se escrevem <i>venit</i>, <i>legit</i>, <i>fugit</i>.', 'Esses perfeitos (tipo 4) só se distinguem do presente pela quantidade da vogal. Num texto sem macrons, decida pelo contexto: numa narração no passado, entre outros perfeitos, é perfeito. Ao ler em voz alta, faça a vogal longa: <i><u>vē</u>nit</i>, "veio".'),
        ('Tomar a 3ª pessoa do plural em <i>-ēre</i> por um infinitivo: <i>Puerī lupum vīdēre</i>, "os meninos ver o lobo".', 'Com sujeito no plural e nenhum verbo que peça infinitivo, <i>-ēre</i> no tema do perfeito é a variante de <i>-ērunt</i>: <i>vīdēre</i> = <i>vīdērunt</i>, "os meninos viram o lobo" (Bennett §§ 101–110; Kennedy § 113). O infinitivo de <i>videō</i> é <i>vidēre</i>, com <i>i</i> breve e tema do presente.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Do texto ao verbete: rēxerant',
            'Num texto você encontra <i lang="la">rēxerant</i>. Identifique tempo, pessoa e número, chegue à entrada de dicionário e traduza.', [
            ('Qual é a terminação?', '<i>-erant</i>: é <i>erant</i>, o imperfeito de <i>esse</i>, colado a um tema. Tema do perfeito + <i>-eram</i> é o <b>mais-que-perfeito</b>; <i>-nt</i>, 3ª pessoa do plural.'),
            ('O que sobra, e que tipo de tema é?', 'Sobra <i>rēx-</i>, um tema de perfeito (o mais-que-perfeito sempre se faz com ele). O <i>x</i> indica o tipo 2: <i>c</i> ou <i>g</i> + <i>s</i>.'),
            ('Que presente reconstruir?', 'Tirando o <i>s</i> e voltando ao <i>g</i> ou ao <i>c</i>: "recō" ou <i>regō</i>. Só <i>regō</i> existe.'),
            ('Confira no verbete.', '<i>regō, regere, rēxī, rēctum</i>: a 3ª parte, <i>rēxī</i>, confirma o tema <i>rēx-</i>.'),
            ('Traduza.', '<i>Rēxerant</i>: "tinham governado", "haviam governado" (ou "governaram", "governaram antes", se o contexto pedir só a anterioridade).'),
        ]),
        pratica_guiada('Prática guiada 2 · Imperfeito e perfeito na mesma frase',
            'Analise e traduza: <i lang="la">Servī in agrō diū labōrābant; tandem dominus vēnit et servōs laudāvit.</i> Vocabulário: <i>diū</i>, por muito tempo; <i>tandem</i>, finalmente; <i>laudō, -āre, -āvī, -ātum</i>, louvar, elogiar.', [
            ('Quais são os verbos e em que tempo estão?', '<i>labōrābant</i>: imperfeito (<i>-bā-</i>), 3ª do plural. <i>vēnit</i>: perfeito de <i>veniō</i> (tema <i>vēn-</i>), 3ª do singular. <i>laudāvit</i>: perfeito de <i>laudō</i> (tema <i>laudāv-</i>), 3ª do singular.'),
            ('Quais são os sujeitos?', '<i>Servī</i> (nominativo plural) para <i>labōrābant</i>; <i>dominus</i> (nominativo singular) para <i>vēnit</i> e <i>laudāvit</i>. <i>Servōs</i>, acusativo, é o objeto de <i>laudāvit</i>.'),
            ('Por que um imperfeito e dois perfeitos?', 'O imperfeito, com <i>diū</i>, descreve a situação que durava: o pano de fundo. Os perfeitos contam os dois fatos novos, um depois do outro: o senhor chegou, o senhor elogiou.'),
            ('Monte a tradução.', '"Os escravos trabalhavam no campo havia muito tempo; finalmente o senhor chegou e elogiou os escravos."'),
        ], 'Conclusão: o imperfeito monta a cena ("trabalhavam"), o perfeito faz a história andar ("chegou", "elogiou").'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Reconheça a forma', 'Dê o tempo, a pessoa, o número e as partes principais do verbo, e traduza. Os verbos estão no vocabulário da seção 4.', [
            ('<i>amāvistis</i>', 'Perfeito, 2ª do plural; <i>amō, amāre, amāvī, amātum</i>: "amastes, vocês amaram". A terminação <i>-istis</i> só existe no perfeito.'),
            ('<i>monuērunt</i>', 'Perfeito, 3ª do plural; <i>moneō, monēre, monuī, monitum</i>: "advertiram". Tema <i>monu-</i> + <i>-ērunt</i>.'),
            ('<i>rēxit</i>', 'Perfeito, 3ª do singular; <i>regō, regere, rēxī, rēctum</i>: "governou". O presente seria <i>regit</i>: o tema <i>rēx-</i> decide.'),
            ('<i>audīverat</i>', 'Mais-que-perfeito, 3ª do singular; <i>audiō, audīre, audīvī, audītum</i>: "tinha ouvido". Tema <i>audīv-</i> + <i>-erat</i>.'),
            ('<i>cēpimus</i>', 'Perfeito, 1ª do plural; <i>capiō, capere, cēpī, captum</i>: "pegamos". O <i>a</i> breve de <i>cap-</i> vira <i>ē</i> (tipo 4); o presente é <i>capimus</i>.'),
            ('<i>fuistī</i>', 'Perfeito, 2ª do singular; <i>sum, esse, fuī, futūrus</i>: "foste, estiveste; você foi, esteve".'),
            ('<i>dūxerō</i>', 'Futuro perfeito, 1ª do singular; <i>dūcō, dūcere, dūxī, ductum</i>: "terei conduzido". Tema <i>dūx-</i> + <i>-erō</i>.'),
            ('<i>vīdērunt</i>', 'Perfeito, 3ª do plural; <i>videō, vidēre, vīdī, vīsum</i>: "viram". Também pode aparecer como <i>vīdēre</i>.'),
            ('<i>dedit</i>', 'Perfeito, 3ª do singular; <i>dō, dare, dedī, datum</i>: "deu". Perfeito com reduplicação (<i>de-d-</i>), exceção na 1ª conjugação.'),
            ('<i>cucurrērunt</i>', 'Perfeito, 3ª do plural; <i>currō, currere, cucurrī, cursum</i>: "correram". Tire a reduplicação <i>cu-</i> para chegar a <i>curr-</i>.'),
            ('<i>dēfendit</i>', 'Presente ou perfeito, 3ª do singular; <i>dēfendō, dēfendere, dēfendī, dēfēnsum</i>: "defende" ou "defendeu". Perfeito sem mudança do tema (tipo 5): só o contexto decide.'),
            ('<i>scrīpserint</i>', 'Futuro perfeito, 3ª do plural; <i>scrībō, scrībere, scrīpsī, scrīptum</i>: "terão escrito". Atenção: a mesma forma é também perfeito do subjuntivo (capítulo 32).'),
        ]),
        exercicio('Exercício 2 · Do perfeito ao presente', 'Diga o tipo de formação do perfeito (1 a 5, seção 4) e dê as duas primeiras partes principais, com a conjugação. Vocabulário: <i>dīcō</i>, dizer; <i>cadō</i>, cair; <i>vertō</i>, virar; <i>agō</i>, conduzir, fazer.', [
            ('<i>laudāvī</i>', 'Tipo 1 (<i>-v-</i>): <i>laudō, laudāre</i>, 1ª conjugação. O <i>v</i> se junta ao tema <i>laudā-</i>.'),
            ('<i>habuī</i>', 'Tipo 1 (<i>-u-</i>): <i>habeō, habēre</i>, 2ª. Como <i>monuī</i>, o <i>ē</i> do tema não aparece no perfeito.'),
            ('<i>dīxī</i>', 'Tipo 2 (<i>-s-</i>): <i>dīcō, dīcere</i>, 3ª. O <i>x</i> é <i>c</i> + <i>s</i>.'),
            ('<i>mīsī</i>', 'Tipo 2 (<i>-s-</i>): <i>mittō, mittere</i>, 3ª. O <i>t</i> cai diante do <i>s</i>, e a vogal fica longa.'),
            ('<i>vēnī</i>', 'Tipo 4 (alongamento): <i>veniō, venīre</i>, 4ª. Exceção ao <i>-īvī</i> da 4ª conjugação.'),
            ('<i>ēgī</i>', 'Tipo 4 (alongamento, com <i>a</i> → <i>ē</i>): <i>agō, agere</i>, 3ª. A vogal muda de timbre, como em <i>faciō</i> → <i>fēcī</i>.'),
            ('<i>cecidī</i>', 'Tipo 3 (reduplicação): <i>cadō, cadere</i>, 3ª. Tire o <i>ce-</i>: sobra <i>cid-</i>, com o <i>a</i> enfraquecido em <i>i</i>; o presente tem <i>cad-</i>.'),
            ('<i>vertī</i>', 'Tipo 5 (sem mudança): <i>vertō, vertere</i>, 3ª. O tema do perfeito é igual ao do presente.'),
            ('<i>fūgī</i>', 'Tipo 4 (alongamento): <i>fugiō, fugere</i>, 3ª em <i>-iō</i>. <i>Fŭg-</i> → <i>fūg-</i>.'),
            ('<i>mānsī</i>', 'Tipo 2 (<i>-s-</i>): <i>maneō, manēre</i>, 2ª. Um perfeito em <i>-sī</i> na 2ª conjugação: mais uma prova de que o perfeito se decora.'),
        ]),
        exercicio('Exercício 3 · Conjugue e transforme', 'Conjugue os três primeiros itens no tempo pedido. Depois passe as frases para o perfeito (ou, no último item, do imperfeito para o mais-que-perfeito), mantendo pessoa e número.', [
            ('<i>dūcō</i> no perfeito', '<i>dūxī, dūxistī, dūxit, dūximus, dūxistis, dūxērunt</i> (ou <i>dūxēre</i>). Tema <i>dūx-</i>, da 3ª parte <i>dūxī</i>.'),
            ('<i>capiō</i> no mais-que-perfeito', '<i>cēperam, cēperās, cēperat, cēperāmus, cēperātis, cēperant</i>. Tema do perfeito <i>cēp-</i> + as formas de <i>eram</i>.'),
            ('<i>sum</i> no futuro perfeito', '<i>fuerō, fueris, fuerit, fuerimus, fueritis, fuerint</i>. Como <i>erō</i>, menos a 3ª do plural: <i>fuerint</i>, não "fuerunt".'),
            ('<i>Puer epistulam scrībit.</i>', '<i>Puer epistulam scrīpsit.</i> "O menino escreveu a carta." <i>Scrībō, scrīpsī</i>: tipo 2.'),
            ('<i>Agricolae equōs dūcunt.</i>', '<i>Agricolae equōs dūxērunt.</i> "Os agricultores conduziram os cavalos." <i>-unt</i> do presente vira <i>-ērunt</i> sobre o tema <i>dūx-</i>.'),
            ('<i>Fābulās poētae audīmus.</i>', '<i>Fābulās poētae audīvimus.</i> "Ouvimos as histórias do poeta." Repare que <i>audīmus</i> e <i>audīvimus</i> diferem só pelo <i>v</i>: é o sinal do tema do perfeito.'),
            ('<i>Puella rosam capit.</i>', '<i>Puella rosam cēpit.</i> "A menina pegou a rosa." Tema <i>cēp-</i>, com vogal longa: o presente é <i>capit</i>.'),
            ('<i>Magistra puerōs monet.</i>', '<i>Magistra puerōs monuit.</i> "A professora advertiu os meninos."'),
            ('Para o mais-que-perfeito: <i>Servī in agrō labōrābant.</i>', '<i>Servī in agrō labōrāverant.</i> "Os escravos tinham trabalhado no campo." Do imperfeito (ação em curso no passado) para o mais-que-perfeito (ação já concluída antes de um momento passado).'),
        ]),
        exercicio('Exercício 4 · Perfeito ou imperfeito?', 'Escolha a forma adequada e explique a escolha; nos dois últimos itens, traduza e comente. Vocabulário: <i>ōlim</i>, outrora; <i>cotīdiē</i>, todos os dias; <i>herī</i>, ontem; <i>subitō</i>, de repente; <i>avus, -ī</i> (m.), avô; <i>rēx, rēgis</i> (m.), rei.', [
            ('<i>Ōlim avus in īnsulā (habitābat / habitāvit) et cotīdiē nāvigābat.</i>', '<i>habitābat</i>: <i>ōlim</i> e <i>cotīdiē</i> descrevem uma situação duradoura e um hábito, valores do imperfeito. "Outrora o avô morava na ilha e navegava todos os dias."'),
            ('<i>Herī Titus epistulam (scrībēbat / scrīpsit) et avō mīsit.</i>', '<i>scrīpsit</i>: dois fatos concluídos em sequência, escrever e depois enviar (<i>mīsit</i>, perfeito de <i>mittō</i>). "Ontem Tito escreveu uma carta e a enviou ao avô." Com <i>scrībēbat</i>, ele "estava escrevendo" e a sequência perderia o sentido.'),
            ('<i>Puerī in hortō ambulābant; subitō lupus (veniēbat / vēnit).</i>', '<i>vēnit</i>: <i>subitō</i> marca um fato pontual que irrompe na cena descrita pelo imperfeito. "Os meninos passeavam no jardim; de repente veio um lobo."'),
            ('<i>Avus fābulās nārrābat, et puerī (audiēbant / audīvērunt).</i>', '<i>audiēbant</i>: as duas ações acontecem ao mesmo tempo, como pano de fundo. "O avô contava histórias, e os meninos escutavam." <i>Audīvērunt</i> não seria errado, mas mudaria a perspectiva: "e os meninos ouviram" (um fato concluído).'),
            ('<i>Rēx erat. · Rēx fuit.</i>', '"Era rei" descreve a situação; "foi rei" apenas a constata, e pode sugerir que já não é. Allen &amp; Greenough usam este par para explicar a diferença entre os dois tempos (§ 470, nota).'),
            ('<i>Habuit, nōn habet.</i> (Cícero, citado em A&amp;G § 474)', '"Teve, não tem mais." <i>Habuit</i> é perfeito de <i>habeō</i> (tema <i>habu-</i>), e o contraste com o presente <i>habet</i> mostra o perfeito enfático: o que existiu já não existe.'),
        ]),
        exercicio('Exercício 5 · Leia o texto', 'O texto abaixo reconta no passado a travessia do capítulo 8. Leia em voz alta e traduza frase a frase, dizendo o tempo de cada verbo e por que ele foi usado. Vocabulário: <i>herī</i>, ontem; <i>cum</i> + ablativo, com; <i>avus, -ī</i> (m.), avô; <i>avia, -ae</i> (f.), avó; <i>nāvigō, -āre, -āvī</i>, navegar; <i>prīmō</i>, primeiro; <i>serēnus, -a, -um</i>, sereno; <i>subitō</i>, de repente; <i>ventus, -ī</i> (m.), vento; <i>nāvicula, -ae</i> (f.), barquinho; <i>intrō, -āre, -āvī</i>, entrar; <i>rēmus, -ī</i> (m.), remo; <i>teneō, -ēre, tenuī</i>, segurar; <i>tandem</i>, finalmente; <i>ōra, -ae</i> (f.), litoral; <i>exspectō, -āre, -āvī</i>, esperar; <i>cēna, -ae</i> (f.), jantar; <i>iam</i>, já; <i>parō, -āre, -āvī</i>, preparar; <i>post</i> + acusativo, depois de; <i>mox</i>, logo; <i>dormiō, -īre, -īvī</i>, dormir.<br><span lang="la"><i>' + _TEXTO_LEITURA + '</i></span>', [
            ('Frases 1–2', '"Ontem Tito e Flávia navegaram com o avô até a ilha. Primeiro o céu estava sereno, e as crianças cantavam." <i>Nāvigāvērunt</i>: perfeito, o fato. <i>Erat</i> e <i>cantābant</i>: imperfeitos, a descrição da cena.'),
            ('Frases 3–4', '"De repente veio um vento forte, e a água entrou no barquinho. Flávia teve medo, mas o avô segurou os remos e chamou Tito." Todos perfeitos (<i>vēnit, intrāvit, timuit, tenuit, vocāvit</i>): uma série de acontecimentos. <i>Timuit</i>, "teve medo, sentiu medo", e não "temia": a reação naquele momento.'),
            ('Frase 5', '"Finalmente o avô levou o barquinho até a ilha." <i>Dūxit</i>: perfeito de <i>dūcō</i> (tipo 2).'),
            ('Frase 6', '"A avó esperava no litoral; já tinha preparado um bom jantar." <i>Exspectābat</i>: imperfeito, situação em curso quando eles chegam. <i>Parāverat</i>: mais-que-perfeito, ação concluída antes desse momento passado (reforçada por <i>iam</i>).'),
            ('Frase 7', '"Depois do jantar o avô contou histórias, e as crianças logo dormiram." <i>Nārrāvit</i> e <i>dormīvērunt</i>: perfeitos, os fatos finais. <i>Puerī</i>, plural masculino, inclui Flávia: "as crianças".'),
            ('Uma frase autêntica: <i>Deum nēmō vīdit umquam.</i> (Jo 1,18; <i>nēmō</i>, ninguém; <i>umquam</i>, alguma vez, jamais)', '"Ninguém jamais viu a Deus." <i>Vīdit</i> é perfeito (tema <i>vīd-</i>, vogal longa); o presente seria <i>videt</i>. <i>Deum</i>, acusativo, é o objeto, e vem primeiro por ênfase; <i>nēmō</i> é o sujeito. É um perfeito definido: até hoje, ninguém viu.'),
        ]),
        exercicio('Exercício 6 · Retroversão', 'Passe para o latim, sem pronomes sujeito, usando o vocabulário do capítulo. Vocabulário extra: <i>crās</i>, amanhã; <i>nunc</i>, agora; <i>liber, librī</i> (m.), livro.', [
            ('Os meninos leram o livro.', '<i>Puerī librum lēgērunt.</i> Perfeito de <i>legō</i>: tema <i>lēg-</i> (vogal longa) + <i>-ērunt</i>. "Legunt" seria presente.'),
            ('Escrevemos uma carta à rainha.', '<i>Rēgīnae epistulam scrīpsimus.</i> <i>Rēgīnae</i> no dativo (a quem); <i>scrīps-</i> + <i>-imus</i>. Também é possível <i>ad rēgīnam</i>, com <i>ad</i> + acusativo, "para a rainha".'),
            ('A menina viu o lobo e fugiu.', '<i>Puella lupum vīdit et fūgit.</i> Dois perfeitos do tipo 4: <i>vīd-</i> e <i>fūg-</i>.'),
            ('Fui marinheiro; agora sou agricultor.', '<i>Nauta fuī; nunc agricola sum.</i> <i>Fuī</i>, perfeito de <i>esse</i>, com o predicativo no nominativo, como no presente (capítulo 6).'),
            ('O agricultor tinha conduzido os cavalos para o campo.', '<i>Agricola equōs in agrum dūxerat.</i> Mais-que-perfeito: tema <i>dūx-</i> + <i>-erat</i>; <i>in</i> + acusativo para a direção.'),
            ('Amanhã terei escrito a carta.', '<i>Crās epistulam scrīpserō.</i> Futuro perfeito: concluída antes de um momento futuro; tema <i>scrīps-</i> + <i>-erō</i>.'),
        ]),
    ],
    leituras=['ravizza-gramatica-latina', 'bennett-new-latin-grammar', 'greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', 'college-dcc-latin-core-vocabulary', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'vulgata-biblia-sacra-vulgata-editio-clementina'],
    leituras_nota='Para consulta, Ravizza dá as terminações do perfeito e dos tempos que dele derivam, em português (n. 86); em Bennett, os tempos do perfectum de cada verbo-modelo estão nos §§ 100–110, a formação do tema no § 118 e as listas de verbos com as partes principais nos §§ 120–122; em Allen &amp; Greenough, as partes principais estão nos §§ 172–173 e a formação do perfeito nos §§ 169 e 177. Para aprender as partes principais, use a lista DCC, que traz os verbos mais frequentes com as quatro formas por extenso: recite-as em voz alta, uma linha de cada vez. Para leitura, em <i>Familia Romana</i> procure, nos capítulos em que as personagens contam o que aconteceu, a alternância entre imperfeito e perfeito; e na Vulgata, os relatos dos Evangelhos (por exemplo, Jo 19 e 20) são uma sequência de perfeitos históricos, com imperfeitos para a cena.',
)
