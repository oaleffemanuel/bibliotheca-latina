from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='51-a-vulgata-marcos', titulo='A Vulgata: o Evangelho de Marcos',
    titulo_latim='Biblia Vulgāta', tempo='75 min',
    resumo='Leitura comentada de um episódio inteiro do Evangelho de Marcos na Vulgata Clementina, a tempestade acalmada (Mc 4,35–40): São Jerônimo e a história da Bíblia latina, o texto com tradução própria, vocabulário e notas versículo a versículo, análise palavra a palavra, o período com ita ut, e os traços do latim cristão estudados no capítulo 50 vistos em ação, com uma nota sobre as diferenças da Nova Vulgata.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['Vulgata', 'São Jerônimo', 'Vetus Latina', 'Vulgata Clementina e Nova Vulgata', 'Evangelho de Marcos', 'Marcos 4,35–40',
             'presente histórico', 'parataxe', 'quia declarativo e explicativo', 'ita ut consecutivo', 'cum com subjuntivo (antecipação)',
             'subjuntivo exortativo', 'depoente comminor com dativo', 'imperativo', 'quid = por quê', 'ablativo de mesma raiz (timuērunt timōre)',
             'ad alterutrum', 'leitura comentada', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 13 (o perfeito e as partes principais: o texto narra no passado, com perfeitos como <i>cessāvit</i> e <i>timuērunt</i>) e capítulo 50 (o que muda no latim cristão: o leitor vai reconhecer aqui <i>quia</i>, <i>ad</i> + acusativo, a parataxe). Algumas construções da Parte III aparecem no texto (o particípio, o subjuntivo depois de <i>cum</i> e de <i>ita ut</i>, o perfeito dos depoentes); as notas as explicam e indicam o capítulo próprio.',
                       licoes=['13-o-perfeito-e-as-partes-principais', '50-latim-cristao-e-medieval']),
    referencias=[
        referencia('Biblia Sacra Vulgata (editio Clementina): Marcos 4,35–40; 1,9–11; 10,13–16', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Marcum', nota='texto lido no capítulo, conferido na Wikisource latina (Evangelium Secundum Mārcum, caps. 1, 4 e 10). Ortografia adaptada (ae por æ, oe por œ, i por j) e macrons acrescentados; pontuação da edição, com dois-pontos e ponto e vírgula ajustados ao uso português', tipo='dominio_publico'),
        referencia('Nova Vulgata Bibliorum Sacrorum Editio: Evangelium secundum Mārcum 4,35–41', None, url='https://www.vatican.va/archive/bible/nova_vulgata/documents/nova-vulgata_nt_evang-marcum_lt.html', nota='usada só para a comparação da seção 6; texto conferido no site da Santa Sé', tipo='site'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 512 (a Bíblia latina: versões pré-jeronimianas; a obra de São Jerônimo e, na nota 1, a revisão dos Evangelhos em 383 por encargo do papa Dâmaso; o nome "vulgata", nota 2; o latim popular das versões, a parataxe e quod/quia/quoniam no discurso indireto, item 10)', tipo='dominio_publico'),
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='Introdução, § 3.f (Jerônimo entre os autores do latim tardio); § 176.3.a (quid adverbial, "por quê?"); § 176.4 (acusativo de mesma raiz, "cognato"); § 187.II.a (dativo com verbos de ameaçar e obedecer); § 259.3 (presente histórico); § 274 (subjuntivo exortativo); § 276 (proibição com nē + subjuntivo); § 284 (orações consecutivas com ut, ita…ut); § 288.1.B (cum com subjuntivo: a situação ou as circunstâncias)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 97.a (diēs às vezes feminino no singular, para um tempo marcado); § 439 (subjuntivo exortativo); § 469 (presente histórico na narração viva); § 537 (consecutivas com ut, ut nōn); § 546 (cum com imperfeito ou mais-que-perfeito do subjuntivo: as circunstâncias)', tipo='dominio_publico'),
    ],
    objetivos=[
        'Situar a Vulgata na história da Bíblia latina (versões antigas, São Jerônimo, Vulgata Clementina, Nova Vulgata).',
        'Ler e traduzir Marcos 4,35–40, explicando cada forma verbal e cada construção.',
        'Reconhecer no texto os traços do latim cristão do capítulo 50: parataxe, <i>quia</i>, <i>ad</i> + acusativo, ablativo de mesma raiz.',
        'Identificar o presente histórico e traduzi-lo de modo natural.',
        'Analisar palavra a palavra um versículo e explicar a estrutura de um período com <i>ita ut</i>.',
    ],
    secoes=[
        ('São Jerônimo, a Vulgata e Marcos', f'''
<p>Os primeiros cristãos do Ocidente leram a Bíblia em grego, a língua do Novo Testamento e da tradução judaica do Antigo feita em Alexandria. Mas nas províncias latinas, e entre o povo, o grego era pouco conhecido, e já no século II circulavam traduções latinas parciais, feitas por anônimos num latim popular e muito literal. Hoje são chamadas, em conjunto, de <i>Vetus Latina</i> ("a antiga latina"). O Pe. Ravizza conta essa história na sua <i>Gramática</i> e observa que o nome <i>vulgāta</i> ("divulgada, comum") se aplicava primeiro a esses textos antigos e só depois passou à tradução de Jerônimo (n. 512, itens 1–2 e nota 2).</p>
<p>Jerônimo (c. 340–420), que Bennett inclui entre os autores representativos do latim tardio (Introdução, § 3.f), recebeu em 383 do papa Dâmaso o encargo de revisar a Bíblia latina. Nos Evangelhos ele não traduziu do zero: corrigiu as versões antigas à luz do grego, para torná-las mais exatas e menos ásperas aos ouvidos cultos. O Antigo Testamento, ao contrário, ele o traduziu em grande parte do hebraico, que aprendeu na Palestina (Ravizza n. 512, nota 1). Ravizza insiste num ponto: Jerônimo eliminou muitos barbarismos de flexão, mas manteve deliberadamente o tom popular, porque o Evangelho não era "privilégio de raça ou de academia" (n. 512, item 5). O texto que você vai ler é, portanto, latim correto na morfologia e popular na sintaxe e no estilo.</p>
<p>Ao longo da Idade Média a Vulgata foi copiada à mão em milhares de manuscritos, com variantes. A edição oficial da Igreja Católica, promulgada pelo papa Clemente VIII em 1592, é a <b>Vulgata Clementina</b>, usada até 1979, quando foi substituída pela <b>Nova Vulgata</b>, uma revisão feita sobre os textos gregos e hebraicos modernos. Este livro lê a Clementina, que é de domínio público e está transcrita na Wikisource latina; a seção 6 mostra as pequenas diferenças da Nova Vulgata neste trecho.</p>
<p>O <b>Evangelho de Marcos</b> é o mais curto dos quatro e o de narração mais viva: frases curtas ligadas por "e", verbos no presente no meio de um relato no passado, pormenores concretos (a almofada na popa, os outros barcos). O episódio escolhido, a tempestade acalmada (Mc 4,35–40), tem começo, meio e fim em seis versículos e reúne quase todos os traços do latim cristão do capítulo 50.</p>
{observacao('Numeração dos versículos', 'Na Vulgata Clementina o episódio vai de 4,35 a 4,40: a pergunta de Jesus e a reação dos discípulos estão no mesmo versículo 40. As Bíblias modernas, inclusive a Nova Vulgata, dividem esse versículo em dois (40 e 41). Se você conferir o texto numa Bíblia em português, procure Marcos 4,35–41.')}
'''),
        ('O texto: Marcos 4,35–40', f'''
<p>O texto vem abaixo versículo a versículo, com o latim de um lado e a tradução do outro. Leia primeiro só o latim, em voz alta (na pronúncia eclesiástica do capítulo 1, se preferir), cobrindo a tradução e tentando seguir a ação; use as notas da seção 3 quando travar; só então confira a tradução.</p>
{exemplos([
    ('<sup>35</sup> Et ait illīs in illā diē, cum sērō esset factum: Trānseāmus contrā.', 'E naquele dia, quando já anoitecia, disse-lhes: "Passemos para a outra margem."'),
    ('<sup>36</sup> Et dīmittentēs turbam, assūmunt eum ita ut erat in nāvī; et aliae nāvēs erant cum illō.', 'E eles, deixando a multidão, levam-no assim como estava, no barco; e havia outros barcos com ele.'),
    ('<sup>37</sup> Et facta est procella magna ventī, et flūctus mittēbat in nāvim, ita ut implērētur nāvis.', 'E levantou-se uma grande tempestade de vento, e as ondas se lançavam para dentro do barco, de modo que o barco se enchia.'),
    ('<sup>38</sup> Et erat ipse in puppī super cervīcal dormiēns; et excitant eum, et dīcunt illī: Magister, nōn ad tē pertinet, quia perīmus?', 'E ele estava na popa, dormindo sobre uma almofada. E acordam-no e lhe dizem: "Mestre, não te importa que estejamos perecendo?"'),
    ('<sup>39</sup> Et exsurgēns comminātus est ventō, et dīxit marī: Tacē, obmūtēsce. Et cessāvit ventus, et facta est tranquillitās magna.', 'E ele, levantando-se, repreendeu o vento e disse ao mar: "Cala-te, emudece!" E o vento parou, e fez-se uma grande calmaria.'),
    ('<sup>40</sup> Et ait illīs: Quid timidī estis? necdum habētis fidem? Et timuērunt timōre magnō, et dīcēbant ad alterutrum: Quis, putās, est iste, quia et ventus et mare obēdiunt eī?', 'E disse-lhes: "Por que sois tão medrosos? Ainda não tendes fé?" E eles tiveram um grande medo e diziam uns aos outros: "Quem é este, afinal, que até o vento e o mar lhe obedecem?"'),
])}
<p>Fonte: Vulgata Clementina, Marcos 4,35–40, no texto da Wikisource latina, com ortografia adaptada (<i>ae</i> por <i>æ</i>, <i>i</i> por <i>j</i>) e macrons acrescentados. A tradução é deste livro.</p>
<p>A tradução procura mostrar a construção latina sem ficar ilegível. Duas escolhas merecem explicação. Os presentes <i>assūmunt</i>, <i>excitant</i>, <i>dīcunt</i> foram mantidos no presente ("levam-no", "acordam-no"), como no latim e no grego de Marcos; em português eles soam tão vivos quanto no original (seção 4). E <i>timuērunt timōre magnō</i>, literalmente "temeram com grande temor", virou "tiveram um grande medo", porque a repetição, natural em hebraico e em grego bíblico, pesa em português. (O grego de Marcos tem aqui o acusativo, <i>ephobḗthēsan phóbon mégan</i>; o tradutor latino preferiu o ablativo.)</p>
'''),
        ('Vocabulário e notas', f'''
{tabela(['Versículo', 'Palavra ou expressão', 'Nota'], [
    ['35', '<i>ait</i>', 'de <i>aiō</i>, verbo defectivo, "dizer"; <i>ait</i> é presente, mas faz as vezes de perfeito ("diz", "disse"; L&amp;S, s.v. <i>aiō</i>). Aqui, "disse".'],
    ['35', '<i>in illā diē</i>', '<i>diēs</i>, em geral masculino, aparece às vezes no feminino singular, sobretudo para um tempo marcado (A&amp;G § 97.a): "naquele dia". <i>Illā</i> ainda é demonstrativo pleno.'],
    ['35', '<i>cum sērō esset factum</i>', '<i>sērō</i>, advérbio, "tarde"; <i>factum esset</i>, mais-que-perfeito do subjuntivo de <i>fīō</i>, "tinha-se feito". <i>Cum</i> + subjuntivo descreve a circunstância (capítulo 34): "quando já se fazia tarde".'],
    ['35', '<i>Trānseāmus contrā</i>', '<i>trānseō, -īre</i>, atravessar (composto de <i>eō</i>, capítulo 26); <i>trānseāmus</i>, presente do subjuntivo, 1ª pl.: exortativo, "passemos" (capítulo 32). <i>Contrā</i>, advérbio: "para o lado oposto".'],
    ['36', '<i>dīmittentēs turbam</i>', '<i>dīmittō, -ere</i>, despedir, deixar ir; <i>dīmittentēs</i>, particípio presente, nominativo plural (capítulo 29): "deixando". O sujeito são os discípulos, implícitos.'],
    ['36', '<i>assūmunt eum ita ut erat in nāvī</i>', '<i>assūmō, -ere</i>, tomar consigo; presente histórico. <i>Ita ut erat</i>, "assim como estava": aqui <i>ut</i> com indicativo é comparativo, não consecutivo. <i>Nāvis, -is</i> (f.), barco, tema em <i>-i</i>: ablativo <i>nāvī</i> (capítulo 10).'],
    ['37', '<i>facta est procella magna ventī</i>', '<i>facta est</i>, perfeito de <i>fīō</i>, "fez-se, surgiu" (capítulos 24 e 26); <i>procella, -ae</i>, tempestade; <i>ventī</i>, genitivo: "tempestade de vento".'],
    ['37', '<i>flūctus mittēbat in nāvim</i>', '<i>flūctus, -ūs</i> (m., 4ª decl.), onda; <i>mittēbat</i>, imperfeito, "lançava(-se)". <i>Flūctus</i> pode ser nominativo singular ("a vaga", sentido coletivo) ou plural ("as ondas") com o verbo no singular, decalque do grego de Marcos, que tem <i>ta kýmata epéballen</i>, sujeito neutro plural com verbo no singular, construção normal em grego. A seção 6 volta ao ponto. <i>In nāvim</i>, <i>in</i> + acusativo (movimento), com o acusativo em <i>-im</i> dos temas em <i>-i</i>.'],
    ['37', '<i>ita ut implērētur nāvis</i>', '<i>impleō, -ēre</i>, encher; <i>implērētur</i>, imperfeito do subjuntivo passivo: "de modo que o barco se enchia". Oração consecutiva (capítulo 33).'],
    ['38', '<i>in puppī super cervīcal</i>', '<i>puppis, -is</i> (f.), popa, ablativo em <i>-ī</i>; <i>cervīcal, -ālis</i> (n.), travesseiro, almofada (de <i>cervīx</i>, nuca); <i>super</i> + acusativo, "sobre".'],
    ['38', '<i>excitant… dīcunt</i>', 'presentes históricos: "acordam… dizem".'],
    ['38', '<i>nōn ad tē pertinet, quia perīmus?</i>', '<i>pertineō ad</i>, dizer respeito a, importar a. <i>Quia</i> declarativo (capítulo 50): "que". <i>Perīmus</i>, presente de <i>pereō</i>, "perecer": "estamos perecendo".'],
    ['39', '<i>exsurgēns comminātus est ventō</i>', '<i>exsurgō, -ere</i>, levantar-se; particípio presente. <i>Comminor, -ārī, comminātus sum</i>, depoente, "ameaçar, repreender" (capítulo 25), com dativo, como os verbos de ameaçar (Bennett § 187.II.a).'],
    ['39', '<i>Tacē, obmūtēsce</i>', 'imperativos de <i>taceō, -ēre</i>, calar-se, e <i>obmūtēscō, -ere</i>, emudecer (capítulo 22).'],
    ['39', '<i>tranquillitās, -ātis</i>', '(f.) calmaria, bonança.'],
    ['40', '<i>Quid timidī estis?</i>', '<i>quid</i>, acusativo neutro usado como advérbio: "por quê?" (Bennett § 176.3.a); <i>timidus</i>, medroso.'],
    ['40', '<i>necdum</i>', '"e ainda não", "ainda não".'],
    ['40', '<i>timuērunt timōre magnō</i>', 'verbo e substantivo da mesma raiz, um torneio bíblico; ver seção 6.'],
    ['40', '<i>ad alterutrum</i>', '"uns aos outros"; <i>ad</i> + acusativo no lugar do dativo (capítulo 50).'],
    ['40', '<i>Quis, putās, est iste</i>', '<i>putās</i>, "pensas tu", intercalado na pergunta, como o nosso "afinal", "será". <i>Iste</i>: "este (homem)".'],
    ['40', '<i>quia… obēdiunt eī</i>', '<i>quia</i>: "visto que, já que", explicando a pergunta. <i>Obēdiō, -īre</i> (de <i>ob</i> + <i>audiō</i>), obedecer, com dativo (<i>eī</i>, "a ele").'],
], 'Marcos 4,35–40: vocabulário e notas, versículo a versículo')}
'''),
        ('Lendo a tempestade: versículos 35–37', f'''
<p>O versículo 35 abre com <i>Et</i>, como quase todos os outros. Esse "e" inicial é a marca mais visível da <b>parataxe</b> do capítulo 50: Marcos não diz "então", "depois", "como", mas encadeia as ações com <i>et</i>, e o leitor deve dar a cada um o valor que o sentido pede ("e", "então", "mas"). Num texto clássico, as três primeiras frases provavelmente seriam um único período com orações subordinadas; aqui são frases coordenadas, curtas, fáceis de seguir.</p>
<p>Dentro desse estilo simples aparecem construções que você viu (ou verá) na Parte III. <i>Cum sērō esset factum</i> é um <i>cum</i> com subjuntivo, que descreve as circunstâncias em que algo acontece (Bennett § 288.1.B; A&amp;G § 546; capítulo 34). <i>Trānseāmus</i> é o subjuntivo exortativo de 1ª pessoa do plural, "passemos" (Bennett § 274; A&amp;G § 439; capítulo 32). <i>Dīmittentēs</i> é um particípio presente que concorda com o sujeito implícito de <i>assūmunt</i>, "eles" (capítulo 29). Nenhuma dessas construções é exclusiva do latim cristão: são clássicas, usadas com sobriedade.</p>
<h3>O presente histórico</h3>
<p>Em <i>assūmunt eum</i> o tempo muda de repente: a narração vinha no passado (<i>ait</i>) e passa ao presente. É o <b>presente histórico</b>, usado "na narração viva" para pôr a cena diante dos olhos (Bennett § 259.3; A&amp;G § 469). César também o usa; Marcos, imitando o próprio grego, abusa dele. Em português o recurso existe e funciona do mesmo jeito ("e aí eles <i>levam</i> Jesus no barco"); você pode mantê-lo, como fez a tradução, ou passar tudo ao passado. O que não pode é traduzir <i>assūmunt</i> como uma ação diferente, no presente real.</p>
<h3>Um período com ita ut</h3>
<p>O versículo 37 é o mais "clássico" do trecho, porque termina numa oração consecutiva: <i>ita ut implērētur nāvis</i>, "de modo que o barco se enchia". <i>Ut</i> + subjuntivo, anunciado por <i>ita</i>, indica a consequência (Bennett § 284; A&amp;G § 537; capítulo 33). O imperfeito <i>implērētur</i> mostra a ação em curso: o barco estava se enchendo, ainda não estava cheio. Compare com <i>ita ut erat</i> no versículo 36: ali <i>ut</i> tem indicativo e significa "como"; quem decide entre "como" e "de modo que" é o modo do verbo.</p>
{diagrama_frase([('facta est procella', 'oração 1 · "levantou-se uma tempestade"'), ('et flūctus mittēbat', 'oração 2 · coordenada por et'), ('in nāvim', 'in + acusativo · "para dentro do barco"'), ('ita ut', 'conjunção consecutiva · "de modo que"'), ('implērētur nāvis', 'imperfeito do subjuntivo · consequência')], 'Marcos 4,37: <i>Et facta est procella magna ventī, et flūctus mittēbat in nāvim, ita ut implērētur nāvis</i>. Duas orações coordenadas (parataxe) e, no fim, uma subordinada consecutiva que depende da segunda.')}
'''),
        ('Análise gramatical: o grito dos discípulos (v. 38)', f'''
<p>O versículo 38 junta descrição (Jesus dorme), ação (acordam-no) e fala direta. É o centro do episódio e um bom exercício de leitura em ordem: cada palavra cria uma expectativa que a seguinte resolve.</p>
{analise('Marcos 4,38, palavra a palavra', [
    ('Et', 'et (conjunção)', 'invariável', 'liga ao versículo anterior (parataxe)'),
    ('erat', 'sum, esse, fuī', 'imperfeito do indicativo, 3ª sing.', 'verbo da 1ª oração: "estava" (descrição de fundo)'),
    ('ipse', 'ipse, ipsa, ipsum', 'nominativo masculino singular', 'sujeito: "ele" (Jesus), com ênfase: enquanto os outros lutam, <b>ele</b> dorme'),
    ('in puppī', 'in + puppis, -is (f.), popa', 'ablativo singular em <i>-ī</i> (tema em <i>-i</i>)', 'lugar onde'),
    ('super cervīcal', 'super + cervīcal, -ālis (n.), almofada', 'acusativo singular neutro (= nominativo)', 'lugar: "sobre a almofada"'),
    ('dormiēns', 'dormiō, -īre, dormir', 'particípio presente, nominativo masc. sing.', 'concorda com <i>ipse</i>: "dormindo"'),
    ('et excitant', 'excitō, -āre, acordar', 'presente do indicativo, 3ª pl.', 'presente histórico; sujeito implícito: os discípulos'),
    ('eum', 'is, ea, id', 'acusativo masculino singular', 'objeto direto: "o" (Jesus)'),
    ('et dīcunt', 'dīcō, -ere, dīxī', 'presente do indicativo, 3ª pl.', 'presente histórico: "dizem"'),
    ('illī', 'ille, illa, illud', 'dativo singular', 'objeto indireto: "a ele", "lhe"'),
    ('Magister', 'magister, -trī (m.), mestre', 'vocativo singular (igual ao nominativo)', 'vocativo, fora da oração'),
    ('nōn… pertinet', 'pertineō, -ēre, dizer respeito', 'presente do indicativo, 3ª sing.', 'verbo da pergunta; o sujeito é a oração com <i>quia</i>'),
    ('ad tē', 'ad + tū', 'acusativo', '<i>pertinēre ad</i>: "importar a ti"'),
    ('quia', 'quia (conjunção)', 'invariável', 'introduz o conteúdo, "que" (capítulo 50)'),
    ('perīmus', 'pereō, -īre, periī, perecer', 'presente do indicativo, 1ª pl.', '"estamos perecendo"; no indicativo, como em português'),
])}
<p>O ponto que exige atenção é <i>quia</i>. Num texto clássico, depois de "não te importa", você esperaria "porque" ou uma oração infinitiva (<i>nōn ad tē pertinet nōs perīre?</i>, com a oração infinitiva como sujeito). Aqui <i>quia</i> é declarativo, o "que" do capítulo 50, e a pergunta inteira é "não te importa <b>que</b> estejamos perecendo?". Traduzir "porque perecemos" daria um sentido torto: não é a causa da indiferença, é o seu objeto. Observe também como o latim pinta a cena com dois tempos: o imperfeito <i>erat… dormiēns</i> dá o fundo (o que durava) e os presentes históricos <i>excitant, dīcunt</i> trazem a ação para o primeiro plano.</p>
<h3>Os versículos 39 e 40</h3>
<p>Jesus responde com quatro verbos: <i>exsurgēns</i> (particípio), <i>comminātus est</i> (perfeito de um depoente: forma passiva, sentido ativo, capítulo 25), <i>dīxit</i> e as duas ordens <i>Tacē, obmūtēsce</i>. O vento e o mar estão no <b>dativo</b>, <i>ventō</i> e <i>marī</i>: o primeiro porque <i>comminor</i>, como os verbos de ameaçar, pede dativo (Bennett § 187.II.a); o segundo porque é a quem se diz algo. A resposta da natureza vem em duas orações curtas e simétricas, <i>cessāvit ventus</i> e <i>facta est tranquillitās magna</i>, que fazem eco ao <i>facta est procella magna</i> do versículo 37: a "grande tempestade" e a "grande calmaria" se respondem.</p>
<p>No versículo 40, <i>Quid timidī estis?</i> começa com o <i>quid</i> adverbial, "por quê?" (Bennett § 176.3.a), e não "o quê?". A reação dos discípulos, <i>timuērunt timōre magnō</i>, repete a raiz do verbo no substantivo. O latim clássico conhece algo parecido no acusativo, <i>vītam dūram vīxī</i>, "vivi uma vida dura" (o acusativo de mesma raiz, Bennett § 176.4); o ablativo com adjetivo, aqui, reflete o estilo bíblico, que gosta dessas repetições enfáticas. A última frase tem o intercalado <i>putās</i> ("pensas tu") e um segundo <i>quia</i>, agora explicativo: "quem é este, já que até o vento e o mar lhe obedecem?" (<i>obēdiō</i>, também com dativo, Bennett § 187.II.a).</p>
'''),
        ('O que o capítulo 50 nos ensina a ver', f'''
<p>Faça agora o balanço. Em seis versículos você encontrou quase todos os traços do latim cristão descritos no capítulo 50, e nenhum deles impediu a leitura:</p>
<ul>
<li><b>Parataxe</b>: dezessete <i>et</i> ligam frases curtas, sem conjunções subordinativas de tempo ou de causa entre elas.</li>
<li><b><i>Quia</i></b> em dois usos: declarativo depois de <i>nōn ad tē pertinet</i> (v. 38, "que") e explicativo na pergunta final (v. 40, "já que").</li>
<li><b>Preposição no lugar de caso</b>: <i>dīcēbant ad alterutrum</i> (v. 40), onde o clássico diria <i>inter sē</i>.</li>
<li><b>Torneio bíblico</b>: <i>timuērunt timōre magnō</i>, verbo e substantivo da mesma raiz.</li>
<li><b>Presente histórico</b> e imperfeito descritivo alternando com o perfeito narrativo: um traço do estilo de Marcos, mais do que do latim cristão.</li>
<li><b>Morfologia clássica</b>: subjuntivos (<i>esset, trānseāmus, implērētur</i>), particípios, um depoente, imperativos, temas em <i>-i</i> (<i>nāvim, nāvī, puppī</i>). Nada que um leitor de Cícero estranhe.</li>
</ul>
<h3>Clementina e Nova Vulgata</h3>
<p>A Nova Vulgata (1979) revisou o texto à luz do grego e retocou alguns pontos de gramática. Neste trecho as diferenças são pequenas e instrutivas:</p>
{comparacao('Marcos 4,35–41: Vulgata Clementina e Nova Vulgata', ['Vulgata Clementina', 'Nova Vulgata', 'Comentário'], [
    ['in illā diē', 'illā diē', 'ablativo de tempo sem preposição, mais clássico'],
    ['Et facta est procella magna ventī', 'Et exoritur procella magna ventī', 'presente histórico (<i>exorior</i>, levantar-se), como o grego'],
    ['flūctus mittēbat in nāvim', 'flūctus sē mittēbant in nāvem', 'plural explícito e reflexivo: "as ondas se lançavam"; acusativo <i>nāvem</i>'],
    ['assūmunt eum ita ut erat', 'assūmunt eum, ut erat', 'só <i>ut</i> comparativo, sem <i>ita</i>'],
    ['ita ut implērētur', 'ita ut iam implērētur', '<i>iam</i>: "já se enchia"'],
    ['super cervīcal; dīcunt illī', 'suprā cervīcal; dīcunt eī', 'pequenas trocas de preposição e de pronome'],
    ['timuērunt timōre magnō', 'timuērunt magnō timōre', 'só a ordem das palavras'],
    ['obēdiunt', 'oboediunt', 'grafia mais próxima da clássica (<i>oboediō</i>)'],
    ['versículo 40 (único)', 'versículos 40 e 41', 'numeração moderna'],
])}
<p>A comparação mostra também como resolver a dúvida do versículo 37: a Nova Vulgata entende <i>flūctus</i> como plural e põe o verbo no plural (<i>mittēbant</i>), com o reflexivo <i>sē</i>; a Clementina, com <i>mittēbat</i> no singular, admite duas leituras: <i>flūctus</i> singular coletivo ("a vaga") ou plural com verbo no singular, que reproduz o grego <i>ta kýmata epéballen</i> (neutro plural com verbo no singular). O sentido não muda: a água entrava no barco.</p>
{dica('<b>Para continuar lendo Marcos</b>: o capítulo 4 começa com a parábola do semeador (4,1–20), cheia de presentes, imperativos e orações relativas; o capítulo 5 traz a cura da filha de Jairo (5,21–43), com a frase aramaica <i>Talitha cumi</i>. Leia um episódio por vez, com o dicionário e sem pressa; depois de três ou quatro, o vocabulário começa a se repetir.')}
'''),
    ],
    erros_comuns=[
        ('Traduzir <i>quia perīmus</i> por "porque perecemos".', 'Depois de <i>nōn ad tē pertinet</i>, "não te importa", <i>quia</i> introduz aquilo que importa ou não: é o "que" declarativo do latim cristão. "Não te importa que estejamos perecendo?" A pergunta-teste do capítulo 50 resolve: a oração responde a "o quê?", não a "por quê?".'),
        ('Corrigir os presentes históricos para o perfeito sem perceber que são presentes, ou traduzi-los como ações atuais.', '<i>Assūmunt, excitant, dīcunt</i> são presentes do indicativo usados para narrar o passado (Bennett § 259.3). Mantenha o presente ("acordam-no") ou passe ao passado ("acordaram-no"), mas trate-os como parte da narração.'),
        ('Ler <i>Quid timidī estis?</i> como "o que sois, medrosos?".', '<i>Quid</i> no início de uma pergunta com <i>esse</i> e adjetivo é o acusativo adverbial "por quê?" (Bennett § 176.3.a). "Por que sois medrosos?"'),
        ('Tomar <i>ventō</i> e <i>marī</i> por ablativos ("com o vento", "no mar").', '<i>Comminor</i> (ameaçar, repreender) e <i>dīcō</i> pedem dativo: o vento é repreendido, ao mar é dito. As formas em <i>-ō</i> (2ª decl.) e em <i>-ī</i> (3ª decl., tema em <i>-i</i>) são ambíguas entre dativo e ablativo; decida pelo verbo.'),
        ('Ler <i>comminātus est</i> como passiva ("foi ameaçado").', '<i>Comminor</i> é depoente: forma passiva, sentido ativo (capítulo 25). <i>Comminātus est ventō</i> = "repreendeu o vento". O dicionário avisa: <i>comminor, -ārī, comminātus sum</i>, sem forma ativa.'),
        ('Confundir os dois <i>ut</i> de <i>ita ut erat</i> (v. 36) e <i>ita ut implērētur</i> (v. 37).', 'Com indicativo, <i>ut</i> é comparativo, "como": "assim como estava". Com subjuntivo depois de <i>ita</i>, é consecutivo, "de modo que": "de modo que o barco se enchia". O modo do verbo decide.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · A pergunta final (v. 40)',
            'Analise e traduza: <i lang="la">Quis, putās, est iste, quia et ventus et mare obēdiunt eī?</i> Vocabulário: <i>putō, -āre</i>, pensar, julgar; <i>obēdiō, -īre</i>, obedecer.', [
            ('Onde está o verbo principal da pergunta, e qual é o sujeito?', '<i>Est</i>; sujeito <i>iste</i>, "este (homem)", e predicativo o interrogativo <i>quis</i>: "quem é este?".'),
            ('O que faz <i>putās</i> no meio da frase?', 'É um verbo intercalado, 2ª sing. do presente de <i>putō</i>: "pensas tu?", "achas?". Não tem função sintática na pergunta; dá o tom de espanto, como o português "quem será este, afinal?".'),
            ('Como entender <i>et… et</i>?', 'A dupla <i>et… et</i> vale "tanto… quanto", "até… e…": "tanto o vento quanto o mar".'),
            ('Que caso é <i>eī</i>, e por quê?', 'Dativo singular de <i>is</i>, "a ele". <i>Obēdiō</i> (de <i>ob</i> + <i>audiō</i>, literalmente "dar ouvidos a") pede dativo, como os verbos de obedecer em geral (Bennett § 187.II.a).'),
            ('E <i>quia</i>: "que" ou "porque"?', 'Aqui <i>quia</i> explica o espanto, não completa um verbo de dizer ou saber: "já que", "visto que". A tradução natural em português usa "que" relativo-explicativo: "Quem é este, que até o vento e o mar lhe obedecem?"'),
        ], 'Conclusão: a pergunta final repete o motivo do episódio. O mesmo vento e o mesmo mar dos versículos 37 e 39 são agora sujeito de <i>obēdiunt</i>: o que era ameaça virou obediência.'),
        pratica_guiada('Prática guiada 2 · O começo do episódio (vv. 35–36)',
            'Analise em ordem: <i lang="la">Et ait illīs in illā diē, cum sērō esset factum: Trānseāmus contrā. Et dīmittentēs turbam, assūmunt eum ita ut erat in nāvī.</i>', [
            ('Quem fala e a quem?', '<i>Ait</i>, "disse", 3ª sing.: Jesus, sujeito implícito retomado do contexto. <i>Illīs</i>, dativo plural de <i>ille</i>: "a eles", os discípulos.'),
            ('Que informação dá <i>cum sērō esset factum</i>?', 'A circunstância de tempo: "quando se fizera tarde", "quando já anoitecia". <i>Cum</i> + mais-que-perfeito do subjuntivo (capítulo 34): a ação concluída que serve de fundo.'),
            ('Que forma é <i>Trānseāmus</i>, e por que não é indicativo?', 'Presente do subjuntivo de <i>trānseō</i> (o indicativo seria <i>trānsīmus</i>), 1ª pl.: exortativo, "passemos" (capítulo 32). É um convite, não uma constatação.'),
            ('Quem é o sujeito de <i>dīmittentēs</i> e <i>assūmunt</i>?', 'Os discípulos, não expressos. <i>Dīmittentēs</i> (particípio presente, nominativo plural) concorda com o sujeito de <i>assūmunt</i> (3ª pl.): "eles, deixando a multidão, levam-no".'),
            ('Monte a tradução.', '"E naquele dia, quando já anoitecia, disse-lhes: Passemos para a outra margem. E eles, deixando a multidão, levam-no assim como estava, no barco."'),
        ]),
    ],
    exercicios=[
        exercicio('Exercício 1 · Compreensão', 'Responda em português, apoiando cada resposta numa palavra ou expressão latina do texto.', [
            ('A que horas do dia começa o episódio?', 'Ao entardecer: <i>cum sērō esset factum</i>, "quando já se fazia tarde" (v. 35).'),
            ('Jesus estava sozinho no lago?', 'Não: <i>aliae nāvēs erant cum illō</i>, "havia outros barcos com ele" (v. 36).'),
            ('O que fazia Jesus durante a tempestade, e onde?', 'Dormia na popa, sobre uma almofada: <i>erat ipse in puppī super cervīcal dormiēns</i> (v. 38).'),
            ('De que os discípulos acusam Jesus?', 'De indiferença: <i>nōn ad tē pertinet, quia perīmus?</i>, "não te importa que estejamos perecendo?" (v. 38).'),
            ('Do que Jesus censura os discípulos?', 'Do medo e da falta de fé: <i>Quid timidī estis? necdum habētis fidem?</i> (v. 40).'),
            ('Qual é a reação dos discípulos depois do milagre?', 'Medo maior e espanto: <i>timuērunt timōre magnō</i>, e perguntam <i>Quis… est iste</i>, "quem é este" (v. 40).'),
        ]),
        exercicio('Exercício 2 · Morfologia', 'Identifique as formas (verbo de dicionário, tempo, modo, voz, pessoa e número; ou caso e número) e traduza.', [
            ('<i>assūmunt</i>', '<i>assūmō, -ere</i>: presente do indicativo ativo, 3ª pl. (presente histórico). "Levam (consigo)".'),
            ('<i>implērētur</i>', '<i>impleō, -ēre</i>: imperfeito do subjuntivo passivo, 3ª sing. (infinitivo <i>implēre</i> + <i>-tur</i>). "Se enchia, era enchido".'),
            ('<i>perīmus</i>', '<i>pereō, -īre</i>: presente do indicativo, 1ª pl. (como <i>īmus</i>, de <i>eō</i>). "Perecemos, estamos perecendo".'),
            ('<i>comminātus est</i>', '<i>comminor, -ārī</i>, depoente: perfeito do indicativo, 3ª sing., forma passiva com sentido ativo. "Repreendeu, ameaçou".'),
            ('<i>Tacē</i> e <i>obmūtēsce</i>', 'Imperativos presentes, 2ª sing., de <i>taceō</i> (2ª conj., <i>ē</i> longo) e <i>obmūtēscō</i> (3ª conj., <i>e</i> breve). "Cala-te", "emudece".'),
            ('<i>timuērunt</i>', '<i>timeō, -ēre, timuī</i>: perfeito do indicativo, 3ª pl. "Temeram".'),
            ('<i>nāvim</i> e <i>nāvī</i>', '<i>nāvis, -is</i> (f.), tema em <i>-i</i>: <i>nāvim</i>, acusativo singular (com <i>in</i>, movimento: "para dentro do barco"); <i>nāvī</i>, ablativo singular (com <i>in</i>, lugar: "no barco").'),
            ('<i>eī</i>', '<i>is, ea, id</i>: dativo singular. "A ele", "lhe".'),
        ]),
        exercicio('Exercício 3 · Sintaxe', 'Explique a construção destacada.', [
            ('<i>cum sērō <b>esset factum</b></i> (v. 35)', '<i>Cum</i> + mais-que-perfeito do subjuntivo: oração temporal-circunstancial (Bennett § 288.1.B; capítulo 34). "Quando já se fizera tarde".'),
            ('<i>ita ut <b>erat</b></i> (v. 36) e <i>ita ut <b>implērētur</b></i> (v. 37)', 'No primeiro, <i>ut</i> + indicativo é comparativo ("como"); no segundo, <i>ita ut</i> + subjuntivo é consecutivo ("de modo que", Bennett § 284).'),
            ('<i>comminātus est <b>ventō</b></i> (v. 39)', 'Dativo exigido por <i>comminor</i>, verbo de ameaçar (Bennett § 187.II.a).'),
            ('<i>nōn ad tē pertinet, <b>quia</b> perīmus?</i> (v. 38)', '<i>Quia</i> declarativo: introduz o conteúdo do que "importa", com indicativo. No latim clássico: oração infinitiva (<i>nōs perīre</i>).'),
            ('<i>dīcēbant <b>ad alterutrum</b></i> (v. 40)', '<i>Ad</i> + acusativo no lugar do dativo (ou de <i>inter sē</i>): traço do latim cristão (capítulo 50).'),
            ('<i>timuērunt <b>timōre magnō</b></i> (v. 40)', 'Ablativo de um substantivo da mesma raiz do verbo, com adjetivo: torneio enfático do estilo bíblico, parente do acusativo de mesma raiz do latim clássico (Bennett § 176.4).'),
        ]),
        exercicio('Exercício 4 · Traduza outro episódio: o batismo de Jesus (Mc 1,9–11)', 'Traduza cada versículo. Vocabulário: <i>Nazareth</i> (indeclinável), Nazaré; <i>Galilaea, -ae</i>, Galileia; <i>Ioannes, -is</i>, João; <i>Iordānēs, -is</i>, o rio Jordão; <i>statim</i>, imediatamente; <i>ascendō, -ere</i>, subir; <i>apertus, -a, -um</i>, aberto; <i>columba, -ae</i>, pomba; <i>tamquam</i>, como; <i>dīlēctus, -a, -um</i>, amado; <i>complaceō, -ēre, complacuī</i>, agradar-se.', [
            ('<i>Et factum est: in diēbus illīs vēnit Iēsūs ā Nazareth Galilaeae, et baptizātus est ā Ioanne in Iordāne.</i>', '"E aconteceu que, naqueles dias, Jesus veio de Nazaré da Galileia e foi batizado por João no Jordão." <i>Et factum est</i>, "e aconteceu", é uma fórmula de abertura bíblica, de origem hebraica; <i>baptizātus est ā Ioanne</i> é perfeito passivo com agente (<i>ā</i> + ablativo, capítulos 23–24).'),
            ('<i>Et statim ascendēns dē aquā, vīdit caelōs apertōs, et Spīritum tamquam columbam dēscendentem, et manentem in ipsō.</i>', '"E logo, ao subir da água, viu os céus abertos e o Espírito, como uma pomba, descendo e permanecendo sobre ele." <i>Ascendēns, dēscendentem, manentem</i> são particípios presentes; os dois últimos concordam com <i>Spīritum</i>, objeto de <i>vīdit</i> ("viu o Espírito descendo"). <i>Apertōs</i> é predicativo do objeto <i>caelōs</i>.'),
            ('<i>Et vōx facta est dē caelīs: Tū es Fīlius meus dīlēctus, in tē complacuī.</i>', '"E fez-se ouvir uma voz dos céus: Tu és o meu Filho amado; em ti me comprazi." <i>Vōx facta est</i>, "uma voz se fez", como <i>facta est procella</i> em 4,37; <i>in tē complacuī</i>, "em ti pus o meu agrado", é um decalque do grego.'),
        ]),
        exercicio('Exercício 5 · Traduza: Jesus e as crianças (Mc 10,14–15)', 'Traduza e responda às perguntas. Vocabulário: <i>indignē ferō</i>, indignar-se (<i>tulit</i>, perfeito de <i>ferō</i>); <i>sinō, -ere</i>, deixar, permitir; <i>parvulus, -ī</i>, criancinha; <i>prohibeō, -ēre, prohibuī</i>, impedir; <i>tālis, -e</i>, tal; <i>quisquis</i>, quem quer que; <i>recipiō, -ere, recēpī</i>, receber; <i>velut</i>, como.', [
            ('<i>Quōs cum vidēret Iēsūs, indignē tulit, et ait illīs: Sinite parvulōs venīre ad mē, et nē prohibuerītis eōs: tālium enim est rēgnum Deī.</i>', '"Jesus, ao vê-los (fazer isso), indignou-se e disse-lhes: Deixai as criancinhas virem a mim e não as impeçais, pois delas (dos que são como elas) é o Reino de Deus." <i>Quōs</i> é relativo de ligação, objeto de <i>vidēret</i>: retoma os discípulos, que no versículo 13 repreendiam os que traziam as crianças; <i>cum vidēret</i>, <i>cum</i> + imperfeito do subjuntivo (capítulo 34).'),
            ('Que construção é <i>nē prohibuerītis</i>?', 'Proibição com <i>nē</i> + perfeito do subjuntivo, 2ª pl. (Bennett § 276; capítulo 32): "não (as) impeçais". O perfeito não tem valor de passado aqui.'),
            ('Que caso é <i>tālium</i> e qual a sua função?', 'Genitivo plural de <i>tālis</i>: genitivo de posse com <i>est</i>, "o Reino de Deus é dos tais", isto é, pertence aos que são como as crianças.'),
            ('<i>Āmēn dīcō vōbīs: Quisquis nōn recēperit rēgnum Deī velut parvulus, nōn intrābit in illud.</i>', '"Em verdade vos digo: quem não receber o Reino de Deus como uma criancinha, não entrará nele." <i>Recēperit</i> é futuro perfeito (capítulo 13): a ação de receber deve estar concluída antes da de entrar; o português usa o futuro do subjuntivo. <i>Āmēn</i> é o hebraísmo do capítulo 50.'),
        ]),
    ],
    leituras=['vulgata-biblia-sacra-vulgata-editio-clementina', 'vulgata-prophetia-ionae-vulgata', 'lhomond-epitome-historiae-sacrae', 'stridonensis-vita-sancti-pauli-primi-eremitae', 'ravizza-gramatica-latina'],
    leituras_nota='Continue o Evangelho de Marcos na Vulgata, um episódio por vez: 4,1–20 (o semeador), 5,21–43 (a filha de Jairo), 6,30–44 (a multiplicação dos pães). O livro de Jonas é uma narrativa bíblica curta e completa, ótima para ler logo depois deste capítulo, com outra tempestade no mar. O <i>Epitome Historiae Sacrae</i> de Lhomond reconta a história bíblica em latim escolar mais clássico: compare a sua sintaxe com a da Vulgata. A <i>Vida de São Paulo, o primeiro eremita</i> mostra Jerônimo escrevendo com a própria voz, em prosa literária, não como tradutor. Para a história da Bíblia latina, leia o n. 512 da <i>Gramática</i> do Pe. Ravizza.',
)
