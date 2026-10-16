from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='16-o-pronome-relativo', titulo='O pronome relativo e as orações relativas',
    titulo_latim='Dē prōnōmine relātīvō', tempo='70 min',
    resumo='O pronome quī, quae, quod e as orações que ele introduz: a declinação, a regra de ouro da concordância (gênero e número do antecedente, caso da própria oração), a pessoa do verbo, o antecedente omitido (quī = "quem, aquele que"), o par is … quī, a oração relativa que vem antes da principal, e o relativo de ligação no começo da frase (quī = et is). Um versículo de Mateus analisado palavra a palavra.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['pronome relativo', 'quī, quae, quod', 'oração relativa', 'antecedente', 'concordância do relativo', 'caso do relativo', 'pessoa do verbo na relativa', 'cuius e o português cujo', 'quōcum, quibuscum', 'antecedente omitido', 'is … quī, id quod', 'relativa antes da principal', 'relativo de ligação', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 15: os demonstrativos, sobretudo <i>is, ea, id</i>, que é o antecedente típico do relativo, e a declinação pronominal (genitivo e dativo em <i>-ius</i>, <i>-ī</i>). Capítulo 10: os adjetivos de segunda classe (<i>omnis, fortis</i>), usados em alguns exemplos. Os capítulos 6 e 9 dão os verbos e os nomes da terceira declinação dos exercícios.',
                       licoes=['15-os-demonstrativos', '10-a-terceira-declinacao-temas-em-i', '14-os-pronomes-pessoais']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 89 e nota 27 (declinação de quī, quae, quod; quīcum), § 247.1 (is como antecedente do relativo; id quod), § 250 (concordância: gênero, número e pessoa do antecedente, caso da própria oração; 250.3 concordância com o predicativo; 250.5 atração), § 251 (251.1 antecedente omitido: quī nātūram sequitur sapiēns est; 251.3 antecedente repetido; 251.4 antecedente incorporado na relativa que vem antes; 251.5 o relativo nunca se omite; 251.6 relativo no início da frase, onde o português usa demonstrativo)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 147 (declinação), § 150 d (cum enclítico: quōcum, quibuscum), §§ 303–304 (o relativo como pronome e como conectivo; quae cum ita sint = et cum ea ita sint), § 305 (concordância em gênero e número, caso pela própria oração), § 306 (concordância com o predicativo; atração), § 307 (antecedente repetido, só na relativa, omitido; id quod), § 308 a, d, f (o relativo nunca se omite; a relativa antes da principal; o relativo de ligação)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 97 (declinação, pelo índice do OCR), § 195 (concordância em gênero, número e pessoa; caso pela própria oração: Amō tē, māter, quae mē amās), §§ 330–331 (o relativo "entre dois casos do mesmo nome": vir quem virum vidēs rēx est e as quatro variantes)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 71 (o relativo une duas proposições e representa na segunda um nome da primeira; declinação com tradução portuguesa: cujus "do qual, cujo"; quōcum, quācum, quibuscum)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Mt 6,9 e 10,40; Jo 8,26 e 18,37', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Matthaeum', nota='frases autênticas das seções 3, 4 e 6 e do exercício 6, conferidas na Wikisource latina; ortografia adaptada (ae por æ, i por j) e macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Declinar <i>quī, quae, quod</i> e reconhecer suas formas ambíguas (<i>quī</i>, <i>quae</i>, <i>quibus</i>).',
        'Aplicar a regra de concordância: gênero e número do antecedente, caso da função que o relativo exerce na sua própria oração; e a pessoa do verbo da relativa.',
        'Delimitar uma oração relativa dentro da frase e traduzi-la por "que, o qual, quem, cujo".',
        'Ler orações relativas sem antecedente expresso (<i>quī</i> = "quem, aquele que"), com <i>is … quī</i> e antepostas à principal.',
        'Reconhecer e traduzir o relativo de ligação no início de frase (<i>quī</i> = "e ele, este").',
    ],
    secoes=[
        ('Duas frases numa só', f'''
<p>Compare duas frases simples: <i>Puer librum legit</i>, "o menino lê um livro", e <i>Puer fīlius meus est</i>, "o menino é meu filho". O mesmo menino aparece nas duas. O português as junta numa só com a palavra "que": "o menino <b>que</b> lê um livro é meu filho". Esse "que" faz duas coisas ao mesmo tempo: <b>liga</b> uma oração à outra e <b>representa</b>, dentro da segunda, o nome que já apareceu na primeira. É um <b>pronome relativo</b>, e o nome que ele representa chama-se <b>antecedente</b>. O latim faz exatamente o mesmo:</p>
{exemplos([('Puer <b>quī</b> librum legit fīlius meus est.', 'O menino que lê o livro é meu filho. (<i>quī</i> representa <i>puer</i> e é o sujeito de <i>legit</i>)'),
           ('Liber <b>quem</b> puer legit meus est.', 'O livro que o menino lê é meu. (<i>quem</i> representa <i>liber</i> e é o objeto de <i>legit</i>)')])}
<p>O antecedente fica na oração principal; o relativo abre uma <b>oração relativa</b>, que funciona como um grande adjetivo do antecedente: "o menino <i>que lê o livro</i>" equivale a "o menino leitor". Daí o nome técnico que as gramáticas também usam, oração adjetiva. Ravizza (n. 71) resume a definição em uma linha: o relativo "serve para unir duas proposições, representando na segunda um nome ou pronome expresso na primeira".</p>
<p>A diferença entre as duas línguas está no que vem a seguir. O "que" português é invariável: serve a sujeito, objeto, masculino, feminino, singular e plural ("o menino que lê", "o livro que leio", "as meninas que cantam"). O relativo latino se <b>declina</b>, como um adjetivo de três gêneros, e por isso carrega em cada forma três informações: o gênero, o número e o caso. Ler bem uma oração relativa é saber o que cada uma dessas três informações diz.</p>
{dica('<b>Como achar a oração relativa.</b> Ela começa no relativo e, em regra, termina no seu próprio verbo. Ao ler, ponha mentalmente a oração entre colchetes: <i>Puer [quī librum legit] fīlius meus est</i>. Fora dos colchetes sobra a oração principal inteira, <i>Puer … fīlius meus est</i>, que se lê como qualquer frase. Dentro dos colchetes, o relativo exerce uma função como qualquer outra palavra.')}
'''),
        ('Quī, quae, quod: a declinação', f'''
<p>O relativo tem formas para os três gêneros e os dois números, como <i>bonus</i>, mas segue em parte a declinação pronominal do capítulo 15: o genitivo singular <i>cuius</i> e o dativo <i>cui</i> são iguais nos três gêneros, como <i>huius, huic</i> e <i>eius, eī</i>.</p>
{tabela_declinacao('quī, quae, quod, "que, o qual, a qual, quem"', [
    ('qu<b>ī</b>', 'qu<b>ae</b>', 'quo<b>d</b>', 'qu<b>ī</b>', 'qu<b>ae</b>', 'qu<b>ae</b>'),
    ('cu<b>ius</b>', 'cu<b>ius</b>', 'cu<b>ius</b>', 'qu<b>ōrum</b>', 'qu<b>ārum</b>', 'qu<b>ōrum</b>'),
    ('cu<b>i</b>', 'cu<b>i</b>', 'cu<b>i</b>', 'qu<b>ibus</b>', 'qu<b>ibus</b>', 'qu<b>ibus</b>'),
    ('qu<b>em</b>', 'qu<b>am</b>', 'quo<b>d</b>', 'qu<b>ōs</b>', 'qu<b>ās</b>', 'qu<b>ae</b>'),
    ('qu<b>ō</b>', 'qu<b>ā</b>', 'qu<b>ō</b>', 'qu<b>ibus</b>', 'qu<b>ibus</b>', 'qu<b>ibus</b>')],
    casos=('Nominativo', 'Genitivo', 'Dativo', 'Acusativo', 'Ablativo'), colunas=('M. sing.', 'F. sing.', 'N. sing.', 'M. pl.', 'F. pl.', 'N. pl.'))}
<p>O plural lembra muito a primeira e a segunda declinação (<i>quōrum, quārum, quōs, quās</i>), com o dativo e ablativo <i>quibus</i>, que parece da terceira. No singular, o acusativo masculino <i>quem</i> também tem cara de terceira declinação (<i>rēgem</i>). <i>Cuius</i> e <i>cui</i> se pronunciam com a vogal <i>u</i> e um <i>i</i> que funciona como consoante em <i>cuius</i> (<i>cui-ius</i>) e forma ditongo em <i>cui</i>. O português guarda o genitivo na palavra <b>"cujo"</b>, que vem de <i>cuius</i>.</p>
<p>Como em todo pronome, há formas que servem a mais de um caso. Convém tê-las bem presentes, porque a regra de leitura da próxima seção depende de decidir o caso:</p>
{tabela(['Forma', 'Possibilidades', 'Como decidir'], [
    ['<i>quī</i>', 'nom. sing. m. · nom. pl. m.', 'o número do verbo da relativa, se <i>quī</i> for sujeito; o número do antecedente'],
    ['<i>quae</i>', 'nom. sing. f. · nom. pl. f. · nom. e ac. pl. n.', 'o gênero e o número do antecedente; a função que falta na relativa'],
    ['<i>quod</i>', 'nom. e ac. sing. n.', 'se a relativa já tem sujeito, é objeto (e cuidado com a conjunção <i>quod</i>, "porque", do capítulo 37)'],
    ['<i>quibus</i>', 'dat. ou abl. pl., três gêneros', 'preposição ao lado → ablativo; "a quem" → dativo'],
    ['<i>quō</i>, <i>quā</i>', 'abl. sing.', 'em geral com preposição: <i>in quō</i>, "no qual"; <i>dē quā</i>, "da qual"'],
], 'As formas ambíguas do relativo', latim_cols=(0,))}
<p>A preposição <i>cum</i> costuma ir <b>depois</b> do relativo, colada a ele, como em <i>mēcum, tēcum</i> (capítulo 14): <i>quōcum</i>, <i>quācum</i>, <i>quibuscum</i>, "com o qual, com a qual, com os quais" (Allen e Greenough § 150 d; Ravizza n. 71). As outras preposições vêm antes: <i>in quō</i>, <i>ad quem</i>, <i>dē quibus</i>.</p>
'''),
        ('A regra de ouro: concordância e caso', f'''
<p>Esta é a regra que organiza todo o capítulo, e todas as gramáticas a formulam da mesma maneira (Bennett § 250.1; Allen e Greenough § 305; Kennedy § 195): <b>o relativo concorda com o antecedente em gênero e número, mas o seu caso é determinado pela função que ele exerce na sua própria oração.</b> A razão é simples. Gênero e número dizem <i>a quem</i> o relativo se refere, e por isso vêm do antecedente; o caso diz <i>o que</i> o relativo faz, e o que ele faz acontece dentro da relativa, não na principal.</p>
<p>Veja o mesmo antecedente, <i>puella</i> (feminino singular), com o relativo em cinco casos. O gênero e o número não mudam nunca; o caso muda conforme a função dentro dos colchetes:</p>
{tabela(['Frase', 'Função do relativo na sua oração', 'Caso', 'Tradução'], [
    ['Puella [<b>quae</b> cantat] fīlia mea est.', 'sujeito de <i>cantat</i>', 'nominativo', 'A menina que canta é minha filha.'],
    ['Puella [<b>cuius</b> patrem vidēs] fīlia mea est.', 'possuidor de <i>patrem</i>', 'genitivo', 'A menina cujo pai você vê é minha filha.'],
    ['Puella [<b>cui</b> rosam dō] fīlia mea est.', 'a quem se dá', 'dativo', 'A menina a quem dou a rosa é minha filha.'],
    ['Puella [<b>quam</b> laudās] fīlia mea est.', 'objeto de <i>laudās</i>', 'acusativo', 'A menina que você elogia é minha filha.'],
    ['Puella [<b>quācum</b> ambulō] fīlia mea est.', 'companhia (<i>cum</i> + abl.)', 'ablativo', 'A menina com quem passeio é minha filha.'],
], 'Um antecedente, cinco casos do relativo', latim_cols=(0,))}
<p>Kennedy (§§ 330–331) propõe uma imagem útil: o relativo está "entre dois casos do mesmo nome" e concorda com o segundo. Em <i>vir quem vidēs rēx est</i>, "o homem que você vê é rei", é como se se dissesse <i>vir, quem virum vidēs, rēx est</i>: o primeiro <i>vir</i> está no caso da principal (nominativo, sujeito de <i>est</i>), o segundo <i>virum</i>, que não se diz, estaria no caso da relativa (acusativo, objeto de <i>vidēs</i>), e o relativo toma esse segundo caso. Às vezes os autores escrevem mesmo os dois nomes (Bennett § 251.3: <i>erant itinera duo, quibus itineribus</i>), e você verá na seção 4 o caso em que o nome aparece só dentro da relativa.</p>
<p>Na prática, faça sempre três perguntas ao encontrar um relativo: <b>(1)</b> qual o gênero e o número? Isso aponta o antecedente, em geral o nome mais próximo antes do relativo com o mesmo gênero e número. <b>(2)</b> Qual o caso? Isso diz a função dentro da relativa. <b>(3)</b> Onde termina a relativa? Normalmente no seu verbo. O exemplo a seguir mostra por que a primeira pergunta importa:</p>
{diagrama_frase([('Fīlia', 'antecedente possível · f. sing.'), ('agricolae', 'antecedente possível · m. sing.'), ('quem', 'relativo · m. sing. · ac.'), ('vidēs', 'verbo da relativa'), ('mea est', 'verbo da principal')],
    '<i>Fīlia agricolae [quem vidēs] mea est</i> = A filha do agricultor que você vê é minha. <i>Quem</i> é masculino: retoma <i>agricolae</i>, não <i>fīlia</i>; você vê o agricultor.')}
<p>Em português, "a filha do agricultor que você vê" é ambíguo: quem você vê, a filha ou o agricultor? Em latim não há ambiguidade. <i>Agricola</i> é masculino (nome de homem, apesar da primeira declinação), e <i>quem</i> é masculino; se o relativo se referisse à filha, seria <i>quam</i>. O caso, acusativo, vem de <i>vidēs</i> e nada tem a ver com o genitivo <i>agricolae</i>.</p>
<p>O relativo concorda também em <b>pessoa</b> (Bennett § 250.1; Kennedy § 195): se o antecedente é "eu" ou "você", o verbo da relativa vai para a primeira ou a segunda pessoa, como em português culto. Kennedy dá o exemplo <i>Amō tē, māter, quae mē amās</i>, "amo-te, mãe, que me amas"; e a oração que milhões de pessoas rezam em latim começa assim:</p>
{exemplos([('Pater noster, <b>quī es</b> in caelīs …', 'Pai nosso, que estás nos céus … (Mt 6,9; <i>quī</i>: nom. sing. m., concorda com <i>Pater</i>; <i>es</i>, 2ª pessoa, porque o antecedente é a pessoa a quem se fala)')])}
{observacao('Cuius não é "cujo"', 'O português "cujo" concorda com a coisa possuída: "a menina cujo pai", "a menina cujas rosas". O latim <i>cuius</i> não concorda com a coisa possuída, porque é um genitivo: toma o gênero e o número do <b>possuidor</b> (o antecedente) e fica no genitivo. Por isso <i>puella cuius patrem vidēs</i> e <i>puella cuius rosās vidēs</i> usam o mesmo <i>cuius</i>; e com antecedente plural usa-se <i>quōrum</i> ou <i>quārum</i>: <i>puellae quārum patrem vidēs</i>, "as meninas cujo pai você vê".')}
'''),
        ('Onde está o antecedente', f'''
<p>Até aqui o antecedente estava sempre escrito, logo antes do relativo. Nos textos, três outras situações são frequentes, e todas se resolvem com a mesma regra.</p>
<h3>1. Antecedente omitido</h3>
<p>Quando o antecedente é uma pessoa qualquer, indefinida, o latim muitas vezes não o escreve (Bennett § 251.1; Allen e Greenough § 307 c). <i>Quī</i> sozinho significa então "quem, aquele que"; <i>quae</i> neutro plural, "as coisas que, o que". É o mesmo "quem" do português "quem espera sempre alcança". O gênero e o número do relativo dizem que tipo de antecedente se subentende: masculino, uma pessoa; neutro, uma coisa.</p>
{exemplos([('<b>Quī</b> bene labōrat, bene vīvit.', 'Quem trabalha bem vive bem. (antecedente subentendido: "aquele"; <i>bene</i>, bem)'),
           ('<b>Quī</b> nātūram sequitur sapiēns est.', 'Quem segue a natureza é sábio. (Bennett § 251.1; <i>sequitur</i>, segue)'),
           ('Omnis <b>quī</b> est ex vēritāte, audit vōcem meam.', 'Todo aquele que é da verdade ouve a minha voz. (Jo 18,37; aqui o antecedente é o adjetivo substantivado <i>omnis</i>, "todo aquele")')])}
<h3>2. Is … quī: o antecedente demonstrativo</h3>
<p>Quando é preciso dar ao antecedente um caso na principal, o latim o explicita com o demonstrativo fraco do capítulo 15: <i>is quī</i>, "aquele que"; <i>ea quae</i>, "aquela que" ou "as coisas que"; <i>id quod</i>, "aquilo que, o que" (Bennett § 247.1). Cada um dos dois pronomes tem o seu caso, o da sua oração; só o gênero e o número coincidem.</p>
{exemplos([('Laudō <b>eum quī</b> labōrat.', 'Elogio aquele que trabalha. (<i>eum</i>: objeto de <i>laudō</i>; <i>quī</i>: sujeito de <i>labōrat</i>)'),
           ('<b>Id quod</b> dīcis vērum est.', 'O que você diz é verdade. (<i>id</i>: sujeito de <i>est</i>; <i>quod</i>: objeto de <i>dīcis</i>; <i>vērus</i>, verdadeiro)'),
           ('Nōn amō <b>eōs quī</b> semper rīdent.', 'Não gosto dos que estão sempre rindo. (<i>semper</i>, sempre; <i>rīdent</i>, riem)')])}
<h3>3. A relativa antes da principal</h3>
<p>Em latim cuidado e enfático, a oração relativa vem muitas vezes <b>antes</b> da principal, e a principal retoma o antecedente com um demonstrativo, quase sempre <i>is</i> ou <i>hīc</i> (Allen e Greenough §§ 307 b e 308 d; Bennett § 251.4). Às vezes o próprio nome antecedente fica dentro da relativa. A ordem portuguesa natural é inverter: começar pela principal.</p>
{exemplos([('… <b>quae</b> audīvī ab eō, <b>haec</b> loquor in mundō.', '… o que ouvi dele, isto falo ao mundo. (Jo 8,26; <i>audīvī</i>, perfeito de <i>audiō</i>, capítulo 13; <i>loquor</i>, falo, verbo depoente, capítulo 25)'),
           ('<b>Quem</b> librum legis, <b>eum</b> ego quoque legō.', 'Leio também o livro que você lê. (o nome <i>librum</i> está dentro da relativa; <i>quoque</i>, também)')])}
<p>Repare que em nenhuma dessas construções o relativo desaparece. O inglês às vezes o dispensa (<i>the book you gave me</i>); o português e o latim, nunca: "o livro que você me deu", <i>liber quem mihi dedistī</i> (Bennett § 251.5; Allen e Greenough § 308 a).</p>
'''),
        ('O relativo de ligação: quī = et is', f'''
<p>Uma das construções mais características da prosa latina, e uma das que mais confundem quem começa a ler textos autênticos, é o relativo no <b>início de uma frase</b>, depois de ponto ou de ponto e vírgula, retomando algo da frase anterior. Ele não introduz uma oração subordinada: liga duas frases independentes, e equivale a um demonstrativo com "e" ou "mas" (Bennett § 251.6; Allen e Greenough §§ 303 e 308 f). <i>Quī</i> vale <i>et is</i>, "e ele"; <i>quem</i> vale <i>et eum</i>, "e o"; <i>quod</i> vale <i>et id</i>, "e isso".</p>
{exemplos([('Magister puerīs fābulam nārrat. <b>Quam</b> puerī libenter audiunt.', 'O mestre conta uma história aos meninos. E os meninos a ouvem com gosto. (<i>quam</i> = <i>et eam</i>; <i>libenter</i>, com gosto)'),
           ('Rēx epistulam scrībit. <b>Quam</b> mīles ad ducem portat.', 'O rei escreve uma carta. O soldado a leva ao general. (<i>portat</i>, leva)'),
           ('<b>Quō</b> factum est …', 'Por isso aconteceu … (expressão citada por Bennett § 251.6; <i>quō</i> = "por isto", ablativo)')])}
<p>Traduzir esses relativos por "que" ou "o qual" produz um português pesado e, às vezes, sem sentido. A tradução natural usa um pronome pessoal ou demonstrativo, com ou sem "e": "e ele", "este", "isso". Para reconhecê-los, basta notar que não há, na mesma frase, uma oração principal a que a relativa se prenda: o antecedente ficou na frase anterior. A regra de concordância continua valendo: <i>quam</i> é feminino singular porque retoma <i>fābulam</i> ou <i>epistulam</i>, e acusativo porque é o objeto de <i>audiunt</i> ou <i>portat</i>.</p>
<p>No capítulo 17 você vai ler um diálogo do Gênesis em que Caim responde a uma pergunta de Deus; a resposta começa por <i>Quī respondit</i>, "e ele respondeu", com um relativo de ligação. Cícero e César usam a construção com muita frequência, muitas vezes em fórmulas como <i>quae cum ita sint</i>, "e, sendo assim" (Allen e Greenough § 303), que você poderá analisar inteiras depois do capítulo 34.</p>
'''),
        ('Análise gramatical: Mt 10,40', f'''
<p>No discurso de missão aos doze apóstolos, no Evangelho de Mateus, há um versículo que é quase um exercício sobre o relativo: três orações relativas, duas com antecedente omitido e uma com <i>is … quī</i>:</p>
{exemplos([('Quī recipit vōs, mē recipit: et quī mē recipit, recipit eum quī mē mīsit.', 'Quem vos recebe, a mim recebe; e quem me recebe, recebe aquele que me enviou. (Mt 10,40, Vulgata Clementina)')])}
{analise('Mt 10,40, palavra a palavra', [
    ('Quī', 'quī, quae, quod, que', 'nominativo singular masculino; antecedente omitido ("quem")', 'sujeito de <i>recipit</i> na relativa; a relativa inteira é sujeito da principal'),
    ('recipit', 'recipiō, -ere, receber (3ª em -iō, como <i>capiō</i>)', '3ª pessoa do singular do presente', 'verbo da primeira relativa'),
    ('vōs', 'vōs, vós, vocês', 'acusativo plural', 'objeto de <i>recipit</i>'),
    ('mē', 'ego, eu', 'acusativo singular', 'objeto do segundo <i>recipit</i>, posto em destaque antes do verbo'),
    ('recipit', 'recipiō, -ere', '3ª pessoa do singular do presente', 'verbo da principal'),
    ('et quī mē recipit', '(as mesmas palavras)', 'relativa com antecedente omitido, como a primeira', 'sujeito do <i>recipit</i> seguinte'),
    ('recipit', 'recipiō, -ere', '3ª pessoa do singular do presente', 'verbo da segunda principal'),
    ('eum', 'is, ea, id, ele, aquele', 'acusativo singular masculino', 'objeto de <i>recipit</i>; antecedente do último <i>quī</i>'),
    ('quī', 'quī, quae, quod', 'nominativo singular masculino', 'concorda com <i>eum</i> em gênero e número; nominativo porque é o sujeito de <i>mīsit</i>'),
    ('mē', 'ego', 'acusativo singular', 'objeto de <i>mīsit</i>'),
    ('mīsit', 'mittō, -ere, mīsī, missum, enviar', '3ª pessoa do singular do perfeito (capítulo 13)', 'verbo da última relativa: "enviou"'),
])}
<p>O versículo mostra as três coisas mais importantes deste capítulo. Primeiro, o antecedente omitido: os dois primeiros <i>quī</i> não têm antecedente escrito; são "quem", e cada relativa inteira funciona como sujeito do verbo seguinte. Segundo, o par <i>eum quī</i>: o demonstrativo está no acusativo, porque é objeto de <i>recipit</i>, e o relativo no nominativo, porque é sujeito de <i>mīsit</i>; os dois são masculinos e singulares, porque se referem à mesma pessoa. É a regra de ouro em estado puro: gênero e número em comum, casos independentes. Terceiro, os colchetes: <i>[Quī recipit vōs], mē recipit: et [quī mē recipit], recipit eum [quī mē mīsit]</i>. Fora dos colchetes sobram duas frases curtíssimas, "recebe a mim" e "recebe aquele".</p>
<p>A tradução portuguesa pode seguir o latim de perto, porque o português tem o mesmo "quem" sem antecedente. Repare também na ordem: <i>mē recipit</i>, com o objeto antes do verbo, põe em destaque o "a mim", em contraste com o <i>vōs</i> da relativa; a tradução "a mim recebe" conserva o efeito.</p>
<h3>Resumo</h3>
<ul>
<li><i>Quī, quae, quod</i>: genitivo <i>cuius</i> e dativo <i>cui</i> nos três gêneros; plural <i>quī, quae, quae; quōrum, quārum, quōrum; quibus; quōs, quās, quae; quibus</i>. Com <i>cum</i>: <i>quōcum, quācum, quibuscum</i>.</li>
<li>Regra de ouro: gênero e número do antecedente (e a pessoa, para o verbo); caso da função dentro da relativa.</li>
<li>Delimite a relativa do relativo até o seu verbo; o que sobra é a principal.</li>
<li>Antecedente omitido: <i>quī</i> = "quem"; <i>quae</i> (n. pl.) = "o que". Antecedente demonstrativo: <i>is quī</i>, <i>id quod</i>. Relativa anteposta: <i>quae …, haec …</i>.</li>
<li>Relativo no início da frase, sem principal a que se prender: relativo de ligação, <i>quī</i> = <i>et is</i>; traduza por "e ele", "este".</li>
</ul>
<p>O capítulo 17 apresenta os parentes próximos do relativo: o interrogativo <i>quis? quid?</i> e o adjetivo interrogativo <i>quī? quae? quod?</i>, que tem exatamente as mesmas formas que você acabou de aprender, e os indefinidos.</p>
'''),
    ],
    erros_comuns=[
        ('Pôr o relativo no caso do antecedente: *<i>Puella quae laudās</i> para "a menina que você elogia".', 'O caso vem da função <b>dentro</b> da relativa. A menina é objeto de <i>laudās</i>: <i>puella quam laudās</i>. Do antecedente o relativo copia só o gênero e o número. Pergunte: o que o relativo faz no seu próprio verbo?'),
        ('Ler <i>quae</i> sempre como feminino singular.', '<i>Quae</i> pode ser nominativo singular feminino, nominativo plural feminino ou nominativo e acusativo plural neutro. Em <i>verba quae dīcis</i>, é neutro plural (concorda com <i>verba</i>) e acusativo (objeto de <i>dīcis</i>). O antecedente decide o gênero e o número; a relativa, o caso.'),
        ('Fazer <i>cuius</i> concordar com a coisa possuída, como o "cujo" português: *<i>puella cuiam rosam</i>.', '<i>Cuius</i> é genitivo do relativo e não varia com a coisa possuída. Varia com o antecedente: <i>puer cuius</i>, <i>puella cuius</i> (singular); <i>puerī quōrum</i>, <i>puellae quārum</i> (plural). "A menina cujas rosas você vê" = <i>puella cuius rosās vidēs</i>.'),
        ('Ligar o relativo ao nome mais próximo sem conferir gênero e número.', 'O antecedente costuma vir perto, mas não necessariamente imediatamente antes. Em <i>fīlia agricolae quem vidēs</i>, <i>quem</i> (m.) retoma <i>agricolae</i> (m.); em <i>fīlia agricolae quam vidēs</i>, <i>quam</i> (f.) retoma <i>fīlia</i>. É justamente o que o latim permite distinguir e o português não.'),
        ('Traduzir o relativo de ligação por "que" ou "o qual": <i>Quam puerī audiunt</i> → *"a qual os meninos ouvem."', 'No início de frase, sem oração principal a que se prender, o relativo equivale a <i>et is</i>: "e os meninos a ouvem", "os meninos ouvem-na". Traduza por pronome pessoal ou demonstrativo, com ou sem "e".'),
        ('Confundir o relativo <i>quod</i> com a conjunção <i>quod</i>, "porque, o fato de que".', 'O relativo <i>quod</i> é neutro singular e tem antecedente (expresso, como <i>id</i> ou <i>templum</i>, ou subentendido, "o que") e uma função na sua oração. A conjunção não tem antecedente nem função: a oração que ela introduz já está completa. A conjunção é tratada no capítulo 37; por ora, se não achar antecedente neutro nem função para <i>quod</i>, desconfie de que seja ela.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Cuius e os colchetes',
            'Analise e traduza: <i lang="la">Mīles cuius gladium vidēs frāter meus est.</i> Vocabulário: <i>gladius, -ī</i> (m.), espada; <i>frāter, frātris</i> (m.), irmão.', [
            ('Onde começa e onde termina a relativa?', 'Começa em <i>cuius</i> e termina no seu verbo, <i>vidēs</i>: <i>Mīles [cuius gladium vidēs] frāter meus est</i>.'),
            ('Leia a principal, fora dos colchetes.', '<i>Mīles … frāter meus est</i>: "o soldado é meu irmão".'),
            ('Qual o antecedente de <i>cuius</i>, e como você sabe?', '<i>Cuius</i> é genitivo singular, de qualquer gênero; o antecedente é um nome singular antes dele: <i>mīles</i>. É o único possível.'),
            ('Que função <i>cuius</i> exerce na relativa?', 'Possuidor de <i>gladium</i>: "a espada do qual", "cuja espada". <i>Gladium</i> é o objeto de <i>vidēs</i>.'),
            ('Monte a tradução.', '"O soldado cuja espada você vê é meu irmão."'),
        ]),
        pratica_guiada('Prática guiada 2 · Um relativo no começo da frase',
            'Traduza o par de frases: <i lang="la">Pater fīliō librum dat. Quem fīlius statim legit.</i> Vocabulário: <i>statim</i>, imediatamente.', [
            ('A segunda frase tem uma oração principal a que <i>quem</i> se prenda?', 'Não: <i>quem fīlius statim legit</i> é tudo o que há. O relativo está no início da frase, depois de ponto: é um relativo de ligação.'),
            ('A que se refere <i>quem</i>?', 'A um nome masculino singular da frase anterior: <i>librum</i> (também <i>fīliō</i> é masculino singular, mas <i>fīlius</i> é o sujeito de <i>legit</i>, e ninguém lê a si mesmo). E é acusativo porque é o objeto de <i>legit</i>.'),
            ('Como traduzir <i>quem</i>?', 'Como <i>et eum</i>: "e o filho o lê imediatamente", ou "o filho lê-o logo".'),
            ('Monte a tradução das duas frases.', '"O pai dá um livro ao filho. E o filho o lê imediatamente."'),
        ], 'Conclusão: relativo no começo da frase, sem principal ao lado, retoma algo da frase anterior; traduza-o por pronome pessoal ou demonstrativo.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Reconheça as formas', 'Dê todas as possibilidades de caso, número e gênero de cada forma do relativo.', [
            ('<i>cuius</i>', 'Genitivo singular, três gêneros.'),
            ('<i>cui</i>', 'Dativo singular, três gêneros.'),
            ('<i>quae</i>', 'Nominativo singular feminino; nominativo plural feminino; nominativo ou acusativo plural neutro.'),
            ('<i>quō</i>', 'Ablativo singular masculino ou neutro.'),
            ('<i>quibus</i>', 'Dativo ou ablativo plural, três gêneros.'),
            ('<i>quod</i>', 'Nominativo ou acusativo singular neutro.'),
            ('<i>quōs</i>', 'Acusativo plural masculino.'),
            ('<i>quārum</i>', 'Genitivo plural feminino.'),
            ('<i>quī</i>', 'Nominativo singular ou plural masculino.'),
            ('<i>quam</i>', 'Acusativo singular feminino.'),
        ]),
        exercicio('Exercício 2 · Complete com o relativo', 'Escreva a forma certa de <i>quī, quae, quod</i> e explique o gênero, o número e o caso. Vocabulário: <i>habitō, -āre</i>, morar; <i>dīcit</i>, diz.', [
            ('<i>Puer ___ vidēs fīlius meus est.</i>', '<i>quem</i>: masculino singular (de <i>puer</i>); acusativo, objeto de <i>vidēs</i>.'),
            ('<i>Puella ___ librum dō laeta est.</i>', '<i>cui</i>: feminino singular (de <i>puella</i>); dativo, a quem dou o livro.'),
            ('<i>Mīlitēs ___ dux laudat fortēs sunt.</i>', '<i>quōs</i>: masculino plural; acusativo, objeto de <i>laudat</i> (o sujeito da relativa é <i>dux</i>).'),
            ('<i>Templum ___ vidēmus antīquum est.</i>', '<i>quod</i>: neutro singular; acusativo, objeto de <i>vidēmus</i>.'),
            ('<i>Fēminae ___ fīliī labōrant in oppidō habitant.</i>', '<i>quārum</i>: feminino plural (de <i>fēminae</i>); genitivo, possuidoras de <i>fīliī</i>: "as mulheres cujos filhos trabalham".'),
            ('<i>Verba ___ magister dīcit vēra sunt.</i>', '<i>quae</i>: neutro plural; acusativo, objeto de <i>dīcit</i>.'),
            ('<i>Oppidum in ___ habitāmus parvum est.</i>', '<i>quō</i>: neutro singular; ablativo com <i>in</i>, lugar onde: "a cidade em que moramos".'),
            ('<i>Amīcus ___ ambulō Mārcus est.</i> ("com quem passeio")', '<i>quōcum</i>: masculino singular; ablativo de companhia, com <i>cum</i> posposto.'),
        ]),
        exercicio('Exercício 3 · Junte as duas frases', 'Transforme a segunda frase numa oração relativa ligada à primeira, como no modelo do início do capítulo, e traduza.', [
            ('<i>Puella rosās amat. Puella in hortō est.</i> (relativa a partir da primeira)', '<i>Puella quae rosās amat in hortō est.</i> "A menina que ama as rosas está no jardim." <i>Quae</i>: f. sing., nominativo (sujeito de <i>amat</i>).'),
            ('<i>Magistrum laudāmus. Magister puerōs docet.</i>', '<i>Magistrum quī puerōs docet laudāmus.</i> "Elogiamos o mestre que ensina os meninos." O antecedente está no acusativo, mas <i>quī</i> fica no nominativo: é sujeito de <i>docet</i>.'),
            ('<i>Agricola equum habet. Fīlius agricolae equum amat.</i>', '<i>Agricola equum habet quem fīlius eius amat.</i> "O agricultor tem um cavalo que o filho dele ama." <i>Quem</i>: m. sing., acusativo.'),
            ('<i>Mīles fortis est. Rēx mīlitī dōnum dat.</i>', '<i>Mīles cui rēx dōnum dat fortis est.</i> "O soldado a quem o rei dá um presente é corajoso." <i>Cui</i>: dativo.'),
            ('<i>Poēta carmina scrībit. Nōmen poētae clārum est.</i>', '<i>Poēta cuius nōmen clārum est carmina scrībit.</i> "O poeta cujo nome é famoso escreve poemas." <i>Cuius</i>: genitivo, masculino porque o poeta é homem.'),
        ]),
        exercicio('Exercício 4 · Traduza', 'Delimite as relativas com colchetes antes de traduzir. Vocabulário: <i>bene</i>, bem; <i>vērus, -a, -um</i>, verdadeiro; <i>dīcis</i>, dizes; <i>rīdent</i>, riem; <i>semper</i>, sempre.', [
            ('<i>Quī bene labōrat, bene vīvit.</i>', '[Quī bene labōrat], bene vīvit: "Quem trabalha bem vive bem." Antecedente omitido.'),
            ('<i>Id quod dīcis vērum est.</i>', 'Id [quod dīcis] vērum est: "O que você diz é verdade." <i>Id</i> é sujeito de <i>est</i>; <i>quod</i>, objeto de <i>dīcis</i>.'),
            ('<i>Nōn amō eōs quī semper rīdent.</i>', 'Nōn amō eōs [quī semper rīdent]: "Não gosto daqueles que estão sempre rindo." <i>Eōs</i> é acusativo; <i>quī</i>, nominativo plural.'),
            ('<i>Ego, quī tē amō, tibi librum dō.</i>', 'Ego, [quī tē amō], tibi librum dō: "Eu, que te amo, te dou um livro." O verbo da relativa está na 1ª pessoa (<i>amō</i>) porque o antecedente é <i>ego</i>.'),
            ('<i>Vōs, quī in agrīs labōrātis, fortēs estis.</i>', 'Vōs, [quī in agrīs labōrātis], fortēs estis: "Vós, que trabalhais nos campos, sois fortes." <i>Quī</i> é plural, e o verbo vai para a 2ª pessoa do plural.'),
            ('<i>Quem librum legis, eum ego quoque legō.</i> (<i>quoque</i>, também)', '[Quem librum legis], eum ego quoque legō: "O livro que você lê eu também leio." A relativa vem antes, com o nome dentro dela; <i>eum</i> o retoma na principal.'),
        ]),
        exercicio('Exercício 5 · Relativo de ligação', 'Traduza cada par de frases com um pronome pessoal ou demonstrativo no lugar do relativo inicial. Vocabulário: <i>salūtō, -āre</i>, cumprimentar; <i>in viā</i>, na rua; <i>gaudet</i>, alegra-se (com ablativo).', [
            ('<i>Puerī in viā magistrum vident. Quem statim salūtant.</i>', '"Os meninos veem o mestre na rua. E logo o cumprimentam." <i>Quem</i> = <i>et eum</i>: m. sing. (de <i>magistrum</i>), acusativo (objeto de <i>salūtant</i>).'),
            ('<i>Pater fīliō librum dat. Quō librō fīlius gaudet.</i>', '"O pai dá um livro ao filho. O filho se alegra com esse livro." <i>Quō librō</i>: o nome é repetido junto do relativo (Bennett § 251.3); ablativo, pedido por <i>gaudet</i>.'),
            ('<i>Rēgīna epistulam scrībit. Quam mīles ad ducem portat.</i> (<i>rēgīna, -ae</i>, rainha; <i>portat</i>, leva)', '"A rainha escreve uma carta. O soldado a leva ao general." <i>Quam</i>: f. sing. (de <i>epistulam</i>), acusativo.'),
        ]),
        exercicio('Exercício 6 · Leitura de dois versículos', 'Jo 18,37 e 8,26, Vulgata Clementina (macrons acrescentados): (a) <i lang="la">Omnis quī est ex vēritāte, audit vōcem meam.</i> (b) <i lang="la">… quae audīvī ab eō, haec loquor in mundō.</i> Vocabulário: <i>omnis</i>, todo (capítulo 10); <i>vēritās, -ātis</i> (f.), verdade; <i>ex</i> + abl., de; <i>audīvī</i>, ouvi (perfeito); <i>ab eō</i>, dele, da parte dele; <i>loquor</i>, falo; <i>mundus, -ī</i>, mundo.', [
            ('Em (a), qual o antecedente de <i>quī</i>, e qual a sua função?', 'O antecedente é <i>omnis</i>, usado como substantivo ("todo aquele"), masculino singular. <i>Quī</i> é nominativo porque é o sujeito de <i>est</i>, dentro da relativa.'),
            ('Em (a), qual é o verbo da principal, e qual o seu sujeito?', '<i>Audit</i>; o sujeito é <i>omnis</i> (com a relativa que o acompanha). <i>Vōcem meam</i> é o objeto.'),
            ('Em (b), por que <i>quae</i> é neutro plural, se não há antecedente antes dele?', 'Porque a relativa vem antes da principal e o antecedente aparece depois, em <i>haec</i> (neutro plural, "estas coisas"). O neutro plural sem nome designa coisas: "as coisas que ouvi". <i>Quae</i> é acusativo, objeto de <i>audīvī</i>.'),
            ('Traduza as duas frases.', '(a) "Todo aquele que é da verdade ouve a minha voz." (b) "O que ouvi dele, isto falo ao mundo." Ou, na ordem portuguesa: "Falo ao mundo o que ouvi dele."'),
        ]),
    ],
    leituras=['lhomond-epitome-historiae-sacrae', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'nutting-a-first-latin-reader', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'd-ooge-latin-for-beginners', 'bennett-new-latin-grammar'],
    leituras_nota='O Epitome Historiae Sacrae, de Lhomond, e A First Latin Reader, de Nutting, contam histórias em frases curtas, com muitos relativos de ligação no começo das frases: leia algumas páginas pondo cada relativa entre colchetes. Na Vulgata, leia Mt 10,37–42, em que quase todo versículo começa por quī, e o capítulo 18 de João. Familia Romana e Latin for Beginners, de D\'Ooge, praticam a regra de concordância de forma graduada. Bennett (§§ 250–251) é a referência para consultar os casos particulares.',
)
