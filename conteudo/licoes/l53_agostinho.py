from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='53-agostinho', titulo='Agostinho: as Confissões',
    titulo_latim='Augustīnus', tempo='90 min',
    resumo='Leitura comentada de duas passagens das Confissões de Agostinho, no texto da edição de Migne: a abertura do livro I (Magnus es, Domine… inquietum est cor nostrum) e a cena do jardim de Milão no livro VIII (Tolle, lege). O estilo de Agostinho (perguntas retóricas, antíteses, repetições e um tecido de citações bíblicas, com os Salmos identificados), os subjuntivos das orações subordinadas e as marcas do latim cristão, com tradução própria.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['Agostinho de Hipona', 'Confissões', 'confessiō: louvor e confissão', 'edição de Migne (Patrologia Latina)', 'Confissões I,1,1', 'Confissões VIII,12,29', 'perguntas retóricas', 'antítese e quiasmo', 'anáfora e repetição', 'citações bíblicas e Salmos (numeração da Vulgata)', 'Vetus Latina', 'dōnec com subjuntivo', 'interrogativa indireta dupla (utrum… an)', 'subjuntivo exortativo na 1ª pessoa do singular', 'quia e quod = "que"', 'quod com subjuntivo depois de verbo de ouvir', 'tamquam com subjuntivo', 'subjuntivo por atração', 'ablativo absoluto na narração', 'presente histórico', 'proibição com nē + perfeito do subjuntivo', 'leitura comentada'],
    prerequisitos=dict(texto='Capítulo 34 (<i>cum</i> e a sequência dos tempos) e capítulo 51 (a leitura da Vulgata). Você vai usar também o subjuntivo e os seus usos independentes (capítulo 32), as orações finais (capítulo 33), a interrogativa indireta (capítulo 35), o ablativo absoluto (capítulo 30) e o que o capítulo 50 explica sobre o latim cristão.',
                       licoes=['30-o-ablativo-absoluto', '32-o-subjuntivo', '33-oracoes-finais-e-consecutivas', '34-cum-e-sequencia-dos-tempos', '35-a-interrogativa-indireta', '50-latim-cristao-e-medieval', '51-a-vulgata-marcos']),
    referencias=[
        referencia('Confessiones, livros I e VIII (ed. J.-P. Migne, Patrologia Latina, vol. 32, Paris, 1841)', 'Aurelius Augustinus', catalogo='hipponensis-confessiones', url='https://la.wikisource.org/wiki/Confessiones_(ed._Migne)/1', nota='texto-base das duas passagens: I, cap. 1, § 1 (página "Confessiones (ed. Migne)/1") e VIII, cap. 12, § 29 (página "Confessiones (ed. Migne)/8") da Wikisource latina, que transcreve a edição de Migne (1841) a partir do Corpus Corporum; as indicações bíblicas entre parênteses na edição (Psal. CXLIV, 3; Psal. CXLVI, 5; I Petr. V, 5; Rom. X, 14; Psal. XXI, 27; Matth. XIX, 21; Rom. XIII, 13–14) foram conferidas. Ortografia adaptada (i por j, ae por oe em caelum, lacrimārum, tamquam) e macrons acrescentados', tipo='dominio_publico'),
        referencia('Confessiones I e VIII (The Latin Library)', 'Aurelius Augustinus', url='https://www.thelatinlibrary.com/augustine/conf1.shtml', nota='usada só para comparar leituras com o texto de Migne (variantes registradas na seção 5 e no relatório de revisão interna); não é o texto-base', tipo='site'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Salmos 6,4; 21,27; 78,5.8; 144,3; 146,5; Romanos 10,14 e 13,13–14; 1 Pedro 5,5', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Liber_Psalmorum', nota='versículos conferidos na Wikisource latina (Liber Psalmorum; Pauli Epistola ad Romanos; Petri Epistola I) para identificar as citações de Agostinho e comparar a redação', tipo='dominio_publico'),
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 162.3 (perguntas retóricas), § 162.4 e 4.a (perguntas duplas; an introduzindo pergunta simples), § 274 (exortativo), § 276 (proibição com nē + presente ou perfeito do subjuntivo), § 277 (deliberativo), § 293 III.2 (dum, dōnec, quoad "até que" com subjuntivo de expectativa), § 299 (quod "o fato de que"), § 300.1 e 300.4 (interrogativa indireta; perguntas duplas indiretas), § 307 (tamquam e quasi com subjuntivo), § 323 (discurso indireto implícito), § 324 (subjuntivo por atração)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', url='https://dcc.dickinson.edu/grammar/latin/dum-d%C5%8Dnec-and-quoad', nota='§ 439 e nota 2 (exortativo; o termo às vezes restrito à 1ª pessoa do plural), § 444 (deliberativo), § 450 (proibição), § 454 (infinitivo como sujeito de verbo impessoal), § 524 (orações comparativas condicionais: tamquam, quasi), § 563.a (iubeō e vetō com oração infinitiva), § 553 e nota 1 (dum e quoad "até que" com subjuntivo; dōnec assim usado na poesia e no latim posterior), § 574 (interrogativa indireta), § 592–593 (discurso indireto informal; atração)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 358 (conjuntivo deliberativo), § 360 (exortativo, sobretudo na 1ª pessoa do plural), § 361 (jussivo)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 370 (subjuntivo dubitativo-interrogativo), n. 371 (subjuntivo exortativo; numeração do OCR conferida pelo índice), n. 442 (dum, quoad, donec com indicativo e com subjuntivo de intenção)', tipo='dominio_publico'),
    ],
    objetivos=[
        'Situar Agostinho e as <i>Confissões</i> e explicar o duplo sentido de <i>cōnfessiō</i> (louvor a Deus e confissão de si).',
        'Ler e traduzir, com apoio do vocabulário, a abertura do livro I e a cena do <i>Tolle, lege</i> do livro VIII.',
        'Identificar as citações bíblicas do texto, inclusive os Salmos, e converter a numeração da Vulgata para a das Bíblias modernas.',
        'Reconhecer os traços do estilo de Agostinho: perguntas retóricas, antíteses, repetições, quiasmo e paralelismo.',
        'Explicar cada subjuntivo das duas passagens (<i>dōnec requiēscat</i>, <i>utrum sit… an</i>, <i>invocem</i>, <i>tamquam dīcerētur</i>, <i>quod invēnissem</i>, <i>nē fēceritis</i>) e as construções próprias do latim cristão (<i>quia</i> e <i>quod</i> = "que").',
    ],
    secoes=[
        ('Agostinho e as Confissões', f'''
<p>Aurélio Agostinho nasceu em 354 em Tagaste, na Numídia (hoje Souk Ahras, na Argélia), estudou retórica em Madaura e em Cartago e ensinou essa arte em Cartago, em Roma e, a partir de 384, em Milão, onde ocupava a cátedra oficial de retórica da cidade. Ali, depois de anos de busca (o maniqueísmo, o ceticismo, os livros dos platônicos), converteu-se ao cristianismo em 386 e foi batizado pelo bispo Ambrósio na Páscoa de 387. Voltou à África, tornou-se padre e, depois, bispo de Hipona, onde morreu em 430, com os vândalos às portas da cidade. Escreveu uma obra imensa; as <i>Confissões</i> (<i>Cōnfessiōnēs</i>), redigidas nos primeiros anos do episcopado, por volta de 397–400, são a mais lida.</p>
<p>O título engana o leitor moderno. <i>Cōnfitērī</i>, no latim cristão, é "reconhecer diante de Deus", e tem dois objetos: os próprios pecados e a grandeza de Deus. A <i>cōnfessiō</i> é, ao mesmo tempo, confissão e louvor, e o livro inteiro é uma oração dirigida a Deus na segunda pessoa (<i>tū</i>), que o leitor ouve como quem escuta alguém rezar. Os livros I a IX contam a vida de Agostinho até a conversão e a morte da mãe, Mônica; os livros X a XIII tratam da memória, do tempo e da criação. Neste capítulo você lê duas páginas: a abertura do livro I, que anuncia o tema de toda a obra, e a cena do jardim de Milão, no livro VIII, que é o seu ponto de virada.</p>
{tabela(['', 'Abertura (I,1,1)', 'Jardim de Milão (VIII,12,29)'], [
    ['Tipo de texto', 'oração e meditação; quase sem narrativa', 'narrativa em primeira pessoa'],
    ['Tempos dominantes', 'presente e futuro do indicativo; subjuntivos de desejo e de pergunta', 'imperfeito e perfeito; presente histórico (<i>audiō</i>)'],
    ['Subjuntivos', '<i>dēlectet, requiēscat, sit, sciāris, quaeram, invocem</i>', '<i>solērent, aperīrem, legerem, invēnissem, admonitus fuerit, dīcerētur, fēceritis</i>'],
    ['Bíblia', 'Salmos, Romanos, 1 Pedro, costurados no texto', 'Mateus (a história de Antão) e Romanos (a página lida)'],
], 'As duas passagens do capítulo')}
<p>A <b>edição</b>. O texto deste capítulo é o da <i>Patrologia Latina</i> de J.-P. Migne (vol. 32, Paris, 1841), que reproduz a edição dos beneditinos de Saint-Maur e está em domínio público; ele foi conferido na transcrição da Wikisource latina. As edições críticas modernas diferem em alguns pontos de pormenor, e as diferenças que interessam à leitura estão indicadas nas notas. A ortografia foi ajustada às convenções deste livro (<i>i</i> por <i>j</i>, <i>caelum</i> e <i>lacrimae</i> em vez de <i>coelum</i> e <i>lacrymae</i>), e os macrons foram acrescentados, como em todo o livro, para ajudar a leitura; o autor, naturalmente, não os escrevia.</p>
{observacao('Por que ler Agostinho depois de Cícero e da Vulgata', 'Agostinho foi professor de retórica: escreve com a gramática e a arte do período que você aprendeu nos capítulos 32 a 39 e com os modelos de Cícero (capítulo 48), mas pensa e reza com as palavras da Bíblia latina (capítulos 50 e 51). Nas <i>Confissões</i> as duas tradições se fundem numa prosa nova, musical, cheia de perguntas, que influenciou toda a escrita cristã posterior em latim.')}
'''),
        ('Texto I: a abertura do livro I (Confissões I,1,1), com vocabulário', f'''
<p>Leia o texto em voz alta duas vezes antes de olhar a tradução. Na coluna da direita está uma tradução própria deste livro, deliberadamente próxima do latim, para que você possa conferir a construção; logo abaixo do texto estão o vocabulário e as notas.</p>
{exemplos([
    ('Magnus es, Domine, et laudābilis valdē: magna virtūs tua, et sapientiae tuae nōn est numerus.', 'Grande és, Senhor, e muito digno de louvor: grande é o teu poder, e a tua sabedoria não tem medida.'),
    ('Et laudāre tē vult homō, aliqua portiō creātūrae tuae;', 'E quer louvar-te o homem, uma pequena parte da tua criação;'),
    ('et homō circumferēns mortālitātem suam, circumferēns testimōnium peccātī suī, et testimōnium quia superbīs resistis:', 'o homem que carrega consigo a sua mortalidade, que carrega consigo o testemunho do seu pecado e o testemunho de que resistes aos soberbos:'),
    ('et tamen laudāre tē vult homō, aliqua portiō creātūrae tuae.', 'e, mesmo assim, quer louvar-te o homem, uma pequena parte da tua criação.'),
    ('Tū excitās, ut laudāre tē dēlectet; quia fēcistī nōs ad tē, et inquiētum est cor nostrum, dōnec requiēscat in tē.', 'Tu o despertas, para que louvar-te seja a sua alegria; porque nos fizeste para ti, e o nosso coração está inquieto até que descanse em ti.'),
    ('Dā mihi, Domine, scīre et intelligere utrum sit prius invocāre tē, an laudāre tē; et scīre tē prius sit, an invocāre tē.', 'Concede-me, Senhor, saber e compreender se vem primeiro invocar-te ou louvar-te, e se vem primeiro conhecer-te ou invocar-te.'),
    ('Sed quis tē invocat, nesciēns tē? Aliud enim prō aliō potest invocāre nesciēns tē.', 'Mas quem te invoca sem te conhecer? Pois quem não te conhece pode invocar uma coisa no lugar de outra.'),
    ('An potius invocāris, ut sciāris?', 'Ou será, antes, que és invocado para seres conhecido?'),
    ('Quōmodo autem invocābunt in quem nōn crēdidērunt? aut quōmodo crēdent sine praedicante?', 'Mas como invocarão aquele em quem não creram? Ou como crerão sem quem lhes pregue?'),
    ('Et laudābunt Dominum quī requīrunt eum.', 'E louvarão o Senhor os que o buscam.'),
    ('Quaerentēs enim inveniēnt eum, et invenientēs laudābunt eum.', 'Pois os que o buscam o encontrarão, e os que o encontram o louvarão.'),
    ('Quaeram tē, Domine, invocāns tē; et invocem tē, crēdēns in tē: praedicātus enim es nōbīs.', 'Que eu te busque, Senhor, invocando-te, e te invoque crendo em ti: pois foste anunciado a nós.'),
    ('Invocat tē, Domine, fidēs mea, quam dedistī mihi, quam īnspīrāstī mihi per hūmānitātem Fīliī tuī, per ministerium praedicātōris tuī.', 'Invoca-te, Senhor, a minha fé, que me deste, que me inspiraste pela humanidade do teu Filho, pelo ministério do teu pregador.'),
])}
<p>Repare na forma do parágrafo antes de entrar nos pormenores. Começa com uma <b>aclamação</b> (frases nominais, sem verbo na segunda: <i>magna virtūs tua</i>), passa a uma <b>afirmação</b> sobre o homem, repetida com <i>et tamen</i>, chega à frase central (<i>fēcistī nōs ad tē…</i>), e então se transforma numa <b>cadeia de perguntas</b>, cada uma nascida da anterior: louvar ou invocar? conhecer ou invocar? como invocar sem conhecer? A resposta vem da Bíblia (Romanos e Salmos) e o parágrafo termina numa oração confiante, com três verbos de primeira pessoa que pedem e um último verbo em que o sujeito já não é Agostinho, mas a sua fé.</p>
<h3>Vocabulário e notas</h3>
{tabela(['Palavra ou expressão', 'Dicionário', 'Nota'], [
    ['<i>laudābilis valdē</i>', '<i>laudābilis, -e</i>, louvável; <i>valdē</i>, muito', 'adjetivo da 3ª declinação (capítulo 10) com advérbio intensivo'],
    ['<i>magna virtūs tua</i>', '<i>virtūs, -ūtis</i> (f.)', 'aqui "poder, força", não "virtude"; frase nominal, com <i>est</i> subentendido'],
    ['<i>sapientiae tuae nōn est numerus</i>', '<i>numerus, -ī</i> (m.), número', 'dativo de posse (capítulo 20): "à tua sabedoria não há número", isto é, ela é incalculável'],
    ['<i>aliqua portiō creātūrae tuae</i>', '<i>portiō, -ōnis</i> (f.), porção; <i>creātūra, -ae</i> (f.), criação, criatura', 'aposto de <i>homō</i>; <i>aliqua</i> tem valor diminutivo: "uma parte qualquer, uma pequena parte"'],
    ['<i>circumferēns</i>', '<i>circumferō, -ferre, -tulī, -lātum</i>, levar à volta, carregar consigo', 'particípio presente (capítulo 29) concordando com <i>homō</i>'],
    ['<i>mortālitās, -ātis</i> (f.)', 'mortalidade, condição de mortal', 'o homem "anda com" a sua morte, como quem leva um peso'],
    ['<i>testimōnium quia…</i>', '<i>testimōnium, -ī</i> (n.), prova, testemunho', '<i>quia</i> aqui não é "porque", mas "que": introduz o conteúdo do testemunho (veja a seção 4)'],
    ['<i>superbīs resistis</i>', '<i>superbus, -a, -um</i>, soberbo; <i>resistō, -ere, restitī</i> + dativo, opor-se a', 'citação de 1 Pedro 5,5 (<i>Deus superbīs resistit</i>), passada para a 2ª pessoa'],
    ['<i>excitās</i>', '<i>excitō, -āre</i>, despertar, estimular', 'o objeto ("o homem") fica subentendido'],
    ['<i>dēlectet</i>', '<i>dēlectō, -āre</i>, deleitar, agradar', 'o sujeito é o infinitivo <i>laudāre tē</i>: "que louvar-te o deleite"'],
    ['<i>inquiētus, -a, -um</i>', 'inquieto, sem repouso', 'predicativo de <i>cor</i> (neutro: por isso <i>inquiētum</i>)'],
    ['<i>dōnec requiēscat</i>', '<i>requiēscō, -ere, -quiēvī</i>, descansar', '"até que descanse": subjuntivo de expectativa (seção 4)'],
    ['<i>intelligere</i>', 'variante gráfica de <i>intellegere</i>', 'a grafia com <i>i</i> é a da edição de Migne'],
    ['<i>utrum… an…</i>', '', 'pergunta dupla indireta: "se… ou…" (capítulo 35)'],
    ['<i>nesciēns tē</i>', '<i>nesciō, -īre</i>, não saber, não conhecer', 'particípio presente com valor condicional ou concessivo: "sem te conhecer"'],
    ['<i>aliud prō aliō</i>', '', '"uma coisa por outra": o pronome repetido em casos diferentes exprime troca'],
    ['<i>invocāris, sciāris</i>', '<i>invocō, -āre</i>; <i>sciō, -īre</i>', '2ª pessoa do singular passiva: presente do indicativo (<i>invocāris</i>) e presente do subjuntivo (<i>sciāris</i>, depois de <i>ut</i> final)'],
    ['<i>sine praedicante</i>', '<i>praedicō, -āre</i>, proclamar, pregar', 'particípio presente substantivado, ablativo depois de <i>sine</i>: "sem alguém que pregue"'],
    ['<i>quaerentēs, invenientēs</i>', '<i>quaerō, -ere</i>, buscar; <i>inveniō, -īre</i>, encontrar', 'particípios substantivados, sujeitos: "os que buscam", "os que encontram"'],
    ['<i>īnspīrāstī</i>', '<i>īnspīrō, -āre</i>, insuflar, inspirar', 'forma sincopada de <i>īnspīrāvistī</i> (capítulo 13)'],
    ['<i>praedicātor, -ōris</i> (m.)', 'pregador, anunciador', 'não identificado no texto: a leitura tradicional pensa em Ambrósio, bispo de Milão; outros comentadores, em Cristo ou em Paulo (J. J. O\'Donnell, comentário às <i>Confissões</i>, 1992, a I,1,1)'],
], 'Vocabulário do texto I', latim_cols=())}
<p>Três notas de leitura completam a tabela. Primeiro, <i>Magnus es</i> abre com o predicativo, e não com o sujeito: a primeira palavra das <i>Confissões</i> é um adjetivo de louvor, e o sujeito (<i>tū</i>) está só na desinência de <i>es</i>. Segundo, <i>homō</i> fica no fim da oração, depois do verbo (<i>laudāre tē vult homō</i>): a ordem põe em contraste a grandeza de Deus, no começo, e a pequenez do homem, no fim. Terceiro, <i>ad tē</i> em <i>fēcistī nōs ad tē</i> é ao mesmo tempo direção e finalidade: "na direção de ti" e "para ti". Traduzir só por "para ti" perde um pouco da imagem do movimento, que volta em <i>requiēscat in tē</i>: o coração sai de Deus, caminha para Deus e só repousa nele.</p>
'''),
        ('O estilo de Agostinho: perguntas, antíteses e a Bíblia', f'''
<p>Agostinho foi um mestre de retórica antes de ser bispo, e a sua prosa usa conscientemente as figuras que você estudou no capítulo 40. Mas ele as põe a serviço de uma oração, e o efeito é mais o de um salmo que o de um discurso no fórum. Quatro procedimentos aparecem já no primeiro parágrafo.</p>
<p><b>Perguntas retóricas e perguntas reais.</b> <i>Quis tē invocat, nesciēns tē?</i> é uma pergunta retórica (Bennett § 162.3): equivale a "ninguém te invoca sem te conhecer". Mas as perguntas de Agostinho também são perguntas de verdade, que ele não sabe responder e deixa abertas, e é isso que dá ao texto o seu tom de busca. Note o <i>an</i> sozinho em <i>An potius invocāris, ut sciāris?</i>: como em latim clássico (Bennett § 162.4.a), <i>an</i> introduz uma pergunta que corrige ou propõe uma alternativa à anterior, "ou será antes que…?".</p>
<p><b>Antítese e repetição.</b> O texto opõe grandeza e pequenez (<i>magnus</i>… <i>aliqua portiō</i>), a vontade do homem e o seu pecado (<i>laudāre tē vult</i>… <i>testimōnium peccātī suī</i>), a inquietação e o repouso (<i>inquiētum</i>… <i>requiēscat</i>, duas palavras da mesma família, <i>quiēs</i>). As repetições são deliberadas: <i>circumferēns… circumferēns</i>, <i>testimōnium… testimōnium</i>, <i>laudāre tē vult homō, aliqua portiō creātūrae tuae</i> dito duas vezes, idêntico, emoldurando o que está no meio. É a <b>anáfora</b> e a <b>epanalepse</b> da retórica antiga, mas o ouvido as reconhece também como o paralelismo dos Salmos.</p>
<p><b>Quiasmo.</b> <i>Quaerentēs… inveniēnt eum, et invenientēs laudābunt eum</i> encadeia os verbos (buscar → encontrar → encontrar → louvar), e a frase seguinte cruza a ordem: <i>Quaeram tē… invocāns tē; et invocem tē, crēdēns in tē</i>. No primeiro membro, o verbo pessoal (<i>quaeram</i>) vem antes do particípio (<i>invocāns</i>); no segundo, o particípio do primeiro membro volta como verbo pessoal (<i>invocem</i>). Uma ideia passa de um membro ao outro e avança um passo.</p>
<p><b>A Bíblia costurada no texto.</b> Agostinho quase não cita "entre aspas": ele fala com as palavras da Bíblia, adaptando-as à segunda pessoa e à frase. A edição de Migne indica as passagens à margem, e é fácil confrontá-las com a Vulgata (capítulo 51). Atenção à <b>numeração dos Salmos</b>: a Vulgata segue a numeração grega (a da Septuaginta), que, entre os Salmos 10 e 147, fica em geral um número atrás da numeração hebraica usada na maioria das Bíblias modernas.</p>
{tabela(['Agostinho', 'Fonte (numeração da Vulgata)', 'Texto da Vulgata Clementina', 'Bíblias modernas'], [
    ['<i>Magnus es, Domine, et laudābilis valdē</i>', 'Salmo 144,3', '<i>Magnus Dominus, et laudābilis nimis</i>', 'Salmo 145,3'],
    ['<i>magna virtūs tua, et sapientiae tuae nōn est numerus</i>', 'Salmo 146,5', '<i>Magnus Dominus noster, et magna virtūs eius, et sapientiae eius nōn est numerus</i>', 'Salmo 147,5'],
    ['<i>testimōnium quia superbīs resistis</i>', '1 Pedro 5,5', '<i>quia Deus superbīs resistit, humilibus autem dat grātiam</i>', '1 Pedro 5,5'],
    ['<i>Quōmodo autem invocābunt in quem nōn crēdidērunt? aut quōmodo crēdent sine praedicante?</i>', 'Romanos 10,14', '<i>Quōmodo ergō invocābunt, in quem nōn crēdidērunt? aut quōmodo crēdent eī, quem nōn audiērunt? quōmodo autem audient sine praedicante?</i>', 'Romanos 10,14'],
    ['<i>Et laudābunt Dominum quī requīrunt eum</i>', 'Salmo 21,27', '<i>et laudābunt Dominum quī requīrunt eum</i>', 'Salmo 22,27 (em algumas, 22,26)'],
], 'As citações bíblicas de Confissões I,1,1', latim_cols=())}
<p>A comparação ensina duas coisas. A primeira é o <b>método</b>: Agostinho transforma a terceira pessoa do Salmo (<i>Magnus Dominus</i>, "grande é o Senhor") em segunda (<i>Magnus es, Domine</i>, "grande és, Senhor"), e o que era hino vira diálogo; resume Romanos 10,14 saltando o elo do meio ("como crerão naquele que não ouviram?"). A segunda é <b>histórica</b>: a redação de Agostinho nem sempre coincide com a da Vulgata (<i>valdē</i> em vez de <i>nimis</i>; no livro VIII, <i>induite… prōvidentiam… in concupīscentiīs</i> em vez de <i>induiminī… cūram… in dēsīderiīs</i>). Ele cita, em geral, as traduções latinas anteriores à de Jerônimo, que se costumam chamar em conjunto <i>Vetus Latina</i> ("a antiga latina", capítulo 51), ou cita de memória. Por isso, quando você identificar uma citação, compare-a com a Vulgata, mas não espere identidade palavra por palavra.</p>
{dica('<b>Como achar um Salmo citado.</b> Se a edição dá o número romano (<i>Psal. CXLIV</i>), procure-o na Vulgata com esse número; para achar o mesmo Salmo numa Bíblia moderna, em geral some um (do Salmo 10 ao 145 da Vulgata, exceto 113–115, onde as divisões diferem; os Salmos 1–8 e 148–150 coincidem; o 9 da Vulgata corresponde aos 9–10 hebraicos, e os 146–147 da Vulgata formam juntos o 147 hebraico). Na dúvida, procure uma frase característica do versículo.')}
'''),
        ('A gramática do texto I: os subjuntivos e o "que" cristão', f'''
<p>O primeiro parágrafo das <i>Confissões</i> tem cinco subjuntivos, e cada um tem uma razão diferente. Reconhecê-los é a melhor revisão dos capítulos 32 a 35.</p>
{tabela(['Forma', 'Construção', 'Por quê', 'Tradução'], [
    ['<i>ut laudāre tē <b>dēlectet</b></i>', '<i>ut</i> + presente do subjuntivo depois de <i>excitās</i>', 'oração final (capítulo 33): o objetivo do estímulo; presente porque <i>excitās</i> é tempo primário (capítulo 34)', '"para que louvar-te o deleite"'],
    ['<i>dōnec <b>requiēscat</b></i>', '<i>dōnec</i> "até que" + subjuntivo', 'algo esperado, ainda não realizado (Bennett § 293 III.2; A&amp;G § 553 e nota 1)', '"até que descanse"'],
    ['<i>utrum <b>sit</b> prius… an…</i>', 'interrogativa indireta dupla', 'depende de <i>scīre et intelligere</i> (Bennett § 300.4; capítulo 35)', '"se vem primeiro… ou…"'],
    ['<i>ut <b>sciāris</b></i>', '<i>ut</i> final + presente do subjuntivo passivo', 'finalidade de <i>invocāris</i>', '"para seres conhecido"'],
    ['<i><b>quaeram</b> tē… et <b>invocem</b> tē</i>', 'subjuntivo independente, 1ª pessoa do singular', 'exortação dirigida a si mesmo: "que eu busque, que eu invoque" (A&amp;G § 439 e nota 2; Bennett § 274 só registra a 1ª do plural)', '"que eu te busque… e te invoque"'],
], 'Os subjuntivos de Confissões I,1,1')}
<p><b>Dōnec com subjuntivo.</b> <i>Dōnec</i> significa "enquanto" ou "até que". Com o <b>indicativo</b>, narra um fato real (<i>dōnec rediit, fuit silentium</i>, "houve silêncio até que ele voltou", Bennett § 293 III.1); com o <b>subjuntivo</b>, indica um termo esperado ou desejado, que ainda não aconteceu (§ 293 III.2). Allen e Greenough (§ 553, nota 1) observam que <i>dōnec</i> com esse subjuntivo é próprio da poesia e do latim posterior; a prosa clássica preferiria <i>dum</i>. Em <i>inquiētum est cor nostrum, dōnec requiēscat in tē</i>, o subjuntivo diz exatamente isto: o repouso é esperado, ainda não alcançado. Um indicativo (<i>dōnec requiēvit</i>) contaria um fato já ocorrido e mudaria o sentido da frase mais famosa do livro.</p>
<p><b>Quaeram: futuro ou subjuntivo?</b> Na 3ª conjugação, a 1ª pessoa do singular do futuro do indicativo é igual à do presente do subjuntivo (capítulo 32): <i>quaeram</i> pode ser "buscarei" ou "que eu busque". Aqui decide o paralelo: <i>invocem</i>, da 1ª conjugação, só pode ser subjuntivo (o futuro seria <i>invocābō</i>). As duas orações coordenadas por <i>et</i> têm, portanto, o mesmo valor: o desejo de quem se exorta a si mesmo. Agostinho fala consigo diante de Deus, e o subjuntivo de exortação na primeira pessoa do singular, que as gramáticas escolares quase não registram (Bennett § 274 restringe o exortativo à 1ª do plural), é natural nessa oração interior.</p>
<p><b>Quia = "que".</b> Em <i>testimōnium quia superbīs resistis</i>, <i>quia</i> não dá a causa de nada: introduz o conteúdo do testemunho, "o testemunho <b>de que</b> resistes aos soberbos". O latim clássico diria <i>testimōnium tē superbīs resistere</i>, com oração infinitiva (capítulo 28), ou usaria <i>quod</i> + indicativo, "o fato de que" (Bennett § 299). O latim cristão estende <i>quia</i> e <i>quod</i> a esse papel de "que" (capítulos 28 e 50), e o leitor precisa decidir em cada caso: no mesmo parágrafo, <i>quia fēcistī nōs ad tē</i> é causal, "porque nos fizeste para ti". O teste é simples: se a oração responde a "por quê?", é causal; se diz "o quê?" de um nome ou verbo (testemunho, saber, dizer, ouvir), é o "que" integrante.</p>
<p><b>O infinitivo como sujeito.</b> Em <i>ut laudāre tē dēlectet</i>, o sujeito de <i>dēlectet</i> é a ação de louvar, <i>laudāre tē</i>, e o objeto (o homem que se deleita) fica subentendido. É o mesmo infinitivo-sujeito de <i>Necesse est morī</i> (A&amp;G § 454). Do mesmo modo, em <i>utrum sit prius invocāre tē an laudāre tē</i>, os dois infinitivos são sujeitos de <i>sit</i>: "se é primeiro o invocar-te ou o louvar-te".</p>
<p>Leia agora palavra a palavra a frase central do parágrafo:</p>
{analise('Confissões I,1,1: Tū excitās, ut laudāre tē dēlectet; quia fēcistī nōs ad tē, et inquiētum est cor nostrum, dōnec requiēscat in tē.', [
    ('Tū', 'tū, tuī (pronome pessoal)', 'nominativo singular', 'sujeito de <i>excitās</i>, enfático (Deus, a quem o livro se dirige)'),
    ('excitās', 'excitō, -āre, despertar, estimular', '2ª pess. sing. do presente do indicativo ativo', 'verbo principal; objeto subentendido (o homem)'),
    ('ut', 'ut (conjunção)', 'com subjuntivo', 'introduz a oração final'),
    ('laudāre', 'laudō, -āre, louvar', 'infinitivo presente ativo', 'sujeito de <i>dēlectet</i>'),
    ('tē', 'tū, tuī', 'acusativo singular', 'objeto de <i>laudāre</i>'),
    ('dēlectet', 'dēlectō, -āre, deleitar', '3ª pess. sing. do presente do subjuntivo ativo', 'verbo da final; presente por sequência primária'),
    ('quia', 'quia (conjunção)', 'com indicativo', 'causal: "porque" (razão afirmada por quem fala)'),
    ('fēcistī', 'faciō, -ere, fēcī, factum, fazer', '2ª pess. sing. do perfeito do indicativo ativo', 'verbo da causal'),
    ('nōs', 'ego, nōs (pronome pessoal)', 'acusativo plural', 'objeto de <i>fēcistī</i>'),
    ('ad tē', 'ad (prep. com acusativo) + tū', 'acusativo singular', 'direção e finalidade: "para ti"'),
    ('et', 'et (conjunção)', 'invariável', 'coordena a segunda causal'),
    ('inquiētum', 'inquiētus, -a, -um, inquieto', 'nominativo singular neutro', 'predicativo de <i>cor</i>'),
    ('est', 'sum, esse, ser, estar', '3ª pess. sing. do presente do indicativo', 'verbo de ligação'),
    ('cor', 'cor, cordis (n.), coração', 'nominativo singular, 3ª declinação', 'sujeito de <i>est</i>'),
    ('nostrum', 'noster, -tra, -trum, nosso', 'nominativo singular neutro', 'concorda com <i>cor</i>'),
    ('dōnec', 'dōnec (conjunção)', 'com subjuntivo', '"até que", termo esperado'),
    ('requiēscat', 'requiēscō, -ere, -quiēvī, -quiētum, descansar', '3ª pess. sing. do presente do subjuntivo ativo', 'verbo da temporal; sujeito subentendido: <i>cor</i>'),
    ('in tē', 'in (prep. com ablativo) + tū', 'ablativo singular', 'lugar onde: "em ti"'),
])}
{diagrama_frase([('Tū excitās', 'oração principal · indicativo'), ('ut … dēlectet', 'final · subjuntivo'), ('quia fēcistī', 'causal · indicativo'), ('et inquiētum est', 'causal coordenada · indicativo'), ('dōnec requiēscat', 'temporal · subjuntivo de expectativa')],
    'O período central de Confissões I,1,1: uma principal curta, uma final, duas causais coordenadas e, presa à segunda, a temporal com <i>dōnec</i>.')}
<p>O diagrama mostra por que a frase se lê com tanta facilidade apesar de ter cinco verbos: as orações vêm uma depois da outra, cada uma ligada à anterior, sem encaixes. Esse estilo "em cadeia", de membros curtos e paralelos, é típico das passagens de oração das <i>Confissões</i>; nas passagens narrativas, como a do livro VIII, Agostinho volta ao período encaixado da prosa clássica.</p>
'''),
        ('Texto II: o jardim de Milão (Confissões VIII,12,29)', f'''
<p>Fim do verão de 386 (agosto ou setembro, conforme os estudiosos). Agostinho, em crise, está num jardim em Milão com o amigo Alípio. Pouco antes (VIII,6) ouvira contar a história de Antão, o monge do Egito que se convertera ao ouvir na igreja uma frase do Evangelho como se fosse dirigida a ele. Afastou-se de Alípio para chorar sozinho debaixo de uma figueira, rezando com palavras dos Salmos: <i>Et tū, Domine, usquequō?</i> ("E tu, Senhor, até quando?", Sl 6,4) e <i>Usquequō, Domine, īrāsceris in fīnem?</i> ("Até quando, Senhor, estarás irado para sempre?", Sl 78,5 (79,5)). É aqui que começa o parágrafo 29.</p>
{exemplos([
    ('Dīcēbam haec, et flēbam amārissimā contrītiōne cordis meī.', 'Eu dizia essas coisas e chorava na mais amarga contrição do meu coração.'),
    ('Et ecce audiō vōcem dē vīcīnā domō cum cantū dīcentis et crēbrō repetentis, quasi puerī an puellae, nesciō: Tolle, lege; tolle, lege.', 'E eis que ouço, vinda de uma casa vizinha, a voz de alguém, menino ou menina, não sei, que dizia cantando e repetia muitas vezes: "Toma e lê, toma e lê."'),
    ('Statimque mūtātō vultū, intentissimus cōgitāre coepī utrumnam solērent puerī in aliquō genere lūdendī cantitāre tāle aliquid;', 'Logo, com o rosto mudado, pus-me a pensar com toda a atenção se as crianças costumavam cantarolar algo assim em algum tipo de brincadeira;'),
    ('nec occurrēbat omnīnō audīvisse mē uspiam.', 'e não me vinha à lembrança de modo nenhum tê-lo ouvido em parte alguma.'),
    ('Repressōque impetū lacrimārum, surrēxī, nihil aliud interpretāns, nisi dīvīnitus mihi iubērī ut aperīrem cōdicem, et legerem quod prīmum caput invēnissem.', 'Contido o ímpeto das lágrimas, levantei-me, entendendo aquilo como nada menos que uma ordem de Deus para que eu abrisse o livro e lesse o primeiro capítulo que encontrasse.'),
    ('Audieram enim dē Antōniō quod ex ēvangelicā lēctiōne, cui forte supervēnerat, admonitus fuerit, tamquam sibi dīcerētur quod legēbātur:', 'Pois eu tinha ouvido dizer de Antão que, por uma leitura do Evangelho a que chegara por acaso, fora advertido, como se a ele se dissesse o que se lia:'),
    ('Vāde, vende omnia quae habēs, et dā pauperibus; et habēbis thēsaurum in caelīs; et venī, sequere mē;', '"Vai, vende tudo o que tens e dá-o aos pobres, e terás um tesouro nos céus; depois vem e segue-me";'),
    ('et tālī ōrāculō cōnfestim ad tē esse conversum.', 'e que por tal oráculo se convertera a ti imediatamente.'),
    ('Itaque concitus rediī ad eum locum ubi sedēbat Alypius: ibi enim posueram cōdicem Apostolī, cum inde surrēxeram.', 'Voltei, pois, apressado ao lugar onde Alípio estava sentado: ali eu deixara o livro do Apóstolo quando me levantara.'),
    ('Arripuī, aperuī, et lēgī in silentiō capitulum, quō prīmum coniectī sunt oculī meī:', 'Agarrei-o, abri-o e li em silêncio o trecho em que primeiro caíram os meus olhos:'),
    ('Nōn in cōmessātiōnibus et ēbrietātibus, nōn in cubīlibus et impudīcitiīs, nōn in contentiōne et aemulātiōne; sed induite Dominum Iēsum Chrīstum, et carnis prōvidentiam nē fēceritis in concupīscentiīs.', '"Não em comilanças e bebedeiras, não em leitos e devassidões, não em brigas e rivalidades; mas revesti-vos do Senhor Jesus Cristo e não cuideis da carne para os seus desejos."'),
    ('Nec ultrā voluī legere; nec opus erat.', 'Não quis ler mais adiante, nem era preciso.'),
    ('Statim quippe cum fīne huiusce sententiae quasi lūce sēcūritātis īnfūsā cordī meō, omnēs dubitātiōnis tenebrae diffūgērunt.', 'Pois logo, com o fim dessa frase, como se uma luz de segurança se derramasse no meu coração, todas as trevas da dúvida se dissiparam.'),
])}
{tabela(['Palavra ou expressão', 'Dicionário', 'Nota'], [
    ['<i>contrītiō, -ōnis</i> (f.)', 'trituração; no latim cristão, contrição', 'de <i>conterō</i>, "moer": o arrependimento como coração "esmagado"'],
    ['<i>cum cantū dīcentis et crēbrō repetentis</i>', '<i>cantus, -ūs</i> (m.), canto; <i>crēbrō</i>, frequentemente', 'genitivos de particípio substantivado, dependentes de <i>vōcem</i>: "a voz de alguém que dizia… e repetia"'],
    ['<i>quasi puerī an puellae, nesciō</i>', '', 'pergunta dupla abreviada, com o verbo <i>nesciō</i> intercalado: "de menino ou de menina, não sei"'],
    ['<i>tolle, lege</i>', '<i>tollō, -ere</i>, levantar, pegar; <i>legō, -ere</i>, ler', 'imperativos presentes (capítulo 22)'],
    ['<i>mūtātō vultū</i>', '<i>vultus, -ūs</i> (m.), rosto, expressão', 'ablativo absoluto (capítulo 30)'],
    ['<i>intentissimus</i>', 'superlativo de <i>intentus</i>, atento', 'predicativo do sujeito: "atentíssimo, com toda a atenção"'],
    ['<i>utrumnam solērent</i>', '<i>soleō, -ēre, solitus sum</i>, costumar', '<i>utrumnam</i> = <i>utrum</i> reforçado por <i>-nam</i>; interrogativa indireta, imperfeito por sequência secundária (<i>coepī</i>)'],
    ['<i>in aliquō genere lūdendī</i>', '<i>lūdō, -ere</i>, brincar', 'gerúndio no genitivo (capítulo 31): "em algum tipo de brincadeira"'],
    ['<i>cantitāre</i>', '<i>cantitō, -āre</i>, cantarolar, cantar repetidamente', 'verbo frequentativo de <i>cantō</i>'],
    ['<i>nec occurrēbat… audīvisse mē</i>', '<i>occurrō, -ere</i>, vir ao encontro, ocorrer', 'impessoal: o sujeito é a oração infinitiva <i>audīvisse mē</i> (A&amp;G § 454)'],
    ['<i>repressō impetū</i>', '<i>reprimō, -ere, repressī, repressum</i>, conter', 'ablativo absoluto coordenado por <i>-que</i> ao período anterior'],
    ['<i>nihil aliud interpretāns, nisi…</i>', '<i>interpretor, -ārī</i> (depoente), interpretar', '"interpretando não outra coisa senão que…": a oração seguinte é a interpretação'],
    ['<i>dīvīnitus mihi iubērī ut…</i>', '<i>dīvīnitus</i>, por vontade divina; <i>iubeō</i>', 'infinitivo passivo impessoal com <i>ut</i>: "que me era ordenado por Deus que…"'],
    ['<i>cōdex, -icis</i> (m.)', 'livro (em folhas, não em rolo)', '<i>cōdex Apostolī</i>: o volume com as cartas de Paulo'],
    ['<i>supervēnerat</i>', '<i>superveniō, -īre</i> + dativo, chegar a, sobrevir', '<i>cui</i>: dativo regido pelo verbo composto'],
    ['<i>concitus</i>', '<i>concieō</i> (<i>conciō</i>), agitar; part. <i>concitus</i>', 'particípio com valor de adjetivo predicativo: "agitado, às pressas"'],
    ['<i>arripuī</i>', '<i>arripiō, -ere, -ripuī</i>, agarrar', 'três perfeitos em assíndeto: <i>arripuī, aperuī, lēgī</i>'],
    ['<i>capitulum, -ī</i> (n.)', 'pequena seção, trecho', 'diminutivo de <i>caput</i>; não é ainda o "capítulo" numerado das Bíblias modernas'],
    ['<i>coniectī sunt</i>', '<i>coniciō, -ere, -iēcī, -iectum</i>, lançar', 'perfeito passivo (capítulo 24): "foram lançados", isto é, "caíram"'],
    ['<i>cōmessātiō, impudīcitia, aemulātiō</i>', 'banquete ruidoso; impudicícia; rivalidade, ciúme', 'ablativos plurais e singulares com <i>in</i>; a grafia <i>comessātiō</i> é a da Bíblia latina (no latim clássico, <i>cōmissātiō</i>)'],
    ['<i>induite</i>', '<i>induō, -ere, -uī, -ūtum</i>, vestir', 'imperativo plural: "revesti-vos de"'],
    ['<i>nē fēceritis</i>', 'faciō', 'proibição com <i>nē</i> + perfeito do subjuntivo (Bennett § 276; A&amp;G § 450)'],
    ['<i>huiusce</i>', '<i>hīc</i> + partícula enfática <i>-ce</i>', '"desta mesma"'],
    ['<i>diffūgērunt</i>', '<i>diffugiō, -ere, -fūgī</i>, dispersar-se fugindo', 'perfeito, 3ª pess. pl.; sujeito <i>tenebrae</i>'],
], 'Vocabulário do texto II', latim_cols=())}
<p>Uma variante merece registro. Onde a edição de Migne traz <i>nihil aliud interpretāns, nisi dīvīnitus mihi iubērī ut aperīrem</i>, as edições críticas modernas, como a que se lê na The Latin Library, trazem <i>nihil aliud interpretāns dīvīnitus mihi iubērī nisi ut aperīrem</i>. O sentido é o mesmo ("entendendo que Deus não me ordenava outra coisa senão que eu abrisse…"), mas a posição de <i>nisi</i> muda a construção. Há também <i>audīvisse</i> (Migne) por <i>audīsse</i> e <i>ad eum locum</i> por <i>in eum locum</i>. Este capítulo segue Migne.</p>
'''),
        ('A gramática do texto II: a narração e o discurso relatado', f'''
<p>O texto II é narrativo e usa outro repertório. O <b>imperfeito</b> descreve o pano de fundo (<i>dīcēbam, flēbam, occurrēbat, sedēbat</i>); o <b>perfeito</b> marca os acontecimentos (<i>coepī, surrēxī, rediī, arripuī, aperuī, lēgī, diffūgērunt</i>); e um <b>presente histórico</b> (<i>audiō</i>), depois de <i>et ecce</i>, faz o leitor ouvir a voz no instante em que Agostinho a ouviu. A sequência dos tempos (capítulo 34) funciona como no latim clássico: depois de <i>coepī</i>, <i>surrēxī</i> e <i>audieram</i>, todos tempos secundários, os subjuntivos estão no imperfeito ou no mais-que-perfeito, com uma exceção instrutiva (<i>admonitus fuerit</i>, abaixo).</p>
{tabela(['Construção', 'Exemplo do texto', 'Explicação'], [
    ['ablativo absoluto', '<i>mūtātō vultū</i>; <i>repressō impetū lacrimārum</i>; <i>lūce… īnfūsā</i>', 'circunstâncias da narração, com particípio perfeito passivo (capítulo 30); na última, <i>quasi</i> transforma a circunstância em comparação'],
    ['interrogativa indireta', '<i>utrumnam solērent puerī… cantitāre</i>', 'depende de <i>cōgitāre</i>; imperfeito por sequência secundária (capítulo 35)'],
    ['oração final completiva', '<i>iubērī ut aperīrem… et legerem</i>', 'na prosa clássica, <i>iubeō</i> pede a oração infinitiva (A&amp;G § 563.a; capítulo 28); aqui o infinitivo passivo impessoal <i>iubērī</i> recebe uma completiva com <i>ut</i>, como os verbos de pedir e exortar'],
    ['relativa no subjuntivo', '<i>quod prīmum caput invēnissem</i>', 'parte integrante da ordem: "o capítulo que eu encontrasse primeiro" (atração: Bennett § 324; A&amp;G § 593); mais-que-perfeito porque o encontrar precede o ler'],
    ['<i>quod</i> + subjuntivo depois de verbo de ouvir', '<i>audieram… quod… admonitus fuerit</i>', 'o latim cristão substitui a oração infinitiva por <i>quod</i>; o subjuntivo marca o fato como relatado por outros (A&amp;G § 592)'],
    ['oração infinitiva', '<i>et tālī ōrāculō cōnfestim ad tē esse conversum</i>', 'a mesma frase continua com a construção clássica: o sujeito <i>eum</i> (Antão) fica subentendido'],
    ['comparativa condicional', '<i>tamquam sibi dīcerētur</i>', '<i>tamquam</i> "como se" + subjuntivo, imperfeito por sequência (Bennett § 307; A&amp;G § 524)'],
    ['<i>cum</i> temporal com indicativo', '<i>cum inde surrēxeram</i>', 'puro tempo, mais-que-perfeito: "quando me levantara de lá" (capítulo 34)'],
    ['proibição', '<i>nē fēceritis</i>', '<i>nē</i> + perfeito do subjuntivo, sem diferença de sentido em relação ao presente (Bennett § 276)'],
], 'As construções do texto II')}
<p><b>Duas construções na mesma frase.</b> A frase sobre Antão é o melhor exemplo, nestas páginas, do latim de um autor que conhece as duas gramáticas. Começa com <i>audieram… quod… admonitus fuerit</i>, construção cristã com <i>quod</i> (como o "que" português: "tinha ouvido que ele fora advertido"), e termina com <i>et… ad tē esse conversum</i>, oração infinitiva clássica dependente do mesmo <i>audieram</i>. O subjuntivo <i>admonitus fuerit</i> é um <b>perfeito</b>, onde a regra estrita da sequência, depois de um mais-que-perfeito, pediria o mais-que-perfeito <i>admonitus esset</i>; no latim tardio essa liberdade com a sequência é frequente (capítulo 50), e você deve apenas reconhecê-la, sem imitá-la quando escrever em latim clássico (capítulo 41).</p>
{observacao('Por que Agostinho lia "em silêncio"?', 'O texto diz <i>lēgī in silentiō</i>. Na Antiguidade lia-se muitas vezes em voz alta, mesmo sozinho, e Agostinho registra noutro passo das <i>Confissões</i> (VI,3) a surpresa de ver Ambrósio ler em silêncio. Não tire daí conclusões apressadas sobre "a invenção da leitura silenciosa", tema discutido pelos estudiosos; para a leitura do latim, basta notar que <i>in silentiō</i> é ablativo de modo com <i>in</i>.')}
<p>Agora uma frase do texto II analisada palavra a palavra. É um período longo, mas inteiramente clássico na estrutura:</p>
{analise('Confissões VIII,12,29: Repressōque impetū lacrimārum, surrēxī, nihil aliud interpretāns, nisi dīvīnitus mihi iubērī ut aperīrem cōdicem, et legerem quod prīmum caput invēnissem.', [
    ('Repressō', 'reprimō, -ere, repressī, repressum, conter', 'particípio perfeito passivo, ablativo singular masculino', 'ablativo absoluto com <i>impetū</i>'),
    ('-que', '-que (enclítica)', 'invariável', 'liga este período ao anterior'),
    ('impetū', 'impetus, -ūs (m.), ímpeto, arrebatamento', 'ablativo singular, 4ª declinação', 'sujeito do ablativo absoluto'),
    ('lacrimārum', 'lacrima, -ae (f.), lágrima', 'genitivo plural', 'complemento de <i>impetū</i>'),
    ('surrēxī', 'surgō, -ere, surrēxī, surrēctum, levantar-se', '1ª pess. sing. do perfeito do indicativo', 'verbo principal'),
    ('nihil aliud', 'nihil (n., indeclinável); alius, -a, -ud', 'acusativo singular neutro', 'objeto de <i>interpretāns</i>: "nenhuma outra coisa"'),
    ('interpretāns', 'interpretor, -ārī, -ātus sum (depoente), interpretar', 'particípio presente, nominativo singular masculino', 'concorda com o sujeito de <i>surrēxī</i> (capítulo 25: o depoente tem particípio presente ativo)'),
    ('nisi', 'nisi (conjunção)', 'invariável', 'depois de <i>nihil aliud</i>: "senão"'),
    ('dīvīnitus', 'dīvīnitus (advérbio)', 'invariável', '"por vontade divina"'),
    ('mihi', 'ego, meī', 'dativo singular', 'a quem se ordena'),
    ('iubērī', 'iubeō, -ēre, iussī, iussum, ordenar', 'infinitivo presente passivo, impessoal', 'conteúdo da interpretação: "que me era ordenado"'),
    ('ut', 'ut (conjunção)', 'com subjuntivo', 'introduz o conteúdo da ordem'),
    ('aperīrem', 'aperiō, -īre, aperuī, apertum, abrir', '1ª pess. sing. do imperfeito do subjuntivo', 'imperfeito por sequência secundária (<i>surrēxī</i>)'),
    ('cōdicem', 'cōdex, -icis (m.), livro', 'acusativo singular, 3ª declinação', 'objeto de <i>aperīrem</i>'),
    ('et legerem', 'legō, -ere, lēgī, lēctum, ler', '1ª pess. sing. do imperfeito do subjuntivo', 'coordenado a <i>aperīrem</i>'),
    ('quod', 'quī, quae, quod (relativo)', 'acusativo singular neutro', 'relativo com o antecedente dentro da oração: "o capítulo que"'),
    ('prīmum', 'prīmum (advérbio)', 'invariável', '"primeiro, em primeiro lugar"'),
    ('caput', 'caput, capitis (n.), cabeça; capítulo', 'acusativo singular neutro', 'antecedente incorporado na relativa; objeto de <i>legerem</i> e de <i>invēnissem</i>'),
    ('invēnissem', 'inveniō, -īre, invēnī, inventum, encontrar', '1ª pess. sing. do mais-que-perfeito do subjuntivo', 'subjuntivo por atração (parte da ordem); anterior a <i>legerem</i>'),
])}
<p>Note a construção <i>quod prīmum caput invēnissem</i>, com o antecedente (<i>caput</i>) dentro da oração relativa; equivale a <i>caput quod prīmum invēnissem</i>. Note também a sequência: <i>aperīrem</i> e <i>legerem</i> (imperfeito: contemporâneos da ordem) e <i>invēnissem</i> (mais-que-perfeito: anterior ao ler). É a regra do capítulo 34 aplicada por um autor do século IV.</p>
<h3>Resumo</h3>
<ul>
<li><i>Cōnfessiō</i> é confissão e louvor; as <i>Confissões</i> são uma longa oração em segunda pessoa.</li>
<li>O estilo de Agostinho combina retórica clássica (perguntas, antíteses, repetições, quiasmo) e linguagem bíblica; as citações vêm adaptadas, muitas vezes de traduções anteriores à Vulgata.</li>
<li>Salmos: a Vulgata numera um a menos que a maioria das Bíblias modernas em geral entre os Salmos 10 e 145 da Vulgata (144 → 145; 21 → 22; 146,5 → 147,5).</li>
<li>Subjuntivos do texto I: final (<i>ut dēlectet, ut sciāris</i>), de expectativa (<i>dōnec requiēscat</i>), interrogativa indireta (<i>utrum sit… an</i>), exortação a si mesmo (<i>quaeram… invocem</i>).</li>
<li>Subjuntivos do texto II: interrogativa indireta (<i>solērent</i>), completiva com <i>ut</i> (<i>aperīrem, legerem</i>), atração (<i>invēnissem</i>), discurso relatado (<i>admonitus fuerit</i>), comparação (<i>tamquam dīcerētur</i>), proibição (<i>nē fēceritis</i>).</li>
<li><i>Quia</i> e <i>quod</i> podem ser "porque" ou "que": pergunte se a oração dá a causa ou o conteúdo.</li>
</ul>
<p>No próximo capítulo, o último do livro, você lê um texto de outro gênero e de outra época: um artigo da <i>Suma de Teologia</i> de Tomás de Aquino, que cita Agostinho a cada página e escreve um latim técnico, preciso e muito regular.</p>
'''),
    ],
    erros_comuns=[
        ('Traduzir todo <i>quia</i> por "porque": *"o testemunho porque resistes aos soberbos".', 'No latim cristão, <i>quia</i> (como <i>quod</i>) também introduz o conteúdo de um nome ou verbo: "o testemunho <b>de que</b> resistes". Pergunte se a oração responde a "por quê?" (causal) ou a "o quê?" (integrante). No mesmo parágrafo, <i>quia fēcistī nōs ad tē</i> é causal.'),
        ('Ler <i>dōnec requiēscat</i> como fato: *"até que descansou".', 'O subjuntivo com <i>dōnec</i> indica um termo esperado, ainda não alcançado (Bennett § 293 III.2). O presente do subjuntivo diz "até que descanse", e é esse adiamento que dá sentido à frase: o coração ainda está inquieto.'),
        ('Tomar <i>quaeram</i> por futuro e <i>invocem</i> por outra coisa, desfazendo o paralelo.', 'Na 3ª conjugação, <i>quaeram</i> pode ser futuro ou presente do subjuntivo; <i>invocem</i> (1ª conjugação) só pode ser subjuntivo. Orações coordenadas com o mesmo papel pedem a mesma leitura: "que eu te busque… e te invoque".'),
        ('Procurar o Salmo citado com o número da Vulgata numa Bíblia moderna e não encontrar o texto.', 'A Vulgata numera os Salmos pela tradição grega: o Salmo 144 da Vulgata é o 145 das Bíblias modernas, o 21 é o 22, o 146 (v. 5) é o 147. Em geral, some um (Salmos 10–145 da Vulgata) e confira pela frase.'),
        ('Considerar erro de Agostinho uma citação que difere da Vulgata (<i>valdē</i> por <i>nimis</i>; <i>induite</i> por <i>induiminī</i>).', 'Agostinho cita, em geral, traduções latinas anteriores à de Jerônimo (<i>Vetus Latina</i>) ou cita de memória. A diferença é um dado histórico, não um erro; ao comentar, cite as duas redações.'),
        ('Ler <i>quod prīmum caput invēnissem</i> como "porque eu encontrara o primeiro capítulo".', '<i>Quod</i> é aqui o relativo neutro concordando com <i>caput</i>, que está dentro da própria relativa: "o capítulo que eu encontrasse primeiro". O subjuntivo vem da atração (a relativa faz parte da ordem <i>ut… legerem</i>), e o mais-que-perfeito marca anterioridade ao ler.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Uma pergunta dupla de Agostinho',
            'Analise e traduza, passo a passo: <i lang="la">Dā mihi, Domine, scīre et intelligere utrum sit prius invocāre tē, an laudāre tē.</i>', [
            ('Qual é o verbo principal, e que forma tem?', '<i>Dā</i>, imperativo presente singular de <i>dō, dare</i>: "dá, concede". O sujeito é Deus, chamado no vocativo <i>Domine</i>; <i>mihi</i> é o dativo de quem recebe.'),
            ('O que Agostinho pede que lhe seja dado?', 'Dois infinitivos, <i>scīre et intelligere</i>, objetos de <i>dā</i>: "concede-me saber e compreender". Como no português "dá-me saber", o infinitivo funciona como objeto.'),
            ('O que ele quer saber? Como reconhecer a oração?', '<i>Utrum… an…</i> introduz uma pergunta dupla, dependente dos verbos de saber: é uma interrogativa indireta (capítulo 35), por isso o verbo está no subjuntivo, <i>sit</i>. A pergunta direta seria <i>Utrum est prius invocāre tē, an laudāre tē?</i>'),
            ('Qual é o sujeito de <i>sit</i>?', 'Os infinitivos <i>invocāre tē</i> e <i>laudāre tē</i>, um em cada membro: "se é primeiro o invocar-te ou o louvar-te". <i>Prius</i> é o comparativo neutro de <i>prior</i>, usado como predicativo ou advérbio: "anterior, primeiro".'),
            ('Por que o presente <i>sit</i>?', 'Porque <i>dā</i> é um imperativo, que conta como tempo primário: na sequência primária, a contemporaneidade se exprime pelo presente do subjuntivo (capítulo 34).'),
            ('Monte a tradução.', '"Concede-me, Senhor, saber e compreender se vem primeiro invocar-te ou louvar-te." Note que o "se" aqui é interrogativo, não condicional.'),
        ]),
        pratica_guiada('Prática guiada 2 · A notícia sobre Antão',
            'Separe as construções e traduza: <i lang="la">Audieram enim dē Antōniō quod ex ēvangelicā lēctiōne, cui forte supervēnerat, admonitus fuerit, tamquam sibi dīcerētur quod legēbātur.</i>', [
            ('Qual é o verbo principal?', '<i>Audieram</i>, mais-que-perfeito do indicativo: "eu tinha ouvido". <i>Dē Antōniō</i>: "a respeito de Antão".'),
            ('Que oração depende de <i>audieram</i>?', '<i>Quod… admonitus fuerit</i>: o conteúdo do que foi ouvido, introduzido por <i>quod</i> = "que", como no latim cristão. O subjuntivo indica que o fato é relatado por outros.'),
            ('E <i>cui forte supervēnerat</i>?', 'Relativa encaixada, com <i>cui</i> no dativo regido por <i>supervēnerat</i> (chegar a): "à qual chegara por acaso". O antecedente é <i>lēctiōne</i>. Fica no indicativo porque é um dado do narrador.'),
            ('Que valor tem <i>tamquam sibi dīcerētur</i>?', 'Comparativa condicional: "como se a ele se dissesse". <i>Tamquam</i> pede subjuntivo (Bennett § 307), e o imperfeito segue a sequência secundária. <i>Sibi</i> é reflexivo indireto, referido a Antão, sujeito da oração com <i>quod</i>.'),
            ('E o último <i>quod legēbātur</i>?', 'Outro <i>quod</i>, agora relativo sem antecedente expresso: "aquilo que se lia". É o sujeito de <i>dīcerētur</i>.'),
            ('Monte a tradução.', '"Pois eu tinha ouvido dizer de Antão que, por uma leitura do Evangelho a que chegara por acaso, fora advertido, como se a ele se dissesse o que se lia." Três <i>quod</i>/<i>cui</i> na mesma frase, cada um com uma função diferente.'),
        ], 'Conclusão: em Agostinho, a pergunta "que palavra é esta?" vale também para as conjunções; <i>quod</i> pode ser "que", "o qual" ou "aquilo que", e o modo do verbo ajuda a decidir.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Compreensão', 'Responda em português, com base nos dois textos.', [
            ('No texto I, por que o homem quer louvar a Deus, apesar de ser "uma pequena parte" da criação e de carregar o seu pecado?', 'Porque é o próprio Deus quem o desperta (<i>Tū excitās</i>) para que encontre alegria no louvor, e porque o homem foi feito "para Deus" (<i>fēcistī nōs ad tē</i>): o seu coração só descansa nele.'),
            ('Que dificuldade lógica Agostinho levanta sobre invocar e conhecer?', 'Para invocar alguém é preciso conhecê-lo (senão se invoca uma coisa por outra), mas talvez se invoque justamente para conhecer. A saída vem de Romanos 10,14: a fé nasce da pregação, e é a fé recebida que invoca.'),
            ('No texto II, o que Agostinho faz primeiro ao ouvir <i>Tolle, lege</i>?', 'Procura uma explicação natural: pergunta-se se as crianças costumavam cantar algo assim em alguma brincadeira (<i>utrumnam solērent puerī…</i>), e não se lembra de ter ouvido isso em parte alguma.'),
            ('Por que a história de Antão é decisiva para a interpretação da voz?', 'Porque Antão se convertera ao ouvir uma frase do Evangelho como se fosse dita a ele; Agostinho entende a voz da mesma maneira: deve abrir o livro e tomar como dirigida a si a primeira passagem que encontrar.'),
            ('O que acontece "com o fim da frase" lida?', 'Uma "luz de segurança" invade o coração e todas as trevas da dúvida se dissipam: Agostinho não precisa ler mais.'),
        ]),
        exercicio('Exercício 2 · Morfologia', 'Dê a forma de dicionário e analise cada palavra (tempo, modo, voz, pessoa ou caso).', [
            ('<i>invocāris</i>', '<i>invocō, -āre</i>: 2ª pess. sing. do presente do indicativo passivo, "és invocado". Não confunda com o futuro perfeito <i>invocāveris</i> nem com <i>invocēris</i>, presente do subjuntivo passivo.'),
            ('<i>sciāris</i>', '<i>sciō, scīre</i>: 2ª pess. sing. do presente do subjuntivo passivo ("sejas conhecido"), depois de <i>ut</i> final.'),
            ('<i>crēdidērunt</i>', '<i>crēdō, -ere, crēdidī, crēditum</i>: 3ª pess. pl. do perfeito do indicativo ativo, "creram".'),
            ('<i>īnspīrāstī</i>', '<i>īnspīrō, -āre</i>: 2ª pess. sing. do perfeito do indicativo, forma sincopada de <i>īnspīrāvistī</i>.'),
            ('<i>solērent</i>', '<i>soleō, -ēre, solitus sum</i> (semidepoente): 3ª pess. pl. do imperfeito do subjuntivo, "costumassem".'),
            ('<i>admonitus fuerit</i>', '<i>admoneō, -ēre, -uī, -itum</i>: 3ª pess. sing. do perfeito do subjuntivo passivo, "tenha sido advertido".'),
            ('<i>coniectī sunt</i>', '<i>coniciō, -ere, -iēcī, -iectum</i>: 3ª pess. pl. do perfeito do indicativo passivo, masculino (concorda com <i>oculī</i>).'),
            ('<i>fēceritis</i>', '<i>faciō, -ere, fēcī, factum</i>: 2ª pess. pl. do perfeito do subjuntivo ativo; com <i>nē</i>, proibição.'),
        ]),
        exercicio('Exercício 3 · Sintaxe: por que o subjuntivo?', 'Explique o modo e o tempo de cada verbo destacado.', [
            ('<i>inquiētum est cor nostrum, dōnec <b>requiēscat</b> in tē</i>', 'Subjuntivo com <i>dōnec</i> "até que" para um termo esperado (Bennett § 293 III.2); presente porque o verbo principal (<i>est</i>) é presente.'),
            ('<i>cōgitāre coepī utrumnam <b>solērent</b> puerī… cantitāre</i>', 'Interrogativa indireta dependente de <i>cōgitāre</i>; imperfeito porque o verbo principal (<i>coepī</i>) é um perfeito histórico, tempo secundário.'),
            ('<i>tamquam sibi <b>dīcerētur</b> quod legēbātur</i>', 'Comparativa condicional com <i>tamquam</i> (Bennett § 307; A&amp;G § 524); imperfeito por sequência secundária. <i>Legēbātur</i> fica no indicativo: é um fato.'),
            ('<i>ut aperīrem cōdicem, et legerem quod prīmum caput <b>invēnissem</b></i>', 'Relativa no subjuntivo por atração, porque faz parte da ordem expressa no subjuntivo (Bennett § 324; A&amp;G § 593); mais-que-perfeito porque o encontrar é anterior ao ler, em sequência secundária.'),
            ('<i>Quaeram tē… et <b>invocem</b> tē</i>', 'Subjuntivo independente de exortação na 1ª pessoa do singular: "que eu te invoque" (A&amp;G § 439). <i>Invocem</i>, da 1ª conjugação, não pode ser futuro.'),
            ('<i>ibi enim posueram cōdicem Apostolī, cum inde <b>surrēxeram</b></i>', 'Indicativo, porque <i>cum</i> aqui é puramente temporal, "quando" (capítulo 34); mais-que-perfeito por ser anterior à ação narrada.'),
        ]),
        exercicio('Exercício 4 · Estilo e Bíblia', 'Identifique a figura ou a fonte e comente brevemente.', [
            ('<i>Et laudāre tē vult homō, aliqua portiō creātūrae tuae… et tamen laudāre tē vult homō, aliqua portiō creātūrae tuae.</i>', 'Repetição em moldura (a mesma frase no início e no fim do período, epanalepse): o que está no meio (mortalidade, pecado) é "cercado" pela vontade de louvar, que permanece apesar de tudo.'),
            ('<i>inquiētum… requiēscat</i>', 'Antítese entre palavras da mesma família (<i>quiēs</i>, repouso): a inquietação e o repouso, os dois polos do livro.'),
            ('<i>Magnus es, Domine, et laudābilis valdē</i>', 'Salmo 144,3 na numeração da Vulgata (145,3 nas Bíblias modernas), passado da 3ª pessoa (<i>Magnus Dominus</i>) para a 2ª; <i>valdē</i> em vez do <i>nimis</i> da Vulgata.'),
            ('<i>Et laudābunt Dominum quī requīrunt eum</i>', 'Salmo 21,27 da Vulgata (22 nas Bíblias modernas): citação literal, que Agostinho desenvolve no quiasmo seguinte (buscar, encontrar, louvar).'),
            ('<i>Nōn in cōmessātiōnibus et ēbrietātibus, nōn in cubīlibus et impudīcitiīs…</i>', 'Romanos 13,13–14. Anáfora de <i>nōn in</i> e pares de substantivos. A Vulgata traz <i>induiminī… cūram… in dēsīderiīs</i>; Agostinho, <i>induite… prōvidentiam… in concupīscentiīs</i>, sinal de uma tradução latina anterior.'),
        ]),
        exercicio('Exercício 5 · Tradução', 'Traduza para o português, explicando as construções principais.', [
            ('<i>Sed quis tē invocat, nesciēns tē? Aliud enim prō aliō potest invocāre nesciēns tē.</i>', '"Mas quem te invoca sem te conhecer? Pois quem não te conhece pode invocar uma coisa no lugar de outra." Pergunta retórica (= ninguém); <i>nesciēns</i> é particípio presente com valor de condição ("se não te conhece"), e na segunda frase funciona como sujeito ("quem não conhece").'),
            ('<i>Quaerentēs enim inveniēnt eum, et invenientēs laudābunt eum.</i>', '"Pois os que o buscam o encontrarão, e os que o encontram o louvarão." Particípios presentes substantivados como sujeitos; futuros do indicativo (<i>inveniēnt</i>, <i>laudābunt</i>).'),
            ('<i>Et ecce audiō vōcem dē vīcīnā domō cum cantū dīcentis et crēbrō repetentis.</i>', '"E eis que ouço, vinda de uma casa vizinha, a voz de alguém que dizia cantando e repetia muitas vezes." Presente histórico (<i>audiō</i>); <i>dīcentis</i> e <i>repetentis</i>, genitivos de particípio substantivado.'),
            ('<i>Nec ultrā voluī legere; nec opus erat.</i>', '"Não quis ler mais adiante, nem era preciso." <i>Opus est</i> = "é necessário"; aqui sem complemento.'),
            ('<i>Statim quippe cum fīne huiusce sententiae quasi lūce sēcūritātis īnfūsā cordī meō, omnēs dubitātiōnis tenebrae diffūgērunt.</i>', '"Pois logo, com o fim dessa frase, como se uma luz de segurança se derramasse no meu coração, todas as trevas da dúvida se dissiparam." <i>Cum fīne</i>: preposição + ablativo; <i>lūce… īnfūsā</i>, ablativo absoluto introduzido por <i>quasi</i>; <i>cordī meō</i>, dativo com o composto <i>īnfundō</i>.'),
        ]),
    ],
    leituras=['hipponensis-confessiones', 'hipponensis-epistulae-cartas-selecionadas', 'hipponensis-de-civitate-dei', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'kempis-de-imitatione-christi', 'short-a-latin-dictionary-lewis-short'],
    leituras_nota='Continue nas <i>Confissões</i>: o resto do livro I (a infância e a escola, com a famosa passagem sobre o estudo do grego e do latim, I,13–14), o livro VIII inteiro (a crise e a conversão) e, quando estiver mais seguro, o livro XI (sobre o tempo). Leia sempre com a Vulgata ao lado, para identificar as citações. As cartas de Agostinho (seleção do catálogo) mostram a sua prosa no dia a dia de bispo, e A Cidade de Deus, em trechos, o seu latim argumentativo. A <i>Imitação de Cristo</i> é um bom contraste: frases curtas, muito mais simples, numa espiritualidade herdeira de Agostinho. Para o vocabulário cristão (<i>contrītiō, cōnfessiō, praedicātor</i>), o dicionário de Lewis e Short registra os sentidos tardios.',
)
