from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='14-os-pronomes-pessoais', titulo='Pronomes pessoais, possessivos e reflexivos', titulo_latim='Dē prōnōminibus persōnālibus', tempo='60 min',
    resumo='Os pronomes ego, tū, nōs, vōs e suas formas (inclusive nostrum × nostrī e mēcum, tēcum, nōbīscum); por que o latim omite o pronome sujeito e quando o usa; is, ea, id no lugar da terceira pessoa; o reflexivo suī, sibi, sē; os possessivos meus, tuus, noster, vester e a distinção entre suus e eius, a armadilha do "seu" português, com uma frase do Evangelho de João analisada palavra a palavra.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['pronomes pessoais', 'ego, tū, nōs, vōs', 'mihi, tibi', 'nostrum × nostrī', 'mēcum, tēcum, nōbīscum', 'omissão do pronome sujeito', 'ênfase e contraste', 'is, ea, id como pronome de 3ª pessoa', 'pronome reflexivo suī, sibi, sē', 'sēcum', 'inter sē (reciprocidade)', 'pronomes possessivos', 'vocativo mī', 'suus × eius', 'o "seu" português', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 5 (segunda declinação e adjetivos de primeira classe, porque os possessivos se declinam como bonus e pulcher) e capítulo 6 (as seis pessoas do presente). Os capítulos 9 a 13 ajudam a reconhecer alguns nomes e as formas de perfeito das frases autênticas, que vêm glosadas.', licoes=['05-a-segunda-declinacao', '06-o-presente-do-indicativo']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 84 (ego, tū, nōs, vōs; 84.1 mī; 84.2 formas em -met; nota 22: o i final de mihi, tibi, sibi é às vezes longo na poesia), § 85 (reflexivo; 85.1 suī para todos os gêneros e os dois números; 85.2 valor recíproco), § 86 (possessivos; 86.1 suus só reflexivo, eius e eōrum, eārum nos outros casos; 86.2 vocativo mī), § 87 (paradigma de is, ea, id), § 142.4 (mēcum, tēcum, sēcum, nōbīscum, vōbīscum), § 166.2 (pronome sujeito implícito no verbo), § 242 (sintaxe dos pessoais: 242.1 ênfase, contraste, clareza; 242.2 meī, tuī, nostrī, vestrī objetivos × nostrum, vestrum partitivos; 242.3 nōs por ego), § 243 (possessivos: 243.1 omitidos quando claros; 243.1a posição), § 244 (reflexivos: 244.1 direto e indireto; 244.4 suus referido a outro caso; 244.5 mē, tē, nōs, vōs como reflexivos), § 245 (inter sē)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 140 (classes de pronomes), § 142 (não há pessoal de 3ª pessoa; usa-se um demonstrativo), § 143 (ego e tū; 143.a nōs por ego; 143.b–c nostrum partitivo, meī, tuī, nostrī objetivos; 143.d -met; 143.f cum enclítico), § 144 (reflexivo; 144.a mē, tē, nōs como reflexivos; nota 1 sēcum), § 145 (possessivos; vocativo mī; nota: suus só reflexivo, patrem suum × patrem eius; 145.c inter sē), § 295 (sintaxe dos pessoais: 295.a sujeito só por distinção ou ênfase; 295.b genitivos; 295.c sem pessoal de 3ª pessoa), § 296 (demonstrativo como pessoal: Caesar et exercitus eius, não suus), § 299 (reflexivo referido ao sujeito), § 300 (reflexivo indireto, só mencionado), § 302 (possessivo concorda com a coisa possuída; 302.a possessivo e não genitivo do pessoal; 302.c omissão)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 68 (pronomes pessoais e reflexivo, em português; b: nostrum, vestrum partitivos × nostrī, vestrī; c: mēcum, tēcum, sēcum, nōbīscum, vōbīscum; d: -met), n. 69 (possessivos; meus com vocativo mī; noster e vester como pulcher), n. 320 (sintaxe do reflexivo: suus referido ao sujeito, eius referido a um complemento)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 92 (pessoais e reflexivo; is, ea, id no lugar da 3ª pessoa; nota: nostrī, vestrī objetivos × nostrum, vestrum partitivos), § 93 (possessivos; meus, tuus, suus como bonus, noster e vester como niger; vocativo mī), §§ 316–318 (sintaxe: o reflexivo refere-se ao sujeito; inter sē; suus × eius)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Jo 10,11 e 10,14; 20,21; Mt 28,20; Lc 1,28; Sl 22,3–4 (23,3–4)', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', nota='Jo 10,11 analisado na seção 6; os demais versículos no exercício 5. Texto conferido em la.wikisource.org ("Vulgata Clementina/Evangelium Secundum Joannem", "Evangelium Secundum Matthaeum", "Evangelium Secundum Lucam", "Liber Psalmorum"); a edição não traz macrons e grafa j e æ: aqui escreve-se i e ae e acrescentam-se os macrons', tipo='dominio_publico'),
    ],
    objetivos=[
        'Declinar <i>ego, tū, nōs, vōs</i> e o reflexivo <i>suī, sibi, sē</i>, distinguindo <i>nostrum, vestrum</i> (partitivos: "de nós", "entre nós") de <i>nostrī, vestrī</i> (objetivos: "por nós", "a nosso respeito") e formando <i>mēcum, tēcum, sēcum, nōbīscum, vōbīscum</i>.',
        'Explicar por que o pronome sujeito latino costuma faltar e reconhecer quando ele aparece (ênfase, contraste).',
        'Usar <i>is, ea, id</i> como pronome de terceira pessoa ("ele, ela; o, a; lhe") e distinguir <i>eum</i> de <i>sē</i> pela referência ao sujeito.',
        'Declinar os possessivos <i>meus, tuus, noster, vester, suus</i> (com o vocativo <i>mī</i>) e fazê-los concordar com a coisa possuída, não com o possuidor.',
        'Escolher entre <i>suus</i> e <i>eius/eōrum</i> ao traduzir o "seu" português, e analisar palavra a palavra uma frase do Evangelho de João.',
    ],
    secoes=[
        ('Ego, tū, nōs, vōs', f'''
<p>No capítulo 6 você viu que o verbo latino traz a pessoa na terminação: <i>amō</i> é "eu amo", <i>amās</i> é "tu amas", <i>amāmus</i> é "nós amamos". Os <b>pronomes pessoais</b> são as palavras que designam essas mesmas pessoas fora do verbo: a 1ª pessoa, quem fala (<i>ego</i>, "eu"; <i>nōs</i>, "nós"), e a 2ª, a quem se fala (<i>tū</i>, "tu, você"; <i>vōs</i>, "vós, vocês"). Como os nomes, eles têm casos, porque podem ser sujeito, objeto, destinatário ou complemento de preposição. Diferentemente dos nomes, não pertencem a nenhuma das cinco declinações: são formas antigas e irregulares, que se aprendem de cor, como em português se aprendem "eu, me, mim, comigo".</p>
{tabela_declinacao('Pronomes pessoais da 1ª e da 2ª pessoa', [
    ('ego', 'nōs', 'tū', 'vōs'),
    ('me<b>ī</b>', 'nostr<b>um</b> · nostr<b>ī</b>', 'tu<b>ī</b>', 'vestr<b>um</b> · vestr<b>ī</b>'),
    ('mi<b>hi</b>', 'nō<b>bīs</b>', 'ti<b>bi</b>', 'vō<b>bīs</b>'),
    ('mē', 'nōs', 'tē', 'vōs'),
    ('—', '—', 'tū', 'vōs'),
    ('mē', 'nō<b>bīs</b>', 'tē', 'vō<b>bīs</b>')],
    colunas=('1ª sing.', '1ª pl.', '2ª sing.', '2ª pl.'))}
<p>Leia as colunas em voz alta: <i>ego, meī, mihi, mē, mē</i>; <i>tū, tuī, tibi, tē, tū, tē</i>. Três observações tornam o quadro mais fácil do que parece. Primeiro, <b>o acusativo e o ablativo singular são iguais</b> (<i>mē, tē</i>), e no plural o nominativo é igual ao acusativo (<i>nōs, vōs</i>) e o dativo igual ao ablativo (<i>nōbīs, vōbīs</i>), como em todos os plurais latinos. Segundo, <i>ego</i> e <i>nōs</i> <b>não têm vocativo</b>, pela razão óbvia de que ninguém chama a si mesmo; o vocativo de <i>tū</i> e <i>vōs</i> é igual ao nominativo. Terceiro, o <i>i</i> final de <i>mihi</i> e <i>tibi</i> é breve (os poetas às vezes o alongam, e há também um dativo contraído <i>mī</i>, poético); o acento cai na primeira sílaba: <u>mi</u>hi, <u>ti</u>bi.</p>
{exemplos([('Magister <b>mē</b> videt.', 'O professor me vê. (acusativo: objeto direto)'), ('Puella <b>tibi</b> rosam dat.', 'A menina te dá uma rosa (dá uma rosa a você). (dativo: destinatário)'), ('Poēta <b>nōbīs</b> fābulam nārrat.', 'O poeta nos conta uma história. (dativo plural)'), ('Amīcī <b>vōs</b> exspectant.', 'Os amigos esperam vocês. (acusativo plural; <i>exspectant</i>, esperam)')])}
<h3>Dois genitivos no plural: nostrum e nostrī</h3>
<p>O genitivo dos pessoais é pouco usado, e por um bom motivo que você verá na seção 4: para dizer "meu livro" o latim não usa o genitivo <i>meī</i>, usa o adjetivo possessivo <i>meus</i>. O que sobra para o genitivo são dois sentidos especiais, e no plural cada um tem sua forma. <b><i>Nostrum</i> e <i>vestrum</i></b> são <b>partitivos</b>: indicam o todo de que se tira uma parte, "de nós" no sentido de "dentre nós" (<i>ūnus nostrum</i>, "um de nós"; <i>multī vestrum</i>, "muitos de vocês"). <b><i>Nostrī</i> e <i>vestrī</i></b>, como <i>meī</i> e <i>tuī</i> no singular, são <b>objetivos</b>: a pessoa é o alvo de um sentimento ou de uma ação contida num nome (<i>amor nostrī</i>, "o amor por nós"; <i>memoria vestrī</i>, "a lembrança de vocês", isto é, que se tem de vocês). O português diz "de nós" nos dois casos, e por isso a distinção precisa ser aprendida; os usos do genitivo serão estudados com calma no capítulo 20.</p>
<h3>Mēcum, tēcum, nōbīscum: a preposição que vem depois</h3>
<p>A preposição <i>cum</i>, "com", pede ablativo, e com os pessoais e o reflexivo ela se <b>cola depois do pronome</b>, formando uma só palavra: <i>mēcum</i>, "comigo"; <i>tēcum</i>, "contigo, com você"; <i>nōbīscum</i>, "conosco"; <i>vōbīscum</i>, "convosco, com vocês"; e <i>sēcum</i>, "consigo" (seção 3). Nunca se diz <i>cum mē</i>. O português guarda a marca dessa construção: em "comigo", "contigo" e "consigo", o final <i>-go</i> é o antigo <i>-cum</i>, que deixou de ser sentido como preposição e recebeu um "com" novo na frente (explicação histórica corrente; o detalhe fonético não importa aqui).</p>
{exemplos([('Mārcus <b>mēcum</b> in hortō ambulat.', 'Marco passeia comigo no jardim. (<i>ambulat</i>, passeia)'), ('Puellae <b>nōbīscum</b> veniunt.', 'As meninas vêm conosco.'), ('Ūnus <b>vestrum</b> librum legit.', 'Um de vocês lê o livro. (<i>ūnus</i>, um: partitivo)')])}
{dica('<b>Ambiguidades do quadro.</b> <i>Mē</i> e <i>tē</i> podem ser acusativo ou ablativo; <i>nōs</i> e <i>vōs</i>, nominativo ou acusativo (ou vocativo, no caso de <i>vōs</i>); <i>nōbīs</i> e <i>vōbīs</i>, dativo ou ablativo. Decida como nos nomes: uma preposição pede ablativo (<i>ā mē</i>, <i>dē nōbīs</i>); um verbo de dar ou dizer pede dativo; e <i>nōs</i> é sempre objeto quando o verbo não está na 1ª pessoa do plural (<i>magister nōs laudat</i>). Com o verbo na 1ª do plural, <i>nōs</i> pode ser o sujeito expresso por ênfase (<i>nōs laudāmus</i>, "nós elogiamos") ou o objeto reflexivo ("nós nos elogiamos", seção 3): o contexto decide.')}
'''),
        ('Quando o pronome sujeito aparece', f'''
<p>Em latim, a regra é <b>não</b> usar o pronome sujeito. A terminação do verbo já diz quem faz a ação, e dizer <i>ego amō</i> seria dizer duas vezes "eu". Por isso <i>videō</i> basta para "eu vejo" e <i>venītis</i> para "vocês vêm". O português do Brasil, que tende a expressar o sujeito ("eu acho", "você sabe"), leva o aluno a pôr <i>ego</i> e <i>tū</i> em toda frase; resista. Um texto latino cheio de <i>ego</i> soa insistente, quase como um "eu, eu mesmo, eu" repetido.</p>
<p>Quando então o pronome aparece? Quando ele carrega uma informação que a terminação não carrega: <b>ênfase</b> ("<i>eu</i>, e não outro") ou <b>contraste</b> entre duas pessoas. Repare como, nos exemplos abaixo, o pronome sempre se opõe a alguém:</p>
{exemplos([('<b>Ego</b> labōrō, <b>tū</b> dormīs.', 'Eu trabalho, (e) tu dormes. (contraste entre duas pessoas: os dois pronomes são necessários)'), ('<b>Nōs</b> librōs legimus; <b>vōs</b> fābulās audītis.', 'Nós lemos livros; vocês ouvem histórias.'), ('Puerī nōn veniunt, sed <b>ego</b> veniō.', 'Os meninos não vêm, mas eu venho. (eu, ao contrário deles; <i>sed</i>, mas)'), ('Librum legō.', 'Leio o livro. (sem ênfase: nenhum pronome)')])}
<p>Daí uma regra prática de tradução nos dois sentidos. Do latim para o português, quando você encontrar um <i>ego</i> ou um <i>tū</i> expressos, procure o contraste que o justifica e, se o português permitir, marque-o ("<i>eu</i> é que trabalho"). Do português para o latim, deixe o pronome de fora, a não ser que a frase contraponha pessoas. Nas frases autênticas da seção 6 e do exercício 5 você verá esse uso funcionando: o <i>Ego</i> que abre Jo 10,11 não está lá por acaso.</p>
{observacao('Nōs no lugar de ego', 'Como o português ("nós achamos que..."), o latim usa com frequência a 1ª pessoa do plural pelo singular, nos pronomes e nos verbos, por modéstia ou à maneira de um autor que fala com o leitor. O contrário não acontece no latim clássico: <i>vōs</i> nunca substitui <i>tū</i> (Allen e Greenough § 143.a), ao contrário do "vós" de cortesia das línguas modernas. Para falar a uma só pessoa, a prosa clássica usa <i>tū</i>, mesmo diante de um rei ou de Deus.')}
<p>Para reforçar ainda mais um pronome, o latim tem uma partícula <i>-met</i> (<i>egomet</i>, "eu mesmo") e o pronome <i>ipse</i>, "mesmo, próprio". A partícula é rara; <i>ipse</i>, que é muito frequente, será estudado com os demonstrativos no capítulo 15.</p>
'''),
        ('A terceira pessoa: is, ea, id e o reflexivo sē', f'''
<p>O quadro da seção 1 não tem 3ª pessoa, e não por esquecimento: <b>o latim não tem um pronome pessoal de 3ª pessoa</b> propriamente dito. Para dizer "ele, ela, o, a, lhe", usa um <b>demonstrativo</b>, em geral o mais fraco deles, <i>is, ea, id</i>, "esse, aquele" (no próximo capítulo você o estudará ao lado de <i>hīc</i>, <i>ille</i> e <i>iste</i>). Aqui interessa só o seu uso como "ele, ela", com o paradigma para consulta:</p>
{tabela_declinacao('is, ea, id, usado como "ele, ela" (paradigma completo no capítulo 15)', [
    ('is', 'ea', 'id', 'eī (iī)', 'eae', 'ea'),
    ('ei<b>us</b>', 'ei<b>us</b>', 'ei<b>us</b>', 'e<b>ōrum</b>', 'e<b>ārum</b>', 'e<b>ōrum</b>'),
    ('e<b>ī</b>', 'e<b>ī</b>', 'e<b>ī</b>', 'e<b>īs</b> (iīs)', 'e<b>īs</b> (iīs)', 'e<b>īs</b> (iīs)'),
    ('e<b>um</b>', 'e<b>am</b>', 'id', 'e<b>ōs</b>', 'e<b>ās</b>', 'e<b>a</b>'),
    ('e<b>ō</b>', 'e<b>ā</b>', 'e<b>ō</b>', 'e<b>īs</b> (iīs)', 'e<b>īs</b> (iīs)', 'e<b>īs</b> (iīs)')],
    casos=('Nominativo', 'Genitivo', 'Dativo', 'Acusativo', 'Ablativo'),
    colunas=('m. sing.', 'f. sing.', 'n. sing.', 'm. pl.', 'f. pl.', 'n. pl.'))}
<p>Fora o genitivo <i>eius</i> e o dativo <i>eī</i> no singular, as terminações são as de <i>bonus</i>: <i>eum, eam</i>; <i>eō, eā</i>; <i>eōs, eās, ea</i>; <i>eōrum, eārum</i>. O pronome concorda em gênero e número com o nome que substitui, e o gênero é o gramatical: um livro (<i>liber</i>, m.) é "ele", <i>eum</i>; uma rosa é <i>eam</i>; um presente (<i>dōnum</i>, n.) é <i>id</i>. No nominativo, como os outros pronomes sujeito, <i>is</i> e <i>ea</i> só aparecem quando há ênfase; nos outros casos, são o modo normal de retomar alguém já mencionado:</p>
{exemplos([('Iūlia in hortō est; <b>eam</b> videō.', 'Júlia está no jardim; eu a vejo. (acusativo feminino)'), ('Puerī veniunt; magister <b>eīs</b> fābulam nārrat.', 'Os meninos chegam; o professor lhes conta uma história. (dativo plural)'), ('Mārcus librum habet et <b>eum</b> legit.', 'Marco tem um livro e o lê. (<i>eum</i>, masculino, porque <i>liber</i> é masculino)')])}
<h3>O reflexivo: suī, sibi, sē</h3>
<p>Compare "Marco o elogia" e "Marco se elogia". No primeiro caso, o objeto é outra pessoa; no segundo, é o próprio Marco. O latim distingue as duas coisas com rigor ainda maior do que o português: para a pessoa que é <b>o próprio sujeito</b> usa o <b>pronome reflexivo</b> <i>sē</i>; para qualquer outra pessoa, <i>is, ea, id</i>.</p>
{tabela_declinacao('Pronome reflexivo da 3ª pessoa (iguais no singular e no plural, nos três gêneros)', [
    ('—',), ('su<b>ī</b>',), ('si<b>bi</b>',), ('sē (sēsē)',), ('sē (sēsē)',)],
    casos=('Nominativo', 'Genitivo', 'Dativo', 'Acusativo', 'Ablativo'), colunas=('Formas',))}
<p>O reflexivo <b>não tem nominativo</b>, e a razão é lógica: ele significa "o próprio sujeito" e, por isso, nunca pode ser o sujeito. Também não distingue gênero nem número: <i>sē</i> é "se, a si mesmo, a si mesma, a si mesmos", conforme o sujeito. Repare que o paradigma copia o de <i>tū</i> (<i>tuī, tibi, tē</i> → <i>suī, sibi, sē</i>), e que <i>cum</i> se cola a ele como aos pessoais: <i>sēcum</i>, "consigo, com ele mesmo".</p>
{comparacao('Reflexivo × não reflexivo', ['Latim', 'Português', 'A quem se refere'], [
    ['Mārcus <b>sē</b> laudat.', 'Marco se elogia (elogia a si mesmo).', 'ao sujeito, Marco'],
    ['Mārcus <b>eum</b> laudat.', 'Marco o elogia (elogia outro homem).', 'a outra pessoa, já mencionada'],
    ['Puellae <b>sibi</b> rosās capiunt.', 'As meninas pegam rosas para si.', 'ao sujeito, as meninas'],
    ['Puellae <b>eīs</b> rosās dant.', 'As meninas dão rosas a eles (ou a elas).', 'a outras pessoas'],
    ['Magister librōs <b>sēcum</b> portat.', 'O professor leva os livros consigo.', 'ao sujeito, o professor'],
])}
<p>Na 1ª e na 2ª pessoa não há confusão possível, e o latim não precisa de uma forma especial: os casos oblíquos de <i>ego</i> e <i>tū</i> servem de reflexivos. <i>Mē laudō</i> é "elogio a mim mesmo"; <i>tē vidēs</i>, "tu te vês"; <i>nōs dēfendimus</i>, "nós nos defendemos" (<i>dēfendō</i>, defender). Nunca se diz <i>ego sē laudō</i>: <i>sē</i> é exclusivamente de 3ª pessoa.</p>
{observacao('Inter sē: "um ao outro"', 'O latim não tem pronome recíproco. Para dizer "um ao outro", "entre si", usa <i>inter sē</i> (e <i>inter nōs</i>, <i>inter vōs</i>), sem outro objeto: <i>Mārcus et Iūlia inter sē laudant</i>, "Marco e Júlia elogiam um ao outro". O mesmo valor recíproco aparece, às vezes, no próprio reflexivo.')}
'''),
        ('Os possessivos: meus, tuus, noster, vester, suus', f'''
<p>Os <b>pronomes possessivos</b> latinos são, na forma, simples <b>adjetivos de primeira classe</b>, como os que você aprendeu no capítulo 5. Há um para cada pessoa: <i>meus</i>, "meu"; <i>tuus</i>, "teu, seu (de você)"; <i>noster</i>, "nosso"; <i>vester</i>, "vosso, de vocês"; e, para a 3ª pessoa, <i>suus</i>, "seu (dele, dela, deles, delas)", que é reflexivo, como <i>sē</i>, e terá a seção seguinte só para ele. <i>Meus, tuus, suus</i> se declinam como <i>bonus</i>; <i>noster</i> e <i>vester</i> como <i>pulcher</i>, perdendo o <i>e</i> fora do nominativo masculino (<i>noster, nostra, nostrum</i>; <i>nostrī, nostrae</i>...).</p>
{tabela_declinacao('meus, mea, meum, "meu" · singular e plural', [
    ('me<b>us</b>', 'me<b>a</b>', 'me<b>um</b>', 'me<b>ī</b>', 'me<b>ae</b>', 'me<b>a</b>'),
    ('me<b>ī</b>', 'me<b>ae</b>', 'me<b>ī</b>', 'me<b>ōrum</b>', 'me<b>ārum</b>', 'me<b>ōrum</b>'),
    ('me<b>ō</b>', 'me<b>ae</b>', 'me<b>ō</b>', 'me<b>īs</b>', 'me<b>īs</b>', 'me<b>īs</b>'),
    ('me<b>um</b>', 'me<b>am</b>', 'me<b>um</b>', 'me<b>ōs</b>', 'me<b>ās</b>', 'me<b>a</b>'),
    ('<b>mī</b>', 'me<b>a</b>', 'me<b>um</b>', 'me<b>ī</b>', 'me<b>ae</b>', 'me<b>a</b>'),
    ('me<b>ō</b>', 'me<b>ā</b>', 'me<b>ō</b>', 'me<b>īs</b>', 'me<b>īs</b>', 'me<b>īs</b>')],
    colunas=('m. sing.', 'f. sing.', 'n. sing.', 'm. pl.', 'f. pl.', 'n. pl.'))}
<p>A única forma inesperada é o <b>vocativo masculino singular <i>mī</i></b>, e não "mee": <i>mī fīlī</i>, "meu filho!"; <i>mī amīce</i>, "meu amigo!". Os outros possessivos praticamente não têm vocativo, porque raramente se chama alguém de "teu" ou "seu"; a exceção é <i>noster</i>, cujo vocativo é igual ao nominativo. Cuidado ainda com <i>meī</i>, que pode ser o genitivo de <i>ego</i> ("de mim") ou uma forma de <i>meus</i> (genitivo singular, nominativo ou vocativo plural); decide o nome com que <i>meus</i> concordaria: <i>amīcī meī</i>, "meus amigos" ou "do meu amigo".</p>
<h3>O possessivo concorda com a coisa, não com o dono</h3>
<p>Como todo adjetivo, o possessivo toma o <b>gênero, o número e o caso do nome a que se refere</b>, isto é, da coisa possuída. A pessoa do possuidor só escolhe qual possessivo usar (<i>meus</i> ou <i>tuus</i>). O português faz o mesmo ("minha rosa", diga-o um homem ou uma mulher), mas o latim exige atenção porque o possessivo também precisa do caso certo:</p>
{exemplos([('Iūlia: "Liber <b>meus</b> in mēnsā est."', 'Júlia: "O meu livro está na mesa." (<i>meus</i>, masculino, por causa de <i>liber</i>, embora quem fala seja uma mulher)'), ('Mārcus rosam <b>tuam</b> spectat.', 'Marco olha a tua rosa (a sua rosa, de você).'), ('Magister cum discipulīs <b>nostrīs</b> ambulat.', 'O professor passeia com os nossos alunos. (ablativo plural, como <i>discipulīs</i>)'), ('Dōna <b>vestra</b> pulchra sunt.', 'Os presentes de vocês são belos. (neutro plural)')])}
<p>Daí também a regra de que o latim <b>não</b> usa o genitivo dos pessoais para indicar posse: "o nosso pai" é <i>pater noster</i>, nunca <i>pater nostrī</i> ou <i>pater nostrum</i>. E, como o latim não tem artigo, o possessivo costuma ser <b>omitido</b> quando o sentido já é claro: <i>Mārcus patrem amat</i> é, normalmente, "Marco ama <i>o seu</i> pai". O possessivo aparece quando há risco de confusão, e então costuma vir depois do nome (<i>pater meus</i>); vem antes quando há ênfase ou contraste (<i>meus pater</i>, "o <i>meu</i> pai", não o seu).</p>
'''),
        ('Suus ou eius? A armadilha do "seu"', f'''
<p>Em português, "seu" é uma das palavras mais ambíguas da língua. "Pedro visitou Paulo e sua irmã": a irmã é de Pedro ou de Paulo? E no Brasil "seu" quer dizer, quase sempre, "de você" ("o seu livro está aqui"). O latim não admite essa ambiguidade, e ao traduzir "seu" você precisa decidir entre três palavras:</p>
{comparacao('As três traduções do "seu" português', ['Latim', 'Quando se usa', 'Exemplo'], [
    ['<b>tuus, -a, -um</b> (vester)', '"seu" = de você (de vocês)', '<i>Liber tuus hīc est.</i> O seu livro (de você) está aqui. (<i>hīc</i>, aqui)'],
    ['<b>suus, -a, -um</b>', '"seu" = do próprio sujeito da oração (reflexivo)', '<i>Mārcus librum suum legit.</i> Marco lê o seu (próprio) livro.'],
    ['<b>eius</b> (sing.) · <b>eōrum, eārum</b> (pl.)', '"seu" = dele, dela, deles, delas: de outra pessoa que não o sujeito', '<i>Mārcus librum eius legit.</i> Marco lê o livro dele (de outro).'],
])}
<p>A regra decisiva é a do reflexivo: <b><i>suus</i> se refere ao sujeito</b> da oração, exatamente como <i>sē</i>. É um adjetivo, e por isso concorda com a coisa possuída (<i>librum suum</i>, <i>rosam suam</i>, <i>dōna sua</i>). <b><i>Eius</i></b>, ao contrário, não é adjetivo: é o <b>genitivo de <i>is</i></b>, "dele, dela", e por isso <b>não varia</b> com a coisa possuída, só com o possuidor: <i>eius</i> para um possuidor (homem ou mulher), <i>eōrum</i> para vários possuidores masculinos (ou neutros), <i>eārum</i> para várias possuidoras.</p>
{diagrama_frase([('Puella', 'nominativo · sujeito'), ('frātrem suum', 'acusativo · suum: da menina'), ('et amīcum eius', 'acusativo · eius: do irmão'), ('laudat', 'verbo · elogia')],
    'Duas posses, duas palavras: <i>Puella frātrem suum et amīcum eius laudat</i> = A menina elogia o seu (próprio) irmão e o amigo dele (do irmão). <i>Suum</i> aponta para o sujeito; <i>eius</i>, para alguém que não é o sujeito.')}
<p>Note três consequências. Primeiro, <b><i>suus</i> concorda com a coisa, não com o possuidor</b>: "Júlia lê o seu livro" é <i>Iūlia librum <b>suum</b> legit</i>, masculino, embora Júlia seja mulher, porque <i>liber</i> é masculino. Segundo, o número do possuidor não muda <i>suus</i>: "os meninos amam o seu cavalo" é <i>puerī equum suum amant</i>, com <i>suum</i> no singular, porque o cavalo é um só. Terceiro, quando o possuidor foi mencionado em <b>outra oração</b> e não é o sujeito daquela em que está a coisa possuída, use <i>eius</i>: <i>Mārcus in hortō est; amīcus <b>eius</b> librum legit</i>, "Marco está no jardim; o amigo dele lê um livro" (<i>suus</i> aqui apontaria para <i>amīcus</i>, sujeito de <i>legit</i>).</p>
{comparacao('suus × eius, lado a lado', ['Latim', 'Tradução', 'Por quê'], [
    ['Pater fīliōs <b>suōs</b> amat.', 'O pai ama os seus (próprios) filhos.', '<i>suōs</i>: possuidor = sujeito (<i>pater</i>); acusativo plural, como <i>fīliōs</i>'],
    ['Pater fīliōs <b>eius</b> amat.', 'O pai ama os filhos dele (de outro homem).', '<i>eius</i>: possuidor ≠ sujeito; invariável'],
    ['Mātrēs fīliās <b>suās</b> vocant.', 'As mães chamam as suas (próprias) filhas.', 'possuidor = sujeito; <i>suās</i> concorda com <i>fīliās</i>'],
    ['Mātrēs fīliās <b>eārum</b> vocant.', 'As mães chamam as filhas delas (de outras mulheres).', '<i>eārum</i>: várias possuidoras, que não são o sujeito'],
    ['Iūlia et frāter <b>eius</b> veniunt.', 'Júlia e o irmão dela vêm.', '<i>frāter eius</i> é parte do sujeito, e não complemento dele: não pode ser <i>suus</i>'],
])}
{observacao('Uma regra com poucas exceções', 'A regra "<i>suus</i> = sujeito" vale para a imensa maioria das frases que você vai ler. As gramáticas registram usos especiais: <i>suus</i> pode apontar para um complemento quando o contexto não deixa dúvida, sobretudo com o sentido de "seu próprio" (<i>Hannibalem suī cīvēs ē cīvitāte ēiēcērunt</i>, "os seus próprios concidadãos expulsaram Aníbal da cidade", exemplo de Bennett § 244.4); e numa oração subordinada <i>sē</i> e <i>suus</i> podem apontar para o sujeito da oração principal (o "reflexivo indireto"), uso que você estudará com a oração infinitiva, no capítulo 28. Por enquanto, aplique a regra básica.')}
'''),
        ('Análise gramatical: uma frase do Evangelho de João', f'''
<p>No capítulo 10 do Evangelho de João, Jesus se compara a um pastor. A frase reúne quase tudo deste capítulo: um pronome sujeito expresso, que você agora sabe que tem um motivo, e duas formas do possessivo reflexivo.</p>
{exemplos([('Ego sum pāstor bonus. Bonus pāstor animam suam dat prō ovibus suīs.', 'Eu sou o bom pastor. O bom pastor dá a sua vida pelas suas ovelhas. (Jo 10,11, Vulgata Clementina; macrons acrescentados)')])}
<p>Vocabulário: <i>pāstor, -ōris</i> (m.), pastor, da 3ª declinação, como <i>victor</i> (capítulo 9); <i>anima, -ae</i> (f.), alma, vida; <i>prō</i>, preposição com ablativo, "em favor de, por"; <i>ovis, ovis</i> (f.), ovelha, da 3ª declinação, tema em <i>-i</i> (capítulo 10). <i>Dat</i> é a 3ª pessoa do singular do presente de <i>dō, dare</i>, "dar".</p>
{analise('Jo 10,11, palavra a palavra', [
    ('Ego', 'ego, meī, pronome pessoal da 1ª pessoa', 'nominativo singular', 'sujeito de <i>sum</i>, expresso por ênfase: "eu (e não outro)"'),
    ('sum', 'sum, esse, ser', 'presente, 1ª pessoa do singular', 'cópula; a terminação já diria "eu"'),
    ('pāstor', 'pāstor, -ōris (m.), pastor', 'nominativo singular, 3ª declinação', 'predicativo do sujeito, no nominativo como <i>ego</i>'),
    ('bonus', 'bonus, -a, -um, bom', 'nominativo singular masculino', 'atributo de <i>pāstor</i>'),
    ('Bonus pāstor', 'bonus · pāstor', 'nominativo singular masculino', 'sujeito de <i>dat</i>'),
    ('animam', 'anima, -ae (f.), vida, alma', 'acusativo singular, 1ª declinação', 'objeto direto de <i>dat</i>'),
    ('suam', 'suus, -a, -um, possessivo reflexivo', 'acusativo singular feminino, concordando com <i>animam</i>', '"a sua (própria)": a vida do sujeito, o pastor'),
    ('dat', 'dō, dare, dar', 'presente, 3ª pessoa do singular', 'verbo da segunda oração'),
    ('prō', 'prō (preposição + ablativo), em favor de, por', 'invariável', 'introduz o beneficiário'),
    ('ovibus', 'ovis, ovis (f.), ovelha', 'ablativo plural, 3ª declinação', 'com <i>prō</i>: "pelas ovelhas"'),
    ('suīs', 'suus, -a, -um', 'ablativo plural feminino, concordando com <i>ovibus</i>', '"suas": as ovelhas do sujeito, o pastor'),
])}
<p>Três observações. Primeiro, <i>Ego</i>: <i>sum</i> sozinho já diria "eu sou"; o pronome está lá para destacar a pessoa, e o versículo seguinte (Jo 10,12) confirma o contraste, falando do mercenário, "que não é pastor". Segundo, <i>suam</i> e <i>suīs</i>: os dois apontam para o sujeito da oração, <i>bonus pāstor</i>, e por isso são reflexivos; se a vida ou as ovelhas fossem de outra pessoa, o texto diria <i>eius</i>. Terceiro, a concordância: <i>suam</i> é feminino singular porque <i>anima</i> é feminino singular, e <i>suīs</i> é ablativo plural feminino porque <i>ovibus</i> o é; nada disso depende do pastor, que é masculino e singular. A tradução portuguesa "a sua vida pelas suas ovelhas" é, por acaso, inequívoca; em muitas outras frases o "seu" português será ambíguo e o latim não.</p>
<h3>Resumo</h3>
<ul>
<li><i>ego, meī, mihi, mē, mē</i>; <i>tū, tuī, tibi, tē, tū, tē</i>; <i>nōs, nostrum/nostrī, nōbīs, nōs, nōbīs</i>; <i>vōs, vestrum/vestrī, vōbīs, vōs, vōs, vōbīs</i>. <i>Nostrum, vestrum</i> = partitivos ("de nós", dentre nós); <i>meī, tuī, nostrī, vestrī</i> = objetivos.</li>
<li><i>Cum</i> se cola ao pronome: <i>mēcum, tēcum, sēcum, nōbīscum, vōbīscum</i>.</li>
<li>O pronome sujeito fica implícito no verbo; aparece só por ênfase ou contraste.</li>
<li>3ª pessoa: <i>is, ea, id</i> ("ele, ela; o, a; lhe"); reflexivo <i>suī, sibi, sē, sē</i>, sem nominativo, para o próprio sujeito. Na 1ª e 2ª pessoa, <i>mē, tē, nōs, vōs</i> servem de reflexivos.</li>
<li>Possessivos: <i>meus</i> (vocativo <i>mī</i>), <i>tuus</i>, <i>suus</i> como <i>bonus</i>; <i>noster</i>, <i>vester</i> como <i>pulcher</i>. Concordam com a coisa possuída.</li>
<li>"Seu": <i>tuus</i> (de você), <i>suus</i> (do sujeito), <i>eius/eōrum/eārum</i> (de outro; invariável com a coisa possuída).</li>
</ul>
<p>No próximo capítulo, <i>is, ea, id</i> volta ao lado dos outros demonstrativos (<i>hīc, ille, iste</i>) e de <i>ipse</i> e <i>īdem</i>.</p>
'''),
    ],
    erros_comuns=[
        ('Pôr <i>ego</i> e <i>tū</i> em todas as frases: <i>Ego librum legō</i>, <i>Tū in hortō ambulās</i>.', 'A terminação já diz a pessoa; o pronome expresso indica ênfase ou contraste. Sem contraste, escreva <i>Librum legō</i>, <i>In hortō ambulās</i>. Use o pronome quando o português o destacaria: "<i>eu</i> leio, <i>tu</i> não".'),
        ('Traduzir todo "seu" por <i>suus</i>: "Pedro visita Paulo e a sua irmã" → <i>Petrus Paulum et sorōrem suam vīsitat</i> (<i>vīsitat</i>, visita), querendo dizer a irmã de Paulo.', '<i>Suus</i> só aponta para o sujeito (aqui, Pedro). Para a irmã de Paulo, use <i>eius</i>: <i>Petrus Paulum et sorōrem eius vīsitat</i>. E se "seu" quer dizer "de você", a palavra é <i>tuus</i>. Antes de traduzir, pergunte: de quem é a coisa?'),
        ('Fazer o possessivo concordar com o possuidor: Júlia diz <i>liber mea</i>; "os meninos amam seu cavalo" → <i>equum suōs</i>.', 'O possessivo é um adjetivo e concorda com a coisa possuída: <i>liber meus</i> (porque <i>liber</i> é masculino), <i>equum suum</i> (porque o cavalo é um só). O possuidor escolhe só a pessoa do possessivo.'),
        ('Usar o genitivo do pessoal para a posse: <i>pater nostrī</i>, <i>liber meī</i>.', 'A posse se exprime pelo possessivo: <i>pater noster</i>, <i>liber meus</i>. <i>Meī, tuī, nostrī, vestrī</i> são genitivos objetivos ("o amor por nós", <i>amor nostrī</i>), e <i>nostrum, vestrum</i> são partitivos ("um de nós", <i>ūnus nostrum</i>).'),
        ('Escrever <i>cum mē</i>, <i>cum tē</i>, <i>cum nōbīs</i>.', 'Com os pessoais e o reflexivo, <i>cum</i> vem depois e se cola ao pronome: <i>mēcum, tēcum, sēcum, nōbīscum, vōbīscum</i>. O português conserva a ideia em "comigo", "contigo", "consigo".'),
        ('Usar <i>sē</i> para a 1ª ou a 2ª pessoa (<i>Nōs sē laudāmus</i>), ou <i>eum</i> quando o objeto é o próprio sujeito (<i>Mārcus eum laudat</i> para "Marco se elogia").', '<i>Sē</i> é só de 3ª pessoa e só para o próprio sujeito: <i>Mārcus sē laudat</i>. Na 1ª e na 2ª pessoa os reflexivos são os próprios pessoais: <i>Nōs laudāmus</i> (com <i>nōs</i> objeto: nós nos elogiamos), <i>Mē laudō</i>. <i>Mārcus eum laudat</i> quer dizer que Marco elogia outra pessoa.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · De quem é o livro?',
            'Leia, analise e traduza: <i lang="la">Mārcus et Iūlia in hortō sunt. Mārcus librum suum legit; Iūlia librum eius spectat et sēcum portat.</i> Vocabulário: <i>portat</i>, leva; os demais termos estão no capítulo e nos capítulos 5 e 6.', [
            ('Na segunda frase, qual é o sujeito de <i>legit</i>, e para quem aponta <i>suum</i>?', 'O sujeito é <i>Mārcus</i> (nominativo singular; <i>legit</i> é 3ª do singular). <i>Suum</i> é reflexivo e aponta para o sujeito da sua oração: o livro é de Marco. "Marco lê o seu (próprio) livro."'),
            ('Na oração seguinte, por que <i>eius</i> e não <i>suum</i>?', 'O sujeito de <i>spectat</i> é <i>Iūlia</i>. Se o texto dissesse <i>librum suum</i>, o livro seria de Júlia. <i>Eius</i>, "dele/dela", indica um possuidor que não é o sujeito; pelo contexto, Marco. "Júlia olha o livro dele."'),
            ('E <i>sēcum</i>?', 'Ablativo do reflexivo com <i>cum</i> colado: "consigo". Como é reflexivo, aponta para o sujeito de <i>portat</i>, que continua sendo Júlia. "...e o leva consigo." Repare que o latim não repete o objeto (<i>librum</i>) com o segundo verbo: o português acrescenta "o".'),
            ('Monte a tradução.', '"Marco e Júlia estão no jardim. Marco lê o seu livro; Júlia olha o livro dele e o leva consigo." Em português, "o seu livro" e "o livro dele" só ficam claros pela escolha das palavras; em latim, <i>suum</i> e <i>eius</i> não deixam dúvida.'),
        ]),
        pratica_guiada('Prática guiada 2 · Retroversão com pronomes',
            'Passe para o latim: "Nós vamos com você ao templo e damos os nossos presentes ao seu amigo." ("Seu" = de você.) Vocabulário: <i>veniō, -īre</i>, vir, ir; <i>ad</i> + acusativo, a, para; <i>dō, dare</i>, dar (<i>damus</i>, damos).', [
            ('Precisa de <i>nōs</i> como sujeito?', 'Não: a terminação <i>-mus</i> de <i>venīmus</i> e <i>damus</i> já diz "nós", e não há contraste com outra pessoa. O latim natural é sem pronome.'),
            ('Como dizer "com você"?', 'Ablativo de <i>tū</i> com <i>cum</i> colado: <i>tēcum</i>. Nunca <i>cum tē</i>.'),
            ('"Os nossos presentes": que forma?', '<i>Dōna nostra</i>: acusativo plural neutro, concordando com <i>dōna</i> (de <i>dōnum</i>, neutro). O possessivo acompanha a coisa, não "nós".'),
            ('"Ao seu amigo", com "seu" = de você: <i>suō</i> ou <i>tuō</i>?', '<i>Tuō</i>. O amigo é da pessoa com quem se fala (2ª pessoa), não do sujeito ("nós"). <i>Suō</i> estaria errado duas vezes: é de 3ª pessoa e aponta para o sujeito. Dativo singular masculino: <i>amīcō tuō</i>.'),
            ('Monte a frase.', '<i>Tēcum ad templum venīmus et dōna nostra amīcō tuō damus.</i> (Também se pode começar por <i>Ad templum tēcum venīmus</i>; a ordem é livre.)'),
        ], 'Conclusão: antes de escrever um pronome ou um possessivo, faça duas perguntas. Que pessoa é (1ª, 2ª, 3ª)? E, se for 3ª, é o próprio sujeito (<i>sē, suus</i>) ou outra pessoa (<i>is, eius</i>)?'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Identifique o pronome', 'Diga a pessoa, o caso e o número da palavra destacada e sua função na frase.', [
            ('<i>Magister <b>nōbīs</b> librōs dat.</i>', '1ª pessoa do plural, dativo: destinatário de <i>dat</i>. "O professor nos dá livros." <i>Nōbīs</i> também poderia ser ablativo, mas não há preposição e "dar" pede "a quem".'),
            ('<i><b>Nōs</b> magister laudat.</i>', '1ª pessoa do plural, acusativo: objeto direto. "O professor nos elogia." Não é nominativo: o sujeito é <i>magister</i>, e o verbo está na 3ª do singular, não em <i>-mus</i>.'),
            ('<i>Iūlia <b>mēcum</b> venit.</i>', '1ª pessoa do singular, ablativo com <i>cum</i>: companhia. "Júlia vem comigo."'),
            ('<i>Mārcus <b>sibi</b> librum capit.</i>', 'Reflexivo de 3ª pessoa, dativo: "para si". Aponta para o sujeito, Marco. "Marco pega um livro para si."'),
            ('<i>Puer <b>eam</b> videt.</i>', '<i>Is, ea, id</i> usado como pronome de 3ª pessoa, acusativo singular feminino: objeto direto. "O menino a vê." É outra pessoa (feminina), não o sujeito.'),
            ('<i>Ūnus <b>vestrum</b> in templō est.</i>', '2ª pessoa do plural, genitivo partitivo: "um de vocês". "Um de vocês está no templo."'),
            ('<i><b>Tū</b>, Mārce, labōrās; ego dormiō.</i>', '2ª pessoa do singular, nominativo: sujeito de <i>labōrās</i>, expresso por contraste com <i>ego</i>. "Tu, Marco, trabalhas; eu durmo." (<i>Mārce</i> é vocativo; <i>tū</i> é sujeito, como mostra o verbo na 2ª pessoa.)'),
            ('<i>Puellae <b>sē</b> spectant.</i>', 'Reflexivo de 3ª pessoa, acusativo (aqui plural, como o sujeito): "As meninas se olham" (a si mesmas). Para "olham umas às outras" o latim prefere <i>inter sē</i>.'),
        ]),
        exercicio('Exercício 2 · Complete com o pronome ou o possessivo', 'Escreva a forma latina pedida entre parênteses e explique o caso.', [
            ('<i>Poēta ___ fābulam nārrat.</i> (a mim)', '<i>mihi</i>: dativo de <i>ego</i>, destinatário de <i>nārrat</i>.'),
            ('<i>Amīcī ___ exspectant.</i> (a ti, te)', '<i>tē</i>: acusativo de <i>tū</i>, objeto de <i>exspectant</i> (esperam).'),
            ('<i>Mārcus ___ ambulat.</i> (conosco)', '<i>nōbīscum</i>: ablativo de <i>nōs</i> com <i>cum</i> colado.'),
            ('<i>Puer ___ librum portat.</i> (o meu; <i>portat</i>, leva)', '<i>meum</i>: acusativo singular masculino, concordando com <i>librum</i>.'),
            ('<i>Agricola cum fīliīs ___ labōrat.</i> (os seus = do agricultor)', '<i>suīs</i>: ablativo plural masculino, concordando com <i>fīliīs</i>; reflexivo porque os filhos são do sujeito.'),
            ('<i>Salvē, ___ fīlī!</i> (meu)', '<i>mī</i>: vocativo singular masculino de <i>meus</i>, concordando com o vocativo <i>fīlī</i>.'),
            ('<i>Rēgīna ___ dōna dat.</i> (a eles)', '<i>eīs</i> (ou <i>iīs</i>): dativo plural de <i>is</i>, destinatário. Não <i>sibi</i>, porque eles não são o sujeito.'),
            ('<i>Templum ___ magnum est.</i> (nosso)', '<i>nostrum</i>: nominativo singular neutro de <i>noster</i>, concordando com <i>templum</i>. Aqui <i>nostrum</i> é o possessivo, não o genitivo partitivo de <i>nōs</i>: a forma é a mesma, a função decide.'),
        ]),
        exercicio('Exercício 3 · Suus ou eius?', 'Complete com a forma certa de <i>suus</i> ou com <i>eius/eōrum/eārum</i>, e explique de quem é a coisa.', [
            ('Marco ama a sua (própria) irmã. <i>Mārcus sorōrem ___ amat.</i>', '<i>suam</i>: a irmã é do sujeito; acusativo singular feminino, como <i>sorōrem</i>.'),
            ('Marco ama a irmã dele (de Paulo). <i>Mārcus Paulum et sorōrem ___ amat.</i>', '<i>eius</i>: a irmã é de Paulo, que não é o sujeito; <i>eius</i> é invariável.'),
            ('Os meninos levam os seus livros. <i>Puerī librōs ___ portant.</i>', '<i>suōs</i>: os livros são do sujeito; acusativo plural masculino, como <i>librōs</i>.'),
            ('As meninas estão no jardim; a mãe delas está no templo. <i>Puellae in hortō sunt; māter ___ in templō est.</i>', '<i>eārum</i>: o possuidor (as meninas) está em outra oração e não é o sujeito de <i>est</i>, que é <i>māter</i>; várias possuidoras femininas.'),
            ('O rei e os seus soldados vêm. <i>Rēx et mīlitēs ___ veniunt.</i>', '<i>eius</i>: <i>mīlitēs</i> é parte do sujeito, não complemento de um verbo cujo sujeito seja o rei; a posse se exprime por <i>eius</i>.'),
            ('A mãe dá um presente à sua filha. <i>Māter fīliae ___ dōnum dat.</i>', '<i>suae</i>: a filha é do sujeito (<i>māter</i>); dativo singular feminino, como <i>fīliae</i>.'),
        ]),
        exercicio('Exercício 4 · Mude a pessoa', 'Reescreva cada frase com o sujeito indicado, ajustando o verbo, o reflexivo e o possessivo.', [
            ('<i>Mārcus sē laudat.</i> → (ego)', '<i>Mē laudō.</i> Na 1ª pessoa o reflexivo é <i>mē</i>; o pronome sujeito fica implícito em <i>laudō</i>.'),
            ('<i>Mārcus sē laudat.</i> → (nōs)', '<i>Nōs laudāmus.</i> Aqui <i>nōs</i> é o objeto (acusativo, "nos"); o sujeito está em <i>-mus</i>. "Nós nos elogiamos."'),
            ('<i>Puella librum suum legit.</i> → (tū)', '<i>Librum tuum legis.</i> O reflexivo da 2ª pessoa é o próprio possessivo <i>tuus</i>.'),
            ('<i>Puella librum suum legit.</i> → (vōs)', '<i>Librum vestrum legitis.</i> Um só livro (de vocês): <i>vestrum</i>, acusativo singular masculino.'),
            ('<i>Agricola fīliōs suōs sēcum dūcit.</i> → (ego)', '<i>Fīliōs meōs mēcum dūcō.</i> "Levo meus filhos comigo."'),
            ('<i>Agricola fīliōs suōs sēcum dūcit.</i> → (agricolae)', '<i>Agricolae fīliōs suōs sēcum dūcunt.</i> <i>Suōs</i> e <i>sēcum</i> não mudam: o reflexivo não distingue número, e o possessivo concorda com <i>fīliōs</i>.'),
        ]),
        exercicio('Exercício 5 · Leia a Vulgata', 'Traduza e explique os pronomes. Textos da Vulgata Clementina (macrons acrescentados). Vocabulário dado em cada item.', [
            ('<i>Ego sum pāstor bonus: et cognōscō meās, et cognōscunt mē meae.</i> (Jo 10,14; <i>cognōscō</i>, conheço)', '"Eu sou o bom pastor: conheço as minhas, e as minhas me conhecem." <i>Meās</i> (acusativo) e <i>meae</i> (nominativo, sujeito de <i>cognōscunt</i>) são femininos plurais substantivados: subentende-se <i>ovēs</i>, as ovelhas. <i>Mē</i> é acusativo, objeto de <i>cognōscunt</i>. <i>Ego</i> é enfático, como no v. 11.'),
            ('<i>Pāx vōbīs. Sīcut mīsit mē Pater, et ego mittō vōs.</i> (Jo 20,21; <i>pāx, pācis</i>, paz; <i>sīcut</i>, assim como; <i>mīsit</i>, perfeito de <i>mittō</i>, enviou)', '"A paz (esteja) convosco. Assim como o Pai me enviou, também eu vos envio." <i>Vōbīs</i>: dativo ("a vocês"), com o verbo subentendido. <i>Mē</i> e <i>vōs</i>: acusativos, objetos. <i>Ego</i> é expresso para contrastar com <i>Pater</i>; <i>et</i> vale "também".'),
            ('<i>... ecce ego vōbīscum sum omnibus diēbus.</i> (Mt 28,20; <i>ecce</i>, eis; <i>omnibus diēbus</i>, todos os dias)', '"Eis que eu estou convosco todos os dias." <i>Vōbīscum</i>: ablativo com <i>cum</i> colado. <i>Ego</i> expresso por ênfase: é a promessa de uma presença pessoal.'),
            ('<i>Ave grātiā plēna: Dominus tēcum.</i> (Lc 1,28; <i>ave</i>, salve; <i>grātiā plēna</i>, cheia de graça)', '"Salve, cheia de graça: o Senhor (está) contigo." <i>Tēcum</i>: ablativo de <i>tū</i> com <i>cum</i>; o verbo <i>est</i> fica subentendido.'),
            ('<i>Dēdūxit mē super sēmitās iūstitiae propter nōmen suum.</i> (Sl 22,3 (23,3); <i>dēdūxit</i>, conduziu; <i>super sēmitās</i>, por sobre as veredas; <i>iūstitia</i>, justiça; <i>propter</i> + acusativo, por causa de; <i>nōmen</i>, nome)', '"Conduziu-me pelas veredas da justiça por causa do seu nome." O sujeito, implícito em <i>dēdūxit</i>, é o Senhor do v. 1 (<i>Dominus regit mē</i>, que você leu no capítulo 6). <i>Suum</i> é reflexivo: o nome é do sujeito, do Senhor, não de quem fala (que seria <i>meum</i>).'),
            ('<i>... nōn timēbō mala, quoniam tū mēcum es.</i> (Sl 22,4; <i>timēbō</i>, temerei, futuro de <i>timeō</i>; <i>mala</i>, males; <i>quoniam</i>, porque)', '"Não temerei males, porque tu estás comigo." <i>Tū</i> é expresso: o salmista passa de falar <i>do</i> Senhor (3ª pessoa nos vv. 1–3) a falar <i>com</i> ele, e o pronome marca essa virada. <i>Mēcum</i>: "comigo".'),
        ]),
        exercicio('Exercício 6 · Retroversão', 'Passe para o latim. Use o pronome sujeito só quando houver contraste. Vocabulário: o do capítulo e dos capítulos 5, 6 e 9; <i>exspectō, -āre</i>, esperar.', [
            ('Eu te vejo, mas tu não me vês.', '<i>Ego tē videō, sed tū mē nōn vidēs.</i> Os pronomes sujeito são necessários: a frase contrapõe as duas pessoas.'),
            ('O professor espera os seus alunos (os alunos dele próprio).', '<i>Magister discipulōs suōs exspectat.</i> <i>Suōs</i>: do sujeito; acusativo plural, como <i>discipulōs</i>.'),
            ('O professor está no templo; os alunos dele esperam no jardim.', '<i>Magister in templō est; discipulī eius in hortō exspectant.</i> <i>Eius</i>, porque o sujeito de <i>exspectant</i> são os alunos, não o professor.'),
            ('Júlia, a sua (de você) mãe está conosco.', '<i>Iūlia, māter tua nōbīscum est.</i> "Seu" = de você → <i>tuus</i>; <i>Iūlia</i> é vocativo, igual ao nominativo na 1ª declinação.'),
            ('Os meninos levam os livros consigo.', '<i>Puerī librōs sēcum portant.</i> <i>Sēcum</i>: reflexivo, com <i>cum</i> colado; o possessivo pode ficar subentendido.'),
            ('Meu amigo, nós amamos a nossa pátria.', '<i>Mī amīce, patriam nostram amāmus.</i> Vocativo <i>mī amīce</i> (de <i>meus</i> e <i>amīcus</i>); <i>nostram</i>, acusativo singular feminino, concorda com <i>patriam</i>, não com "nós"; sem <i>nōs</i>, porque não há contraste.'),
        ]),
    ],
    leituras=['orberg-colloquia-personarum', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'lhomond-epitome-historiae-sacrae', 'ravizza-gramatica-latina', 'bennett-new-latin-grammar'],
    leituras_nota='Os pronomes de 1ª e 2ª pessoa vivem no diálogo: os Colloquia Personarum de Ørberg, diálogos que acompanham os capítulos de Familia Romana, são o melhor lugar para vê-los, com mēcum e tēcum, e para notar como o pronome sujeito só aparece quando alguém se contrapõe a alguém. Nos capítulos de Familia Romana que você já leu, procure agora cada suus e cada eius e pergunte de quem é a coisa. No Epitome Historiae Sacrae de Lhomond, narrativa contínua em 3ª pessoa, a alternância entre sē/suus e eum/eius aparece com frequência. Na Vulgata, leia Jo 10,1–18 inteiro, de onde vêm a frase analisada e o exercício 5, e o Sl 22 (23 na numeração hebraica). Para consulta, Ravizza nn. 68–69 e 320 e Bennett §§ 84–86 e 242–245 têm os paradigmas e as regras.',
)
