from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama, svg_caixas, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='21-usos-do-acusativo-e-do-ablativo', titulo='Usos do acusativo e do ablativo', titulo_latim='Dē accūsātīvō et ablātīvō', tempo='90 min',
    resumo='O acusativo além do objeto direto (duplo acusativo, extensão de tempo e de espaço, direção para cidades, exclamação) e o ablativo inteiro, organizado pelas suas três origens: o ablativo de afastamento (separação, origem, comparação), o instrumental (meio, causa, modo, companhia, diferença, qualidade, preço, aspecto) e o locativo (lugar e tempo); com os verbos ūtor, fruor, fungor, potior, vescor, com dignus e com opus est.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['acusativo de objeto direto', 'duplo acusativo (predicativo; pessoa e coisa)', 'doceō, rogō, vocō, appellō', 'acusativo de extensão de tempo e de espaço', 'acusativo de direção (Rōmam, domum, rūs)', 'acusativo exclamativo', 'acusativo grego (nota)', 'preposições com acusativo', 'as três origens do ablativo', 'ablativo de separação e de origem', 'ablativo de comparação', 'ablativo de meio', 'ūtor, fruor, fungor, potior, vescor', 'opus est', 'ablativo de causa', 'ablativo de modo', 'ablativo de companhia', 'ablativo de diferença (multō, paulō)', 'ablativo de qualidade', 'ablativo de preço', 'ablativo de aspecto (limitação); dignus', 'ablativo de lugar e de tempo', 'agente, sujeito do infinitivo e ablativo absoluto (menções)', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulos 4 (preposições com acusativo e com ablativo) e 11 (as cinco declinações). Este capítulo retoma também os comparativos do capítulo 18, as expressões de tempo e de lugar do capítulo 19 e o genitivo de qualidade e de valor do capítulo 20, com os quais o ablativo forma pares.',
                       licoes=['04-a-primeira-declinacao', '11-a-quarta-e-a-quinta-declinacoes', '18-comparativos-e-superlativos', '19-numerais-tempo-e-lugar', '20-usos-do-genitivo-e-do-dativo']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§§ 141–143 (preposições com acusativo, com ablativo e in/sub com os dois), §§ 172–185 (acusativo: 173 objeto afetado e produzido; 176.3–4 acusativo adverbial e cognato; 177 predicativo; 178 pessoa e coisa: rogō, doceō, cēlō; 180 acusativo grego; 181 extensão de tempo e espaço; 182 limite do movimento, 182.5 a ideia de alvo como função original; 183 exclamação; 184 sujeito do infinitivo, só a menção), §§ 213–231 (ablativo: 213 as três origens; 214 separação; 215 origem; 216 agente, só a menção; 217 comparação; 218 meio, 218.1 ūtor etc., 218.2 opus est, 218.8 verbos de encher; 219 causa; 220 modo; 222 companhia; 223 diferença; 224 qualidade; 225 preço; 226 aspecto, 226.2 dignus; 227 ablativo absoluto, só a menção; 228 lugar onde; 229 lugar de onde; 230–231 tempo), § 232 (locativo)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', url='https://dcc.dickinson.edu/grammar/latin/ablative', nota='§§ 220–221 (preposições), §§ 386–397 (acusativo: 393 predicativo; 396 pessoa e coisa com verbos de pedir e ensinar; 397.a adverbial; 397.b grego; 397.d exclamação; 397.e sujeito do infinitivo), §§ 398–399 (as três origens do ablativo), §§ 400–402 (separação), § 403 (origem e matéria), § 404 (causa), § 405 (agente), §§ 406–407 (comparação; quam), §§ 408–411 (meio; 410 ūtor, fruor, fungor, potior, vescor; 411 opus e ūsus), § 412 (modo), § 413 (companhia), § 414 (diferença), § 415 (qualidade), §§ 416–417 (preço; genitivo de valor), § 418 (aspecto; 418.b dignus), §§ 419–420 (ablativo absoluto, só a menção), §§ 423–425 (tempo e extensão), §§ 426–427 (lugar; cidades, domus, rūs)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§§ 203–213 (acusativo: 204 objeto; 206 verbos factitivos; 208 doceō, rogō, cēlō; 211 lugar para onde; 212 cognato; 213 acusativo de relação), §§ 228–246 (ablativo: 229 separação; 230 origem; 231 comparação; 233 associação; 234 qualidade; 235 aspecto; 236 modo; 237 absoluto; 239 agente; 240 instrumento; 241 causa; 242 fungor, fruor, potior, ūtor, vescor; 243 dignus, opus est; 244 diferença; 245 preço; 246 locativo)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 177 (objeto direto), nn. 179–189 (lugar onde, de onde, por onde; cidades sem preposição), nn. 193–202 (tempo: quando, em quanto tempo, por quanto tempo), n. 203 (causa), n. 205 (instrumento), n. 208 (fruor, fungor, ūtor, vescor, potior), nn. 213–214 (preço; tantī, quantī, plūris, minōris só no genitivo), n. 215 (modo), n. 216 (companhia), n. 217 (limitação), n. 218 (acusativo de relação, imitação do grego), n. 219 (dignus, indignus), n. 223 (afastamento), n. 225 (medidas), n. 233 (opus esse), nn. 245–262 (acusativo: 254 doceō e rogō com dois acusativos; 262 exclamações), n. 295 (no ablativo fundem-se três casos). Números lidos no OCR, que às vezes troca dígitos ("293" por 203, "285" por 205, "2535" por 233); conferidos pela sequência dos parágrafos.', tipo='dominio_publico'),
        referencia('Commentarii de Bello Gallico I, 1', 'Caio Júlio César', catalogo='caesar-commentarii-de-bello-gallico-texto-integral', url='http://www.thelatinlibrary.com/caesar/gall1.shtml', nota='frases analisadas na seção 6 e usadas nos exercícios 2 e 6, conferidas no texto da Latin Library; macrons acrescentados', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Gênesis 3,19; Atos 28,14; João 15,15', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Liber_Genesis', nota='frases da seção 6 e do exercício 6, conferidas na Wikisource latina; ortografia adaptada (ae por æ, i por j) e macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Reconhecer os empregos do acusativo além do objeto direto: duplo acusativo, extensão de tempo e de espaço, direção para nomes de cidade e para <i>domum, rūs</i>, exclamação.',
        'Explicar por que o ablativo reúne três casos antigos (afastamento, instrumento, lugar) e classificar cada ablativo de uma frase num desses grupos.',
        'Distinguir os ablativos de separação, origem, comparação, meio, causa, modo, companhia, diferença, qualidade, preço, aspecto, lugar e tempo, e traduzi-los com a preposição portuguesa adequada.',
        'Usar corretamente o ablativo com <i>ūtor, fruor, fungor, potior, vescor</i>, com <i>dignus</i> e com <i>opus est</i>, e escolher entre acusativo e ablativo em expressões de tempo, de lugar e de preço.',
        'Analisar frases autênticas de César e da Vulgata identificando a função de cada acusativo e de cada ablativo.',
    ],
    secoes=[
        ('O acusativo: o objeto, e o objeto duplo', f'''
<p>O acusativo é, antes de tudo, o caso do <b>objeto direto</b>: aquilo que a ação do verbo atinge (<i>librum legō</i>, "leio o livro") ou produz (<i>librum scrībō</i>, "escrevo um livro", Bennett § 173). Mas Bennett lembra que a ideia mais antiga do acusativo parece ter sido a de <b>alvo</b>, o ponto a que algo se dirige (§ 182.5). Essa ideia ajuda a entender quase todos os seus empregos: o objeto é o alvo da ação; <i>Rōmam</i>, em <i>Rōmam veniō</i>, é o alvo do movimento; <i>trēs annōs</i> é a extensão que a ação percorre até o fim. Guarde a imagem: o acusativo <b>aponta e mede</b>; o ablativo, como você verá, <b>situa e acompanha</b>.</p>
<h3>Duplo acusativo: objeto e predicativo</h3>
<p>Verbos de <b>nomear, eleger, tornar, considerar, mostrar</b> (<i>vocō, appellō, nōminō, dīcō</i> "chamar"; <i>creō</i> "eleger"; <i>faciō, reddō</i> "tornar"; <i>habeō, putō, iūdicō</i> "considerar") levam dois acusativos: o objeto e o seu <b>predicativo</b>, que diz o que o objeto passa a ser ou é considerado (Bennett § 177; A&G § 393). Os dois acusativos designam a mesma pessoa ou coisa.</p>
{exemplos([('Populus <b>Numam rēgem</b> creāvit.', 'O povo elegeu Numa rei. (<i>Numa</i> é o objeto; <i>rēgem</i>, o predicativo)'), ('Rōmulus <b>urbem Rōmam</b> vocāvit.', 'Rômulo chamou a cidade de Roma.'), ('Cupiditās <b>hominēs caecōs</b> reddit.', 'A cobiça torna os homens cegos. (exemplo de Bennett § 177.2)')])}
<h3>Duplo acusativo: pessoa e coisa</h3>
<p>Alguns verbos levam dois acusativos que designam coisas <b>diferentes</b>: a pessoa e a coisa. São os de <b>ensinar</b> (<i>doceō</i>), de <b>pedir e perguntar</b> (<i>rogō, ōrō, poscō, flāgitō</i>) e o de <b>esconder</b> (<i>cēlō</i>): "ensinar alguém (ac.) uma coisa (ac.)", "pedir a alguém (ac.) uma coisa (ac.)" (Bennett § 178; A&G § 396; Ravizza n. 254). Aqui o português engana, porque diz "ensinar <b>a</b> alguém" e "perguntar <b>a</b> alguém", e o aluno põe a pessoa no dativo.</p>
{tabela(['Verbo', 'Pessoa (ac.)', 'Coisa (ac.)', 'Tradução'], [
    ['<i>doceō</i>', '<i>puerōs</i>', '<i>grammaticam</i>', '<i>Puerōs grammaticam docet</i>: ensina gramática aos meninos.'],
    ['<i>rogō</i>', '<i>senātōrem</i>', '<i>sententiam</i>', '<i>Cōnsul senātōrem sententiam rogat</i>: o cônsul pede ao senador o seu parecer.'],
    ['<i>cēlō</i>', '<i>tē</i>', '<i>sermōnem</i>', '<i>Nōn tē sermōnem cēlāvī</i>: não te escondi a conversa (Bennett § 178.1.e).'],
], 'Verbos com acusativo da pessoa e acusativo da coisa')}
<p>Muitos desses verbos também se constroem de outro modo, e o autor escolhe: <i>poscō</i> e <i>petō</i> preferem a pessoa no ablativo com <i>ab</i> (<i>opem ā tē poscō</i>, "peço-te ajuda"), e <i>rogō</i> no sentido de "perguntar sobre" aceita <i>dē</i> + ablativo. Dois acusativos aparecem ainda em formações mais livres: o <b>acusativo cognato</b>, um objeto da mesma raiz do verbo (<i>vītam dūram vīvere</i>, "viver uma vida dura"), e os neutros usados como advérbios (<i>multum valet</i>, "tem muita força"; <i>nihil</i>, "em nada"), que nasceram de acusativos (Bennett § 176.3–4).</p>
'''),
        ('O acusativo que mede e o que aponta: extensão, direção e exclamação', f'''
<h3>Extensão no tempo e no espaço</h3>
<p>Sem preposição, o acusativo indica <b>quanto tempo dura</b> algo e <b>que distância ou dimensão</b> algo tem (Bennett § 181; A&G §§ 423, 425). O capítulo 19 apresentou as expressões de tempo e de lugar com os numerais; aqui elas entram no quadro geral dos casos. Para dar ênfase à duração, acrescenta-se <i>per</i>: <i>per trēs annōs</i>, "durante três anos inteiros".</p>
{exemplos([('<b>Trēs annōs</b> Athēnīs vīxit.', 'Viveu três anos em Atenas. (duração: por quanto tempo?)'), ('Mūrus <b>vīgintī pedēs</b> altus est.', 'O muro tem vinte pés de altura. (dimensão)'), ('<b>Mīlle passūs</b> ambulāvimus.', 'Caminhamos mil passos (uma milha). (distância)')])}
<h3>Direção sem preposição: cidades, pequenas ilhas, domum, rūs</h3>
<p>Para indicar o lugar <b>para onde</b> se vai, o latim usa normalmente <i>ad</i> ou <i>in</i> + acusativo (capítulo 4). Com nomes de <b>cidades e pequenas ilhas</b>, porém, e com <i>domum</i> ("para casa") e <i>rūs</i> ("para o campo"), o acusativo vai <b>sem preposição</b> (Bennett § 182.1; A&G § 427). É o acusativo de alvo em estado puro.</p>
{comparacao('Para onde? Com preposição e sem preposição', ['Latim', 'Tradução', 'Por quê'], [
    ['Rōmam vēnit.', 'Veio a Roma.', 'nome de cidade: sem preposição'],
    ['Athēnās nāvigāvit.', 'Navegou para Atenas.', '<i>Athēnae, -ārum</i>, cidade (só plural)'],
    ['Domum properat.', 'Apressa-se para casa.', '<i>domum</i>, "para casa", sem preposição'],
    ['In Italiam vēnit.', 'Veio para a Itália.', 'país: com preposição'],
    ['Ad urbem vēnit.', 'Veio até a cidade.', '<i>urbs</i> é nome comum: com preposição'],
    ['Ad Rōmam vēnit.', 'Veio para as imediações de Roma.', '<i>ad</i> com cidade = "para perto de" (Bennett § 182.3)'],
])}
<h3>Exclamação, e duas menções</h3>
<p>Numa exclamação, o acusativo, em geral com um adjetivo, exprime o objeto do espanto ou da dor: <i>Mē miserum!</i>, "pobre de mim!"; <i>Ō fallācem spem!</i>, "ó esperança enganosa!" (exemplos de Bennett § 183; Ravizza n. 262). Repare que o português também usa uma construção sem verbo.</p>
<p>Há outro acusativo muito frequente que não depende de nenhum verbo transitivo: o <b>sujeito do infinitivo</b>, em frases como <i>videō hominem abīre</i>, "vejo o homem ir embora" (Bennett § 184). Ele é a base da oração infinitiva, que terá o capítulo 28 inteiro.</p>
{observacao('O acusativo grego (de relação)', 'Na poesia, por imitação do grego, um acusativo indica a <b>parte</b> a que se refere um verbo ou adjetivo, quase sempre uma parte do corpo: <i>nūda genū</i>, "com o joelho nu" (literalmente "nua quanto ao joelho"); <i>tremit artūs</i>, "treme nos membros" (Bennett § 180; A&G § 397.b; Ravizza n. 218). Na prosa clássica, a mesma ideia se diz com o ablativo de aspecto (seção 5): <i>pede claudus</i>, "manco de um pé". Basta reconhecê-lo quando aparecer em Virgílio ou Ovídio.')}
<h3>As preposições com acusativo</h3>
<p>O capítulo 4 apresentou as mais frequentes. Aqui está o quadro mais completo (Bennett § 141); as marcadas com * você encontrará a toda hora nos textos.</p>
{tabela(['Preposição', 'Sentido', 'Preposição', 'Sentido'], [
    ['<i>ad</i>*', 'para, até, junto a', '<i>inter</i>*', 'entre'],
    ['<i>adversus</i>', 'contra, diante de', '<i>intrā</i>', 'dentro de'],
    ['<i>ante</i>*', 'antes de, diante de', '<i>ob</i>*', 'por causa de'],
    ['<i>apud</i>*', 'junto de, na casa de, entre', '<i>per</i>*', 'através de, durante, por'],
    ['<i>circum, circā</i>', 'ao redor de', '<i>post</i>*', 'depois de, atrás de'],
    ['<i>contrā</i>*', 'contra', '<i>praeter</i>', 'além de, exceto'],
    ['<i>ergā</i>', 'para com', '<i>prope</i>', 'perto de'],
    ['<i>extrā</i>', 'fora de', '<i>propter</i>*', 'por causa de; perto de'],
    ['<i>īnfrā</i>', 'abaixo de', '<i>suprā</i>', 'acima de'],
    ['<i>trāns</i>*', 'além de, através de', '<i>ultrā</i>', 'além de'],
], 'Preposições que pedem acusativo')}
<p>E duas pedem acusativo ou ablativo conforme o sentido: <i>in</i> e <i>sub</i>. Com acusativo indicam <b>movimento</b> (<i>in urbem</i>, "para dentro da cidade"; <i>sub iugum</i>, "para debaixo do jugo"); com ablativo, <b>repouso</b> (<i>in urbe</i>, "na cidade"; <i>sub arbore</i>, "debaixo da árvore") (Bennett § 143).</p>
'''),
        ('O ablativo: três casos num só', f'''
<p>O ablativo latino parece um caso caótico, com uma dúzia de empregos que não têm nada em comum. A desordem desaparece quando se sabe a sua história: ele <b>reúne três casos</b> que na língua-mãe dos latinos eram distintos na forma e no sentido, e que o latim fundiu num só (Bennett § 213; A&G § 398; Ravizza n. 295). Cada emprego do ablativo vem de um deles.</p>
{diagrama(svg_caixas([('ā, ab, ē, ex, dē', 'ablativo próprio · "de onde?"'), ('cum, ou nada', 'instrumental · "com quê? como?"'), ('in, ou nada', 'locativo · "onde? quando?"')], seta=False), 'As três raízes do ablativo e as preposições que costumam acompanhar cada uma. Pergunte primeiro a qual das três famílias pertence o ablativo que você está lendo.')}
{tabela(['Origem', 'Ideia', 'Empregos', 'Exemplos'], [
    ['Ablativo propriamente dito', 'afastamento: "de, desde"', 'separação; origem; lugar de onde; agente da passiva (cap. 23); comparação', '<i>cūrīs līberāre</i>; <i>Iove nātus</i>; <i>Rōmā venīre</i>; <i>melle dulcior</i>'],
    ['Instrumental', 'associação: "com"', 'meio; causa; modo; companhia; diferença; qualidade; preço; aspecto', '<i>gladiō</i>; <i>metū</i>; <i>magnā cūrā</i>; <i>cum amīcīs</i>; <i>multō maior</i>; <i>eximiā fōrmā</i>; <i>magnō</i>; <i>virtūte</i>'],
    ['Locativo', 'situação: "em"', 'lugar onde; tempo em que e dentro do qual', '<i>in urbe</i>; <i>Athēnīs</i>; <i>prīmā lūce</i>; <i>paucīs diēbus</i>'],
], 'O ablativo organizado pelas suas três origens')}
<h3>O ablativo de afastamento: separação, origem, lugar de onde</h3>
<p>Verbos e adjetivos de <b>libertar, privar, carecer</b> levam o ablativo da coisa de que se separa, sem preposição: <i>līberō, solvō</i> (libertar), <i>prīvō, spoliō</i> (privar), <i>careō, egeō</i> (carecer, precisar), e os adjetivos <i>līber, vacuus, nūdus</i> (Bennett § 214.1; A&G § 401). Quando aquilo de que se separa é uma <b>pessoa</b>, usa-se <i>ā/ab</i>: <i>urbem ā tyrannō līberāvērunt</i>, "libertaram a cidade do tirano" (Bennett § 214, nota 1). Com os demais verbos de afastamento, a preposição é a regra (<i>ab urbe discēdere</i>).</p>
{exemplos([('Agricolae <b>aquā</b> carent.', 'Os agricultores não têm água (carecem de água).'), ('Cōnsul urbem <b>metū</b> līberāvit.', 'O cônsul livrou a cidade do medo.'), ('Nōbilī <b>genere</b> nātus est.', 'Nasceu de família nobre. (origem, com <i>nātus</i>, "nascido": Bennett § 215)'), ('<b>Ex urbe</b> discessit; <b>Rōmā</b> discessit.', 'Partiu da cidade; partiu de Roma. (nome de cidade, sem preposição: Bennett § 229.1)')])}
<p>Dois empregos dessa família ganharam capítulos próprios. O <b>agente da passiva</b> com <i>ā/ab</i> (<i>ā Caesare laudātur</i>, "é louvado por César", Bennett § 216) vem no capítulo 23, junto com a voz passiva. E o <b>ablativo de comparação</b>, que você viu no capítulo 18 (<i>melle dulcior</i>, "mais doce que o mel"), é um ablativo de afastamento: mede-se a partir do outro termo. Lembre a regra de Bennett (§ 217.2): o ablativo substitui <i>quam</i> só quando o termo comparado estaria no nominativo ou no acusativo; nos outros casos, usa-se <i>quam</i>.</p>
'''),
        ('O ablativo instrumental (1): meio, causa, modo e companhia', f'''
<h3>Meio ou instrumento</h3>
<p>O ablativo sem preposição indica <b>com que</b> algo é feito: <i>gladiō pugnat</i>, "luta com a espada"; <i>oculīs vidēmus</i>, "vemos com os olhos" (Bennett § 218; A&G § 409). Aqui está o erro mais comum de quem fala português: o "com" do instrumento <b>não</b> se traduz por <i>cum</i>. <i>Cum</i> é para quem acompanha, não para aquilo com que se faz.</p>
{comparacao('Com quê? ou com quem?', ['Latim', 'Tradução', 'Função'], [
    ['Gladiō pugnat.', 'Luta com a espada.', 'meio: ablativo sem preposição'],
    ['Cum amīcō pugnat.', 'Luta junto com o amigo (ou: contra o amigo).', 'companhia: <i>cum</i> + ablativo'],
    ['Magnā cūrā labōrat.', 'Trabalha com grande cuidado.', 'modo: com adjetivo, <i>cum</i> é opcional'],
    ['Cum cūrā labōrat.', 'Trabalha com cuidado.', 'modo sem adjetivo: <i>cum</i> obrigatório'],
])}
<h3>Os cinco verbos com ablativo: ūtor, fruor, fungor, potior, vescor</h3>
<p>Cinco verbos muito frequentes levam o complemento no ablativo, e não no acusativo como seus equivalentes portugueses (Bennett § 218.1; A&G § 410; Ravizza n. 208). Os cinco são <b>depoentes</b>, isto é, têm forma passiva e sentido ativo, como você estudará no capítulo 25; por isso aqui eles entram só como vocabulário, nas formas da 3ª pessoa do presente. Bennett explica a construção pelo sentido original: <i>ūtor</i> seria "sirvo-me <b>por meio de</b>", <i>vescor</i> "alimento-me <b>com</b>".</p>
{tabela(['Verbo (dicionário)', 'Sentido', '3ª pessoa do presente', 'Exemplo', 'Tradução'], [
    ['<i>ūtor, ūtī, ūsus sum</i>', 'usar', '<i>ūtitur, ūtuntur</i>', '<i>Mīles <b>gladiō</b> ūtitur.</i>', 'O soldado usa a espada.'],
    ['<i>fruor, fruī, frūctus sum</i>', 'desfrutar, gozar', '<i>fruitur, fruuntur</i>', '<i>Rōmānī <b>pāce</b> fruuntur.</i>', 'Os romanos gozam a paz.'],
    ['<i>fungor, fungī, fūnctus sum</i>', 'desempenhar, cumprir', '<i>fungitur, funguntur</i>', '<i>Cōnsul <b>officiō</b> fungitur.</i>', 'O cônsul cumpre o seu dever.'],
    ['<i>potior, potīrī, potītus sum</i>', 'apoderar-se de', '<i>potītur, potiuntur</i>', '<i>Hostēs <b>castrīs</b> potiuntur.</i>', 'Os inimigos apoderam-se do acampamento.'],
    ['<i>vescor, vescī</i>', 'alimentar-se de, comer', '<i>vescitur, vescuntur</i>', '<i>Lupī <b>carne</b> vescuntur.</i>', 'Os lobos comem carne.'],
], 'Os cinco verbos que pedem ablativo (vocabulário; a forma depoente vem no capítulo 25)')}
<p>Ao lado deles, guarde a expressão <b><i>opus est</i></b>, "há necessidade": quem precisa vai para o <b>dativo</b>, aquilo de que se precisa vai para o <b>ablativo</b>: <i>Nōbīs opus est duce</i>, "precisamos de um comandante" (Bennett § 218.2; A&G § 411). Quando o que falta é um pronome neutro, ele pode ser o sujeito: <i>Hōc mihi opus est</i>, "isto me é necessário". Também os verbos de <b>encher</b> levam o ablativo de meio: <i>fossās aquā complent</i>, "enchem os fossos de água" (Bennett § 218.8); o adjetivo <i>plēnus</i>, como você viu no capítulo 20, prefere o genitivo.</p>
<h3>Causa</h3>
<p>O ablativo sem preposição indica também o <b>motivo</b>: <i>Puer metū tacet</i>, "o menino cala-se de medo"; <i>Multa glōriae cupiditāte fēcit</i>, "fez muitas coisas por desejo de glória" (Bennett § 219). É frequente com verbos de sentimento: <i>gaudeō, laetor</i> (alegrar-se com), <i>glōrior</i> (orgulhar-se de): <i>Victōriā gaudent</i>, "alegram-se com a vitória". A causa também se exprime com preposições (<i>ob, propter</i> + acusativo), que são mais claras para quem escreve.</p>
<h3>Modo e companhia</h3>
<p>O <b>modo</b> diz <i>como</i> algo é feito: <i>cum</i> + ablativo quando o nome está sozinho (<i>cum gravitāte loquitur</i>, "fala com dignidade"); com um adjetivo, o <i>cum</i> pode cair e, quando fica, costuma ir entre o adjetivo e o nome (<i>magnā cum cūrā</i> ou <i>magnā cūrā</i>) (Bennett § 220). Algumas palavras dispensam sempre a preposição: <i>iūre</i> (com razão), <i>iniūriā</i> (injustamente), <i>vī</i> (à força), <i>silentiō</i> (em silêncio), <i>fraude</i>; e também as expressões de conformidade, como <i>meā sententiā</i>, "na minha opinião" (§ 220.2–3).</p>
<p>A <b>companhia</b> pede <i>cum</i>: <i>cum amīcīs ambulat</i>, "passeia com os amigos"; com os pronomes, <i>cum</i> se cola depois (<i>mēcum, tēcum, nōbīscum</i>, capítulo 14). Na linguagem militar, a tropa que acompanha o general pode vir sem <i>cum</i> quando tem um adjetivo que não seja numeral: <i>omnibus cōpiīs</i>, "com todas as tropas", mas <i>cum duābus legiōnibus</i> (Bennett § 222.1).</p>
'''),
        ('O ablativo instrumental (2) e o locativo: diferença, qualidade, preço, aspecto, lugar e tempo', f'''
<h3>Diferença</h3>
<p>Com comparativos e com palavras que implicam comparação (<i>ante, post</i>), o ablativo indica <b>por quanto</b> uma coisa difere da outra (Bennett § 223; A&G § 414): <i>multō maior</i>, "muito maior" (literalmente "maior por muito"); <i>paulō post</i>, "pouco depois"; <i>tribus pedibus altior</i>, "três pés mais alto". Note que o português diz "<b>muito</b> maior", com advérbio; o latim exige o ablativo <i>multō</i>, e não o advérbio <i>multum</i>. A correlação <i>quō... eō...</i> é o mesmo ablativo: <i>quō plūra habēmus, eō ampliōra cupimus</i>, "quanto mais temos, mais queremos" (Bennett § 223).</p>
<h3>Qualidade</h3>
<p>Como o genitivo do capítulo 20, o ablativo com um adjetivo descreve uma pessoa ou coisa: <i>puella eximiā fōrmā</i>, "uma menina de beleza excepcional"; <i>vir singulārī industriā</i>, "um homem de dedicação singular" (Bennett § 224; A&G § 415). As duas construções se sobrepõem em boa parte. Na prática: medidas e idades vão de preferência no genitivo (<i>puer decem annōrum</i>), e as qualidades físicas e os estados passageiros, no ablativo (<i>bonō animō esse</i>, "estar de bom ânimo"). Bennett (§ 203.1–2) reserva o genitivo às características internas ou permanentes e às medidas; Allen e Greenough (§ 415.a) observam que as duas construções muitas vezes se equivalem, mas que as qualidades físicas vêm mais vezes no ablativo.</p>
<h3>Preço</h3>
<p>Com verbos de comprar, vender, custar, o <b>preço determinado</b> vai no ablativo: <i>Servum quīnque minīs ēmit</i>, "comprou o escravo por cinco minas" (Bennett § 225). O preço indeterminado também vai no ablativo com <i>magnō, parvō, plūrimō, minimō</i> ("caro, barato") (§ 225.1). A armadilha é que <i>tantī, quantī, plūris, minōris</i> ficam no <b>genitivo</b> mesmo com verbos de comprar (Bennett § 203.4; Ravizza n. 214), e que "estimar muito" é <i>magnī aestimāre</i>, genitivo de valor (capítulo 20), nunca <i>magnō aestimāre</i>.</p>
{comparacao('Valor e preço: genitivo ou ablativo?', ['Latim', 'Caso', 'Tradução'], [
    ['Domum magnō ēmit.', 'ablativo de preço', 'Comprou a casa caro.'],
    ['Domum centum mīlibus sēstertium ēmit.', 'ablativo de preço determinado', 'Comprou a casa por cem mil sestércios. (<i>sēstertium</i>, genitivo plural de <i>sēstertius</i>)'],
    ['Quantī domum ēmistī?', 'genitivo (<i>quantī</i> é sempre genitivo)', 'Por quanto compraste a casa?'],
    ['Domum magnī aestimō.', 'genitivo de valor (cap. 20)', 'Tenho a casa em grande estima.'],
])}
<h3>Aspecto (especificação, limitação) e dignus</h3>
<p>O ablativo indica <b>em que aspecto</b> uma afirmação é verdadeira: <i>Helvētiī reliquōs Gallōs virtūte praecēdunt</i>, "os helvécios superam os demais gauleses em valor" (César, <i>BG</i> 1.1.4); <i>pede claudus</i>, "manco de um pé"; <i>maior nātū</i>, "mais velho" (literalmente "maior quanto ao nascimento") (Bennett § 226; A&G § 418). Pertence a esse uso o ablativo com <b><i>dignus</i></b> e <b><i>indignus</i></b>: <i>dignus laude</i>, "digno de louvor"; <i>fidē indignus</i>, "indigno de confiança" (Bennett § 226.2; A&G § 418.b; Ravizza n. 219). O português diz "digno <b>de</b>", e o falante tende ao genitivo; o latim clássico usa o ablativo.</p>
<h3>O ablativo locativo: lugar onde e tempo</h3>
<p>A terceira família responde a "onde?" e "quando?". O <b>lugar onde</b> se diz com <i>in</i> + ablativo (<i>in urbe habitat</i>), mas sem preposição com nomes de cidade da 3ª declinação ou no plural (<i>Carthāgine, Athēnīs</i>), com <i>locō, locīs, parte</i>, com expressões com <i>tōtus</i> (<i>tōtā Italiā</i>, "em toda a Itália") e em <i>terrā marīque</i>, "por terra e por mar" (Bennett § 228). As cidades da 1ª e da 2ª declinação no singular conservam o antigo <b>locativo</b>, de forma igual ao genitivo: <i>Rōmae</i>, "em Roma"; <i>Corinthī</i>, "em Corinto"; assim também <i>domī</i>, "em casa", e <i>rūrī</i>, "no campo" (Bennett § 232). O <b>tempo</b> em que algo acontece e o tempo <b>dentro do qual</b> acontece vão no ablativo sem preposição (<i>prīmā lūce</i>, "ao amanhecer"; <i>paucīs diēbus</i>, "em poucos dias"; Bennett §§ 230–231). O capítulo 19 desenvolveu esses dois grupos; o quadro abaixo os reúne aos acusativos de mesmo assunto, que são o par natural deles.</p>
{tabela(['Pergunta', 'Caso', 'Nome comum', 'Cidade (1ª/2ª decl., sing.)', 'Cidade (3ª decl. ou plural)', 'domus / rūs'], [
    ['Para onde?', 'acusativo', '<i>in urbem, ad urbem</i>', '<i>Rōmam</i>', '<i>Carthāginem, Athēnās</i>', '<i>domum, rūs</i>'],
    ['Onde?', 'ablativo (locativo)', '<i>in urbe</i>', '<i>Rōmae</i> (locativo)', '<i>Carthāgine, Athēnīs</i>', '<i>domī, rūrī</i> (locativo)'],
    ['De onde?', 'ablativo', '<i>ex urbe, ab urbe</i>', '<i>Rōmā</i>', '<i>Carthāgine, Athēnīs</i>', '<i>domō, rūre</i>'],
], 'Lugar: o par acusativo e ablativo (Bennett §§ 182, 228–229, 232)')}
{tabela(['Pergunta', 'Caso', 'Exemplo', 'Tradução'], [
    ['Quando?', 'ablativo', '<i>tertiō diē</i>; <i>hieme</i>', 'no terceiro dia; no inverno'],
    ['Em quanto tempo?', 'ablativo', '<i>paucīs diēbus</i>', 'em poucos dias, dentro de poucos dias'],
    ['Por quanto tempo?', 'acusativo', '<i>trēs diēs</i>; <i>per trēs diēs</i>', 'durante três dias'],
], 'Tempo: ablativo para o ponto e o prazo, acusativo para a duração')}
{dica('<b>O ablativo absoluto.</b> Um nome no ablativo com um particípio concordando, solto do resto da frase (<i>urbe captā</i>, "tomada a cidade"), forma a construção mais característica da prosa latina, o ablativo absoluto (Bennett § 227). Ele depende dos particípios e tem o capítulo 30 só para si; por ora, se vir um ablativo que não se encaixa em nenhuma das funções deste capítulo e vem acompanhado de uma forma verbal, desconfie dele.')}
'''),
        ('Lendo frases autênticas: César e o Gênesis', f'''
<p>A primeira página da <i>Guerra da Gália</i> é um pequeno manual de ablativos. Logo depois de dividir a Gália em três partes, César descreve os povos que as habitam:</p>
{exemplos([('Hī omnēs linguā, īnstitūtīs, lēgibus inter sē differunt.', 'Todos estes diferem entre si na língua, nos costumes e nas leis. (César, <i>BG</i> 1.1.2)')])}
{analise('César, BG 1.1.2, palavra a palavra', [
    ('Hī', 'hīc, haec, hōc, este (capítulo 15)', 'nominativo plural masculino', 'sujeito: "estes" (os três povos)'),
    ('omnēs', 'omnis, -e, todo (capítulo 10)', 'nominativo plural masculino', 'concorda com <i>hī</i>: "todos estes"'),
    ('linguā', 'lingua, -ae (f.), língua', 'ablativo singular, 1ª declinação', '<b>ablativo de aspecto</b>: "quanto à língua"'),
    ('īnstitūtīs', 'īnstitūtum, -ī (n.), costume, instituição', 'ablativo plural, 2ª declinação', 'ablativo de aspecto, coordenado sem conjunção'),
    ('lēgibus', 'lēx, lēgis (f.), lei', 'ablativo plural, 3ª declinação', 'ablativo de aspecto'),
    ('inter sē', 'inter (prep. + ac.); sē, reflexivo (capítulo 14)', '<i>inter</i> + acusativo', 'reciprocidade: "entre si"'),
    ('differunt', 'differō, differre, distulī, dīlātum, diferir', 'presente, 3ª pessoa do plural (composto de <i>ferō</i>, capítulo 26)', 'verbo da oração'),
])}
<p>Os três ablativos <i>linguā, īnstitūtīs, lēgibus</i> estão justapostos sem <i>et</i> (assíndeto), um traço do estilo seco de César. Não são meios nem causas: respondem a "<b>em que</b> eles diferem?", e por isso são ablativos de aspecto (Bennett § 226). A frase seguinte, que você traduzirá no exercício 6, traz o ablativo de afastamento com <i>ā/ab</i>: <i>Gallōs ab Aquītānīs Garumna flūmen... dīvidit</i>.</p>
<p>A segunda frase é a sentença de Deus a Adão depois da queda, no Gênesis:</p>
{exemplos([('In sūdōre vultūs tuī vescēris pāne.', 'No suor do teu rosto comerás o pão. (Gn 3,19, Vulgata)')])}
{analise('Gn 3,19, palavra a palavra', [
    ('In', 'in (prep.)', 'aqui com ablativo', 'circunstância: "no, em"'),
    ('sūdōre', 'sūdor, -ōris (m.), suor', 'ablativo singular, 3ª declinação', '<i>in</i> + ablativo: a situação em que se come (circunstância, próxima do modo)'),
    ('vultūs', 'vultus, -ūs (m.), rosto', 'genitivo singular, 4ª declinação (capítulo 11)', 'genitivo de posse dependente de <i>sūdōre</i>'),
    ('tuī', 'tuus, -a, -um, teu', 'genitivo singular masculino', 'concorda com <i>vultūs</i>'),
    ('vescēris', 'vescor, vescī, alimentar-se de', 'futuro, 2ª pessoa do singular (depoente: capítulo 25)', 'verbo: "comerás"'),
    ('pāne', 'pānis, -is (m.), pão', 'ablativo singular, 3ª declinação', '<b>complemento de <i>vescor</i> no ablativo</b>'),
])}
<p>Dois pontos para observar. Primeiro, <i>vultūs</i>: a terminação <i>-ūs</i> da 4ª declinação é ao mesmo tempo genitivo singular e nominativo e acusativo plural; aqui só o genitivo faz sentido, porque a palavra depende de <i>sūdōre</i> e o adjetivo que a acompanha, <i>tuī</i>, é genitivo singular. Segundo, <i>pāne</i>: o português diz "comerás <b>o pão</b>", com objeto direto, mas <i>vescor</i>, como <i>ūtor</i>, leva ablativo. A tradução não pode imitar o latim ("comerás com o pão"); o caso só mostra a construção do verbo.</p>
{diagrama_frase([('Mārcus', 'nominativo · sujeito'), ('cum amīcīs', 'ablativo · companhia (com quem)'), ('paucīs diēbus', 'ablativo · tempo (em quanto tempo)'), ('Athēnās', 'acusativo · direção (para onde)'), ('pervēnit', 'verbo · "chegou"')], 'Acusativo e ablativo na mesma frase: <i>Mārcus cum amīcīs paucīs diēbus Athēnās pervēnit</i> = Marco chegou a Atenas com os amigos em poucos dias. O acusativo aponta o alvo; os ablativos situam e acompanham.')}
<h3>Resumo</h3>
<ul>
<li><b>Acusativo</b>: objeto direto; duplo acusativo (predicativo com <i>vocō, appellō, creō, faciō</i>; pessoa e coisa com <i>doceō, rogō, cēlō</i>); extensão de tempo e de espaço; direção sem preposição com cidades, pequenas ilhas, <i>domum, rūs</i>; exclamação; com as preposições da tabela e com <i>in, sub</i> de movimento.</li>
<li><b>Ablativo</b>, em três famílias: <b>afastamento</b> (separação, origem, lugar de onde, comparação; agente no cap. 23); <b>instrumental</b> (meio, com <i>ūtor, fruor, fungor, potior, vescor</i> e <i>opus est</i>; causa; modo; companhia com <i>cum</i>; diferença <i>multō, paulō</i>; qualidade; preço; aspecto, com <i>dignus</i>); <b>locativo</b> (lugar onde, tempo em que e dentro do qual). O ablativo absoluto fica para o capítulo 30.</li>
<li>O "com" do instrumento não é <i>cum</i>; o "de" de "digno de" é ablativo; "estimar muito" é genitivo, "comprar caro" é ablativo.</li>
</ul>
'''),
    ],
    erros_comuns=[
        ('Usar preposição com nomes de cidade: <i>in Rōmam vēnit</i>, <i>in Rōmā habitat</i>, <i>ex Rōmā discessit</i>.', 'Com cidades e pequenas ilhas, e com <i>domus</i> e <i>rūs</i>, o latim dispensa a preposição: <i>Rōmam vēnit</i>, <i>Rōmae habitat</i> (locativo), <i>Rōmā discessit</i>. A preposição volta com nomes de países e com nomes comuns: <i>in Italiam</i>, <i>in urbe</i>.'),
        ('Traduzir todo "com" por <i>cum</i>: <i>cum gladiō pugnat</i> (= luta usando a espada), <i>cum aquā rigat</i>.', '<i>Cum</i> indica companhia ou, junto de um nome sem adjetivo, o modo. O instrumento vai no ablativo sem preposição: <i>gladiō pugnat</i>, <i>aquā rigat</i>. Pergunte: é alguém que acompanha, ou algo que se usa?'),
        ('Confundir a duração com o ponto no tempo: <i>tribus diēbus mānsit</i> para "ficou três dias"; <i>tertium diem vēnit</i> para "veio no terceiro dia".', 'Duração (por quanto tempo?) é acusativo: <i>trēs diēs mānsit</i>. Ponto no tempo (quando?) e prazo (em quanto tempo?) são ablativo: <i>tertiō diē vēnit</i>; <i>tribus diēbus rediit</i>, "voltou em três dias".'),
        ('Pôr no acusativo o complemento de <i>ūtor, fruor, fungor, potior, vescor</i>: <i>gladium ūtitur</i>, <i>pācem fruuntur</i>.', 'Esses cinco verbos levam ablativo: <i>gladiō ūtitur</i>, <i>pāce fruuntur</i>. O mesmo vale para <i>opus est</i> (<i>opus est duce</i>) e para <i>dignus</i> (<i>dignus laude</i>, não <i>dignus laudis</i>).'),
        ('Pôr no dativo a pessoa com <i>doceō</i> e <i>rogō</i>, porque o português diz "ensinar <b>a</b> alguém": <i>Magister puerīs grammaticam docet</i>.', 'Esses verbos levam dois acusativos, a pessoa e a coisa: <i>Magister puerōs grammaticam docet</i>; <i>Cōnsul senātōrem sententiam rogat</i>.'),
        ('Trocar o genitivo de valor pelo ablativo de preço, ou o contrário: <i>magnō aestimō</i>; <i>multum maior</i>.', '"Estimar muito" é <i>magnī aestimāre</i> (genitivo, capítulo 20); "comprar caro" é <i>magnō emere</i> (ablativo). E a diferença com comparativos é ablativo: <i>multō maior</i>, "muito maior", nunca <i>multum maior</i>.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Um período de César, caso a caso',
            'Analise e traduza: <i lang="la">Caesar eō diē magnā cum cūrā legiōnēs ex castrīs in Galliam dūxit.</i> Vocabulário: <i>is, ea, id</i>, este, esse (capítulo 14); <i>diēs, -ēī</i>, dia; <i>cūra, -ae</i>, cuidado; <i>legiō, -ōnis</i>, legião; <i>castra, -ōrum</i> (n. pl.), acampamento; <i>dūcō, -ere, dūxī</i>, conduzir.', [
            ('Qual é o verbo e o que ele permite esperar?', '<i>Dūxit</i>, perfeito de <i>dūcō</i>, 3ª pessoa do singular: "conduziu". Espera-se um sujeito singular, um objeto (quem é conduzido) e, por ser verbo de movimento, talvez um "de onde" e um "para onde".'),
            ('Que caso é <i>eō diē</i>, e que pergunta responde?', 'Ablativo singular (<i>eō</i>, de <i>is</i>; <i>diē</i>, de <i>diēs</i>, 5ª declinação): <b>ablativo de tempo</b>, "quando?": "naquele dia". Família locativa.'),
            ('E <i>magnā cum cūrā</i>?', 'Ablativo de <b>modo</b>, com adjetivo; o <i>cum</i>, opcional aqui, está na posição usual, entre o adjetivo e o nome. "Com grande cuidado". Família instrumental.'),
            ('<i>Legiōnēs</i>: nominativo ou acusativo plural?', 'As duas formas coincidem na 3ª declinação. O sujeito já é <i>Caesar</i> (singular, como o verbo); <i>legiōnēs</i> é o <b>objeto direto</b>: "as legiões".'),
            ('E <i>ex castrīs</i> e <i>in Galliam</i>?', '<i>Ex castrīs</i>: <i>ex</i> + ablativo, <b>lugar de onde</b> (família de afastamento): "do acampamento". <i>In Galliam</i>: <i>in</i> + acusativo, <b>direção</b>: "para a Gália". <i>Gallia</i> é uma região, não uma cidade; por isso a preposição.'),
            ('Monte a tradução.', '"Naquele dia, César conduziu com grande cuidado as legiões do acampamento para a Gália."'),
        ]),
        pratica_guiada('Prática guiada 2 · Genitivo e ablativo descrevendo uma pessoa',
            'Analise e traduza: <i lang="la">Mārcus, puer novem annōrum, frātre suō paulō minor est, sed ingeniō multō maior.</i> Vocabulário: <i>novem</i>, nove; <i>annus, -ī</i>, ano; <i>frāter, -tris</i>, irmão; <i>suus</i>, seu (reflexivo, capítulo 14); <i>minor, maior</i>, menor, maior (capítulo 18); <i>ingenium, -ī</i>, inteligência, talento.', [
            ('Que função tem <i>puer novem annōrum</i>?', '<i>Puer</i> é aposto de <i>Mārcus</i>; <i>novem annōrum</i> é <b>genitivo de qualidade</b> com numeral, indicando a idade (capítulo 20): "um menino de nove anos".'),
            ('Por que <i>frātre suō</i> está no ablativo?', 'Depende do comparativo <i>minor</i>: é o <b>ablativo de comparação</b>, "menor <b>que</b> o seu irmão" (capítulo 18). Equivale a <i>quam frāter suus</i>.'),
            ('E <i>paulō</i>?', 'Ablativo de <b>diferença</b> com o comparativo: "menor por pouco" = "um pouco menor".'),
            ('Que ablativos há em <i>sed ingeniō multō maior</i>?', '<i>Ingeniō</i>: ablativo de <b>aspecto</b>, "quanto à inteligência". <i>Multō</i>: ablativo de <b>diferença</b>, "muito maior". O <i>est</i> fica subentendido do início.'),
            ('Monte a tradução.', '"Marco, um menino de nove anos, é um pouco menor que o seu irmão, mas muito maior em inteligência."'),
        ], 'Num só período, três ablativos da família instrumental (diferença duas vezes, aspecto) e um da família de afastamento (comparação), ao lado de um genitivo de qualidade: é assim que os casos se combinam nos textos.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Que acusativo é este?', 'Classifique o acusativo destacado (objeto direto; predicativo do objeto; pessoa e coisa; duração; extensão no espaço; direção sem preposição; exclamação; com preposição) e traduza. Vocabulário: <i>creō, -āre</i>, eleger; <i>grammatica, -ae</i>, gramática; <i>vīvō, -ere, vīxī</i>, viver; <i>pēs, pedis</i>, pé (medida); <i>Corinthus, -ī</i> (f.), Corinto; <i>fortūnātus</i>, feliz; <i>iter, itineris</i> (n.), caminho, marcha.', [
            ('<i>Populus Numam <b>rēgem</b> creāvit.</i>', 'Predicativo do objeto (<i>Numam</i>) com verbo de eleger: "O povo elegeu Numa rei."'),
            ('<i>Magister <b>puerōs grammaticam</b> docet.</i>', 'Duplo acusativo de pessoa (<i>puerōs</i>) e coisa (<i>grammaticam</i>) com <i>doceō</i>: "O professor ensina gramática aos meninos."'),
            ('<i><b>Trēs annōs</b> Athēnīs vīximus.</i>', 'Duração no tempo: "Vivemos três anos em Atenas." (<i>Athēnīs</i> é ablativo de lugar onde, sem preposição.)'),
            ('<i>Mūrus <b>vīgintī pedēs</b> altus est.</i>', 'Extensão no espaço (dimensão): "O muro tem vinte pés de altura."'),
            ('<i>Cōnsul <b>Corinthum</b> nāvigāvit.</i>', 'Direção sem preposição com nome de cidade: "O cônsul navegou para Corinto."'),
            ('<i>Ō <b>fortūnātum hominem</b>!</i>', 'Acusativo exclamativo, com adjetivo: "Ó homem feliz!"'),
            ('<i><b>Domum</b> properāmus.</i>', 'Direção sem preposição com <i>domum</i>: "Apressamo-nos para casa."'),
            ('<i>Mīlitēs per <b>silvam</b> <b>iter</b> faciunt.</i>', '<i>Silvam</i>: acusativo com a preposição <i>per</i>, "através da floresta". <i>Iter</i>: objeto direto de <i>faciunt</i> (neutro, nominativo = acusativo). "Os soldados marcham através da floresta."'),
        ]),
        exercicio('Exercício 2 · Que ablativo é este?', 'Diga a família (afastamento, instrumental, locativo) e o emprego do ablativo destacado, e traduza. Vocabulário: <i>careō, -ēre</i>, carecer de; <i>tyrannus, -ī</i>, tirano; <i>metus, -ūs</i>, medo; <i>taceō</i>, calar-se; <i>eximius</i>, excepcional; <i>emō, -ere, ēmī</i>, comprar; <i>praecēdō</i>, superar; <i>discēdō, -ere, discessī</i>, partir; <i>Iuppiter, Iovis</i>, Júpiter.', [
            ('<i>Agricola <b>aquā</b> caret.</i>', 'Afastamento, separação (com <i>careō</i>, sem preposição): "O agricultor não tem água."'),
            ('<i>Urbem <b>ā tyrannō</b> līberāvērunt.</i>', 'Afastamento, separação; a preposição aparece porque se trata de uma pessoa: "Libertaram a cidade do tirano."'),
            ('<i>Mīlitēs <b>gladiīs</b> pugnant.</i>', 'Instrumental, meio: "Os soldados lutam com espadas."'),
            ('<i>Puer <b>metū</b> tacet.</i>', 'Instrumental, causa: "O menino cala-se de medo."'),
            ('<i><b>Magnā cum cūrā</b> scrībit.</i>', 'Instrumental, modo (com adjetivo; <i>cum</i> opcional): "Escreve com grande cuidado."'),
            ('<i><b>Cum frātre</b> ambulō.</i>', 'Instrumental, companhia: "Passeio com o meu irmão."'),
            ('<i>Sōl <b>lūnā</b> maior est.</i>', 'Afastamento, comparação: "O sol é maior que a lua."'),
            ('<i>Hīc mūrus <b>multō</b> altior est.</i>', 'Instrumental, diferença: "Este muro é muito mais alto."'),
            ('<i>puella <b>eximiā fōrmā</b></i>', 'Instrumental, qualidade: "uma menina de beleza excepcional".'),
            ('<i>Equum <b>magnō</b> ēmit.</i>', 'Instrumental, preço indeterminado: "Comprou o cavalo caro."'),
            ('<i>Helvētiī reliquōs Gallōs <b>virtūte</b> praecēdunt.</i> (César, <i>BG</i> 1.1.4)', 'Instrumental, aspecto: "Os helvécios superam os demais gauleses em valor."'),
            ('<i><b>Prīmā lūce</b> discessērunt.</i>', 'Locativo, tempo em que: "Partiram ao amanhecer."'),
            ('<i><b>Carthāgine</b> habitābat.</i>', 'Locativo, lugar onde, sem preposição (cidade da 3ª declinação): "Morava em Cartago."'),
            ('<i><b>Iove</b> nātus</i>', 'Afastamento, origem (com <i>nātus</i>): "filho de Júpiter", "nascido de Júpiter".'),
        ]),
        exercicio('Exercício 3 · Acusativo ou ablativo?', 'Complete a frase latina para que traduza o português e explique a escolha. Vocabulário: <i>hortus, -ī</i>, jardim; <i>currō, -ere</i>, correr; <i>maneō, -ēre, mānsī</i>, ficar; <i>laus, laudis</i>, louvor; <i>pecūnia, -ae</i>, dinheiro.', [
            ('O menino corre para dentro do jardim. → <i>Puer in ___ currit.</i> (hortus)', '<i>hortum</i>: <i>in</i> + acusativo, movimento para dentro. Com <i>in hortō currit</i> o sentido seria "corre (de um lado para o outro) no jardim".'),
            ('Os soldados ficaram três dias no acampamento. → <i>Mīlitēs ___ in castrīs mānsērunt.</i>', '<i>trēs diēs</i>: duração, acusativo. (<i>In castrīs</i>: lugar onde, ablativo.)'),
            ('Chegaram a Roma. → <i>___ pervēnērunt.</i>', '<i>Rōmam</i>: direção, acusativo sem preposição (nome de cidade).'),
            ('Partiram de Roma. → <i>___ discessērunt.</i>', '<i>Rōmā</i>: lugar de onde, ablativo sem preposição.'),
            ('Moram em Roma. → <i>___ habitant.</i>', '<i>Rōmae</i>: locativo (cidade da 1ª declinação no singular), igual ao genitivo na forma.'),
            ('Moram em Atenas. → <i>___ habitant.</i>', '<i>Athēnīs</i>: ablativo sem preposição, porque <i>Athēnae</i> é plural.'),
            ('Veio no terceiro dia. → <i>___ vēnit.</i>', '<i>Tertiō diē</i>: tempo em que, ablativo.'),
            ('Precisamos de dinheiro. → <i>Nōbīs opus est ___.</i>', '<i>pecūniā</i>: com <i>opus est</i>, aquilo de que se precisa vai no ablativo; quem precisa, no dativo (<i>nōbīs</i>).'),
            ('É digno de louvor. → <i>___ dignus est.</i>', '<i>Laude</i>: <i>dignus</i> pede ablativo (de aspecto), apesar do "de" português.'),
            ('Pedro é muito mais velho. → <i>Petrus ___ maior nātū est.</i>', '<i>multō</i>: ablativo de diferença com o comparativo; <i>nātū</i> é ablativo de aspecto ("quanto ao nascimento").'),
        ]),
        exercicio('Exercício 4 · Traduza', 'Antes de traduzir, classifique cada acusativo e cada ablativo. Vocabulário: <i>perveniō, -īre, pervēnī</i>, chegar; <i>exercitus, -ūs</i>, exército; <i>frūmentum, -ī</i>, trigo; <i>egeō, -ēre</i>, precisar de; <i>Graecus</i>, grego; <i>litterae, -ārum</i>, as letras, a literatura; <i>rēmus, -ī</i>, remo; <i>portus, -ūs</i>, porto; <i>altum, -ī</i>, alto-mar; <i>agō, -ere</i>, impelir.', [
            ('<i>Caesar paucīs diēbus magnō cum exercitū in Galliam pervēnit.</i>', '<i>Paucīs diēbus</i>: tempo dentro do qual; <i>magnō cum exercitū</i>: companhia (militar, com adjetivo); <i>in Galliam</i>: direção. "César chegou à Gália em poucos dias com um grande exército."'),
            ('<i>Mīlitēs frūmentō carēbant et auxiliō egēbant.</i>', '<i>Frūmentō</i> e <i>auxiliō</i>: ablativos de separação com verbos de carecer. "Os soldados não tinham trigo e precisavam de ajuda."'),
            ('<i>Pater fīlium litterās Graecās docuit.</i>', 'Duplo acusativo com <i>doceō</i>: <i>fīlium</i> (pessoa), <i>litterās Graecās</i> (coisa). "O pai ensinou ao filho a literatura grega."'),
            ('<i>Mārcus frātre tribus annīs maior nātū est.</i>', '<i>Frātre</i>: comparação; <i>tribus annīs</i>: diferença; <i>nātū</i>: aspecto ("maior quanto ao nascimento" = mais velho). "Marco é três anos mais velho que o irmão."'),
            ('<i>Mē miserum! Nūllum amīcum Rōmae habeō.</i>', '<i>Mē miserum</i>: acusativo exclamativo; <i>amīcum</i>: objeto; <i>Rōmae</i>: locativo. "Pobre de mim! Não tenho nenhum amigo em Roma."'),
            ('<i>Nautae ventō et rēmīs nāvem ē portū in altum agunt.</i>', '<i>Ventō et rēmīs</i>: meio; <i>nāvem</i>: objeto; <i>ē portū</i>: lugar de onde; <i>in altum</i>: direção. "Os marinheiros, com o vento e os remos, levam o navio do porto para o alto-mar."'),
        ]),
        exercicio('Exercício 5 · Retroversão', 'Passe para o latim.', [
            ('Eles moraram dez anos em Cartago.', '<i>Decem annōs Carthāgine habitāvērunt.</i> Duração no acusativo; lugar onde, cidade da 3ª declinação, no ablativo sem preposição.'),
            ('O professor ensina gramática às meninas.', '<i>Magister puellās grammaticam docet.</i> Dois acusativos; não o dativo <i>puellīs</i>.'),
            ('Caminhamos para casa com os amigos.', '<i>Cum amīcīs domum ambulāmus.</i> <i>Domum</i> sem preposição; companhia com <i>cum</i>.'),
            ('Este jovem é digno de grande louvor.', '<i>Hīc adulēscēns magnā laude dignus est.</i> <i>Dignus</i> + ablativo.'),
            ('Os cidadãos elegeram Marco cônsul.', '<i>Cīvēs Mārcum cōnsulem creāvērunt.</i> Objeto e predicativo, ambos no acusativo.'),
            ('Precisamos de um bom comandante.', '<i>Nōbīs opus est bonō duce.</i> Dativo da pessoa, ablativo da coisa.'),
            ('O soldado usa uma espada curta.', '<i>Mīles gladiō brevī ūtitur.</i> <i>Ūtor</i> + ablativo (<i>brevis</i> tem ablativo em <i>-ī</i>, capítulo 10).'),
        ]),
        exercicio('Exercício 6 · Leitura autêntica', 'Identifique acusativos e ablativos e traduza. Textos conferidos na Vulgata Clementina e na Latin Library; as glosas dão o que ainda não foi estudado.', [
            ('<i>...rogātī sumus manēre apud eōs diēs septem: et sīc vēnimus Rōmam.</i> (At 28,14) Vocabulário: <i>rogātī sumus</i>, "fomos convidados" (passiva, capítulo 24); <i>manēre</i>, permanecer (infinitivo); <i>apud</i> + ac., junto de; <i>sīc</i>, assim.', '<i>Apud eōs</i>: preposição com acusativo, "junto deles"; <i>diēs septem</i>: acusativo de <b>duração</b>; <i>Rōmam</i>: acusativo de <b>direção</b> sem preposição. "Fomos convidados a ficar com eles sete dias; e assim chegamos a Roma."'),
            ('<i>Iam nōn dīcam vōs servōs... vōs autem dīxī amīcōs.</i> (Jo 15,15) Vocabulário: <i>iam nōn</i>, já não; <i>dīcam</i>, futuro de <i>dīcō</i> (capítulo 12); <i>dīxī</i>, perfeito; <i>autem</i>, mas.', 'Duplo acusativo com <i>dīcō</i> no sentido de "chamar": <i>vōs</i> é o objeto e <i>servōs</i>, <i>amīcōs</i> os predicativos. "Já não vos chamarei servos... mas a vós chamei amigos."'),
            ('<i>Gallōs ab Aquītānīs Garumna flūmen, ā Belgīs Mātrona et Sēquana dīvidit.</i> (César, <i>BG</i> 1.1.2) Vocabulário: <i>Aquītānī</i>, os aquitanos; <i>Garumna, Mātrona, Sēquana</i>, os rios Garona, Marne e Sena; <i>flūmen, -inis</i>, rio; <i>dīvidō, -ere</i>, separar.', '<i>Gallōs</i>: objeto direto; <i>ab Aquītānīs</i>, <i>ā Belgīs</i>: ablativos de <b>separação</b> com <i>ā/ab</i>, porque são povos (pessoas). O verbo <i>dīvidit</i>, no singular, é dito uma só vez e serve também ao segundo sujeito. "O rio Garona separa os gauleses dos aquitanos; o Marne e o Sena, dos belgas."'),
            ('<i>Quā dē causā Helvētiī quoque reliquōs Gallōs virtūte praecēdunt.</i> (César, <i>BG</i> 1.1.4) Vocabulário: <i>quā dē causā</i>, "por essa razão" (relativo de ligação, capítulo 16); <i>quoque</i>, também; <i>reliquus</i>, restante.', '<i>Quā dē causā</i>: <i>dē</i> + ablativo, causa; <i>reliquōs Gallōs</i>: objeto; <i>virtūte</i>: ablativo de <b>aspecto</b>. "Por essa razão, também os helvécios superam em valor os demais gauleses."'),
        ]),
    ],
    leituras=['bennett-new-latin-grammar', 'greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', 'ravizza-gramatica-latina', 'caesar-commentarii-de-bello-gallico-selecoes', 'collar-the-gate-to-caesar-de-bello-gallico-ii-simplificado-e-original', 'vulgata-biblia-sacra-vulgata-editio-clementina'],
    leituras_nota='Para consulta: Bennett, §§ 172–185 (acusativo) e §§ 213–232 (ablativo e locativo); Allen e Greenough, §§ 386–431, com exemplos de autores e uma página para cada ablativo; o Pe. Ravizza, que organiza o assunto em português por "complementos" (lugar, tempo, causa, instrumento, modo, preço) nos nn. 177–235. Para leitura, César é o autor ideal: o primeiro capítulo da <i>Guerra da Gália</i>, nas seleções comentadas, traz ablativos de aspecto, de separação e de tempo em frases curtas, e <i>The Gate to Caesar</i> apresenta o livro II em versão simplificada ao lado do original. Nos Atos dos Apóstolos (cap. 27–28), a viagem de Paulo a Roma é um bom exercício de acusativos e ablativos de lugar e de tempo.',
)
