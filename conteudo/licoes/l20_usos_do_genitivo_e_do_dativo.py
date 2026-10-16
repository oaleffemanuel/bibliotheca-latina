from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='20-usos-do-genitivo-e-do-dativo', titulo='Usos do genitivo e do dativo', titulo_latim='Dē genetīvō et datīvō', tempo='75 min',
    resumo='Os dois casos que respondem "de quem?" e "a quem, para quem?", agora com todos os seus empregos importantes: o genitivo de posse, partitivo, subjetivo e objetivo, de qualidade e de valor, e com adjetivos; o dativo de objeto indireto, de posse, de interesse, de referência e de finalidade (o duplo dativo), com adjetivos, com os verbos intransitivos que o português trata como transitivos e com os verbos compostos.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['genitivo de posse', 'genitivo predicativo (est + genitivo)', 'genitivo partitivo', 'nihil novī, satis pecūniae', 'genitivo subjetivo e objetivo', 'genitivo de qualidade', 'genitivo de valor (magnī, parvī)', 'genitivo com adjetivos', 'meminī e oblīvīscor (vocabulário)', 'dativo de objeto indireto', 'dativo de posse (mihi est)', 'dativo de interesse', 'dativo de referência', 'dativo de finalidade e duplo dativo', 'dativo com adjetivos', 'dativo com verbos intransitivos', 'dativo com verbos compostos', 'dativo de agente (menção)', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 11 (o quadro completo das cinco declinações, porque aqui aparecem genitivos e dativos de todas elas). Os exemplos usam também os pronomes dos capítulos 14 a 16, o perfeito do capítulo 13 e os superlativos do capítulo 18; quando aparece algo ainda não estudado, há glosa.',
                       licoes=['03-introducao-aos-casos', '11-a-quarta-e-a-quinta-declinacoes', '14-os-pronomes-pessoais', '18-comparativos-e-superlativos']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 186 (o dativo: "a, para"), § 187 (objeto indireto: I com transitivos; II com intransitivos de favorecer, confiar, persuadir, prejudicar, poupar etc., e a nota sobre iuvō, laedō, dēlectō com acusativo; III com compostos: praefuit, succurrit), § 188 (dativo de referência; 188.2.b ético; 188.2.c da pessoa que julga), § 189 (dativo de agente, só a menção), § 190 (dativo de posse; 190.1 mihi Mārcō nōmen est), § 191 (dativo de finalidade; 191.2 com outro dativo: cui bonō?, Atticīs vēnit auxiliō), § 192 (dativo com adjetivos), §§ 194–204 (genitivo: 198 posse, 198.1 causā e grātiā, 198.2 genitivo predicativo; 199 subjetivo; 200 objetivo, 200.1 ergā; 201 do todo, 201.1.a ex/dē com cardinais, 201.2 nihil bonī, satis pecūniae, 201.2.b nihil dulcius; 203 qualidade, 203.2 medida, 203.3 valor; 204 com adjetivos, 204.3 similis), §§ 205–206 (meminī, oblīvīscor), § 359.1 (genitivo × dativo de posse)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', url='https://dcc.dickinson.edu/grammar/latin/genitive', nota='§§ 341–348 (genitivo com nomes: 341 "caso adjetivo"; 343 posse, 343.b predicativo, 343 nota 1 o possuidor como agente; 345 qualidade, só com adjetivo; 346 partitivo, 346.c ex/dē com cardinais, 346.e "todo" concorda; 348 objetivo), § 349 (adjetivos com genitivo: perītus, memor, plēnus), § 350 (meminī, oblīvīscor), §§ 360–373 (dativo: 361–362 objeto indireto; 367 verbos especiais, 367.a iuvō, laedō, iubeō, dēlectō com acusativo; 370 compostos; 373 posse, 373 nota ênfase, 373.a nōmen est), § 374 (agente, só a menção), §§ 376–378 (referência, pessoa que julga), § 382 (finalidade; nota 1: abstrato, singular, sem adjetivo salvo de grau), §§ 383–385 (dativo com adjetivos; 385.c amīcus Cicerōnī × Cicerōnis amīcus; similis)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§§ 214–227 (dativo: 215 transitivos de dar e dizer; 216–217 intransitivos e a nota sobre dēlectō, iuvō, laedō, iubeō; 218 adjetivos; 220 compostos; 221 vantagem e desvantagem; 223 ético; 224 possuidor; 225–226 finalidade e duplo dativo), §§ 247–262 (genitivo: 254 possessivo; 255 qualidade; 257 valor; 258–260 partitivo; 261–262 subjetivo e objetivo), § 265 (verbos de lembrar e esquecer)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 212 (complemento de apreciação: magnī, parvī com aestimāre, facere, esse), n. 228 (qualidade: vir magnae prūdentiae), n. 264 (genitivo determinativo; subjetivo × objetivo, metus hostium; ergā, in), n. 266 (possessivo), n. 267 (esse + genitivo, "é próprio de"), n. 269 (partitivo), n. 272 (adjetivos com genitivo), n. 273 (meminisse, oblīvīscī), nn. 280–294 (dativo: 283 verbos transitivos em português e intransitivos em latim; 284 compostos de esse; 289 adjetivos; 291 interesse; 292 posse; 293 est mihi nōmen; 294 duplo dativo). A numeração foi lida no OCR, que às vezes troca dígitos; os números citados foram conferidos pela sequência dos parágrafos.', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Salmo 110,10; João 1,6; Salmo 22,1; Mateus 5,3', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Liber_Psalmorum', nota='frases das seções 6 e do exercício 6, conferidas na Wikisource latina (numeração dos Salmos da Vulgata); ortografia adaptada (ae por æ, I por J) e macrons acrescentados', tipo='dominio_publico'),
        referencia('Commentarii de Bello Gallico I, 1', 'Caio Júlio César', catalogo='caesar-commentarii-de-bello-gallico-texto-integral', url='http://www.thelatinlibrary.com/caesar/gall1.shtml', nota='"Horum omnium fortissimi sunt Belgae" (exercício 6), conferido no texto da Latin Library; macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Distinguir os principais empregos do genitivo (posse, partitivo, subjetivo, objetivo, qualidade, valor, com adjetivos) e traduzir cada um com a preposição portuguesa adequada.',
        'Resolver a ambiguidade entre genitivo subjetivo e objetivo (<i>amor patris</i>) pelo contexto.',
        'Reconhecer e traduzir o dativo de posse (<i>mihi est liber</i>), o de interesse, o de referência e o duplo dativo (<i>sociīs auxiliō venīre</i>).',
        'Usar o dativo com os adjetivos e com os verbos intransitivos e compostos que o pedem (<i>crēdō, pāreō, persuādeō, praesum</i>), sem confundi-los com <i>iuvō, laedō, iubeō</i>, que pedem acusativo.',
        'Analisar frases autênticas da Vulgata e de César identificando a função de cada genitivo e de cada dativo.',
    ],
    secoes=[
        ('Dois casos, duas perguntas: "de quem?" e "a quem?"', f'''
<p>No capítulo 3 você aprendeu que o genitivo responde a "de quem? de quê?" e o dativo a "a quem? para quem?". Essa primeira aproximação continua válida, mas agora, com as cinco declinações completas (capítulo 11) e os pronomes (capítulos 14 a 16), é hora de ver o que os autores fazem de fato com esses dois casos. Há um princípio que organiza tudo e que vale a pena guardar desde já: o <b>genitivo</b> é, antes de tudo, o caso que <b>liga um nome a outro nome</b>; por isso Allen e Greenough o chamam de "caso adjetivo" (§ 341): <i>domus rēgis</i> é "a casa do rei" assim como <i>domus rēgia</i> é "a casa real". O <b>dativo</b>, ao contrário, gira em torno da <b>pessoa interessada</b> no que acontece: aquela a quem algo é dado, que tem algo, que se beneficia ou se prejudica, que obedece ou confia. Bennett resume: o dativo exprime as relações que dizemos com "a" e "para" (§ 186).</p>
<p>Daí sai uma regra prática de leitura: quando encontrar um genitivo, procure o <b>substantivo</b> (ou o adjetivo) de que ele depende; quando encontrar um dativo, pergunte <b>quem está interessado</b> na ação e de que modo. O quadro abaixo é o mapa do capítulo; cada linha é desenvolvida nas seções seguintes.</p>
{tabela(['Caso', 'Emprego', 'Exemplo', 'Tradução'], [
    ['Genitivo', 'posse', '<i>domus <b>rēgis</b></i>', 'a casa do rei'],
    ['Genitivo', 'predicativo de posse ("é de", "é próprio de")', '<i>Haec domus <b>rēgis</b> est.</i>', 'Esta casa é do rei.'],
    ['Genitivo', 'partitivo (do todo)', '<i>pars <b>mīlitum</b></i>; <i>nihil <b>novī</b></i>', 'parte dos soldados; nada de novo'],
    ['Genitivo', 'subjetivo / objetivo', '<i>amor <b>patris</b></i>', 'o amor do pai / o amor ao pai'],
    ['Genitivo', 'qualidade (com adjetivo)', '<i>vir <b>magnae virtūtis</b></i>', 'homem de grande coragem'],
    ['Genitivo', 'valor', '<i><b>magnī</b> aestimāre</i>', 'estimar muito'],
    ['Genitivo', 'com adjetivos', '<i>cupidus <b>glōriae</b></i>', 'desejoso de glória'],
    ['Dativo', 'objeto indireto', '<i>Librum <b>amīcō</b> dō.</i>', 'Dou o livro ao amigo.'],
    ['Dativo', 'posse com <i>esse</i>', '<i><b>Mihi</b> est liber.</i>', 'Eu tenho um livro.'],
    ['Dativo', 'interesse (vantagem ou desvantagem)', '<i><b>Sibi</b> nōn labōrat.</i>', 'Não trabalha para si.'],
    ['Dativo', 'referência (ponto de vista)', '<i><b>Mihi</b> deus erit.</i>', 'Para mim, será um deus.'],
    ['Dativo', 'finalidade (duplo dativo)', '<i><b>Sociīs auxiliō</b> vēnit.</i>', 'Veio em auxílio dos aliados.'],
    ['Dativo', 'com adjetivos', '<i><b>patrī</b> cārus</i>', 'querido ao pai'],
    ['Dativo', 'com verbos intransitivos e compostos', '<i><b>Ducī</b> pāret.</i> <i><b>Legiōnī</b> praeest.</i>', 'Obedece ao comandante. Comanda a legião.'],
], 'Mapa dos empregos do genitivo e do dativo')}
{dica('<b>Desconfie do "de" e do "a" do português.</b> O "de" português corresponde ao genitivo só quando liga um nome a outro nome ("a casa <i>do</i> rei"); "venho <i>de</i> Roma", "feito <i>de</i> ouro" e "falar <i>de</i> alguém" são ablativos, que você verá no capítulo 21. Do mesmo modo, o "a" de "obedecer <i>ao</i> pai" é dativo, mas o de "ir <i>a</i> Roma" é acusativo de direção.')}
'''),
        ('O genitivo com substantivos: posse, parte do todo, sujeito e objeto', f'''
<h3>Genitivo de posse</h3>
<p>É o emprego mais frequente: o genitivo indica a quem algo pertence ou de quem procede (<i>domus Cicerōnis</i>, "a casa de Cícero"; <i>Mārcī fīlius</i>, "o filho de Marco"; <i>dicta Platōnis</i>, "as palavras de Platão"). Dois desdobramentos merecem atenção. Primeiro, com <i>causā</i> e <i>grātiā</i>, "por causa de, em atenção a", o genitivo vem <b>antes</b>: <i>amīcōrum causā</i>, "por causa dos amigos" (Bennett § 198.1). Segundo, o genitivo de posse pode ficar no <b>predicado</b>, ligado ao sujeito por <i>esse</i>: <i>Haec domus rēgis est</i>, "esta casa é do rei". Dessa construção nasce uma expressão muito latina, <i>est</i> + genitivo no sentido de "é próprio de, é dever de": <i>Hōc cōnsulis est</i>, "isto é dever do cônsul", "isto cabe ao cônsul" (Ravizza n. 267 dá <i>cōnsulis est</i>, "é dever do cônsul", e <i>iūdicis officium est</i>, "é dever do juiz"; Allen e Greenough § 343.b–c). Nos textos, o sujeito dessa expressão costuma ser um infinitivo ("é próprio do sábio calar"), construção que o capítulo 27 apresenta.</p>
{exemplos([('Fīlia <b>rēgis</b> in hortō ambulat.', 'A filha do rei passeia no jardim. (posse, parentesco)'), ('Hīc ager nōn <b>meus</b> est, sed <b>frātris</b>.', 'Este campo não é meu, mas do meu irmão. (posse predicativa; com <i>ego</i> usa-se o possessivo <i>meus</i>, capítulo 14)'), ('<b>Patriae causā</b> labōrāmus.', 'Trabalhamos pela pátria (por causa da pátria).'), ('Hōc <b>bonī cīvis</b> est.', 'Isto é próprio do bom cidadão. (<i>hōc</i>, "isto", resume uma atitude já mencionada)')])}
<h3>Genitivo partitivo, ou do todo</h3>
<p>O genitivo indica o <b>todo</b> de que se toma uma parte. Aparece depois de nomes que significam parte ou quantidade (<i>pars, multitūdō, nēmō</i>), de pronomes (<i>quis nostrum?</i>, "qual de nós?"; lembre <i>nostrum, vestrum</i> partitivos, do capítulo 14), de superlativos e ordinais (<i>fortissimus omnium</i>, "o mais forte de todos"; <i>prīmus rēgum</i>), e, de modo muito característico, depois de um <b>neutro singular usado como substantivo</b> e dos advérbios <i>satis, parum, nimis</i>: <i>nihil novī</i>, "nada de novo"; <i>quid cōnsiliī?</i>, "que plano?"; <i>multum vīnī</i>, "muito vinho"; <i>plūs labōris</i>, "mais trabalho"; <i>satis pecūniae</i>, "dinheiro suficiente" (Bennett § 201.2). O português às vezes acompanha ("nada <i>de</i> novo"), às vezes não ("dinheiro suficiente").</p>
{tabela(['Tipo de palavra', 'Latim', 'Tradução', 'Observação'], [
    ['nome de parte', '<i>magna pars <b>hominum</b></i>', 'grande parte dos homens', ''],
    ['pronome', '<i>quis <b>vestrum</b>?</i>', 'qual de vocês?', '<i>vestrum</i>, não <i>vestrī</i>'],
    ['superlativo', '<i>altissimus <b>montium</b></i>', 'o mais alto dos montes', 'capítulo 18'],
    ['neutro substantivado', '<i>nihil <b>bonī</b></i>; <i>aliquid <b>novī</b></i>', 'nada de bom; algo de novo', 'só adjetivos de 1ª classe'],
    ['advérbio de quantidade', '<i>satis <b>cibī</b></i>; <i>parum <b>temporis</b></i>', 'comida suficiente; pouco tempo', ''],
    ['numeral cardinal', '<i>ūnus <b>ex mīlitibus</b></i>', 'um dos soldados', 'em geral <i>ex/dē</i> + ablativo, não genitivo'],
], 'O genitivo partitivo e as palavras que o pedem')}
{observacao('Quando NÃO há partitivo', 'Três limites evitam erros de retroversão. (1) Com os <b>cardinais</b> e com <i>quīdam</i>, o latim prefere <i>ex</i> ou <i>dē</i> + ablativo: <i>ūnus ex mīlitibus</i>, <i>trēs dē servīs</i> (Bennett § 201.1.a; A&G § 346.c). (2) Palavras que abrangem o <b>todo</b> concordam com o nome, sem genitivo: "todos os soldados" é <i>omnēs mīlitēs</i>, "nós trezentos" é <i>trecentī</i> (A&G § 346.e). (3) Os adjetivos de <b>segunda classe</b> (capítulo 10) não entram no partitivo: concordam com o neutro. Diz-se <i>nihil bonī</i>, mas <i>nihil dulcius</i>, "nada mais doce", e <i>nihil memorābile</i>, "nada memorável" (Bennett § 201.2.a–b).')}
<h3>Genitivo subjetivo e genitivo objetivo</h3>
<p>Muitos substantivos contêm uma ação ou um sentimento: <i>amor</i> (amar), <i>timor, metus</i> (temer), <i>odium</i> (odiar), <i>cūra</i> (cuidar), <i>cupiditās</i> (desejar), <i>spēs</i> (esperar). O genitivo que os acompanha pode indicar <b>quem sente ou faz</b> (genitivo subjetivo) ou <b>o alvo</b> do sentimento ou da ação (genitivo objetivo). O teste mais simples é transformar o substantivo em verbo, como faz o Pe. Ravizza (n. 264): se o genitivo vira sujeito, é subjetivo; se vira objeto, é objetivo.</p>
{comparacao('O mesmo genitivo, duas leituras', ['Latim', 'Subjetivo (quem sente)', 'Objetivo (o que é sentido)', 'Em contexto'], [
    ['amor patris', 'o pai ama → "o amor do pai" (pelo filho)', 'alguém ama o pai → "o amor ao pai"', 'decide o contexto'],
    ['timor hostium', 'os inimigos temem → "o medo dos inimigos" (que eles sentem)', 'alguém teme os inimigos → "o medo dos inimigos" (que temos deles)', 'o português tem a mesma ambiguidade'],
    ['amor patriae', '(a pátria não ama)', '"o amor à pátria"', 'só objetivo'],
    ['adventus Caesaris', '"a chegada de César" (ele chega)', '(não se "chega" alguém)', 'só subjetivo'],
])}
<p>Muitas vezes o sentido do substantivo decide sozinho, como nas duas últimas linhas. Quando não decide, o contexto decide; e, quando o próprio autor quer evitar a ambiguidade, usa uma preposição no lugar do genitivo objetivo: <i>amor ergā parentēs</i>, "o amor para com os pais"; <i>odium in cīvēs</i>, "o ódio contra os cidadãos" (Bennett § 200.1). Na tradução, o genitivo objetivo pede com frequência outra preposição portuguesa: "amor <b>à</b> pátria", "medo <b>da</b> morte", "esperança <b>de</b> vitória", "cuidado <b>com</b> os filhos" (<i>cūra līberōrum</i>).</p>
'''),
        ('Genitivo de qualidade, de valor e com adjetivos', f'''
<h3>Genitivo de qualidade (descritivo)</h3>
<p>Para descrever uma pessoa ou coisa por uma qualidade, o latim põe o nome da qualidade no genitivo, <b>sempre acompanhado de um adjetivo</b>: <i>vir magnae virtūtis</i>, "um homem de grande coragem"; <i>rēs eius modī</i>, "uma coisa desse tipo". Sem o adjetivo a construção não existe: "um homem de coragem" não é <i>vir virtūtis</i>, mas <i>vir fortis</i> (A&G § 345). Com numerais, o mesmo genitivo dá medidas e idades: <i>fossa quīndecim pedum</i>, "um fosso de quinze pés" (Bennett § 203.2); <i>puer decem annōrum</i>, "um menino de dez anos". O capítulo 21 mostrará que a qualidade também se diz no ablativo (<i>vir magnā virtūte</i>); para medidas e idades, o genitivo é a forma usual.</p>
<h3>Genitivo de valor</h3>
<p>Com verbos de estimar e avaliar (<i>aestimō, faciō, putō, dūcō, pendō</i>) e com <i>esse</i> no sentido de "valer", um pequeno grupo de genitivos indica o <b>valor indeterminado</b>: <i>magnī, plūris, plūrimī</i> (muito, mais, muitíssimo), <i>parvī, minōris, minimī</i> (pouco, menos, pouquíssimo), <i>tantī, quantī</i> (tanto, quanto) e <i>nihilī</i> (nada). Bennett (§ 203.3) os aproxima do genitivo de qualidade; o Pe. Ravizza (n. 212) chama a construção de "complemento de apreciação".</p>
{exemplos([('Amīcitiam tuam <b>magnī</b> aestimō.', 'Estimo muito a tua amizade.'), ('Virtūtem <b>plūris</b> facimus quam dīvitiās.', 'Damos mais valor à virtude que às riquezas. (<i>dīvitiae, -ārum</i>, riquezas)'), ('Hōc cōnsilium <b>parvī</b> est.', 'Este plano vale pouco.'), ('Quantī est hīc liber?', 'Quanto vale este livro? (o preço exato, em dinheiro, vai no ablativo: capítulo 21)')])}
<h3>Genitivo com adjetivos</h3>
<p>Adjetivos que precisam de um complemento para ter sentido completo, sobretudo os de <b>desejo, conhecimento, lembrança, participação e plenitude</b> (e seus contrários), levam o genitivo (Bennett § 204.1; A&G § 349). É o mesmo genitivo objetivo dos substantivos, aplicado a um adjetivo: quem é <i>cupidus glōriae</i> deseja a glória. O português usa quase sempre "de", mas nem sempre: <i>perītus bellī</i> é "perito <b>na</b> guerra".</p>
{tabela(['Sentido', 'Adjetivos', 'Exemplo', 'Tradução'], [
    ['desejo', '<i>cupidus, avidus, studiōsus</i>', '<i>cupidus <b>pācis</b></i>', 'desejoso de paz'],
    ['conhecimento', '<i>perītus, imperītus, ignārus</i>', '<i>perītus <b>bellī</b></i>', 'experiente na guerra'],
    ['lembrança', '<i>memor, immemor</i>', '<i>memor <b>beneficiī</b></i>', 'lembrado do favor'],
    ['participação', '<i>particeps, expers</i>', '<i>particeps <b>cōnsiliī</b></i>', 'participante do plano'],
    ['plenitude', '<i>plēnus</i>', '<i>plēnus <b>aquae</b></i>', 'cheio de água'],
    ['semelhança (pessoas)', '<i>similis, dissimilis</i>', '<i>patris <b>similis</b></i>', 'parecido com o pai'],
], 'Adjetivos que pedem genitivo')}
<p>Dois avisos. <i>Plēnus</i> admite também o ablativo, mais raro com ele (Bennett § 218.8.a), e os verbos de encher (<i>compleō</i>) preferem o ablativo: capítulo 21. E <i>similis</i> oscila: em Cícero, leva de preferência o genitivo quando se trata de pessoas e genitivo ou dativo quando se trata de coisas (Bennett § 204.3; A&G § 385.c): <i>fīlius patris similis</i>, mas <i>mors somnō</i> (ou <i>somnī</i>) <i>similis</i>.</p>
{observacao('Vocabulário: meminī e oblīvīscor', '"Lembrar-se" e "esquecer-se" também levam genitivo, mas os dois verbos são especiais na forma, por isso ficam aqui apenas como vocabulário. <i>Meminī, meminisse</i> ("lembro-me") só tem formas de perfeito, com sentido de presente; <i>oblīvīscor, oblīvīscī, oblītus sum</i> ("esqueço-me") é um verbo depoente, de forma passiva e sentido ativo, que você estudará no capítulo 25. Ambos levam o genitivo, sobretudo de pessoas (<i>vīvōrum meminī</i>, "lembro-me dos vivos"), e com coisas aceitam também o acusativo; um pronome neutro fica sempre no acusativo (<i>haec meminī</i>, "lembro-me disto"). Ver Bennett §§ 205–206 e A&G § 350.')}
'''),
        ('O dativo da pessoa interessada: objeto indireto, posse, interesse e referência', f'''
<h3>Objeto indireto</h3>
<p>É o dativo que você conhece desde o capítulo 3: a pessoa a quem algo é <b>dado, dito, mostrado, enviado ou prometido</b>, ao lado de um objeto direto no acusativo (<i>Pecūniam <b>mihi</b> dat</i>, "dá-me o dinheiro"). O verbo é transitivo e o dativo completa a ação; por isso, em português, ele corresponde ao objeto indireto com "a" ou "para", ou aos pronomes "me, te, lhe, nos, vos, lhes" (Bennett § 187.I).</p>
<h3>Dativo de posse</h3>
<p>Com o verbo <i>esse</i>, o dativo indica o <b>possuidor</b>: <i>Mihi est liber</i>, literalmente "para mim há um livro", isto é, "eu tenho um livro" (Bennett § 190). Repare que o sujeito gramatical é a coisa possuída (<i>liber</i>), e o verbo concorda com ela: <i>Mihi sunt duo frātrēs</i>, "tenho dois irmãos". Na tradução, quem possui vira sujeito do verbo "ter". O latim também tem <i>habeō</i>, e as duas construções convivem; a diferença, segundo Bennett (§ 359.1) e A&G (§ 373, nota), é de ênfase: o dativo sublinha o <b>fato de haver</b> posse (<i>mihi hortus est</i>, "eu tenho um jardim"), enquanto o genitivo predicativo sublinha <b>quem</b> é o dono (<i>hortus patris est</i>, "o jardim é do meu pai"). Com <i>nōmen est</i>, o nome próprio fica no nominativo ou, por atração, no próprio dativo: <i>Mihi nōmen est Mārcus</i> ou <i>Mihi Mārcō nōmen est</i>, "chamo-me Marco" (Bennett § 190.1).</p>
{comparacao('Três maneiras de falar de posse', ['Latim', 'Construção', 'Ênfase', 'Tradução'], [
    ['Mihi est equus.', 'dativo + <i>esse</i>', 'o fato de ter', 'Eu tenho um cavalo.'],
    ['Equum habeō.', '<i>habeō</i> + acusativo', 'neutra', 'Tenho um cavalo.'],
    ['Hīc equus meus est. / Hīc equus Mārcī est.', 'possessivo ou genitivo predicativo', 'quem é o dono', 'Este cavalo é meu. / Este cavalo é de Marco.'],
])}
<h3>Dativo de interesse (vantagem ou desvantagem)</h3>
<p>Às vezes o dativo não completa o verbo, mas indica <b>em favor de quem</b> (ou em prejuízo de quem) a ação acontece. A frase estaria completa sem ele; o dativo acrescenta o interessado (A&G § 376; Kennedy § 221). Traduz-se por "para", "em favor de", "por".</p>
{exemplos([('Agricola nōn <b>sibi</b> sed <b>fīliīs</b> arborēs serit.', 'O agricultor planta árvores não para si, mas para os filhos. (<i>serō, -ere</i>, plantar)'), ('<b>Tibi</b> sōlī cēnam parō.', 'Preparo o jantar só para você.'), ('Hostēs <b>nostrīs</b> viam claudunt.', 'Os inimigos fecham o caminho aos nossos (em prejuízo dos nossos). (<i>nostrī</i>, "os nossos", substantivado)')])}
<p>Quando "para" ou "por" significa "em defesa de" ou "em lugar de", o latim não usa o dativo, e sim <i>prō</i> + ablativo: <i>prō patriā pugnāre</i>, "lutar pela pátria" (A&G § 379, nota; Ravizza n. 291).</p>
<h3>Dativo de referência e dativo ético</h3>
<p>Uma variedade do dativo de interesse indica <b>do ponto de vista de quem</b> uma afirmação é verdadeira, o "dativo da pessoa que julga" (Bennett § 188.2.c; A&G § 378). O exemplo de Bennett é um verso de Virgílio (<i>Éclogas</i> 1,7, segundo o índice de fontes da gramática): <i>erit ille mihi semper deus</i>, "ele será sempre um deus para mim", isto é, na minha opinião. Outro uso muito comum substitui o genitivo de posse quando se fala de partes do corpo e de coisas pessoais: <i>Caput mihi dolet</i>, "a cabeça me dói", "dói-me a cabeça" (o português faz o mesmo com "me"). Por fim, o <b>dativo ético</b>, só com pronomes pessoais, quase não tem função: exprime o envolvimento afetivo de quem fala (<i>quid mihi Celsus agit?</i>, "e o meu Celso, como vai?", verso de Horácio citado por Bennett § 188.2.b). Traduza-o livremente ou omita-o.</p>
'''),
        ('Duplo dativo, dativo com adjetivos e com verbos', f'''
<h3>Dativo de finalidade e o duplo dativo</h3>
<p>Um substantivo abstrato no dativo pode indicar <b>a finalidade</b> ou <b>o efeito</b>: "para quê" algo serve ou "como o quê" algo funciona. Esse dativo vem quase sempre acompanhado de um segundo dativo, o da pessoa interessada; daí o nome escolar de <b>duplo dativo</b>. O verbo mais comum é <i>esse</i>, mas aparecem também <i>venīre, mittere, relinquere, dare, habēre</i>. O dativo de finalidade é, em regra, <b>singular, abstrato e sem adjetivo</b>, salvo adjetivos de grau como <i>magnō, maximō</i> (A&G § 382, nota 1). Kennedy (§ 226) dá um exemplo de César: <i>equitātum auxiliō Caesarī mīsērunt</i>, "enviaram a cavalaria em auxílio de César".</p>
{tabela(['Dativo de finalidade', 'Expressão', 'Tradução natural'], [
    ['<i>auxiliō</i>', '<i>sociīs auxiliō venīre</i>', 'vir em auxílio dos aliados'],
    ['<i>praesidiō</i>', '<i>urbī praesidiō esse</i>', 'servir de proteção à cidade'],
    ['<i>ūsuī</i>', '<i>nōbīs magnō ūsuī esse</i>', 'ser de grande utilidade para nós'],
    ['<i>cūrae</i>', '<i>mihi cūrae esse</i>', 'ser motivo de preocupação para mim; preocupar-me'],
    ['<i>odiō</i>', '<i>omnibus odiō esse</i>', 'ser odiado por todos'],
    ['<i>exemplō</i>', '<i>cēterīs exemplō esse</i>', 'servir de exemplo aos outros'],
    ['<i>dōnō</i>', '<i>amīcō dōnō dare</i>', 'dar de presente a um amigo'],
    ['<i>salūtī</i>', '<i>patriae salūtī esse</i>', 'ser a salvação da pátria'],
], 'Os duplos dativos mais frequentes')}
<p>Traduzir palavra por palavra ("é para preocupação para mim") produz um português impossível. Monte a ideia: a pessoa no dativo é o interessado, o abstrato no dativo é o papel que a coisa desempenha. <i>Haec rēs mihi cūrae est</i>: "isto me preocupa". A velha pergunta proverbial <i>cui bonō?</i>, "a quem isso aproveita?", é um duplo dativo sem verbo (Bennett § 191.2.a).</p>
<h3>Dativo com adjetivos</h3>
<p>Adjetivos que indicam <b>amizade e hostilidade, semelhança e igualdade, proximidade, utilidade e adequação</b> levam dativo (Bennett § 192; A&G § 384): <i>amīcus, inimīcus, fidēlis, cārus, grātus, molestus; similis, pār, aequālis; proximus, fīnitimus, vīcīnus; ūtilis, inūtilis, idōneus, aptus, facilis, difficilis, necessārius</i>. A lógica é a mesma do dativo de interesse: alguém é "amigo <b>para</b>", "útil <b>para</b>", "próximo <b>a</b>".</p>
{exemplos([('Hīc locus castrīs <b>idōneus</b> est.', 'Este lugar é apropriado para um acampamento. (<i>castra, -ōrum</i>, acampamento)'), ('Germānī Rhēnō <b>proximī</b> sunt.', 'Os germanos são vizinhos do Reno (estão junto ao Reno).'), ('Liber <b>discipulīs</b> ūtilis est.', 'O livro é útil aos alunos.'), ('Tribūnus <b>nōbīs</b> amīcus est.', 'O tribuno é amigável conosco.')])}
{observacao('Amīcus Cicerōnī ou Cicerōnis amīcus?', 'Como adjetivo, <i>amīcus</i> leva dativo: <i>amīcus Cicerōnī</i>, "favorável a Cícero". Como substantivo, leva genitivo: <i>Cicerōnis amīcus</i>, "um amigo de Cícero" (A&G § 385.c). O mesmo vale para <i>inimīcus</i> e <i>familiāris</i>. Com adjetivos de adequação (<i>aptus, idōneus</i>), a finalidade também se exprime por <i>ad</i> + acusativo, sobretudo quando é uma coisa: <i>aptus ad rem mīlitārem</i> (A&G § 385.a).')}
<h3>Dativo com verbos intransitivos</h3>
<p>Este é o ponto em que o falante de português mais erra. Vários verbos que em português são transitivos diretos ("obedecer o pai" se diz, mas a norma pede "ao pai"; "ajudar", "persuadir", "perdoar alguém") são <b>intransitivos</b> em latim e levam o complemento no dativo. Bennett insiste em que eles não pedem dativo por causa do sentido português, mas porque em latim são intransitivos, construídos com um objeto indireto (§ 187.II, nota). Pense em cada um como "ser obediente <b>a</b>", "ser favorável <b>a</b>", "fazer mal <b>a</b>", "tornar algo convincente <b>para</b>".</p>
{tabela(['Verbo', 'Sentido literal', 'Exemplo', 'Tradução'], [
    ['<i>crēdō, -ere, crēdidī</i>', 'dar crédito a', '<i>Nēmō <b>mendācī</b> crēdit.</i>', 'Ninguém acredita no mentiroso.'],
    ['<i>pāreō, -ēre, pāruī</i>', 'ser obediente a', '<i>Mīlitēs <b>ducī</b> pārent.</i>', 'Os soldados obedecem ao comandante.'],
    ['<i>noceō, -ēre, nocuī</i>', 'fazer mal a', '<i>Fūmus <b>oculīs</b> nocet.</i>', 'A fumaça faz mal aos olhos.'],
    ['<i>placeō, -ēre, placuī</i>', 'ser agradável a', '<i>Haec fābula <b>puerīs</b> placet.</i>', 'Esta história agrada aos meninos.'],
    ['<i>faveō, -ēre, fāvī</i>', 'ser favorável a', '<i>Fortūna <b>fortibus</b> favet.</i>', 'A sorte favorece os corajosos.'],
    ['<i>persuādeō, -ēre, persuāsī</i>', 'tornar convincente para', '<i><b>Patrī</b> persuāsī.</i>', 'Persuadi meu pai.'],
    ['<i>ignōscō, -ere, ignōvī</i>', 'conceder perdão a', '<i>Rēx <b>captīvīs</b> ignōscit.</i>', 'O rei perdoa os prisioneiros.'],
    ['<i>imperō, -āre</i>', 'dar ordens a', '<i>Caesar <b>mīlitibus</b> imperat.</i>', 'César dá ordens aos soldados.'],
    ['<i>serviō, -īre</i>', 'ser escravo de, servir a', '<i><b>Patriae</b> servīmus.</i>', 'Servimos à pátria.'],
    ['<i>parcō, -ere, pepercī</i>', 'ter consideração por, poupar', '<i>Victor <b>victīs</b> pepercit.</i>', 'O vencedor poupou os vencidos.'],
    ['<i>resistō, -ere, restitī</i>', 'opor-se a', '<i><b>Hostibus</b> resistimus.</i>', 'Resistimos aos inimigos.'],
], 'Verbos intransitivos com dativo (os mais frequentes)')}
<p>E o contrário também acontece: verbos de sentido parecido são <b>transitivos</b> e levam acusativo: <i>iuvō</i> e <i>adiuvō</i> ("ajudar"), <i>laedō</i> ("ferir, prejudicar"), <i>iubeō</i> ("mandar"), <i>dēlectō</i> ("agradar, encantar"): <i>Deus fortēs iuvat</i>; <i>Fābula puerōs dēlectat</i> (A&G § 367.a; Kennedy § 217). Por isso não há atalho: o caso que o verbo pede se aprende com o verbo, e um bom dicionário o indica (<i>alicui</i> = com dativo; <i>aliquem</i> = com acusativo).</p>
<h3>Dativo com verbos compostos</h3>
<p>Muitos verbos compostos com <i>ad, ante, con-, in, inter, ob, post, prae, prō, sub, super</i> passam a levar dativo, porque o prefixo acrescenta uma relação "a, diante de, sobre" (Bennett § 187.III; A&G § 370). Os compostos de <i>sum</i> são os primeiros a aprender: <i>adsum</i> (estar presente, assistir a), <i>praesum</i> (estar à frente de, comandar), <i>dēsum</i> (faltar a), <i>obsum</i> (prejudicar), <i>prōsum</i> (ser útil a; presente <i>prōsum, prōdes, prōdest</i>), <i>intersum</i> (tomar parte em). Verbos transitivos compostos podem ter acusativo <b>e</b> dativo: <i>Caesar Labiēnum legiōnī praefēcit</i>, "César pôs Labieno no comando da legião" (<i>praeficiō, -ere, praefēcī</i>).</p>
{exemplos([('Cicerō <b>amīcīs</b> semper aderat.', 'Cícero sempre assistia os amigos (estava ao lado deles). (dativo com <i>adsum</i>)'), ('Labiēnus <b>legiōnī</b> praeest.', 'Labieno comanda a legião.'), ('Cōnsilium <b>tibi</b> nōn dēest.', 'Não te falta juízo. (<i>cōnsilium</i> é o sujeito; <i>tibi</i>, o dativo com <i>dēsum</i>)'), ('Haec lēx <b>cīvibus</b> prōdest.', 'Esta lei é útil aos cidadãos.')])}
{dica('<b>Para mais tarde.</b> Esses verbos, por não terem objeto direto, só têm passiva impessoal (<i>mihi persuādētur</i>, "estou sendo persuadido"; Bennett § 187.II.b): você verá isso no capítulo 24. E há um dativo que indica <b>quem deve fazer</b> algo, o dativo de agente com o gerundivo (<i>haec nōbīs agenda sunt</i>, "isto deve ser feito por nós"; Bennett § 189), assunto do capítulo 31.')}
'''),
        ('Lendo frases autênticas: um salmo e o Evangelho de João', f'''
<p>Duas frases curtas da Vulgata mostram, uma, o genitivo objetivo, a outra, o dativo de posse. A primeira é o último versículo do Salmo 110 (na numeração da Vulgata), uma das sentenças mais citadas da literatura sapiencial:</p>
{exemplos([('Initium sapientiae timor Dominī.', 'O princípio da sabedoria é o temor do Senhor. (Sl 110,10 [111,10], Vulgata)')])}
{analise('Sl 110,10, palavra a palavra', [
    ('Initium', 'initium, -ī (n.), início, princípio', 'nominativo singular, 2ª declinação', 'predicativo (a frase não tem verbo expresso; subentende-se <i>est</i>)'),
    ('sapientiae', 'sapientia, -ae (f.), sabedoria', 'genitivo singular, 1ª declinação', 'adjunto de <i>initium</i>: "o princípio da sabedoria"'),
    ('timor', 'timor, -ōris (m.), temor, medo', 'nominativo singular, 3ª declinação', 'sujeito'),
    ('Dominī', 'dominus, -ī (m.), senhor; o Senhor', 'genitivo singular, 2ª declinação', '<b>genitivo objetivo</b> de <i>timor</i>: o Senhor é temido'),
])}
<p>A frase é nominal: em máximas desse tipo o latim dispensa com frequência o <i>est</i>, e você o acrescenta na tradução. Qual dos nominativos é o sujeito? A tradição lê "o temor do Senhor é o princípio da sabedoria": <i>timor Dominī</i> é aquilo de que se fala, e <i>initium sapientiae</i> é o que se diz dele. O ponto principal, porém, é <i>Dominī</i>. Pelo teste do Pe. Ravizza, "o temor do Senhor" vira "alguém teme o Senhor", e não "o Senhor teme": o genitivo é <b>objetivo</b>. O português conserva a mesma ambiguidade aparente ("temor do Senhor"), e é o sentido que a resolve.</p>
<p>A segunda frase é o versículo que apresenta João Batista no prólogo do quarto Evangelho:</p>
{exemplos([('Fuit homo missus ā Deō, cui nōmen erat Ioannes.', 'Houve um homem enviado por Deus, cujo nome era João (literalmente: ao qual o nome era João). (Jo 1,6, Vulgata)')])}
{analise('Jo 1,6, palavra a palavra', [
    ('Fuit', 'sum, esse, fuī, ser, haver', 'perfeito, 3ª pessoa do singular (capítulo 13)', 'verbo da oração principal: "houve, existiu"'),
    ('homo', 'homō, -inis (m.), ser humano, homem', 'nominativo singular, 3ª declinação', 'sujeito de <i>fuit</i>'),
    ('missus', 'mittō, -ere, mīsī, missum, enviar', 'particípio perfeito passivo, nominativo masculino singular (capítulo 29)', 'concorda com <i>homo</i>: "enviado"'),
    ('ā Deō', 'ā/ab (prep. + abl.); deus, -ī', 'ablativo singular com <i>ā</i>', 'agente: "por Deus" (capítulo 23)'),
    ('cui', 'quī, quae, quod, que, o qual', 'dativo singular masculino (capítulo 16)', '<b>dativo de posse</b> com <i>erat</i>; antecedente <i>homo</i>'),
    ('nōmen', 'nōmen, -inis (n.), nome', 'nominativo singular, 3ª declinação', 'sujeito de <i>erat</i>'),
    ('erat', 'sum, esse', 'imperfeito, 3ª pessoa do singular (capítulo 12)', 'verbo da oração relativa'),
    ('Ioannes', 'Ioannes, -is (m.), João', 'nominativo singular', 'aposto de <i>nōmen</i>: o nome próprio fica no nominativo'),
])}
<p>A construção <i>cui nōmen erat</i> é a mesma de <i>mihi nōmen est</i>: o possuidor no dativo, o nome como sujeito de <i>esse</i>. A tradução portuguesa usual, "cujo nome era", troca o dativo por um pronome possessivo, que é a forma natural de dizer posse numa oração relativa em português. Note ainda que o nome próprio, <i>Ioannes</i>, ficou no nominativo, e não atraído para o dativo (<i>cui Ioanni</i>): as duas possibilidades existem, e Bennett (§ 190.1) observa que a atração ao dativo é a mais comum (cf. A&G § 373.a); a Vulgata usa aqui o nominativo.</p>
{diagrama_frase([('Sociī', 'nominativo · sujeito'), ('Rōmānīs', 'dativo · interessado (a quem)'), ('nāvēs', 'acusativo · objeto direto'), ('auxiliō', 'dativo · finalidade (para quê)'), ('mīsērunt', 'verbo · "enviaram"')], 'Um duplo dativo: <i>Sociī Rōmānīs nāvēs auxiliō mīsērunt</i> = Os aliados enviaram navios em auxílio dos romanos. Os dois dativos respondem a perguntas diferentes: a quem? e para quê?')}
<h3>Resumo</h3>
<ul>
<li><b>Genitivo</b>: liga nome a nome. Posse (<i>domus rēgis</i>, <i>rēgis est</i>), partitivo (<i>pars mīlitum, nihil novī, satis pecūniae</i>; mas <i>ūnus ex mīlitibus</i>), subjetivo e objetivo (<i>amor patris</i>), qualidade com adjetivo (<i>vir magnae virtūtis</i>), valor (<i>magnī, parvī aestimāre</i>), com adjetivos de desejo, conhecimento, lembrança e plenitude.</li>
<li><b>Dativo</b>: a pessoa interessada. Objeto indireto, posse com <i>esse</i> (<i>mihi est</i>), interesse, referência, finalidade (<i>auxiliō, ūsuī, cūrae</i>), com adjetivos de amizade, semelhança, proximidade e utilidade, com os intransitivos <i>crēdō, pāreō, noceō, placeō, faveō, persuādeō, ignōscō, imperō</i> e com compostos como <i>adsum, praesum, dēsum</i>.</li>
<li>O caso que um verbo ou adjetivo pede aprende-se com a palavra, no dicionário; o "de" e o "a" do português não decidem.</li>
</ul>
'''),
    ],
    erros_comuns=[
        ('Traduzir para o genitivo todo "de" do português: "venho de Roma" → <i>Rōmae veniō</i>; "estátua de ouro" → <i>statua aurī</i>.', 'O genitivo liga um nome a outro nome (posse, parte, objeto de um sentimento). Origem e afastamento são ablativo (<i>Rōmā veniō</i>; <i>ex Ītaliā</i>), e a matéria se diz com <i>ex</i> + ablativo ou com um adjetivo (<i>statua ex aurō</i>, <i>statua aurea</i>): capítulo 21. Pergunte qual é a relação, não qual preposição o português usaria.'),
        ('Pôr no acusativo o complemento de <i>crēdō, pāreō, persuādeō, noceō, ignōscō</i>: <i>Mīlitēs ducem pārent</i>; <i>Patrem persuāsī</i>.', 'Esses verbos são intransitivos em latim e levam dativo: <i>Mīlitēs ducī pārent</i>; <i>Patrī persuāsī</i>. Ajuda traduzir mentalmente pelo sentido literal: "ser obediente <b>ao</b> comandante", "tornar a ideia convincente <b>para o</b> pai".'),
        ('Generalizar a regra e pôr no dativo o objeto de <i>iuvō, laedō, iubeō, dēlectō</i>: <i>Deus fortibus iuvat</i>.', 'Esses são transitivos e levam acusativo: <i>Deus fortēs iuvat</i>; <i>Fābula puerōs dēlectat</i>. Não há regra de sentido que separe os dois grupos: aprenda o caso com o verbo (o dicionário indica <i>alicui</i> ou <i>aliquem</i>).'),
        ('Procurar em <i>Mihi est liber</i> um sujeito "eu", ou traduzir "a mim é um livro".', 'O sujeito é <i>liber</i>, e o verbo concorda com ele (<i>mihi sunt librī</i>). O dativo indica o possuidor, que em português vira sujeito de "ter": "eu tenho um livro". Num relativo, o mesmo dativo vira "cujo": <i>cui nōmen erat</i>, "cujo nome era".'),
        ('No duplo dativo, pluralizar ou adjetivar o dativo de finalidade (<i>sociīs magnīs auxiliīs vēnit</i>) ou traduzir literalmente "veio para auxílio para os aliados".', 'O dativo de finalidade fica no singular e só admite adjetivos de grau (<i>magnō ūsuī</i>). Na tradução, junte os dois dativos numa expressão portuguesa: "veio em auxílio dos aliados", "isto me preocupa" (<i>mihi cūrae est</i>), "é de grande utilidade para nós" (<i>nōbīs magnō ūsuī est</i>).'),
        ('Usar o partitivo onde o latim faz concordar: <i>omnēs mīlitum</i>, <i>nihil bonus</i>, <i>nihil dulcis</i>.', '"Todos os soldados" é <i>omnēs mīlitēs</i>, porque <i>omnēs</i> abrange o todo. Com <i>nihil</i>, o adjetivo de 1ª classe vai para o genitivo partitivo (<i>nihil bonī</i>), mas o de 2ª classe concorda com o neutro (<i>nihil dulce</i>, <i>nihil dulcius</i>). Com cardinais, prefira <i>ex</i> + ablativo: <i>ūnus ex mīlitibus</i>.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Três genitivos e um dativo',
            'Analise e traduza, na ordem latina: <i lang="la">Pars mīlitum, cupida glōriae, ducī nōn pāruit.</i> Vocabulário: <i>pars, partis</i> (f.), parte; <i>mīles, -itis</i> (m.), soldado; <i>cupidus, -a, -um</i>, desejoso; <i>glōria, -ae</i>, glória; <i>dux, ducis</i> (m.), comandante; <i>pāreō, -ēre, pāruī</i>, obedecer.', [
            ('Qual é o verbo, e que caso ele pede?', '<i>Pāruit</i>, perfeito de <i>pāreō</i>, 3ª pessoa do singular: "obedeceu". <i>Pāreō</i> é intransitivo e leva <b>dativo</b>; espere, então, um dativo, não um acusativo.'),
            ('Qual é o sujeito? Por que o verbo está no singular se quem desobedece são soldados?', 'O sujeito é <i>pars</i>, nominativo singular: "uma parte". O verbo concorda gramaticalmente com <i>pars</i>, e não com <i>mīlitum</i>.'),
            ('Que tipo de genitivo é <i>mīlitum</i>?', 'Genitivo plural de <i>mīles</i>, dependente de <i>pars</i>: <b>partitivo</b>, o todo de que se toma a parte. "Parte dos soldados".'),
            ('E <i>cupida glōriae</i>?', '<i>Cupida</i> é nominativo feminino singular: concorda com <i>pars</i> (feminino), não com <i>mīlitum</i>. <i>Glōriae</i> é genitivo pedido pelo adjetivo de desejo <i>cupidus</i>. "Desejosa de glória".'),
            ('E <i>ducī</i>?', 'Dativo singular de <i>dux</i>, complemento de <i>pāruit</i>: "ao comandante".'),
            ('Monte a tradução.', '"Uma parte dos soldados, desejosa de glória, não obedeceu ao comandante." Em português pode-se pôr o adjetivo no plural pelo sentido ("parte dos soldados, desejosos de glória"), mas em latim <i>cupida</i> concorda com <i>pars</i>.'),
        ]),
        pratica_guiada('Prática guiada 2 · Posse, interesse e finalidade',
            'Analise e traduza: <i lang="la">Rōmānīs nūlla classis erat; itaque sociī eīs nāvēs auxiliō mīsērunt.</i> Vocabulário: <i>nūllus, -a, -um</i>, nenhum; <i>classis, -is</i> (f.), frota; <i>itaque</i>, por isso; <i>socius, -ī</i> (m.), aliado; <i>nāvis, -is</i> (f.), navio; <i>auxilium, -ī</i> (n.), auxílio; <i>mittō, -ere, mīsī</i>, enviar.', [
            ('Na primeira oração, qual é o sujeito de <i>erat</i>?', '<i>Nūlla classis</i>, nominativo singular: "nenhuma frota". <i>Rōmānīs</i> não pode ser sujeito: é dativo (ou ablativo) plural.'),
            ('Que dativo é <i>Rōmānīs</i>?', 'Com <i>esse</i> e uma coisa como sujeito, é <b>dativo de posse</b>: "para os romanos não havia frota" = "os romanos não tinham frota".'),
            ('Na segunda oração, quantos dativos há, e o que cada um responde?', 'Dois: <i>eīs</i> (dativo plural de <i>is</i>, capítulo 14), a quem se envia, isto é, a pessoa interessada (os romanos); e <i>auxiliō</i>, para quê se envia: <b>dativo de finalidade</b>. Juntos formam um duplo dativo.'),
            ('E <i>nāvēs</i>?', 'Acusativo plural de <i>nāvis</i> (tema em <i>-i</i>, capítulo 10): o objeto direto de <i>mīsērunt</i>. A forma <i>nāvēs</i> também poderia ser nominativo, mas o sujeito já é <i>sociī</i>.'),
            ('Monte a tradução.', '"Os romanos não tinham frota; por isso os aliados lhes enviaram navios em auxílio" (ou "enviaram navios para ajudá-los").'),
        ], 'Repare que as duas orações usam o dativo com funções diferentes, posse na primeira, interesse e finalidade na segunda, e que nenhuma delas se traduz com "a" ou "para" palavra por palavra.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Que genitivo é este?', 'Classifique o genitivo destacado (posse, predicativo, partitivo, subjetivo, objetivo, qualidade, valor, com adjetivo) e traduza a expressão. Vocabulário: <i>cōnsul, -is</i>, cônsul; <i>prūdentia, -ae</i>, sabedoria prática; <i>cibus, -ī</i>, comida; <i>aestimō, -āre</i>, avaliar.', [
            ('<i>pars <b>cīvium</b></i>', 'Partitivo: o todo de que se toma uma parte. "Parte dos cidadãos".'),
            ('<i>amor <b>patriae</b></i>', 'Objetivo: a pátria é amada, não ama. "O amor à pátria".'),
            ('<i>domus <b>cōnsulis</b></i>', 'Posse: "a casa do cônsul".'),
            ('<i>vir <b>summae prūdentiae</b></i>', 'Qualidade, com o adjetivo <i>summae</i> obrigatório: "um homem de enorme sabedoria".'),
            ('<i>Satis <b>cibī</b> habēmus.</i>', 'Partitivo depois do advérbio de quantidade <i>satis</i>: "Temos comida suficiente."'),
            ('<i>Mīles cupidus <b>glōriae</b> est.</i>', 'Genitivo com adjetivo de desejo (<i>cupidus</i>): "O soldado é ávido de glória."'),
            ('<i>Hanc domum <b>magnī</b> aestimō.</i>', 'Valor (genitivo de apreciação): "Tenho esta casa em grande estima" ou "Dou muito valor a esta casa."'),
            ('<i>Haec vīlla <b>rēgīnae</b> est.</i>', 'Posse predicativa, com <i>esse</i>: "Esta casa de campo é da rainha." Atenção: <i>rēgīnae</i> também poderia ser dativo de posse ("a rainha tem esta casa"), porque as formas coincidem na 1ª declinação. Com o demonstrativo <i>haec</i> apontando uma casa já conhecida, a pergunta é "de quem é?", e a leitura natural é o genitivo.'),
            ('<i>puer <b>decem annōrum</b></i>', 'Qualidade com numeral, indicando a idade: "um menino de dez anos".'),
            ('<i>adventus <b>hostium</b></i>', 'Subjetivo: os inimigos chegam. "A chegada dos inimigos".'),
        ]),
        exercicio('Exercício 2 · Que dativo é este?', 'Classifique o dativo destacado (objeto indireto, posse, interesse, finalidade, com adjetivo, com verbo intransitivo, com composto) e traduza a frase. Vocabulário: <i>discipulus, -ī</i>, aluno; <i>fīlia, -ae</i>, filha; <i>serō, -ere</i>, plantar; <i>legiō, -ōnis</i>, legião; <i>castra, -ōrum</i> (n. pl.), acampamento.', [
            ('<i>Magister <b>discipulīs</b> librōs dat.</i>', 'Objeto indireto: "O professor dá livros aos alunos."'),
            ('<i><b>Rēgī</b> trēs fīliae erant.</i>', 'Posse com <i>esse</i> (o sujeito é <i>trēs fīliae</i>, e por isso o verbo está no plural): "O rei tinha três filhas."'),
            ('<i>Mīlitēs <b>ducī</b> pārent.</i>', 'Com verbo intransitivo (<i>pāreō</i>): "Os soldados obedecem ao comandante."'),
            ('<i>Haec rēs <b>nōbīs magnō ūsuī</b> est.</i>', 'Duplo dativo: <i>nōbīs</i> é o interessado e <i>ūsuī</i> a finalidade, com o adjetivo de grau <i>magnō</i>. "Isto nos é de grande utilidade."'),
            ('<i>Labiēnus <b>legiōnī</b> praeest.</i>', 'Com composto de <i>sum</i> (<i>praesum</i>): "Labieno comanda a legião."'),
            ('<i>Agricola nōn <b>sibi</b> sed <b>fīliīs</b> arborēs serit.</i>', 'Interesse (vantagem): a frase estaria completa sem os dativos. "O agricultor planta árvores não para si, mas para os filhos."'),
            ('<i>Iste locus <b>castrīs</b> idōneus est.</i>', 'Com adjetivo de adequação (<i>idōneus</i>): "Esse lugar é apropriado para um acampamento."'),
            ('<i>Nēmō <b>tibi</b> crēdit.</i>', 'Com verbo intransitivo (<i>crēdō</i>): "Ninguém acredita em você."'),
        ]),
        exercicio('Exercício 3 · Genitivo ou dativo?', 'Complete com a forma correta da palavra entre parênteses e diga por quê. Vocabulário: <i>fugiō, -ere, fūgī</i>, fugir; <i>soror, -ōris</i>, irmã; <i>salūs, -ūtis</i> (f.), saúde, salvação; <i>pāx, pācis</i>, paz; <i>cūra, -ae</i>, preocupação; <i>sapientia, -ae</i>, sabedoria.', [
            ('<i>Fīlius ___ pāret.</i> (pater)', '<i>patrī</i>: dativo exigido por <i>pāreō</i>. "O filho obedece ao pai."'),
            ('<i>Pars ___ fūgit.</i> (mīles)', '<i>mīlitum</i>: genitivo plural partitivo depois de <i>pars</i>. "Parte dos soldados fugiu."'),
            ('<i>___ est soror.</i> (ego)', '<i>Mihi</i>: dativo de posse com <i>esse</i>. "Eu tenho uma irmã."'),
            ('<i>Dux cupidus ___ nōn est.</i> (pāx)', '<i>pācis</i>: genitivo pedido pelo adjetivo de desejo <i>cupidus</i>. "O comandante não deseja a paz."'),
            ('<i>Tua salūs mihi ___ est.</i> (cūra)', '<i>cūrae</i>: dativo de finalidade, formando duplo dativo com <i>mihi</i>. "A tua saúde me preocupa."'),
            ('<i>Ille vir magnae ___ est.</i> (sapientia)', '<i>sapientiae</i>: genitivo de qualidade, com o adjetivo <i>magnae</i>, em posição de predicativo. "Aquele homem é de grande sabedoria."'),
            ('<i>Nihil ___ audiō.</i> (novus)', '<i>novī</i>: genitivo partitivo de um adjetivo de 1ª classe depois de <i>nihil</i>. "Não ouço nada de novo."'),
            ('<i>Victor ___ pepercit.</i> (victī, os vencidos)', '<i>victīs</i>: dativo exigido por <i>parcō</i>. "O vencedor poupou os vencidos."'),
            ('<i>Hīc liber ___ ūtilis est.</i> (puer)', '<i>puerō</i>: dativo com o adjetivo <i>ūtilis</i>. "Este livro é útil ao menino."'),
            ('<i>Fīlius ___ similis est.</i> (pater)', '<i>patris</i>: com <i>similis</i> referido a pessoa, o genitivo é o uso preferido de Cícero (Bennett § 204.3); <i>patrī</i> também se encontra. "O filho é parecido com o pai."'),
        ]),
        exercicio('Exercício 4 · Traduza', 'Antes de traduzir, identifique cada genitivo e cada dativo. Vocabulário: <i>exercitus, -ūs</i>, exército; <i>parum</i>, pouco, pouco demais; <i>frūmentum, -ī</i>, trigo; <i>quod</i>, porque; <i>saepe</i>, muitas vezes; <i>ager, agrī</i>, campo; <i>lēx, lēgis</i>, lei.', [
            ('<i>Caesarī magnus exercitus erat, sed parum frūmentī.</i>', '<i>Caesarī</i>: dativo de posse; <i>frūmentī</i>: genitivo partitivo depois de <i>parum</i>. "César tinha um grande exército, mas pouco trigo."'),
            ('<i>Mīlitēs ducī nōn crēdunt, quod dux eīs saepe nocuit.</i>', '<i>Ducī</i>: dativo com <i>crēdō</i>; <i>eīs</i>: dativo com <i>noceō</i>. "Os soldados não confiam no comandante, porque o comandante muitas vezes os prejudicou."'),
            ('<i>Hīc ager nōbīs magnae cūrae est.</i>', 'Duplo dativo (<i>nōbīs</i>, interessado; <i>cūrae</i>, finalidade, com o adjetivo de grau <i>magnae</i>). "Este campo nos dá grande preocupação" ou "Nós nos preocupamos muito com este campo."'),
            ('<i>Amor patriae Rōmānīs maximus erat.</i>', '<i>Patriae</i>: genitivo objetivo; <i>Rōmānīs</i>: dativo de posse (ou de referência). "Os romanos tinham um enorme amor à pátria."'),
            ('<i>Bonī cīvēs lēgibus pārent et patriae serviunt.</i>', '<i>Lēgibus</i> e <i>patriae</i>: dativos exigidos por <i>pāreō</i> e <i>serviō</i>. "Os bons cidadãos obedecem às leis e servem à pátria." (<i>Patriae</i> não é genitivo: não há substantivo de que dependa, e <i>serviunt</i> pede dativo.)'),
        ]),
        exercicio('Exercício 5 · Retroversão', 'Passe para o latim, usando o vocabulário deste capítulo.', [
            ('Eu tenho dois irmãos.', '<i>Mihi sunt duo frātrēs.</i> (dativo de posse; o verbo concorda com <i>frātrēs</i>) Também correto: <i>Duōs frātrēs habeō.</i>'),
            ('A rainha veio em auxílio da cidade.', '<i>Rēgīna urbī auxiliō vēnit.</i> Duplo dativo: <i>urbī</i> (interessado) e <i>auxiliō</i> (finalidade, no singular).'),
            ('Ninguém persuade o meu pai.', '<i>Nēmō patrī meō persuādet.</i> <i>Persuādeō</i> leva dativo; o português "persuadir alguém" engana.'),
            ('Um dos soldados era experiente na guerra.', '<i>Ūnus ex mīlitibus perītus bellī erat.</i> Com o cardinal, <i>ex</i> + ablativo; <i>perītus</i> pede genitivo.'),
            ('Dou muito valor aos teus conselhos.', '<i>Tua cōnsilia magnī aestimō</i> (ou <i>faciō</i>). Genitivo de valor.'),
            ('Este lugar fica perto do mar.', '<i>Hīc locus marī proximus est.</i> <i>Proximus</i> leva dativo (Bennett § 192.1).'),
        ]),
        exercicio('Exercício 6 · Leitura autêntica', 'Identifique os genitivos e dativos e traduza. As frases foram conferidas na Vulgata Clementina e na Latin Library; as glosas dão o que ainda não foi estudado.', [
            ('<i>Beātī pauperēs spīritū: quoniam ipsōrum est rēgnum caelōrum.</i> (Mt 5,3) Vocabulário: <i>beātus</i>, feliz, bem-aventurado; <i>pauper, -eris</i>, pobre; <i>spīritū</i>, "em espírito" (ablativo, capítulo 21); <i>quoniam</i>, porque; <i>ipse</i>, ele mesmo (capítulo 15); <i>caelum, -ī</i>, céu (aqui no plural).', '<i>Ipsōrum</i>: genitivo de posse <b>predicativo</b>, com <i>est</i>: "deles é". <i>Caelōrum</i>: genitivo dependente de <i>rēgnum</i>, "o reino dos céus". Frase nominal no início (subentenda <i>sunt</i>): "Bem-aventurados os pobres em espírito, porque deles é o reino dos céus."'),
            ('<i>Dominus regit mē, et nihil mihi dēerit.</i> (Sl 22,1 [23,1], Vulgata) Vocabulário: <i>regō, -ere</i>, guiar, governar; <i>dēerit</i>, futuro de <i>dēsum</i>, faltar.', '<i>Mihi</i>: dativo com o composto <i>dēsum</i>, "faltar a alguém"; <i>nihil</i> é o sujeito de <i>dēerit</i>. "O Senhor me guia, e nada me faltará."'),
            ('<i>Fuit homo missus ā Deō, cui nōmen erat Ioannes.</i> (Jo 1,6)', '<i>Cui</i>: dativo de posse com <i>erat</i>; o nome fica no nominativo. "Houve um homem enviado por Deus, cujo nome era João." (Veja a análise na seção 6.)'),
            ('<i>Hōrum omnium fortissimī sunt Belgae.</i> (César, <i>BG</i> 1.1.3) Vocabulário: <i>hīc, haec, hōc</i>, este (capítulo 15); <i>omnis, -e</i>, todo; <i>fortissimus</i>, superlativo de <i>fortis</i> (capítulo 18); <i>Belgae, -ārum</i>, os belgas.', '<i>Hōrum omnium</i>: genitivo plural <b>partitivo</b>, dependente do superlativo <i>fortissimī</i>: "de todos estes" (César acabou de nomear os três povos da Gália). "De todos estes, os mais valentes são os belgas."'),
        ]),
    ],
    leituras=['bennett-new-latin-grammar', 'greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', 'ravizza-gramatica-latina', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'lhomond-epitome-historiae-sacrae', 'caesar-commentarii-de-bello-gallico-selecoes'],
    leituras_nota='Para consulta, os usos do genitivo estão em Bennett §§ 194–212 e os do dativo em §§ 186–193; em Allen e Greenough, §§ 341–385, com muitos exemplos de autores. O Pe. Ravizza trata os dois casos, em português, nos nn. 263–294. Para praticar a leitura, o <i>Epitome historiae sacrae</i> de Lhomond traz dativos de posse e de interesse em frases curtas, e o primeiro capítulo da <i>Guerra da Gália</i>, nas seleções comentadas, mostra o genitivo partitivo e os verbos com dativo na prosa de César. Na Vulgata, procure o dativo de posse com <i>nōmen</i> nos Evangelhos.',
)
