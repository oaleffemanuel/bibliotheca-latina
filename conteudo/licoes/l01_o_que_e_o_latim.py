from conteudo.util import (tabela, exemplos, dica, diagrama, diagrama_frase, exercicio, svg_caixas, referencia,
                           pratica_guiada, analise, observacao)

LICAO = dict(
    slug='01-o-que-e-o-latim', titulo='O que é o latim?', titulo_latim='Dē linguā Latīnā', tempo='45 min',
    resumo='De onde vem a língua que você vai aprender, por que ela está mais perto do português do que parece, e como pronunciá-la desde o primeiro dia.',
    status='publicada',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['história da língua latina', 'latim e português', 'alfabeto', 'i/j e u/v', 'pronúncia restaurada e eclesiástica', 'divisão silábica', 'quantidade vocálica e silábica', 'acento tônico', 'leitura em voz alta de frase autêntica'],
    prerequisitos=dict(texto='Nenhum. Este é o primeiro capítulo.', licoes=[]),
    referencias=[referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 1 (alfabeto), §§ 2–5 (classificação dos sons; i e u consoantes), § 7 (divisão silábica), § 8 (pronúncia restaurada), §§ 9–11 (quantidade da vogal e da sílaba), § 12 (acento)', tipo='dominio_publico'),
                 referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='Introdução, § 3 (períodos da língua); §§ 1–3 (alfabeto e pronúncia), § 4 (sílabas), § 5 (quantidade), § 6 (acento)', tipo='dominio_publico'),
                 referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 4 (quantidade das vogais), § 9 (acento)', tipo='dominio_publico'),
                 referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='cap. 1, nn. 1–6 (alfabeto, escrita e pronúncia, quantidade, acento)', tipo='dominio_publico'),
                 referencia('Commentarii de Bello Gallico, 1.1.1', 'Gaius Iulius Caesar', catalogo='caesar-commentarii-de-bello-gallico-selecoes', nota='frase da prática guiada 2; texto conferido na ed. T. Rice Holmes (Oxford, 1914), via Perseus', tipo='dominio_publico'),
                 referencia('Biblia Sacra Vulgata (editio Clementina), Mt 6,9', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', nota='frase autêntica lida e analisada na seção 5', tipo='dominio_publico'),
                 referencia('The Liber Usualis, with introduction and rubrics in English', 'Monges de Solesmes (ed.)', url='https://archive.org/details/liber-usualis-1949-digital', nota='ed. Desclée, 1949: introdução, cap. IX, "The reading and pronunciation of liturgical Latin" (pronúncia romana; o h soa "k" em mihi e nihil, grafados michi e nichil nos livros antigos; em todos os outros casos é mudo)', tipo='obra'),
                 referencia('Vox Latina: a guide to the pronunciation of classical Latin', 'W. Sidney Allen', nota='obra de referência sobre a pronúncia restaurada (não está no catálogo; edição comercial)', tipo='obra')],
    objetivos=[
        'Situar o latim no tempo: períodos, autores e por que ele nunca "morreu" de verdade.',
        'Reconhecer o parentesco entre latim e português e usar isso a seu favor.',
        'Conhecer o alfabeto latino e as duas pronúncias em uso (restaurada e eclesiástica).',
        'Dividir uma palavra em sílabas, dizer se a penúltima é longa ou breve e aplicar a regra do acento.',
        'Ler em voz alta, com o acento certo, uma frase autêntica curta.',
    ],
    secoes=[
        ('Uma língua, muitas épocas', f'''
<p>O latim é a língua do <i>Latium</i>, a região da Itália central onde fica Roma. Começou como o falar de uma cidade pequena e, com a expansão romana, tornou-se a língua de todo o Mediterrâneo ocidental: da administração, do exército, das escolas e, mais tarde, da Igreja. Durante mais de dois mil anos foi escrito sem interrupção, e é por isso que se costuma dividi-lo em períodos.</p>
{diagrama(svg_caixas([('Arcaico', 'até c. 80 a.C.'), ('Clássico', 'séc. I a.C. – I d.C.'), ('Tardio', 'séc. II – VI'), ('Medieval', 'séc. VII – XIV'), ('Neolatino', 'séc. XV em diante')]), 'Os grandes períodos do latim escrito. As datas são aproximadas: as mudanças foram graduais.')}
<ul>
<li><b>Latim clássico</b> (Cícero, César, Virgílio, Ovídio, Tito Lívio): o latim literário que as gramáticas tomam como modelo. É o padrão que você estuda, mas não é o único latim.</li>
<li><b>Latim tardio e patrístico</b> (Jerônimo, Agostinho, a Vulgata): o latim da Igreja antiga, de frases mais curtas e vocabulário mais próximo do que viria a ser o português.</li>
<li><b>Latim medieval</b> (Beda, Anselmo, Tomás de Aquino): a língua internacional das universidades, da filosofia e das crônicas. Simples na sintaxe, técnico no vocabulário.</li>
<li><b>Neolatim</b> (Erasmo, Descartes, Newton): o latim dos humanistas e da ciência moderna, que imita de propósito o modelo clássico.</li>
</ul>
<p>Nenhum desses latins é "pior" ou "mais difícil" que outro. Nesta biblioteca, as etapas VI (<i>Latinitas Christiana</i>) e VII (<i>Sapientia Mediaevalis</i>) são caminhos paralelos ao clássico, não degraus acima dele.</p>
<h3>O latim morreu?</h3>
<p>Não exatamente: ele mudou de nome. O latim falado pelo povo (<i>sermo vulgaris</i>) continuou se transformando até virar o português, o espanhol, o italiano, o francês, o romeno e outras línguas. O português é, literalmente, o latim de Portugal depois de dois mil anos de mudanças. Ao aprender latim, você está lendo a versão mais antiga da sua própria língua.</p>
'''),
        ('O latim que você já sabe', f'''
<p>Para quem fala português, o vocabulário latino é a parte mais fácil. Boa parte das palavras mais frequentes do latim tem um parente direto em português, muitas vezes transparente:</p>
{tabela(['Latim', 'Português', 'Observação'], [
    ['aqua', 'água', ''], ['terra', 'terra', ''], ['vīta', 'vida', 't entre vogais virou d'], ['lūna', 'lua', 'o n entre vogais caiu'],
    ['pater', 'pai', 'do acusativo <i>patrem</i>'], ['māter', 'mãe', ''], ['fīlius', 'filho', 'li + vogal virou lh'], ['amīcus', 'amigo', 'c entre vogais virou g'],
    ['nox (noctem)', 'noite', 'ct virou it'], ['octō', 'oito', 'ct virou it'], ['caelum', 'céu', ''], ['manus', 'mão', ''],
    ['dīcere', 'dizer', ''], ['facere', 'fazer', ''], ['venīre', 'vir', ''], ['bonus', 'bom', ''],
], 'Parentes diretos: o som mudou com regularidade', latim_cols=(0,))}
<p>Repare nas regularidades: <i>t</i> entre vogais vira <i>d</i> (<i>vīta</i> → vida, <i>rota</i> → roda); <i>c</i> entre vogais vira <i>g</i> (<i>amīcus</i> → amigo, <i>lacus</i> → lago); <i>ct</i> vira <i>it</i> (<i>noctem</i> → noite, <i>factum</i> → feito); <i>l</i> e <i>n</i> entre vogais costumam cair (<i>cael(um)</i>, <i>lū(n)a</i>). Quando você souber essas correspondências, muitas palavras novas vão se "traduzir sozinhas".</p>
{dica('<b>Cuidado com os falsos amigos.</b> Nem toda semelhança é sinônimo: <i>vīlla</i> é uma casa de campo, não uma vila; <i>hostis</i> é inimigo (hóspede é <i>hospes</i>); <i>virtūs</i> é coragem antes de ser virtude; <i>familia</i> inclui os escravos da casa. Você vai conhecer os principais ao longo do curso.')}
<p>A dificuldade do latim não está nas palavras, mas na <b>forma</b> delas: a mesma palavra muda de terminação conforme a função na frase. É disso que tratam os próximos capítulos.</p>
'''),
        ('O alfabeto e os sons', f'''
<p>O alfabeto latino clássico tinha 23 letras: <span class="lat">A B C D E F G H I K L M N O P Q R S T V X Y Z</span>. Não havia <i>J</i>, <i>U</i> nem <i>W</i>: a letra <i>I</i> servia tanto para a vogal quanto para a consoante (<i>Iūlius</i> = "Júlio"), e <i>V</i> para a vogal <i>u</i> e para a consoante (<i>VENI</i> = <i>venī</i>). As edições modernas costumam escrever <i>u</i> para a vogal e <i>v</i> para a consoante; algumas também usam <i>j</i>. <i>K</i> é raríssimo; <i>Y</i> e <i>Z</i> só aparecem em palavras gregas. (Algumas gramáticas escolares, como a do Pe. Ravizza, contam 24 letras porque já incluem o <i>U</i> moderno; a diferença é de convenção, não de língua.)</p>
<p>Hoje existem duas maneiras correntes de pronunciar o latim. As duas são legítimas; escolha uma e seja consistente.</p>
<ul>
<li><b>Pronúncia restaurada</b> (ou clássica): a reconstrução de como se falava em Roma no século I a.C. É o padrão nas universidades e nos áudios de textos clássicos.</li>
<li><b>Pronúncia eclesiástica</b> (ou romana): a da Igreja Católica, muito próxima do italiano. É a da liturgia, dos hinos e de muitas gravações de textos cristãos. Soa natural para brasileiros.</li>
</ul>
{tabela(['Grafia', 'Restaurada', 'Eclesiástica', 'Exemplo'], [
    ['c', 'sempre /k/, como em "casa"', '/tch/ antes de e, i, ae, oe; /k/ nos outros casos', '<i>Cicerō</i>: "Kíkero" · "Tchítchero"'],
    ['g', 'sempre /g/, como em "gato"', '/dj/ antes de e, i; /g/ nos outros casos', '<i>genus</i>: "guénus" · "djénus"'],
    ['v', '/w/, como o u de "quase"', '/v/', '<i>vīta</i>: "uíta" · "víta"'],
    ['ae, oe', 'ditongos "ai", "oi"', '/e/ aberto', '<i>Caesar</i>: "Káissar" · "Tchéssar"'],
    ['ti + vogal', '/ti/', '/tsi/ (exceto após s, t, x)', '<i>grātia</i>: "grátia" · "grátsia"'],
    ['gn', '/gn/ (como em "digno")', '/nh/', '<i>agnus</i>: "ágnus" · "ánhus"'],
    ['h', 'aspirado leve, como em inglês', 'mudo (exceto em <i>mihi</i> e <i>nihil</i>: ver abaixo)', '<i>homō</i>: "hómo" · "ómo"'],
    ['sc + e, i', '/sk/', '/ch/', '<i>scientia</i>: "skiéntia" · "chiéntsia"'],
    ['qu', '/ku/', '/ku/', '<i>aqua</i>: "ákua" nas duas'],
    ['r', 'vibrante, como o "r" de "caro"', 'igual', '<i>Rōma</i>: "Rôma" (nunca como o "r" carioca)'],
], 'As diferenças que importam entre as duas pronúncias')}
<p>Uma exceção da pronúncia eclesiástica merece nota. Nas regras do <i>Liber Usualis</i>, o livro de canto da liturgia romana editado pelos monges de Solesmes, o <i>h</i> é mudo em toda parte, menos em <i>mihi</i> ("a mim") e <i>nihil</i> ("nada"), que se pronunciam "míki" e "níkil". As grafias medievais <i>michi</i> e <i>nichil</i>, frequentes nos manuscritos, refletem essa pronúncia. É a norma da tradição romana tal como a codificaram os livros litúrgicos do século XX, não uma regra universal: muitos cantores e escolas dizem simplesmente "mi-i" e "ní-il". Na pronúncia restaurada, o <i>h</i> dessas palavras é só uma aspiração leve.</p>
<p>Nas duas pronúncias, as vogais são "puras", como no espanhol: <i>e</i> e <i>o</i> não se fecham em ditongo, e as vogais átonas não se reduzem como no português brasileiro (<i>e</i> final não vira "i"). E as consoantes dobradas se pronunciam dobradas: em <i>puella</i> e <i>terra</i> você ouve os dois <i>l</i> e os dois <i>r</i>.</p>
'''),
        ('Vogais longas, vogais breves e o acento', f'''
<p>Cada vogal latina pode ser <b>longa</b> ou <b>breve</b>. A diferença é de duração: uma longa dura cerca do dobro da breve. Os romanos não marcavam isso na escrita de modo sistemático, mas os livros para estudantes marcam as longas com um traço, o <b>macron</b>: <i>ā ē ī ō ū</i>. Vale a pena aprender com eles, por duas razões:</p>
<ul>
<li>A quantidade distingue formas: <i>puella</i> (a menina, sujeito) e <i>puellā</i> (com a menina, ablativo) só diferem pela duração do <i>a</i> final.</li>
<li>A quantidade determina o <b>acento tônico</b>, que é o que faz a palavra soar certa.</li>
</ul>
<h3>Primeiro passo: dividir em sílabas</h3>
<p>Uma palavra latina tem tantas sílabas quantas são as suas vogais e ditongos. Uma consoante isolada entre vogais vai com a vogal seguinte (<i>pa-ter</i>, <i>a-mī-cus</i>); consoantes dobradas se separam (<i>pu-el-la</i>, <i>ter-ra</i>); nos outros grupos de consoantes, a primeira fica com a vogal anterior (<i>ma-gis-ter</i>). A exceção é o grupo de uma <b>consoante oclusiva</b> (<i>p, b, t, d, c, g</i>) seguida de <i>l</i> ou <i>r</i>, que vai inteiro para a sílaba seguinte: <i>a-gri-co-la</i>, <i>pa-tris</i>.</p>
<h3>A regra do acento</h3>
<p>Em palavras de mais de uma sílaba, o acento latino não cai na última (as raríssimas exceções, como <i>illīc</i>, vêm da perda de uma sílaba final). A regra é simples:</p>
<ol>
<li>Palavras de <b>duas sílabas</b> são acentuadas na primeira: <i>Rō-ma</i>, <i>a-qua</i>, <i>pa-ter</i>.</li>
<li>Palavras de <b>três ou mais sílabas</b> são acentuadas na <b>penúltima</b> se ela for longa; se a penúltima for breve, o acento recua para a <b>antepenúltima</b>.</li>
</ol>
<p>Uma sílaba é longa quando tem vogal longa ou ditongo (<i>a-mī-cus</i>, <i>Rō-mā-nus</i>) ou quando a sua vogal, mesmo breve, é seguida de duas consoantes ou de <i>x</i>, que vale por duas (<i>pu-el-la</i>, <i>ma-gis-ter</i>, <i>sax-um</i>). Aqui também vale a exceção: oclusiva + <i>l</i> ou <i>r</i> <b>não</b> torna longa a sílaba anterior na prosa, e é por isso que <i>agricola</i> se acentua em <i>gri</i> e <i>tenebrae</i> em <i>te</i>. Uma vogal seguida imediatamente de outra vogal é breve (<i>vi-a</i>, <i>fī-li-us</i>): esse detalhe decide o acento de muitas palavras em <i>-ia</i> e <i>-ius</i>.</p>
{tabela(['Palavra', 'Sílabas', 'Penúltima', 'Acento'], [
    ['amīcus', 'a-mī-cus', 'longa (ī)', 'a-<b>mī</b>-cus'],
    ['dominus', 'do-mi-nus', 'breve (i)', '<b>do</b>-mi-nus'],
    ['puella', 'pu-el-la', 'longa (vogal seguida de duas consoantes)', 'pu-<b>el</b>-la'],
    ['fēmina', 'fē-mi-na', 'breve (i)', '<b>fē</b>-mi-na'],
    ['nātūra', 'nā-tū-ra', 'longa (ū)', 'nā-<b>tū</b>-ra'],
    ['magister', 'ma-gis-ter', 'longa (vogal seguida de duas consoantes)', 'ma-<b>gis</b>-ter'],
    ['fīlius', 'fī-li-us', 'breve (vogal antes de vogal)', '<b>fī</b>-li-us'],
], 'A regra do acento em ação', latim_cols=(0,))}
{dica('<b>Os ditongos</b> <i>ae</i>, <i>oe</i> e <i>au</i> formam uma só sílaba e são sempre longos: <i>Cae-sar</i>, <i>poe-na</i>, <i>au-rum</i>. Já <i>i</i> e <i>u</i> seguidos de vogal costumam ser consoantes no início de palavra (<i>Iū-li-us</i>, <i>vī-ta</i>).')}
{observacao('O macron não é acento', 'O traço marca <b>duração</b>, não tonicidade. <i>Rōmānus</i> tem duas vogais longas e só uma sílaba tônica (<i>mā</i>); <i>puellā</i> tem o <i>ā</i> final longo, e mesmo assim o acento continua em <i>el</i>. Quem lê o macron como acento agudo erra justamente nessas palavras.')}
<p>Não é preciso decorar a quantidade de cada vogal agora. Lendo com macrons e em voz alta, o ouvido aprende sozinho: é exatamente o que fazem os métodos recomendados abaixo.</p>
'''),
        ('Lendo em voz alta: uma frase autêntica', f'''
<p>Para juntar tudo, leia uma frase que gerações de brasileiros já ouviram, o começo do Pai-Nosso na tradução de São Jerônimo. Por enquanto não importa a gramática: o objetivo é pronunciar cada palavra com as sílabas, as quantidades e o acento certos.</p>
{exemplos([('Pater noster, quī es in caelīs, sānctificētur nōmen tuum.', 'Pai nosso, que estás nos céus, santificado seja o teu nome. (Mt 6,9, Vulgata)')])}
{diagrama_frase([('Pater noster', 'PA-ter NOS-ter · duas dissílabas'), ('quī es', 'monossílabos · sem acento a calcular'), ('in caelīs', 'CAE-līs · ditongo'), ('sānctificētur', 'sān-cti-fi-CĒ-tur · penúltima longa'), ('nōmen tuum', 'NŌ-men TU-um · dissílabas')], 'O acento palavra a palavra. As maiúsculas marcam a sílaba tônica.')}
{analise('Mt 6,9, palavra a palavra (pronúncia)', [
    ('Pater', 'pater, "pai"', 'pa-ter; as duas vogais são breves', 'dissílaba: acento na primeira, <b>PA</b>-ter. Nas duas pronúncias, "páter".'),
    ('noster', 'noster, "nosso"', 'nos-ter; o <i>o</i> é breve, mas a sílaba é longa (vogal + duas consoantes)', 'dissílaba: <b>NOS</b>-ter. Pronuncie o <i>o</i> fechado e curto, sem ditongar.'),
    ('quī', 'quī, "que" (relativo)', 'uma sílaba; <i>qu</i> conta como uma consoante; <i>ī</i> longo', 'monossílabo: "kuí" nas duas pronúncias.'),
    ('es', 'es, "(tu) és, estás"', 'uma sílaba, vogal breve', 'monossílabo átono, apoiado na palavra vizinha.'),
    ('in', 'in, "em"', 'uma sílaba', 'monossílabo: forma uma unidade com <i>caelīs</i>, "in-<b>CAE</b>-līs".'),
    ('caelīs', 'caelum, "céu"', 'cae-līs; ditongo <i>ae</i> + <i>ī</i> longo', 'dissílaba: <b>CAE</b>-līs. Restaurada: "káilīs"; eclesiástica: "tchélis" (c antes de ae soa "tch").'),
    ('sānctificētur', 'sānctificāre, "santificar"', 'sān-cti-fi-cē-tur (das três consoantes <i>nct</i>, só a primeira fica com a vogal anterior, como em <i>ma-gis-ter</i> e no exemplo <i>mōn-strum</i> de Bennett, § 4.3; quem divide <i>sānc-ti-</i> chega ao mesmo acento); penúltima <i>cē</i> longa', 'cinco sílabas, acento na penúltima longa: san-cti-fi-<b>CĒ</b>-tur. Restaurada: "sanktifikétur"; eclesiástica: "sanktifitchétur".'),
    ('nōmen', 'nōmen, "nome"', 'nō-men; <i>ō</i> longo', 'dissílaba: <b>NŌ</b>-men, com o <i>o</i> fechado e longo.'),
    ('tuum', 'tuus, "teu"', 'tu-um; o primeiro <i>u</i> é breve porque vem antes de vogal', 'dissílaba: <b>TU</b>-um, duas vogais distintas, sem fundi-las.'),
])}
<p>Repare em três coisas. Primeiro, as palavras de duas sílabas nunca dão trabalho: o acento vai sempre na primeira. Segundo, numa palavra longa como <i>sānctificētur</i> basta olhar a penúltima: é longa, então leva o acento. Terceiro, a diferença entre as duas pronúncias aparece só em poucas letras (aqui, o <i>c</i> antes de <i>ae</i> e de <i>e</i>); o acento é o mesmo nas duas.</p>
'''),
        ('Como este curso funciona', '''
<p>O <i>Elementa Linguae Latinae</i> ensina a gramática na ordem em que ela aparece nos textos, sempre com exemplos em latim e exercícios curtos com resposta. Cada capítulo termina com leituras do catálogo para praticar o que foi visto. Você não precisa de nada além do navegador, mas um método completo ao lado (como o <i>Familia Romana</i> ou o <i>Latine loqui</i>, em português) multiplica o rendimento.</p>
<p>Três hábitos desde o primeiro capítulo: <b>ler em voz alta</b> tudo o que estiver em latim, <b>não traduzir palavra por palavra</b> (o próximo capítulo explica por quê) e <b>anotar pouco, mas com a frase inteira</b>. O <a href="../percurso.html">percurso de leitura</a> detalha o método.</p>
'''),
    ],
    erros_comuns=[
        ('Ler o macron como se fosse acento agudo.', 'O macron marca só a duração. Em <i>Rōmānus</i> há duas vogais longas e o acento cai apenas em <i>mā</i>; em <i>puellā</i> o <i>ā</i> final é longo, mas o acento fica em <i>el</i>. Para achar a tônica, aplique a regra da penúltima.'),
        ('Acentuar a palavra latina como a palavra portuguesa que veio dela.', 'Muitas vezes coincidem, mas não sempre: o português diz "filosofia", com tônica em "fi", e o latim diz <i>philo<b>so</b>phia</i>, porque a penúltima (<i>phi</i>, com vogal antes de vogal) é breve. Na dúvida, divida em sílabas e examine a penúltima.'),
        ('Pronunciar o latim com as vogais reduzidas do português brasileiro.', 'O <i>e</i> final latino não vira "i" nem o <i>o</i> final vira "u": <i>ave</i> soa "áve", não "ávi"; <i>Cicerō</i> termina em "o" mesmo. As vogais latinas são sempre pronunciadas por inteiro, como no espanhol ou no italiano.'),
        ('Misturar as duas pronúncias na mesma leitura.', 'Dizer "Kíkero" e logo depois "tchélis" é incoerente: ou o <i>c</i> é sempre /k/ (restaurada), ou vira "tch" antes de <i>e, i, ae, oe</i> (eclesiástica). Escolha uma das duas e use-a em todo o texto.'),
        ('Considerar longa toda sílaba seguida de duas consoantes.', 'Oclusiva + <i>l</i> ou <i>r</i> (<i>br, cr, gr, pl, tr</i>...) não alonga a sílaba anterior na prosa: <i>a-gri-co-la</i> se acentua em <i>gri</i>, e <i>te-ne-brae</i> em <i>te</i>, porque <i>co</i> e <i>ne</i> continuam breves.'),
        ('Pronunciar as consoantes dobradas como simples.', 'Em latim, <i>ll, rr, ss, tt</i> soam dobradas (<i>pu-el-la</i>, <i>ter-ra</i>), e isso importa: a consoante dobrada é o que torna longa a penúltima de <i>puella</i> e leva o acento para <i>el</i>.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Achar o acento de uma palavra nova',
            'Descubra, passo a passo, a sílaba tônica de <i lang="la">Ītalia</i> e de <i lang="la">senātor</i>.', [
            ('Divida <i>Ītalia</i> em sílabas.', '<i>Ī-ta-li-a</i>: quatro vogais, quatro sílabas. O <i>i</i> antes do <i>a</i> final é vogal, não consoante, porque não está no início da palavra.'),
            ('A penúltima, <i>li</i>, é longa ou breve?', 'Breve: a vogal <i>i</i> vem imediatamente antes de outra vogal (<i>a</i>), e vogal antes de vogal é breve. Não há ditongo nem duas consoantes.'),
            ('Onde cai o acento?', 'Na antepenúltima: <i>Ī-<b>ta</b>-li-a</i>. Note que o macron do <i>Ī</i> inicial não atrai o acento: ele só diz que aquela vogal é longa.'),
            ('Agora <i>senātor</i>: sílabas e penúltima.', '<i>se-nā-tor</i>; a penúltima <i>nā</i> tem vogal longa (macron), logo é longa.'),
            ('Onde cai o acento?', 'Na penúltima: <i>se-<b>nā</b>-tor</i>. O português "senador" tem a tônica em outra sílaba porque vem de outra forma da palavra, o acusativo <i>se-nā-<b>tō</b>-rem</i>, que perdeu a sílaba final.'),
        ]),
        pratica_guiada('Prática guiada 2 · Uma frase de César em voz alta',
            'Prepare a leitura em voz alta da primeira frase dos Comentários de César sobre a Guerra da Gália (<i>BG</i> 1.1.1): <i lang="la">Gallia est omnis dīvīsa in partēs trēs.</i> ("A Gália, em seu conjunto, está dividida em três partes.")', [
            ('Quais palavras não exigem cálculo?', 'Os monossílabos <i>est</i>, <i>in</i>, <i>trēs</i>, e as dissílabas <i>omnis</i> (<b>om</b>-nis) e <i>partēs</i> (<b>par</b>-tēs), sempre acentuadas na primeira.'),
            ('Divida e acentue <i>Gallia</i>.', '<i>Gal-li-a</i>: a penúltima <i>li</i> é breve (vogal antes de vogal), então o acento recua: <i><b>Gal</b>-li-a</i>. E o <i>ll</i> soa dobrado.'),
            ('Divida e acentue <i>dīvīsa</i>.', '<i>dī-vī-sa</i>: a penúltima <i>vī</i> tem vogal longa, então leva o acento: <i>dī-<b>vī</b>-sa</i>.'),
            ('Leia a frase inteira nas duas pronúncias.', 'Restaurada: "GÁL-li-a est ÓM-nis di-UÍ-sa in PÁR-tēs trēs" (o <i>v</i> soa como "u"). Eclesiástica: "GÁL-lia est ÓM-nis di-VÍ-sa in PÁR-tes tres". O acento é o mesmo; muda só o som do <i>v</i>.'),
        ], 'Moral: as palavras de duas sílabas resolvem-se sozinhas; nas mais longas, olhe só a penúltima.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Parentes em português', 'Sem dicionário, diga o que significam estas palavras latinas. Use as correspondências de som que você viu.', [
            ('<i>schola</i>', 'escola. O português acrescentou um <i>e</i> antes do <i>sc</i> inicial, como em <i>spīritus</i> → espírito.'),
            ('<i>vēritās</i>', 'verdade (do acusativo <i>vēritātem</i>: <i>t</i> entre vogais virou <i>d</i>).'),
            ('<i>stella</i>', 'estrela.'),
            ('<i>lupus</i>', 'lobo (<i>p</i> entre vogais virou <i>b</i>, como em <i>sapere</i> → saber).'),
            ('<i>lībertās</i>', 'liberdade.'),
            ('<i>porta</i>', 'porta. Nem tudo muda!'),
        ]),
        exercicio('Exercício 2 · O acento tônico', 'Divida em sílabas e marque a sílaba tônica. As vogais longas estão marcadas.', [
            ('<i>Rōmānus</i>', 'Rō-<b>mā</b>-nus: a penúltima tem vogal longa.'),
            ('<i>oculus</i>', '<b>o</b>-cu-lus: a penúltima (<i>cu</i>) é breve, o acento recua.'),
            ('<i>Caesar</i>', '<b>Cae</b>-sar: duas sílabas, acento na primeira; <i>ae</i> é ditongo.'),
            ('<i>agricola</i>', 'a-<b>gri</b>-co-la: a penúltima (<i>co</i>) é breve, o acento recua para <i>gri</i>. O grupo <i>gr</i> fica inteiro na sílaba seguinte (oclusiva + <i>r</i>).'),
            ('<i>Minerva</i>', 'Mi-<b>ner</b>-va: a vogal da penúltima é seguida de duas consoantes (<i>r</i> + <i>v</i>), logo a sílaba é longa.'),
            ('<i>philosophia</i>', 'phi-lo-<b>so</b>-phi-a: a penúltima (<i>phi</i>) é breve, porque o <i>i</i> vem antes de outra vogal; o acento recua para <i>so</i>. Não há macron em nenhuma vogal desta palavra. Compare com o português "filosofia", acentuado em outra sílaba.'),
        ]),
        exercicio('Exercício 3 · Duas pronúncias', 'Pronuncie em voz alta na pronúncia restaurada e na eclesiástica.', [
            ('<i>Cicerō</i>', 'Restaurada: "Kíkero". Eclesiástica: "Tchítchero".'),
            ('<i>Vergilius</i>', 'Restaurada: "Uerguílius". Eclesiástica: "Verdjílius".'),
            ('<i>vēnī, vīdī, vīcī</i>', 'Restaurada: "uéni, uídi, uíki". Eclesiástica: "véni, vídi, vítchi".'),
            ('<i>Agnus Deī</i>', 'Restaurada: "ágnus déi". Eclesiástica: "ánhus déi".'),
            ('<i>grātia</i>', 'Restaurada: "grátia". Eclesiástica: "grátsia".'),
        ]),
        exercicio('Exercício 4 · Longa ou breve?', 'Diga se a penúltima sílaba é longa ou breve, explique por quê e marque a tônica.', [
            ('<i>fenestra</i> (janela)', 'fe-nes-tra. A penúltima <i>nes</i> é longa: a vogal é seguida de <i>s</i> + <i>t</i> (o grupo <i>str</i> começa com <i>s</i>, que não é oclusiva). Acento: fe-<b>nes</b>-tra.'),
            ('<i>tenebrae</i> (trevas)', 'te-ne-brae. A penúltima <i>ne</i> é breve: <i>br</i> é oclusiva + <i>r</i> e vai inteiro para a sílaba seguinte. Acento: <b>te</b>-ne-brae.'),
            ('<i>mīlitēs</i> (soldados)', 'mī-li-tēs. A penúltima <i>li</i> é breve (vogal breve + uma só consoante). Acento: <b>mī</b>-li-tēs. O macron de <i>tēs</i> não importa: a última sílaba nunca é tônica.'),
            ('<i>Athēnae</i> (Atenas)', 'A-thē-nae. A penúltima <i>thē</i> tem vogal longa. Acento: A-<b>thē</b>-nae. O <i>th</i> é uma só consoante (letra grega).'),
            ('<i>saxum</i> (rochedo)', 'sax-um: o <i>x</i> fica com a vogal anterior. Duas sílabas, logo acento na primeira, <b>sax</b>-um. A primeira sílaba é longa de qualquer modo, porque <i>x</i> vale por duas consoantes (<i>cs</i>); numa palavra mais longa, isso bastaria para atrair o acento.'),
        ]),
        exercicio('Exercício 5 · Da inscrição à edição moderna', 'Os romanos escreviam em maiúsculas, sem distinguir <i>I/J</i> nem <i>U/V</i>. Reescreva em letras minúsculas, com <i>u</i> para a vogal e <i>v</i> para a consoante (os macrons não se deduzem da escrita antiga; as respostas os acrescentam para você).', [
            ('IVLIA', '<i>Iūlia</i>: o primeiro <i>I</i> é consoante (antes de vogal, no início da palavra) e o <i>V</i> é vogal. Pronúncia restaurada: "Iúlia", com o <i>i</i> inicial soando como o "i" de "iate".'),
            ('VENI VIDI VICI', '<i>vēnī, vīdī, vīcī</i>: cada <i>V</i> inicial vem antes de vogal, logo é consoante (<i>v</i>).'),
            ('IVVENIS', '<i>iuvenis</i> (jovem): <i>I</i> consoante, <i>V</i> vogal, <i>V</i> consoante, depois <i>e, i</i>. Em edições que usam <i>j</i>: <i>juvenis</i>.'),
            ('VVLTVS', '<i>vultus</i> (rosto): o primeiro <i>V</i> é consoante, o segundo, entre consoantes, é vogal, e o último também (<i>-tus</i>).'),
        ]),
    ],
    leituras=['leite-latine-loqui-curso-basico-de-latim-volume-i', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'd-ooge-latin-for-beginners', 'latinitium', 'ravizza-gramatica-latina', 'vulgata-biblia-sacra-vulgata-editio-clementina'],
    leituras_nota='Para começar a ouvir latim desde já: o Latinitium tem um arquivo gratuito de áudios curtos, e os métodos indicados trazem a pronúncia explicada nas primeiras páginas. Na Vulgata, leia em voz alta o Pai-Nosso inteiro (Mt 6,9–13) aplicando a regra do acento; a gramática do Pe. Ravizza (cap. 1) resume a pronúncia em português.',
)
