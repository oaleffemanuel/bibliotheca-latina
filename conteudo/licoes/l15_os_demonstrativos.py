from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

_CASOS5 = ('Nominativo', 'Genitivo', 'Dativo', 'Acusativo', 'Ablativo')
_COLS6 = ('M. sing.', 'F. sing.', 'N. sing.', 'M. pl.', 'F. pl.', 'N. pl.')

LICAO = dict(
    slug='15-os-demonstrativos', titulo='Demonstrativos; ipse e īdem',
    titulo_latim='Dē prōnōminibus dēmōnstrātīvīs', tempo='70 min',
    resumo='As palavras que apontam: hīc, iste e ille, que correspondem a "este", "esse" e "aquele"; is, ea, id, o demonstrativo fraco que serve de pronome de terceira pessoa; o intensivo ipse ("ele mesmo") e īdem ("o mesmo"). A declinação pronominal, com genitivo em -īus e dativo em -ī, o par hīc … ille ("este … aquele" = "o último … o primeiro") e uma frase de Cícero contra Catilina.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['pronomes demonstrativos', 'hīc, haec, hōc', 'iste, ista, istud', 'ille, illa, illud', 'is, ea, id', 'ipse', 'īdem', 'declinação pronominal', 'genitivo em -īus e dativo em -ī', 'adjetivos pronominais (ūnus, sōlus, tōtus, nūllus, alius, alter)', 'dêixis: este, esse, aquele', 'hīc … ille (o último … o primeiro)', 'eius e suus', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 14: os pronomes pessoais, possessivos e reflexivos (<i>ego, tū, sē, suus</i>), com o primeiro uso de <i>is, ea, id</i> como pronome de terceira pessoa. Também as declinações dos capítulos 4, 5 e 9, porque os demonstrativos tomam delas a maior parte das terminações.',
                       licoes=['14-os-pronomes-pessoais', '05-a-segunda-declinacao', '09-a-terceira-declinacao-temas-consonantais']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 66 (adjetivos com genitivo em -īus e dativo em -ī: alius, alter, ūllus, nūllus, uter, neuter, sōlus, tōtus, ūnus; nota 15: alterīus no lugar de alīus), § 86.1 (suus reflexivo; eius, eōrum não reflexivos), § 87 (hīc, iste, ille, is, īdem: os demonstrativos de 1ª, 2ª e 3ª pessoa e os paradigmas), § 88 (ipse), § 140 (advérbio hīc, "aqui"), § 246 (hīc … ille = o último … o primeiro; ille "o famoso"; iste depreciativo; atração ao gênero do predicativo), § 247 (is como antecedente do relativo e como pronome de 3ª pessoa), § 248 (īdem = "também"), § 249 (ipse; concordância com o sujeito em sē ipse)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 113 (os nove adjetivos com genitivo em -īus e dativo em -ī; o -ī- breve em verso, alterius), § 146 e notas (paradigmas; hīc = ho- + -ce; vogal originalmente breve em hīc, hōc; īdem = is + -dem, m → n antes de d: eundem), §§ 296–298 (usos: pronome e adjetivo; hīc, ille, iste, is; neutros referidos a uma ideia; īdem e ipse; mē ipse cōnsōlor)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='paradigmas de hīc, ille, iste, is (§ 94, pelo índice do OCR), īdem e ipse (§ 95, "definitive"), § 101 (adjetivos pronominais com -ius e -ī), §§ 318–321 (eius; hīc … ille em contraste, com o verso de Ovídio; iste depreciativo; ipse; īdem "também")', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 70 (os seis demonstrativos com tradução portuguesa: hīc "este", iste "esse", ille "aquele"; genitivo em -ius e dativo em -i; distinção entre ipse e idem; regra de concordância como pronome e como adjetivo); n. 76 (alter, alius, unus, totus, solus, nullus, ullus)', tipo='dominio_publico'),
        referencia('Cícero, In Catilinam I, 1–2', 'Marco Túlio Cícero', catalogo='cicero-in-catilinam-i-iv', url='https://www.thelatinlibrary.com/cicero/cat1.shtml', nota='frase analisada na seção 6 (§ 2) e expressões do § 1 (furor iste tuus) e do § 3 (huius ordinis, in hāc rē pūblicā), conferidas no texto da Latin Library; macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Declinar <i>hīc, haec, hōc</i>; <i>ille, illa, illud</i> (e <i>iste</i>); <i>is, ea, id</i>; <i>ipse</i> e <i>īdem</i>, reconhecendo o genitivo em <i>-īus</i> e o dativo em <i>-ī</i> da declinação pronominal.',
        'Escolher entre <i>hīc</i>, <i>iste</i> e <i>ille</i> pela distância em relação a quem fala e a quem ouve, comparando com "este", "esse" e "aquele".',
        'Usar os demonstrativos como adjetivos (concordando com o nome) e como pronomes (gênero e número do referente, caso da própria função).',
        'Distinguir <i>ipse</i> ("ele mesmo, em pessoa") de <i>īdem</i> ("o mesmo") e de <i>sē</i> (reflexivo).',
        'Interpretar o par <i>hīc … ille</i> como "este … aquele" = "o último … o primeiro" e analisar uma frase autêntica de Cícero.',
    ],
    secoes=[
        ('Apontar com palavras: este, esse, aquele', f'''
<p>Toda língua precisa de palavras que <b>apontam</b>: "este livro", "aquela casa", "isso que você disse". Elas não descrevem a coisa (não dizem se o livro é grande ou velho); dizem <b>onde</b> ela está em relação a quem fala, ou a que parte do discurso ela pertence. São os <b>demonstrativos</b>, e o fenômeno que eles expressam chama-se <b>dêixis</b>, do grego "mostrar". O português tem um sistema de três graus que o latim conhece muito bem, porque é de onde ele vem: "este" (perto de mim), "esse" (perto de você), "aquele" (longe de nós dois). O latim clássico tem os mesmos três graus, e as gramáticas os chamam, por isso, de demonstrativos da primeira, da segunda e da terceira pessoa (Bennett § 87; Allen e Greenough § 297):</p>
{comparacao('Os três graus da dêixis', ['Latim', 'Pessoa', 'Onde está a coisa', 'Português'], [
    ['hīc, haec, hōc', '1ª', 'perto de quem fala; aquilo de que se acaba de falar', 'este, esta, isto'],
    ['iste, ista, istud', '2ª', 'perto de quem ouve; o que é "seu", do interlocutor', 'esse, essa, isso'],
    ['ille, illa, illud', '3ª', 'longe dos dois; distante no tempo; famoso', 'aquele, aquela, aquilo'],
    ['is, ea, id', '—', 'não aponta lugar: só retoma algo já mencionado', 'ele, ela; esse, aquele (fraco); o (que)'],
])}
{exemplos([('<b>Hīc</b> liber meus est.', 'Este livro (aqui comigo) é meu.'),
           ('<b>Iste</b> liber tuus est.', 'Esse livro (aí com você) é seu.'),
           ('<b>Ille</b> liber magistrī est.', 'Aquele livro (lá longe) é do mestre.'),
           ('Puer librum habet; <b>eum</b> legit.', 'O menino tem um livro; lê-o. (<i>eum</i> só retoma <i>librum</i>, sem apontar lugar algum)')])}
<p>Repare que o falante de português do Brasil tem aqui uma pequena vantagem e uma pequena armadilha. A vantagem: o sistema de três graus é familiar. A armadilha: na fala cotidiana, "este" e "esse" se confundem, e quase sempre se diz "esse" para tudo. O latim não confunde: <i>hīc</i> é o que está do lado de quem fala, <i>iste</i> o que está do lado de quem ouve. Quando ler um diálogo, vale a pena perguntar a cada demonstrativo: perto de quem está essa coisa?</p>
<p>Todos os demonstrativos têm <b>dois usos</b>. Como <b>adjetivos</b>, acompanham um nome e concordam com ele em gênero, número e caso, como <i>bonus</i>: <i>hīc liber</i>, <i>haec puella</i>, <i>hōc templum</i>. Como <b>pronomes</b>, aparecem sozinhos e ocupam o lugar de um nome: tomam o gênero e o número da coisa ou pessoa a que se referem, e o caso da função que exercem na própria frase (Ravizza n. 70; Allen e Greenough § 296). <i>Hīc labōrat, ille dormit</i>: "este trabalha, aquele dorme". No neutro, o pronome designa uma ideia ou um conjunto de coisas: <i>hōc</i>, "isto"; <i>illud</i>, "aquilo"; <i>haec</i> (neutro plural), "estas coisas, isto tudo".</p>
{observacao('O latim não tem artigo, mas o português tirou o seu de ille', 'O latim clássico não tem artigo definido: <i>puer</i> é "menino", "o menino" ou "um menino", conforme o contexto. Mas no latim falado tardio <i>ille</i> foi perdendo a força de "aquele" e passou a acompanhar nomes como mera marca de coisa conhecida. Daí saíram, pela explicação tradicional da gramática histórica, o artigo português "o, a" (de <i>illum, illam</i>) e o pronome "ele" (de <i>ille</i>). Por isso, ao traduzir, não ponha "aquele" em toda ocorrência de <i>ille</i>; e, ao verter para o latim, não procure uma palavra para "o, a": ela não existe.')}
'''),
        ('Hīc, haec, hōc: o demonstrativo da primeira pessoa', f'''
<p><i>Hīc</i> aponta para o que está perto de quem fala, no espaço ("este livro aqui"), no tempo ("este ano") ou no pensamento ("isto que acabo de dizer"). É a palavra que um orador usa para o lugar onde está falando, o momento presente e a pessoa que ele indica com o dedo. A declinação é irregular e precisa ser decorada, mas tem lógica: o tema é <i>ho-</i>, e várias formas conservam uma antiga partícula <i>-ce</i> ("aqui"), reduzida a <i>-c</i>: <i>hi-c</i>, <i>hun-c</i>, <i>hae-c</i> (Allen e Greenough § 146, nota 1).</p>
{tabela_declinacao('hīc, haec, hōc, "este, esta, isto"', [
    ('hī<b>c</b>', 'hae<b>c</b>', 'hō<b>c</b>', 'h<b>ī</b>', 'h<b>ae</b>', 'hae<b>c</b>'),
    ('hu<b>ius</b>', 'hu<b>ius</b>', 'hu<b>ius</b>', 'h<b>ōrum</b>', 'h<b>ārum</b>', 'h<b>ōrum</b>'),
    ('hui<b>c</b>', 'hui<b>c</b>', 'hui<b>c</b>', 'h<b>īs</b>', 'h<b>īs</b>', 'h<b>īs</b>'),
    ('hun<b>c</b>', 'han<b>c</b>', 'hō<b>c</b>', 'h<b>ōs</b>', 'h<b>ās</b>', 'hae<b>c</b>'),
    ('h<b>ōc</b>', 'h<b>āc</b>', 'h<b>ōc</b>', 'h<b>īs</b>', 'h<b>īs</b>', 'h<b>īs</b>')],
    casos=_CASOS5, colunas=_COLS6)}
<p>Leia a tabela procurando o que você já sabe. O plural é quase todo da primeira e da segunda declinação: <i>hī, hōrum, hīs, hōs</i> lembram <i>dominī, dominōrum, dominīs, dominōs</i>, e <i>hae, hārum, hās</i> lembram <i>rosae, rosārum, rosās</i>. O singular é o que tem de ser decorado, sobretudo o genitivo <i>huius</i> e o dativo <i>huic</i>, iguais nos três gêneros. Os demonstrativos não têm vocativo.</p>
<p>Três formas pedem atenção especial. <b><i>Haec</i></b> tem dois valores: nominativo singular feminino ("esta") e nominativo ou acusativo plural neutro ("estas coisas"). <b><i>Hīs</i></b> é dativo ou ablativo plural dos três gêneros, como <i>-īs</i> nas duas primeiras declinações. E <b><i>hōc</i></b> serve a três casos: nominativo e acusativo neutro ("isto") e ablativo masculino ou neutro ("com este, por isto"); a frase decide. Sobre os macrons: este livro escreve <i>hīc</i> e <i>hōc</i>, como Bennett (§ 87), Allen e Greenough (§ 146) e o dicionário de Lewis e Short. Allen e Greenough observam, porém, que a vogal de <i>hīc, hōc</i> era originalmente breve e talvez nunca tenha deixado de sê-lo (§ 146, nota 1); por isso outros livros e dicionários imprimem <i>hic</i> e <i>hoc</i>. Não se preocupe com a divergência: na leitura, o que distingue as formas é a frase.</p>
{dica('<b>Pronome ou advérbio?</b> Existe também o <b>advérbio</b> <i>hīc</i>, "aqui" (Bennett § 140), da mesma família e escrito exatamente igual. A regra prática é sintática: se <i>hīc</i> concorda com um nome masculino ou funciona como sujeito ("este homem"), é pronome; se responde à pergunta "onde?", é advérbio. <i>Hīc puer hīc labōrat</i>: "este menino trabalha aqui".')}
{exemplos([('<b>Hīc</b> puer <b>huic</b> puellae rosam dat.', 'Este menino dá uma rosa a esta menina. (<i>hīc</i>: nom. sing. m.; <i>huic</i>: dat. sing. f., concordando com <i>puellae</i>)'),
           ('<b>Hōrum</b> mīlitum pater <b>hanc</b> lēgem laudat.', 'O pai destes soldados elogia esta lei.'),
           ('<b>Haec</b> verba <b>hīs</b> puerīs nārrō.', 'Conto estas palavras a estes meninos. (<i>haec</i>: ac. pl. neutro, com <i>verba</i>; não é feminino singular)'),
           ('<b>Hōc</b> videō, sed <b>hōc</b> librō nōn labōrō.', 'Vejo isto, mas não trabalho com este livro. (o primeiro <i>hōc</i> é acusativo neutro, objeto de <i>videō</i>; o segundo é ablativo, concordando com <i>librō</i>)')])}
'''),
        ('Ille, iste e a declinação pronominal', f'''
<p><i>Ille</i> aponta para o que está longe de quem fala e de quem ouve: "aquele homem lá", "aquele tempo", e também "aquele" que todo mundo conhece. <i>Iste</i> aponta para o que está perto do interlocutor ou pertence a ele: "esse teu livro". Os dois se declinam do mesmo modo, e esse modo é o padrão da chamada <b>declinação pronominal</b>:</p>
{tabela_declinacao('ille, illa, illud, "aquele, aquela, aquilo"', [
    ('ill<b>e</b>', 'ill<b>a</b>', 'ill<b>ud</b>', 'ill<b>ī</b>', 'ill<b>ae</b>', 'ill<b>a</b>'),
    ('ill<b>īus</b>', 'ill<b>īus</b>', 'ill<b>īus</b>', 'ill<b>ōrum</b>', 'ill<b>ārum</b>', 'ill<b>ōrum</b>'),
    ('ill<b>ī</b>', 'ill<b>ī</b>', 'ill<b>ī</b>', 'ill<b>īs</b>', 'ill<b>īs</b>', 'ill<b>īs</b>'),
    ('ill<b>um</b>', 'ill<b>am</b>', 'ill<b>ud</b>', 'ill<b>ōs</b>', 'ill<b>ās</b>', 'ill<b>a</b>'),
    ('ill<b>ō</b>', 'ill<b>ā</b>', 'ill<b>ō</b>', 'ill<b>īs</b>', 'ill<b>īs</b>', 'ill<b>īs</b>')],
    casos=_CASOS5, colunas=_COLS6)}
<p>Compare com <i>bonus, -a, -um</i>: quase tudo é igual. As diferenças são só três, e elas são a marca da declinação pronominal: o <b>genitivo singular em <i>-īus</i></b> (<i>illīus</i>, nos três gêneros, no lugar de <i>bonī, bonae, bonī</i>); o <b>dativo singular em <i>-ī</i></b> (<i>illī</i>, nos três gêneros, no lugar de <i>bonō, bonae, bonō</i>); e o <b>neutro singular em <i>-ud</i></b> (<i>illud</i>, no lugar de *<i>illum</i>). O nominativo masculino <i>ille</i> também é irregular. <i>Iste, ista, istud</i> segue exatamente o mesmo modelo: <i>istīus, istī, istum, istō</i>; <i>istī, istae, ista</i> e assim por diante.</p>
<p>A forma que mais engana é <b><i>illī</i></b> (e <i>istī</i>): pode ser <b>dativo singular</b> de qualquer gênero ("àquele, àquela") ou <b>nominativo plural masculino</b> ("aqueles"). Em <i>illī puellae</i> é dativo, porque concorda com <i>puellae</i> (dat. sing. f.); em <i>illī puerī</i>, sozinho, pode ser nominativo plural; o verbo decide. O genitivo <i>illīus</i>, por sua vez, não tem rival: é sempre genitivo singular.</p>
{observacao('Nove adjetivos que se declinam como ille', 'Alguns adjetivos muito usados tomam o genitivo em <i>-īus</i> e o dativo em <i>-ī</i> no singular, embora sejam, no resto, adjetivos de primeira classe: <i>ūnus</i> (um, um só), <i>sōlus</i> (só), <i>tōtus</i> (todo, inteiro), <i>ūllus</i> (algum, com negação), <i>nūllus</i> (nenhum), <i>alius</i> (outro), <i>alter</i> (o outro, de dois), <i>uter</i> (qual dos dois?) e <i>neuter</i> (nenhum dos dois). Assim: <i>ūnīus fīliae</i>, "de uma só filha"; <i>nūllī puerō</i>, "a nenhum menino"; <i>sōlī Deō</i>, "só a Deus"; <i>tōtīus oppidī</i>, "da cidade inteira". O plural é regular, como o de <i>bonus</i> (Bennett § 66; Allen e Greenough § 113). <i>Alius</i> tem o neutro <i>aliud</i>, e no genitivo usa-se quase sempre <i>alterīus</i>. Por ora basta reconhecer essas formas quando aparecerem; os numerais (<i>ūnus</i>) voltam no capítulo 19, e <i>uter</i> no capítulo 17. Na poesia, o <i>-ī-</i> do genitivo pode ser breve: <i>alterius</i>, <i>utrius</i> (Allen e Greenough § 113 c).')}
<p>Além de apontar para o que está longe, <i>ille</i> e <i>iste</i> adquirem um colorido afetivo que vale a pena perceber na leitura (Bennett § 246.3–4; Allen e Greenough § 297 b–c). <i>Ille</i>, geralmente depois do nome, significa "aquele famoso": <i>Solōn ille</i>, "o célebre Sólon". <i>Iste</i>, ao contrário, por apontar o lado do interlocutor, é a palavra do advogado contra o adversário, e muitas vezes soa depreciativa: "esse sujeito aí". Cícero abre o primeiro discurso contra Catilina perguntando por quanto tempo ainda <i>furor iste tuus</i>, "essa tua loucura", vai zombar de nós (<i>Cat.</i> 1.1); <i>iste</i> e <i>tuus</i> juntos apontam a loucura do lado do acusado, com desprezo.</p>
{exemplos([('Mīlitēs <b>illum</b> ducem laudant.', 'Os soldados elogiam aquele general.'),
           ('Nōmen <b>illīus</b> poētae clārum est.', 'O nome daquele poeta é famoso.'),
           ('<b>Illī</b> puellae librum dō; <b>illī</b> puerī nōn legunt.', 'Dou um livro àquela menina; aqueles meninos não leem. (o primeiro <i>illī</i> é dat. sing. f.; o segundo, nom. pl. m.)'),
           ('<b>Istud</b> verbum nōn amō.', 'Não gosto dessa palavra (que você disse). (<i>istud</i>: ac. sing. neutro)')])}
'''),
        ('Is, ea, id: o demonstrativo que não aponta', f'''
<p>O mais frequente de todos os demonstrativos é também o mais fraco. <i>Is, ea, id</i> não indica lugar nenhum: limita-se a <b>retomar</b> algo já mencionado ou a anunciar algo que vai ser explicado em seguida (Allen e Greenough § 297 d). No capítulo 14 você o encontrou como pronome de terceira pessoa ("ele, ela"), porque o latim não tem um pronome pessoal próprio para "ele"; aqui está a declinação completa:</p>
{tabela_declinacao('is, ea, id, "ele, ela; esse, aquele"', [
    ('is', 'e<b>a</b>', 'i<b>d</b>', 'e<b>ī</b> (i<b>ī</b>)', 'e<b>ae</b>', 'e<b>a</b>'),
    ('e<b>ius</b>', 'e<b>ius</b>', 'e<b>ius</b>', 'e<b>ōrum</b>', 'e<b>ārum</b>', 'e<b>ōrum</b>'),
    ('e<b>ī</b>', 'e<b>ī</b>', 'e<b>ī</b>', 'e<b>īs</b> (i<b>īs</b>)', 'e<b>īs</b> (i<b>īs</b>)', 'e<b>īs</b> (i<b>īs</b>)'),
    ('e<b>um</b>', 'e<b>am</b>', 'i<b>d</b>', 'e<b>ōs</b>', 'e<b>ās</b>', 'e<b>a</b>'),
    ('e<b>ō</b>', 'e<b>ā</b>', 'e<b>ō</b>', 'e<b>īs</b> (i<b>īs</b>)', 'e<b>īs</b> (i<b>īs</b>)', 'e<b>īs</b> (i<b>īs</b>)')],
    casos=_CASOS5, colunas=_COLS6)}
<p>Fora do nominativo singular, o tema é <i>e-</i>, e as terminações são as de <i>bonus</i>, com o genitivo <i>eius</i> e o dativo <i>eī</i> da declinação pronominal. As formas entre parênteses (<i>iī, iīs</i>) são variantes que você encontrará em muitas edições (Bennett § 87). Note as ambiguidades: <i>eī</i> pode ser dativo singular ou nominativo plural masculino, como <i>illī</i>; <i>ea</i> pode ser nominativo singular feminino ou nominativo e acusativo plural neutro, como <i>haec</i>; e <i>eā</i>, com <i>ā</i> longo, é o ablativo feminino.</p>
<p>O valor de <i>is</i> depende do uso. Como <b>pronome</b>, é o "ele, ela" do português e, nos casos oblíquos, o "o, a, lhe": <i>Puerum videō et eum vocō</i>, "vejo o menino e o chamo". Como <b>adjetivo</b>, é um "esse, aquele" sem ênfase, que lembra que a coisa já foi mencionada: <i>ea puella</i>, "essa menina (de quem falamos)". E é com <i>is</i> que se anuncia uma oração relativa: <i>is quī</i>, "aquele que"; <i>id quod</i>, "aquilo que" (Bennett § 247). Esse último uso é a ponte para o capítulo 16.</p>
<p>O genitivo <i>eius</i> ("dele, dela") e o plural <i>eōrum, eārum</i> ("deles, delas") fazem o papel de possessivo da terceira pessoa quando o possuidor <b>não</b> é o sujeito da frase. Quando é o sujeito, usa-se o reflexivo <i>suus</i>, que você viu no capítulo 14 (Bennett § 86.1). A diferença, que o português apaga com o ambíguo "seu", é nítida em latim:</p>
{comparacao('suus ou eius?', ['Latim', 'Tradução', 'De quem é o livro?'], [
    ['Mārcus amīcum videt et <b>suum</b> librum legit.', 'Marcos vê o amigo e lê o seu livro.', 'de Marcos, o sujeito (reflexivo)'],
    ['Mārcus amīcum videt et librum <b>eius</b> legit.', 'Marcos vê o amigo e lê o livro dele.', 'do amigo (não é o sujeito)'],
    ['Puerī magistrum amant; <b>eius</b> verba audiunt.', 'Os meninos amam o mestre; ouvem as palavras dele.', 'do mestre'],
    ['Magister puerōs docet; <b>eōrum</b> patrēs labōrant.', 'O mestre ensina os meninos; os pais deles trabalham.', 'dos meninos'],
])}
'''),
        ('Ipse e īdem: "ele mesmo" e "o mesmo"', f'''
<p>O português usa a palavra "mesmo" para duas ideias diferentes, e o latim tem uma palavra para cada uma. "O rei <b>mesmo</b> veio", "o próprio rei veio", "o rei em pessoa veio" é <i>ipse</i>: a palavra põe em destaque uma pessoa ou coisa, em oposição às outras. "O <b>mesmo</b> rei voltou", isto é, o rei de que falamos e não outro, é <i>īdem</i>: a palavra indica identidade. O Pe. Ravizza (n. 70) insiste para que não se confundam, e o exemplo dele resume bem: <i>idem rēx</i>, "o mesmo rei, o rei já mencionado e não outro".</p>
{tabela_declinacao('ipse, ipsa, ipsum, "ele mesmo, o próprio"', [
    ('ips<b>e</b>', 'ips<b>a</b>', 'ips<b>um</b>', 'ips<b>ī</b>', 'ips<b>ae</b>', 'ips<b>a</b>'),
    ('ips<b>īus</b>', 'ips<b>īus</b>', 'ips<b>īus</b>', 'ips<b>ōrum</b>', 'ips<b>ārum</b>', 'ips<b>ōrum</b>'),
    ('ips<b>ī</b>', 'ips<b>ī</b>', 'ips<b>ī</b>', 'ips<b>īs</b>', 'ips<b>īs</b>', 'ips<b>īs</b>'),
    ('ips<b>um</b>', 'ips<b>am</b>', 'ips<b>um</b>', 'ips<b>ōs</b>', 'ips<b>ās</b>', 'ips<b>a</b>'),
    ('ips<b>ō</b>', 'ips<b>ā</b>', 'ips<b>ō</b>', 'ips<b>īs</b>', 'ips<b>īs</b>', 'ips<b>īs</b>')],
    casos=_CASOS5, colunas=_COLS6)}
<p><i>Ipse</i> declina-se como <i>ille</i>, com uma única diferença: o neutro singular é <i>ipsum</i>, e não *<i>ipsud</i>. Pode acompanhar um nome (<i>rēx ipse</i>, "o próprio rei"; <i>ipsō diē</i>, "naquele mesmo dia, exatamente no dia"), um pronome de qualquer pessoa (<i>ego ipse</i>, "eu mesmo"; <i>tū ipse</i>, "você mesmo") ou ficar sozinho, como "ele em pessoa". Os discípulos de Pitágoras, conta a tradição, encerravam as discussões com <i>Ipse dīxit</i>, "ele (o mestre) disse" (Kennedy § 320; Allen e Greenough § 298 d).</p>
<p>O ponto delicado é a diferença entre <i>ipse</i> e o reflexivo <i>sē</i>. Em português, "ele mesmo" serve para as duas coisas: "ele mesmo veio" (ênfase) e "ele feriu a si mesmo" (reflexivo). Em latim, a ênfase é <i>ipse</i> e o reflexivo é <i>sē</i> (Allen e Greenough § 298 c, nota 2). E, quando os dois se juntam, <i>ipse</i> concorda normalmente com o <b>sujeito</b>, não com o reflexivo: <i>Mē ipse cōnsōlor</i>, "consolo a mim mesmo", diz Cícero (<i>Laelius</i> 10, citado por Allen e Greenough § 298 f), com <i>ipse</i> no nominativo, e não *<i>mē ipsum</i> (Bennett § 249.2).</p>
{tabela_declinacao('īdem, eadem, idem, "o mesmo, a mesma"', [
    ('<b>ī</b>dem', 'e<b>a</b>dem', '<b>i</b>dem', 'e<b>ī</b>dem (<b>ī</b>dem)', 'e<b>ae</b>dem', 'e<b>a</b>dem'),
    ('e<b>ius</b>dem', 'e<b>ius</b>dem', 'e<b>ius</b>dem', 'e<b>ōrun</b>dem', 'e<b>ārun</b>dem', 'e<b>ōrun</b>dem'),
    ('e<b>ī</b>dem', 'e<b>ī</b>dem', 'e<b>ī</b>dem', 'e<b>īs</b>dem (<b>īs</b>dem)', 'e<b>īs</b>dem', 'e<b>īs</b>dem'),
    ('e<b>un</b>dem', 'e<b>an</b>dem', '<b>i</b>dem', 'e<b>ōs</b>dem', 'e<b>ās</b>dem', 'e<b>a</b>dem'),
    ('e<b>ō</b>dem', 'e<b>ā</b>dem', 'e<b>ō</b>dem', 'e<b>īs</b>dem', 'e<b>īs</b>dem', 'e<b>īs</b>dem')],
    casos=_CASOS5, colunas=_COLS6)}
<p><i>Īdem</i> é simplesmente <i>is</i> com a partícula invariável <i>-dem</i>: declina-se a primeira parte como <i>is</i> e acrescenta-se <i>-dem</i> (Allen e Greenough § 146, nota 9). Só duas coisas mudam. No nominativo, <i>is-dem</i> virou <i>īdem</i> (masculino, com <i>ī</i> longo), e o neutro é <i>idem</i> (com <i>i</i> breve). E o <i>m</i> final de <i>eum, eam, eōrum, eārum</i> vira <i>n</i> diante do <i>d</i>: <i>eundem, eandem, eōrundem, eārundem</i>, como em português se escreve <i>n</i> antes de <i>d</i>. Quem sabe <i>is</i> sabe <i>īdem</i>.</p>
<p>Além de "o mesmo", <i>īdem</i> muitas vezes se traduz por um advérbio, "também, ao mesmo tempo", quando atribui uma segunda qualidade a quem já foi nomeado (Bennett § 248; Kennedy § 321). Kennedy (§ 321) cita de Cícero: <i>ego vir fortis, īdemque philosophus</i>, "eu, homem corajoso e também filósofo".</p>
{exemplos([('Rēx <b>ipse</b> mīlitibus dōna dat.', 'O próprio rei (o rei em pessoa) dá presentes aos soldados.'),
           ('<b>Īdem</b> rēx mīlitibus dōna dat.', 'O mesmo rei (aquele de que falamos) dá presentes aos soldados.'),
           ('Puer <b>sē</b> in aquā videt.', 'O menino se vê na água. (reflexivo: <i>sē</i>, não <i>ipse</i>)'),
           ('<b>Eadem</b> verba semper audīmus.', 'Ouvimos sempre as mesmas palavras. (<i>eadem</i>: ac. pl. neutro com <i>verba</i>; <i>semper</i>, sempre)'),
           ('Magistrī <b>ipsīus</b> liber est.', 'É o livro do próprio mestre.')])}
'''),
        ('Hīc … ille; análise de uma frase de Cícero', f'''
<p>Quando <i>hīc</i> e <i>ille</i> aparecem juntos referindo-se a duas coisas já mencionadas, <b><i>hīc</i> designa normalmente a última</b> (a mais próxima no texto) e <b><i>ille</i> a primeira</b> (a mais distante): é exatamente o "este … aquele" do português culto, que também se pode dizer "o último … o primeiro" (Bennett § 246.1; Kennedy § 319). Kennedy (§ 319) ilustra a regra com um verso de Ovídio, que, no mar, só vê <i>pontus et āēr</i>, "o mar e o céu", e o cita assim: <i>nūbibus hīc tumidus, fluctibus ille mināx</i>, "este (o céu) inchado de nuvens, aquele (o mar) ameaçador de ondas"; <i>hīc</i> retomaria <i>āēr</i>, a palavra mais próxima. Mas as edições de Ovídio (<i>Tristia</i> 1.2.24, na edição de A. L. Wheeler publicada pela Loeb e reproduzida no Perseus, e também no texto da The Latin Library) leem <i>fluctibus hīc tumidus, nūbibus ille mināx</i>: aí <i>hīc</i> retoma <i>pontus</i>, o primeiro nomeado. A regra, portanto, indica só o caso mais comum; Allen e Greenough (§ 297.a) registram que <i>hīc</i> pode, mais raramente, designar o primeiro, quando ele, embora mais distante no texto, está mais próximo de quem fala no tempo, no lugar ou no pensamento. Quando os referentes têm gêneros diferentes, o próprio gênero do pronome resolve a dúvida, e a regra da posição nem precisa ser aplicada.</p>
{diagrama_frase([('Mārcus', 'nomeado primeiro · retomado por ille'), ('et Iūlius', 'nomeado por último · retomado por hīc'), ('hīc legit', '"este" = Júlio · lê'), ('ille scrībit', '"aquele" = Marcos · escreve')],
    '<i>Mārcus et Iūlius in hortō sunt: hīc legit, ille scrībit</i> = Marcos e Júlio estão no jardim: este (Júlio) lê, aquele (Marcos) escreve.')}
<p>Os dois nomes são masculinos, e por isso só a posição decide: <i>hīc</i>, "este", aponta para o mais próximo no texto, <i>Iūlius</i>; <i>ille</i>, "aquele", para o mais distante, <i>Mārcus</i>. Numa tradução, quando "este" e "aquele" soarem pesados, repita os nomes: "Júlio lê, Marcos escreve".</p>
<p>Agora uma frase autêntica. Em novembro de 63 a.C., Cícero, cônsul, denuncia no senado a conjuração de Catilina, que está sentado ali mesmo, entre os senadores. No § 2 do primeiro discurso, depois da célebre exclamação <i>Ō tempora, ō mōrēs!</i> ("Que tempos, que costumes!"), ele diz:</p>
{exemplos([('Senātus haec intellegit. Cōnsul videt; hīc tamen vīvit.', 'O senado entende estas coisas. O cônsul as vê; este homem, porém, vive. (Cícero, <i>Cat.</i> 1.2)')])}
{analise('Cícero, In Catilinam I, 2, palavra a palavra', [
    ('Senātus', 'senātus, -ūs (m.), senado', 'nominativo singular, 4ª declinação (capítulo 11)', 'sujeito de <i>intellegit</i>'),
    ('haec', 'hīc, haec, hōc, este', 'acusativo plural neutro, usado como pronome', 'objeto: "estas coisas" (os planos da conjuração, que todos ali conhecem)'),
    ('intellegit', 'intellegō, -ere, entender, perceber', '3ª pessoa do singular do presente, 3ª conjugação', 'verbo da primeira oração'),
    ('Cōnsul', 'cōnsul, cōnsulis (m.), cônsul', 'nominativo singular, 3ª declinação (tema <i>cōnsul-</i>)', 'sujeito de <i>videt</i>; o próprio Cícero, falando de si na terceira pessoa'),
    ('videt', 'videō, -ēre, ver', '3ª pessoa do singular do presente, 2ª conjugação', 'verbo; o objeto <i>haec</i> fica subentendido'),
    ('hīc', 'hīc, haec, hōc, este', 'nominativo singular masculino, usado como pronome', 'sujeito de <i>vīvit</i>: "este homem", Catilina, presente na sala'),
    ('tamen', 'tamen (advérbio), porém, contudo', 'invariável', 'opõe a terceira oração às duas primeiras'),
    ('vīvit', 'vīvō, -ere, viver', '3ª pessoa do singular do presente, 3ª conjugação', 'verbo da terceira oração'),
])}
<p>As duas formas de <i>hīc</i> mostram os dois usos de um demonstrativo sem nome ao lado. <i>Haec</i>, no neutro plural, designa um conjunto de coisas, "isto tudo", como o neutro faz sempre (Allen e Greenough § 297 f); não pode ser o feminino singular, porque <i>senātus</i> já é o sujeito e <i>intellegit</i> pede um objeto. <i>Hīc</i>, no masculino, designa uma pessoa, e aqui a dêixis é literal: Catilina está no mesmo recinto que o orador, ao alcance do seu gesto. Traduzir <i>hīc</i> por "ele" perderia o dedo apontado; "este homem" o conserva. O efeito da frase vem da gradação: o senado sabe, o cônsul vê, e <b>este aqui</b>, apesar de tudo, continua vivo.</p>
<p>O mesmo discurso usa os outros demonstrativos do capítulo poucas linhas depois e antes: <i>furor iste tuus</i> (§ 1), "essa tua loucura", com o <i>iste</i> da segunda pessoa e do desprezo; <i>huius ōrdinis</i> (§ 3), "desta ordem", isto é, do senado onde Cícero fala; <i>in hāc rē pūblicā</i> (§ 3), "nesta república". É um bom texto para voltar a ler quando você tiver estudado os tempos do passado e o subjuntivo.</p>
<h3>Resumo</h3>
<ul>
<li><i>hīc</i> = este (perto de quem fala); <i>iste</i> = esse (perto de quem ouve; muitas vezes depreciativo); <i>ille</i> = aquele (longe; "o famoso"); <i>is</i> = ele, esse (só retoma; sem dêixis).</li>
<li>Declinação pronominal: genitivo singular em <i>-īus</i> (<i>illīus, ipsīus</i>; <i>huius, eius</i>) e dativo em <i>-ī</i> (<i>illī, ipsī, huic, eī</i>) nos três gêneros; neutro em <i>-ud</i> ou <i>-d</i> (<i>illud, istud, id</i>). O mesmo genitivo e dativo têm <i>ūnus, sōlus, tōtus, ūllus, nūllus, alius, alter, uter, neuter</i>.</li>
<li>Como adjetivos, concordam com o nome; como pronomes, tomam o gênero e o número do referente e o caso da própria função. O neutro designa ideias: <i>hōc</i>, "isto"; <i>haec</i>, "estas coisas".</li>
<li><i>ipse</i> = "ele mesmo, o próprio" (ênfase); <i>īdem</i> = "o mesmo" (identidade) = <i>is</i> + <i>-dem</i>; <i>sē</i> = reflexivo.</li>
<li><i>eius, eōrum</i> = "dele, deles" (possuidor que não é o sujeito); <i>suus</i> = possuidor que é o sujeito.</li>
<li><i>hīc … ille</i> = "este … aquele" = "o último … o primeiro".</li>
</ul>
<p>No próximo capítulo, <i>is</i> encontra o seu parceiro natural, o pronome relativo <i>quī, quae, quod</i>, e você aprende a ler as orações que começam por ele.</p>
'''),
    ],
    erros_comuns=[
        ('Ler <i>haec</i> sempre como feminino singular: <i>haec verba</i> traduzido por *"esta palavras".', '<i>Haec</i> é também nominativo e acusativo plural <b>neutro</b>, e com <i>verba</i> (neutro plural) só pode ser isso: "estas palavras". Sozinho, no neutro, significa "estas coisas, isto tudo". O nome ao lado, ou a função que falta na frase, decide.'),
        ('Tomar <i>illī</i>, <i>istī</i>, <i>eī</i> ou <i>ipsī</i> sempre por nominativos plurais, como <i>dominī</i>.', 'Na declinação pronominal, <i>-ī</i> é também o <b>dativo singular</b> dos três gêneros. Em <i>illī puellae librum dō</i>, <i>illī</i> concorda com <i>puellae</i>, dativo feminino: "dou o livro àquela menina". Procure o nome com que o demonstrativo concorda e veja o número do verbo.'),
        ('Traduzir todo <i>hīc</i> por "aqui", ou todo <i>ille</i> por "aquele".', '<i>Hīc</i> pronome ("este") e <i>hīc</i> advérbio ("aqui") se escrevem igual, com ou sem macrons: se concorda com um nome ou é sujeito, é pronome. E <i>ille</i>, conforme o contexto, é "ele", "o famoso" ou, junto de <i>hīc</i>, "o primeiro"; às vezes a melhor tradução é simplesmente repetir o nome.'),
        ('Usar <i>ipse</i> como reflexivo: *<i>Puer ipsum videt</i> para "o menino se vê".', 'O reflexivo é <i>sē</i>: <i>puer sē videt</i>. <i>Ipse</i> só dá ênfase ("o próprio menino", "em pessoa"). Para reforçar o reflexivo, junte os dois, com <i>ipse</i> concordando com o sujeito: <i>puer sē ipse videt</i>, "o menino vê a si mesmo".'),
        ('Traduzir "mesmo" sempre pela mesma palavra: *<i>īdem rēx venit</i> para "o próprio rei vem".', '"O rei mesmo, o próprio rei, o rei em pessoa" = <i>rēx ipse</i> (ênfase). "O mesmo rei" (não outro) = <i>īdem rēx</i> (identidade). Teste: se der para trocar "mesmo" por "próprio" ou "em pessoa", é <i>ipse</i>; se der para dizer "o mesmo de antes", é <i>īdem</i>.'),
        ('Igualar <i>iste</i> ao "este" do português e <i>ipse</i> ao "esse".', 'As palavras portuguesas descendem delas ("este" de <i>iste</i>, "esse" de <i>ipse</i>, pela explicação tradicional da gramática histórica), mas o sentido mudou no caminho. Em latim clássico, "este" é <i>hīc</i>; <i>iste</i> é "esse (aí, seu)"; e <i>ipse</i> não é demonstrativo de lugar, é "o próprio".'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Achar o nome de cada demonstrativo',
            'Analise e traduza: <i lang="la">Huius puerī pater illī mīlitī eundem librum dat.</i> Vocabulário: todas as palavras já foram vistas; <i>dat</i>, dá.', [
            ('Qual é o verbo, e o que ele faz esperar?', '<i>Dat</i>, "dá", 3ª pessoa do singular: um sujeito singular, o que é dado (acusativo) e a quem se dá (dativo).'),
            ('Com que nome concorda <i>huius</i>?', '<i>Huius</i> é genitivo singular de <i>hīc</i>, em qualquer gênero. O nome vizinho em genitivo singular é <i>puerī</i>: "deste menino". (<i>Puerī</i> sozinho também poderia ser nominativo plural, mas o verbo é singular e <i>huius</i> confirma o genitivo.)'),
            ('Quem é o sujeito?', '<i>Pater</i>, nominativo singular: "o pai deste menino".'),
            ('E <i>illī mīlitī</i>?', '<i>Mīlitī</i> é dativo singular de <i>mīles</i>; <i>illī</i> concorda com ele (dativo singular masculino). Não é nominativo plural: o nome ao lado é singular. "Àquele soldado": é quem recebe.'),
            ('<i>Eundem librum</i>?', '<i>Eundem</i> é acusativo singular masculino de <i>īdem</i> (<i>eum</i> + <i>-dem</i>, com <i>m</i> → <i>n</i>), concordando com <i>librum</i>: "o mesmo livro". É o objeto.'),
            ('Monte a tradução.', '"O pai deste menino dá o mesmo livro àquele soldado."'),
        ]),
        pratica_guiada('Prática guiada 2 · Este e aquele',
            'Traduza, decidindo a quem se refere cada pronome: <i lang="la">Pater et fīlius in agrō sunt: hīc labōrat, ille spectat.</i> Vocabulário: <i>ager, agrī</i> (m.), campo; <i>labōrō, -āre</i>, trabalhar; <i>spectō, -āre</i>, olhar.', [
            ('Quantas pessoas foram mencionadas, e em que ordem?', 'Duas: primeiro <i>pater</i>, depois <i>fīlius</i>. As duas são masculinas, então o gênero de <i>hīc</i> e <i>ille</i> não ajuda.'),
            ('A quem se refere <i>hīc</i>?', 'Ao último nomeado, o mais próximo no texto: <i>fīlius</i>. "Este" (o filho) trabalha.'),
            ('E <i>ille</i>?', 'Ao primeiro nomeado, mais distante no texto: <i>pater</i>. "Aquele" (o pai) olha.'),
            ('Monte a tradução e uma versão mais natural.', '"O pai e o filho estão no campo: este trabalha, aquele olha." Mais natural: "o filho trabalha, o pai olha".'),
        ], 'Conclusão: em <i>hīc … ille</i>, olhe primeiro o gênero; se não resolver, <i>hīc</i> é o último nomeado e <i>ille</i> o primeiro.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Reconheça as formas', 'Diga de que pronome vem cada forma e dê todas as possibilidades de caso, número e gênero.', [
            ('<i>huius</i>', 'Genitivo singular de <i>hīc</i>, nos três gêneros: "deste, desta".'),
            ('<i>haec</i>', 'De <i>hīc</i>: nominativo singular feminino ("esta") ou nominativo/acusativo plural neutro ("estas coisas").'),
            ('<i>hōs</i>', 'Acusativo plural masculino de <i>hīc</i>: "estes".'),
            ('<i>illīus</i>', 'Genitivo singular de <i>ille</i>, nos três gêneros: "daquele, daquela".'),
            ('<i>illī</i>', 'De <i>ille</i>: dativo singular dos três gêneros ou nominativo plural masculino. Só a frase decide.'),
            ('<i>istud</i>', 'Nominativo ou acusativo singular neutro de <i>iste</i>: "isso".'),
            ('<i>eī</i>', 'De <i>is</i>: dativo singular dos três gêneros ("a ele, a ela, lhe") ou nominativo plural masculino ("eles").'),
            ('<i>eōrum</i>', 'Genitivo plural masculino ou neutro de <i>is</i>: "deles".'),
            ('<i>ipsā</i>', 'Ablativo singular feminino de <i>ipse</i>.'),
            ('<i>eandem</i>', 'Acusativo singular feminino de <i>īdem</i>: <i>eam</i> + <i>-dem</i>, com <i>m</i> → <i>n</i>.'),
            ('<i>eīsdem</i>', 'Dativo ou ablativo plural de <i>īdem</i>, nos três gêneros.'),
            ('<i>idem</i> e <i>īdem</i>', '<i>Idem</i> (<i>i</i> breve): nominativo ou acusativo singular neutro. <i>Īdem</i> (<i>ī</i> longo): nominativo singular masculino (e variante do nominativo plural masculino). Sem macrons, só a concordância distingue.'),
        ]),
        exercicio('Exercício 2 · Faça concordar', 'Escreva o demonstrativo indicado na forma que concorda com o nome, no caso pedido.', [
            ('<i>hīc</i> + <i>puella</i>, nominativo', '<i>haec puella</i>: nominativo singular feminino.'),
            ('<i>ille</i> + <i>rēx</i>, genitivo', '<i>illīus rēgis</i>: genitivo singular em <i>-īus</i>, embora o nome faça <i>-is</i>. A concordância é de gênero, número e caso, não de terminação.'),
            ('<i>is</i> + <i>corpus</i>, acusativo', '<i>id corpus</i>: <i>corpus</i> é neutro, e no neutro o acusativo é igual ao nominativo.'),
            ('<i>ipse</i> + <i>māter</i>, dativo', '<i>ipsī mātrī</i>: dativo singular, igual nos três gêneros.'),
            ('<i>īdem</i> + <i>verbum</i>, ablativo', '<i>eōdem verbō</i>: ablativo singular neutro.'),
            ('<i>iste</i> + <i>mīlitēs</i>, acusativo', '<i>istōs mīlitēs</i>: acusativo plural masculino.'),
            ('<i>hīc</i> + <i>tempus</i>, ablativo', '<i>hōc tempore</i>: ablativo singular neutro ("neste tempo"), com <i>ō</i> longo.'),
            ('<i>ille</i> + <i>nōmina</i>, nominativo', '<i>illa nōmina</i>: nominativo plural neutro. Não é feminino singular.'),
        ]),
        exercicio('Exercício 3 · Este, esse ou aquele?', 'Verta para o latim, escolhendo o demonstrativo pela situação descrita entre parênteses. Vocabulário: <i>antīquus, -a, -um</i>, antigo; <i>furor, furōris</i> (m.), loucura.', [
            ('Este livro é meu. (o livro está na mão de quem fala)', '<i>Hīc liber meus est.</i> Perto de quem fala: <i>hīc</i>.'),
            ('Esse livro é seu. (o livro está na mão de quem ouve)', '<i>Iste liber tuus est.</i> Perto do interlocutor: <i>iste</i>.'),
            ('Aquele templo é antigo. (o templo está longe dos dois)', '<i>Illud templum antīquum est.</i> Longe: <i>ille</i>, no neutro, concordando com <i>templum</i>.'),
            ('Essa sua loucura não me assusta. (dito com desprezo a um adversário; "assusta" = <i>terret</i>)', '<i>Furor iste tuus mē nōn terret.</i> <i>Iste</i> com <i>tuus</i>: a loucura é do interlocutor, e o tom é de desprezo, como em Cícero, <i>Cat.</i> 1.1.'),
            ('Os soldados amam aquele famoso general.', '<i>Mīlitēs ducem illum amant.</i> <i>Ille</i> depois do nome tem o valor de "o famoso"; antes do nome (<i>illum ducem</i>) seria só "aquele general".'),
        ]),
        exercicio('Exercício 4 · Traduza', 'Anote o caso e a função de cada demonstrativo antes de traduzir. Vocabulário: <i>semper</i>, sempre; <i>soror, sorōris</i> (f.), irmã.', [
            ('<i>Hīc puer illam puellam amat.</i>', 'Este menino ama aquela menina. (<i>hīc</i> concorda com <i>puer</i>, nom.; <i>illam</i> com <i>puellam</i>, ac.)'),
            ('<i>Mīlitēs ducem vident et eum laudant.</i>', 'Os soldados veem o general e o elogiam. (<i>eum</i>: ac. sing. m., retoma <i>ducem</i>)'),
            ('<i>Magister puerōs docet; eōrum patrēs labōrant.</i>', 'O mestre ensina os meninos; os pais deles trabalham. (<i>eōrum</i>: possuidor que não é o sujeito da sua oração)'),
            ('<i>Rēx ipse mīlitibus dōna dat.</i>', 'O próprio rei dá presentes aos soldados.'),
            ('<i>Eadem verba semper audīmus.</i>', 'Ouvimos sempre as mesmas palavras. (<i>eadem</i>: ac. pl. neutro)'),
            ('<i>Frāter et soror in hortō sunt: haec legit, ille dormit.</i>', 'O irmão e a irmã estão no jardim: ela lê, ele dorme. O gênero resolve: <i>haec</i> (f.) é a irmã, <i>ille</i> (m.) o irmão. Aqui coincide com a regra da posição: <i>soror</i> foi nomeada por último.'),
            ('<i>Huius templī nōmen clārum est.</i>', 'O nome deste templo é famoso. (<i>huius</i>: gen. sing. com <i>templī</i>)'),
        ]),
        exercicio('Exercício 5 · Ipse, īdem ou sē?', 'Verta para o latim. Vocabulário: <i>epistula, -ae</i>, carta; <i>aqua, -ae</i>, água; <i>diēs, diēī</i> (m.), dia (5ª declinação, capítulo 11).', [
            ('O próprio pai lê a carta.', '<i>Pater ipse epistulam legit.</i> Ênfase: <i>ipse</i>, concordando com <i>pater</i>.'),
            ('O mesmo pai lê a carta.', '<i>Īdem pater epistulam legit.</i> Identidade: <i>īdem</i>.'),
            ('O menino se vê na água.', '<i>Puer sē in aquā videt.</i> Reflexivo: <i>sē</i>.'),
            ('O menino vê a si mesmo na água.', '<i>Puer sē ipse in aquā videt.</i> O reflexivo é <i>sē</i>; <i>ipse</i> reforça e concorda com o sujeito (Bennett § 249.2).'),
            ('Vemos os mesmos soldados.', '<i>Eōsdem mīlitēs vidēmus.</i> Acusativo plural masculino de <i>īdem</i>.'),
            ('no mesmo dia', '<i>eōdem diē</i>: ablativo singular masculino (<i>diēs</i> é masculino aqui).'),
        ]),
        exercicio('Exercício 6 · Leitura', 'Leia em voz alta e responda. Texto escrito para este capítulo. Vocabulário: <i>rīdet</i>, ri; <i>nam</i>, pois; <i>tum</i>, então; <i>sed</i>, mas.<br><br><i lang="la">Mārcus et Iūlia in hortō sunt. Hīc librum legit, haec rosās spectat. Liber Mārcī nōn est: magister eum Mārcō dat. Iūlia eundem librum amat, sed Mārcus eum nōn dat. Tum Iūlia: "Iste liber meus est!" Mārcus rīdet; nam liber magistrī ipsīus est.</i>', [
            ('Quem lê, e quem olha as rosas? Como você sabe?', 'Marcos lê (<i>hīc</i>, masculino); Júlia olha as rosas (<i>haec</i>, feminino). O gênero resolve antes de qualquer regra de posição.'),
            ('A que palavra se refere <i>eum</i>, nas duas vezes?', 'A <i>librum</i>: acusativo singular masculino de <i>is</i>, que retoma um nome masculino já mencionado.'),
            ('Por que Júlia diz <i>iste liber</i>, e não <i>hīc liber</i>?', 'Porque o livro está com Marcos, o interlocutor: é "esse livro aí". <i>Hīc</i> indicaria um livro que ela mesma tem nas mãos.'),
            ('De quem é o livro, afinal? Que palavra mostra isso?', 'Do próprio mestre: <i>magistrī ipsīus</i>, "do mestre em pessoa", genitivo de <i>ipse</i> concordando com <i>magistrī</i>.'),
            ('Traduza o texto.', 'Marcos e Júlia estão no jardim. Ele lê um livro, ela olha as rosas. O livro não é de Marcos: o mestre o dá (empresta) a Marcos. Júlia ama o mesmo livro, mas Marcos não o dá. Então Júlia: "Esse livro é meu!" Marcos ri, pois o livro é do próprio mestre.'),
        ]),
    ],
    leituras=['orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'd-ooge-latin-for-beginners', 'sonnenschein-pro-patria-a-latin-story-for-beginners', 'henderson-in-catilinam-i-com-notas-e-vocabulario', 'ravizza-gramatica-latina', 'bennett-new-latin-grammar'],
    leituras_nota='Familia Romana, de Ørberg, e Pro Patria, de Sonnenschein, usam os demonstrativos o tempo todo em narrativa simples: leia um capítulo procurando cada forma de hīc, ille e is e perguntando a quem ela se refere. Latin for Beginners, de D\'Ooge, tem exercícios graduados sobre esses pronomes. Para ver Cícero apontando para Catilina, leia os §§ 1–3 do primeiro discurso na edição comentada de Henderson, contando só os demonstrativos; o resto do texto pede os capítulos sobre o passado e o subjuntivo. Para consulta, Ravizza (n. 70) e Bennett (§§ 87–88, 246–249).',
)
