from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='03-introducao-aos-casos', titulo='Introdução aos casos gramaticais', titulo_latim='Dē cāsibus', tempo='50 min',
    resumo='Os seis casos do latim, um a um: o que cada um faz na frase, como se diz a mesma coisa em português, como reconhecê-los numa palavra da primeira declinação e como usá-los para ler uma frase autêntica.',
    status='publicada',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['os seis casos', 'nominativo', 'genitivo', 'dativo', 'acusativo', 'vocativo', 'ablativo', '1ª declinação', 'locativo (menção)', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulos 1 e 2: saber ler em voz alta e reconhecer sujeito e objeto pelas terminações.', licoes=['01-o-que-e-o-latim', '02-como-funciona-uma-frase-latina']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§§ 17–19 (os casos, na mesma ordem deste livro), §§ 20–22 (1ª declinação)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§§ 35–39 (número e caso; terminações das cinco declinações), §§ 40–43 (1ª declinação)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 34 (paradigma de mensa na ordem britânica (N, V, Ac, G, D, Ab))', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='nn. 16–18 (os casos, as declinações e a 1ª declinação, rosa), em português, na mesma ordem deste livro', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Gênesis 1,1', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', nota='frase autêntica analisada na seção 5', tipo='dominio_publico'),
    ],
    objetivos=[
        'Nomear os seis casos latinos e a função principal de cada um.',
        'Associar cada caso à pergunta que ele responde e à construção correspondente em português.',
        'Reconhecer os casos nas terminações de um nome da primeira declinação (<i>rosa, -ae</i>), inclusive as formas que coincidem.',
        'Analisar uma frase simples e uma frase autêntica caso a caso, lendo na ordem latina.',
    ],
    secoes=[
        ('O que é um caso', f'''
<p>No capítulo anterior você viu que <i>Mārcus</i> e <i>Mārcum</i> são a mesma palavra com crachás diferentes: sujeito e objeto. Cada um desses crachás é um <b>caso</b>. A palavra vem do latim <i>cāsus</i>, "queda": os gramáticos antigos imaginavam o nome "caindo" da sua forma básica para as outras formas. Caso, portanto, é a forma que o nome assume para mostrar sua função na frase.</p>
<p>O latim clássico tem <b>seis casos</b>. O conjunto das formas de uma palavra, no singular e no plural, chama-se <b>declinação</b>, e "declinar" uma palavra é recitar essas formas em ordem. Os nomes latinos distribuem-se em cinco famílias, as cinco declinações, cada uma com seu jogo de terminações; neste capítulo usamos a primeira, a das palavras em <i>-a</i> como <i>rosa</i>, <i>puella</i>, <i>terra</i>.</p>
{tabela(['Caso', 'Função principal', 'Responde a', 'Em português'], [
    ['<b>Nominativo</b>', 'sujeito; predicativo do sujeito', 'quem? o quê? (faz, é)', 'o sujeito da frase'],
    ['<b>Genitivo</b>', 'posse, pertencimento, parte de um todo', 'de quem? de quê?', 'complemento com "de"'],
    ['<b>Dativo</b>', 'destinatário da ação (objeto indireto)', 'a quem? para quem?', 'complemento com "a", "para"'],
    ['<b>Acusativo</b>', 'objeto direto; com preposição, direção', 'quem? o quê? (recebe); para onde?', 'objeto direto; "para", "a" com movimento'],
    ['<b>Vocativo</b>', 'chamamento, invocação', '(a pessoa a quem se fala)', 'o vocativo: "Júlia, vem!"'],
    ['<b>Ablativo</b>', 'meio, companhia, lugar, origem, tempo', 'com quê? com quem? onde? de onde? quando?', '"com", "em", "por", "de"'],
], 'Os seis casos e suas funções principais')}
<p>A ordem em que os casos aparecem nas tabelas varia conforme a tradição. Este livro usa nominativo, genitivo, dativo, acusativo, vocativo e ablativo, que é a ordem da gramática de Bennett (§ 17) e da <i>Gramática Latina</i> do Pe. Ravizza, usada por gerações de estudantes brasileiros. A tradição escolar britânica, fixada pela gramática de Kennedy, recita nominativo, vocativo, acusativo, genitivo, dativo e ablativo; e os métodos que ensinam latim em latim, como o de Ørberg, apresentam os casos aos poucos, a começar pelo nominativo e pelo acusativo. As formas são as mesmas; só muda a ordem da recitação.</p>
{dica('<b>Você já usa casos em português.</b> Os pronomes ainda os conservam: <i>eu</i> (sujeito), <i>me</i> (objeto), <i>mim</i> (depois de preposição), <i>lhe</i> (objeto indireto): "<i>eu</i> vi", "ele <i>me</i> viu", "para <i>mim</i>", "dei-<i>lhe</i> um livro". Em latim, todos os nomes funcionam assim, não só os pronomes.')}
'''),
        ('Os casos, um a um', f'''
<h3>Nominativo: quem faz, ou quem é</h3>
<p>É a forma "de dicionário" do nome e o caso do sujeito. Também é o caso do predicativo com o verbo <i>esse</i> (ser, estar): o que se diz do sujeito fica no mesmo caso que ele.</p>
{exemplos([('<b>Puella</b> cantat.', 'A menina canta.'), ('<b>Rosa</b> pulchr<b>a</b> est.', 'A rosa é bela. (<i>pulchra</i>, predicativo, também está no nominativo)')])}
<h3>Genitivo: de quem, de quê</h3>
<p>Liga um nome a outro nome, quase sempre traduzido por "de": posse (<i>a casa da senhora</i>), parentesco (<i>a filha do agricultor</i>), parte de um todo (<i>uma parte da Gália</i>). O genitivo depende de um substantivo, não do verbo, e costuma ficar perto dele.</p>
{exemplos([('vīlla <b>dominae</b>', 'a casa da senhora'), ('fīlia <b>agricolae</b>', 'a filha do agricultor'), ('Rosa <b>puellae</b> pulchra est.', 'A rosa da menina é bela.')])}
<h3>Dativo: a quem, para quem</h3>
<p>Marca a pessoa a quem algo é dado, dito ou mostrado: o objeto indireto do português, mas <b>sem preposição</b>. Verbos como "dar", "mostrar", "contar", "escrever (a alguém)" pedem dativo.</p>
{exemplos([('Puella rosam <b>amīcae</b> dat.', 'A menina dá uma rosa à amiga.'), ('Magistra fābulam <b>puellīs</b> nārrat.', 'A professora conta uma história às meninas.')])}
<h3>Acusativo: o quê, e para onde</h3>
<p>Marca o objeto direto, aquilo que recebe diretamente a ação. Com certas preposições (<i>ad</i>, "para, até"; <i>in</i>, "para dentro de") indica o <b>lugar para onde</b> se vai.</p>
{exemplos([('Puella <b>rosam</b> amat.', 'A menina ama a rosa.'), ('Nautae <b>stellās</b> spectant.', 'Os marinheiros contemplam as estrelas.'), ('Puella ad <b>vīllam</b> ambulat.', 'A menina caminha até a casa.')])}
<h3>Vocativo: a pessoa chamada</h3>
<p>É o caso de quem é chamado ou invocado. Em quase todas as palavras é igual ao nominativo; a exceção importante são os nomes masculinos em <i>-us</i> da segunda declinação, que fazem o vocativo em <i>-e</i> (<i>Mārcus</i> → <i>Mārce</i>), e os nomes próprios em <i>-ius</i>, que o fazem em <i>-ī</i> (<i>Iūlius</i> → <i>Iūlī</i>). Você os verá no capítulo 5.</p>
{exemplos([('Salvē, <b>Iūlia</b>!', 'Olá, Júlia!'), ('<b>Puellae</b>, cantāte!', 'Meninas, cantai! (cantem!)')])}
<h3>Ablativo: com quê, onde, de onde, quando</h3>
<p>É o caso mais variado: reúne funções que o português distribui entre várias preposições. Sozinho, indica muitas vezes o meio ou instrumento ("com água"); com <i>cum</i>, a companhia; com <i>in</i>, o lugar onde; com <i>ā/ab</i> e <i>ē/ex</i>, a origem ("de, desde"). As preposições que o acompanham são a melhor pista para reconhecê-lo.</p>
{exemplos([('Puella cum <b>amīcā</b> ambulat.', 'A menina passeia com a amiga.'), ('Rosa in <b>mēnsā</b> est.', 'A rosa está na mesa.'), ('Nautae ex <b>Ītaliā</b> nāvigant.', 'Os marinheiros navegam (saindo) da Itália.'), ('Agricola <b>aquā</b> terram rigat.', 'O agricultor rega a terra com água. (meio, sem preposição)')])}
{observacao('Acusativo ou ablativo depois de in?', '<i>In vīllam</i> (acusativo) = <i>para dentro da casa</i>: há movimento. <i>In vīllā</i> (ablativo) = <i>dentro da casa</i>: não há movimento. A diferença de sentido está inteira na terminação <i>-am</i> / <i>-ā</i>. O português usa a mesma preposição "em" para os dois ("entrou em casa", "está em casa"); o latim não.')}
'''),
        ('A primeira declinação: rosa', f'''
<p>Agora as terminações, todas juntas. A primeira declinação reúne os nomes cujo genitivo singular termina em <i>-ae</i>; quase todos são femininos. As exceções são nomes de homens e de ofícios masculinos, como <i>nauta</i> (marinheiro), <i>agricola</i> (agricultor) e <i>poēta</i> (poeta), que se declinam igualmente.</p>
{tabela_declinacao('Primeira declinação: rosa, rosae (f.), "rosa"', [
    ('ros<b>a</b>', 'ros<b>ae</b>'), ('ros<b>ae</b>', 'ros<b>ārum</b>'), ('ros<b>ae</b>', 'ros<b>īs</b>'),
    ('ros<b>am</b>', 'ros<b>ās</b>'), ('ros<b>a</b>', 'ros<b>ae</b>'), ('ros<b>ā</b>', 'ros<b>īs</b>')])}
<p>Repare nas formas que coincidem, porque é nelas que o leitor iniciante tropeça:</p>
{comparacao('Formas iguais na primeira declinação', ['Terminação', 'Pode ser', 'Como decidir'], [
    ['-ae', 'genitivo sing. · dativo sing. · nominativo/vocativo pl.', 'o número do verbo (sujeito plural?), um nome vizinho de que dependa ("de"), um verbo de dar/dizer ("a")'],
    ['-a / -ā', 'nominativo/vocativo sing. · ablativo sing.', 'nos textos com macron, a vogal longa; sem macron, uma preposição (<i>cum, in, ex</i>) ou a função que falta na frase'],
    ['-īs', 'dativo pl. · ablativo pl.', 'uma preposição pede ablativo; um verbo de dar ou dizer pede dativo'],
])}
<p>Recite a declinação em voz alta, nos dois números: <i>rosa, rosae, rosae, rosam, rosa, rosā; rosae, rosārum, rosīs, rosās, rosae, rosīs</i>. Depois faça o mesmo com <i>puella</i>, <i>terra</i>, <i>aqua</i>, <i>stella</i>. Todas se comportam igual.</p>
'''),
        ('Uma frase, caso a caso', f'''
<p>Veja como os casos distribuem os papéis numa frase um pouco mais longa, lida na ordem em que um romano a ouviria:</p>
{diagrama_frase([('Puella', 'nominativo · quem dá'), ('rosam', 'acusativo · o que dá'), ('amīcae', 'dativo · a quem dá'), ('in hortō', 'ablativo · onde'), ('dat', 'verbo · "dá"')], 'Lendo em ordem: <i>Puella rosam amīcae in hortō dat</i> = A menina dá uma rosa à amiga no jardim.')}
<p><i>Puella</i>: nominativo, o sujeito; alguém vai fazer algo. <i>Rosam</i>: acusativo, eis o que é feito com uma rosa. <i>Amīcae</i>: pode ser genitivo ("a rosa da amiga") ou dativo ("à amiga"); a dúvida fica em suspenso. <i>In hortō</i>: <i>in</i> + ablativo, o lugar onde (<i>hortus</i>, jardim, é da segunda declinação, com ablativo em <i>-ō</i>). <i>Dat</i>: "dá", um verbo que pede exatamente um objeto e um destinatário; agora <i>amīcae</i> se resolve como dativo.</p>
<p>A ambiguidade de <i>amīcae</i> é normal e não atrapalha, porque a frase se resolve quando o verbo chega. Ler em ordem é também saber <b>esperar</b>.</p>
'''),
        ('Análise gramatical: uma frase autêntica', f'''
<p>Com seis casos e uma declinação você já consegue analisar uma das frases mais conhecidas do latim, a primeira da Bíblia na tradução de São Jerônimo:</p>
{exemplos([('In prīncipiō creāvit Deus caelum et terram.', 'No princípio, Deus criou o céu e a terra. (Gn 1,1, Vulgata)')])}
<p>Três palavras pertencem à segunda declinação, que você ainda não estudou; basta saber, por ora, que <i>-us</i> é nominativo e <i>-um</i> e <i>-ō</i> podem ser, respectivamente, acusativo e ablativo. O verbo <i>creāvit</i> está no perfeito ("criou"), tempo que você verá no capítulo 13; a terminação <i>-t</i> já diz que o sujeito é singular.</p>
{analise('Gn 1,1, palavra a palavra', [
    ('In', 'in (preposição)', 'pede acusativo ou ablativo', 'introduz a circunstância'),
    ('prīncipiō', 'prīncipium, -ī (n.), princípio', 'ablativo singular, 2ª declinação', '<i>in</i> + ablativo: "no princípio" (tempo)'),
    ('creāvit', 'creō, creāre, criar', 'perfeito, 3ª pessoa do singular', 'verbo da oração: "criou"'),
    ('Deus', 'deus, -ī (m.), deus', 'nominativo singular, 2ª declinação', 'sujeito'),
    ('caelum', 'caelum, -ī (n.), céu', 'acusativo singular, 2ª declinação (neutro)', 'objeto direto'),
    ('et', 'et (conjunção)', 'invariável', 'liga os dois objetos'),
    ('terram', 'terra, -ae (f.), terra', 'acusativo singular, 1ª declinação', 'objeto direto'),
])}
<p>Um ponto exige atenção: <i>caelum</i> é neutro, e nos neutros o nominativo e o acusativo são sempre iguais. Como saber que ele é objeto, e não sujeito? Por duas pistas: o sujeito já existe (<i>Deus</i>, nominativo inequívoco, concordando com o verbo singular), e <i>caelum</i> está ligado por <i>et</i> a <i>terram</i>, um acusativo claro. Palavras coordenadas por <i>et</i> costumam estar no mesmo caso. Esse raciocínio por exclusão, "esta função já está ocupada, então a palavra ambígua tem a outra", é a ferramenta mais útil do leitor de latim.</p>
'''),
        ('Resumo e próximos passos', '''
<ul>
<li><b>Seis casos</b>: nominativo (sujeito), genitivo ("de"), dativo ("a, para"), acusativo (objeto; "para onde"), vocativo (chamamento), ablativo (meio, companhia, lugar, origem, tempo).</li>
<li><b>Primeira declinação</b>: <i>-a, -ae, -ae, -am, -a, -ā</i> / <i>-ae, -ārum, -īs, -ās, -ae, -īs</i>.</li>
<li><b>Formas iguais</b> (<i>-ae</i>, <i>-a/-ā</i>, <i>-īs</i>) decidem-se pelo verbo, pelas preposições e por exclusão.</li>
<li><b>Ler em ordem</b>: registrar o caso de cada palavra, criar expectativas e deixar a frase se resolver no verbo.</li>
</ul>
<p>O próximo capítulo completa a primeira declinação (gênero, formas especiais, preposições com acusativo e com ablativo) e traz o primeiro texto corrido. Não tente decorar tudo de uma vez: os casos se aprendem vendo-os, centenas de vezes, nas frases dos leitores graduados.</p>
'''),
    ],
    erros_comuns=[
        ('Achar que toda palavra terminada em <i>-a</i> é o sujeito.', 'Em <i>-a</i> terminam também o ablativo singular (<i>rosā</i>, com vogal longa) e, como você verá, o nominativo e o acusativo plural dos neutros (<i>bella</i>). Antes de decidir, procure uma preposição e confira o número do verbo.'),
        ('Traduzir toda forma em <i>-ae</i> por "da".', 'Só o genitivo se traduz por "de". <i>Puellae cantant</i> são "as meninas cantam" (nominativo plural: o verbo está em <i>-nt</i>); <i>Mārcus puellae rosam dat</i> é "Marco dá uma rosa à menina" (dativo).'),
        ('Escolher o caso latino pela preposição do português.', 'O "de" português corresponde a casos diferentes: posse é genitivo (<i>vīlla dominae</i>, "a casa da senhora"), origem é ablativo com preposição (<i>ex Ītaliā</i>, "da Itália"). Pergunte qual é a função, não qual preposição o português usaria.'),
        ('Esquecer que <i>in</i> muda de sentido com o caso.', '<i>In vīllam</i> é "para dentro da casa" (acusativo, movimento); <i>in vīllā</i> é "dentro da casa" (ablativo, lugar). A terminação decide, não a preposição.'),
        ('Reordenar a frase antes de identificar os casos.', 'Quem reordena primeiro costuma pôr a primeira palavra como sujeito. Em <i>Rosās puella amat</i>, o sujeito é <i>puella</i>, e não <i>rosās</i>. Identifique o caso de cada palavra na ordem latina; só depois monte a frase em português.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Uma frase com cinco funções',
            'Leia em voz alta e analise, na ordem latina: <i lang="la">Fīlia rēgīnae nautīs aquam in īnsulā dat.</i> Vocabulário: <i>fīlia</i>, filha; <i>rēgīna</i>, rainha; <i>nauta</i>, marinheiro; <i>aqua</i>, água; <i>īnsula</i>, ilha; <i>dat</i>, dá.', [
            ('Qual é o verbo, e o que ele permite esperar?', '<i>Dat</i>, "dá", 3ª pessoa do singular. Espera-se um sujeito no nominativo singular, uma coisa dada (acusativo) e alguém que recebe (dativo).'),
            ('Que caso é <i>fīlia</i>, e por quê?', 'Nominativo singular. A forma em <i>-a</i> poderia ser ablativo (<i>fīliā</i>), mas não há preposição, ela abre a frase e o verbo singular precisa de um sujeito: é "a filha".'),
            ('E <i>rēgīnae</i>: genitivo, dativo ou nominativo plural?', 'Não pode ser sujeito plural, porque o verbo está no singular e o sujeito já é <i>fīlia</i>. Entre genitivo e dativo, a posição ao lado de <i>fīlia</i> sugere o genitivo: "a filha <b>da rainha</b>". O dativo ficará com outra palavra.'),
            ('Que caso é <i>nautīs</i>?', 'Dativo ou ablativo plural (<i>-īs</i>). Não há preposição, e o verbo "dar" pede um destinatário: dativo, "<b>aos marinheiros</b>".'),
            ('E <i>aquam</i> e <i>in īnsulā</i>?', '<i>Aquam</i>: acusativo singular, o objeto, "água". <i>In īnsulā</i>: <i>in</i> + ablativo, lugar onde, "na ilha".'),
            ('Monte a tradução.', '"A filha da rainha dá água aos marinheiros na ilha."'),
        ]),
        pratica_guiada('Prática guiada 2 · O mesmo -ae, três funções',
            'Compare as três frases e diga o caso de cada forma em <i>-ae</i>. Vocabulário: <i>amīca</i>, amiga; <i>pulchra</i>, bela (concorda com o nome); <i>sunt</i>, são; <i>cantant</i>, cantam.', [
            ('<i lang="la">Puella rosās amīcae dat.</i>', '<i>Amīcae</i> é <b>dativo</b>: o verbo "dar" pede destinatário, e o sujeito singular <i>puella</i> já está dado. "A menina dá rosas à amiga."'),
            ('<i lang="la">Rosae amīcae pulchrae sunt.</i>', '<i>Rosae</i> é <b>nominativo plural</b> (o verbo <i>sunt</i> é plural); <i>pulchrae</i> concorda com ele como predicativo. <i>Amīcae</i>, ao lado de <i>rosae</i> e sem verbo de dar, é <b>genitivo</b>: "As rosas da amiga são belas." (Com o verbo <i>esse</i>, um dativo pode indicar posse, "a amiga tem rosas belas"; esse uso aparece no capítulo 20. Aqui, ao lado de <i>rosae</i>, a leitura natural é o genitivo.)'),
            ('<i lang="la">Amīcae cantant.</i>', '<i>Amīcae</i> é <b>nominativo plural</b>: é a única palavra que pode ser sujeito, e o verbo está em <i>-nt</i>. "As amigas cantam."'),
        ], 'Conclusão: a terminação <i>-ae</i> sozinha não decide o caso. Quem decide é o resto da frase: o número do verbo, o tipo de verbo e as funções já ocupadas.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Que caso é este?', 'Diga o caso (e o número) da palavra destacada e sua função na frase. Vocabulário: <i>portat</i> = carrega; <i>spectant</i> = contemplam; <i>est</i> = está, é; <i>nārrat</i> = conta; <i>fābula</i> = história; <i>lupa</i> = loba; <i>silva</i> = floresta.', [
            ('<i>Fīlia agricolae <b>aquam</b> portat.</i>', 'Acusativo singular: objeto direto de <i>portat</i>. A filha do agricultor carrega água.'),
            ('<i>Fīlia <b>agricolae</b> aquam portat.</i>', 'Genitivo singular: "do agricultor", ligado a <i>fīlia</i>. Não é nominativo plural, porque o verbo está no singular; e "carregar água a alguém" não é o sentido natural de <i>portat</i>, por isso não é dativo.'),
            ('<i>Nautae <b>stellās</b> spectant.</i>', 'Acusativo plural: objeto direto. Os marinheiros contemplam as estrelas.'),
            ('<i><b>Nautae</b> stellās spectant.</i>', 'Nominativo plural: sujeito, confirmado pelo verbo em <i>-nt</i>. Lembre que <i>nauta</i> é masculino.'),
            ('<i>Lupa in <b>silvā</b> est.</i>', 'Ablativo singular, com <i>in</i>: lugar onde. A loba está na floresta.'),
            ('<i>Magistra <b>puellīs</b> fābulam nārrat.</i>', 'Dativo plural: destinatário de <i>nārrat</i>. A professora conta uma história às meninas. A forma <i>-īs</i> também é ablativo, mas não há preposição e "contar" pede "a quem".'),
            ('<i>Salvē, <b>magistra</b>!</i>', 'Vocativo singular: a pessoa a quem se fala. Olá, professora!'),
        ]),
        exercicio('Exercício 2 · Escolha a forma', 'Complete com a forma correta da palavra entre parênteses. Todas são da primeira declinação. Vocabulário: <i>videt</i> = vê; <i>magna</i> = grande; <i>ambulat</i> = passeia, caminha; <i>lūcent</i> = brilham; <i>nāvigant</i> = navegam.', [
            ('A menina vê a lua. → <i>Puella ___ videt.</i> (lūna)', '<i>lūnam</i>: objeto direto, acusativo singular.'),
            ('A casa da rainha é grande. → <i>Vīlla ___ magna est.</i> (rēgīna)', '<i>rēgīnae</i>: genitivo singular, "da rainha".'),
            ('Marco dá rosas à menina. → <i>Mārcus rosās ___ dat.</i> (puella)', '<i>puellae</i>: dativo singular, "à menina".'),
            ('A menina passeia com a amiga. → <i>Puella cum ___ ambulat.</i> (amīca)', '<i>amīcā</i>: ablativo singular, depois de <i>cum</i>.'),
            ('As estrelas brilham. → <i>___ lūcent.</i> (stella)', '<i>Stellae</i>: nominativo plural, sujeito de um verbo no plural.'),
            ('Os marinheiros navegam para a Itália. → <i>Nautae in ___ nāvigant.</i> (Ītalia)', '<i>Ītaliam</i>: acusativo com <i>in</i>, porque há movimento ("para dentro da Itália"). Com ablativo (<i>in Ītaliā</i>) seria "navegam na Itália", sem movimento de chegada.'),
        ]),
        exercicio('Exercício 3 · Decline', 'Decline no singular e no plural, em voz alta e depois por escrito.', [
            ('<i>terra, terrae</i> (f.), terra', 'Singular: terra, terrae, terrae, terram, terra, terrā. Plural: terrae, terrārum, terrīs, terrās, terrae, terrīs.'),
            ('<i>nauta, nautae</i> (m.), marinheiro', 'Singular: nauta, nautae, nautae, nautam, nauta, nautā. Plural: nautae, nautārum, nautīs, nautās, nautae, nautīs. As terminações são as mesmas de <i>rosa</i>; só o gênero é masculino, o que importa para os adjetivos (<i>nauta bonus</i>, capítulo 5).'),
        ]),
        exercicio('Exercício 4 · Traduza lendo em ordem', 'Anote o caso de cada palavra antes de traduzir. Vocabulário: <i>epistula</i> = carta; <i>scrībit</i> = escreve; <i>pecūnia</i> = dinheiro; <i>nōn</i> = não; <i>habent</i> = têm; <i>Rōma</i> = Roma; <i>habitat</i> = mora; <i>poēta</i> = poeta.', [
            ('<i>Fīlia rēgīnae epistulam amīcae scrībit.</i>', '<i>Fīlia</i> (nom., sujeito), <i>rēgīnae</i> (gen., "da rainha"), <i>epistulam</i> (ac., objeto), <i>amīcae</i> (dat., "à amiga", confirmado por <i>scrībit</i>, "escreve a alguém"): A filha da rainha escreve uma carta à amiga.'),
            ('<i>Nautae pecūniam nōn habent.</i>', '<i>Nautae</i> (nom. pl.), <i>pecūniam</i> (ac.), <i>nōn habent</i>: Os marinheiros não têm dinheiro.'),
            ('<i>Poēta Rōmae cum puellīs habitat.</i>', '<i>Poēta</i> (nom. sing., masculino), <i>Rōmae</i> (com nomes de cidade, esta forma indica o lugar onde: "em Roma"; é um resto de um sétimo caso, o locativo, igual ao genitivo na primeira declinação), <i>cum puellīs</i> (abl. pl., companhia), <i>habitat</i>: O poeta mora em Roma com as meninas.'),
        ]),
        exercicio('Exercício 5 · Análise completa', 'Para cada frase, faça a tabela da seção 5 (palavra, caso e número, função) e traduza. Vocabulário: <i>fābula</i> = história; <i>nārrant</i> = contam; <i>dēlectat</i> = agrada, encanta.', [
            ('<i>Poētae fābulās puellīs nārrant.</i>', '<i>Poētae</i>: nominativo plural, sujeito (verbo em <i>-nt</i>). <i>Fābulās</i>: acusativo plural, objeto. <i>Puellīs</i>: dativo plural, destinatário de <i>nārrant</i>. Os poetas contam histórias às meninas.'),
            ('<i>Fābula poētae puellās dēlectat.</i>', '<i>Fābula</i>: nominativo singular, sujeito (verbo em <i>-t</i>). <i>Poētae</i>: genitivo singular, "do poeta", ligado a <i>fābula</i>; não pode ser sujeito plural, porque o verbo é singular. <i>Puellās</i>: acusativo plural, objeto. A história do poeta encanta as meninas.'),
        ]),
    ],
    leituras=['ravizza-gramatica-latina', 'kennedy-kennedy-s-revised-latin-primer', 'bennett-new-latin-grammar', 'leite-latine-loqui-curso-basico-de-latim-volume-i', 'sonnenschein-ora-maritima-a-latin-story-for-beginners', 'vulgata-biblia-sacra-vulgata-editio-clementina'],
    leituras_nota='As gramáticas servem para consultar a tabela quando você se perder (em Bennett, os casos estão nos §§ 17–19 e a primeira declinação no § 20). Ora Maritima pratica exatamente este capítulo em texto corrido, e o Gênesis na Vulgata é um bom primeiro texto autêntico para reconhecer casos.',
)
