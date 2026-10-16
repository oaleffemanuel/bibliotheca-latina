from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Texto: Ovídio, Metamorfoses 1,1–31, segundo Hugo Magnus (Gotha: F. A. Perthes, 1892), na Perseus Digital Library
# (canonical-latinLit, phi0959.phi006.perseus-lat2). Macrons acrescentados por nós.

def _poema(versos, traducao, inicio):
    linhas = []
    for i, v in enumerate(versos):
        n = inicio + i
        linhas.append(v + (f' <small>({n})</small>' if n % 5 == 0 else ''))
    return exemplos([('<br>'.join(linhas), traducao)])

PROEMIO = [
    'In nova fert animus mūtātās dīcere fōrmās',
    'corpora; dī, coeptīs (nam vōs mūtāstis et illās)',
    'adspīrāte meīs prīmāque ab orīgine mundī',
    'ad mea perpetuum dēdūcite tempora carmen.',
]
CAOS = [
    'Ante mare et terrās et quod tegit omnia caelum',
    'ūnus erat tōtō nātūrae vultus in orbe,',
    'quem dīxēre chaos: rudis indīgestaque mōlēs',
    'nec quicquam nisi pondus iners congestaque eōdem',
    'nōn bene iūnctārum discordia sēmina rērum.',
    'nūllus adhūc mundō praebēbat lūmina Tītān,',
    'nec nova crēscendō reparābat cornua Phoebē,',
    'nec circumfūsō pendēbat in āere tellūs',
    'ponderibus lībrāta suīs, nec bracchia longō',
    'margine terrārum porrēxerat Amphitrītē;',
    'utque āēr, tellūs illīc et pontus et aethēr.',
    'Sīc erat īnstabilis tellūs, innābilis unda,',
    'lūcis egēns āēr: nūllī sua fōrma manēbat,',
    'obstābatque aliīs aliud, quia corpore in ūnō',
    'frīgida pugnābant calidīs, ūmentia siccīs,',
    'mollia cum dūrīs, sine pondere habentia pondus.',
]
CAOS_PT = ('Antes do mar, das terras e do céu que cobre todas as coisas, / havia em todo o universo uma só face da natureza, / '
           'a que chamaram Caos: massa bruta e desordenada, / nada mais que um peso inerte, e, amontoadas no mesmo lugar, / '
           'as sementes discordantes de coisas mal unidas. / Nenhum Titã dava ainda luz ao mundo, / '
           'nem Febe, crescendo, renovava os seus chifres novos, / nem a terra pendia no ar derramado à sua volta, / '
           'equilibrada pelo próprio peso, nem os braços, ao longo da extensa / margem das terras, Anfitrite tinha estendido; / '
           'e, assim como o ar, estavam ali a terra, o mar e o éter. / Assim, a terra era instável, a água impossível de nadar, / '
           'o ar privado de luz: nenhuma coisa conservava a sua forma, / e uma coisa se opunha às outras, porque num só corpo / '
           'o frio lutava com o quente, o úmido com o seco, / o mole com o duro, o que não tem peso com o que tem peso. '
           '<small>(Tradução nossa, literal; as barras marcam o fim dos versos latinos.)</small>')
SEPARACAO = [
    'Hanc deus et melior lītem nātūra dirēmit.',
    'Nam caelō terrās et terrīs abscidit undās,',
    'et liquidum spissō sēcrēvit ab āere caelum.',
    'Quae postquam ēvolvit caecōque exēmit acervō,',
    'dissociāta locīs concordī pāce ligāvit.',
    'Ignea convexī vīs et sine pondere caelī',
    'ēmicuit summāque locum sibi fēcit in arce:',
    'proximus est āēr illī levitāte locōque:',
    'dēnsior hīs tellūs, elementaque grandia trāxit',
    'et pressa est gravitāte suā: circumfluus ūmor',
    'ultima possēdit solidumque coercuit orbem.',
]
SEPARACAO_PT = ('Esta discórdia, um deus e uma natureza melhor a resolveram. / Pois separou do céu as terras e das terras as águas, / '
                'e apartou do ar espesso o céu límpido. / Depois que os desembaraçou e os tirou do montão cego, / '
                'uniu-os, separados nos seus lugares, por uma paz concorde. / A força ígnea e sem peso do céu convexo / '
                'lançou-se para o alto e fez para si um lugar na cidadela mais elevada; / o ar é o mais próximo dele em leveza e em lugar; / '
                'mais densa que estes, a terra arrastou consigo os elementos pesados / e ficou comprimida pelo próprio peso; a água que corre em volta / '
                'ocupou os lugares extremos e encerrou o orbe sólido. <small>(Tradução nossa.)</small>')

LICAO = dict(
    slug='46-ovidio', titulo='Ovídio: a criação do mundo (Metamorfoses I)',
    titulo_latim='Ovidius', tempo='90 min',
    resumo='Leitura comentada do começo das Metamorfoses de Ovídio: o proêmio (1,1–4), o Caos (1,5–20) e a separação dos elementos (1,21–31), no texto de Hugo Magnus (1892). Vocabulário e notas, escansão do hexâmetro em tabelas, particípios e gerúndio no verso, figuras (antítese, lítotes, hipérbato, metonímia dos nomes divinos), comparação com o Gênesis, análise palavra a palavra, exercícios e tradução própria.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['Ovídio', 'Metamorfoses', 'proêmio', 'Caos', 'criação do mundo', 'os quatro elementos', 'hexâmetro datílico', 'escansão',
             'cesura pentemímera', 'elisão', 'quantidade das palavras gregas (āēr, aethēr)', 'perfeito em -ēre', 'perfeitos sincopados',
             'particípio conjunto', 'particípio × ablativo absoluto', 'gerúndio no ablativo', 'ablativo de comparação', 'ablativo de limitação',
             'antítese', 'lítotes', 'hipérbato', 'metonímia', 'Gênesis 1 e Metamorfoses 1', 'leitura comentada', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 30 (o ablativo absoluto e, com ele, a leitura dos particípios do capítulo 29) e capítulo 40 (quantidade, pés, elisão, o hexâmetro e as figuras). O capítulo 45 já treinou a leitura de poesia com escansão; aqui o metro é o hexâmetro narrativo. Ajudam também os capítulos 18 (ablativo de comparação) e 31 (gerúndio).',
                       licoes=['30-o-ablativo-absoluto', '40-metrica-e-figuras', '29-os-participios', '45-catulo-e-horacio', '18-comparativos-e-superlativos', '31-gerundio-e-gerundivo']),
    referencias=[
        referencia('P. Ovidius Naso, Metamorphoses, ed. Hugo Magnus (Gotha: F. A. Perthes, 1892)', 'Publius Ovidius Naso', catalogo='naso-metamorphoses-texto-integral', url='https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0029', nota='versos 1,1–31 conferidos no arquivo TEI da Perseus (canonical-latinLit, phi0959.phi006.perseus-lat2), que declara a edição de Magnus; comparados com The Latin Library (ovid/ovid.met1.shtml), que traz outra leitura no v. 15 (ver a nota da seção 2); vv. 2 e 15 conferidos também em Magnus 1885 (archive.org bub_gb_ycgzAQAAMAAJ), Merkel–Ehwald (Teubner, archive.org operadivo02ovid) e Miller (Loeb, 1916, archive.org metamorphoses01ovid). Macrons acrescentados por nós.', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Gênesis 1,1–3', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Liber_Genesis', nota='texto da comparação da seção 5, conferido no wikitexto da Wikisource latina; æ → ae, macrons acrescentados', tipo='dominio_publico'),
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 5 (quantidade; vogal longa antes de ns, nf), § 101 (3ª pl. do perfeito em -ēre: amāvērunt, -ēre), § 116.1 (perfeitos sincopados: amāstī, amāsse), § 189.1 (dativo de agente com o gerundivo, só para comparação), § 218 (ablativo de meio), § 227 (o ablativo absoluto é gramaticalmente independente da oração), § 338.4.a (ablativo do gerúndio como meio: mēns discendō alitur), § 350.11.a (hipérbato), § 358.3 (dativo com verbos de luta e de mistura nos poetas: contendis Homērō), § 362.1.d e § 365 (quantidade das palavras gregas: āēr, aethēr), § 363.1.a (-ā longo no ablativo da 1ª declinação), § 363.3 (sibi com i breve), § 364.1 (illīc), § 364.5.a (-īs longo nos plurais), § 364.6.b (tellūs, -ūris), § 366 (pés, ictus, elisão, cesura, anceps), § 368 (hexâmetro: esquema, espondaico, cesuras masculina e feminina, diérese bucólica), § 375.1 (lítotes)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 181.a (formas contraídas do perfectum), § 603 (regras gerais de quantidade; 603.a.4: palavras gregas conservam a vogal longa, com o exemplo āēr; 603.f: posição e sílabas comuns), § 604 (quantidade das sílabas finais; 604.j: āēr, aethēr entre as exceções). A edição DCC consultada não traz a parte de versificação.', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 474 (pés; elisão), § 476 (escansão; cesura forte e fraca; exemplos de Virgílio), § 477 (hexâmetro: quinto pé dáctilo, sexto espondeu ou troqueu; cesuras pentemímera, heptemímera e tritemímera). Números lidos no OCR local.', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 533 (pés: dáctilo e espondeu), n. 534 (cesura; masculina e feminina), n. 535 (elisão), n. 536 (hexâmetro, com exemplos de Ovídio; principais cesuras masculinas: tritemímera, pentemímera, heptemímera). Números lidos no OCR local, que às vezes os deforma.', tipo='dominio_publico'),
    ],
    objetivos=[
        'Situar Ovídio e as Metamorfoses e explicar o programa do poema a partir do proêmio (1,1–4).',
        'Ler e traduzir Metamorfoses 1,5–31 com o vocabulário e as notas, reconhecendo os particípios, o gerúndio e os ablativos que estruturam a descrição.',
        'Escandir hexâmetros datílicos, marcando elisões, dáctilos, espondeus e a cesura principal, e usar a métrica para decidir casos (nātūra nominativo × nātūrā ablativo).',
        'Reconhecer antítese, lítotes, hipérbato e a metonímia dos nomes divinos, e explicar como elas desenham o Caos e a ordem.',
        'Comparar a cosmogonia de Ovídio com o começo do Gênesis, identificando semelhanças de quadro e diferenças de concepção.',
    ],
    secoes=[
        ('Ovídio e o poema das transformações', f'''
<p><b>Públio Ovídio Nasão</b> (<i>Pūblius Ovidius Nāsō</i>, 43 a.C.–c. 17 d.C.), nascido em Sulmona, no centro da Itália, foi o poeta mais fecundo e mais lido da época de Augusto. Começou com poesia amorosa em dísticos elegíacos (os <i>Amōrēs</i>), escreveu cartas fictícias de heroínas, um poema sobre o calendário romano e, por volta dos cinquenta anos, a sua obra maior, as <b><i>Metamorfoses</i></b>. Em 8 d.C., por razões que ele mesmo chama de "um poema e um erro", Augusto o exilou em Tomis, à beira do mar Negro, onde morreu sem ter sido chamado de volta.</p>
<p>As <i>Metamorfoses</i> são quinze livros de hexâmetros, quase doze mil versos, que encadeiam umas duzentas e cinquenta histórias de transformação: deuses e homens mudados em árvores, pedras, animais, fontes e estrelas. O fio que as une é o tempo, da criação do mundo até a época do próprio poeta. Para a Idade Média e o Renascimento, o poema foi o grande manual da mitologia clássica, e é por ele que muita gente conhece Dafne, Narciso, Píramo e Tisbe ou Orfeu. Este capítulo lê o começo: os quatro versos do <b>proêmio</b> e a descrição do <b>Caos</b> e da sua ordenação. O texto é o da edição de Hugo Magnus (1892), conferido na Perseus Digital Library; os macrons são nossos, e as traduções também.</p>
{_poema(PROEMIO, 'O ânimo me leva a cantar as formas mudadas em novos / corpos; deuses, (pois vós também as mudastes) aos meus começos / sede propícios e, desde a primeira origem do mundo / até os meus tempos, conduzi um canto contínuo. <small>(Tradução nossa.)</small>', 1)}
<p>Quatro versos bastam para o programa. O assunto: <i>mūtātās … fōrmās</i>, "as formas mudadas", com o hipérbato que abraça o verso inteiro e o enjambement de <i>corpora</i>, que só aparece no verso seguinte, como se as palavras também se transformassem. Os deuses são invocados porque eles mesmos são os autores das transformações: <i>nam vōs mūtāstis et illās</i>, "pois também a elas (as formas) vós mudastes"; <i>mūtāstis</i> é a forma sincopada de <i>mūtāvistis</i> (Bennett § 116.1). O plano: <i>prīmā ab orīgine mundī / ad mea … tempora</i>, da origem do mundo até hoje. E o gênero: <i>perpetuum carmen</i>, "um canto contínuo", sem interrupção, isto é, um poema longo em hexâmetros, o verso da epopeia.</p>
{observacao('Uma leitura diferente no verso 2', 'Todas as edições antigas conferidas para este capítulo trazem <i>illās</i>, referido a <i>fōrmās</i>: H. Magnus (edição escolar, Gotha, 1885, e edição de 1892 reproduzida na Perseus), R. Merkel e R. Ehwald (Leipzig, Teubner, <i>editio minor</i>), F. J. Miller (Loeb, 1916) e The Latin Library. Em edições e comentários mais recentes você pode encontrar <i>nam vōs mūtāstis et illa</i>, leitura proposta por P. Lejay em 1894: "pois vós mudastes também aqueles (os meus começos)", isto é, a carreira do poeta, que passou da elegia à epopeia. A diferença é de uma letra e não muda a gramática do resto; este livro segue <i>illās</i>.')}
'''),
        ('O Caos (versos 5–20)', f'''
<p>Ovídio descreve o estado anterior ao mundo em dezesseis versos, e quase todos dizem o que <b>ainda não havia</b>. O procedimento é a negação acumulada (<i>nec … nec … nec</i>): sem sol, sem lua, sem terra suspensa, sem mar com margens. Leia o trecho inteiro antes de entrar nas notas:</p>
{_poema(CAOS, CAOS_PT, 5)}
{tabela(['v.', 'Palavra', 'Dicionário', 'Sentido e nota'], [
    ['5', 'ante', 'preposição + acusativo', 'antes de; rege <i>mare</i>, <i>terrās</i> e <i>caelum</i>'],
    ['5', 'quod tegit omnia', 'tegō, -ere, tēxī, tēctum', '"que cobre todas as coisas": oração relativa que antecipa o seu antecedente, <i>caelum</i>'],
    ['6', 'vultus', 'vultus, -ūs (m.)', 'rosto, face, aspecto; sujeito de <i>erat</i>'],
    ['6', 'tōtō … in orbe', 'tōtus, -a, -um; orbis, -is (m.)', '"em todo o orbe", em todo o universo; hipérbato'],
    ['7', 'dīxēre', 'dīcō, -ere, dīxī, dictum', '= <i>dīxērunt</i>, 3ª pl. do perfeito (Bennett § 101): "chamaram", sujeito indeterminado'],
    ['7', 'chaos', 'chaos (n., palavra grega)', 'Caos, o "abismo, vazio"; aqui, a massa informe'],
    ['7', 'rudis indīgestaque mōlēs', 'rudis, -e; indīgestus, -a, -um; mōlēs, -is (f.)', '"massa bruta e não ordenada": aposto de <i>chaos</i>'],
    ['8', 'nec quicquam nisi', 'quisquam, quicquam', '"e nada senão": <i>nec quicquam</i> = <i>et nihil</i>'],
    ['8', 'pondus iners', 'pondus, -eris (n.); iners, inertis', '"peso inerte, sem movimento"'],
    ['8', 'congesta … eōdem', 'congerō, -ere, -gessī, -gestum; eōdem (adv.)', '"amontoadas no mesmo lugar"; particípio perfeito, concorda com <i>sēmina</i>'],
    ['9', 'nōn bene iūnctārum … rērum', 'iungō, -ere, iūnxī, iūnctum', '"de coisas mal unidas": particípio no genitivo plural; <i>nōn bene</i> é lítotes'],
    ['9', 'discordia sēmina', 'discors, -cordis; sēmen, -inis (n.)', '"sementes discordantes": nom. pl. neutro, sujeito (com <i>pondus</i>) do <i>erat</i> subentendido'],
    ['10', 'Tītān', 'Tītān, -ānis (m.)', 'o Titã, isto é, o Sol (filho do titã Hiperíon); metonímia'],
    ['10', 'praebēbat lūmina', 'praebeō, -ēre; lūmen, -inis (n.)', '"oferecia as luzes", dava luz; imperfeito'],
    ['11', 'crēscendō', 'crēscō, -ere, crēvī', 'gerúndio no ablativo: "crescendo", "pelo crescimento" (capítulo 31)'],
    ['11', 'reparābat cornua Phoebē', 'reparō, -āre; cornū, -ūs (n.); Phoebē, -ēs (f.)', '"Febe (a Lua) renovava os chifres": os "chifres" são as pontas do crescente'],
    ['12', 'circumfūsō … in āere', 'circumfundō, -ere, -fūdī, -fūsum; āēr, āeris (m.)', '"no ar derramado à volta"; <i>in</i> + ablativo, não ablativo absoluto'],
    ['12', 'pendēbat', 'pendeō, -ēre', 'estar suspenso, pender'],
    ['12', 'tellūs', 'tellūs, -ūris (f.)', 'a terra (palavra poética, sinônimo de <i>terra</i>)'],
    ['13', 'ponderibus lībrāta suīs', 'lībrō, -āre', '"equilibrada pelo próprio peso": particípio perfeito + ablativo de meio; o plural <i>ponderibus</i> é poético'],
    ['13–14', 'bracchia … porrēxerat', 'bracchium, -ī (n.); porrigō, -ere, -rēxī, -rēctum', '"tinha estendido os braços": mais-que-perfeito'],
    ['14', 'margine', 'margō, -inis (m.)', 'margem, borda; <i>longō … margine</i>, "ao longo da extensa margem" (hipérbato)'],
    ['14', 'Amphitrītē', 'Amphitrītē, -ēs (f.)', 'deusa do mar, esposa de Netuno; por metonímia, o próprio mar'],
    ['15', 'pontus; aethēr', 'pontus, -ī (m.); aethēr, -eris (m.)', 'o mar (palavra poética); o éter, o ar puro e luminoso das alturas'],
    ['16', 'īnstabilis; innābilis', 'adjetivos em <i>-bilis</i>', '"instável" (onde não se pode ficar de pé); "impossível de nadar"'],
    ['17', 'lūcis egēns', 'egeō, -ēre (+ gen. ou abl.)', '"carente de luz": particípio presente com genitivo'],
    ['17', 'nūllī sua fōrma manēbat', 'maneō, -ēre', '"a nenhuma coisa permanecia a sua forma": <i>nūllī</i> é dativo'],
    ['18', 'obstābat aliīs aliud', 'obstō, -āre (+ dat.); alius, -a, -ud', '"uma coisa se opunha às outras"'],
    ['18', 'corpore in ūnō', 'corpus, -oris (n.)', '"num só corpo": a preposição vem depois do primeiro nome (anástrofe)'],
    ['19–20', 'frīgida … calidīs; ūmentia … siccīs; mollia cum dūrīs', 'frīgidus, calidus, ūmēns, siccus, mollis, dūrus', 'adjetivos neutros plurais substantivados: "as coisas frias" lutavam "com as quentes"; dativo com verbo de luta, construção dos poetas (Bennett § 358.3: <i>contendis Homērō</i>) e, no fim, <i>cum</i> + ablativo'],
    ['20', 'sine pondere habentia pondus', 'habeō, -ēre', '"as coisas sem peso com as que têm peso": <i>sine pondere</i> funciona como substantivo; <i>habentia</i> é particípio presente neutro plural'],
], 'Vocabulário e notas: Metamorfoses 1,5–20', latim_cols=(1,))}
<h3>Notas de leitura</h3>
<p><b>Versos 5–9.</b> O primeiro período é uma frase só: <i>ante mare … ūnus erat … vultus</i>, "antes do mar … havia uma única face". O sujeito, <i>vultus</i>, vem só no fim do verso 6, separado do seu adjetivo <i>ūnus</i>; <i>tōtō … in orbe</i> faz o mesmo. Em seguida, três apostos redefinem a coisa: <i>chaos</i>, <i>rudis indīgestaque mōlēs</i>, <i>pondus iners</i>, <i>discordia sēmina</i>. A expressão <i>nōn bene iūnctārum</i> é uma <b>lítotes</b>, a afirmação de uma ideia pela negação do contrário (Bennett § 375.1): "não bem unidas" = mal unidas, desunidas.</p>
<p><b>Versos 10–14.</b> Ovídio dá aos elementos os nomes dos deuses que os presidem: o Sol é <i>Tītān</i>, a Lua é <i>Phoebē</i>, o mar é <i>Amphitrītē</i>. É uma <b>metonímia</b> (o deus pela coisa), muito frequente na poesia, e o leitor precisa reconhecê-la para não procurar personagens onde há só sol, lua e mar. As imagens são precisas: a lua "renova os chifres" a cada mês, crescendo (<i>crēscendō</i>, gerúndio de meio); a terra "pende" no ar, "equilibrada pelo próprio peso"; o mar "estende os braços" ao longo das costas.</p>
<p><b>Versos 15–20.</b> O verso 15, na edição de Magnus, diz que o ar, a terra, o mar e o éter estavam todos "ali" (<i>illīc</i>), no mesmo lugar; daí a conclusão do verso 16, <i>sīc</i>, "assim": uma terra onde não se pisa, uma água onde não se nada, um ar sem luz. Os versos 19–20 fecham com uma série de <b>antíteses</b> em pares, frio e quente, úmido e seco, mole e duro, leve e pesado, que são as qualidades com que a física antiga descrevia os elementos. O último par é quase um paradoxo: <i>sine pondere habentia pondus</i>.</p>
{observacao('A leitura do verso 15', 'A edição de Magnus (1892), que este capítulo segue, lê <i>utque āēr, tellūs illīc et pontus et aethēr</i>, com ponto final, e começa nova frase com <i>Sīc erat</i>. Na sua edição escolar (1885), Magnus explica <i>ut</i> como "onde": "e onde estava o ar, ali estavam a terra, o mar e o éter". As outras edições antigas conferidas (Merkel e Ehwald, Teubner; Miller, Loeb, 1916; The Latin Library) leem <i>utque erat et tellūs illīc et pontus et āēr, / sīc erat īnstabilis tellūs…</i>: "e, embora ali houvesse terra, mar e ar, a terra era instável…". Nas duas leituras o sentido geral é o mesmo: os elementos existiam, mas misturados e sem as suas propriedades. Questões de texto como esta são normais nos autores antigos e são decididas pelos editores a partir dos manuscritos.')}
'''),
        ('A separação dos elementos (versos 21–31)', f'''
<p>No verso 21, de repente, aparece um agente: <i>deus et melior … nātūra</i>, "um deus e uma natureza melhor". Ovídio não diz que deus é, e mais adiante (v. 32) o chamará de <i>quisquis fuit ille deōrum</i>, "quem quer que tenha sido aquele dos deuses". O que importa é a ação, contada numa sequência de perfeitos: separou, apartou, desembaraçou, tirou, uniu.</p>
{_poema(SEPARACAO, SEPARACAO_PT, 21)}
{tabela(['v.', 'Palavra', 'Dicionário', 'Sentido e nota'], [
    ['21', 'hanc … lītem', 'līs, lītis (f.)', '"esta disputa", a luta descrita nos vv. 18–20; acusativo, com hipérbato'],
    ['21', 'dirēmit', 'dirimō, -ere, dirēmī, dirēmptum', 'separar, resolver (uma disputa); o verbo concorda com o sujeito mais próximo, <i>nātūra</i>'],
    ['22', 'abscidit', 'abscindō, -ere, abscidī, abscissum', 'arrancar, separar; o <i>i</i> breve (o metro o exige) mostra que vem de <i>abscindō</i>, não de <i>abscīdō</i>'],
    ['22', 'caelō terrās et terrīs … undās', 'caelum, terra, unda', 'ablativos de separação sem preposição: "do céu as terras, e das terras as águas"'],
    ['23', 'liquidum … caelum', 'liquidus, -a, -um', '"o céu límpido", isto é, o éter, separado do ar mais denso'],
    ['23', 'spissō … ab āere', 'spissus, -a, -um', '"do ar espesso"'],
    ['23', 'sēcrēvit', 'sēcernō, -ere, sēcrēvī, sēcrētum', 'separar, pôr à parte'],
    ['24', 'quae', 'quī, quae, quod', 'relativo de ligação: "e estas coisas", neutro plural (os elementos)'],
    ['24', 'ēvolvit', 'ēvolvō, -ere, ēvolvī', 'desenrolar, desembaraçar'],
    ['24', 'caecō … acervō', 'caecus, -a, -um; acervus, -ī (m.)', '"do montão cego (escuro)": ablativo de separação com <i>exēmit</i>'],
    ['24', 'exēmit', 'eximō, -ere, exēmī, exēmptum', 'tirar para fora'],
    ['25', 'dissociāta locīs', 'dissociō, -āre; locus, -ī (m.)', '"separados nos (seus) lugares": particípio perfeito neutro plural, concorda com <i>quae</i>'],
    ['25', 'concordī pāce ligāvit', 'concors, -cordis; pāx, pācis (f.); ligō, -āre', '"uniu numa paz concorde": ablativo de meio'],
    ['26', 'ignea … vīs', 'igneus, -a, -um; vīs (f.)', '"a força ígnea", o fogo, o mais leve dos elementos'],
    ['26', 'convexī … caelī', 'convexus, -a, -um', '"do céu convexo (em forma de abóbada)"; hipérbato que abraça o verso'],
    ['27', 'ēmicuit', 'ēmicō, -āre, ēmicuī', 'lançar-se, saltar para fora (como a chama)'],
    ['27', 'summā … in arce', 'summus, -a, -um; arx, arcis (f.)', '"no alto da cidadela", no ponto mais elevado'],
    ['28', 'proximus … illī', 'proximus, -a, -um (+ dat.)', '"o mais próximo dele (do fogo)"'],
    ['28', 'levitāte locōque', 'levitās, -ātis (f.); locus', 'ablativos de limitação: "em leveza e em lugar"'],
    ['29', 'dēnsior hīs', 'dēnsus, -a, -um; comparativo', '"mais densa que estes": <i>hīs</i> é ablativo de comparação (capítulo 18)'],
    ['29', 'elementa grandia', 'elementum, -ī (n.); grandis, -e', '"os elementos pesados (grosseiros)"'],
    ['30', 'pressa est', 'premō, -ere, pressī, pressum', 'perfeito passivo: "foi comprimida, ficou comprimida"'],
    ['30', 'circumfluus ūmor', 'circumfluus, -a, -um; ūmor, -ōris (m.)', '"a umidade que corre em volta", a água'],
    ['31', 'ultima possēdit', 'ultimus, -a, -um; possīdō, -ere, possēdī', '"ocupou os (lugares) extremos": <i>ultima</i> é neutro plural substantivado'],
    ['31', 'coercuit', 'coerceō, -ēre, coercuī', 'conter, cercar'],
], 'Vocabulário e notas: Metamorfoses 1,21–31', latim_cols=(1,))}
<h3>Notas de leitura</h3>
<p><b>Versos 21–25.</b> O verso 21 é o eixo do trecho, e a análise da seção 6 o examina palavra a palavra. Repare que <i>deus et melior nātūra</i> pode ser lido como dois sujeitos ("um deus e a natureza") ou como uma só ideia com duas palavras ("um deus, isto é, uma natureza melhor"); a gramática, com o verbo no singular, admite as duas leituras. Nos versos 22–23, o poeta repete as palavras em casos diferentes (<i>terrās et terrīs</i>), uma figura chamada poliptoto, para mostrar a separação em cadeia: céu / terras / águas; éter / ar. No verso 25, a expressão <i>dissociāta … concordī pāce ligāvit</i> junta separação e união: o deus separa para poder unir, e a ordem do mundo é uma "paz" entre elementos que antes lutavam (<i>pugnābant</i>, v. 19).</p>
<p><b>Versos 26–31.</b> A descrição segue a física antiga dos quatro elementos, ordenados pelo peso: o fogo, sem peso (<i>sine pondere</i>), sobe ao ponto mais alto; logo abaixo vem o ar, "o mais próximo em leveza e lugar"; a terra, mais densa, desce e fica comprimida "pelo próprio peso"; a água corre em volta e cerca o orbe sólido. Quatro elementos, quatro sujeitos (<i>vīs</i>, <i>āēr</i>, <i>tellūs</i>, <i>ūmor</i>), na ordem do mais leve ao mais pesado.</p>
{tabela(['Elemento', 'Palavra no texto', 'Qualidade', 'Lugar'], [
    ['fogo', '<i>ignea vīs</i> (v. 26)', 'sem peso (<i>sine pondere</i>)', 'o mais alto (<i>summā in arce</i>)'],
    ['ar', '<i>āēr</i> (v. 28)', 'leve (<i>levitāte</i>)', 'logo abaixo do fogo (<i>proximus illī</i>)'],
    ['terra', '<i>tellūs</i> (v. 29)', 'densa, pesada (<i>dēnsior</i>, <i>gravitāte suā</i>)', 'embaixo, comprimida (<i>pressa est</i>)'],
    ['água', '<i>circumfluus ūmor</i> (v. 30)', 'fluida', 'em volta da terra (<i>ultima possēdit</i>)'],
], 'Os quatro elementos depois da separação')}
'''),
        ('O hexâmetro de Ovídio', f'''
<p>As <i>Metamorfoses</i> estão em <b>hexâmetros datílicos</b>, o verso da epopeia, que você conheceu no capítulo 40 e encontrou como primeiro verso do dístico de Catulo 85 (capítulo 45). O esquema tem seis pés: os quatro primeiros podem ser dáctilos (<b>– ˘ ˘</b>) ou espondeus (<b>– –</b>); o quinto é quase sempre dáctilo; o sexto tem duas sílabas, a última indiferente (Bennett § 368.1; Kennedy § 477; Ravizza n. 536). Ovídio prefere hexâmetros rápidos, com muitos dáctilos, e evita elisões duras: é um bom autor para aprender a escandir.</p>
{tabela(['Pés', 'Esquema', 'Observação'], [
    ['1–4', '– ˘ ˘ ou – –', 'dáctilo ou espondeu, à escolha do poeta'],
    ['5', '– ˘ ˘', 'quase sempre dáctilo (com espondeu, o verso se diz espondaico)'],
    ['6', '– ×', 'duas sílabas; a última indiferente'],
], 'O hexâmetro datílico')}
<p>Primeiro verso do Caos, com uma elisão (<i>mar(e) et</i>):</p>
{tabela(['Pé', 'Sílabas', 'Tipo', 'Por quê'], [
    ['1', 'An | te | ma', 'dáctilo', '<i>An-</i> longa por posição (<i>n</i> + <i>t</i>); <i>te</i>, <i>ma</i> breves'],
    ['2', 'r(e) et | ter', 'espondeu', 'o <i>-e</i> de <i>mare</i> se elide; <i>ret</i> longa por posição (<i>t</i> + <i>t</i>); <i>ter</i> longa (<i>r</i> + <i>r</i>)'],
    ['3', 'rās ‖ et', 'espondeu', '<i>-ās</i> do acusativo plural, longo; <i>et</i> longa por posição (<i>t</i> + <i>qu</i>). Cesura depois de <i>terrās</i>'],
    ['4', 'quod | te | git', 'dáctilo', '<i>quod</i> longa (<i>d</i> + <i>t</i>); <i>te</i>, <i>git</i> breves (<i>git</i> antes de vogal)'],
    ['5', 'om | ni | a', 'dáctilo', '<i>om-</i> longa (<i>m</i> + <i>n</i>); <i>-ni-a</i> breves'],
    ['6', 'cae | lum', 'espondeu', 'ditongo <i>ae</i>; sílaba final'],
], 'Escansão de Metamorfoses 1,5: Ante mare et terrās et quod tegit omnia caelum')}
{tabela(['Pé', 'Sílabas', 'Tipo', 'Por quê'], [
    ['1', 'ū | nu | se', 'dáctilo', '<i>ū</i> longo por natureza; <i>-nus</i> + <i>e-</i>: o <i>s</i> passa à sílaba seguinte, e <i>nu</i>, <i>se</i> ficam breves'],
    ['2', 'rat | tō', 'espondeu', '<i>rat</i> longa por posição (<i>t</i> + <i>t</i>); <i>tō</i> longo por natureza'],
    ['3', 'tō ‖ nā', 'espondeu', 'ablativo <i>tōtō</i>, longo; <i>nā</i> longo por natureza. Cesura depois de <i>tōtō</i>'],
    ['4', 'tū | rae', 'espondeu', '<i>ū</i> longo; ditongo <i>ae</i>'],
    ['5', 'vul | tu | si', 'dáctilo', '<i>vul-</i> longa (<i>l</i> + <i>t</i>); <i>tus in</i> → <i>tu-sin</i>, breves'],
    ['6', 'nor | be', 'troqueu', '<i>nor</i> longa (<i>r</i> + <i>b</i>); <i>be</i> final indiferente'],
], 'Escansão de Metamorfoses 1,6: ūnus erat tōtō nātūrae vultus in orbe')}
<p>Agora o verso 21, que traz uma lição de gramática dentro da métrica:</p>
{tabela(['Pé', 'Sílabas', 'Tipo', 'Por quê'], [
    ['1', 'Hanc | de | us', 'dáctilo', '<i>hanc</i> longa (<i>n</i> + <i>c</i>); <i>de</i> breve antes de vogal; <i>us</i> breve (o <i>s</i> se junta a <i>et</i>)'],
    ['2', 'et | me | li', 'dáctilo', '<i>et</i> longa por posição (<i>t</i> + <i>m</i>); <i>me</i>, <i>li</i> breves'],
    ['3', 'or ‖ lī', 'espondeu', '<i>or</i> longa por posição (<i>r</i> + <i>l</i>); <i>lī</i> longo por natureza (<i>līs, lītis</i>). Cesura depois de <i>melior</i>'],
    ['4', 'tem | nā', 'espondeu', '<i>tem</i> longa (<i>m</i> + <i>n</i>); <i>nā</i> longo'],
    ['5', 'tū | ra | di', 'dáctilo', '<i>tū</i> longo; <b><i>ra</i> breve</b>; <i>di</i> breve'],
    ['6', 'rē | mit', 'espondeu', '<i>rē</i> longo (perfeito <i>dirēmī</i>); final indiferente'],
], 'Escansão de Metamorfoses 1,21: Hanc deus et melior lītem nātūra dirēmit')}
{dica('<b>A métrica decide o caso.</b> Sem macrons, <i>natura</i> pode ser nominativo (<i>nātūra</i>, <i>a</i> breve) ou ablativo (<i>nātūrā</i>, <i>ā</i> longo; Bennett § 363.1.a). No verso 21, o quinto pé tem de ser dáctilo, e <i>tū-ra-di</i> só é dáctilo se o <i>a</i> for breve: é nominativo, sujeito de <i>dirēmit</i>, e não um ablativo "pela natureza". O mesmo raciocínio mostra, no verso 22, que <i>abscidit</i> tem <i>i</i> breve (pé 5: <i>abs-ci-dit</i>) e vem de <i>abscindō</i>.')}
<h3>A cesura</h3>
<p>Nos três versos, uma palavra termina logo depois da primeira sílaba longa do terceiro pé: depois de <i>terrās</i>, de <i>tōtō</i>, de <i>melior</i>. É a <b>cesura pentemímera</b> (de "cinco meios pés"), a mais comum do hexâmetro (Bennett § 368.3.a; Kennedy § 477; Ravizza n. 536), que divide o verso em duas partes desiguais e marca uma pausa leve na leitura. Às vezes a cesura cai entre as duas breves do terceiro pé (cesura feminina, Bennett § 368.3.c), ou no quarto pé, acompanhada de outra no segundo (Bennett § 368.3.b).</p>
{observacao('Quantidades das palavras gregas', 'As palavras que o latim tomou do grego conservam as quantidades gregas (Bennett § 365; A&amp;G § 603.a.4). Por isso <i>āēr</i> tem as duas vogais longas no nominativo (v. 17: <i>lū-ci-se | gēns-ā | ēr-nūl</i>…), embora nos outros casos se diga <i>āĕris, āĕre</i> (v. 12: <i>in āere</i>); <i>aethēr</i>, <i>Tītān</i>, <i>Phoebē</i> e <i>Amphitrītē</i> terminam em sílaba longa. O nominativo <i>tellūs</i> também é longo, mas por outra razão: o <i>u</i> pertence ao tema (<i>tellūris</i>; Bennett § 364.6.b).')}
'''),
        ('Língua e estilo: particípios, gerúndio, figuras; Ovídio e o Gênesis', f'''
<p>A descrição do Caos é feita, em boa parte, com <b>particípios</b> (capítulo 29). Quase todos são particípios conjuntos, isto é, concordam com um nome da frase e o qualificam: <i>congesta</i> (com <i>sēmina</i>), <i>iūnctārum</i> (com <i>rērum</i>), <i>lībrāta</i> (com <i>tellūs</i>), <i>dissociāta</i> (com <i>quae</i>), <i>habentia</i> (neutro plural substantivado). Um caso pede atenção: <i>circumfūsō … in āere</i> (v. 12) é um particípio no ablativo concordando com um nome no ablativo, mas <b>não</b> é ablativo absoluto (capítulo 30), porque a preposição <i>in</i> liga o grupo ao verbo <i>pendēbat</i>: "pendia no ar derramado em volta". O ablativo absoluto é gramaticalmente independente da oração (Bennett § 227) e nunca vem regido por preposição.</p>
{tabela(['Forma', 'Verso', 'Tipo', 'Concorda com', 'Tradução'], [
    ['congesta', '8', 'particípio perfeito passivo, nom. pl. n.', '<i>sēmina</i>', 'amontoadas'],
    ['iūnctārum', '9', 'particípio perfeito passivo, gen. pl. f.', '<i>rērum</i>', 'unidas'],
    ['circumfūsō', '12', 'particípio perfeito passivo, abl. sing. m.', '<i>āere</i> (com <i>in</i>)', 'derramado em volta'],
    ['lībrāta', '13', 'particípio perfeito passivo, nom. sing. f.', '<i>tellūs</i>', 'equilibrada'],
    ['egēns', '17', 'particípio presente, nom. sing.', '<i>āēr</i>', 'carente'],
    ['habentia', '20', 'particípio presente, nom. pl. n. (substantivado)', 'nenhum nome: vale por si', 'as coisas que têm'],
    ['dissociāta', '25', 'particípio perfeito passivo, ac. pl. n.', '<i>quae</i>', 'separados'],
    ['pressa est', '30', 'perfeito passivo (particípio + <i>est</i>)', 'sujeito <i>tellūs</i>', 'foi comprimida'],
], 'Os particípios de Metamorfoses 1,5–31', latim_cols=(0,))}
<p>O único <b>gerúndio</b> do trecho é <i>crēscendō</i> (v. 11), no ablativo sem preposição, com valor de meio ou de modo: a Lua renovava os chifres "crescendo", "pelo crescimento" (Bennett § 338.4.a, com o exemplo <i>mēns discendō alitur</i>, "a mente se alimenta aprendendo"). Entre os ablativos, distinga ainda os de <b>separação</b> (<i>caelō terrās … abscidit</i>, <i>caecō exēmit acervō</i>), o de <b>comparação</b> (<i>dēnsior hīs</i>), os de <b>limitação</b> (<i>levitāte locōque</i>, "em leveza e lugar") e os de <b>meio</b> (<i>ponderibus lībrāta suīs</i>, <i>concordī pāce ligāvit</i>; Bennett § 218).</p>
{diagrama_frase([('Ante … caelum', 'ante + acusativo · "antes de…"'), ('ūnus … vultus', 'nominativo · sujeito'), ('erat', 'verbo · "havia"'), ('tōtō … in orbe', 'in + ablativo · "em todo o orbe"'), ('nātūrae', 'genitivo · "da natureza"')],
    'O primeiro período do Caos (vv. 5–6) reduzido ao essencial: <i>Ante mare … ūnus erat nātūrae vultus tōtō in orbe</i> = Antes do mar … havia em todo o orbe uma só face da natureza. Os dois hipérbatos (<i>ūnus … vultus</i>, <i>tōtō … in orbe</i>) obrigam a guardar o adjetivo na memória até o fim do verso.')}
<h3>Ovídio e o começo do Gênesis</h3>
<p>Muitos leitores, desde a Antiguidade cristã, compararam esta página com o início da Bíblia. A Vulgata começa assim (Gênesis 1,1–3):</p>
{exemplos([('In prīncipiō creāvit Deus caelum et terram. Terra autem erat inānis et vacua, et tenebrae erant super faciem abyssī: et spīritus Deī ferēbātur super aquās. Dīxitque Deus: Fīat lūx. Et facta est lūx.', 'No princípio, Deus criou o céu e a terra. Ora, a terra era informe e vazia, e as trevas estavam sobre a face do abismo, e o Espírito de Deus pairava sobre as águas. E Deus disse: Faça-se a luz. E a luz foi feita. (Vulgata Clementina; tradução nossa)')])}
{comparacao('Duas narrativas do começo', ['Ponto', 'Ovídio, Metamorfoses 1', 'Gênesis 1 (Vulgata)'], [
    ['Estado inicial', '<i>chaos</i>, <i>rudis indīgestaque mōlēs</i>: matéria já existente, misturada', '<i>terra … inānis et vacua</i>, <i>tenebrae super faciem abyssī</i>'],
    ['Quem age', '<i>deus et melior nātūra</i>; "quem quer que tenha sido aquele dos deuses" (v. 32)', '<i>Deus</i>, o único, nomeado desde a primeira frase'],
    ['Como age', 'separa e ordena o que já existia (<i>abscidit, sēcrēvit, ligāvit</i>)', 'cria (<i>creāvit</i>) e ordena pela palavra (<i>Dīxitque Deus: Fīat lūx</i>)'],
    ['Imagem da ordem', 'cada elemento no seu lugar, por peso; uma <i>concors pāx</i>', 'separação da luz e das trevas, das águas e da terra, em seis dias'],
])}
<p>A semelhança de quadro é real, e a palavra-chave dos dois textos é a mesma: <b>separar</b> (<i>dīvīsit</i>, no Gênesis 1,4; <i>abscidit</i>, <i>sēcrēvit</i>, em Ovídio). A diferença também é clara: em Ovídio a matéria já estava lá, e o deus é anônimo e quase um artesão; no Gênesis, Deus cria (<i>creāvit</i>) e chama as coisas ao ser pela palavra. Ler os dois textos lado a lado ajuda a perceber o que cada um afirma, sem fazer de um a cópia do outro.</p>
'''),
        ('Análise palavra a palavra', f'''
<p>O verso 21 resolve a luta descrita nos dezesseis versos anteriores e é um bom exercício de ordem das palavras: o objeto abre o verso, o sujeito se divide em dois e o verbo fecha.</p>
{analise('Metamorfoses 1,21, palavra a palavra', [
    ('Hanc', 'hīc, haec, hōc, este', 'acusativo singular feminino', 'concorda com <i>lītem</i> (hipérbato)'),
    ('deus', 'deus, -ī (m.), deus', 'nominativo singular', 'sujeito (1º membro)'),
    ('et', 'et (conjunção)', 'invariável', 'liga <i>deus</i> e <i>nātūra</i>'),
    ('melior', 'melior, melius, comparativo de bonus', 'nominativo singular feminino', 'concorda com <i>nātūra</i>: "uma natureza melhor"'),
    ('lītem', 'līs, lītis (f.), disputa, litígio', 'acusativo singular', 'objeto direto de <i>dirēmit</i>'),
    ('nātūra', 'nātūra, -ae (f.), natureza', 'nominativo singular (o metro exige <i>a</i> breve)', 'sujeito (2º membro)'),
    ('dirēmit', 'dirimō, -ere, dirēmī, dirēmptum, separar, resolver', 'perfeito do indicativo ativo, 3ª sing.', 'verbo; concorda com o sujeito mais próximo'),
])}
<p>Três observações. O demonstrativo <i>hanc</i> retoma tudo o que veio antes: "esta luta" é a dos frios com os quentes, dos úmidos com os secos (vv. 18–20). O verbo no singular com dois sujeitos é normal quando o verbo concorda com o mais próximo, e aqui reforça a possibilidade de que "deus" e "natureza melhor" sejam uma só realidade vista de dois lados. E <i>dirimere lītem</i> é linguagem jurídica, "dirimir um litígio", expressão que o português conservou: o deus age como um juiz que põe fim a um processo.</p>
<p>Os versos seguintes completam o período com a mesma construção, agora com ablativos de separação:</p>
{analise('Metamorfoses 1,22, palavra a palavra', [
    ('Nam', 'nam (conjunção)', 'invariável', 'explica o verso anterior: "pois"'),
    ('caelō', 'caelum, -ī (n.), céu', 'ablativo singular', 'separação: "do céu"'),
    ('terrās', 'terra, -ae (f.), terra', 'acusativo plural', 'objeto de <i>abscidit</i>'),
    ('et', 'et (conjunção)', 'invariável', 'liga os dois pares'),
    ('terrīs', 'terra, -ae (f.)', 'ablativo plural', 'separação: "das terras" (poliptoto com <i>terrās</i>)'),
    ('abscidit', 'abscindō, -ere, abscidī, abscissum, arrancar, separar', 'perfeito do indicativo ativo, 3ª sing.', 'verbo das duas orações; sujeito: o deus'),
    ('undās', 'unda, -ae (f.), onda, água', 'acusativo plural', 'objeto de <i>abscidit</i>'),
])}
<h3>Resumo</h3>
<ul>
<li>O proêmio anuncia o assunto (<i>mūtātās fōrmās</i>), a fonte (os deuses, autores das mudanças) e o plano (da origem do mundo ao tempo do poeta, num <i>perpetuum carmen</i>).</li>
<li>O Caos é descrito por negações (<i>nec … nec</i>), metonímias (<i>Tītān, Phoebē, Amphitrītē</i>) e antíteses (<i>frīgida … calidīs</i>); a ordem, por uma série de perfeitos de separação (<i>dirēmit, abscidit, sēcrēvit, exēmit, ligāvit</i>).</li>
<li>Hexâmetro: quatro pés livres (dáctilo ou espondeu), quinto dáctilo, sexto de duas sílabas; cesura principal pentemímera.</li>
<li>A métrica decide quantidades e casos: <i>nātūra</i> nominativo no v. 21, <i>abscĭdit</i> de <i>abscindō</i> no v. 22.</li>
<li>Particípios conjuntos não são ablativos absolutos: <i>circumfūsō in āere</i> depende de <i>in</i> e do verbo.</li>
</ul>
<p>No próximo capítulo, o hexâmetro volta com Virgílio, na noite da queda de Troia (<i>Eneida</i> II).</p>
'''),
    ],
    erros_comuns=[
        ('Ler <i>nātūra</i> (v. 21) como ablativo, "pela natureza", e fazer de <i>deus</i> o único sujeito.', 'Sem macrons a forma é ambígua, mas o metro exige o <i>a</i> breve no quinto pé (<i>tū-ra-di</i>), e o <i>a</i> breve é do nominativo. <i>Nātūra</i> é sujeito ao lado de <i>deus</i>, e <i>melior</i> (nominativo feminino) concorda com ela.'),
        ('Tomar <i>circumfūsō in āere</i> por um ablativo absoluto.', 'O ablativo absoluto é independente da oração e não vem com preposição. Aqui <i>in</i> + ablativo indica o lugar onde a terra "pendia" (<i>pendēbat</i>), e <i>circumfūsō</i> é um particípio que concorda com <i>āere</i>: "no ar derramado em volta".'),
        ('Procurar personagens em <i>Tītān</i>, <i>Phoebē</i> e <i>Amphitrītē</i> e traduzir como se fossem deuses agindo na cena.', 'São metonímias: o nome do deus pelo elemento que ele preside. <i>Tītān</i> é o Sol, <i>Phoebē</i> a Lua, <i>Amphitrītē</i> o mar. Na tradução, mantenha o nome e, se preciso, explique numa nota; o sentido é "não havia sol, nem lua, nem mar".'),
        ('Traduzir <i>dīxēre</i> (v. 7) como infinitivo ("dizer").', 'O infinitivo de <i>dīcō</i> é <i>dīcere</i>. <i>Dīxēre</i>, com o tema do perfeito <i>dīx-</i> e o <i>ē</i> longo, é a 3ª pessoa do plural do perfeito, variante poética de <i>dīxērunt</i> (Bennett § 101): "chamaram".'),
        ('Escandir sem elidir: <i>An-te-ma-re-et-ter-rās</i>…', 'Vogal final diante de vogal se elide (Bennett § 366.7): <i>mar(e) et</i> conta como uma sílaba, <i>ret</i>, longa por posição. Marque todas as elisões antes de dividir os pés; um hexâmetro tem, salvo raríssimas exceções, entre treze e dezessete sílabas.'),
        ('Ligar os adjetivos à palavra mais próxima: em <i>longō margine</i> isso funciona, mas ler <i>ūnus erat</i> como "um era" ou <i>tōtō nātūrae</i> como "de toda a natureza" está errado.', 'Em <i>ūnus erat tōtō nātūrae vultus in orbe</i>, <i>ūnus</i> concorda com <i>vultus</i> (nominativo masculino), quatro palavras adiante; <i>tōtō</i> com <i>orbe</i> (ablativo). Deixe o adjetivo em suspenso até encontrar o nome com o mesmo gênero, número e caso.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Ler os versos 10–12',
            'Leia e traduza, na ordem latina: <i lang="la">nūllus adhūc mundō praebēbat lūmina Tītān, nec nova crēscendō reparābat cornua Phoebē, nec circumfūsō pendēbat in āere tellūs</i>. Use o vocabulário da seção 2.', [
            ('Que forma é <i>nūllus</i>, e o que ela faz esperar?', 'Nominativo singular masculino de <i>nūllus</i>. Espera-se um nome masculino no nominativo com que ele concorde, e esse nome só aparece no fim do verso: <i>Tītān</i>. Até lá, <i>nūllus</i> fica em suspenso.'),
            ('Analise <i>mundō praebēbat lūmina</i>.', '<i>Mundō</i>: dativo singular, "ao mundo"; <i>praebēbat</i>: imperfeito, 3ª sing., "oferecia"; <i>lūmina</i>: acusativo plural neutro de <i>lūmen</i>, objeto. "Nenhum Titã dava ainda luz ao mundo."'),
            ('No segundo verso, com que nome concorda <i>nova</i>?', '<i>Nova</i> pode ser nominativo feminino singular ou neutro plural (nominativo ou acusativo). O sujeito feminino é <i>Phoebē</i>, mas o sentido e a posição indicam <i>cornua</i> (acusativo plural neutro): "os chifres novos". O hipérbato separa <i>nova</i> de <i>cornua</i> por duas palavras.'),
            ('Que forma é <i>crēscendō</i>?', 'Gerúndio no ablativo, sem preposição, com valor de meio ou de modo: "crescendo, pelo crescimento". A Lua renova as pontas do crescente a cada mês.'),
            ('Traduza o terceiro verso e diga se há ablativo absoluto.', '"Nem a terra pendia no ar derramado em volta." Não há ablativo absoluto: <i>circumfūsō</i> concorda com <i>āere</i>, e o grupo é regido pela preposição <i>in</i>; <i>tellūs</i>, nominativo, é o sujeito de <i>pendēbat</i>.'),
        ]),
        pratica_guiada('Prática guiada 2 · Escandir o verso 19',
            'Escanda <i lang="la">frīgida pugnābant calidīs, ūmentia siccīs</i>.', [
            ('Há elisões?', 'Não: <i>calidīs</i> termina em <i>s</i>, e nenhuma palavra termina em vogal diante de outra vogal. O verso tem quinze sílabas (<i>ūmentia</i> conta quatro): <i>frī-gi-da-pug-nā-bant-ca-li-dīs-ū-men-ti-a-sic-cīs</i>.'),
            ('Os dois primeiros pés?', '<i>frī-gi-da</i>: <i>frī</i> longo por natureza, <i>gi</i> e <i>da</i> breves, dáctilo. <i>pug-nā</i>: <i>pug</i> longa por posição (<i>g</i> + <i>n</i>), <i>nā</i> longo por natureza: espondeu.'),
            ('Terceiro e quarto pés?', '<i>bant-ca-li</i>: <i>bant</i> longa por posição, <i>ca</i> e <i>li</i> breves: dáctilo. <i>dīs-ū</i>: <i>-īs</i> longo do ablativo/dativo plural (Bennett § 364.5.a) e <i>ū</i> longo por natureza: espondeu. A cesura cai depois de <i>pugnābant</i>, na primeira sílaba do terceiro pé: pentemímera.'),
            ('Termine o verso.', '<i>men-ti-a</i>: <i>men</i> longa por posição (<i>n</i> + <i>t</i>), <i>ti</i> e <i>a</i> breves: dáctilo (o quinto pé, como deve ser). <i>sic-cīs</i>: espondeu.'),
        ], 'Esquema: – ˘ ˘ | – – | – ˘ ˘ | – – | – ˘ ˘ | – –. A métrica confirma que <i>calidīs</i> e <i>siccīs</i> são formas em <i>-īs</i> (dativo plural), e não um nominativo singular em <i>-is</i>.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Compreensão', 'Responda em português, citando o latim.', [
            ('Que três coisas "ainda não" existiam, segundo os versos 10–14?', 'O sol (<i>nūllus … Tītān</i>), a lua com as suas fases (<i>nec … Phoebē</i>) e a terra suspensa no ar (<i>nec … pendēbat … tellūs</i>); também não havia o mar com margens (<i>nec bracchia … porrēxerat Amphitrītē</i>).'),
            ('Por que nada conservava a sua forma (v. 17)?', 'Porque tudo estava num só corpo (<i>corpore in ūnō</i>) e os contrários lutavam entre si: frio com quente, úmido com seco, mole com duro, leve com pesado (vv. 18–20).'),
            ('Quem pôs fim à desordem?', '<i>Deus et melior nātūra</i> (v. 21), "um deus e uma natureza melhor"; Ovídio não diz que deus, e mais adiante o chama "quem quer que tenha sido aquele dos deuses".'),
            ('Em que ordem ficaram os elementos, e por quê?', 'Do mais leve ao mais pesado: o fogo no alto, o ar logo abaixo, a terra comprimida embaixo, a água em volta. O critério é o peso (<i>sine pondere</i>, <i>levitāte</i>, <i>gravitāte suā</i>).'),
        ]),
        exercicio('Exercício 2 · Morfologia', 'Dê a análise completa e a forma de dicionário.', [
            ('<i>dīxēre</i> (v. 7)', 'Perfeito do indicativo ativo, 3ª pl., de <i>dīcō, -ere, dīxī, dictum</i>; = <i>dīxērunt</i>.'),
            ('<i>porrēxerat</i> (v. 14)', 'Mais-que-perfeito do indicativo ativo, 3ª sing., de <i>porrigō, -ere, porrēxī, porrēctum</i>: "tinha estendido".'),
            ('<i>egēns</i> (v. 17)', 'Particípio presente ativo, nominativo singular, de <i>egeō, -ēre</i>; concorda com <i>āēr</i> e rege o genitivo <i>lūcis</i>.'),
            ('<i>sēcrēvit</i> (v. 23)', 'Perfeito do indicativo ativo, 3ª sing., de <i>sēcernō, -ere, sēcrēvī, sēcrētum</i>.'),
            ('<i>pressa est</i> (v. 30)', 'Perfeito do indicativo passivo, 3ª sing. feminino, de <i>premō, -ere, pressī, pressum</i>; concorda com <i>tellūs</i>.'),
            ('<i>dēnsior</i> (v. 29)', 'Comparativo de <i>dēnsus, -a, -um</i>, nominativo singular feminino (concorda com <i>tellūs</i>); o segundo termo, <i>hīs</i>, está no ablativo de comparação.'),
        ]),
        exercicio('Exercício 3 · Sintaxe dos casos', 'Diga o caso e a função das palavras destacadas.', [
            ('<i>nūllī</i> sua fōrma manēbat (v. 17)', 'Dativo singular: "a nenhuma coisa permanecia a sua forma", isto é, nenhuma coisa conservava a sua forma (dativo de posse ou de interesse).'),
            ('nam <i>caelō</i> terrās et <i>terrīs</i> abscidit undās (v. 22)', 'Ablativos de separação, sem preposição, com um verbo de separar: "do céu", "das terras".'),
            ('proximus est āēr <i>illī</i> <i>levitāte</i> locōque (v. 28)', '<i>Illī</i>: dativo regido por <i>proximus</i>, "dele (do fogo)". <i>Levitāte</i> (e <i>locō</i>): ablativos de limitação, "em leveza e em lugar".'),
            ('dēnsior <i>hīs</i> tellūs (v. 29)', 'Ablativo de comparação: "mais densa que estes (o fogo e o ar)".'),
            ('<i>crēscendō</i> (v. 11)', 'Ablativo do gerúndio, sem preposição: meio ou modo, "crescendo".'),
        ]),
        exercicio('Exercício 4 · Métrica', 'Escanda e justifique.', [
            ('Escanda o verso 7: <i>quem dīxēre chaos: rudis indīgestaque mōlēs</i>.', '<i>quem dī</i> | <i>xē re cha</i> | <i>os ‖ ru dis</i> | <i>in dī</i> | <i>ges ta que</i> | <i>mō lēs</i>: espondeu, dáctilo, dáctilo, espondeu, dáctilo, espondeu. <i>Os</i> fica longa por posição (<i>s</i> + <i>r</i>); <i>in-</i> também (<i>n</i> + <i>d</i>). Cesura depois de <i>chaos</i>.'),
            ('Escanda o verso 22: <i>Nam caelō terrās et terrīs abscidit undās</i>.', '<i>Nam cae</i> | <i>lō ter</i> | <i>rās ‖ et</i> | <i>ter rīs</i> | <i>abs ci dit</i> | <i>un dās</i>: quatro espondeus, dáctilo e espondeu. O quinto pé (<i>abs-ci-dit</i>) só é dáctilo com <i>i</i> breve: o verbo é <i>abscindō</i>.'),
            ('Por que o verso 28 começa por um dáctilo (<i>prox-i-mus</i>) se <i>-mus</i> é seguido de <i>est</i>?', 'Porque <i>est</i> começa por vogal: o <i>s</i> de <i>-mus</i> passa para a sílaba seguinte (<i>mu-sest</i>), e <i>mu</i> fica aberta e breve. Só uma consoante depois da vogal não faz posição.'),
        ]),
        exercicio('Exercício 5 · Tradução e comentário', 'Traduza e comente brevemente.', [
            ('Traduza os versos 26–27: <i>Ignea convexī vīs et sine pondere caelī / ēmicuit summāque locum sibi fēcit in arce</i>.', '"A força ígnea e sem peso do céu convexo lançou-se para cima e fez para si um lugar no ponto mais alto." <i>Vīs</i> é o sujeito, com <i>ignea</i> e <i>sine pondere</i>; <i>convexī … caelī</i>, genitivo, abraça o verso (hipérbato); <i>sibi</i> é dativo de interesse.'),
            ('Traduza os versos 30–31: <i>circumfluus ūmor / ultima possēdit solidumque coercuit orbem</i>.', '"A água que corre em volta ocupou os lugares extremos e encerrou o orbe sólido." <i>Ultima</i> é neutro plural substantivado, objeto de <i>possēdit</i>; <i>solidum orbem</i> é o objeto de <i>coercuit</i>.'),
            ('Em três ou quatro linhas, compare o agente da ordem em Ovídio (v. 21) e no Gênesis 1,1–3.', 'Em Ovídio, o agente é indeterminado, <i>deus et melior nātūra</i>, e trabalha sobre uma matéria que já existe, separando e unindo (<i>abscidit, sēcrēvit, ligāvit</i>). No Gênesis, <i>Deus</i> é nomeado desde a primeira frase, cria (<i>creāvit</i>) o céu e a terra e dá forma ao mundo pela palavra (<i>Dīxitque Deus: Fīat lūx</i>). Os dois textos têm em comum a ideia de que ordenar é separar.'),
        ]),
    ],
    leituras=['naso-metamorphoses-texto-integral', 'naso-metamorphoses-iii-511-733-penteu', 'naso-amores-liber-i', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'ravizza-gramatica-latina', 'bennett-new-latin-grammar'],
    leituras_nota='Continue na edição de Magnus (Perseus) com o resto da criação (1,32–88), até o nascimento do homem, e depois com as Quatro Idades (1,89–150): os mesmos hábitos de leitura deste capítulo bastam. Para um episódio inteiro com vocabulário e notas em página oposta, a edição comentada de Gildenhard e Zissos traz Penteu e Baco (livro III), de acesso aberto. Se quiser treinar o dístico elegíaco de Ovídio, o livro I dos <i>Amores</i> na edição comentada do DCC tem vocabulário, notas e áudio. Para a comparação com a Bíblia, leia Gênesis 1 inteiro na Vulgata. As regras de métrica estão em Ravizza (nn. 533–536) e em Bennett (§§ 366–368).',
)
