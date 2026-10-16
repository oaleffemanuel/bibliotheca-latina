from conteudo.util import (tabela, tabela_conjugacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Texto original do capítulo (para o exercício 5), escrito só com a gramática dos capítulos 1–8 e 12; o resto vai glosado.
_TEXTO_LEITURA = ('<sup>1</sup> Ōlim avus nauta erat et cum amīcīs ad īnsulās longinquās nāvigābat. '
                  '<sup>2</sup> Avia in ōrā habitābat et nautās exspectābat. '
                  '<sup>3</sup> Nunc avus nōn iam nāvigat: in casā manet et fābulās nārrat. '
                  '<sup>4</sup> Crās autem Titus et Flāvia cum avō ad īnsulam iterum nāvigābunt. '
                  '<sup>5</sup> Titus rēmōs portābit, Flāvia cibum parābit, avus nāviculam dūcet. '
                  '<sup>6</sup> Avia in ōrā erit et puerōs exspectābit.')

LICAO = dict(
    slug='12-o-imperfeito-e-o-futuro', titulo='Imperfeito e futuro do indicativo', titulo_latim='Dē imperfectō et futūrō', tempo='75 min',
    resumo='O sistema do infectum: presente, imperfeito e futuro formados do mesmo tema. O imperfeito com o sinal -ba- e seus valores (ação em curso, hábito, tentativa); os dois futuros, -bō/-bis na 1ª e 2ª conjugações e -am/-ēs na 3ª e 4ª; eram e erō; e um procedimento para não confundir regēs (futuro) com monēs (presente).',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['infectum', 'tema do presente', 'sinal de tempo', 'imperfeito do indicativo', 'sinal -ba-', 'eram (imperfeito de esse)',
             'imperfeito durativo, habitual e conativo', 'pretérito imperfeito português', 'futuro do indicativo', 'futuro em -bō (1ª e 2ª)',
             'futuro em -am/-ēs (3ª, 3ª em -iō e 4ª)', 'erō (futuro de esse)', 'regēs × monēs', 'presente, imperfeito ou futuro: procedimento',
             'futuro latino × "vou fazer"', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 6: as terminações pessoais, o presente de esse e das quatro conjugações (amō, moneō, regō, audiō e capiō) e a entrada de dicionário do verbo, que diz a conjugação pelo infinitivo. Os exemplos usam sobretudo nomes da 1ª e da 2ª declinação (capítulos 4 e 5) e o vocabulário do texto do capítulo 8; as poucas palavras da 3ª declinação (capítulo 9) vêm glosadas.',
                       licoes=['06-o-presente-do-indicativo']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 96 (terminações pessoais), § 97 (o tema do presente forma presente, imperfeito e futuro do indicativo), § 100 (sum: imperfeito eram, futuro erō), §§ 101, 103, 105, 107 (imperfeito e futuro de amō, moneō, regō, audiō), §§ 109.1 e 110 (verbos em -iō; capiō: capiēbam, capiam), § 257 (os tempos: época e tipo de ação), § 260 (imperfeito: ação em curso, descrição, hábito, tentativa, começo), § 261 (futuro: o latim é mais exato que o inglês; valor de imperativo)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 160 (os tempos do indicativo), § 165 (vocā-bā-s: tema, sinal de tempo e terminação pessoal), § 167 (vogal longa abreviada antes de -m, -t, -nt), § 168.b–d e nota de rodapé 2 (formação do imperfeito e dos dois futuros; origem de -bam), § 170 (sum; ES vira ER no imperfeito), § 175 (tema do presente = infinitivo sem -re), § 188 (verbos em -iō), §§ 470–471 (imperfeito: descritivo, contínuo, habitual, conativo e incoativo), § 472 (futuro), § 597 (a palavra mais importante vem primeiro)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 105 (tempos; rogabam, "I was asking"), § 115 (sum: ero, eram), §§ 117–118 (paradigmas de moneo e rego: monebam, regebam), § 147 (tempos derivados do tema do presente: imperfeito a-bam, e-bam, -ebam; futuro a-bo, e-bo, -am)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 80 (os seis tempos: "pretérito imperfeito", "futuro imperfeito"), n. 82 (esse: éram, éro), n. 85 (formação, a partir do presente, do imperfeito em -ābam/-ēbam e do futuro em -bo/-ebo ou -am, -es)', tipo='dominio_publico'),
        referencia('Grammática histórica da língua portuguêsa', 'António Garcia Ribeiro de Vasconcellos', url='https://archive.org/details/grammticahist00vascuoft', nota='Paris/Lisboa, Aillaud, 1901; Liv. I, § 97 (b intervocálico: amabat > amava, faciebat > fazia); Liv. II, §§ 232 e 235 (perda do futuro latino; futuro com o infinitivo + haver: amar hei > amarei); conferido no scan do archive.org', tipo='dominio_publico'),
        referencia('An Introduction to Vulgar Latin', 'C. H. Grandgent', url='https://archive.org/details/cu31924021623800', nota='Boston, Heath, 1907; §§ 125–129 e 411 (o futuro clássico sai do uso; infinitivo + habeo; mesóclise portuguesa), § 318 (b intervocálico), §§ 420–421 (imperfeito: -ēbam, -ībam popular, -ea); conferido no scan do archive.org', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Jo 1,1; Jo 8,32; Mt 5,8', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', nota='frases autênticas das seções 4 e 6 (texto conferido na Wikisource latina, "Vulgata Clementina/Evangelium Secundum Joannem", caps. 1 e 8, e "Vulgata Clementina/Evangelium Secundum Matthaeum", cap. 5; macrons acrescentados)', tipo='dominio_publico'),
    ],
    objetivos=[
        'Explicar por que presente, imperfeito e futuro formam um só sistema, o <i>infectum</i>, construído sobre o tema do presente.',
        'Formar e reconhecer o imperfeito ativo nas quatro conjugações (<i>amābam, monēbam, regēbam, audiēbam, capiēbam</i>) e o de <i>esse</i> (<i>eram</i>).',
        'Formar e reconhecer o futuro ativo nos seus dois sistemas, <i>amābō, monēbō</i> e <i>regam, capiam, audiam</i>, e o de <i>esse</i> (<i>erō</i>).',
        'Decidir, por um procedimento em passos, se uma forma é presente, imperfeito ou futuro, sem confundir <i>regēs, reget</i> (futuro) com <i>monēs, monet</i> (presente).',
        'Traduzir o imperfeito (ação em curso, hábito, tentativa) e o futuro para o português e analisar palavra a palavra João 1,1 e 8,32.',
    ],
    secoes=[
        ('Três tempos, um tema: o infectum', f'''
<p>No capítulo 6 você aprendeu o presente. O indicativo latino tem seis tempos ao todo (Bennett § 257; A&amp;G § 160; Ravizza n. 80), mas eles não são seis coisas soltas: dividem-se em dois grupos de três, e cada grupo se constrói sobre um <b>tema</b> diferente. O primeiro grupo é o do <b>tema do presente</b>, o mesmo que você já usa: segundo Bennett (§ 97), dele saem o presente, o imperfeito e o futuro do indicativo. Para achá-lo, basta tirar o <i>-re</i> do infinitivo (A&amp;G § 175): <i>amā-re</i> → <i>amā-</i>, <i>monē-re</i> → <i>monē-</i>, <i>audī-re</i> → <i>audī-</i>; na 3ª conjugação sobra <i>rege-</i>, com um <i>e</i> breve que muda de timbre ou desaparece conforme a forma, como você viu em <i>regō, regis, regunt</i>.</p>
<p>Os gramáticos chamam esse grupo de <b><i>infectum</i></b> ("não acabado"), porque os três tempos apresentam a ação em andamento, sem dizer que ela terminou. Bennett mostra isso numa tabela (§ 257): <i>scrībō</i>, "escrevo, estou escrevendo"; <i>scrībēbam</i>, "eu estava escrevendo"; <i>scrībam</i>, "escreverei, estarei escrevendo". A ação está em curso no presente, no passado ou no futuro. O outro grupo, o do <b><i>perfectum</i></b> (perfeito, mais-que-perfeito e futuro perfeito), apresenta a ação concluída e usa outro tema (<i>amāv-</i>, <i>rēx-</i>): é o assunto do capítulo 13.</p>
<p>A vantagem prática é grande: para o imperfeito e o futuro você não precisa decorar nenhum tema novo. Basta pôr, entre o tema e as terminações pessoais do capítulo 6, um pequeno elemento que marca o tempo, o <b>sinal de tempo</b>. Allen &amp; Greenough (§ 165) analisam assim a forma <i>vocābās</i>, "chamavas": <i>vocā-</i> (tema) + <i>-bā-</i> (sinal do imperfeito) + <i>-s</i> (terminação da 2ª pessoa do singular). Toda forma deste capítulo se lê com essa mesma divisão em três peças.</p>
{tabela(['Tempo', 'Sinal', 'Exemplo dividido', 'Forma', 'Português'], [
    ['Presente', '(nenhum)', 'amā · s', 'amās', 'amas, você ama'],
    ['Imperfeito', '<b>-bā-</b>', 'amā · <b>bā</b> · s', 'amābās', 'amavas, você amava'],
    ['Futuro (1ª e 2ª conj.)', '<b>-bi-</b>', 'amā · <b>bi</b> · s', 'amābis', 'amarás, você vai amar'],
    ['Futuro (3ª e 4ª conj.)', '<b>-ē-</b>', 'reg · <b>ē</b> · s', 'regēs', 'regerás, você vai reger'],
], 'O tema do presente com e sem sinal de tempo (2ª pessoa do singular)', latim_cols=(1, 2, 3))}
<p>Um aviso de nomenclatura. A gramática portuguesa chama "pretérito imperfeito" o tempo de <i>amava</i> e "futuro do presente" o de <i>amarei</i>. Ravizza, seguindo a tradição latina, chama o futuro de <b>"futuro imperfeito"</b> (n. 80), para distingui-lo do futuro perfeito ("terei amado"). Neste livro, "imperfeito" é sempre o pretérito imperfeito, e "futuro", sem adjetivo, é o futuro do <i>infectum</i>.</p>
'''),
        ('O imperfeito: o sinal -ba-', f'''
<p>O imperfeito tem a formação mais regular de todo o verbo latino. Ao tema do presente junta-se o sinal <b><i>-bā-</i></b> e, depois dele, as terminações pessoais. Há só um detalhe novo: a 1ª pessoa do singular termina em <b><i>-m</i></b>, e não em <i>-ō</i>. Você já conhece esse <i>-m</i> de <i>sum</i> (capítulo 6); no imperfeito ele aparece em todos os verbos: <i>amābam</i>, "eu amava".</p>
<p>A vogal que precede o <i>-ba-</i> é sempre <b>longa</b>. Na 1ª e na 2ª conjugação é a própria vogal do tema: <i>amā-bam</i>, <i>monē-bam</i>. Na 3ª e na 4ª aparece um <b><i>ē</i> longo</b> que o presente não tinha: <i>reg-ē-bam</i>, <i>audi-ē-bam</i>, e também <i>capi-ē-bam</i>, que conserva o <i>i</i> porque, pela regra prática de Bennett (§ 109.1), os verbos em <i>-iō</i> seguem a 4ª onde há duas vogais seguidas. Ravizza resume assim: na primeira conjugação acrescenta-se <i>-ābam</i>; na segunda, terceira e quarta, <i>-ēbam</i> (n. 85). Os paradigmas completos estão em Bennett §§ 101, 103, 105, 107 e 110.</p>
{tabela(['Pessoa', '1ª · amō', '2ª · moneō', '3ª · regō', '4ª · audiō', '3ª em -iō · capiō'], [
    ['1ª sing.', 'amā<b>bam</b>', 'monē<b>bam</b>', 'regē<b>bam</b>', 'audiē<b>bam</b>', 'capiē<b>bam</b>'],
    ['2ª sing.', 'amā<b>bās</b>', 'monē<b>bās</b>', 'regē<b>bās</b>', 'audiē<b>bās</b>', 'capiē<b>bās</b>'],
    ['3ª sing.', 'amā<b>bat</b>', 'monē<b>bat</b>', 'regē<b>bat</b>', 'audiē<b>bat</b>', 'capiē<b>bat</b>'],
    ['1ª pl.', 'amā<b>bāmus</b>', 'monē<b>bāmus</b>', 'regē<b>bāmus</b>', 'audiē<b>bāmus</b>', 'capiē<b>bāmus</b>'],
    ['2ª pl.', 'amā<b>bātis</b>', 'monē<b>bātis</b>', 'regē<b>bātis</b>', 'audiē<b>bātis</b>', 'capiē<b>bātis</b>'],
    ['3ª pl.', 'amā<b>bant</b>', 'monē<b>bant</b>', 'regē<b>bant</b>', 'audiē<b>bant</b>', 'capiē<b>bant</b>'],
], 'O imperfeito do indicativo ativo nas quatro conjugações', latim_cols=(1, 2, 3, 4, 5))}
<p>Repare na quantidade do próprio sinal: <i>-bā-</i> é longo em <i>amābās, amābāmus, amābātis</i>, mas breve em <i>amābam, amābat, amābant</i>. É a mesma regra que você viu em <i>amat, amant</i>: uma vogal longa se abrevia antes de <i>-m</i>, <i>-t</i> e <i>-nt</i> finais (A&amp;G § 167). Uma regra, aplicada em toda parte.</p>
<p>O acento também fica previsível. Como a vogal antes do sinal é longa, ela leva o acento sempre que for a penúltima sílaba: a<u>mā</u>bam, mo<u>nē</u>bam, re<u>gē</u>bam, audi<u>ē</u>bam. Nas formas mais longas, a penúltima é o próprio <i>bā</i>, longo: amā<u>bā</u>mus, regē<u>bā</u>tis. Cuidado com a 3ª conjugação: no infinitivo se diz <u>re</u>gere, com a penúltima breve, mas no imperfeito o <i>ē</i> é longo e puxa o acento, re<u>gē</u>bam.</p>
<h3>O imperfeito de esse: eram</h3>
<p><i>Esse</i> não usa <i>-ba-</i>. O imperfeito tem um radical próprio, <i>er-</i>, seguido de <i>-a-</i> e das terminações, com o mesmo <i>-m</i> na primeira pessoa (Bennett § 100). Allen &amp; Greenough explicam a origem do radical: a raiz de <i>sum</i> é <i>ES</i>, que no imperfeito vira <i>ER</i> (§ 170), pela mesma troca de <i>s</i> por <i>r</i> entre vogais que você verá em outras palavras.</p>
{tabela_conjugacao('Imperfeito do indicativo de esse', [
    ('er<b>am</b>', 'eu era, estava'), ('er<b>ās</b>', 'tu eras, você era'), ('er<b>at</b>', 'ele/ela era, estava; havia'),
    ('er<b>āmus</b>', 'nós éramos, estávamos'), ('er<b>ātis</b>', 'vós éreis, vocês eram'), ('er<b>ant</b>', 'eles/elas eram, estavam; havia')])}
<p>O português herdou essas formas quase sem mudança: <i>eram</i>, era; <i>erās</i>, eras; <i>erant</i>, eram. Mas atenção ao <b>falso amigo</b>: o latim <i>eram</i> é "eu era", e o português "eram" corresponde ao latim <i>erant</i>. O uso não muda em relação ao presente: com predicativo no nominativo, <i>erat</i> é "era, estava" (<i>Agricola laetus erat</i>, "o agricultor estava contente"); sem predicativo, é o "há" do capítulo 6 levado ao passado, "havia" (<i>In īnsulā erat vīlla</i>, "havia uma casa na ilha"). Os compostos de <i>sum</i> e o verbo <i>possum</i>, "poder", seguem esse modelo, mas ficam para o capítulo 26.</p>
{exemplos([('Puerī in hortō cantā<b>bant</b>.', 'Os meninos cantavam (estavam cantando) no jardim.'), ('Magistra fābulās nārrā<b>bat</b>; puerī audiē<b>bant</b>.', 'A professora contava histórias; os meninos ouviam.'), ('Servī equōs dūcē<b>bant</b>.', 'Os escravos conduziam os cavalos. (<i>dūcō, -ere</i>, 3ª: <i>dūc-ē-bant</i>)'), ('Nautae er<b>āmus</b> et in īnsulā habitā<b>bāmus</b>.', 'Éramos marinheiros e morávamos na ilha.')])}
'''),
        ('O que o imperfeito significa', f'''
<p>O nome já diz o essencial: o imperfeito apresenta a ação como <b>não acabada</b>, vista no meio do caminho, no passado. Bennett (§ 260) e Allen &amp; Greenough (§§ 470–471) distinguem os valores que nascem daí, e todos têm correspondente direto no português:</p>
<ul>
<li><b>Ação em curso no passado</b> (Bennett § 260.1): <i>librum legēbam</i>, "eu estava lendo um livro", "eu lia um livro". Por isso o imperfeito é o tempo da <b>descrição</b>, do pano de fundo (§ 260.1.a; A&amp;G § 471.a).</li>
<li><b>Ação repetida ou habitual</b> (§ 260.2): <i>lēgātōs interrogābat</i>, "ele interrogava repetidamente os embaixadores"; "costumava", "vivia fazendo".</li>
<li><b>Tentativa</b>, o imperfeito <b>conativo</b> (§ 260.3; A&amp;G § 471.c): a ação foi iniciada ou intentada, mas não se completou: "tentava", "procurava".</li>
<li><b>Começo da ação</b>, o imperfeito <b>incoativo</b> (§ 260.3), muitas vezes com <i>iam</i>, "já" (A&amp;G § 471.c, nota): "começava a", "já ia".</li>
</ul>
<p>Para quem fala português, o imperfeito é o tempo mais fácil do latim, porque o nosso pretérito imperfeito tem exatamente essas funções. "Eu lia quando você chegou" é ação em curso; "nas férias, a gente ia à praia" é hábito; "o ladrão já fugia quando o guarda o agarrou" é tentativa ou começo. Na maioria das frases, portanto, traduza o imperfeito latino pelo imperfeito português (<i>amābat</i>, "amava"; <i>legēbat</i>, "lia") e só mude a tradução quando o contexto pedir: "estava lendo" para destacar o andamento, "costumava ler" para o hábito, "tentava" quando a ação não se completou.</p>
{exemplos([('Puer librum legē<b>bat</b>.', 'O menino lia (estava lendo) um livro. (ação em curso)'), ('Avus fābulās nārrā<b>bat</b>.', 'O avô contava (costumava contar) histórias. (hábito)'), ('Agricola equum in agrum dūcē<b>bat</b>, sed equus nōn veniē<b>bat</b>.', 'O agricultor tentava levar o cavalo para o campo, mas o cavalo não vinha. (conativo: o <i>sed</i> mostra que a ação não se completou; <i>in</i> + acusativo, "para dentro de")'), ('In silvā er<b>ant</b> multī lupī.', 'Na floresta havia muitos lobos. (descrição; <i>erant</i> sem predicativo)')])}
<p>O imperfeito não é o único tempo passado do latim. Quando a ação é simplesmente <b>registrada como fato concluído</b> ("ele leu", "amou"), o latim usa o perfeito, que você aprende no capítulo 13. Allen &amp; Greenough dão o par <i>rēx erat</i> e <i>rēx fuit</i>, ambos "era rei": o primeiro <b>descreve</b> a situação; o segundo apenas a <b>afirma</b> (§ 470, nota). É a mesma diferença entre "era" e "foi" em português, e por isso o imperfeito latino nunca se traduz por "amou" ou "leu".</p>
{observacao('De amābam a "amava"', 'O <i>-va</i> do português <i>amava</i> continua o <i>-ba-</i> de <i>amābam</i>: entre vogais, o <i>b</i> latino passou a <i>v</i>, como em <i>fabam</i> &gt; "fava". Nas outras conjugações, o <i>b</i> caiu e <i>-ēbam</i> deu o <i>-ia</i> de "temia" (<i>timēbam</i>) e "fazia" (<i>faciēbam</i>); na 4ª, "ouvia" continua a forma popular <i>audībam</i>, que convivia com <i>audiēbam</i>. É o que registram as gramáticas históricas: Vasconcellos, <i>Grammática histórica da língua portuguêsa</i> (1901), Liv. I, § 97; Grandgent, <i>An Introduction to Vulgar Latin</i> (1907), §§ 318, 420–421. Allen &amp; Greenough lembram que o próprio <i>-bam</i> foi, na origem, um verbo independente que significava "eu era, eu estava", da mesma raiz de <i>fuī</i>: <i>vidē-bam</i> seria algo como "eu estava a ver" (§ 168, nota de rodapé 2).')}
{dica('<b>O que não transportar do português.</b> O imperfeito do português do Brasil tem dois usos que o latim não conhece: o pedido polido ("eu queria um café") e o condicional coloquial ("se eu pudesse, eu ia"). No latim, as duas ideias pedem o subjuntivo (capítulos 32 e 36). Ao passar frases para o latim, use o imperfeito do indicativo só para o passado real: em curso, habitual ou tentado.')}
'''),
        ('O futuro: dois sistemas', f'''
<p>O futuro é o tempo que exige mais atenção, porque o latim tem <b>dois modos de formá-lo</b>, conforme a conjugação. Allen &amp; Greenough descrevem os dois em § 168.c–d; Kennedy os mostra lado a lado na tabela dos tempos derivados do tema do presente (§ 147).</p>
<h3>1ª e 2ª conjugações: -bō, -bis, -bit</h3>
<p>Na 1ª e na 2ª conjugação o futuro se forma como o imperfeito: tema + sinal com <i>b</i> + terminações. A diferença está na vogal que segue o <i>b</i>: <b><i>-bō, -bis, -bit, -bimus, -bitis, -bunt</i></b>. Se essa lista lhe parece familiar, é porque é: depois do <i>b</i> vêm exatamente as vogais e terminações do presente de <i>regō</i>, <i>-ō, -is, -it, -imus, -itis, -unt</i>. Quem sabe <i>regō, regis, regit</i> já sabe <i>amābō, amābis, amābit</i>.</p>
<h3>3ª, 3ª em -iō e 4ª conjugações: -am, -ēs, -et</h3>
<p>Na 3ª e na 4ª conjugação (e nos verbos em <i>-iō</i>) não há <i>b</i>. O futuro usa outra série: <b><i>-am</i></b> na 1ª pessoa do singular e <b><i>ē</i></b> em todas as outras, <b><i>-am, -ēs, -et, -ēmus, -ētis, -ent</i></b>. Na 3ª conjugação essas terminações se juntam à raiz (<i>reg-am</i>); na 4ª e nos verbos em <i>-iō</i>, ao tema terminado em <i>i</i> (<i>audi-am</i>, <i>capi-am</i>), de novo pela regra de Bennett § 109.1. As vogais se abreviam antes de <i>-m</i>, <i>-t</i> e <i>-nt</i> (A&amp;G § 167): <i>regam, reget, regent</i> têm vogal breve; <i>regēs, regēmus, regētis</i>, longa.</p>
{tabela(['Pessoa', '1ª · amō', '2ª · moneō', '3ª · regō', '4ª · audiō', '3ª em -iō · capiō'], [
    ['1ª sing.', 'amā<b>bō</b>', 'monē<b>bō</b>', 'reg<b>am</b>', 'audi<b>am</b>', 'capi<b>am</b>'],
    ['2ª sing.', 'amā<b>bis</b>', 'monē<b>bis</b>', 'reg<b>ēs</b>', 'audi<b>ēs</b>', 'capi<b>ēs</b>'],
    ['3ª sing.', 'amā<b>bit</b>', 'monē<b>bit</b>', 'reg<b>et</b>', 'audi<b>et</b>', 'capi<b>et</b>'],
    ['1ª pl.', 'amā<b>bimus</b>', 'monē<b>bimus</b>', 'reg<b>ēmus</b>', 'audi<b>ēmus</b>', 'capi<b>ēmus</b>'],
    ['2ª pl.', 'amā<b>bitis</b>', 'monē<b>bitis</b>', 'reg<b>ētis</b>', 'audi<b>ētis</b>', 'capi<b>ētis</b>'],
    ['3ª pl.', 'amā<b>bunt</b>', 'monē<b>bunt</b>', 'reg<b>ent</b>', 'audi<b>ent</b>', 'capi<b>ent</b>'],
], 'O futuro do indicativo ativo nas quatro conjugações', latim_cols=(1, 2, 3, 4, 5))}
<p>Por que dois sistemas? Allen &amp; Greenough explicam que as terminações <i>-am, -ēs</i> da 3ª e da 4ª são, na origem, terminações de subjuntivo usadas com sentido de futuro (§ 168.d). Uma consequência prática: <i>regam</i>, <i>audiam</i> e <i>capiam</i> servem também de presente do subjuntivo, como se vê no paradigma de <i>capiō</i> em Bennett (§ 110). Por enquanto, no indicativo, leia-os como futuro; o subjuntivo vem no capítulo 32. Quanto ao acento, siga a regra de sempre: a<u>mā</u>bō, mo<u>nē</u>bimus (penúltima breve, acento na antepenúltima), re<u>gē</u>mus, audi<u>ē</u>tis, <u>re</u>gent.</p>
<h3>O futuro de esse: erō</h3>
<p>O futuro de <i>esse</i> usa o mesmo radical <i>er-</i> do imperfeito e as terminações que você acabou de ver depois do <i>b</i>: <i>er-ō, er-is, er-it, er-imus, er-itis, er-unt</i> (Bennett § 100; Kennedy § 115; Ravizza n. 82). Basta comparar a vogal depois do <i>r</i>: <i>a</i> no imperfeito (<i>erat</i>, "era"), <i>i</i> ou <i>u</i> no futuro (<i>erit</i>, "será"; <i>erunt</i>, "serão").</p>
{tabela_conjugacao('Futuro do indicativo de esse', [
    ('er<b>ō</b>', 'eu serei, estarei'), ('er<b>is</b>', 'tu serás, você será'), ('er<b>it</b>', 'ele/ela será, estará; haverá'),
    ('er<b>imus</b>', 'nós seremos, estaremos'), ('er<b>itis</b>', 'vós sereis, vocês serão'), ('er<b>unt</b>', 'eles/elas serão, estarão; haverá')])}
<h3>Como traduzir o futuro</h3>
<p>O futuro latino indica o que vai acontecer (A&amp;G § 472) e, como os outros tempos do <i>infectum</i>, pode também apresentar a ação em andamento: <i>scrībam</i> é "escreverei" ou "estarei escrevendo" (Bennett § 257). Em português do Brasil há duas traduções igualmente boas: o futuro simples, mais formal (<i>amābō</i>, "amarei"), e a perífrase com "ir", mais corrente na fala (<i>amābō</i>, "vou amar"). Escolha conforme o registro do texto; o latim clássico, porém, não tem perífrase com "ir": é sempre uma palavra só.</p>
{exemplos([('Crās agricola in agrō labōrā<b>bit</b>.', 'Amanhã o agricultor trabalhará (vai trabalhar) no campo. (<i>crās</i>, amanhã)'), ('Puerī librōs leg<b>ent</b>.', 'Os meninos lerão (vão ler) os livros. (<i>legō</i>, 3ª: <i>leg-ent</i>, não "legunt")'), ('Fābulās poētae audi<b>ēmus</b>.', 'Ouviremos as histórias do poeta.'), ('Puella rosam capi<b>et</b>.', 'A menina vai pegar a rosa.'), ('Beātī mundō corde: quoniam ipsī Deum vidē<b>bunt</b>.', 'Bem-aventurados os puros de coração, porque eles verão a Deus. (Mt 5,8; <i>beātus, -a, -um</i>, feliz, bem-aventurado; <i>mundus, -a, -um</i>, puro; <i>corde</i>, ablativo de <i>cor, cordis</i> (n.), coração; <i>quoniam</i>, porque; <i>ipsī</i>, "eles mesmos", capítulo 15)')])}
{observacao('Amābō e "amarei" não são parentes', 'O futuro em <i>-bō</i> e em <i>-am</i> caiu em desuso no latim falado tardio e não passou ao português. Em seu lugar, as línguas românicas construíram um futuro novo com o infinitivo seguido de <i>habēre</i>: "amar + hei" deu "amarei", e "amar + há" deu "amará" (Grandgent §§ 125–129 e 411; Vasconcellos, Liv. II, §§ 232 e 235). A antiga separação das duas peças ainda se vê na mesóclise: "amá-lo-ei". Por isso o futuro português não se parece com <i>amābō</i>, e a perífrase "vou amar" é, de certo modo, a repetição da mesma história com outro auxiliar.')}
<p>Por fim, o latim é mais exato que muitas línguas modernas no uso do futuro (Bennett § 261.1): quando uma oração subordinada se refere ao futuro, ele também a põe no futuro. O português faz algo parecido com o futuro do subjuntivo, e é por esse tempo que você deve traduzir: <i>Sī puerī labōrā<b>bunt</b>, agricola laetus <b>erit</b></i>, "se os meninos trabalharem, o agricultor ficará contente" (<i>sī</i>, "se"). Allen &amp; Greenough dão um exemplo de Cícero, <i>Sānābimur sī volēmus</i>, "seremos curados se quisermos" (§ 472.b).</p>
'''),
        ('Presente, imperfeito ou futuro? Um procedimento', f'''
<p>Os três tempos do <i>infectum</i> usam as mesmas terminações pessoais; o que os separa é o que vem antes delas. Na leitura, a dúvida aparece sempre nos mesmos lugares, e um procedimento fixo evita quase todos os erros. Siga os passos na ordem:</p>
<ol>
<li><b>Ache a terminação pessoal</b> (<i>-ō/-m, -s, -t, -mus, -tis, -nt</i>) e separe o que vem antes dela.</li>
<li><b>Há <i>-ba-</i> antes da terminação</b> (<i>-bam, -bās, -bat, -bāmus, -bātis, -bant</i>)? É <b>imperfeito</b>, em qualquer conjugação. De <i>esse</i>, o imperfeito é <i>eram, erās, erat</i>…</li>
<li><b>Há <i>b</i> seguido de <i>ō, i, u</i></b> (<i>-bō, -bis, -bit, -bimus, -bitis, -bunt</i>)? É <b>futuro da 1ª ou da 2ª</b> conjugação. De <i>esse</i>: <i>erō, eris, erit</i>…</li>
<li><b>Confira se o <i>b</i> não é da raiz.</b> Em <i>scrībit</i> e <i>habent</i> o <i>b</i> pertence ao verbo (<i>scrībō</i>, <i>habeō</i>), e as formas são presente. Compare com a entrada de dicionário: <i>scrīb-ēba-t</i> é imperfeito, <i>hab-ē-bi-t</i> é futuro.</li>
<li><b>Sem sinal com <i>b</i>, vá ao dicionário.</b> A forma é presente ou futuro em <i>-am/-ēs</i>, e quem decide é a conjugação, isto é, o infinitivo. Com <i>-ēs, -et, -ēmus, -ētis, -ent</i>, um verbo da <b>2ª</b> (<i>-ēre</i>) está no <b>presente</b> (<i>monēs</i>); um da <b>3ª</b>, da <b>3ª em -iō</b> ou da <b>4ª</b> está no <b>futuro</b> (<i>regēs, capiēs, audiēs</i>). O presente dessas conjugações tem <i>i</i> ou <i>u</i>: <i>regis, regit, regunt; audīs, audit, audiunt</i>. Na 1ª conjugação, o indicativo não tem formas em <i>-ēs</i>: <i>amās</i> é presente e <i>amābis</i>, futuro.</li>
</ol>
<p>O passo 5 é a armadilha clássica. Observe a tabela: o presente de <i>moneō</i> e o futuro de <i>regō</i> têm, da 2ª pessoa do singular em diante, <b>exatamente as mesmas terminações</b>. Nem o macron ajuda, porque o <i>ē</i> é longo nos dois; só a 1ª pessoa (<i>moneō</i> × <i>regam</i>) e o dicionário distinguem.</p>
{tabela(['Pessoa', 'moneō · presente', 'regō · futuro', 'regō · presente', 'moneō · futuro'], [
    ['1ª sing.', 'mone<b>ō</b>', 'reg<b>am</b>', 'reg<b>ō</b>', 'monē<b>bō</b>'],
    ['2ª sing.', 'monē<b>s</b>', 'reg<b>ēs</b>', 'reg<b>is</b>', 'monē<b>bis</b>'],
    ['3ª sing.', 'mone<b>t</b>', 'reg<b>et</b>', 'reg<b>it</b>', 'monē<b>bit</b>'],
    ['1ª pl.', 'monē<b>mus</b>', 'reg<b>ēmus</b>', 'reg<b>imus</b>', 'monē<b>bimus</b>'],
    ['2ª pl.', 'monē<b>tis</b>', 'reg<b>ētis</b>', 'reg<b>itis</b>', 'monē<b>bitis</b>'],
    ['3ª pl.', 'mone<b>nt</b>', 'reg<b>ent</b>', 'reg<b>unt</b>', 'monē<b>bunt</b>'],
], 'A armadilha: o presente da 2ª e o futuro da 3ª têm as mesmas terminações', latim_cols=(1, 2, 3, 4))}
<p>Por isso o capítulo 6 insistiu em aprender o infinitivo junto com cada verbo. Compare <i>docet</i> e <i>dūcet</i>: a mesma terminação <i>-et</i>, tempos diferentes, e só a entrada de dicionário explica por quê. <i>doceō, -ēre</i> é da 2ª, e <i>docet</i> é presente, "ensina"; <i>dūcō, -ere</i> é da 3ª, e <i>dūcet</i> é futuro, "conduzirá". Num texto sem macrons a situação é a mesma, e a solução também.</p>
{comparacao('Pares que enganam', ['Forma', 'Tempo', 'Por quê', 'Par'], [
    ['regēs · reget', 'futuro (3ª)', '<i>regō, -ere</i> é da 3ª: <i>ē/e</i> = futuro', '<i>regis · regit</i>, presente'],
    ['monēs · monet', 'presente (2ª)', '<i>moneō, -ēre</i> é da 2ª: o <i>ē</i> é do tema', '<i>monēbis · monēbit</i>, futuro'],
    ['audiet · audient', 'futuro (4ª)', '<i>e</i> depois do <i>i</i> do tema', '<i>audit · audiunt</i>, presente'],
    ['capiet · capient', 'futuro (3ª em -iō)', 'como <i>audiet</i>', '<i>capit · capiunt</i>, presente'],
    ['regēbam', 'imperfeito (3ª)', '<i>-ba-</i>: imperfeito em qualquer conjugação', '<i>monēbō</i>, futuro (2ª): <i>-bō</i>'],
    ['amābant', 'imperfeito', '<i>-ba-</i>', '<i>amābunt</i>, futuro: <i>-bu-</i>'],
    ['erat · erant', 'imperfeito de esse', '<i>a</i> depois de <i>er-</i>', '<i>erit · erunt</i>, futuro'],
])}
{dica('<b>Uma frase para lembrar.</b> "B com <i>a</i>, passado; B com <i>i, o, u</i>, futuro; sem B, pergunte ao dicionário." O <i>b</i> de tempo só existe na 1ª e na 2ª conjugação para o futuro, mas em todas para o imperfeito.')}
'''),
        ('Análise gramatical: dois versículos de João', f'''
<p>O início do Evangelho de João, na Vulgata, é um dos textos latinos mais conhecidos, e é feito quase só de imperfeitos de <i>esse</i>. Um pouco adiante, no capítulo 8, um versículo curto traz os dois sistemas de futuro numa mesma frase. Os dois foram conferidos no texto da Vulgata Clementina publicado na Wikisource latina, que não traz macrons; aqui eles foram acrescentados. <i>Vēritās</i> é da 3ª declinação (capítulo 9) e <i>vōs</i> é pronome (capítulo 14); o quadro dá a forma de cada palavra.</p>
{exemplos([('In prīncipiō erat Verbum, et Verbum erat apud Deum, et Deus erat Verbum.', 'No princípio era o Verbo, e o Verbo estava junto de Deus, e o Verbo era Deus. (Jo 1,1)'), ('Et cognōscētis vēritātem, et vēritās līberābit vōs.', 'E conhecereis a verdade, e a verdade vos libertará. (Jo 8,32)')])}
{analise('Jo 1,1 e 8,32, palavra a palavra', [
    ('In prīncipiō', 'in + prīncipium, -ī (n.), princípio, começo', 'ablativo singular, 2ª declinação, com <i>in</i>', 'tempo/lugar: "no princípio"'),
    ('erat', 'sum, esse, ser', 'imperfeito, 3ª pessoa do singular (<i>er-a-t</i>)', 'verbo: "era, existia"'),
    ('Verbum', 'verbum, -ī (n.), palavra; o Verbo', 'nominativo singular, 2ª declinação (neutro)', 'sujeito de <i>erat</i>'),
    ('et', 'et, conjunção', 'invariável', 'liga as orações'),
    ('Verbum erat', 'verbum, -ī · sum, esse', 'nominativo singular · imperfeito, 3ª sing.', 'sujeito e verbo: "o Verbo estava"'),
    ('apud Deum', 'apud + acusativo, junto de · deus, -ī (m.), Deus', 'acusativo singular, 2ª declinação', 'lugar: "junto de Deus"'),
    ('Deus', 'deus, -ī (m.), Deus', 'nominativo singular', 'predicativo do sujeito, posto em primeiro lugar por ênfase'),
    ('erat Verbum', 'sum, esse · verbum, -ī', 'imperfeito, 3ª sing. · nominativo singular', 'cópula e sujeito'),
    ('cognōscētis', 'cognōscō, -ere (3ª), conhecer, vir a conhecer', 'futuro, 2ª pessoa do plural (<i>cognōsc-ētis</i>)', 'verbo; sujeito "vós" na terminação'),
    ('vēritātem', 'vēritās, -ātis (f.), verdade', 'acusativo singular, 3ª declinação (capítulo 9)', 'objeto direto de <i>cognōscētis</i>'),
    ('vēritās', 'vēritās, -ātis (f.)', 'nominativo singular', 'sujeito de <i>līberābit</i>'),
    ('līberābit', 'līberō, -āre (1ª), libertar', 'futuro, 3ª pessoa do singular (<i>līberā-bi-t</i>)', 'verbo'),
    ('vōs', 'pronome pessoal da 2ª pessoa do plural', 'acusativo plural (capítulo 14)', 'objeto direto: "vos"'),
])}
<p>Três observações. Em Jo 1,1, <i>erat</i> aparece três vezes e cobre três sentidos que o capítulo 6 ensinou para <i>est</i>: "existir" (<i>In prīncipiō erat Verbum</i>, sem predicativo), "estar" com expressão de lugar (<i>erat apud Deum</i>) e cópula (<i>Deus erat Verbum</i>). É o imperfeito descritivo: o texto não narra um acontecimento, descreve uma situação que já existia "no princípio".</p>
<p>Em <i>Deus erat Verbum</i> há dois nominativos, como em <i>Deus cāritās est</i> (capítulo 6). Lá o sujeito era <i>Deus</i>; aqui é <i>Verbum</i>, porque o versículo inteiro fala do Verbo, que já era o sujeito das duas orações anteriores. <i>Deus</i> vem em primeiro lugar porque, em latim, a palavra mais importante para quem fala tende a abrir a frase (A&amp;G § 597). A tradução portuguesa tradicional repõe a ordem do sujeito: "o Verbo era Deus".</p>
<p>Em Jo 8,32, os dois sistemas do futuro aparecem lado a lado. <i>Cognōscētis</i> é da 3ª conjugação (<i>cognōscō, -ere</i>): não tem <i>b</i>, e o <i>ē</i> antes de <i>-tis</i> é o do futuro, porque o presente seria <i>cognōscitis</i>. <i>Līberābit</i> é da 1ª: tema <i>līberā-</i>, sinal <i>-bi-</i>, terminação <i>-t</i>. O diagrama mostra a segunda oração:</p>
{diagrama_frase([('et', 'conjunção · liga as orações'), ('vēritās', 'nominativo sing. · sujeito'), ('līberābit', 'verbo · futuro: -bi-t, 3ª sing.'), ('vōs', 'acusativo pl. · objeto')], '<i>Et vēritās līberābit vōs</i> = E a verdade vos libertará. O <i>-t</i> pede um sujeito singular: <i>vēritās</i>, nominativo. O <i>-bi-</i> diz que a ação é futura, e o tema em <i>ā</i> diz que o verbo é da 1ª conjugação.')}
<h3>Resumo</h3>
<ul>
<li><b><i>Infectum</i></b>: presente, imperfeito e futuro saem do tema do presente; entre tema e terminação vem o sinal de tempo.</li>
<li><b>Imperfeito</b>: <i>-bam, -bās, -bat, -bāmus, -bātis, -bant</i> depois de <i>ā</i> (1ª), <i>ē</i> (2ª e 3ª) ou <i>iē</i> (4ª e <i>-iō</i>); <i>esse</i>: <i>eram, erās, erat</i>. Valores: em curso, hábito, tentativa, começo; traduza pelo imperfeito português.</li>
<li><b>Futuro, 1ª e 2ª</b>: <i>-bō, -bis, -bit, -bimus, -bitis, -bunt</i>. <b>3ª, <i>-iō</i> e 4ª</b>: <i>-am, -ēs, -et, -ēmus, -ētis, -ent</i>. <i>Esse</i>: <i>erō, eris, erit</i>. Traduza por "amarei" ou "vou amar".</li>
<li><b>Decisão</b>: <i>-ba-</i> = imperfeito; <i>-bō/-bi-/-bu-</i> = futuro (1ª e 2ª); sem <i>b</i>, o infinitivo decide: <i>monēs</i> é presente, <i>regēs</i> é futuro.</li>
</ul>
<p>No capítulo 13 você conhece o outro lado do verbo, o <i>perfectum</i>: o perfeito ("amei"), o mais-que-perfeito e o futuro perfeito, formados de um tema diferente e anunciados pelas partes principais do dicionário.</p>
'''),
    ],
    erros_comuns=[
        ('Ler <i>regēs, reget, regent</i> como presente, por analogia com <i>monēs, monet, monent</i>.', 'As terminações são as mesmas, mas os tempos são diferentes: na 2ª conjugação o <i>ē</i> é a vogal do tema e a forma é presente; na 3ª, na 3ª em <i>-iō</i> e na 4ª, o <i>ē/e</i> é o sinal do futuro. O presente de <i>regō</i> é <i>regis, regit, regunt</i>. Antes de traduzir, confira o infinitivo da entrada de dicionário.'),
        ('Formar o futuro da 3ª e da 4ª com <i>-bō</i>: "regēbō", "audiēbō", "capiēbō".', 'O futuro em <i>-bō, -bis</i> é só da 1ª e da 2ª conjugação (<i>amābō, monēbō</i>). Na 3ª e na 4ª o futuro é <i>regam, regēs</i>; <i>audiam, audiēs</i>; <i>capiam, capiēs</i>. Uma forma em <i>-ēba-</i> nesses verbos é sempre imperfeito: <i>regēbam</i>, "eu regia".'),
        ('Tomar qualquer <i>b</i> como sinal de tempo e ler <i>scrībit</i> ou <i>habent</i> como futuro ou imperfeito.', 'O <i>b</i> de <i>scrībō</i> e de <i>habeō</i> pertence à raiz do verbo. Tire a terminação e compare com a entrada de dicionário: <i>scrīb-it</i> é presente, "escreve"; <i>scrīb-ēba-t</i>, imperfeito; <i>scrīb-e-t</i>, futuro; <i>hab-ē-bi-t</i>, futuro, "terá".'),
        ('Traduzir <i>eram</i> por "eles eram", levado pelo português.', 'O latim <i>eram</i> é a 1ª pessoa do singular, "eu era"; o "eram" português corresponde a <i>erant</i>. Olhe sempre a terminação: <i>-m</i> é "eu", <i>-nt</i> é "eles". Pelo mesmo motivo, <i>erat</i> é "era" e <i>erit</i> é "será": a vogal depois de <i>er-</i> decide o tempo.'),
        ('Usar <i>regō</i>, <i>dūcō</i> ou <i>audiō</i> como 1ª pessoa do futuro ("eu regerei").', '<i>Regō, dūcō, audiō</i> são presente. A 1ª pessoa do futuro da 3ª e da 4ª conjugação termina em <i>-am</i>: <i>regam, dūcam, audiam</i>. O <i>-ō</i> só aparece no futuro da 1ª e da 2ª, e sempre depois do <i>b</i>: <i>amābō, monēbō</i> (e em <i>erō</i>).'),
        ('Traduzir o imperfeito pelo pretérito perfeito português: <i>legēbat</i>, "leu"; <i>amābant</i>, "amaram".', 'O imperfeito apresenta a ação em curso, repetida ou tentada: <i>legēbat</i> é "lia, estava lendo, costumava ler"; <i>amābant</i>, "amavam". O pretérito perfeito ("leu", "amaram") corresponde ao perfeito latino (<i>lēgit</i>, <i>amāvērunt</i>), do capítulo 13.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Reget ou monet?',
            'Num texto você encontra <i lang="la">reget</i> e, na linha seguinte, <i lang="la">monet</i>. As duas terminam em <i>-et</i>. Diga o tempo, a pessoa e o número de cada uma, e traduza.', [
            ('Qual é a terminação pessoal, e o que vem antes dela?', 'As duas terminam em <i>-t</i>, 3ª pessoa do singular. Antes dela há um <i>e</i> nas duas: <i>rege-t</i>, <i>mone-t</i>. Não há <i>b</i>, portanto não é imperfeito nem futuro da 1ª ou 2ª (passos 2 e 3 do procedimento).'),
            ('O que diz o dicionário?', '<i>regō, regere</i>: infinitivo em <i>-ere</i> breve, 3ª conjugação. <i>moneō, monēre</i>: infinitivo em <i>-ēre</i> longo, 2ª conjugação.'),
            ('Então, que tempo é cada forma?', 'Na 2ª conjugação, o <i>e</i> é a vogal do tema: <i>monet</i> é presente. Na 3ª, o presente seria <i>regit</i>, com <i>i</i>; o <i>e</i> de <i>reget</i> é o sinal do futuro (<i>regam, regēs, reget</i>).'),
            ('Como seriam as outras formas, para conferir?', 'O futuro de <i>moneō</i> é <i>monēbit</i>, com <i>-bi-</i>; o presente de <i>regō</i> é <i>regit</i>. Se as duas formas fossem do mesmo tempo, teriam de ser <i>monet</i> e <i>regit</i>, ou <i>monēbit</i> e <i>reget</i>.'),
            ('Traduza.', '<i>Reget</i>: "regerá, governará", "vai governar". <i>Monet</i>: "adverte, aconselha".'),
        ], 'Conclusão: diante de <i>-ēs, -et, -ēmus, -ētis, -ent</i> sem <i>b</i>, a forma sozinha não basta; a conjugação, dada pelo infinitivo, decide entre presente (2ª) e futuro (3ª e 4ª).'),
        pratica_guiada('Prática guiada 2 · O procedimento numa frase',
            'Analise e traduza: <i lang="la">Puella epistulam scrībēbat; crās magistra epistulam leget et puellam laudābit.</i> Vocabulário: <i>epistula, -ae</i> (f.), carta; <i>crās</i>, amanhã; <i>magistra, -ae</i> (f.), professora; <i>laudō, -āre</i>, louvar, elogiar.', [
            ('Quais são os verbos?', '<i>scrībēbat</i>, <i>leget</i> e <i>laudābit</i>, todos com <i>-t</i>: 3ª pessoa do singular. Os sujeitos serão <i>puella</i> e <i>magistra</i>, nominativos singulares.'),
            ('<i>Scrībēbat</i>: há dois <i>b</i>. Qual deles é o sinal de tempo?', 'O primeiro pertence à raiz de <i>scrībō, -ere</i> (3ª). Depois da raiz vem <i>-ēba-</i>: <i>scrīb-ēba-t</i>, imperfeito, "escrevia, estava escrevendo".'),
            ('<i>Leget</i>: não há <i>b</i>. Presente ou futuro?', 'O dicionário dá <i>legō, -ere</i>, 3ª conjugação. O presente seria <i>legit</i>; o <i>e</i> antes do <i>-t</i> é o do futuro: <i>leg-e-t</i>, "lerá". O advérbio <i>crās</i> confirma.'),
            ('<i>Laudābit</i>?', '<i>laudō, -āre</i>, 1ª conjugação: <i>laudā-bi-t</i>, futuro com o sinal <i>-bi-</i>, "elogiará, vai elogiar".'),
            ('Monte a tradução.', '"A menina estava escrevendo uma carta; amanhã a professora vai ler a carta e vai elogiar a menina." (ou "lerá a carta e elogiará a menina").'),
        ], 'Conclusão: o mesmo procedimento serve para todas as formas, mas o passo do dicionário é indispensável para os verbos sem <i>b</i> e para conferir se um <i>b</i> é da raiz.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Reconheça a forma', 'Dê o tempo (presente, imperfeito ou futuro), a pessoa, o número e a entrada de dicionário, e traduza. Os verbos estão no vocabulário do capítulo 6.', [
            ('<i>amābant</i>', 'Imperfeito, 3ª do plural; <i>amō, -āre</i> (1ª): "amavam". Sinal <i>-ba-</i>.'),
            ('<i>amābunt</i>', 'Futuro, 3ª do plural; <i>amō, -āre</i>: "amarão, vão amar". Sinal com <i>b</i> + <i>u</i>, da 1ª conjugação.'),
            ('<i>monent</i>', 'Presente, 3ª do plural; <i>moneō, -ēre</i> (2ª): "advertem". Sem <i>b</i>; o <i>e</i> é a vogal do tema da 2ª.'),
            ('<i>regent</i>', 'Futuro, 3ª do plural; <i>regō, -ere</i> (3ª): "regerão, vão governar". Sem <i>b</i>; como o verbo é da 3ª, o <i>e</i> é sinal de futuro (o presente é <i>regunt</i>).'),
            ('<i>monēbunt</i>', 'Futuro, 3ª do plural; <i>moneō, -ēre</i>: "advertirão". O futuro da 2ª tem <i>-bu-</i>, como o da 1ª.'),
            ('<i>audiēs</i>', 'Futuro, 2ª do singular; <i>audiō, -īre</i> (4ª): "ouvirás, você vai ouvir". O presente seria <i>audīs</i>.'),
            ('<i>capiēbāmus</i>', 'Imperfeito, 1ª do plural; <i>capiō, -ere</i> (3ª em <i>-iō</i>): "pegávamos". <i>-iē-</i> + <i>-bā-</i> + <i>-mus</i>.'),
            ('<i>erit</i>', 'Futuro, 3ª do singular de <i>sum, esse</i>: "será, estará; haverá". Vogal <i>i</i> depois de <i>er-</i>.'),
            ('<i>erātis</i>', 'Imperfeito, 2ª do plural de <i>esse</i>: "éreis, vocês eram". Vogal <i>a</i> depois de <i>er-</i>.'),
            ('<i>dūcam</i>', 'Futuro, 1ª do singular; <i>dūcō, -ere</i> (3ª): "conduzirei". O <i>-am</i> é a 1ª pessoa do futuro da 3ª e da 4ª.'),
            ('<i>scrībit</i>', 'Presente, 3ª do singular; <i>scrībō, -ere</i> (3ª): "escreve". O <i>b</i> é da raiz; depois dela vem o <i>i</i> breve do presente da 3ª.'),
            ('<i>habēbit</i>', 'Futuro, 3ª do singular; <i>habeō, -ēre</i> (2ª): "terá". O primeiro <i>b</i> é da raiz (<i>hab-</i>); o segundo, seguido de <i>i</i>, é o sinal do futuro.'),
            ('<i>veniet</i> e <i>venit</i>', '<i>veniō, -īre</i> (4ª). <i>Veniet</i>: futuro, 3ª do singular, "virá"; <i>venit</i>: presente, "vem". O <i>e</i> depois do <i>i</i> é o sinal do futuro.'),
        ]),
        exercicio('Exercício 2 · Forme o imperfeito e o futuro', 'Dê o imperfeito e o futuro na pessoa indicada, explicando o sistema usado.', [
            ('<i>labōrō, -āre</i> · 3ª do plural', 'Imperfeito <i>labōrābant</i>; futuro <i>labōrābunt</i>. 1ª conjugação: <i>-ba-</i> no imperfeito, <i>-bu-</i> no futuro.'),
            ('<i>timeō, -ēre</i> · 1ª do singular', 'Imperfeito <i>timēbam</i>; futuro <i>timēbō</i>. 2ª conjugação: futuro com <i>b</i>.'),
            ('<i>dūcō, -ere</i> · 2ª do singular', 'Imperfeito <i>dūcēbās</i>; futuro <i>dūcēs</i>. 3ª conjugação: <i>ē</i> + <i>-ba-</i> no imperfeito; futuro em <i>-ēs</i>, sem <i>b</i> (não "dūcēbis").'),
            ('<i>veniō, -īre</i> · 1ª do plural', 'Imperfeito <i>veniēbāmus</i>; futuro <i>veniēmus</i>. 4ª conjugação: o <i>i</i> do tema fica, seguido de <i>ē</i>.'),
            ('<i>faciō, -ere</i> · 3ª do plural', 'Imperfeito <i>faciēbant</i>; futuro <i>facient</i>. 3ª em <i>-iō</i>: as duas formas têm duas vogais seguidas e por isso seguem a 4ª (<i>audiēbant, audient</i>).'),
            ('<i>sum, esse</i> · 2ª do plural', 'Imperfeito <i>erātis</i>; futuro <i>eritis</i>. Radical <i>er-</i>, com <i>a</i> no imperfeito e <i>i</i> no futuro.'),
            ('<i>habeō, -ēre</i> · 3ª do singular', 'Imperfeito <i>habēbat</i>; futuro <i>habēbit</i>. 2ª conjugação; o <i>b</i> de <i>hab-</i> é da raiz.'),
            ('<i>scrībō, -ere</i> · 1ª do singular', 'Imperfeito <i>scrībēbam</i>; futuro <i>scrībam</i>. 3ª conjugação: futuro em <i>-am</i>. Repare que <i>scrībam</i> tem um <i>b</i>, mas é o da raiz.'),
        ]),
        exercicio('Exercício 3 · Mude o tempo', 'Passe cada frase do presente para o imperfeito e para o futuro, e traduza as três versões.', [
            ('<i>Puerī librōs legunt.</i>', 'Imperfeito <i>Puerī librōs legēbant</i>, "os meninos liam livros"; futuro <i>Puerī librōs legent</i>, "os meninos lerão (vão ler) livros". <i>Legō</i> é da 3ª: <i>legunt</i> → <i>legēbant</i> → <i>legent</i>.'),
            ('<i>Agricola in agrō labōrat.</i>', '<i>labōrābat</i>, "trabalhava"; <i>labōrābit</i>, "trabalhará". 1ª conjugação.'),
            ('<i>Nautae sumus.</i>', '<i>Nautae erāmus</i>, "éramos marinheiros"; <i>Nautae erimus</i>, "seremos marinheiros". O predicativo continua no nominativo.'),
            ('<i>Puella rosam capit.</i>', '<i>capiēbat</i>, "pegava (tentava pegar)"; <i>capiet</i>, "pegará". 3ª em <i>-iō</i>: o <i>i</i> volta no imperfeito e no futuro.'),
            ('<i>Magistra puerōs monet.</i>', '<i>monēbat</i>, "advertia"; <i>monēbit</i>, "advertirá". 2ª conjugação: futuro com <i>b</i>, não "monet".'),
            ('<i>Fābulās poētae audīmus.</i>', '<i>audiēbāmus</i>, "ouvíamos"; <i>audiēmus</i>, "ouviremos". 4ª conjugação.'),
            ('<i>In hortō multae rosae sunt.</i>', '<i>erant</i>, "havia muitas rosas no jardim"; <i>erunt</i>, "haverá muitas rosas". O "há" do presente vira "havia" e "haverá", e o verbo latino continua no plural.'),
        ]),
        exercicio('Exercício 4 · Que imperfeito é este?', 'Traduza e diga qual valor do imperfeito o contexto sugere (em curso, habitual, conativo ou incoativo). Vocabulário: <i>ōlim</i>, outrora, antigamente; <i>autem</i>, porém; <i>cotīdiē</i>, todos os dias; <i>teneō, -ēre</i>, segurar; <i>iam</i>, já; <i>lūceō, -ēre</i>, brilhar.', [
            ('<i>Ōlim in īnsulā habitābāmus.</i>', '"Antigamente morávamos na ilha." Estado ou hábito que durou no passado; <i>ōlim</i> reforça.'),
            ('<i>Magister fābulam nārrābat; puerī autem dormiēbant.</i>', '"O mestre contava (estava contando) uma história; os meninos, porém, dormiam." Duas ações em curso ao mesmo tempo: descrição de uma cena.'),
            ('<i>Avus cotīdiē in hortō ambulābat.</i>', '"O avô passeava (costumava passear) todos os dias no jardim." Habitual; <i>cotīdiē</i> mostra a repetição.'),
            ('<i>Puer rosam capiēbat, sed puella rosam tenēbat.</i>', '"O menino tentava pegar a rosa, mas a menina segurava a rosa." Conativo: o <i>sed</i> mostra que a ação não se completou.'),
            ('<i>Iam stellae in caelō lūcēbant.</i>', '"Já as estrelas começavam a brilhar no céu." Incoativo: com <i>iam</i>, o imperfeito marca o começo do estado (Bennett § 260.3). "Já brilhavam" também é aceitável.'),
        ]),
        exercicio('Exercício 5 · Leia o texto', 'Leia em voz alta o texto abaixo, que reencontra as personagens do capítulo 8. Depois traduza frase a frase, dizendo o tempo de cada verbo. Vocabulário: <i>ōlim</i>, outrora; <i>cum</i> + ablativo, com; <i>longinquus, -a, -um</i>, distante; <i>ōra, -ae</i> (f.), litoral; <i>nunc</i>, agora; <i>nōn iam</i>, já não; <i>casa, -ae</i> (f.), cabana; <i>crās</i>, amanhã; <i>iterum</i>, de novo; <i>rēmus, -ī</i> (m.), remo; <i>cibus, -ī</i> (m.), comida; <i>nāvicula, -ae</i> (f.), barquinho.<br><span lang="la"><i>' + _TEXTO_LEITURA + '</i></span>', [
            ('Frase 1', '<i>erat</i>, <i>nāvigābat</i>: imperfeitos (de <i>esse</i> e da 1ª). "Antigamente o avô era marinheiro e navegava com os amigos para ilhas distantes." Imperfeito de hábito no passado.'),
            ('Frase 2', '<i>habitābat</i>, <i>exspectābat</i>: imperfeitos da 1ª. "A avó morava no litoral e esperava os marinheiros."'),
            ('Frase 3', '<i>nāvigat</i>, <i>manet</i>, <i>nārrat</i>: presentes (1ª, 2ª, 1ª). "Agora o avô já não navega: fica em casa e conta histórias." <i>Manet</i> é presente porque <i>maneō</i> é da 2ª.'),
            ('Frase 4', '<i>nāvigābunt</i>: futuro da 1ª, 3ª do plural (dois sujeitos ligados por <i>et</i>). "Amanhã, porém, Tito e Flávia vão navegar de novo com o avô para a ilha."'),
            ('Frase 5', '<i>portābit</i>, <i>parābit</i>: futuros da 1ª (<i>-bi-</i>); <i>dūcet</i>: futuro da 3ª (<i>dūcō, -ere</i>; o presente seria <i>dūcit</i>). "Tito vai carregar os remos, Flávia vai preparar a comida, o avô vai conduzir o barquinho."'),
            ('Frase 6', '<i>erit</i>: futuro de <i>esse</i>; <i>exspectābit</i>: futuro da 1ª. "A avó estará no litoral e esperará as crianças." Como no capítulo 8, <i>puerōs</i> pode designar um grupo misto, "as crianças".'),
        ]),
        exercicio('Exercício 6 · Retroversão', 'Passe para o latim, sem pronomes sujeito. Vocabulário extra: <i>nunc</i>, agora; <i>crās</i>, amanhã; <i>cēna, -ae</i> (f.), jantar; <i>in</i> + acusativo, para dentro de.', [
            ('Os meninos liam livros.', '<i>Puerī librōs legēbant.</i> Imperfeito da 3ª: <i>leg-ēba-nt</i>.'),
            ('Você vai ouvir a professora.', '<i>Magistram audiēs.</i> Futuro da 4ª, 2ª do singular: <i>audi-ē-s</i> (não "audībis").'),
            ('Éramos marinheiros; agora somos agricultores.', '<i>Nautae erāmus; nunc agricolae sumus.</i> Imperfeito e presente de <i>esse</i>, com predicativos no nominativo plural.'),
            ('O agricultor vai conduzir os cavalos para o campo.', '<i>Agricola equōs in agrum dūcet.</i> Futuro da 3ª: <i>dūc-e-t</i>; "vai conduzir" é uma palavra só em latim.'),
            ('As meninas costumavam cantar no jardim.', '<i>Puellae in hortō cantābant.</i> O imperfeito sozinho exprime o hábito; não há verbo para "costumar".'),
            ('Amanhã vocês verão a ilha.', '<i>Crās īnsulam vidēbitis.</i> Futuro da 2ª: <i>vidē-bi-tis</i>.'),
            ('Eles vão fazer o jantar.', '<i>Cēnam facient.</i> <i>Faciō</i> é da 3ª em <i>-iō</i>: futuro <i>faci-ent</i>, como <i>audient</i>.'),
        ]),
    ],
    leituras=['ravizza-gramatica-latina', 'bennett-new-latin-grammar', 'greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', 'd-ooge-latin-for-beginners', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'vulgata-biblia-sacra-vulgata-editio-clementina'],
    leituras_nota='Para consulta, Ravizza dá em português as terminações do imperfeito e do futuro por conjugação (n. 85) e esse completo (n. 82); em Bennett, os paradigmas estão nos §§ 100–110 e os valores dos tempos nos §§ 257–261; em Allen & Greenough, a formação está no § 168 e os usos nos §§ 470–472. Para exercitar, as lições XVIII, XX, XXI, XXIV, XXV e XXVI de Latin for Beginners, de D\'Ooge, tratam justamente de sum, do imperfeito e do futuro nas quatro conjugações e dos verbos em -iō, com frases curtas. Para leitura, procure os imperfeitos e futuros nos capítulos de Familia Romana em que aparecem, aplicando o procedimento da seção 5; e na Vulgata, leia o começo de João (1,1–4), em que erat aparece seis vezes.',
)
