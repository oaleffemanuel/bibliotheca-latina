from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Texto latino: César, De bello Gallico I, 1, ed. T. Rice Holmes (Oxford: Clarendon, 1914), conferido no Perseus
# (Perseus:text:1999.02.0002) e na The Latin Library (caesar/gall1.shtml), com as mesmas palavras.
# Holmes põe os §§ 5–7 entre colchetes (suspeita de interpolação); o texto é dado inteiro, com nota.
# Macrons acrescentados. Auditoria 2026-10-15: Matrona (L&S Matrŏna, sem ā), Orgetorix (L&S Orgĕtŏrix, -ĭgis), Pȳrēnaeus (L&S).
TEXTO = [
    ('1', 'Gallia est omnis dīvīsa in partēs trēs, quārum ūnam incolunt Belgae, aliam Aquītānī, tertiam quī ipsōrum linguā Celtae, nostrā Gallī appellantur.'),
    ('2', 'Hī omnēs linguā, īnstitūtīs, lēgibus inter sē differunt. Gallōs ab Aquītānīs Garumna flūmen, ā Belgīs Matrona et Sēquana dīvidit.'),
    ('3', 'Hōrum omnium fortissimī sunt Belgae, proptereā quod ā cultū atque hūmānitāte prōvinciae longissimē absunt, minimēque ad eōs mercātōrēs saepe commeant atque ea quae ad effēminandōs animōs pertinent important,'),
    ('4', 'proximīque sunt Germānīs, quī trāns Rhēnum incolunt, quibuscum continenter bellum gerunt. Quā dē causā Helvētiī quoque reliquōs Gallōs virtūte praecēdunt, quod ferē cotīdiānīs proeliīs cum Germānīs contendunt, cum aut suīs fīnibus eōs prohibent aut ipsī in eōrum fīnibus bellum gerunt.'),
    ('5', 'Eōrum ūna pars, quam Gallōs obtinēre dictum est, initium capit ā flūmine Rhodanō, continētur Garumnā flūmine, Ōceanō, fīnibus Belgārum, attingit etiam ab Sēquanīs et Helvētiīs flūmen Rhēnum, vergit ad septentriōnēs.'),
    ('6', 'Belgae ab extrēmīs Galliae fīnibus oriuntur, pertinent ad īnferiōrem partem flūminis Rhēnī, spectant in septentriōnem et orientem sōlem.'),
    ('7', 'Aquītānia ā Garumnā flūmine ad Pȳrēnaeōs montēs et eam partem Ōceanī quae est ad Hispāniam pertinet; spectat inter occāsum sōlis et septentriōnēs.'),
]

LICAO = dict(
    slug='44-cesar', titulo='César: o início da Guerra da Gália',
    titulo_latim='Caesar', tempo='90 min',
    resumo='Leitura comentada do primeiro capítulo da Guerra da Gália (Gallia est omnis dīvīsa in partēs trēs): César e os seus Comentários, a narração em terceira pessoa, o texto latino com vocabulário e notas, um mapa em tabela dos povos, rios e montes, as orações relativas, a oração infinitiva e o ablativo absoluto no texto e nos capítulos seguintes, a análise da frase inicial e a tradução.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['César', 'Commentarii de bello Gallico', 'Gallia est omnis divisa', 'narração em terceira pessoa', 'geografia da Gália', 'belgas, aquitanos e celtas', 'rios da Gália', 'orações relativas', 'antecedente omitido', 'relativo de ligação (quā dē causā)', 'quibuscum', 'oração infinitiva em texto', 'dictum est com oração infinitiva', 'ablativo absoluto com cōnsulibus', 'ablativo de especificação', 'dativo com proximus', 'superlativos', 'gerundivo (glosa)', 'cum com indicativo', 'leitura comentada'],
    prerequisitos=dict(texto='Capítulos 28 e 30: a oração infinitiva (acusativo com infinitivo) e o ablativo absoluto, que você vai encontrar no texto e nos dois trechos complementares (I, 2 e I, 7). Também são usados os pronomes relativos (capítulo 16), os superlativos (capítulo 18), os usos dos casos (capítulos 20–21) e a passiva (capítulos 23–24). O gerundivo (capítulo 31) e o <i>cum</i> com indicativo (capítulo 34) aparecem uma vez cada e estão glosados.',
                       licoes=['28-a-oracao-infinitiva', '30-o-ablativo-absoluto']),
    referencias=[
        referencia('C. Iuli Caesaris Commentarii rerum in Gallia gestarum VII, ed. T. Rice Holmes (Oxford: Clarendon, 1914)', 'Caio Júlio César', catalogo='caesar-commentarii-de-bello-gallico-texto-integral', url='https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0002:book=1:chapter=1', nota='texto de I, 1, I, 2.1 e I, 7.1 conferido no Perseus, que reproduz a edição de Holmes; Holmes põe I, 1, 5–7 entre colchetes e, em I, 2.1, as palavras [et P.]; comparado com a The Latin Library (caesar/gall1.shtml), mesmas palavras; macrons acrescentados', tipo='dominio_publico'),
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 142.4 (cum anexado ao relativo: quibuscum), § 192.1 (dativo com adjetivos de proximidade, com o exemplo sunt proximī Germānīs), § 214 (ablativo de separação), § 218 (ablativo de meio), § 226 (ablativo de especificação, com Helvētiī … virtūte praestābant), § 227 e 227.1 (ablativo absoluto; Cn. Pompejō, M. Crassō cōnsulibus), § 250.1 e 250.3 (concordância do relativo; Belgae, quae est tertia pars), § 251.1 (antecedente omitido), § 259.3 (presente histórico), § 286.1 (quod causal com indicativo), § 330 (infinitivo com sujeito acusativo como sujeito de expressões impessoais), § 331 (como objeto de verbos de dizer e saber), § 339.2 (gerundivo com ad: ad pācem petendam), § 350.7.b (quā dē causā), § 350.9 (palavras que retomam a frase anterior vêm primeiro)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 305 (concordância do relativo), § 307.c (antecedente omitido), §§ 383–384 (dativo com adjetivos), § 418 (ablativo de especificação), § 419 e 419.a (ablativo absoluto; L. Domitiō Ap. Claudiō cōnsulibus), § 424.g (datas pelos cônsules: L. Pīsōne A. Gabīniō cōnsulibus, B. G. 1, 6), § 506 (gerúndio e gerundivo com ad: finalidade), § 540 (quod causal com indicativo), § 547 (cum temporal com presente do indicativo), §§ 577–579 (discurso indireto; acusativo com infinitivo depois de verbos de dizer e saber), §§ 597–598 (ordem das palavras, com comentário de ênfase à abertura da Guerra da Gália)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 195 (concordância do relativo), § 237 (ablativo absoluto; nātus est Augustus cōnsulibus Cicerōne et Antōniō)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 175 (concordância do relativo), n. 296 (ablativo absoluto), n. 379 (acusativo com infinitivo depois de verbos de sentir e de dizer)', tipo='dominio_publico'),
    ],
    objetivos=[
        'Situar César e os <i>Comentários</i> e explicar o efeito da narração em terceira pessoa.',
        'Ler e traduzir <i>De bello Gallico</i> I, 1 com o vocabulário e as notas, e desenhar (numa tabela ou num esboço) a divisão da Gália que o texto descreve.',
        'Identificar cada oração relativa do texto, o seu antecedente (expresso, omitido ou retomado) e o caso do relativo.',
        'Reconhecer e traduzir a oração infinitiva (<i>quam Gallōs obtinēre dictum est</i>; <i>eōs … iter facere cōnārī</i>) e o ablativo absoluto de data (<i>M. Messālā, M. Pīsōne cōnsulibus</i>).',
        'Explicar os usos dos casos mais frequentes do trecho: ablativo de especificação, dativo com <i>proximus</i>, <i>ab</i> no sentido de "do lado de".',
    ],
    secoes=[
        ('César e os seus Comentários', f'''
<p>Caio Júlio César (<i>Gāius Iūlius Caesar</i>, 100–44 a.C.) foi general, político e, para a posteridade, também escritor. Entre 58 e 50 a.C., como governador das províncias da Gália, conduziu as campanhas que submeteram a Roma o território das atuais França e Bélgica e de partes da Suíça, da Alemanha e dos Países Baixos. Sobre essas campanhas ele escreveu os <i>Commentāriī dē bellō Gallicō</i>, os "Comentários sobre a Guerra da Gália", em sete livros, um por ano de guerra (um oitavo foi acrescentado depois por Aulo Hírcio, um oficial seu). O título é modesto de propósito: <i>commentārius</i> era um relatório, uma coleção de notas que serviria de material para um historiador. O resultado, porém, é uma prosa tão clara, regular e econômica que se tornou, por séculos, o primeiro texto clássico lido nas escolas.</p>
<p>A característica mais conhecida dos <i>Comentários</i> é que César fala de si mesmo na <b>terceira pessoa</b>. Ele nunca diz "eu fiz", e sim "César fez": o general aparece como um personagem entre outros, visto de fora, o que dá ao relato um ar de objetividade (e torna a autopromoção menos evidente). Veja o começo do capítulo 7 do livro I, quando César recebe a notícia de que os helvécios querem atravessar a província romana:</p>
{exemplos([('Caesarī cum id nūntiātum esset, eōs per prōvinciam nostram iter facere cōnārī, mātūrat ab urbe proficīscī.', 'Quando foi anunciado a César que eles tentavam fazer caminho pela nossa província, ele se apressa a partir da cidade. (Guerra da Gália I, 7, 1)')])}
<p>Três traços do estilo de César já estão nessa frase. O sujeito é César, chamado pelo nome (<i>Caesarī</i>, dativo: "a César"), e o verbo principal está na 3ª pessoa. O conteúdo da notícia vem numa <b>oração infinitiva</b> (capítulo 28): <i>eōs … iter facere cōnārī</i>, "que eles tentavam fazer caminho", com o sujeito <i>eōs</i> no acusativo e o verbo <i>cōnārī</i> no infinitivo. E o verbo principal <i>mātūrat</i> está no <b>presente histórico</b> (Bennett § 259.3), que dá rapidez à ação. A única marca de primeira pessoa é o plural <i>nostram</i>, "nossa": é a voz do romano que escreve para romanos, não a de César indivíduo. A mesma voz aparece logo na primeira frase do livro, em <i>nostrā (linguā)</i>, "na nossa língua".</p>
{observacao('Quando foi escrito', 'Não se sabe se César escreveu os sete livros de uma vez, no fim da guerra, ou um por ano, ao fim de cada campanha; os especialistas discutem a questão até hoje. Para o leitor, o importante é que o texto foi escrito pelo próprio protagonista, perto dos fatos e com o objetivo de apresentá-los ao público romano.')}
'''),
        ('O texto: Guerra da Gália I, 1', f'''
<p>O texto é o da edição de T. Rice Holmes (Oxford, 1914), conferido no Perseus, que a reproduz, e na The Latin Library, que traz as mesmas palavras. A numeração é a dos parágrafos modernos (§§ 1–7). A edição de Holmes (que morreu em 1933) está em domínio público. Holmes põe os §§ 5–7 entre colchetes: ele e outros editores suspeitaram que essa descrição das fronteiras tivesse sido acrescentada ao texto por outra mão. A questão é para especialistas; as edições escolares imprimem o capítulo inteiro, e este livro faz o mesmo. Os macrons são acréscimo deste livro.</p>
{tabela(['§', 'Texto latino (ed. Holmes, 1914)'], [[n, f'<span lang="la">{v}</span>'] for n, v in TEXTO], 'César, Guerra da Gália I, 1', latim_cols=(1,))}
<p>O capítulo tem duas partes. Os §§ 1–4 são <b>etnografia</b>: quem mora na Gália, como esses povos se distinguem e qual deles é o mais valente, e por quê. Os §§ 5–7 são <b>geografia</b>: os limites e a orientação de cada parte. Repare como o texto avança por <b>retomadas</b>: cada frase começa com uma palavra que se refere ao que acabou de ser dito (<i>Hī omnēs</i>, <i>Hōrum omnium</i>, <i>Quā dē causā</i>, <i>Eōrum</i>). Esse encadeamento é uma das razões da clareza de César, e Bennett o registra como regra da ordem latina (§ 350.9): palavras que se referem à frase anterior vêm em primeiro lugar.</p>
{dica('<b>Leia em blocos.</b> César escreve frases longas, mas feitas de blocos curtos e paralelos. Em <i>Hī omnēs linguā, īnstitūtīs, lēgibus inter sē differunt</i>, os três ablativos formam um bloco; em <i>initium capit …, continētur …, attingit …, vergit …</i> (§ 5), quatro verbos com o mesmo sujeito descrevem a mesma região. Antes de traduzir, marque os verbos e os blocos que dependem de cada um.')}
'''),
        ('Vocabulário e notas', f'''
{tabela(['No texto', 'Dicionário', 'Sentido aqui', 'Nota'], [
    ['Gallia', 'Gallia, -ae (f.)', 'a Gália', 'aqui, a Gália "livre", fora da província romana'],
    ['omnis', 'omnis, -e', 'considerada no todo', 'com sentido coletivo: "a Gália, no seu conjunto"'],
    ['est … dīvīsa', 'dīvidō, -ere, dīvīsī, dīvīsum', 'está dividida', 'particípio como predicativo: um estado, não um ato'],
    ['in partēs trēs', 'pars, partis (f.)', 'em três partes', '<i>in</i> + acusativo: o resultado da divisão'],
    ['quārum', 'quī, quae, quod', 'das quais', 'genitivo plural feminino; antecedente <i>partēs</i>'],
    ['incolunt', 'incolō, -ere, -coluī', 'habitam', 'transitivo: <i>ūnam (partem) incolunt</i>'],
    ['Belgae, Aquītānī', 'Belgae, -ārum; Aquītānī, -ōrum (m.)', 'os belgas, os aquitanos', 'sujeitos de <i>incolunt</i>'],
    ['ipsōrum linguā', 'ipse, -a, -um; lingua, -ae', 'na língua deles mesmos', 'ablativo de meio; <i>ipsōrum</i> contrasta com <i>nostrā</i>'],
    ['nostrā', 'noster, -tra, -trum', 'na nossa (língua)', 'subentende-se <i>linguā</i>: elipse'],
    ['appellantur', 'appellō, -āre, -āvī, -ātum', 'são chamados', 'presente passivo (capítulo 23)'],
    ['īnstitūtīs', 'īnstitūtum, -ī (n.)', 'costumes, instituições', 'ablativo de especificação, com <i>linguā</i> e <i>lēgibus</i>'],
    ['inter sē differunt', 'differō, differre (irregular)', 'diferem entre si', '<i>inter sē</i>: reciprocidade'],
    ['Garumna flūmen', 'Garumna, -ae (m.); flūmen, -inis (n.)', 'o rio Garona', '<i>flūmen</i> em aposto'],
    ['Matrona et Sēquana', 'Matrona, -ae (m.); Sēquana, -ae (f.; m. em Plínio)', 'o Marne e o Sena', 'dois sujeitos com verbo no singular (<i>dīvidit</i>); gêneros conforme o Lewis & Short'],
    ['fortissimī', 'fortis, -e (superlativo)', 'os mais valentes', 'superlativo relativo com genitivo partitivo (<i>hōrum omnium</i>)'],
    ['proptereā quod', 'conjunção causal', 'porque', 'causa dada pelo próprio autor: indicativo'],
    ['ā cultū atque hūmānitāte', 'cultus, -ūs (m.); hūmānitās, -ātis (f.)', 'da civilização e do refinamento', '<i>ā</i> + ablativo de separação com <i>absunt</i>'],
    ['prōvinciae', 'prōvincia, -ae (f.)', 'da Província', 'a província romana no sul da Gália (hoje, Provença)'],
    ['longissimē absunt', 'longē; absum, abesse, āfuī', 'estão muito longe', 'superlativo do advérbio'],
    ['minimē … saepe', 'advérbios', 'muito raramente', 'lê-se junto: "o menos frequentemente possível"'],
    ['mercātōrēs', 'mercātor, -ōris (m.)', 'mercadores', 'sujeito de <i>commeant</i> e de <i>important</i>'],
    ['commeant', 'commeō, -āre', 'vão e vêm', 'o vaivém do comércio'],
    ['ea quae … pertinent', 'is, ea, id; pertineō, -ēre', 'as coisas que servem para…', '<i>ea</i>: neutro plural, objeto de <i>important</i>'],
    ['ad effēminandōs animōs', 'effēminō, -āre; animus, -ī (m.)', 'para amolecer os ânimos', 'gerundivo com <i>ad</i>: finalidade (capítulo 31)'],
    ['important', 'importō, -āre', 'trazem, importam', 'presente'],
    ['proximī … Germānīs', 'proximus, -a, -um', 'os mais próximos dos germanos', 'dativo com adjetivo de proximidade'],
    ['trāns Rhēnum', 'Rhēnus, -ī (m.)', 'do outro lado do Reno', '<i>trāns</i> + acusativo'],
    ['quibuscum', 'quī + cum', 'com os quais', 'a preposição vem depois do relativo (Bennett § 142.4)'],
    ['continenter', 'advérbio', 'continuamente, sem parar', ''],
    ['bellum gerunt', 'gerō, -ere, gessī, gestum', 'fazem guerra', 'expressão fixa'],
    ['Quā dē causā', 'quī; causa', 'por essa razão', 'relativo de ligação: = <i>et eā dē causā</i>'],
    ['Helvētiī', 'Helvētiī, -ōrum (m.)', 'os helvécios', 'povo gaulês da atual Suíça'],
    ['reliquōs', 'reliquus, -a, -um', 'os demais', 'concorda com <i>Gallōs</i>'],
    ['virtūte praecēdunt', 'virtūs, -ūtis (f.); praecēdō, -ere', 'superam em valor', 'ablativo de especificação'],
    ['cotīdiānīs proeliīs', 'cotīdiānus, -a, -um; proelium, -ī (n.)', 'em combates diários', 'ablativo de meio ou de circunstância'],
    ['contendunt', 'contendō, -ere, -tendī, -tentum', 'lutam, combatem', ''],
    ['cum aut … aut …', 'conjunção', 'quando ou … ou …', '<i>cum</i> com indicativo: explica o "combater"'],
    ['suīs fīnibus eōs prohibent', 'fīnis, -is (m.), pl. território; prohibeō, -ēre', 'os mantêm longe do seu território', 'ablativo de separação; <i>suīs</i> = dos helvécios, <i>eōs</i> = os germanos'],
    ['in eōrum fīnibus', 'is', 'no território deles (dos germanos)', '<i>eōrum</i>, não reflexivo: outra pessoa'],
    ['Eōrum ūna pars', 'is; pars', 'uma parte deles', 'a parte dos gauleses propriamente ditos'],
    ['quam Gallōs obtinēre dictum est', 'obtineō, -ēre; dīcō', 'que, como foi dito, os gauleses ocupam', 'oração infinitiva com <i>dictum est</i>: seção 5'],
    ['initium capit', 'initium, -ī (n.); capiō', 'começa', 'literalmente "toma o seu início"'],
    ['ā flūmine Rhodanō', 'Rhodanus, -ī (m.)', 'no rio Ródano', '<i>ā</i>: ponto de partida'],
    ['continētur', 'contineō, -ēre', 'é limitada', 'passiva, com três ablativos de meio'],
    ['Ōceanō', 'Ōceanus, -ī (m.)', 'pelo Oceano', 'o Atlântico'],
    ['attingit', 'attingō, -ere', 'toca, alcança', ''],
    ['ab Sēquanīs et Helvētiīs', 'Sēquanī, -ōrum (m.)', 'do lado dos séquanos e helvécios', '<i>ab</i> = "do lado de", não agente'],
    ['vergit ad septentriōnēs', 'vergō, -ere; septentriōnēs, -um (m.)', 'volta-se para o norte', '<i>septentriōnēs</i>: as sete estrelas da Ursa Maior'],
    ['ab extrēmīs Galliae fīnibus oriuntur', 'extrēmus, -a, -um; orior, orīrī, ortus sum', 'começam nos confins extremos da Gália', 'os belgas pelo território deles; depoente'],
    ['pertinent ad', 'pertineō', 'estendem-se até', 'mesmo verbo do § 3, com outro sentido'],
    ['īnferiōrem partem', 'īnferior, -ius', 'a parte inferior (o curso baixo)', 'perto da foz do Reno'],
    ['spectant in', 'spectō, -āre', 'estão voltados para', ''],
    ['orientem sōlem', 'oriēns, -entis (particípio de orior); sōl, sōlis (m.)', 'o sol nascente, o leste', ''],
    ['Pȳrēnaeōs montēs', 'Pȳrēnaeus, -a, -um; mōns, montis (m.)', 'os montes Pireneus', ''],
    ['ad Hispāniam', 'Hispānia, -ae (f.)', 'junto à Hispânia', '<i>ad</i>: proximidade'],
    ['occāsum sōlis', 'occāsus, -ūs (m.)', 'o pôr do sol, o oeste', '<i>inter occāsum … et septentriōnēs</i>: o noroeste'],
], 'Vocabulário de Guerra da Gália I, 1', latim_cols=(0, 1))}
<h3>Notas aos parágrafos</h3>
<p><b>§ 1.</b> <i>Gallia est omnis dīvīsa</i>: <i>dīvīsa</i> pode ser lido como parte de um perfeito passivo ("foi dividida") ou, melhor aqui, como predicativo que descreve um estado ("está dividida"); César não fala de quem dividiu, mas de como a Gália se apresenta. <i>Omnis</i>, separado de <i>Gallia</i> e posto depois do verbo, significa "tomada no seu conjunto". Na última oração falta o antecedente do relativo: <i>tertiam (incolunt eī) quī … appellantur</i>, "a terceira, (habitam-na aqueles) que se chamam…". <b>§ 2.</b> <i>Dīvidit</i> está no singular com dois sujeitos (<i>Matrona et Sēquana</i>): o verbo concorda com o mais próximo, o que é comum quando os sujeitos formam uma ideia só, "a linha Marne-Sena".</p>
<p><b>§§ 3–4.</b> A explicação da valentia dos belgas tem três causas, todas no indicativo depois de <i>proptereā quod</i>, porque é o próprio autor quem as afirma (Bennett § 286.1): estão longe da civilização da Província; os mercadores quase não lhes levam artigos de luxo; e vivem em guerra com os germanos. <i>Minimē … saepe</i> se lê junto: "muito raramente". <i>Ad effēminandōs animōs</i> é um gerundivo com <i>ad</i>, que indica finalidade: "para amolecer os ânimos" (capítulo 31; Bennett § 339.2). <i>Quā dē causā</i> começa uma frase nova com um relativo que retoma a anterior ("e por essa causa"): é o <b>relativo de ligação</b>, e a preposição <i>dē</i> fica entre o relativo e o nome (Bennett § 350.7.b). <i>Cum aut … prohibent aut … gerunt</i>: <i>cum</i> com indicativo presente, "quando", explica em que consistem os combates diários (Allen e Greenough § 547).</p>
<p><b>§§ 5–7.</b> A descrição das fronteiras usa sempre os mesmos verbos de "começar", "estender-se", "tocar" e "estar voltado para". <i>Eōrum ūna pars</i> refere-se à parte dos gauleses propriamente ditos. <i>Continētur Garumnā flūmine, Ōceanō, fīnibus Belgārum</i>: a passiva com três ablativos de meio, "é contida, limitada por". Atenção a <i>ab Sēquanīs et Helvētiīs</i>: com nomes de lugar ou de povo, <i>ab</i> indica "do lado de", "na região de", e não o agente da passiva. Em <i>Belgae … oriuntur</i>, os belgas estão no lugar do território deles: é uma metonímia comum em César.</p>
'''),
        ('A Gália em tabela: povos, rios e montes', f'''
<p>O capítulo é, ao mesmo tempo, um mapa. Os romanos raramente desenhavam mapas para acompanhar um texto: a geografia era feita com palavras, a partir de pontos de referência (rios, montes, o mar) e de orientações pelo céu (<i>septentriōnēs</i>, as estrelas do norte; o sol nascente e o poente). Organize primeiro as informações sobre os povos:</p>
{tabela(['Nome latino (forma no texto)', 'Português', 'Onde, segundo César', 'Hoje, aproximadamente'], [
    ['<i>Belgae</i>', 'belgas', 'ao norte; dos confins da Gália até o curso inferior do Reno', 'norte da França, Bélgica'],
    ['<i>Aquītānī</i>; região <i>Aquītānia</i>', 'aquitanos; Aquitânia', 'ao sudoeste; do Garona aos Pireneus', 'sudoeste da França'],
    ['<i>Celtae</i> (na língua deles) = <i>Gallī</i> (na nossa)', 'celtas, gauleses', 'a parte central, entre o Garona, o Sena e o Marne, e o Ródano', 'centro da França'],
    ['<i>Germānī</i> (<i>Germānīs</i>)', 'germanos', 'do outro lado do Reno', 'Alemanha'],
    ['<i>Helvētiī</i>', 'helvécios', 'um povo gaulês junto ao Reno, em guerra com os germanos', 'Suíça'],
    ['<i>Sēquanī</i> (<i>ab Sēquanīs</i>)', 'séquanos', 'povo gaulês junto ao Reno, vizinho dos helvécios', 'Franco-Condado (leste da França)'],
    ['<i>prōvincia</i> (<i>prōvinciae</i>)', 'a Província', 'território já romano, ao sul (de onde vem a "civilização")', 'Provença e Languedoque'],
], 'Os povos de Guerra da Gália I, 1', latim_cols=())}
<p>Depois, os acidentes geográficos, que funcionam como as linhas do mapa:</p>
{tabela(['No texto', 'Nominativo', 'Português', 'Papel na descrição'], [
    ['<i>Garumna flūmen</i>; <i>Garumnā flūmine</i>', 'Garumna', 'rio Garona', 'separa os gauleses dos aquitanos; início da Aquitânia'],
    ['<i>Matrona</i>', 'Matrona', 'rio Marne', 'com o Sena, separa os gauleses dos belgas'],
    ['<i>Sēquana</i>', 'Sēquana', 'rio Sena', 'idem'],
    ['<i>Rhēnum</i>, <i>Rhēnī</i>', 'Rhēnus', 'rio Reno', 'fronteira com os germanos; os belgas chegam ao seu curso inferior'],
    ['<i>ā flūmine Rhodanō</i>', 'Rhodanus', 'rio Ródano', 'ponto de partida da parte dos gauleses'],
    ['<i>Ōceanō</i>, <i>Ōceanī</i>', 'Ōceanus', 'o Oceano (Atlântico)', 'limite a oeste'],
    ['<i>ad Pȳrēnaeōs montēs</i>', 'Pȳrēnaeī montēs', 'montes Pireneus', 'limite sul da Aquitânia'],
    ['<i>ad Hispāniam</i>', 'Hispānia', 'Hispânia (Península Ibérica)', 'a parte do Oceano junto a ela fecha a Aquitânia'],
], 'Rios, montes e mares', latim_cols=())}
<p>Agora junte tudo num quadro de três partes, como César as apresenta. Se quiser, desenhe um esboço: um retângulo com o Reno no alto à direita, o Oceano à esquerda, os Pireneus embaixo, o Ródano à direita e, cortando o retângulo, o Garona (embaixo) e o Sena com o Marne (em cima).</p>
{tabela(['Parte', 'Habitantes', 'Limites (§§ 2 e 5–7)', 'Voltada para'], [
    ['1. A Gália "céltica"', '<i>Celtae / Gallī</i>', 'começa no Ródano; limitada pelo Garona, pelo Oceano e pelas fronteiras dos belgas; toca o Reno do lado dos séquanos e helvécios', 'o norte (<i>ad septentriōnēs</i>)'],
    ['2. A Bélgica', '<i>Belgae</i>', 'começa nos confins da Gália (o Sena e o Marne); estende-se até o curso inferior do Reno', 'o norte e o leste (<i>in septentriōnem et orientem sōlem</i>)'],
    ['3. A Aquitânia', '<i>Aquītānī</i>', 'do Garona aos Pireneus e à parte do Oceano junto à Hispânia', 'entre o poente e o norte (o noroeste)'],
], 'A divisão da Gália segundo César', latim_cols=())}
{observacao('A Gália de César e a Gália romana', 'A "Gália" de César é a Gália ainda independente. Ao sul havia a <b>Província</b> (<i>prōvincia</i>), território romano desde o fim do século II a.C., que César trata como "nossa" (<i>prōvinciam nostram</i>, I, 7). A divisão em três partes é a visão de um romano em 58 a.C., não uma descrição neutra: ela prepara a narrativa de uma guerra que começa justamente com os helvécios, apresentados no § 4 como os mais valentes dos gauleses.')}
'''),
        ('Relativas, oração infinitiva e ablativo absoluto', f'''
<p>O primeiro capítulo de César é um bom exercício de <b>orações relativas</b> (capítulo 16), porque mostra quase todas as maneiras de usá-las. A regra é sempre a mesma: o relativo concorda com o antecedente em gênero e número, mas o seu caso vem da função na sua própria oração (Bennett § 250.1; Allen e Greenough § 305). O que varia é a posição do antecedente.</p>
{tabela(['Relativo', 'Caso e número', 'Antecedente', 'Função na relativa', 'Observação'], [
    ['<i>quārum</i> (§ 1)', 'gen. pl. fem.', '<i>partēs</i>', 'partitivo: "das quais uma…"', 'liga a frase à enumeração'],
    ['<i>quī</i> (§ 1)', 'nom. pl. masc.', 'omitido: (<i>eī</i>) "aqueles"', 'sujeito de <i>appellantur</i>', 'antecedente omitido (Bennett § 251.1)'],
    ['<i>quae</i> (§ 3)', 'nom. pl. neutro', '<i>ea</i>', 'sujeito de <i>pertinent</i>', '<i>ea quae</i>: "as coisas que"'],
    ['<i>quī</i> (§ 4)', 'nom. pl. masc.', '<i>Germānīs</i>', 'sujeito de <i>incolunt</i>', 'o antecedente está no dativo, o relativo no nominativo'],
    ['<i>quibuscum</i> (§ 4)', 'abl. pl. masc.', '<i>Germānīs</i>', 'com <i>cum</i>: companhia', '<i>cum</i> anexado ao relativo (Bennett § 142.4)'],
    ['<i>Quā</i> (dē causā) (§ 4)', 'abl. sing. fem.', 'a frase anterior inteira', 'adjetivo de <i>causā</i>', 'relativo de ligação: "por essa causa"'],
    ['<i>quam</i> (§ 5)', 'ac. sing. fem.', '<i>pars</i>', 'objeto do infinitivo <i>obtinēre</i>', 'dentro de uma oração infinitiva'],
    ['<i>quae</i> (§ 7)', 'nom. sing. fem.', '<i>partem</i>', 'sujeito de <i>est</i>', '"a parte do Oceano que fica junto à Hispânia"'],
], 'As orações relativas de I, 1')}
<p>O relativo do § 5 merece um comentário à parte, porque nele se cruzam as duas construções que são o pré-requisito deste capítulo. Em <i>quam Gallōs obtinēre dictum est</i>, o verbo principal da relativa é <i>dictum est</i>, "foi dito", um perfeito passivo usado impessoalmente. O que foi dito vem numa <b>oração infinitiva</b> (capítulo 28): <i>Gallōs obtinēre</i>, com o sujeito <i>Gallōs</i> no acusativo e o verbo <i>obtinēre</i> no infinitivo; e o objeto desse infinitivo é o próprio relativo <i>quam</i>. Literalmente: "a qual foi dito os gauleses ocuparem", isto é, "a qual, como foi dito, os gauleses ocupam". Não confunda os acusativos: <i>quam</i> é o objeto, <i>Gallōs</i> é o sujeito, e o que decide é o sentido (os gauleses ocupam a parte, não o contrário) e o fato de que <i>quam</i>, feminino singular, só pode retomar <i>pars</i>. A oração infinitiva funciona como sujeito de <i>dictum est</i>, o mesmo uso que Bennett descreve no § 330 para as expressões impessoais.</p>
{comparacao('A oração infinitiva em César', ['Latim', 'Sujeito do infinitivo (acusativo)', 'Verbo que a rege', 'Tradução'], [
    ['quam <b>Gallōs obtinēre</b> dictum est (I, 1, 5)', '<i>Gallōs</i>', '<i>dictum est</i>, impessoal', 'que, como foi dito, os gauleses ocupam'],
    ['cum id nūntiātum esset, <b>eōs</b> per prōvinciam nostram iter facere <b>cōnārī</b> (I, 7, 1)', '<i>eōs</i> (os helvécios)', '<i>nūntiātum esset</i>; <i>id</i> anuncia a oração', 'quando foi anunciado que eles tentavam passar pela nossa província'],
])}
<p>O <b>ablativo absoluto</b> (capítulo 30) não aparece no capítulo 1, mas aparece logo na segunda frase do capítulo 2, na forma mais típica dos historiadores romanos: a data dada pelos nomes dos cônsules do ano.</p>
{exemplos([('Apud Helvētiōs longē nōbilissimus fuit et dītissimus Orgetorix. Is M. Messālā, M. Pīsōne cōnsulibus rēgnī cupiditāte inductus coniūrātiōnem nōbilitātis fēcit.', 'Entre os helvécios, o mais nobre e o mais rico, de longe, foi Orgetórix. Este, no consulado de Marco Messala e Marco Pisão, levado pelo desejo do poder real, fez uma conspiração da nobreza. (Guerra da Gália I, 2, 1)')])}
<p><i>M. Messālā, M. Pīsōne cōnsulibus</i> é um ablativo absoluto sem particípio: dois nomes próprios e o nome <i>cōnsulibus</i>, todos no ablativo, literalmente "sendo cônsules Marco Messala e Marco Pisão" (Bennett § 227.1; Allen e Greenough § 419.a). Como o latim não tem particípio presente de <i>esse</i>, o "sendo" fica subentendido. Os romanos datavam os anos assim, pelos cônsules: esses dois foram cônsules em 61 a.C. (693 da cidade, pela conta do capítulo 43). Holmes imprime ainda as palavras <i>[et P.]</i> entre os dois nomes, marcadas como espúrias; este livro as omite. Note também o particípio conjunto <i>inductus</i>, "levado", concordando com <i>Is</i>, e o ablativo de causa <i>rēgnī cupiditāte</i>.</p>
{tabela(['Construção', 'Exemplo no texto', 'Regra', 'Referência'], [
    ['ablativo de especificação', '<i>linguā, īnstitūtīs, lēgibus … differunt</i>; <i>virtūte praecēdunt</i>', 'o ablativo diz "em que aspecto"', 'Bennett § 226 (com <i>Helvētiī … virtūte praestābant</i>)'],
    ['dativo com adjetivo', '<i>proximī … Germānīs</i>', 'adjetivos de proximidade pedem dativo', 'Bennett § 192.1 (com <i>sunt proximī Germānīs</i>)'],
    ['superlativo com genitivo', '<i>Hōrum omnium fortissimī</i>', '"os mais valentes de todos estes"', 'capítulo 18'],
    ['ablativo de separação', '<i>suīs fīnibus eōs prohibent</i>; <i>ā cultū … absunt</i>', 'verbos de afastar e de estar longe', 'Bennett § 214'],
    ['gerundivo com <i>ad</i>', '<i>ad effēminandōs animōs</i>', 'finalidade: "para amolecer os ânimos"', 'Bennett § 339.2; capítulo 31'],
], 'Outros usos do trecho')}
'''),
        ('Análise, diagrama e tradução', f'''
<p>A primeira frase de César é, provavelmente, a frase mais citada da prosa latina. Analise-a palavra a palavra:</p>
{analise('César, Guerra da Gália I, 1, 1', [
    ('Gallia', 'Gallia, -ae (f.), Gália', 'nominativo singular', 'sujeito de <i>est dīvīsa</i>'),
    ('est', 'sum, esse, fuī', 'presente do indicativo, 3ª sing.', 'verbo de ligação'),
    ('omnis', 'omnis, -e, todo', 'nominativo singular feminino', 'concorda com <i>Gallia</i>: "no seu conjunto"'),
    ('dīvīsa', 'dīvidō, -ere, dīvīsī, dīvīsum, dividir', 'particípio perfeito passivo, nom. sing. fem.', 'predicativo do sujeito: "dividida"'),
    ('in partēs trēs', 'pars, partis (f.); trēs, tria', '<i>in</i> + acusativo plural', 'resultado da divisão: "em três partes"'),
    ('quārum', 'quī, quae, quod (relativo)', 'genitivo plural feminino', 'partitivo, depende de <i>ūnam</i>; antecedente <i>partēs</i>'),
    ('ūnam', 'ūnus, -a, -um', 'acusativo singular feminino', 'objeto de <i>incolunt</i> (subentende-se <i>partem</i>)'),
    ('incolunt', 'incolō, -ere, incoluī, habitar', 'presente do indicativo, 3ª pl.', 'verbo da relativa, que vale também para os membros seguintes'),
    ('Belgae', 'Belgae, -ārum (m.), belgas', 'nominativo plural', 'sujeito de <i>incolunt</i>'),
    ('aliam', 'alius, -a, -ud, outro', 'acusativo singular feminino', 'objeto de <i>incolunt</i> subentendido'),
    ('Aquītānī', 'Aquītānī, -ōrum (m.)', 'nominativo plural', 'sujeito de <i>incolunt</i> subentendido'),
    ('tertiam', 'tertius, -a, -um, terceiro', 'acusativo singular feminino', 'objeto de <i>incolunt</i> subentendido'),
    ('quī', 'quī, quae, quod (relativo)', 'nominativo plural masculino', 'sujeito de <i>appellantur</i>; antecedente omitido (<i>eī</i>), sujeito de <i>incolunt</i>'),
    ('ipsōrum', 'ipse, ipsa, ipsum', 'genitivo plural masculino', 'determina <i>linguā</i>: "deles mesmos"'),
    ('linguā', 'lingua, -ae (f.), língua', 'ablativo singular', 'meio: "na língua"'),
    ('Celtae', 'Celtae, -ārum (m.)', 'nominativo plural', 'predicativo com <i>appellantur</i>'),
    ('nostrā', 'noster, nostra, nostrum', 'ablativo singular feminino', 'concorda com <i>linguā</i> subentendido'),
    ('Gallī', 'Gallī, -ōrum (m.)', 'nominativo plural', 'predicativo com <i>appellantur</i>'),
    ('appellantur', 'appellō, -āre, -āvī, -ātum, chamar', 'presente do indicativo passivo, 3ª pl.', 'verbo da relativa: "são chamados"'),
])}
<p>A frase tem uma oração principal curta e uma relativa longa, em que o verbo <i>incolunt</i> é dito uma vez e vale três vezes (elipse), e a terceira parte traz uma segunda relativa, com o antecedente omitido. Em diagrama:</p>
{diagrama_frase([('Gallia', 'sujeito · nom. sing. f.'), ('est omnis dīvīsa', 'predicado · estado'), ('in partēs trēs', 'resultado · in + acusativo'), ('quārum ūnam … aliam … tertiam', 'relativa · incolunt três vezes'), ('quī … appellantur', 'relativa · antecedente omitido')],
    'Esqueleto: <i>Gallia est omnis dīvīsa in partēs trēs</i>; depois, <i>quārum</i> distribui as três partes entre os três povos.')}
{tabela(['§', 'Tradução (Bibliotheca Latina)'], [
    ['1', 'A Gália, no seu conjunto, está dividida em três partes: uma delas é habitada pelos belgas, outra pelos aquitanos, e a terceira por aqueles que, na sua própria língua, se chamam celtas e, na nossa, gauleses.'],
    ['2', 'Todos esses povos diferem entre si na língua, nas instituições e nas leis. O rio Garona separa os gauleses dos aquitanos; o Marne e o Sena separam-nos dos belgas.'],
    ['3', 'De todos esses, os mais valentes são os belgas, porque estão muito longe da civilização e do refinamento da Província, porque os mercadores raramente vão até eles levar as coisas que servem para amolecer os ânimos,'],
    ['4', 'e porque são os vizinhos mais próximos dos germanos, que moram do outro lado do Reno e com os quais estão em guerra continuamente. Por essa razão também os helvécios superam em valor os demais gauleses: combatem com os germanos em batalhas quase diárias, quando os mantêm afastados do seu próprio território ou quando eles mesmos fazem guerra no território deles.'],
    ['5', 'A parte que, como foi dito, os gauleses ocupam começa no rio Ródano; é limitada pelo rio Garona, pelo Oceano e pelas fronteiras dos belgas; do lado dos séquanos e dos helvécios, toca também o rio Reno; está voltada para o norte.'],
    ['6', 'O território dos belgas começa nos confins extremos da Gália, estende-se até o curso inferior do rio Reno e está voltado para o norte e para o leste.'],
    ['7', 'A Aquitânia estende-se do rio Garona até os montes Pireneus e até a parte do Oceano que fica junto à Hispânia; está voltada para o noroeste, entre o poente e o norte.'],
], 'Tradução de Guerra da Gália I, 1')}
<p>Algumas escolhas. A passiva de <i>incolunt</i> ("é habitada pelos belgas") deixa as três partes como sujeito em português, o que mantém o foco de César nas partes; "os belgas habitam uma delas" também estaria certo. As três causas do §§ 3–4 foram marcadas com "porque" repetido, para que o leitor perceba que <i>proptereā quod</i> rege as três. <i>Eōrum ūna pars</i> virou simplesmente "a parte", porque "uma parte deles" soaria estranho depois de uma descrição de povos. E <i>Belgae … oriuntur</i> virou "o território dos belgas começa": o português não aceita bem a metonímia latina do povo pelo território.</p>
<h3>Resumo</h3>
<ul>
<li>César conta a sua própria guerra na terceira pessoa; a única primeira pessoa é o "nós" romano (<i>nostrā</i>, <i>prōvinciam nostram</i>).</li>
<li>I, 1: três partes (belgas, aquitanos, celtas ou gauleses), separadas pelo Garona e pela linha Marne-Sena; os belgas e os helvécios são os mais valentes por estarem longe da Província e perto dos germanos.</li>
<li>Relativas: o relativo concorda em gênero e número com o antecedente; o caso vem da sua oração; o antecedente pode faltar (<i>tertiam quī</i>) ou ser a frase anterior (<i>Quā dē causā</i>).</li>
<li>Oração infinitiva: <i>quam Gallōs obtinēre dictum est</i>, com <i>Gallōs</i> sujeito e <i>quam</i> objeto do infinitivo.</li>
<li>Ablativo absoluto de data: <i>M. Messālā, M. Pīsōne cōnsulibus</i>, "no consulado de Messala e Pisão" (61 a.C.).</li>
</ul>
<p>Com César termina o primeiro bloco da parte IV, dedicado à prosa narrativa. O capítulo 45 passa à poesia lírica, com Catulo e Horácio.</p>
'''),
    ],
    erros_comuns=[
        ('Traduzir <i>Gallia est omnis dīvīsa</i> como "Cada Gália é dividida" ou "A Gália toda foi dividida (por alguém)".', '<i>Omnis</i>, no singular e com um nome próprio, significa "no seu conjunto", não "cada". E <i>dīvīsa</i> descreve aqui um estado ("está dividida"), não uma ação com agente. A tradução tradicional "A Gália, no seu todo, está dividida em três partes" respeita as duas coisas.'),
        ('Procurar o antecedente de <i>quī</i> em <i>tertiam</i> ("a terceira, que se chamam…").', '<i>Quī</i> é masculino plural e <i>tertiam</i> é feminino singular: não podem concordar. O antecedente está omitido: "a terceira (habitam-na aqueles) que se chamam celtas" (Bennett § 251.1). Sempre que o relativo não concordar com nenhum nome à vista, pense num "aqueles" subentendido.'),
        ('Ler <i>Gallōs</i> como objeto e <i>quam</i> como sujeito em <i>quam Gallōs obtinēre dictum est</i>.', 'Na oração infinitiva, os dois acusativos (sujeito e objeto) têm a mesma forma de caso, e o sentido decide: os gauleses ocupam a parte. <i>Quam</i>, feminino singular, retoma <i>pars</i> e é objeto de <i>obtinēre</i>; <i>Gallōs</i> é o sujeito do infinitivo.'),
        ('Separar <i>minimē</i> de <i>saepe</i>: "de modo nenhum… muitas vezes".', 'Os dois advérbios formam uma unidade: <i>minimē saepe</i>, "o menos frequentemente possível", isto é, "muito raramente". César quer dizer que o comércio de luxo quase não chega aos belgas, não que nunca chegue.'),
        ('Tomar <i>Germānīs</i> por ablativo ("pelos germanos") e <i>ab Sēquanīs</i> por agente da passiva ("pelos séquanos").', '<i>Germānīs</i> depende de <i>proximī</i>, adjetivo de proximidade, e é dativo (Bennett § 192.1). <i>Ab Sēquanīs et Helvētiīs</i> não tem verbo passivo de que possa ser agente (<i>attingit</i> é ativo): com nomes de povos e lugares, <i>ab</i> significa "do lado de".'),
        ('Traduzir <i>ad effēminandōs animōs</i> como "aos ânimos que devem ser amolecidos".', 'O gerundivo com <i>ad</i> exprime finalidade: "para amolecer os ânimos" (Bennett § 339.2; capítulo 31). A ideia de obrigação do gerundivo não aparece nesse uso; traduza por "para" + infinitivo.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Por que os belgas são os mais valentes (§§ 3–4)',
            'Traduza: <i lang="la">Hōrum omnium fortissimī sunt Belgae, proptereā quod ā cultū atque hūmānitāte prōvinciae longissimē absunt, … proximīque sunt Germānīs, quī trāns Rhēnum incolunt, quibuscum continenter bellum gerunt.</i>', [
            ('Qual é a oração principal?', '<i>Hōrum omnium fortissimī sunt Belgae</i>: sujeito <i>Belgae</i>, verbo <i>sunt</i>, predicativo <i>fortissimī</i> (superlativo) com o genitivo partitivo <i>hōrum omnium</i>: "De todos estes, os mais valentes são os belgas".'),
            ('O que <i>proptereā quod</i> introduz, e por que o verbo está no indicativo?', 'A causa: "porque". O indicativo (<i>absunt</i>, e depois <i>sunt</i>, <i>commeant</i>, <i>important</i>) mostra que é o próprio César quem afirma a causa (Bennett § 286.1).'),
            ('Traduza <i>ā cultū atque hūmānitāte prōvinciae longissimē absunt</i>.', '<i>Absunt</i>, "estão longe", com <i>ā</i> + ablativo de separação; <i>prōvinciae</i>, genitivo, determina os dois nomes; <i>longissimē</i>, superlativo de <i>longē</i>: "estão muito longe da civilização e do refinamento da Província".'),
            ('Que caso é <i>Germānīs</i>, e de que depende?', 'Dativo plural, regido pelo adjetivo <i>proximī</i>: "os mais próximos dos germanos" (Bennett § 192.1, que cita esta mesma passagem). O <i>-que</i> de <i>proximīque</i> liga esta causa às anteriores.'),
            ('Quais são os antecedentes de <i>quī</i> e de <i>quibuscum</i>?', 'Os dois retomam <i>Germānīs</i>. <i>Quī</i> está no nominativo (sujeito de <i>incolunt</i>); <i>quibuscum</i> é o ablativo <i>quibus</i> com a preposição <i>cum</i> posposta (Bennett § 142.4), "com os quais". O sujeito de <i>gerunt</i> volta a ser os belgas.'),
            ('Monte a tradução.', '"De todos estes, os mais valentes são os belgas, porque estão muito longe da civilização e do refinamento da Província, … e porque são os vizinhos mais próximos dos germanos, que moram do outro lado do Reno, e com os quais fazem guerra continuamente."'),
        ]),
        pratica_guiada('Prática guiada 2 · A parte dos gauleses (§ 5)',
            'Traduza: <i lang="la">Eōrum ūna pars, quam Gallōs obtinēre dictum est, initium capit ā flūmine Rhodanō, continētur Garumnā flūmine, Ōceanō, fīnibus Belgārum.</i>', [
            ('Qual é o sujeito, e quantos verbos ele tem?', '<i>Eōrum ūna pars</i>, "uma parte deles". Tem dois verbos neste trecho: <i>initium capit</i> ("começa") e <i>continētur</i> ("é limitada"); no texto completo, mais dois (<i>attingit</i>, <i>vergit</i>).'),
            ('Analise a relativa <i>quam Gallōs obtinēre dictum est</i>.', 'Verbo da relativa: <i>dictum est</i>, impessoal, "foi dito". Dele depende a oração infinitiva <i>Gallōs obtinēre</i> (sujeito <i>Gallōs</i>, acusativo), cujo objeto é <i>quam</i> (= <i>pars</i>). "Que, como foi dito, os gauleses ocupam."'),
            ('O que indica <i>ā flūmine Rhodanō</i>?', 'O ponto de partida: <i>ā</i> + ablativo com <i>initium capit</i>, "começa no (a partir do) rio Ródano".'),
            ('E os três ablativos depois de <i>continētur</i>?', '<i>Garumnā flūmine</i>, <i>Ōceanō</i>, <i>fīnibus Belgārum</i> são ablativos de meio com o verbo passivo: "é limitada pelo rio Garona, pelo Oceano e pelas fronteiras dos belgas". Não levam <i>ā</i>, porque não são pessoas que agem, e sim limites.'),
            ('Monte a tradução.', '"A parte deles que, como foi dito, os gauleses ocupam começa no rio Ródano e é limitada pelo rio Garona, pelo Oceano e pelas fronteiras dos belgas."'),
        ], 'Conclusão: numa relativa com oração infinitiva, ache primeiro o verbo conjugado (<i>dictum est</i>), depois o infinitivo e o seu sujeito acusativo, e por último o papel do relativo dentro da oração infinitiva.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Compreensão', 'Responda em português, citando o texto latino.', [
            ('Em quantas partes César divide a Gália, e quem habita cada uma?', 'Em três: os belgas, os aquitanos e os celtas, chamados gauleses pelos romanos (<i>quārum ūnam incolunt Belgae, aliam Aquītānī, tertiam quī ipsōrum linguā Celtae, nostrā Gallī appellantur</i>).'),
            ('Em que os três povos diferem?', 'Na língua, nas instituições e nas leis: <i>linguā, īnstitūtīs, lēgibus inter sē differunt</i>.'),
            ('Quais são as três razões da valentia dos belgas?', 'Estão longe da civilização da Província; os mercadores raramente lhes levam artigos que amolecem os ânimos; e são vizinhos dos germanos, com quem vivem em guerra (§§ 3–4).'),
            ('Por que os helvécios superam os outros gauleses?', 'Porque combatem quase todo dia com os germanos, defendendo o próprio território ou atacando o deles: <i>quod ferē cotīdiānīs proeliīs cum Germānīs contendunt</i>.'),
            ('Onde fica a Aquitânia?', 'Entre o Garona, os Pireneus e a parte do Oceano junto à Hispânia; voltada para o noroeste (§ 7).'),
        ]),
        exercicio('Exercício 2 · O mapa', 'Responda com base no texto e nas tabelas da seção 4.', [
            ('Que rio separa os gauleses dos aquitanos?', 'O Garona: <i>Gallōs ab Aquītānīs Garumna flūmen … dīvidit</i>.'),
            ('Que rios separam os gauleses dos belgas?', 'O Marne e o Sena: <i>ā Belgīs Matrona et Sēquana dīvidit</i>.'),
            ('Que rio separa os gauleses (e os belgas) dos germanos?', 'O Reno: os germanos moram <i>trāns Rhēnum</i>, "do outro lado do Reno".'),
            ('Para que direção está voltada a Bélgica? Traduza a expressão latina.', '<i>In septentriōnem et orientem sōlem</i>: "para o norte e para o sol nascente", isto é, para o nordeste.'),
            ('O que significam <i>occāsus sōlis</i> e <i>septentriōnēs</i>?', '"O pôr do sol" (o oeste) e "as sete estrelas" da Ursa Maior (o norte). César orienta o mapa pelo céu.'),
        ]),
        exercicio('Exercício 3 · Os relativos', 'Para cada relativo, dê o caso, o antecedente e a função.', [
            ('<i>quārum</i> (§ 1)', 'Genitivo plural feminino; antecedente <i>partēs</i>; partitivo, depende de <i>ūnam</i>: "das quais uma".'),
            ('<i>quae</i> em <i>ea quae ad effēminandōs animōs pertinent</i> (§ 3)', 'Nominativo plural neutro; antecedente <i>ea</i>; sujeito de <i>pertinent</i>: "as coisas que servem para…".'),
            ('<i>quibuscum</i> (§ 4)', 'Ablativo plural masculino com <i>cum</i>; antecedente <i>Germānīs</i>; companhia: "com os quais".'),
            ('<i>Quā</i> em <i>Quā dē causā</i> (§ 4)', 'Ablativo singular feminino, concorda com <i>causā</i>; retoma a frase anterior inteira (relativo de ligação): "por essa causa".'),
            ('<i>quam</i> (§ 5)', 'Acusativo singular feminino; antecedente <i>pars</i>; objeto do infinitivo <i>obtinēre</i>.'),
            ('<i>quae</i> (§ 7)', 'Nominativo singular feminino; antecedente <i>partem</i>; sujeito de <i>est</i>: "a parte do Oceano que fica junto à Hispânia".'),
        ]),
        exercicio('Exercício 4 · Oração infinitiva e ablativo absoluto', 'Faça o que se pede em cada item.', [
            ('Passe para uma oração infinitiva depois de <i>Caesar scrībit</i> ("César escreve"): <i>Belgae fortissimī sunt.</i>', '<i>Caesar scrībit Belgās fortissimōs esse.</i> O sujeito vai ao acusativo (<i>Belgās</i>), o verbo ao infinitivo (<i>esse</i>) e o predicativo concorda com o sujeito acusativo (<i>fortissimōs</i>): "César escreve que os belgas são os mais valentes".'),
            ('Idem: <i>Helvētiī cum Germānīs contendunt.</i>', '<i>Caesar scrībit Helvētiōs cum Germānīs contendere.</i> "César escreve que os helvécios combatem com os germanos." Presente do infinitivo: ação simultânea.'),
            ('Traduza e diga o tipo de construção: <i>L. Pīsōne, A. Gabīniō cōnsulibus</i> (Guerra da Gália I, 6, citado por Allen e Greenough § 424.g).', 'Ablativo absoluto sem particípio: "no consulado de Lúcio Pisão e Aulo Gabínio" (58 a.C., o ano em que começa a guerra).'),
            ('Traduza: <i>Caesarī cum id nūntiātum esset, eōs per prōvinciam nostram iter facere cōnārī, mātūrat ab urbe proficīscī.</i> Explique <i>eōs … cōnārī</i>.', '"Quando foi anunciado a César que eles tentavam passar pela nossa província, ele se apressa a partir da cidade." <i>Eōs … cōnārī</i> é uma oração infinitiva (sujeito <i>eōs</i>, verbo <i>cōnārī</i>, infinitivo de depoente) que explica <i>id</i>, sujeito de <i>nūntiātum esset</i>.'),
        ]),
        exercicio('Exercício 5 · Usos dos casos', 'Diga o caso e a função.', [
            ('<i>linguā, īnstitūtīs, lēgibus</i> (§ 2)', 'Ablativos de especificação: "na língua, nas instituições, nas leis" (Bennett § 226).'),
            ('<i>virtūte</i> em <i>reliquōs Gallōs virtūte praecēdunt</i> (§ 4)', 'Ablativo de especificação: superam "em valor".'),
            ('<i>suīs fīnibus</i> em <i>suīs fīnibus eōs prohibent</i> (§ 4)', 'Ablativo de separação com <i>prohibeō</i>: "afastam-nos do seu território".'),
            ('<i>Garumnā flūmine</i> em <i>continētur Garumnā flūmine</i> (§ 5)', 'Ablativo de meio com verbo passivo: "é limitada pelo rio Garona".'),
            ('<i>ipsōrum linguā</i> (§ 1)', '<i>Linguā</i>: ablativo de meio, "na (pela) língua"; <i>ipsōrum</i>: genitivo, "deles mesmos".'),
        ]),
        exercicio('Exercício 6 · Traduza para o latim', 'Use o vocabulário do capítulo.', [
            ('Os belgas habitam uma parte da Gália.', '<i>Belgae ūnam partem Galliae incolunt.</i>'),
            ('O Reno separa os gauleses dos germanos.', '<i>Rhēnus Gallōs ā Germānīs dīvidit.</i> Mesma construção de <i>Gallōs ab Aquītānīs Garumna flūmen … dīvidit</i>.'),
            ('Os helvécios são os mais próximos dos germanos.', '<i>Helvētiī proximī sunt Germānīs.</i> <i>Proximus</i> pede dativo.'),
            ('Foi dito que os belgas são os mais valentes.', '<i>Dictum est Belgās fortissimōs esse.</i> Oração infinitiva como sujeito de <i>dictum est</i>, como no § 5.'),
        ]),
    ],
    leituras=['caesar-commentarii-de-bello-gallico-selecoes', 'caesar-commentarii-de-bello-gallico-texto-integral', 'collar-the-gate-to-caesar-de-bello-gallico-ii-simplificado-e-original', 'nepos-vita-hannibalis', 'greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc'],
    leituras_nota='Continue em César pelas seleções da DCC (no catálogo), que trazem o livro I com macrons, vocabulário e notas: leia I, 2–7, a conspiração de Orgetórix e a partida dos helvécios, onde aparecem muitos ablativos absolutos e orações infinitivas. <i>The Gate to Caesar</i>, de Collar, apresenta o livro II duas vezes, primeiro simplificado e depois no original, e é uma ótima ponte. O texto integral da edição de Holmes está no Perseus, com análise de cada palavra. A <i>Vida de Aníbal</i>, de Nepos, é outra prosa histórica clara, do mesmo período. Na gramática de Allen e Greenough, os §§ 597–598 comentam a ordem das palavras justamente na abertura da Guerra da Gália.',
)
