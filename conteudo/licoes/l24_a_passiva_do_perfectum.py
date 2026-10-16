from conteudo.util import (tabela, tabela_conjugacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='24-a-passiva-do-perfectum', titulo='A passiva do perfectum e a passiva impessoal', titulo_latim='Dē passīvō perfectī', tempo='65 min',
    resumo='O particípio perfeito passivo como quarta parte principal do verbo; o perfeito, o mais-que-perfeito e o futuro perfeito passivos (amātus sum, eram, erō), com o particípio concordando com o sujeito; o infinitivo perfeito passivo (amātus esse); a passiva impessoal dos verbos intransitivos (pugnātur, ventum est, ītur); e o quadro completo dos seis tempos do indicativo, ativos e passivos.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['particípio perfeito passivo', 'quarta parte principal', 'supino e particípio no dicionário', 'perfeito passivo', 'mais-que-perfeito passivo', 'futuro perfeito passivo',
             'concordância do particípio com o sujeito', 'sujeito composto e particípio', 'amātus sum × amor', 'est + particípio: ação e estado', 'infinitivo perfeito passivo',
             'passiva impessoal', 'verbos intransitivos na passiva', 'ventum est, pugnātum est, ītur', 'quadro dos seis tempos do indicativo', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 23: as terminações passivas, a passiva do infectum, o agente com ā/ab e a passagem da ativa para a passiva. Do capítulo 13, as partes principais e os três tempos do perfectum ativo; do capítulo 5, a declinação de bonus, -a, -um.',
                       licoes=['23-a-voz-passiva-infectum', '13-o-perfeito-e-as-partes-principais']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 97 (o tema do particípio forma os tempos passivos do perfectum e o infinitivo perfeito passivo), § 99 (partes principais; o particípio perfeito como quarta parte; nota 28), § 102 (amātus sum, eram, erō; amātus esse; nota 36, fuī, fueram, fuerō às vezes por sum, eram, erō), §§ 104, 106, 108, 111 (monitus, rēctus, audītus, captus sum), § 119 (formação do particípio: -tus, -sus, -itus; lēctus, scrīptus, monitus), § 138.IV (passiva dos intransitivos: ītur, curritur, ventum est), § 216 (agente), § 254.2 (o particípio das formas compostas concorda com o sujeito em gênero), § 255.5 e § 235.B.2 (sujeitos de gêneros diferentes), § 256.3 (passiva impessoal dos intransitivos)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 172 (a quarta parte principal é o neutro do particípio perfeito, amātum, ou o particípio futuro), § 173 (partes principais da passiva: amor, amārī, amātus), § 179.g (os tempos passivos de ação acabada: particípio + tempos do infectum de esse), § 495 e nota (o particípio como adjetivo predicativo: Gallia est dīvīsa; origem dos tempos compostos da passiva), §§ 207–208 (verbos impessoais; § 208.d, passiva impessoal dos intransitivos: ventum est, pugnātur, ītur, parcitur mihi), § 316, nota (nas formas com particípio, este concorda com o sujeito em gênero e número), § 405.b (per + acusativo)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 112 (formas básicas da passiva: amor, amārī, amātus), §§ 120–123 (tempos passivos do perfectum nas quatro conjugações: amātus sum, eram, erō), §§ 296 e 299–302 (passagem para a passiva; intransitivos usados impessoalmente na passiva, com ou sem agente; sīc ītur ad astra; pugnātum est)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 87.2 (o particípio perfeito passivo forma-se do supino, trocando -um por -us, -a, -um), n. 90 (regra B: perfeito, mais-que-perfeito e futuro perfeito passivos com o particípio e sum/fuī, eram/fueram, erō/fuerō; infinitivo perfeito passivo), n. 92.2 (infinitivo perfeito passivo), n. 140.IV (passiva impessoal dos intransitivos: curritur, pugnātur, ītur, ventum est)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Mateus 4,1 e 10,30; Lucas 1,26; João 1,3', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', nota='frases autênticas das seções 3 e 4, conferidas na Wikisource latina (Vulgata Clementina); grafia normalizada (ae por æ, i por j) e macrons acrescentados por este livro', tipo='dominio_publico'),
        referencia('Commentarii de bello Gallico I, 1 e I, 26', 'Caio Júlio César', catalogo='caesar-commentarii-de-bello-gallico-texto-integral', nota='frases das seções 3 e 5, conferidas no texto da Latin Library', tipo='dominio_publico'),
        referencia('Eneida IX, 641', 'Públio Virgílio Marão', catalogo='maro-aeneis-texto-integral', nota='sīc ītur ad astra (seção 5), conferido no texto da Latin Library', tipo='dominio_publico'),
    ],
    objetivos=[
        'Reconhecer o particípio perfeito passivo como quarta parte principal do verbo e encontrá-lo no dicionário (<i>amātum</i> → <i>amātus, -a, -um</i>).',
        'Formar e traduzir o perfeito, o mais-que-perfeito e o futuro perfeito passivos, fazendo o particípio concordar com o sujeito em gênero, número e caso.',
        'Distinguir <i>amātus sum</i> ("fui amado") de <i>amor</i> ("sou amado") e <i>amātus erat</i> ("tinha sido amado") de <i>amābātur</i> ("era amado").',
        'Formar o infinitivo perfeito passivo (<i>amātus esse</i>) e reconhecê-lo ao lado dos outros infinitivos já estudados.',
        'Ler e traduzir a passiva impessoal dos verbos intransitivos (<i>pugnātur, pugnātum est, ventum est, ītur</i>).',
    ],
    secoes=[
        ('A quarta parte principal: o particípio perfeito passivo', f'''
<p>No capítulo 23, a passiva do infectum se fez numa palavra só: <i>amātur</i>, "é amado". Nos três tempos do <b>perfectum</b>, o latim procede como o português: junta uma forma nominal do verbo, o <b>particípio perfeito passivo</b>, e o verbo "ser". "Foi amado" é <i>amātus est</i>; "tinha sido amado", <i>amātus erat</i>. Antes de montar os tempos, portanto, é preciso conhecer a peça nova.</p>
<p>O particípio perfeito passivo é a forma que corresponde ao nosso particípio "amado", "governado", "ouvido". É ele que fornece a <b>quarta parte principal</b> do verbo, aquela que no capítulo 13 ficou anunciada (Bennett § 99): <i>amō, amāre, amāvī, <b>amātum</b></i>. Os dicionários e as gramáticas registram essa parte de duas maneiras. Uns dão o neutro em <i>-um</i> (<i>amātum</i>), que também é a forma do supino (capítulo 31); outros dão o masculino em <i>-us</i> (<i>amātus</i>), e a passiva se registra então como <i>amor, amārī, amātus sum</i> (A&amp;G §§ 172–173; Kennedy § 112). As duas notações dizem a mesma coisa: o tema do particípio é <i>amāt-</i>. Ravizza ensina a passagem: do supino "mudando-se <i>um</i> em <i>us, a, um</i>" (n. 87.2).</p>
<p>O particípio se declina como <b><i>bonus, -a, -um</i></b> (capítulo 5): <i>amātus, amāta, amātum</i>. Neste capítulo ele aparece só como parte das formas verbais; os seus usos como adjetivo verbal independente ("o soldado ferido", "a cidade tomada") são o assunto do capítulo 29.</p>
<h3>Como se forma, e por que é preciso decorá-lo</h3>
<p>O particípio se forma com <i>-tus</i> (às vezes <i>-sus</i>) acrescentado ao tema (Bennett § 119). Na 1ª e na 4ª conjugações ele é quase sempre regular: <i>amā-tus</i>, <i>audī-tus</i>. Na 2ª, o tipo mais comum é <i>-itus</i>: <i>moneō → monitus</i>. Na 3ª, o <i>-tus</i> se junta diretamente à raiz e provoca mudanças de som (<i>g</i> vira <i>c</i>, <i>b</i> vira <i>p</i>, <i>d</i> + <i>t</i> dá <i>s</i>), de modo que a forma precisa ser aprendida com o verbo: <i>regō → rēctus</i>, <i>scrībō → scrīptus</i>, <i>mittō → missus</i>. É exatamente por isso que o dicionário dá a quarta parte.</p>
{tabela(['Verbo', 'Partes principais', 'Particípio', 'Significado'], [
    ['amō (1ª)', 'amō, amāre, amāvī, amātum', 'amāt<b>us</b>, -a, -um', 'amado'],
    ['moneō (2ª)', 'moneō, monēre, monuī, monitum', 'monit<b>us</b>', 'advertido'],
    ['videō (2ª)', 'videō, vidēre, vīdī, vīsum', 'vīs<b>us</b>', 'visto'],
    ['regō (3ª)', 'regō, regere, rēxī, rēctum', 'rēct<b>us</b>', 'governado'],
    ['dūcō (3ª)', 'dūcō, dūcere, dūxī, ductum', 'duct<b>us</b>', 'conduzido'],
    ['mittō (3ª)', 'mittō, mittere, mīsī, missum', 'miss<b>us</b>', 'enviado'],
    ['scrībō (3ª)', 'scrībō, scrībere, scrīpsī, scrīptum', 'scrīpt<b>us</b>', 'escrito'],
    ['legō (3ª)', 'legō, legere, lēgī, lēctum', 'lēct<b>us</b>', 'lido; escolhido'],
    ['capiō (3ª em -iō)', 'capiō, capere, cēpī, captum', 'capt<b>us</b>', 'pego, tomado'],
    ['faciō (3ª em -iō)', 'faciō, facere, fēcī, factum', 'fact<b>us</b>', 'feito'],
    ['audiō (4ª)', 'audiō, audīre, audīvī, audītum', 'audīt<b>us</b>', 'ouvido'],
], 'Partes principais e particípio perfeito passivo de verbos frequentes', latim_cols=(1, 2))}
{dica('<b>Os particípios explicam o português.</b> Muitas palavras portuguesas vêm do particípio latino, e não do presente: <i>scrīptus</i> → "escrito"; <i>factus</i> → "feito", "fato"; <i>missus</i> → "missão"; <i>ductus</i> → "duto", "conduto"; <i>vīsus</i> → "visto", "visão"; <i>ēlēctus</i> (de <i>ēligō</i>) → "eleito". Quando um particípio parecer estranho, procure um cognato português: muitas vezes ele existe e ajuda a lembrar a forma.')}
'''),
        ('Os três tempos passivos do perfectum', f'''
<p>Com o particípio na mão, os três tempos passivos do perfectum se montam juntando-lhe os tempos do <b>infectum</b> de <i>esse</i> (A&amp;G § 179.g; Ravizza n. 90):</p>
<ul>
<li><b>perfeito</b> passivo = particípio + <b>presente</b> de <i>esse</i>: <i>amātus sum</i>, "fui amado";</li>
<li><b>mais-que-perfeito</b> passivo = particípio + <b>imperfeito</b> de <i>esse</i>: <i>amātus eram</i>, "tinha sido amado";</li>
<li><b>futuro perfeito</b> passivo = particípio + <b>futuro</b> de <i>esse</i>: <i>amātus erō</i>, "terei sido amado".</li>
</ul>
{tabela(['Pessoa', 'Perfeito', 'Mais-que-perfeito', 'Futuro perfeito'], [
    ['1ª sing.', 'amātus, -a <b>sum</b>', 'amātus, -a <b>eram</b>', 'amātus, -a <b>erō</b>'],
    ['2ª sing.', 'amātus, -a <b>es</b>', 'amātus, -a <b>erās</b>', 'amātus, -a <b>eris</b>'],
    ['3ª sing.', 'amātus, -a, -um <b>est</b>', 'amātus, -a, -um <b>erat</b>', 'amātus, -a, -um <b>erit</b>'],
    ['1ª pl.', 'amātī, -ae <b>sumus</b>', 'amātī, -ae <b>erāmus</b>', 'amātī, -ae <b>erimus</b>'],
    ['2ª pl.', 'amātī, -ae <b>estis</b>', 'amātī, -ae <b>erātis</b>', 'amātī, -ae <b>eritis</b>'],
    ['3ª pl.', 'amātī, -ae, -a <b>sunt</b>', 'amātī, -ae, -a <b>erant</b>', 'amātī, -ae, -a <b>erunt</b>'],
    ['tradução', 'fui amado, tenho sido amado', 'tinha (havia) sido amado', 'terei sido amado'],
], 'Os tempos passivos do perfectum: amō', latim_cols=(1, 2, 3))}
<p>Todas as conjugações funcionam igual; muda só o particípio: <i>monitus sum</i>, <i>rēctus sum</i>, <i>audītus sum</i>, <i>captus sum</i> (Bennett §§ 104, 106, 108, 111; Kennedy §§ 120–123). Não há nada novo a decorar além do particípio de cada verbo.</p>
<h3>O tempo do auxiliar engana</h3>
<p>A dificuldade não está na forma, mas na tradução. O auxiliar está um tempo "atrás" do sentido: <i>sum</i> é presente, mas <i>amātus sum</i> é <b>perfeito</b>; <i>eram</i> é imperfeito, mas <i>amātus eram</i> é <b>mais-que-perfeito</b>. Quem traduz palavra por palavra ("amado sou", "amado era") cai na armadilha mais comum deste capítulo.</p>
{comparacao('Formas que o português confunde', ['Latim', 'Tempo', 'Tradução correta', 'Tradução errada'], [
    ['<b>amor</b>', 'presente passivo (cap. 23)', 'sou amado', '—'],
    ['<b>amātus sum</b>', 'perfeito passivo', 'fui amado', '*sou amado'],
    ['<b>amābar</b>', 'imperfeito passivo (cap. 23)', 'era amado, estava sendo amado', '—'],
    ['<b>amātus eram</b>', 'mais-que-perfeito passivo', 'tinha sido amado', '*era amado'],
    ['<b>amābor</b>', 'futuro passivo (cap. 23)', 'serei amado', '—'],
    ['<b>amātus erō</b>', 'futuro perfeito passivo', 'terei sido amado', '*serei amado'],
])}
<p>Duas notas de leitura. Primeira: em vez de <i>sum, eram, erō</i>, você encontrará às vezes <i>fuī, fueram, fuerō</i>: <i>amātus fuit</i> por <i>amātus est</i> (Bennett § 102, nota 36; Ravizza n. 90). O sentido é praticamente o mesmo; não procure diferença onde o texto não a marca. Segunda: o auxiliar pode vir antes do particípio, longe dele ou ser omitido, como acontece com <i>esse</i> em geral (capítulo 22): <i>urbs capta</i> (subentendido <i>est</i>), "a cidade (foi) tomada" (Bennett § 166.3 dá exemplos dessa omissão). Ao ler, junte mentalmente o particípio e a forma de <i>esse</i> que lhe corresponde.</p>
'''),
        ('A concordância do particípio', f'''
<p>O particípio é um adjetivo e, como predicativo, concorda com o sujeito em <b>gênero, número e caso</b> (Bennett § 254.2; A&amp;G § 316, nota). O caso é sempre o nominativo, porque o sujeito está no nominativo; o gênero e o número variam com o sujeito. O verbo <i>esse</i>, por sua vez, concorda em pessoa e número, como qualquer verbo.</p>
{exemplos([('Mārcus ā magistrō laudāt<b>us</b> est.', 'Marco foi elogiado pelo mestre. (masculino singular)'), ('Iūlia ā magistrō laudāt<b>a</b> est.', 'Júlia foi elogiada pelo mestre. (feminino singular)'), ('Dōn<b>um</b> rēgī dat<b>um</b> est.', 'O presente foi dado ao rei. (neutro singular)'), ('Puellae ā mātre vocāt<b>ae</b> erant.', 'As meninas tinham sido chamadas pela mãe. (feminino plural)'), ('Mīlitēs in castra duct<b>ī</b> erunt.', 'Os soldados terão sido conduzidos ao acampamento. (masculino plural)'), ('Bell<b>a</b> gest<b>a</b> sunt.', 'As guerras foram travadas. (neutro plural; <i>gerō, -ere, gessī, gestum</i>)')])}
<p>Quando o sujeito é um pronome implícito, o particípio revela o gênero de quem fala ou de quem se fala: <i>laudāta sum</i> só pode ser dito por uma mulher, "fui elogiada"; <i>vocātī estis</i>, "fostes chamados", dirige-se a homens ou a um grupo misto. Com <b>sujeitos de gêneros diferentes</b>, valem as regras do adjetivo predicativo (Bennett § 255.5, que remete ao § 235.B.2): se forem pessoas, masculino plural (<i>pater et māter laudātī sunt</i>); se forem coisas, de preferência neutro plural.</p>
<h3>Quatro frases autênticas</h3>
<p>A Vulgata está cheia de perfeitos passivos. Em Mateus 10,30 lemos <i>Vestrī autem capillī capitis omnēs numerātī sunt</i>, "os vossos cabelos da cabeça estão todos contados": <i>numerātī</i> é masculino plural, como <i>capillī</i> (<i>capillus, -ī</i>, cabelo). Em João 1,3, <i>Omnia per ipsum facta sunt</i>, "todas as coisas foram feitas por meio dele": <i>facta</i> é neutro plural, como <i>omnia</i>; e o "por meio dele" vem com <i>per</i> + acusativo, a construção do intermediário que você viu no capítulo 23 (A&amp;G § 405.b). Em Mateus 4,1, <i>Tunc Iēsūs ductus est in dēsertum ā Spīritū</i>, "então Jesus foi conduzido ao deserto pelo Espírito", com o agente pessoal <i>ā Spīritū</i>.</p>
<p>A quarta frase é a mais conhecida da prosa latina: <i>Gallia est omnis dīvīsa in partēs trēs</i>, "a Gália, em seu conjunto, está dividida em três partes" (César, <i>BG</i> 1.1.1). Formalmente, <i>est dīvīsa</i> tem a forma de um perfeito passivo, com <i>dīvīsa</i> feminino singular concordando com <i>Gallia</i>. Mas César não conta quando nem por quem a Gália foi dividida: descreve uma situação. Por isso se traduz "está dividida", e não "foi dividida". Allen e Greenough (§ 495) citam justamente esta frase como exemplo do particípio usado como <b>adjetivo predicativo</b>, ligado ao sujeito por <i>esse</i> ("Gaul is divided"), e explicam na nota que dessa construção predicativa nasceram os tempos compostos da passiva. O perfeito passivo latino pode exprimir tanto a <b>ação</b> concluída ("foi dividida") quanto o <b>estado</b> que resulta dela ("está dividida"), e o português obriga você a escolher entre "foi" e "está". Decida pelo contexto: se há agente ou uma indicação de momento, prefira "foi"; se a frase descreve uma situação, "está".</p>
{diagrama_frase([('Puellae', 'nominativo pl. fem. · sujeito'), ('ā mātre', 'ā + ablativo · agente'), ('vocātae', 'particípio nom. pl. fem. · concorda com puellae'), ('erant', 'imperfeito de esse · 3ª pl.')], '<i>Puellae ā mātre vocātae erant</i> = As meninas tinham sido chamadas pela mãe. O particípio concorda com o sujeito em gênero, número e caso; o auxiliar concorda em pessoa e número; juntos, particípio e imperfeito de <i>esse</i> formam o mais-que-perfeito passivo.')}
'''),
        ('Análise: o anjo enviado e o infinitivo perfeito passivo', f'''
<p>O Evangelho de Lucas abre a cena da Anunciação com um perfeito passivo que tem tudo o que este capítulo e o anterior ensinaram: auxiliar, particípio, sujeito com aposto e agente pessoal.</p>
{exemplos([('In mēnse autem sextō, missus est angelus Gabriel ā Deō in cīvitātem Galilaeae, cui nōmen Nazareth.', 'No sexto mês, foi enviado o anjo Gabriel, da parte de Deus, a uma cidade da Galileia chamada Nazaré. (Lc 1,26, Vulgata)')])}
{analise('Lc 1,26, palavra a palavra (até Galilaeae)', [
    ('In mēnse', 'in + mēnsis, -is (m.), mês', 'ablativo singular', '<i>in</i> + ablativo: tempo em que (capítulo 19)'),
    ('autem', 'autem (conjunção)', 'invariável; vem em segundo lugar', '"porém, e"; liga a cena ao que precede'),
    ('sextō', 'sextus, -a, -um, sexto', 'ablativo singular masculino', 'atributo de <i>mēnse</i>'),
    ('missus', 'mittō, mittere, mīsī, missum, enviar', 'particípio perfeito passivo, nominativo singular masculino', 'forma, com <i>est</i>, o perfeito passivo; concorda com <i>angelus</i>'),
    ('est', 'sum, esse', 'presente, 3ª sing.', 'auxiliar: <i>missus est</i>, "foi enviado"'),
    ('angelus', 'angelus, -ī (m.), anjo', 'nominativo singular', 'sujeito'),
    ('Gabriel', 'Gabriel (nome hebraico, indeclinável)', 'aqui, nominativo', 'aposto de <i>angelus</i>'),
    ('ā Deō', 'ā + deus, -ī (m.)', 'ablativo singular', 'agente pessoal da passiva'),
    ('in cīvitātem', 'in + cīvitās, -ātis (f.), cidade', 'acusativo singular', '<i>in</i> + acusativo: lugar para onde'),
    ('Galilaeae', 'Galilaea, -ae (f.), Galileia', 'genitivo singular', 'complemento de <i>cīvitātem</i>: "da Galileia"'),
])}
<p>Três observações. A frase começa pelo verbo (<i>missus est</i>), e não pelo sujeito: na narrativa da Vulgata é comum o verbo abrir a frase, e aqui ele põe em primeiro plano o acontecimento, o envio (capítulo 22, ordem e ênfase). O particípio <i>missus</i> está longe do sujeito, mas a concordância (nominativo masculino singular) mostra a que palavra pertence. E o agente <i>ā Deō</i> é uma pessoa, com <i>ā</i>, como você aprendeu no capítulo 23; a tradução "da parte de Deus" é tão correta quanto "por Deus". O final, <i>cui nōmen Nazareth</i>, é uma relativa com o verbo <i>esse</i> subentendido e um dativo de posse: "a qual (tinha) o nome de Nazaré", isto é, "chamada Nazaré" (capítulos 16 e 20).</p>
<h3>O infinitivo perfeito passivo</h3>
<p>O infinitivo perfeito passivo se forma do mesmo modo: <b>particípio + <i>esse</i></b>: <i>amātus esse</i>, "ter sido amado"; <i>rēctus esse</i>, "ter sido governado"; <i>captus esse</i>, "ter sido tomado" (Bennett § 102; Ravizza n. 92.2). O particípio concorda com a palavra a que o infinitivo se refere: <i>urbs capta esse vidētur</i>, "a cidade parece ter sido tomada". No capítulo 28 você verá que esse infinitivo aparece quase sempre com o particípio no <b>acusativo</b> (<i>amātum, -am, -um esse</i>), na oração infinitiva; é por isso que Ravizza o dá nessa forma (n. 90.b). Por ora, basta reconhecê-lo no quadro dos infinitivos que você já conhece:</p>
{tabela(['', 'Ativo', 'Passivo'], [
    ['<b>presente</b>', 'amā<b>re</b> · reg<b>ere</b> (amar · governar)', 'amā<b>rī</b> · reg<b>ī</b> (ser amado · ser governado)'],
    ['<b>perfeito</b>', 'amāv<b>isse</b> · rēx<b>isse</b> (ter amado · ter governado)', 'amātus <b>esse</b> · rēctus <b>esse</b> (ter sido amado · ter sido governado)'],
], 'Os infinitivos presente e perfeito, ativos e passivos (o futuro fica para o capítulo 27)', latim_cols=(1, 2))}
'''),
        ('A passiva impessoal', f'''
<p>No capítulo 23 você aprendeu que só os verbos transitivos têm passiva <b>pessoal</b>, porque só eles têm um objeto que possa virar sujeito. Os verbos <b>intransitivos</b>, porém, também podem ir para a passiva, de um modo particular: na <b>3ª pessoa do singular, sem sujeito</b> (Bennett § 256.3; A&amp;G § 208.d; Kennedy § 299; Ravizza n. 140.IV). A frase diz que a ação acontece, sem dizer quem a pratica.</p>
{tabela(['Latim', 'Literalmente', 'Tradução natural'], [
    ['pugnā<b>tur</b>', '"é lutado"', 'luta-se; há combate; estão lutando'],
    ['curri<b>tur</b>', '"é corrido"', 'corre-se; as pessoas correm'],
    ['vīvi<b>tur</b>', '"é vivido"', 'vive-se'],
    ['ī<b>tur</b> (de <i>eō</i>, ir, capítulo 26)', '"é ido"', 'vai-se; vão'],
    ['pugnā<b>tum est</b>', '"foi lutado"', 'lutou-se; houve combate; lutaram'],
    ['ven<b>tum est</b>', '"foi vindo"', 'chegou-se; chegaram'],
], 'A passiva impessoal dos intransitivos', latim_cols=(0,))}
<p>Nos tempos do perfectum, o particípio da passiva impessoal fica no <b>neutro singular</b>: <i>pugnātum est</i>, <i>ventum est</i>, <i>perventum erat</i>. É o gênero e o número de "algo indeterminado", como o "isso" que o português subentende em "chove". Ravizza observa que, por não terem passiva pessoal, esses verbos só usam o particípio nessa forma neutra: <i>ventum est</i>, "mas não <i>ventus, a, um</i>" (n. 140.IV).</p>
<p>Como traduzir? A tradução literal ("foi lutado") não existe em português. As melhores soluções são a passiva com "se" ("luta-se", "lutou-se"), o verbo "haver" com um substantivo ("houve combate") ou a 3ª pessoa do plural indeterminada ("lutaram", "chegaram"). O contexto mostra quem agiu, e você pode explicitá-lo: num relato de César, <i>ad castra ventum est</i> será "(os soldados) chegaram ao acampamento". Se o autor quiser dizer quem agiu, pode usar o agente: <i>ā nōbīs curritur</i>, "corremos nós" (Kennedy § 300). E um intransitivo que pede dativo conserva o dativo na construção impessoal: <i>parcitur mihi</i>, "sou poupado", literalmente "poupa-se a mim" (A&amp;G § 208.d; Kennedy § 302).</p>
<h3>Duas frases célebres</h3>
<p>A passiva impessoal é muito frequente nos historiadores, que a usam para descrever ações coletivas. César, no relato da batalha contra os helvécios, resume assim um combate em duas frentes:</p>
{exemplos([('Ita ancipitī proeliō diū atque ācriter pugnātum est.', 'Assim, num combate em duas frentes, lutou-se longa e duramente. (César, <i>BG</i> 1.26.1)')])}
{analise('César, BG 1.26.1, palavra a palavra', [
    ('Ita', 'ita (advérbio)', 'invariável', '"assim, desse modo"; retoma o que foi narrado'),
    ('ancipitī', 'anceps, ancipitis, de duas frentes, duplo', 'ablativo singular (3ª declinação, adjetivo de uma terminação)', 'atributo de <i>proeliō</i>'),
    ('proeliō', 'proelium, -ī (n.), combate', 'ablativo singular', 'adjunto: em que circunstância ou modo se lutou'),
    ('diū', 'diū (advérbio)', 'invariável', 'adjunto de tempo: "por muito tempo"'),
    ('atque', 'atque (conjunção)', 'invariável', 'liga os dois advérbios'),
    ('ācriter', 'ācriter (advérbio de ācer, capítulo 18)', 'invariável', 'adjunto de modo: "duramente, com ardor"'),
    ('pugnātum', 'pugnō, -āre, -āvī, -ātum, lutar (intransitivo)', 'particípio perfeito passivo, nominativo singular neutro', 'com <i>est</i>, perfeito passivo impessoal'),
    ('est', 'sum, esse', 'presente, 3ª sing.', 'auxiliar; não há sujeito'),
])}
<p>Não há sujeito, nem pode haver: <i>pugnō</i> é intransitivo. Quem lutou? Os dois exércitos, romanos e helvécios; César não precisa dizê-lo, e a construção impessoal põe em primeiro plano a própria luta, longa e dura. Uma tradução fluente poderia ser "assim, combateu-se por muito tempo e com ardor em duas frentes", ou "houve um combate longo e duro em duas frentes".</p>
<p>A segunda frase é de Virgílio. Apolo felicita o jovem Ascânio pela primeira vitória: <i>macte novā virtūte, puer, sīc ītur ad astra</i>, "parabéns pelo teu novo valor, menino: assim se vai aos astros" (<i>En.</i> 9.641). <i>Ītur</i> é a passiva impessoal de <i>eō</i>, "ir" (verbo irregular do capítulo 26), e <i>sīc ītur ad astra</i> virou proverbial: "é assim que se chega às estrelas". Na mesma frase há um vocativo, <i>puer</i>, e o raro vocativo <i>macte</i> (A&amp;G § 340.c).</p>
'''),
        ('Quadro geral: os seis tempos do indicativo, ativa e passiva', f'''
<p>Com este capítulo você completou o indicativo: seis tempos, duas vozes. O quadro abaixo reúne as primeiras pessoas do singular de dois verbos-modelo, <i>amō</i> (1ª) e <i>regō</i> (3ª). Para os outros verbos, basta trocar o tema do presente (infectum), o tema do perfeito (perfectum ativo) ou o particípio (perfectum passivo).</p>
{tabela(['Tempo', 'Ativa · amō', 'Passiva · amō', 'Ativa · regō', 'Passiva · regō', 'Tradução da passiva'], [
    ['<b>presente</b>', 'am<b>ō</b>', 'am<b>or</b>', 'reg<b>ō</b>', 'reg<b>or</b>', 'sou amado, sou governado'],
    ['<b>imperfeito</b>', 'amā<b>bam</b>', 'amā<b>bar</b>', 'regē<b>bam</b>', 'regē<b>bar</b>', 'era amado, era governado'],
    ['<b>futuro</b>', 'amā<b>bō</b>', 'amā<b>bor</b>', 'reg<b>am</b>', 'reg<b>ar</b>', 'serei amado, serei governado'],
    ['<b>perfeito</b>', 'amāv<b>ī</b>', 'amātus <b>sum</b>', 'rēx<b>ī</b>', 'rēctus <b>sum</b>', 'fui amado, fui governado'],
    ['<b>mais-que-perfeito</b>', 'amāv<b>eram</b>', 'amātus <b>eram</b>', 'rēx<b>eram</b>', 'rēctus <b>eram</b>', 'tinha sido amado, governado'],
    ['<b>futuro perfeito</b>', 'amāv<b>erō</b>', 'amātus <b>erō</b>', 'rēx<b>erō</b>', 'rēctus <b>erō</b>', 'terei sido amado, governado'],
], 'Os seis tempos do indicativo, ativa e passiva (1ª pessoa do singular)', latim_cols=(1, 2, 3, 4))}
<p>Observe a arquitetura. Na voz <b>ativa</b>, os três tempos do infectum usam o tema do presente (<i>ama-</i>, <i>reg-</i>) e os três do perfectum, o tema do perfeito (<i>amāv-</i>, <i>rēx-</i>), sempre numa só palavra. Na voz <b>passiva</b>, o infectum continua numa só palavra, com as terminações em <i>-r</i>, e o perfectum passa a duas palavras, particípio + <i>esse</i>. Por isso, para conjugar um verbo inteiro nas duas vozes, você precisa exatamente das <b>quatro partes principais</b>: <i>regō</i> e <i>regere</i> dão o infectum, <i>rēxī</i> dá o perfectum ativo, <i>rēctum</i> dá o perfectum passivo (Bennett § 97).</p>
{comparacao('Pares que se distinguem por uma letra ou pela posição', ['Forma', 'Análise', 'Tradução'], [
    ['amāverint · amātī erunt', 'futuro perfeito ativo, 3ª pl. · futuro perfeito passivo, 3ª pl.', 'terão amado · terão sido amados'],
    ['amāvērunt · amātī sunt', 'perfeito ativo, 3ª pl. · perfeito passivo, 3ª pl.', 'amaram · foram amados'],
    ['amāverat · amātus erat · amābātur', 'mais-que-perfeito ativo · mais-que-perfeito passivo · imperfeito passivo', 'tinha amado · tinha sido amado · era amado'],
    ['rēxit · rēctus est · regitur', 'perfeito ativo · perfeito passivo · presente passivo', 'governou · foi governado · é governado'],
])}
<h3>Resumo e próximos passos</h3>
<ul>
<li><b>Particípio perfeito passivo</b> = quarta parte principal (<i>amātum</i> → <i>amātus, -a, -um</i>), declinado como <i>bonus</i>.</li>
<li><b>Perfectum passivo</b>: particípio + <i>sum</i> (perfeito), <i>eram</i> (mais-que-perfeito), <i>erō</i> (futuro perfeito); às vezes <i>fuī, fueram, fuerō</i>.</li>
<li><b>Concordância</b>: o particípio concorda com o sujeito em gênero, número e caso; o auxiliar, em pessoa e número.</li>
<li><b>Tradução</b>: <i>amātus sum</i> = "fui amado" (ou "estou amado", se for estado), nunca "sou amado".</li>
<li><b>Infinitivo perfeito passivo</b>: <i>amātus esse</i>, "ter sido amado".</li>
<li><b>Passiva impessoal</b>: intransitivos na 3ª sing. sem sujeito (<i>pugnātur</i>, <i>ītur</i>); no perfectum, particípio neutro (<i>pugnātum est, ventum est</i>).</li>
</ul>
<p>O capítulo 25 apresenta os <b>verbos depoentes</b>, que têm as formas passivas que você acabou de aprender, mas sentido ativo: <i>hortātus sum</i> não é "fui exortado", e sim "exortei". Tudo o que você decorou nestes dois capítulos será usado de novo, com outra tradução.</p>
'''),
    ],
    erros_comuns=[
        ('Traduzir <i>amātus sum</i> por "sou amado".', 'O auxiliar no presente engana: <i>amātus sum</i> é perfeito, "fui amado". "Sou amado" é <i>amor</i> (capítulo 23). Leia o particípio e o auxiliar como um bloco e conte um tempo "para trás": <i>sum</i> → perfeito, <i>eram</i> → mais-que-perfeito, <i>erō</i> → futuro perfeito.'),
        ('Traduzir <i>amātus erat</i> por "era amado", confundindo-o com <i>amābātur</i>.', '<i>Amābātur</i> é imperfeito ("era amado, estava sendo amado"); <i>amātus erat</i> é mais-que-perfeito ("tinha sido amado"). A ação do mais-que-perfeito já estava concluída no momento passado de que se fala.'),
        ('Esquecer a concordância do particípio: *<i>Iūlia laudātus est</i>, *<i>puerī vocātus sunt</i>.', 'O particípio é um adjetivo e concorda com o sujeito em gênero, número e caso: <i>Iūlia laudāta est</i>, <i>puerī vocātī sunt</i>, <i>dōna data sunt</i>. Antes de escrever, pergunte: qual é o sujeito, e qual é o seu gênero e número?'),
        ('Pegar a quarta parte do dicionário e usá-la sem mudar: *<i>Iūlia amātum est</i>.', 'Muitos dicionários dão a quarta parte em <i>-um</i> (<i>amātum</i>), que é o neutro do particípio (e o supino). Para formar a passiva, decline-a como <i>bonus, -a, -um</i> e faça-a concordar: <i>Iūlia amāta est</i>, <i>Mārcus amātus est</i>, <i>bellum amātum est</i>.'),
        ('Procurar um sujeito na passiva impessoal, ou traduzi-la literalmente: <i>pugnātum est</i> como "a luta foi lutada" ou "foi lutado".', 'Os intransitivos não têm passiva pessoal; <i>pugnātum est</i> não tem sujeito. Traduza por "lutou-se", "houve combate" ou "lutaram", e tire do contexto quem agiu. O neutro singular do particípio é a marca da construção.'),
        ('Confundir o infinitivo perfeito passivo com o ativo: <i>amātus esse</i> com <i>amāvisse</i>.', '<i>Amāvisse</i> (tema do perfeito + <i>-isse</i>) é "ter amado"; <i>amātus esse</i> (particípio + <i>esse</i>) é "ter sido amado". A presença do particípio, que concorda com alguém, é a marca da passiva.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Do perfeito ativo ao perfeito passivo',
            'Passe para a passiva e traduza: <i lang="la">Hostēs urbem cēpērunt et templa dēlēvērunt.</i> Vocabulário: <i>capiō, capere, cēpī, captum</i>, tomar; <i>dēleō, dēlēre, dēlēvī, dēlētum</i>, destruir; <i>templum, -ī</i> (n.), templo.', [
            ('Quais são os verbos e em que tempo estão?', '<i>Cēpērunt</i> e <i>dēlēvērunt</i>: perfeito ativo, 3ª pl. (tema do perfeito <i>cēp-</i>, <i>dēlēv-</i> + <i>-ērunt</i>). "Os inimigos tomaram a cidade e destruíram os templos."'),
            ('Quais serão os sujeitos das passivas?', 'Os objetos da ativa: <i>urbem</i> → <i>urbs</i> (nominativo singular, feminino) e <i>templa</i> → <i>templa</i> (nominativo plural, neutro; a forma não muda, só a função).'),
            ('Forme o primeiro perfeito passivo.', 'Particípio de <i>capiō</i>: <i>captus, -a, -um</i>. Concorda com <i>urbs</i>: feminino singular, <i>capta</i>. Auxiliar no presente, 3ª sing.: <i>est</i>. Resultado: <i>urbs capta est</i>, "a cidade foi tomada".'),
            ('Forme o segundo.', 'Particípio de <i>dēleō</i>: <i>dēlētus</i>. Concorda com <i>templa</i>: neutro plural, <i>dēlēta</i>. Auxiliar 3ª pl.: <i>sunt</i>. Resultado: <i>templa dēlēta sunt</i>.'),
            ('E os inimigos? Monte a frase e traduza.', 'Pessoas: agente com <i>ab</i> (diante de vogal), <i>ab hostibus</i>. <i>Urbs ab hostibus capta est et templa dēlēta sunt.</i> "A cidade foi tomada pelos inimigos, e os templos foram destruídos." Basta dizer o agente uma vez.'),
        ]),
        pratica_guiada('Prática guiada 2 · Uma passiva impessoal num relato',
            'Traduza: <i lang="la">Ā prīmā lūce ad merīdiem ācriter pugnātum est; tandem ad castra Rōmānōrum ventum est.</i> Vocabulário: <i>lūx, lūcis</i> (f.), luz (<i>prīmā lūce</i>, ao romper do dia); <i>merīdiēs, -ēī</i> (m.), meio-dia; <i>tandem</i>, finalmente; <i>veniō, venīre, vēnī, ventum</i>, vir, chegar.', [
            ('Qual é o primeiro verbo, e tem sujeito?', '<i>Pugnātum est</i>: perfeito passivo de <i>pugnō</i>, intransitivo. Não tem sujeito; o particípio está no neutro singular. É passiva impessoal: "lutou-se".'),
            ('Que função têm <i>ā prīmā lūce</i> e <i>ad merīdiem</i>?', 'Adjuntos de tempo: "desde o romper do dia" (<i>ā</i> + ablativo, ponto de partida) e "até o meio-dia" (<i>ad</i> + acusativo, limite). <i>Ā</i> aqui não é agente: <i>lūx</i> não é pessoa, e o sentido é temporal.'),
            ('E <i>ventum est</i>?', 'Perfeito passivo impessoal de <i>veniō</i>, intransitivo: "chegou-se". O particípio neutro <i>ventum</i> só existe nessa construção.'),
            ('Monte uma tradução natural.', '"Lutou-se duramente desde o romper do dia até o meio-dia; finalmente chegou-se ao acampamento dos romanos." Ou, explicitando os agentes pelo contexto: "Lutaram com ardor do amanhecer ao meio-dia; por fim chegaram ao acampamento dos romanos."'),
        ], 'Repare que a construção impessoal permite ao narrador falar da ação sem nomear os combatentes; a tradução portuguesa escolhe entre a passiva com "se" e o plural indeterminado.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Partes principais e perfeito passivo', 'Dê o particípio perfeito passivo (masculino) e o perfeito passivo na 3ª pessoa do singular, com sujeito masculino; traduza.', [
            ('<i>laudō, laudāre, laudāvī, laudātum</i>', '<i>laudātus</i>; <i>laudātus est</i>, "foi elogiado".'),
            ('<i>moneō, monēre, monuī, monitum</i>', '<i>monitus</i>; <i>monitus est</i>, "foi advertido".'),
            ('<i>dūcō, dūcere, dūxī, ductum</i>', '<i>ductus</i>; <i>ductus est</i>, "foi conduzido".'),
            ('<i>videō, vidēre, vīdī, vīsum</i>', '<i>vīsus</i>; <i>vīsus est</i>, "foi visto". (Como <i>videor</i> significa também "parecer", <i>vīsus est</i> pode ser "pareceu"; o contexto decide.)'),
            ('<i>scrībō, scrībere, scrīpsī, scrīptum</i>', '<i>scrīptus</i>; <i>scrīptus est</i>, "foi escrito". Com <i>liber</i>: <i>liber scrīptus est</i>; com <i>epistula</i>: <i>epistula scrīpta est</i>.'),
            ('<i>audiō, audīre, audīvī, audītum</i>', '<i>audītus</i>; <i>audītus est</i>, "foi ouvido".'),
        ]),
        exercicio('Exercício 2 · Analise e traduza a forma', 'Diga o tempo, a pessoa, o número e o gênero do sujeito, e traduza.', [
            ('<i>laudātae sunt</i>', 'Perfeito passivo, 3ª pl., sujeito feminino: "foram elogiadas".'),
            ('<i>missus erat</i>', 'Mais-que-perfeito passivo, 3ª sing., masculino: "tinha sido enviado".'),
            ('<i>captum erit</i>', 'Futuro perfeito passivo, 3ª sing., neutro: "terá sido tomado" (por exemplo, <i>oppidum</i>).'),
            ('<i>ductī estis</i>', 'Perfeito passivo, 2ª pl., masculino (ou grupo misto): "fostes conduzidos".'),
            ('<i>vocāta es</i>', 'Perfeito passivo, 2ª sing., feminino: "foste chamada". Fala-se a uma mulher.'),
            ('<i>audītī erāmus</i>', 'Mais-que-perfeito passivo, 1ª pl., masculino: "tínhamos sido ouvidos".'),
            ('<i>dēlēta erunt</i>', 'Futuro perfeito passivo, 3ª pl., neutro: "terão sido destruídos" (por exemplo, <i>templa</i>).'),
        ]),
        exercicio('Exercício 3 · Complete a concordância', 'Complete o particípio com a terminação certa e traduza. Vocabulário: <i>lēx, lēgis</i> (f.), lei; <i>scrībō</i>, escrever; <i>līberō, -āre</i>, libertar; <i>servus</i>, escravo; <i>vulnerō, -āre</i>, ferir.', [
            ('<i>Lēgēs ā cōnsule scrīpt__ sunt.</i>', '<i>scrīptae</i>: feminino plural, como <i>lēgēs</i>. "As leis foram escritas pelo cônsul."'),
            ('<i>Servī ā dominō līberāt__ erant.</i>', '<i>līberātī</i>: masculino plural. "Os escravos tinham sido libertados pelo senhor."'),
            ('<i>Bellum ā Rōmānīs gest__ est.</i>', '<i>gestum</i>: neutro singular, como <i>bellum</i>. "A guerra foi travada pelos romanos."'),
            ('<i>Iūlia et Mārcus ā patre laudāt__ sunt.</i>', '<i>laudātī</i>: sujeitos de gêneros diferentes que são pessoas → masculino plural (Bennett § 235.B.2). "Júlia e Marco foram elogiados pelo pai."'),
            ('<i>Dux sagittā vulnerāt__ est.</i>', '<i>vulnerātus</i>: masculino singular (<i>dux</i>, aqui um homem). "O comandante foi ferido por uma flecha." A flecha é meio: ablativo sem preposição.'),
        ]),
        exercicio('Exercício 4 · Mude a voz', 'Nos itens 1–3, passe para a passiva; nos itens 4–5, para a ativa. Mantenha o tempo.', [
            ('<i>Rōmānī Carthāginem dēlēvērunt.</i> (<i>Carthāgō, -inis</i>, f., Cartago)', '<i>Carthāgō ā Rōmānīs dēlēta est.</i> "Cartago foi destruída pelos romanos." Perfeito ativo → perfeito passivo; particípio feminino singular.'),
            ('<i>Magister puerōs monuerat.</i>', '<i>Puerī ā magistrō monitī erant.</i> "Os meninos tinham sido advertidos pelo mestre." Mais-que-perfeito → particípio + <i>erant</i>.'),
            ('<i>Iūlia epistulās scrīpserit.</i>', '<i>Epistulae ā Iūliā scrīptae erunt.</i> "As cartas terão sido escritas por Júlia." Futuro perfeito ativo → particípio + futuro de <i>esse</i>.'),
            ('<i>Oppidum ā mīlitibus captum est.</i>', '<i>Mīlitēs oppidum cēpērunt.</i> "Os soldados tomaram a cidade." O agente volta a ser sujeito; o perfeito passivo volta a ser perfeito ativo (<i>cēpērunt</i>, não *<i>capiunt</i>).'),
            ('<i>Puella ā mātre vocāta erat.</i>', '<i>Māter puellam vocāverat.</i> "A mãe tinha chamado a menina." Mais-que-perfeito ativo, 3ª sing.'),
        ]),
        exercicio('Exercício 5 · Passiva impessoal', 'Traduza de modo natural. Vocabulário: <i>currō, -ere</i>, correr; <i>dormiō, -īre</i>, dormir; <i>perveniō, -īre, -vēnī, -ventum</i>, chegar; <i>pugnō, -āre</i>, lutar; <i>clāmō, -āre</i>, gritar.', [
            ('<i>In forō curritur et clāmātur.</i>', '"No fórum corre-se e grita-se" ou "no fórum as pessoas correm e gritam". Duas passivas impessoais do presente.'),
            ('<i>Tōtā nocte nōn dormiēbātur.</i>', '"Durante a noite inteira não se dormia" ou "ninguém dormia a noite inteira". Imperfeito passivo impessoal de <i>dormiō</i>; <i>tōtā nocte</i>, ablativo de tempo.'),
            ('<i>Ad flūmen perventum est.</i>', '"Chegou-se ao rio" ou "chegaram ao rio". Perfeito passivo impessoal; particípio neutro <i>perventum</i>.'),
            ('<i>Diū pugnātum erat, cum nūntius vēnit.</i> (<i>cum</i>, quando)', '"Lutava-se havia muito tempo (tinha-se lutado longamente) quando chegou o mensageiro." Mais-que-perfeito passivo impessoal: a luta já durava quando o mensageiro chegou.'),
        ]),
        exercicio('Exercício 6 · Quadro dos seis tempos e retroversão', 'Nos itens 1–2, dê os seis tempos do indicativo, na 3ª pessoa do singular, ativa e passiva. Nos itens 3–4, passe para o latim.', [
            ('<i>vocō, vocāre, vocāvī, vocātum</i>', 'Ativa: <i>vocat, vocābat, vocābit, vocāvit, vocāverat, vocāverit</i>. Passiva: <i>vocātur, vocābātur, vocābitur, vocātus est, vocātus erat, vocātus erit</i>.'),
            ('<i>mittō, mittere, mīsī, missum</i>', 'Ativa: <i>mittit, mittēbat, mittet, mīsit, mīserat, mīserit</i>. Passiva: <i>mittitur, mittēbātur, mittētur, missus est, missus erat, missus erit</i>.'),
            ('A carta tinha sido escrita pelo poeta.', '<i>Epistula ā poētā scrīpta erat.</i> Mais-que-perfeito passivo; <i>scrīpta</i> concorda com <i>epistula</i>; agente pessoal com <i>ā</i>.'),
            ('As meninas foram chamadas, mas não vieram.', '<i>Puellae vocātae sunt, sed nōn vēnērunt.</i> Perfeito passivo com particípio feminino plural; depois, perfeito ativo de <i>veniō</i>.'),
        ]),
    ],
    leituras=['lhomond-urbis-romae-viri-illustres-selecoes', 'eutropius-breviarium-ab-urbe-condita', 'collar-the-gate-to-caesar-de-bello-gallico-ii-simplificado-e-original', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'ravizza-gramatica-latina', 'bennett-new-latin-grammar'],
    leituras_nota='O De viris illustribus de Lhomond e o Breviarium de Eutrópio (que você lerá no capítulo 43) narram a história romana em frases curtas, cheias de perfeitos passivos do tipo "foi eleito", "foi morto", "foi vencido": leia algumas vidas procurando o particípio e o seu sujeito. The Gate to Caesar apresenta a Guerra da Gália primeiro simplificada e depois no original, e é um bom lugar para encontrar a passiva impessoal dos relatos de batalha. Na Vulgata, o primeiro capítulo de Lucas e o primeiro de João têm vários perfeitos passivos. Ravizza (n. 90 e n. 140) e Bennett (§§ 102 e 256) resumem as regras.',
)
