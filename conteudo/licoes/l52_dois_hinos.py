from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='52-dois-hinos', titulo='Dois hinos: Pange lingua e Dies irae',
    titulo_latim='Hymnī', tempo='80 min',
    resumo='Leitura comentada de dois hinos medievais: o Pange lingua de Tomás de Aquino, inteiro, e as dez primeiras estrofes do Dies irae atribuído a Tomás de Celano. Como a poesia latina passou da quantidade ao acento e à rima, o ritmo trocaico dos dois hinos, contagem de sílabas sem elisão, o contexto litúrgico, vocabulário e notas, e os subjuntivos de que os hinos vivem (exortativo, jussivo, optativo, proibição), com traduções próprias.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['hinos latinos', 'Pange lingua (Tomás de Aquino)', 'Tantum ergo', 'Dies irae (Tomás de Celano, atribuído)', 'Venâncio Fortunato',
             'verso quantitativo e verso rítmico', 'acento e número de sílabas', 'rima', 'tetrâmetro trocaico catalético', 'dímetro trocaico',
             'ausência de elisão', 'subjuntivo exortativo', 'subjuntivo jussivo', 'subjuntivo optativo', 'proibição com nē + presente',
             'relativa final com unde', 'cum causal e concessivo', 'perifrástica ativa', 'liturgia: Corpus Christi e missa de defuntos', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 32 (o subjuntivo e os seus usos independentes: os hinos são feitos de exortações, ordens e desejos) e capítulo 50 (o latim cristão e medieval, a ortografia e a pronúncia eclesiástica, que é a usada no canto destes hinos). A noção de pé e de verso quantitativo vem do capítulo 40; se você ainda não o estudou, a seção 1 dá o necessário.',
                       licoes=['32-o-subjuntivo', '50-latim-cristao-e-medieval']),
    referencias=[
        referencia('Pange lingua gloriosi corporis mysterium', 'Tomás de Aquino', catalogo='aquino-pange-lingua-gloriosi-corporis-mysterium', url='https://la.wikisource.org/wiki/Pange_lingua', nota='texto integral (seis estrofes e Amen) conferido na Wikisource latina; ortografia da página conservada (coenae), com macrons acrescentados', tipo='dominio_publico'),
        referencia('Dies irae, no texto de Charles C. Nott, The Seven Great Hymns of the Mediaeval Church (Nova York, 1902)', 'Tomás de Celano (atribuído)', catalogo='celano-dies-irae', url='https://la.wikisource.org/wiki/The_seven_great_hymns_of_the_mediaeval_church/Dies_Ir%C3%A6/Tommaso', nota='estrofes I–X lidas no capítulo e XI–XVIII usadas nos exercícios, conferidas na transcrição da Wikisource latina (páginas 86–94 do volume); adaptado: ae por æ, i por j, cum por quum, Sibyllā por Sybillâ, sem os acentos circunflexos da edição; macrons acrescentados', tipo='dominio_publico'),
        referencia('Pange lingua gloriosi proelium certaminis', 'Venâncio Fortunato', url='https://la.wikisource.org/wiki/Pange_lingua_gloriosi_proelium_certaminis', nota='primeiros versos do hino do século VI que serviu de modelo ao de Tomás, conferidos na Wikisource latina', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Sofonias 1,15; João 4,6', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina', nota='fonte do primeiro verso do Dies irae e do "sentaste-te cansado" da estrofe X, conferidos na Wikisource latina', tipo='dominio_publico'),
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 115 (perifrástica ativa: particípio futuro + sum); § 274 (subjuntivo exortativo, 1ª pl.); § 275 (jussivo); § 276 (proibição com nē + presente ou perfeito do subjuntivo; 276.a, pouco frequente na prosa clássica); § 279 (optativo); § 282.1–2 (orações finais com nē; relativas finais com quī, ubi, unde, quō: unde = ut inde); § 286.2 (cum causal com subjuntivo); § 309.3 (cum "embora" com subjuntivo); § 366.1–11 (mora, pé, troqueu, ictus, elisão, verso catalético, dímetro e tetrâmetro)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 439 e nota 3 (subjuntivo exortativo; negação nōn ocasional nos poetas e nos autores tardios); §§ 441–442 (optativo; utinam); § 549 (cum causal ou concessivo com subjuntivo)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 475 (metro: nos versos jâmbicos e trocaicos dois pés formam "um metro"; dímetro, trímetro, tetrâmetro; verso acatalético e catalético)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='início do capítulo de métrica (a poesia antiga é quantitativa, a moderna se baseia no acento; o verso latino não tem rima; no OCR o número aparece como "552", e a sequência indica 532); n. 541 (metros clássicos usados pela Igreja na hinologia; e: trocaicos octonários catalécticos, com o exemplo "Pange lingua gloriosi — lauream certaminis"; nota final sobre a passagem da poesia quantitativa às assonâncias, às rimas e à acentuação)', tipo='dominio_publico'),
    ],
    objetivos=[
        'Explicar a diferença entre o verso quantitativo clássico e o verso rítmico medieval (número de sílabas, acento, rima, ausência de elisão).',
        'Contar as sílabas e marcar os acentos de uma estrofe do <i>Pange lingua</i> e do <i>Dies irae</i>, reconhecendo o movimento trocaico.',
        'Ler e traduzir o <i>Pange lingua</i> inteiro e as dez primeiras estrofes do <i>Dies irae</i>, com o apoio das notas.',
        'Identificar e classificar os subjuntivos dos hinos (exortativo, jussivo, optativo, proibição, final, causal), comparando-os com a norma clássica do capítulo 32.',
        'Situar os dois hinos na liturgia e na história da poesia latina.',
    ],
    secoes=[
        ('Da quantidade ao acento', f'''
<p>A poesia latina clássica é <b>quantitativa</b>: o verso é uma sequência regular de sílabas longas e breves, agrupadas em pés. A unidade é a sílaba breve, a <i>mora</i>; uma longa vale duas. O <b>troqueu</b> é o pé de uma longa e uma breve (– ∪), o jambo é o inverso, e o verso se nomeia pelo pé que domina e pelo número de pares de pés: um verso trocaico de quatro pares é um <b>tetrâmetro</b>, de dois, um <b>dímetro</b>; se o último pé está incompleto, o verso é <b>catalético</b> (Bennett § 366.1–11; Kennedy § 475). Na leitura, uma vogal final se elide diante de outra vogal: <i>tantum ergō</i> soa <i>tant(um) ergō</i> (Bennett § 366.7). O capítulo 40 trata disso com vagar. O Pe. Ravizza resume a diferença que importa aqui: a poesia dos gregos e dos romanos "chama-se quantitativa, a dos povos modernos baseia-se na acentuação"; o verso latino clássico "não tem rima, nem se compõe de um número determinado de sílabas" (início do capítulo de métrica).</p>
<p>Entre os séculos IV e IX, à medida que a distinção entre vogais longas e breves desaparecia da língua falada, os poetas cristãos passaram a compor para ouvidos que já não a sentiam. Muitos hinos antigos ainda são quantitativos (Ravizza lista os metros clássicos que a Igreja conservou nos seus hinos, n. 541), mas pouco a pouco o verso passou a se apoiar em três outras coisas, as mesmas da poesia portuguesa: o <b>número de sílabas</b>, a posição dos <b>acentos</b> das palavras e a <b>rima</b>. Ravizza fecha o seu quadro dos metros litúrgicos com esta observação: da poesia de tipo clássico "paulatinamente passou-se à poesia com assonâncias e rimas", e daí à acentuação, "que deu origem à poesia moderna baseada no número das sílabas e na sucessão dos acentos" (n. 541).</p>
{comparacao('Verso quantitativo e verso rítmico', ['Traço', 'Verso clássico (quantitativo)', 'Verso medieval (rítmico)'], [
    ['Base do ritmo', 'alternância de sílabas longas e breves', 'alternância de sílabas acentuadas e átonas'],
    ['Medida', 'pés (moras); o número de sílabas varia', 'número fixo de sílabas por verso'],
    ['Acento da palavra', 'pode coincidir ou não com o tempo forte', 'coincide com o tempo forte (com exceções)'],
    ['Elisão', 'regular: vogal final diante de vogal desaparece', 'em geral ausente: todas as sílabas contam'],
    ['Rima', 'ausente (ou ocasional, como ornamento)', 'essencial, muitas vezes dupla ou tripla'],
])}
<p>Os dois hinos deste capítulo são rítmicos e <b>trocaicos</b>: os acentos caem nas sílabas ímpares (1ª, 3ª, 5ª, 7ª), como num troqueu acentual (forte-fraco). Leia em voz alta o primeiro verso do <i>Dies irae</i> batendo o acento: <i><b>Dí</b>-ēs <b>ī</b>-rae, <b>dí</b>-ēs <b>íl</b>-la</i>. Quatro tempos fortes, oito sílabas. Agora repare na quantidade: o <i>i</i> de <i>diēs</i> é <b>breve</b>, e a sílaba seguinte, <i>ēs</i>, é longa. Num verso clássico, <i>diēs</i> (∪ –) seria um jambo, o contrário de um troqueu; aqui ele abre o verso com acento na primeira sílaba, porque o ouvido medieval segue o acento da palavra, não a duração da vogal.</p>
{dica('<b>Como ler um hino rítmico</b>: (1) leia na pronúncia eclesiástica do capítulo 1, que é a do canto; (2) conte as sílabas sem elidir nada (<i>tantum ergō</i> são quatro sílabas, não três); (3) marque o acento de cada palavra pela regra da penúltima (capítulo 1) e confira se os acentos caem nas sílabas ímpares; (4) procure as rimas no fim dos versos.')}
'''),
        ('Pange lingua: o texto', f'''
<p>O <i>Pange lingua glōriōsī corporis mystērium</i> é atribuído a Tomás de Aquino (c. 1225–1274), o teólogo dominicano que você lê no capítulo 54. Segundo a tradição, foi escrito para o ofício da festa de <i>Corpus Christi</i>, instituída para toda a Igreja pelo papa Urbano IV em 1264 (bula <i>Transiturus</i>), e canta a Eucaristia. As duas últimas estrofes, a partir de <i>Tantum ergō</i>, ganharam vida própria: são cantadas na bênção do Santíssimo Sacramento, e o hino inteiro acompanha a procissão de Quinta-feira Santa. O primeiro verso é uma homenagem: repete o início de outro hino, sobre a cruz, composto no século VI por Venâncio Fortunato, <i>Pange, lingua, glōriōsī proelium certāminis</i>, "Canta, ó língua, o combate da gloriosa luta". Tomás troca a cruz pelo corpo, e a batalha pelo mistério. (<i>Proelium</i> é a leitura dos manuscritos, seguida pela Wikisource; o Breviário Romano trazia <i>lauream certāminis</i>, "o laurel da luta", e é essa a forma que Ravizza cita no n. 541. A Catholic Encyclopedia de 1911, s.v. <i>Pange Lingua Gloriosi</i>, registra as duas.)</p>
{exemplos([
    ('Pange, lingua, glōriōsī<br>corporis mystērium,<br>sanguinisque pretiōsī,<br>quem in mundī pretium<br>frūctus ventris generōsī<br>rēx effūdit gentium.', '1. Canta, ó língua, o mistério do corpo glorioso e do sangue precioso que, como resgate do mundo, derramou o Rei das nações, fruto de um ventre nobre.'),
    ('Nōbīs datus, nōbīs nātus<br>ex intāctā Virgine,<br>et in mundō conversātus,<br>sparsō verbī sēmine,<br>suī morās incolātūs<br>mīrō clausit ōrdine.', '2. Dado a nós, nascido para nós de uma Virgem intacta, e tendo vivido no mundo, depois de espalhar a semente da palavra, ele encerrou de modo admirável o tempo da sua morada entre nós.'),
    ('In suprēmae nocte coenae<br>recumbēns cum frātribus,<br>observātā lēge plēnē<br>cibīs in lēgālibus,<br>cibum turbae duodēnae<br>sē dat suīs manibus.', '3. Na noite da última ceia, reclinado à mesa com os irmãos, cumprida plenamente a lei nos alimentos prescritos, ele se dá como alimento, com as próprias mãos, ao grupo dos Doze.'),
    ('Verbum carō pānem vērum<br>verbō carnem efficit,<br>fitque sanguis Chrīstī merum;<br>et sī sēnsus dēficit,<br>ad firmandum cor sincērum<br>sōla fidēs sufficit.', '4. O Verbo feito carne, com uma palavra, faz do pão verdadeiro a sua carne, e o vinho se torna o sangue de Cristo; e, se os sentidos falham, para firmar um coração sincero basta só a fé.'),
    ('Tantum ergō sacrāmentum<br>venerēmur cernuī,<br>et antīquum documentum<br>novō cēdat rītuī;<br>praestet fidēs supplēmentum<br>sēnsuum dēfectuī.', '5. Veneremos, pois, prostrados, tão grande sacramento, e ceda o antigo ensinamento ao novo rito; que a fé supra o que falta aos sentidos.'),
    ('Genitōrī Genitōque<br>laus et iūbilātiō,<br>salūs, honor, virtūs quoque<br>sit et benedictiō;<br>prōcēdentī ab utrōque<br>compar sit laudātiō.<br>Āmēn.', '6. Ao Pai e ao Filho, louvor e júbilo, salvação, honra e também poder e bênção; ao que procede de ambos, igual louvor. Amém.'),
])}
<p>Fonte: Wikisource latina (<i>Pange lingua</i>), com macrons acrescentados e a grafia <i>coenae</i> conservada (é <i>cēnae</i>, "da ceia": um caso do <i>oe</i> por <i>e</i> do capítulo 50). A tradução é deste livro e segue o latim de perto; ela não procura conservar a métrica nem as rimas.</p>
'''),
        ('Lendo o Pange lingua', f'''
<h3>O ritmo e as rimas</h3>
<p>Cada estrofe tem seis versos que alternam <b>oito</b> e <b>sete</b> sílabas. O verso de oito termina em palavra paroxítona (<i>glō-ri-<b>ō</b>-sī</i>); o de sete, em proparoxítona (<i><b>cor</b>-po-ris mys-<b>tē</b>-ri-um</i>). Juntando dois versos, temos uma linha de quinze sílabas, que é a versão acentual do tetrâmetro trocaico catalético: quatro pares de troqueus, o último incompleto. É o mesmo molde do hino de Venâncio, que Ravizza classifica entre os "trocaicos octonários catalécticos" e que se pode dividir em duas metades, "o primeiro perfeito, o segundo cataléctico" (n. 541). As rimas alternam: os versos ímpares rimam entre si (<i>glōriōsī, pretiōsī, generōsī</i>) e os pares também (<i>mystērium, pretium, gentium</i>). Nenhuma sílaba se elide: <i>quem in mundī pretium</i> tem sete sílabas contando <i>quem</i> e <i>in</i> separadamente, e <i>Tantum ergō sacrāmentum</i>, oito, com <i>-tum</i> e <i>er-</i> inteiros. Num verso clássico, <i>quem in</i> e <i>tantum ergō</i> perderiam uma sílaba na elisão.</p>
<h3>Notas</h3>
{tabela(['Estrofe', 'Expressão', 'Nota'], [
    ['1', '<i>pange</i>', 'imperativo de <i>pangō, -ere</i>, compor, cantar (um poema). <i>Lingua</i> é vocativo.'],
    ['1', '<i>sanguinisque pretiōsī, quem…</i>', 'genitivo coordenado a <i>corporis</i>. O relativo <i>quem</i> (masculino) retoma <i>sanguinis</i>: "o sangue que…".'],
    ['1', '<i>in mundī pretium</i>', '<i>in</i> + acusativo de finalidade: "como preço (resgate) do mundo".'],
    ['1', '<i>frūctus ventris generōsī rēx… gentium</i>', 'sujeito de <i>effūdit</i>: <i>rēx gentium</i>, "o Rei das nações", com o aposto <i>frūctus ventris generōsī</i>, "fruto de um ventre nobre".'],
    ['2', '<i>Nōbīs datus, nōbīs nātus</i>', 'particípios perfeitos passivos (capítulo 29) com dativos de interesse: "dado a nós, nascido para nós". O sujeito, Cristo, só aparece no verbo <i>clausit</i>.'],
    ['2', '<i>sparsō verbī sēmine</i>', 'ablativo absoluto (capítulo 30): "espalhada a semente da palavra".'],
    ['2', '<i>suī morās incolātūs</i>', '<i>mora, -ae</i>, demora, tempo de permanência; <i>incolātus, -ūs</i> (4ª decl.), residência, estada; <i>suī</i>, genitivo de <i>suus</i> concordando com <i>incolātūs</i>: "o tempo da sua estada".'],
    ['3', '<i>observātā lēge plēnē cibīs in lēgālibus</i>', 'ablativo absoluto: "observada plenamente a lei"; <i>cibīs in lēgālibus</i> = <i>in cibīs lēgālibus</i>, "nos alimentos prescritos pela lei" (a ceia pascal judaica). A preposição entre o nome e o adjetivo é uma licença poética.'],
    ['3', '<i>cibum turbae duodēnae sē dat</i>', '<i>sē</i> é o objeto e <i>cibum</i> o predicativo dele: "dá-se a si mesmo como alimento"; <i>turbae duodēnae</i>, dativo, "ao grupo dos doze" (<i>duodēnī</i>, distributivo, capítulo 19).'],
    ['4', '<i>Verbum carō… efficit</i>', '<i>Verbum carō</i>, "o Verbo (feito) carne", é o sujeito; <i>efficit</i> com dois acusativos, <i>pānem</i> e <i>carnem</i>: "faz do pão carne". <i>Verbō</i>, ablativo de meio: "por uma palavra". O jogo <i>Verbum… verbō</i> é proposital.'],
    ['4', '<i>fitque sanguis Chrīstī merum</i>', '<i>merum, -ī</i> (n.), vinho puro, é o sujeito de <i>fit</i>; <i>sanguis</i>, o predicativo: "e o vinho torna-se o sangue de Cristo".'],
    ['4', '<i>ad firmandum cor sincērum</i>', '<i>ad</i> + gerundivo concordando com <i>cor</i>: finalidade, "para firmar um coração sincero" (capítulo 31).'],
    ['5', '<i>cernuī</i>', '<i>cernuus, -a, -um</i>, inclinado para a frente, prostrado; nominativo plural, predicativo do sujeito "nós".'],
    ['5', '<i>antīquum documentum</i>', '<i>documentum, -ī</i> (n.), ensinamento, lição: a Lei antiga. É <b>nominativo</b>, sujeito de <i>cēdat</i>, embora tenha a mesma forma do acusativo.'],
    ['5', '<i>sēnsuum dēfectuī</i>', 'genitivo plural e dativo singular da 4ª declinação (<i>sēnsus, -ūs</i>; <i>dēfectus, -ūs</i>): "à falha dos sentidos".'],
    ['6', '<i>Genitōrī Genitōque</i>', 'dativos: "ao que gerou e ao que foi gerado", o Pai e o Filho.'],
    ['6', '<i>laus et iūbilātiō… sit</i>', 'vários sujeitos com o verbo no singular, concordando com o mais próximo; subjuntivo de desejo: "seja (dado) louvor e júbilo".'],
    ['6', '<i>prōcēdentī ab utrōque</i>', 'particípio presente no dativo: "ao que procede de ambos", o Espírito Santo. <i>Compar</i>, "igual".'],
], 'Pange lingua: notas, estrofe a estrofe')}
<h3>Análise: o Tantum ergo</h3>
<p>A quinta estrofe é a mais cantada do hino e um pequeno catálogo dos subjuntivos de vontade do capítulo 32:</p>
{analise('Pange lingua, estrofe 5, palavra a palavra', [
    ('Tantum', 'tantus, -a, -um, tão grande', 'acusativo singular neutro', 'adjunto de <i>sacrāmentum</i>'),
    ('ergō', 'ergō (conjunção)', 'invariável', '"pois, portanto": tira a consequência das estrofes anteriores'),
    ('sacrāmentum', 'sacrāmentum, -ī (n.)', 'acusativo singular', 'objeto direto de <i>venerēmur</i>'),
    ('venerēmur', 'veneror, -ārī, venerātus sum (depoente, 1ª conj.)', 'presente do subjuntivo, 1ª pl. (<i>ā</i> → <i>ē</i>)', 'exortativo: "veneremos" (Bennett § 274)'),
    ('cernuī', 'cernuus, -a, -um, prostrado', 'nominativo plural masculino', 'predicativo do sujeito "nós"'),
    ('et antīquum documentum', 'antīquus, -a, -um; documentum, -ī (n.)', 'nominativo singular neutro', 'sujeito de <i>cēdat</i>'),
    ('novō… rītuī', 'novus, -a, -um; rītus, -ūs (m.), rito', 'dativo singular (4ª decl. em <i>-uī</i>)', 'complemento de <i>cēdat</i>: "ao novo rito"'),
    ('cēdat', 'cēdō, -ere, cessī, ceder', 'presente do subjuntivo, 3ª sing. (3ª conj.: + <i>a</i>)', 'jussivo: "ceda" (Bennett § 275)'),
    ('praestet', 'praestō, -āre, fornecer', 'presente do subjuntivo, 3ª sing. (1ª conj.: <i>ā</i> → <i>e</i>)', 'jussivo: "que forneça, supra"'),
    ('fidēs', 'fidēs, -eī (f.), fé', 'nominativo singular', 'sujeito de <i>praestet</i>; sentido cristão (capítulo 50)'),
    ('supplēmentum', 'supplēmentum, -ī (n.), complemento', 'acusativo singular', 'objeto direto de <i>praestet</i>'),
    ('sēnsuum', 'sēnsus, -ūs (m.), sentido', 'genitivo plural', 'adjunto de <i>dēfectuī</i>'),
    ('dēfectuī', 'dēfectus, -ūs (m.), falha, falta', 'dativo singular', 'objeto indireto: "à falha"'),
])}
<p>O ponto delicado é <i>antīquum documentum</i>. Quem lê em ordem vê um acusativo possível (a forma neutra é ambígua) logo depois do objeto <i>sacrāmentum</i> e tende a juntá-lo a <i>venerēmur</i>. Mas o <i>et</i> abre uma nova oração, e <i>cēdat</i>, no singular, precisa de um sujeito: é <i>documentum</i>. O raciocínio por exclusão do capítulo 3 resolve: <i>novō rītuī</i> está no dativo, <i>cēdō</i> é intransitivo, e só sobra o neutro para sujeito.</p>
'''),
        ('Dies irae: o texto', f'''
<p>O <i>Dies irae</i> é uma <b>sequência</b>, isto é, um poema cantado na missa antes do Evangelho. Ele é tradicionalmente atribuído a Tomás de Celano, frade franciscano do século XIII e biógrafo de São Francisco, mas a autoria não é segura. Durante séculos foi a sequência da missa de defuntos (o <i>Requiem</i>) no rito romano; a reforma litúrgica de 1969–1970 tirou-o da missa, e ele sobrevive na liturgia das horas, nas celebrações segundo os livros anteriores à reforma e nas obras de Mozart, Verdi e tantos outros. O primeiro verso vem da Vulgata, do profeta Sofonias: <i>Diēs īrae diēs illa, diēs tribulātiōnis et angustiae…</i>, "Dia de ira aquele dia, dia de tribulação e de angústia…" (Sf 1,15). O poema descreve o Juízo Final e passa, na estrofe VII, da descrição à súplica pessoal.</p>
{exemplos([
    ('Diēs īrae, diēs illa,<br>solvet saeclum in favillā,<br>teste David cum Sibyllā.', 'I. Dia de ira, aquele dia, desfará o mundo em cinzas, como atestam Davi e a Sibila.'),
    ('Quantus tremor est futūrus,<br>quandō iūdex est ventūrus,<br>cūncta strictē discussūrus!', 'II. Quanto tremor haverá, quando o juiz vier para examinar tudo com rigor!'),
    ('Tuba, mīrum spargēns sonum<br>per sepulcra regiōnum,<br>cōget omnēs ante thronum.', 'III. A trombeta, espalhando um som assombroso pelos sepulcros de todas as terras, reunirá todos diante do trono.'),
    ('Mors stupēbit et nātūra,<br>cum resurget creātūra,<br>iūdicantī respōnsūra.', 'IV. A morte e a natureza ficarão atônitas, quando a criatura ressurgir para responder a quem a julga.'),
    ('Liber scrīptus prōferētur,<br>in quō tōtum continētur,<br>unde mundus iūdicētur.', 'V. Será apresentado o livro escrito, em que tudo está contido, pelo qual o mundo há de ser julgado.'),
    ('Iūdex ergō cum sedēbit,<br>quidquid latet appārēbit:<br>nīl inultum remanēbit.', 'VI. Quando, pois, o juiz se assentar, tudo o que está oculto aparecerá: nada ficará sem castigo.'),
    ('Quid sum miser tunc dictūrus?<br>Quem patrōnum rogātūrus,<br>cum vix iūstus sit sēcūrus?', 'VII. Que hei de dizer então, miserável? A que protetor hei de recorrer, quando nem o justo estará seguro?'),
    ('Rēx tremendae māiestātis,<br>quī salvandōs salvās grātīs,<br>salvā mē, fōns pietātis.', 'VIII. Rei de tremenda majestade, que salvas de graça os que hão de ser salvos, salva-me, fonte de bondade!'),
    ('Recordāre, Iēsū pie,<br>quod sum causa tuae viae:<br>nē mē perdās illā diē.', 'IX. Lembra-te, ó bom Jesus, de que sou a razão do teu caminho: não me percas naquele dia.'),
    ('Quaerēns mē sēdistī lassus,<br>redēmistī crucem passus:<br>tantus labor nōn sit cassus.', 'X. Ao me procurar, sentaste-te cansado; remiste-me sofrendo a cruz: que tanto trabalho não seja em vão.'),
])}
<p>Fonte: texto de Charles C. Nott (1902), na Wikisource latina, estrofes I–X de dezoito; adaptações: <i>ae</i> por <i>æ</i>, <i>i</i> por <i>j</i>, <i>cum</i> por <i>quum</i> (capítulo 50), <i>Sibyllā</i> por <i>Sybillâ</i>, macrons acrescentados. As estrofes XI–XVIII são lidas no exercício 4. O texto litúrgico acrescenta, depois da última estrofe, uma prece final (<i>Pie Iēsū Domine, dōnā eīs requiem</i>) que não está na edição de Nott. A tradução é deste livro.</p>
'''),
        ('Lendo o Dies irae', f'''
<h3>O ritmo e as rimas</h3>
<p>O <i>Dies irae</i> é mais simples e mais insistente que o <i>Pange lingua</i>. Cada verso tem <b>oito sílabas</b>, todas paroxítonas no fim, com acentos nas ímpares: é um dímetro trocaico acentual, dois pares de troqueus completos. Os versos se agrupam em <b>tercetos</b> com uma só rima: <i>illa, favillā, Sibyllā</i>; <i>futūrus, ventūrus, discussūrus</i>; <i>sonum, regiōnum, thronum</i>. Essa rima tripla, que soa como um sino, é o recurso mais característico do poema. Para caber nas oito sílabas, o poeta usa às vezes formas mais curtas: <i>saeclum</i> por <i>saeculum</i>, <i>nīl</i> por <i>nihil</i>. Com <i>saeculum</i>, o segundo verso teria nove sílabas; num verso clássico, a elisão de <i>saeclum in</i> resolveria a conta de outro modo, mas aqui todas as sílabas soam: <i>sol-vet-sae-clum-in-fa-vil-lā</i>.</p>
<h3>Notas</h3>
{tabela(['Estrofe', 'Expressão', 'Nota'], [
    ['I', '<i>solvet saeclum in favillā</i>', '<i>solvō, -ere</i>, dissolver; futuro. <i>Saeclum</i>, forma sincopada de <i>saeculum</i>, "o mundo" (sentido cristão, capítulo 50); <i>favilla, -ae</i>, cinza.'],
    ['I', '<i>teste David cum Sibyllā</i>', 'ablativo absoluto sem particípio (capítulo 30): "sendo testemunha Davi com a Sibila", isto é, os Salmos e os oráculos da Sibila, que a tradição cristã lia como profecias.'],
    ['II', '<i>est futūrus… est ventūrus… discussūrus</i>', 'particípios futuros com <i>sum</i>: a perifrástica ativa, "está para ser, há de vir" (Bennett § 115). <i>Discussūrus</i> (de <i>discutiō</i>, examinar) indica a finalidade: "para examinar".'],
    ['III', '<i>cōget</i>', 'futuro de <i>cōgō, -ere</i>, reunir (de <i>co-</i> + <i>agō</i>).'],
    ['IV', '<i>iūdicantī respōnsūra</i>', '<i>iūdicantī</i>, particípio presente no dativo, "a quem julga"; <i>respōnsūra</i>, particípio futuro concordando com <i>creātūra</i>: "para responder".'],
    ['V', '<i>unde mundus iūdicētur</i>', 'relativa final: <i>unde</i> = <i>ut inde</i>, "para que a partir dele" (Bennett § 282.2). Ver o diagrama abaixo.'],
    ['VI', '<i>nīl inultum remanēbit</i>', '<i>inultus, -a, -um</i>, impune, não vingado: "nada ficará impune".'],
    ['VII', '<i>Quid sum miser tunc dictūrus? Quem patrōnum rogātūrus</i>', 'perifrástica ativa (o <i>sum</i> se subentende no segundo verso): "que hei de dizer, a que protetor hei de rogar?". <i>Miser</i> é predicativo do sujeito "eu".'],
    ['VII', '<i>cum vix iūstus sit sēcūrus</i>', '<i>cum</i> + subjuntivo causal ou concessivo (Bennett §§ 286.2 e 309.3; A&amp;G § 549): "quando, já que, nem o justo está seguro".'],
    ['VIII', '<i>quī salvandōs salvās grātīs</i>', '<i>salvandōs</i>, gerundivo (capítulo 31) usado como substantivo: "os que devem ser salvos"; <i>grātīs</i>, advérbio, "de graça". <i>Salvāre</i> é o verbo cristão do capítulo 50.'],
    ['IX', '<i>Recordāre… quod sum causa tuae viae</i>', '<i>recordāre</i>, imperativo do depoente <i>recordor</i> (capítulo 25); <i>quod</i> + indicativo no lugar da oração infinitiva, como no latim cristão (capítulo 50): "lembra-te de que sou a causa".'],
    ['IX', '<i>nē mē perdās</i>', 'proibição com <i>nē</i> + presente do subjuntivo: ver a seção 6.'],
    ['X', '<i>Quaerēns mē sēdistī lassus</i>', 'alusão a Jo 4,6, onde Jesus, cansado do caminho, se senta junto ao poço: <i>Iēsūs ergō fatīgātus ex itinere, sedēbat sīc suprā fontem</i>. <i>Sēdistī</i>, perfeito de <i>sedeō</i>.'],
    ['X', '<i>crucem passus</i>', 'particípio perfeito de <i>patior</i>, depoente: "tendo sofrido (sofrendo) a cruz".'],
], 'Dies irae, estrofes I–X: notas')}
{diagrama_frase([('Liber scrīptus', 'sujeito · "o livro escrito"'), ('prōferētur', 'futuro passivo · "será apresentado"'), ('in quō tōtum', 'relativa · "em que tudo"'), ('continētur', 'presente passivo · "está contido"'), ('unde… iūdicētur', 'relativa final · subjuntivo')], 'Dies irae, estrofe V: uma oração principal e duas relativas que dependem de <i>liber</i>. A primeira (<i>in quō</i>) descreve o livro, no indicativo; a segunda (<i>unde</i>, "de onde, pelo qual") diz para que ele serve, no subjuntivo: <i>unde</i> = <i>ut inde</i> (Bennett § 282.2).')}
'''),
        ('Os subjuntivos dos hinos', f'''
<p>Um hino é uma oração cantada: convida, ordena, deseja, suplica. Por isso vive do subjuntivo de vontade estudado no capítulo 32, e lê-lo é uma boa revisão daquele capítulo. A tabela reúne os subjuntivos dos dois textos e compara cada um com a norma clássica.</p>
{tabela(['Forma', 'Onde', 'Uso', 'Comentário'], [
    ['<i>venerēmur</i>', 'Pange lingua 5', 'exortativo (1ª pl.)', 'clássico (Bennett § 274): "veneremos"'],
    ['<i>cēdat, praestet</i>', 'Pange lingua 5', 'jussivo (3ª sing.)', 'clássico (Bennett § 275): "ceda", "supra"'],
    ['<i>sit… sit</i>', 'Pange lingua 6', 'optativo / jussivo', 'desejo sem <i>utinam</i>, como nas fórmulas de louvor (Bennett § 279; A&amp;G § 441): "seja"'],
    ['<i>iūdicētur</i>', 'Dies irae V', 'relativa final', 'clássico (Bennett § 282.2): <i>unde</i> = <i>ut inde</i>'],
    ['<i>sit sēcūrus</i>', 'Dies irae VII', '<i>cum</i> causal ou concessivo', 'clássico (Bennett §§ 286.2, 309.3)'],
    ['<i>nē… perdās</i>', 'Dies irae IX', 'proibição: <i>nē</i> + presente', 'Bennett § 276 admite o presente e o perfeito, mas nota que as duas construções são pouco frequentes na prosa clássica, que prefere <i>nōlī</i> + infinitivo; nas orações e na Vulgata o presente é comum (<i>nē nōs indūcās</i>, capítulo 32)'],
    ['<i>nōn sit cassus</i>', 'Dies irae X', 'jussivo/optativo negado com <i>nōn</i>', 'a norma é <i>nē</i>; A&amp;G § 439, nota 3, registra <i>nōn</i> "ocasionalmente nos poetas e nos autores tardios"'],
])}
<p>Repare que quase todos os usos são clássicos: o latim dos hinos não inventa subjuntivos novos, usa os de sempre com a frequência que o gênero pede. As duas marcas tardias são pequenas e coerentes com o capítulo 50: a preferência pelo presente na proibição, que vem da linguagem da oração e da Vulgata, e a negação <i>nōn</i> num desejo, que soa ao ouvido medieval como o nosso "que não seja em vão".</p>
{observacao('Indicativo, subjuntivo e futuro no Dies irae', 'As seis primeiras estrofes descrevem o Juízo no <b>futuro do indicativo</b> (<i>solvet, cōget, stupēbit, prōferētur, appārēbit, remanēbit</i>) e na perifrástica ativa (<i>est futūrus, est ventūrus</i>): é o que vai acontecer. A partir da estrofe VII, a voz passa à primeira pessoa e os modos mudam: perguntas deliberativas na perifrástica (<i>quid sum dictūrus?</i>), imperativos (<i>salvā mē, recordāre</i>) e subjuntivos de súplica (<i>nē mē perdās, nōn sit cassus</i>). A gramática acompanha a passagem do medo à oração.')}
<h3>Resumo</h3>
<ul>
<li><b>Verso rítmico</b>: número fixo de sílabas, acentos nas posições fortes, rima, sem elisão; a quantidade deixa de contar.</li>
<li><b>Pange lingua</b>: estrofes de seis versos de 8 e 7 sílabas (o tetrâmetro trocaico catalético em versão acentual), rimas alternadas; Tomás de Aquino, festa de <i>Corpus Christi</i>; <i>Tantum ergō</i> nas duas últimas estrofes.</li>
<li><b>Dies irae</b>: tercetos de versos de 8 sílabas (dímetro trocaico acentual) com rima única; sequência da missa de defuntos; atribuído a Tomás de Celano; primeiro verso de Sofonias 1,15.</li>
<li><b>Subjuntivos</b>: exortativo, jussivo, optativo, relativa final, <i>cum</i> causal, proibição com <i>nē</i> + presente; <i>nōn</i> em desejo como traço tardio.</li>
</ul>
<p>O capítulo 53 volta à prosa: as <i>Confissões</i> de Agostinho, um latim cristão de alta retórica.</p>
'''),
    ],
    erros_comuns=[
        ('Escandir o hino por longas e breves, como um verso de Virgílio.', 'Os hinos rítmicos ignoram a quantidade: <i>diēs</i>, com <i>i</i> breve, abre o <i>Dies irae</i> num tempo forte. Conte sílabas e marque os acentos das palavras; a escansão quantitativa (capítulo 40) serve para a poesia clássica e para os hinos antigos de metro clássico, não para estes.'),
        ('Elidir vogais ao contar as sílabas (<i>tant(um) ergō</i>, <i>sae(clum) in</i>).', 'No verso rítmico todas as sílabas soam. <i>Tantum ergō sacrāmentum</i> tem oito sílabas, e é com oito que ele casa com a melodia e com os outros versos ímpares do hino.'),
        ('Ler <i>antīquum documentum</i> como objeto de <i>venerēmur</i>.', 'O <i>et</i> abre outra oração, cujo verbo é <i>cēdat</i>, no singular: o sujeito só pode ser o neutro <i>documentum</i>. "Ceda a antiga lição ao novo rito", não "veneremos a antiga lição".'),
        ('Traduzir <i>est futūrus</i>, <i>est ventūrus</i> como presentes ("é futuro", "é vindouro").', 'É a perifrástica ativa (Bennett § 115): particípio futuro + <i>sum</i> = "há de ser, está para vir". Em português, "quanto tremor haverá, quando o juiz vier".'),
        ('Corrigir <i>nōn sit cassus</i> para <i>nē sit cassus</i>, ou <i>nē perdās</i> para <i>nē perdiderīs</i>.', 'O texto está certo para o seu tempo. A norma clássica prefere <i>nē</i> nos desejos e o perfeito ou <i>nōlī</i> nas proibições, mas o presente proibitivo é comum nas orações e na Vulgata, e <i>nōn</i> no jussivo aparece nos poetas e nos autores tardios (A&amp;G § 439, nota 3). Reconheça, não corrija.'),
        ('Ler <i>cibum… sē dat</i> como "dá o alimento a si mesmo".', '<i>Sē</i> é o objeto direto e <i>cibum</i> o seu predicativo: "dá-se a si mesmo como alimento". O destinatário está no dativo, <i>turbae duodēnae</i>.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Contar, acentuar, rimar',
            'Faça a análise rítmica dos dois primeiros versos do Tantum ergo: <i lang="la">Tantum ergō sacrāmentum / venerēmur cernuī</i>.', [
            ('Divida o primeiro verso em sílabas, sem elisão. Quantas são?', '<i>tan-tum-er-gō-sa-crā-men-tum</i>: oito sílabas. O <i>-um</i> de <i>tantum</i> não se elide diante de <i>ergō</i>.'),
            ('Onde caem os acentos das palavras?', '<i><b>tan</b>tum</i> (dissílaba, acento na primeira), <i><b>er</b>gō</i> (idem), <i>sa-crā-<b>men</b>-tum</i> (penúltima longa por posição, <i>-men-</i> seguido de <i>nt</i>, recebe o acento). Acentos nas sílabas 1, 3 e 7; a 5ª (<i>sa-</i>) recebe um acento secundário no canto. Movimento trocaico: forte-fraco.'),
            ('E o segundo verso?', '<i>ve-ne-rē-mur-cer-nu-ī</i>: sete sílabas. Acentos: <i>ve-ne-<b>rē</b>-mur</i> (penúltima <i>rē</i> longa) e <i><b>cer</b>-nu-ī</i> (penúltima <i>nu</i> breve, acento na antepenúltima). O verso termina em proparoxítona, como todos os versos pares do hino.'),
            ('Com que versos da mesma estrofe eles rimam?', '<i>Sacrāmentum</i> rima com <i>documentum</i> e <i>supplēmentum</i> (versos ímpares, <i>-entum</i>); <i>cernuī</i> com <i>rītuī</i> e <i>dēfectuī</i> (versos pares, <i>-uī</i>).'),
        ], 'Conclusão: 8 + 7 sílabas, acentos nas ímpares, rimas alternadas: é a arquitetura de todas as estrofes do <i>Pange lingua</i>.'),
        pratica_guiada('Prática guiada 2 · Uma súplica (Dies irae, IX)',
            'Analise e traduza: <i lang="la">Recordāre, Iēsū pie, / quod sum causa tuae viae: / nē mē perdās illā diē.</i> Vocabulário: <i>recordor, -ārī</i>, lembrar-se; <i>pius, -a, -um</i>, piedoso, bom; <i>via, -ae</i>, caminho; <i>perdō, -ere</i>, perder.', [
            ('Que forma é <i>recordāre</i>? Cuidado com o infinitivo.', 'É o imperativo presente, 2ª sing., do depoente <i>recordor</i>: "lembra-te". Nos depoentes o imperativo singular tem a forma de um infinitivo ativo (capítulo 25); o vocativo ao lado (<i>Iēsū pie</i>) confirma que é uma ordem a alguém.'),
            ('Que caso são <i>Iēsū</i> e <i>pie</i>?', 'Vocativos: <i>Iēsū</i>, vocativo de <i>Iēsūs, -ū</i>; <i>pie</i>, de <i>pius</i>, com o <i>-e</i> dos adjetivos em <i>-us</i>.'),
            ('Como funciona <i>quod sum causa tuae viae</i>?', '<i>Quod</i> + indicativo diz o conteúdo da lembrança: "(lembra-te) de que sou a causa do teu caminho". É o <i>quod</i> declarativo do capítulo 50; em latim clássico, <i>mē esse causam</i>. "O teu caminho" é a vinda de Cristo ao mundo.'),
            ('E <i>nē mē perdās</i>?', 'Proibição (ou súplica negativa) com <i>nē</i> + presente do subjuntivo de <i>perdō</i> (3ª conj., + <i>a</i>), 2ª sing.: "não me percas" (Bennett § 276). <i>Illā diē</i>, ablativo de tempo: "naquele dia".'),
            ('Monte a tradução.', '"Lembra-te, ó bom Jesus, de que eu sou a razão do teu caminho: não me percas naquele dia."'),
        ]),
    ],
    exercicios=[
        exercicio('Exercício 1 · Sílabas e acentos', 'Conte as sílabas sem elisão, marque os acentos e diga se o verso é de 8 ou de 7 sílabas e se termina em paroxítona ou proparoxítona.', [
            ('<i>Nōbīs datus, nōbīs nātus</i>', '<i><b>nō</b>-bīs-<b>da</b>-tus-<b>nō</b>-bīs-<b>nā</b>-tus</i>: 8 sílabas, acentos nas ímpares, final paroxítono.'),
            ('<i>ex intāctā Virgine</i>', '<i>ex-in-<b>tāc</b>-tā-<b>vir</b>-gi-ne</i>: 7 sílabas (sem elisão de <i>ex in-</i>), final proparoxítono (<i><b>Vir</b>-gi-ne</i>).'),
            ('<i>Quid sum miser tunc dictūrus</i>', '<i><b>quid</b>-sum-<b>mi</b>-ser-<b>tunc</b>-dic-<b>tū</b>-rus</i>: 8 sílabas. <i>Miser</i> tem <i>i</i> breve, mas recebe o acento: o ritmo é acentual.'),
            ('<i>Solvet saeclum in favillā</i>', '<i><b>sol</b>-vet-<b>sae</b>-clum-in-fa-<b>vil</b>-lā</i>: 8 sílabas sem elisão; com <i>saeculum</i> seriam 9. A 5ª sílaba (<i>in</i>) é fraca: nem todo verso tem os quatro acentos.'),
            ('<i>Procedenti ab utroque</i> (Pange lingua 6)', '<i>prō-cē-<b>den</b>-tī-ab-u-<b>trō</b>-que</i>: 8 sílabas, sem elisão de <i>-tī ab</i>.'),
        ]),
        exercicio('Exercício 2 · Rimas e estrutura', 'Responda.', [
            ('Qual é o esquema de rimas da estrofe 3 do Pange lingua?', 'Alternado, ABABAB: <i>coenae, plēnē, duodēnae</i> (A, <i>-ēn-</i>) e <i>frātribus, lēgālibus, manibus</i> (B, <i>-ibus</i>).'),
            ('Qual é o esquema das estrofes do Dies irae?', 'AAA: uma rima por terceto (<i>tremor… futūrus / ventūrus / discussūrus</i>). Na estrofe XVIII, de quatro versos, a rima muda no meio (<i>illa / favillā</i> e <i>reus / Deus</i>).'),
            ('Que palavra do Dies irae I foi encurtada para caber no verso, e por quê?', '<i>Saeclum</i>, forma sincopada de <i>saeculum</i>: com a forma longa o verso teria nove sílabas, e no verso rítmico não há elisão que absorva a sílaba a mais.'),
            ('De onde vem o primeiro verso do Pange lingua?', 'Do hino de Venâncio Fortunato (século VI) sobre a cruz, <i>Pange, lingua, glōriōsī proelium certāminis</i>. Tomás repete as três primeiras palavras e o molde rítmico.'),
        ]),
        exercicio('Exercício 3 · Classifique os subjuntivos', 'Dê o tempo, a pessoa e o uso do subjuntivo e traduza a expressão.', [
            ('<i>venerēmur</i> (Pange lingua 5)', 'Presente, 1ª pl., do depoente <i>veneror</i>; exortativo: "veneremos".'),
            ('<i>compar sit laudātiō</i> (Pange lingua 6)', 'Presente de <i>sum</i>, 3ª sing.; optativo/jussivo de louvor: "seja igual o louvor".'),
            ('<i>unde mundus iūdicētur</i> (Dies irae V)', 'Presente passivo, 3ª sing., de <i>iūdicō</i>; relativa final com <i>unde</i> = <i>ut inde</i>: "pelo qual o mundo seja julgado".'),
            ('<i>cum vix iūstus sit sēcūrus</i> (Dies irae VII)', 'Presente de <i>sum</i>, 3ª sing.; <i>cum</i> causal/concessivo: "quando nem o justo está seguro".'),
            ('<i>nē mē perdās</i> (Dies irae IX)', 'Presente, 2ª sing., de <i>perdō</i>; proibição com <i>nē</i>: "não me percas".'),
            ('<i>nē perennī cremer igne</i> (Dies irae XIV; <i>cremō, -āre</i>, queimar; <i>perennis, -e</i>, eterno)', 'Presente passivo, 1ª sing., de <i>cremō</i> (1ª conj.: <i>crem-e-r</i>); oração final com <i>nē</i> depois de <i>fac benignē</i>: "(faze, em tua bondade,) que eu não seja queimado no fogo eterno" (Bennett § 282.1).'),
        ]),
        exercicio('Exercício 4 · Traduza as estrofes finais do Dies irae', 'Traduza. Texto de Nott (1902), adaptado como as estrofes I–X. Vocabulário: <i>ultiō, -ōnis</i>, castigo, vingança; <i>remissiō, -ōnis</i>, perdão; <i>ratiō, -ōnis</i>, prestação de contas; <i>ingemīscō, -ere</i>, gemer; <i>tamquam</i>, como; <i>reus, -ī</i>, réu; <i>rubeō, -ēre</i>, ficar vermelho; <i>vultus, -ūs</i>, rosto; <i>supplicō, -āre</i>, suplicar; <i>parcō, -ere</i>, poupar (com dativo); <i>supplex, -icis</i>, suplicante; <i>acclīnis, -e</i>, inclinado; <i>contrītus</i>, triturado, contrito; <i>cinis, -eris</i>, cinza; <i>lacrimōsus</i>, lacrimoso.', [
            ('<i>Iūste iūdex ultiōnis, / dōnum fac remissiōnis / ante diem ratiōnis.</i> (XI)', '"Justo juiz do castigo, concede o dom do perdão antes do dia das contas." <i>Iūste iūdex</i>, vocativo; <i>fac</i>, imperativo curto de <i>faciō</i> (capítulo 22); <i>dōnum fac</i>, "faze (dá) o dom".'),
            ('<i>Ingemīscō tamquam reus, / culpā rubet vultus meus: / supplicantī parce, Deus.</i> (XII)', '"Gemo como um réu, de culpa enrubesce o meu rosto: poupa, ó Deus, quem te suplica." <i>Culpā</i>, ablativo de causa; <i>supplicantī</i>, particípio presente no dativo, exigido por <i>parce</i>.'),
            ('<i>Ōrō supplex et acclīnis, / cor contrītum quasi cinis: / gere cūram meī fīnis.</i> (XVII)', '"Rogo suplicante e inclinado, com o coração contrito como cinza: cuida do meu fim." <i>Cor contrītum</i> é um nominativo solto (ou acusativo de relação), "(tendo) o coração contrito"; <i>gere cūram</i> + genitivo, "tem cuidado de"; <i>meī</i> concorda com <i>fīnis</i>.'),
            ('<i>Lacrimōsa diēs illa, / quā resurget ex favillā / iūdicandus homō reus: / huic ergō parce, Deus.</i> (XVIII)', '"Dia de lágrimas aquele, em que ressurgirá da cinza o homem culpado para ser julgado: poupa-o, pois, ó Deus." <i>Quā</i>, ablativo de tempo do relativo (retoma <i>diēs</i>, aqui feminino); <i>iūdicandus</i>, gerundivo, "que deve ser julgado"; <i>huic</i>, dativo de <i>hīc</i> com <i>parce</i>.'),
        ]),
        exercicio('Exercício 5 · Construções do Pange lingua', 'Explique a construção destacada e traduza.', [
            ('<i><b>sparsō verbī sēmine</b></i> (2)', 'Ablativo absoluto (capítulo 30): particípio <i>sparsō</i> + nome <i>sēmine</i> no ablativo, com o genitivo <i>verbī</i>. "Espalhada a semente da palavra", "depois de espalhar a semente da palavra".'),
            ('<i><b>observātā lēge</b> plēnē</i> (3)', 'Outro ablativo absoluto: "observada plenamente a lei".'),
            ('<i>pānem vērum verbō <b>carnem efficit</b></i> (4)', '<i>Efficiō</i> com dois acusativos, objeto (<i>pānem</i>) e predicativo do objeto (<i>carnem</i>): "faz do pão carne", como <i>Populus Cicerōnem cōnsulem creat</i>, "o povo elege Cícero cônsul" (capítulo 22).'),
            ('<i><b>ad firmandum</b> cor sincērum</i> (4)', '<i>Ad</i> + gerundivo concordando com <i>cor</i>: finalidade (capítulo 31). "Para firmar um coração sincero".'),
            ('<i><b>Genitōrī Genitōque</b> laus… sit</i> (6)', 'Dativos de interesse ("ao Pai e ao Filho") com o subjuntivo de desejo <i>sit</i>: "ao Pai e ao Filho seja louvor".'),
        ]),
    ],
    leituras=['aquino-pange-lingua-gloriosi-corporis-mysterium', 'celano-dies-irae', 'ambrosio-te-deum', 'todi-stabat-mater', 'xii-xiii-carmina-burana-selecao', 'ravizza-gramatica-latina'],
    leituras_nota='Leia os dois hinos inteiros nas páginas do catálogo (o <i>Dies irae</i> com as oito estrofes que ficaram para o exercício 4) e, se puder, ouça-os cantados em gregoriano: a melodia torna o ritmo evidente. O <i>Stabat Mater</i>, atribuído a Jacopone da Todi, usa um verso trocaico muito parecido com o do <i>Dies irae</i> (8 + 8 + 7 sílabas) e é o melhor texto para treinar o que você aprendeu aqui. O <i>Te Deum</i>, mais antigo, é prosa rítmica, sem métrica regular: compare. Os <i>Carmina Burana</i> mostram o verso rítmico rimado fora da igreja, em canções de taberna e de amor; são mais difíceis (nível 4 no catálogo). No Pe. Ravizza, o n. 541 lista os metros clássicos que a Igreja conservou nos seus hinos, com exemplos que você já pode ler.',
)
