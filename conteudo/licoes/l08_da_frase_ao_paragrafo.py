from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Texto original do capítulo (escrito para este livro só com a gramática dos capítulos 1–7; o resto vai glosado).
_P1 = ('<sup>1</sup> Flāvia Titusque in ōrā Campāniae habitant. <sup>2</sup> Avus nauta est et nāviculam caeruleam habet. '
       '<sup>3</sup> Hodiē puerī cum avō ad īnsulam nāvigant, nam avia in īnsulā habitat. '
       '<sup>4</sup> Titus rēmōs portat; Flāvia cibum et aquam in nāviculam portat.')
_P2 = ('<sup>5</sup> Prīmō caelum serēnum est, et aura nāviculam per undās movet. '
       '<sup>6</sup> Puerī laetī sunt et cantant; avus autem caelum spectat et tacet. '
       '<sup>7</sup> Nam ventus magnus ab Āfricā venit. <sup>8</sup> Mox undae magnae sunt, et aqua in nāviculam intrat. '
       '<sup>9</sup> Flāvia timet, sed avus nōn timet: rēmōs tenet et Titum vocat. '
       '<sup>10</sup> Titus situlā aquam ēicit. <sup>11</sup> Flāvia quoque labōrat et cibum servat.')
_P3 = ('<sup>12</sup> Tandem ventus cessat, et undae iam parvae sunt. '
       '<sup>13</sup> Avus nāviculam ad īnsulam dūcit; ibi avia in ōrā puerōs exspectat. '
       '<sup>14</sup> Avia nautam et puerōs videt et gaudet. <sup>15</sup> Itaque cēnam bonam parat. '
       '<sup>16</sup> Post cēnam Flāvia et Titus avō grātiās agunt. '
       '<sup>17</sup> Avus autem rīdet et fābulās dē ventīs et undīs nārrat. <sup>18</sup> Mox puerī in casā aviae dormiunt.')

_V1 = ('<i>Flāvia, -ae</i> (f.), Flávia · <i>Titus, -ī</i> (m.), Tito · <i>-que</i>, e (pendurado na 2ª palavra) · '
       '<i>ōra, -ae</i> (f.), costa, litoral · <i>Campānia, -ae</i> (f.), Campânia, região da Itália · <i>avus, -ī</i> (m.), avô · '
       '<i>nāvicula, -ae</i> (f.), barquinho · <i>caeruleus, -a, -um</i>, azul · <i>hodiē</i>, hoje · '
       '<i>puer, -ī</i> (m.), menino; no plural, também "crianças" (grupo misto) · <i>nam</i>, pois, é que · '
       '<i>avia, -ae</i> (f.), avó · <i>rēmus, -ī</i> (m.), remo · <i>cibus, -ī</i> (m.), comida')
_V2 = ('<i>prīmō</i>, no início · <i>serēnus, -a, -um</i>, sereno, limpo · <i>aura, -ae</i> (f.), brisa · '
       '<i>unda, -ae</i> (f.), onda · <i>moveō, -ēre</i>, mover · <i>laetus, -a, -um</i>, alegre · '
       '<i>autem</i>, porém, por sua vez (nunca em 1º lugar) · <i>taceō, -ēre</i>, calar-se, ficar quieto · '
       '<i>ventus, -ī</i> (m.), vento · <i>Āfrica, -ae</i> (f.), África · <i>mox</i>, logo, em pouco tempo · '
       '<i>intrō, -āre</i>, entrar · <i>timeō, -ēre</i>, ter medo · <i>teneō, -ēre</i>, segurar · '
       '<i>situla, -ae</i> (f.), balde · <i>ēiciō, -ere</i>, jogar para fora · <i>quoque</i>, também (depois da palavra) · '
       '<i>labōrō, -āre</i>, trabalhar · <i>servō, -āre</i>, guardar, proteger')
_V3 = ('<i>tandem</i>, finalmente · <i>cessō, -āre</i>, parar, cessar · <i>iam</i>, já, agora · '
       '<i>dūcō, -ere</i>, conduzir · <i>ibi</i>, ali · <i>exspectō, -āre</i>, esperar · <i>gaudeō, -ēre</i>, alegrar-se · '
       '<i>itaque</i>, por isso, e assim · <i>cēna, -ae</i> (f.), jantar · <i>parō, -āre</i>, preparar · '
       '<i>post</i> + ac., depois de · <i>grātiās agere</i> + dat., agradecer a (lit. "render graças") · '
       '<i>rīdeō, -ēre</i>, rir, sorrir · <i>dē</i> + abl., sobre, a respeito de · <i>casa, -ae</i> (f.), casa simples, cabana · '
       '<i>dormiō, -īre</i>, dormir')

_TEXTO = tabela(['Texto', 'Vocabulário ao lado'], [[_P1, _V1], [_P2, _V2], [_P3, _V3]],
                'Nāvicula avī ("O barquinho do avô"), texto original deste livro', latim_cols=(0,))

LICAO = dict(
    slug='08-da-frase-ao-paragrafo', titulo='Da frase ao parágrafo: técnica de leitura e primeiro texto corrido',
    titulo_latim='Prīma lēctiō', tempo='70 min',
    resumo='Um método para ler texto corrido: ler em voz alta, avançar na ordem latina, reconhecer onde cada frase termina e o que os conectivos anunciam, seguir o sujeito que não aparece, decidir ambiguidades pelo contexto e consultar o dicionário na hora certa. No centro, um texto original de dezoito frases e um primeiro versículo autêntico.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['técnica de leitura', 'leitura em voz alta', 'ordem latina e expectativas', 'fronteiras de frase', 'conectivos (et, -que, sed, autem, nam, itaque)',
             'sujeito oculto', 'referentes no parágrafo', 'ambiguidade e contexto', 'uso do dicionário durante a leitura', 'summarium', 'texto corrido original', 'Salmo 18,2 (Vulgata)'],
    prerequisitos=dict(texto='Capítulos 1–7: os casos, a primeira e a segunda declinação, os adjetivos de primeira classe, as preposições com acusativo e com ablativo, o presente do indicativo de esse e das quatro conjugações, e o uso do dicionário.',
                       licoes=['01-o-que-e-o-latim', '02-como-funciona-uma-frase-latina', '03-introducao-aos-casos', '04-a-primeira-declinacao',
                               '05-a-segunda-declinacao', '06-o-presente-do-indicativo', '07-como-usar-o-dicionario']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar',
                   nota='§ 166.2 e § 242.1 (o pronome sujeito fica implícito no verbo, salvo ênfase ou contraste); § 341 (et, -que: -que se pendura na segunda palavra); § 343.1 (sed; autem, pospositivo, marca transição); § 344.1 (itaque); § 345 (nam); § 346 (assíndeto); §§ 348–349 (ordem normal e ordem enfática)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc',
                   nota='§§ 223–224 (classes de conjunções coordenativas: copulativas, adversativas, causais, ilativas); § 323 (as coordenativas ligam construções iguais, no mesmo caso); § 324.a e d (et e -que; sed e autem, "a mais fraca das adversativas"); § 295.a (pronome pessoal não se exprime como sujeito, salvo distinção ou ênfase)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina',
                   nota='§§ 149–150 (conjunções coordenativas, em português: et, -que; sed sempre em primeiro lugar; autem "a mais branda das adversativas", depois de uma ou duas palavras; nam; itaque em primeiro lugar)', tipo='dominio_publico'),
        referencia('A Latin Dictionary (Lewis & Short)', 'Charlton T. Lewis e Charles Short', catalogo='short-a-latin-dictionary-lewis-short',
                   nota='verbete caelum: o plural masculino caelī, -ōrum é "muito frequente" no latim eclesiástico (cita Vulg. Psa.)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Salmo 18,2', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina',
                   url='https://la.wikisource.org/wiki/Vulgata_Clementina/Liber_Psalmorum',
                   nota='texto conferido na Wikisource latina (Caput 18, v. 2); grafia normalizada aqui (ae por æ, i por j, macrons acrescentados)', tipo='dominio_publico'),
    ],
    objetivos=[
        'Aplicar a um parágrafo latino um método de leitura em etapas: voz alta, leitura na ordem latina, releitura, consulta ao dicionário e tradução.',
        'Reconhecer as fronteiras de frase e o valor dos conectivos <i>et</i>, <i>-que</i>, <i>sed</i>, <i>autem</i>, <i>nam</i> e <i>itaque</i>, inclusive a posição de cada um.',
        'Identificar o sujeito de verbos sem sujeito expresso e acompanhar as pessoas e coisas de que um parágrafo fala.',
        'Resolver formas ambíguas (<i>-ae</i>, <i>-ī</i>, <i>-īs</i>, neutros) pelo número do verbo, pelas funções já ocupadas e pelo contexto.',
        'Ler e traduzir um texto corrido de dezoito frases e resumi-lo em latim (<i>summarium</i>).',
    ],
    secoes=[
        ('Ler um texto, não uma frase', f'''
<p>Até aqui você leu frases soltas, cada uma com todas as peças à vista: sujeito, objeto, verbo. Um texto funciona de outro modo. As frases se apoiam umas nas outras: o sujeito de uma continua valendo na seguinte, uma palavra pequena no começo anuncia se vem uma causa ou uma consequência, e o sentido de uma forma ambígua fica claro duas frases depois. Ler um parágrafo, portanto, não é ler dez frases isoladas uma depois da outra; é acompanhar um fio. Este capítulo propõe um método para segui-lo, em etapas que você pode repetir com qualquer texto do seu nível.</p>
{tabela(['Etapa', 'O que fazer', 'Por quê'], [
    ['1. Voz alta', 'Leia o parágrafo inteiro em voz alta, sem traduzir, respeitando as quantidades (capítulo 1).', 'O ouvido agrupa as palavras, percebe as pausas e fixa as terminações antes que você comece a analisar.'],
    ['2. Primeira passada', 'Leia na ordem latina, frase por frase, registrando o caso de cada nome e a pessoa de cada verbo, sem dicionário.', 'É a leitura por expectativas do capítulo 2: cada forma anuncia o que deve vir.'],
    ['3. Fio do texto', 'Anote quem são as personagens, onde estão e o que fazem; marque os conectivos.', 'Os sujeitos implícitos e os conectivos só fazem sentido no conjunto.'],
    ['4. Dicionário', 'Consulte só as palavras que impedem entender a frase.', 'Muitas palavras desconhecidas se esclarecem pelo contexto ou pelo português.'],
    ['5. Releitura e tradução', 'Releia em voz alta, agora entendendo; só então traduza por escrito.', 'A tradução é o último passo, não o primeiro: ela registra uma compreensão que já aconteceu.'],
    ['6. Summarium', 'Resuma o texto em três ou quatro frases latinas simples.', 'Resumir em latim prova que você entendeu sem passar pelo português.'],
], 'Um método de leitura em seis etapas')}
<p>A etapa 2 é a mais importante e a que mais exige paciência. No capítulo 2 você aprendeu a ler "como um romano ouvia": a cada palavra, registrar o caso e formular uma expectativa. Um nominativo pede um verbo; um acusativo pede um verbo que o receba; <i>cum</i> pede um ablativo; um verbo como <i>dat</i> pede alguém que recebe. Num texto, essa leitura ganha uma camada a mais, porque as expectativas atravessam as frases: se o parágrafo começou com <i>avus</i> e a frase seguinte traz só <i>rēmōs tenet</i>, você já sabe quem segura os remos.</p>
{dica('<b>Releia mais do que traduz.</b> Três leituras em voz alta de um parágrafo curto ensinam mais latim do que uma tradução palavra por palavra feita com o dicionário aberto. Se você traduzir cedo demais, a frase vira um quebra-cabeça de português e você para de ouvir o latim.')}
'''),
        ('Onde a frase termina: pontuação e conectivos', f'''
<p>Os manuscritos antigos quase não tinham pontuação; a que você vê nas edições modernas foi posta pelos editores. Ela ajuda, e você deve usá-la: o ponto final fecha uma frase, o ponto e vírgula separa duas orações independentes que o autor quis manter próximas, e os dois-pontos costumam introduzir uma explicação ou um detalhe do que acabou de ser dito. Mas a pontuação é uma interpretação do editor; a verdadeira fronteira de uma oração é o seu verbo. Cada verbo conjugado é o centro de uma oração, e cada oração precisa de um sujeito (expresso ou não) que concorde com ele. Quando você encontra um segundo verbo conjugado, começou uma nova oração.</p>
<p>Entre as orações aparecem pequenas palavras que dizem como a nova oração se relaciona com a anterior. São as <b>conjunções coordenativas</b>, que ligam orações independentes (Allen &amp; Greenough §§ 223–224; Ravizza n. 150). Elas valem ouro para o leitor, porque anunciam o tipo de informação que vem antes mesmo de ela chegar:</p>
{comparacao('Os conectivos deste capítulo', ['Conectivo', 'Relação', 'Posição', 'Exemplo do texto'], [
    ['et', 'adição: "e"', 'entre os termos ligados', '<i>Avus nauta est <b>et</b> nāviculam caeruleam habet.</i>'],
    ['-que', 'adição mais estreita: "e"', 'pendurado (enclítico) na <b>segunda</b> palavra ligada', '<i>Flāvia Titus<b>que</b></i> = Flávia e Tito'],
    ['sed', 'oposição: "mas"', 'sempre em primeiro lugar na oração', '<i>Flāvia timet, <b>sed</b> avus nōn timet.</i>'],
    ['autem', 'contraste fraco, transição: "porém, por sua vez"', 'nunca em primeiro lugar; em geral é a 2ª palavra', '<i>avus <b>autem</b> caelum spectat</i>'],
    ['nam', 'explicação, causa: "pois, é que"', 'em primeiro lugar', '<i><b>Nam</b> ventus magnus ab Āfricā venit.</i>'],
    ['itaque', 'consequência: "por isso, e assim"', 'em primeiro lugar', '<i><b>Itaque</b> cēnam bonam parat.</i>'],
])}
<p>Repare nas duas palavras que pedem atenção à posição. <b><i>-que</i></b> não é uma palavra separada: ela se cola no fim da segunda das duas palavras que liga, de modo que <i>Flāvia Titusque</i> vale "Flávia e Tito", e não "Flávia, e Tito também" (Bennett § 341.2.a). Ao ler, separe mentalmente <i>Titus|que</i> e transfira o "e" para antes da palavra. <b><i>Autem</i></b> é <b>pospositiva</b>: não pode abrir a oração, por isso vem depois da primeira palavra, e é essa primeira palavra que ela põe em contraste (Bennett § 343.1.c; Ravizza n. 150.e). Em <i>Puerī laetī sunt et cantant; avus autem caelum spectat</i>, o contraste é entre as crianças e o avô: elas cantam, ele, por sua vez, olha o céu. Allen & Greenough chamam <i>autem</i> de "a mais fraca das adversativas" (§ 324.d), e Ravizza observa que às vezes ela se traduz só por "e"; não a force a ser um "mas" pesado.</p>
<p><b><i>Nam</i></b> e <b><i>itaque</i></b> são os conectivos que mais ajudam a entender uma história, porque marcam a lógica dela. <i>Nam</i> olha para trás: a frase que ele abre explica a anterior (Bennett § 345). <i>Itaque</i> olha para a frente: a frase que ele abre é consequência da anterior (Bennett § 344.1). Quando você lê <i>nam</i>, pergunte "explica o quê?"; quando lê <i>itaque</i>, pergunte "consequência de quê?".</p>
{observacao('Quando não há conectivo', 'Às vezes duas orações aparecem lado a lado sem nenhuma conjunção, separadas só por vírgula ou ponto e vírgula. É o <b>assíndeto</b> (Bennett § 346), frequente em narração viva. A relação fica por conta do leitor: em <i>Titus rēmōs portat; Flāvia cibum et aquam portat</i>, o ponto e vírgula pede um "e" ou um "enquanto isso". Em português fazemos o mesmo: "Tito leva os remos; Flávia leva a comida".')}
'''),
        ('O sujeito que não aparece e o fio do parágrafo', f'''
<p>Em latim, o verbo traz o sujeito dentro de si: <i>cantat</i> já é "ele (ou ela) canta", <i>cantant</i>, "eles cantam". Por isso o pronome sujeito normalmente <b>não</b> é escrito; aparece só quando há ênfase ou contraste (Bennett § 166.2 e § 242.1; Allen &amp; Greenough § 295.a). O português faz o mesmo ("Chegou cedo e saiu tarde"), mas o latim leva o hábito mais longe, e num texto narrativo o sujeito de uma frase muitas vezes continua valendo para as frases seguintes, até que um <b>novo nominativo</b> apareça.</p>
<p>A regra prática é esta: <b>enquanto não surgir outro nominativo que concorde com o verbo, o sujeito é o último que foi mencionado e que combina em número com o verbo</b>. Veja como ela funciona em três frases do texto:</p>
{exemplos([
    ('Flāvia timet, sed <b>avus</b> nōn timet: rēmōs <b>tenet</b> et Titum <b>vocat</b>.', 'Flávia tem medo, mas o avô não tem medo: (ele) segura os remos e chama Tito. (Depois de <i>avus</i>, nenhum nominativo novo: <i>tenet</i> e <i>vocat</i> são do avô.)'),
    ('Avia nautam et puerōs videt et gaudet. Itaque cēnam bonam <b>parat</b>.', 'A avó vê o marinheiro e as crianças e se alegra. Por isso (ela) prepara um bom jantar. (<i>Parat</i> está na frase seguinte, mas o último sujeito singular foi <i>avia</i>.)'),
    ('<b>Puerī</b> laetī sunt et <b>cantant</b>; <b>avus</b> autem caelum spectat et <b>tacet</b>.', 'As crianças estão alegres e cantam; o avô, por sua vez, olha o céu e fica calado. (Cada novo nominativo muda o assunto; os verbos seguintes o acompanham.)'),
])}
<p>Seguir o fio também significa reconhecer a mesma personagem com nomes diferentes. Na frase 2 do texto você lê <i>Avus nauta est</i>, "o avô é marinheiro"; na frase 14, <i>Avia nautam et puerōs videt</i>: o "marinheiro" que a avó vê não é uma personagem nova, é o avô. Do mesmo modo, <i>puerī</i> retoma Flávia e Tito. Um bom hábito é manter, à margem, uma lista curta das personagens e de como o texto as chama.</p>
{observacao('Por que puerī, se Flávia é menina?', 'Em latim, quando um grupo mistura masculino e feminino, usa-se o masculino: <i>puerī</i> é "meninos", mas também "crianças", e o adjetivo que se refere a eles vai para o masculino plural (<i>puerī laetī</i>). O português faz o mesmo com "os filhos", "os alunos". A concordância, aliás, é outra ferramenta para seguir o fio: um adjetivo feminino singular só pode estar falando de Flávia ou da avó.')}
'''),
        ('Contexto, dicionário e summarium', f'''
<p>Num texto, quase toda forma ambígua se resolve sozinha. As mesmas perguntas que você fazia em frases soltas continuam valendo, mas agora com mais pistas: qual é o número do verbo? Que funções já estão ocupadas? O que as frases anteriores já contaram? Veja três casos do texto:</p>
{comparacao('Ambiguidades e o que as resolve', ['Forma', 'Pode ser', 'O que decide'], [
    ['aviae (fr. 18)', 'genitivo sing. · dativo sing. · nominativo pl.', 'O sujeito de <i>dormiunt</i> já é <i>puerī</i>, e há uma só avó na história: <i>in casā aviae</i>, "na casa <b>da</b> avó".'],
    ['avō (fr. 16)', 'dativo sing. · ablativo sing.', 'Não há preposição, e <i>grātiās agere</i> se faz <b>a</b> alguém: dativo, "agradecem <b>ao</b> avô". Na fr. 3, <i>cum avō</i> é ablativo por causa de <i>cum</i>.'],
    ['caelum (fr. 5 e 6)', 'nominativo · acusativo (neutro)', 'Na fr. 5, <i>caelum serēnum est</i>: com <i>est</i> e sem outro sujeito, é nominativo. Na fr. 6, o sujeito já é <i>avus</i>: <i>caelum</i> é o objeto de <i>spectat</i>.'],
    ['situlā (fr. 10)', 'nominativo sing. (situla) · ablativo sing. (situlā)', 'O sujeito é <i>Titus</i>; sem preposição, o ablativo indica o meio: "com um balde".'],
])}
<p><b>Quando abrir o dicionário?</b> Depois da primeira passada, não durante. Na primeira passada, sublinhe as palavras desconhecidas e siga em frente: muitas se esclarecem pelo contexto (<i>nāvicula</i>, ao lado de <i>nāvigant</i> e <i>rēmōs</i>, só pode ser uma embarcação) ou pelo português (<i>serēnum</i>, <i>intrat</i>, <i>cessat</i>). Consulte só as que impedem entender a frase, e use o que o capítulo 7 ensinou: procure pela forma de dicionário (nominativo singular; primeira pessoa do presente), leia o genitivo ou as partes principais para saber a declinação ou a conjugação, e escolha, entre os sentidos do verbete, o que cabe no contexto. Neste capítulo o vocabulário está ao lado do texto, como nos leitores graduados; tente mesmo assim fazer a primeira passada sem olhar para ele.</p>
<p>Por fim, o <b><i>summarium</i></b>. Resumir um texto em latim, em três ou quatro frases curtas, é o melhor teste de compreensão que você pode fazer sozinho: obriga a escolher o essencial, a reaproveitar o vocabulário e a construir frases corretas sem a muleta da tradução. Use frases simples (sujeito, objeto, verbo no presente), troque os detalhes pelo principal e mantenha a ordem dos acontecimentos. O exercício 6 pede um <i>summarium</i> do texto deste capítulo e traz um modelo.</p>
'''),
        ('Prīma lēctiō: o texto', f'''
<p>Eis o primeiro texto corrido deste livro. Foi escrito para ele, só com o que os capítulos 1–7 ensinaram: os casos, a primeira e a segunda declinação, os adjetivos de primeira classe, as preposições e o presente do indicativo. Os advérbios (<i>hodiē, prīmō, mox, tandem, iam, ibi</i>), os conectivos e as palavras novas estão glosados na coluna ao lado. Leia primeiro em voz alta, o parágrafo inteiro; depois faça a primeira passada sem olhar o vocabulário; só então confira.</p>
{_TEXTO}
<p>A prática guiada 1 percorre o primeiro parágrafo passo a passo; os exercícios 1 a 5 fazem o mesmo com o resto, e a tradução completa está no gabarito do exercício 5. Antes disso, veja duas frases de perto. A frase 6 reúne quase tudo o que este capítulo ensina: duas orações ligadas por ponto e vírgula, um sujeito que vale para dois verbos, uma troca de sujeito marcada por <i>autem</i> e um neutro ambíguo.</p>
{analise('Frase 6: Puerī laetī sunt et cantant; avus autem caelum spectat et tacet.', [
    ('Puerī', 'puer, -ī (m.), menino; pl., crianças', 'nominativo plural, 2ª declinação', 'sujeito de <i>sunt</i> e de <i>cantant</i>'),
    ('laetī', 'laetus, -a, -um, alegre', 'nominativo plural masculino, concorda com <i>puerī</i>', 'predicativo do sujeito'),
    ('sunt', 'sum, esse, ser, estar', 'presente, 3ª pessoa do plural', 'verbo de ligação'),
    ('et', 'et (conjunção)', 'invariável', 'liga duas orações com o mesmo sujeito'),
    ('cantant', 'cantō, -āre (1ª), cantar', 'presente, 3ª pessoa do plural', 'verbo; sujeito <i>puerī</i>, não repetido'),
    ('avus', 'avus, -ī (m.), avô', 'nominativo singular, 2ª declinação', 'novo sujeito: muda o assunto'),
    ('autem', 'autem (conjunção pospositiva)', 'invariável, em 2º lugar', 'contraste fraco: "o avô, por sua vez"'),
    ('caelum', 'caelum, -ī (n.), céu', 'nominativo ou acusativo singular (neutro); aqui acusativo', 'objeto direto: o sujeito já é <i>avus</i>'),
    ('spectat', 'spectō, -āre (1ª), olhar, observar', 'presente, 3ª pessoa do singular', 'verbo'),
    ('et', 'et (conjunção)', 'invariável', 'liga os dois verbos do avô'),
    ('tacet', 'taceō, -ēre (2ª), calar-se', 'presente, 3ª pessoa do singular', 'verbo; sujeito <i>avus</i>, não repetido'),
])}
<p>A frase 16 mostra como um grupo preposicional, um sujeito duplo e um dativo se encaixam antes do verbo, que só chega no fim e confirma tudo:</p>
{diagrama_frase([('Post cēnam', 'post + acusativo · quando'), ('Flāvia et Titus', 'nominativo · sujeito duplo'), ('avō', 'dativo · a quem'), ('grātiās', 'acusativo · objeto'), ('agunt', 'verbo plural · "dão"')],
    'Lendo em ordem: <i>Post cēnam Flāvia et Titus avō grātiās agunt</i> = Depois do jantar, Flávia e Tito agradecem ao avô (lit. "dão graças ao avô"). O verbo no plural confirma o sujeito duplo.')}
'''),
        ('Uma ponte para os textos reais: Salmo 18,2', f'''
<p>Com o método deste capítulo você já pode enfrentar um versículo autêntico. O Salmo 18 na Vulgata (19 na numeração hebraica) começa com uma frase famosa, que se lê quase toda com o que você sabe:</p>
{exemplos([('Caelī ēnārrant glōriam Deī, et opera manuum eius annūntiat firmāmentum.', 'Os céus narram a glória de Deus, e o firmamento anuncia as obras das mãos dele. (Sl 18,2 (19,2), Vulgata Clementina)')])}
<p>Três palavras ainda não foram estudadas e vão glosadas: <i>opera</i>, "obras" (de <i>opus, operis</i>, neutro da terceira declinação, capítulo 9), <i>manuum</i>, "das mãos" (de <i>manus</i>, quarta declinação, capítulo 11) e <i>eius</i>, "dele" (um pronome, capítulo 15). Há também uma surpresa de dicionário: <i>caelum</i>, que você conhece como neutro singular, tem no latim da Bíblia um plural masculino <i>caelī, -ōrum</i>, "os céus"; o dicionário de Lewis & Short registra esse plural como muito frequente nos autores cristãos.</p>
{analise('Sl 18,2, palavra a palavra', [
    ('Caelī', 'caelum, -ī (n.), céu; pl. eclesiástico caelī, -ōrum (m.)', 'nominativo plural masculino (poderia ser genitivo singular)', 'sujeito: <i>ēnārrant</i> é plural e não há outro nominativo'),
    ('ēnārrant', 'ēnārrō, -āre (1ª), narrar por inteiro, proclamar', 'presente, 3ª pessoa do plural', 'verbo da 1ª oração'),
    ('glōriam', 'glōria, -ae (f.), glória', 'acusativo singular', 'objeto direto'),
    ('Deī', 'deus, -ī (m.), deus', 'genitivo singular', '"de Deus", depende de <i>glōriam</i>'),
    ('et', 'et (conjunção)', 'invariável', 'liga as duas orações'),
    ('opera', 'opus, operis (n.), obra (3ª decl.)', 'nominativo ou acusativo plural (neutro); aqui acusativo', 'objeto direto'),
    ('manuum', 'manus, -ūs (f.), mão (4ª decl.)', 'genitivo plural', '"das mãos", depende de <i>opera</i>'),
    ('eius', 'pronome (capítulo 15)', 'genitivo singular', '"dele" (de Deus)'),
    ('annūntiat', 'annūntiō, -āre (1ª), anunciar', 'presente, 3ª pessoa do singular', 'verbo da 2ª oração'),
    ('firmāmentum', 'firmāmentum, -ī (n.), firmamento', 'nominativo ou acusativo singular (neutro); aqui nominativo', 'sujeito: o verbo é singular, e <i>opera</i> é plural'),
])}
<p>O ponto decisivo é a segunda oração. <i>Opera</i> e <i>firmāmentum</i> são ambos neutros, e nos neutros o nominativo e o acusativo são iguais; qual é o sujeito? O verbo responde: <i>annūntiat</i> é singular, e <i>opera</i> é plural; o sujeito só pode ser <i>firmāmentum</i>, guardado para o fim da frase. O paralelismo confirma: céus e firmamento são as duas faces da mesma imagem, cada um sujeito de um verbo de "dizer". Repare também que a ordem se inverte: na primeira oração o sujeito vem no começo, na segunda vem no fim. É a liberdade da ordem latina posta a serviço do estilo, e é por isso que o leitor deve confiar nas terminações, e não na posição.</p>
<p><b>Para levar deste capítulo:</b> leia em voz alta antes de analisar; avance na ordem latina criando expectativas; use os conectivos para prever a relação entre as frases; mantenha o sujeito até que um novo nominativo o substitua; resolva as ambiguidades pelo verbo, pelas funções ocupadas e pela história; abra o dicionário só depois da primeira passada; e confira a compreensão com um <i>summarium</i>.</p>
'''),
    ],
    erros_comuns=[
        ('Traduzir frase por frase como se cada uma fosse independente, e "inventar" um sujeito quando ele não aparece.', 'Num texto, o sujeito costuma continuar o da frase anterior. Em <i>Itaque cēnam bonam parat</i>, quem prepara o jantar é a avó, sujeito da frase 14; não há "alguém" indeterminado. Antes de traduzir um verbo sem sujeito expresso, volte ao último nominativo que concorda com ele em número.'),
        ('Tratar <i>-que</i> como parte da palavra (ou procurar <i>Titusque</i> no dicionário).', '<i>-que</i> é uma conjunção enclítica, colada à segunda palavra ligada: <i>Flāvia Titusque</i> = "Flávia e Tito". Separe-a e ponha o "e" antes da palavra. Cuidado com as palavras que apenas terminam em <i>-que</i>, como <i>quoque</i> ("também") e <i>itaque</i> ("por isso"): essas estão inteiras no dicionário.'),
        ('Traduzir <i>autem</i> pela palavra que vem antes dele, ou sempre por um "mas" forte.', '<i>Autem</i> é pospositiva: aparece em segundo lugar, mas pertence à oração inteira e põe em relevo a palavra que a precede. <i>Avus autem caelum spectat</i> = "o avô, por sua vez, olha o céu" ou "já o avô olha o céu". Muitas vezes "porém", "e" ou "já" soam mais naturais que "mas".'),
        ('Ler <i>nam</i> como "então" ou "portanto".', 'É o contrário: <i>nam</i> introduz a causa ou explicação do que veio antes ("pois, é que"), e <i>itaque</i> introduz a consequência ("por isso"). Em <i>avus caelum spectat et tacet. Nam ventus magnus ab Āfricā venit</i>, a frase com <i>nam</i> explica o silêncio do avô.'),
        ('Abrir o dicionário a cada palavra desconhecida já na primeira leitura.', 'Isso quebra o fio do texto e faz você perder o que o contexto já resolveria. Faça a primeira passada inteira, sublinhando as dúvidas; muitas desaparecem na segunda leitura. Consulte depois só o que bloqueia a compreensão.'),
        ('Decidir o caso de uma forma ambígua só pela posição.', 'Em <i>opera manuum eius annūntiat firmāmentum</i>, a primeira palavra não é o sujeito: <i>opera</i> é plural e o verbo é singular. O número do verbo e as funções já ocupadas decidem; a posição, no máximo, sugere.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · O primeiro parágrafo, passo a passo',
            'Leia em voz alta as frases 1 a 4 do texto (<i lang="la">Flāvia Titusque in ōrā Campāniae habitant ... Flāvia cibum et aquam in nāviculam portat.</i>) e siga as etapas do método.', [
            ('Frase 1. Que forma tem <i>Titusque</i>, e o que você espera depois de <i>Flāvia Titusque</i>?', '<i>Titus</i> + <i>-que</i> ("e"): "Flávia e Tito". São dois nominativos coordenados, portanto um sujeito duplo; espera-se um verbo no <b>plural</b>.'),
            ('Ainda na frase 1: <i>in ōrā Campāniae</i> e o verbo.', '<i>In</i> + ablativo (<i>ōrā</i>, com <i>ā</i> longo): lugar onde, "na costa". <i>Campāniae</i> é genitivo, ligado a <i>ōrā</i>: "da Campânia". <i>Habitant</i>, plural, confirma o sujeito duplo: "Flávia e Tito moram na costa da Campânia".'),
            ('Frase 2. Quantas orações há, e qual é o sujeito de <i>habet</i>?', 'Duas, ligadas por <i>et</i>: <i>Avus nauta est</i> ("o avô é marinheiro"; <i>nauta</i> é predicativo, no nominativo) e <i>nāviculam caeruleam habet</i>. Não aparece outro nominativo: o sujeito de <i>habet</i> continua sendo <i>avus</i>. "...e tem um barquinho azul."'),
            ('Frase 3. Quem são os <i>puerī</i>, e o que <i>nam</i> anuncia?', '<i>Puerī</i> retoma Flávia e Tito (masculino plural para um grupo misto): "as crianças". <i>Cum avō</i>: ablativo de companhia; <i>ad īnsulam</i>: destino. <i>Nam</i> anuncia uma explicação: por que vão à ilha? Porque <i>avia in īnsulā habitat</i>, "a avó mora na ilha".'),
            ('Frase 4. Que relação liga as duas orações, se não há conjunção?', 'O ponto e vírgula separa duas orações paralelas, cada uma com seu sujeito: <i>Titus rēmōs portat</i>; <i>Flāvia cibum et aquam in nāviculam portat</i>. É um assíndeto: a relação é de simultaneidade ("Tito leva os remos; Flávia leva comida e água para o barquinho"). <i>In nāviculam</i>, com acusativo, indica movimento: "para dentro do barquinho".'),
            ('Agora faça um pequeno quadro das personagens.', 'Flávia e Tito (= <i>puerī</i>), o avô (<i>avus</i>, marinheiro, dono do barquinho), a avó (<i>avia</i>, mora na ilha). Lugares: a costa da Campânia e a ilha.'),
        ], 'Com o quadro das personagens montado, o resto do texto se lê muito mais depressa: você já sabe a quem cada verbo pode se referir.'),
        pratica_guiada('Prática guiada 2 · Seguir o fio no último parágrafo',
            'Nas frases 12 a 18, diga quem é o sujeito de cada verbo e como você sabe.', [
            ('<i>cessat</i> (fr. 12) e <i>sunt</i> (fr. 12)', '<i>Ventus</i> (nominativo singular) para <i>cessat</i>; <i>undae</i> (nominativo plural, confirmado pelo plural <i>sunt</i>) para <i>sunt</i>. Cada oração tem seu sujeito expresso.'),
            ('<i>dūcit</i> e <i>exspectat</i> (fr. 13)', '<i>Avus</i> conduz o barquinho; depois de <i>ibi</i>, um novo nominativo, <i>avia</i>, é o sujeito de <i>exspectat</i>. <i>Puerōs</i> é acusativo: são as crianças que ela espera.'),
            ('<i>videt</i> e <i>gaudet</i> (fr. 14); <i>parat</i> (fr. 15)', 'Todos da avó. Na fr. 14 ela é o nominativo expresso; na fr. 15 não aparece nenhum nominativo novo, e <i>itaque</i> liga a frase à anterior: "por isso (a avó) prepara um bom jantar". <i>Nautam</i>, objeto de <i>videt</i>, é o avô.'),
            ('<i>agunt</i> (fr. 16) e <i>rīdet</i>, <i>nārrat</i> (fr. 17)', '<i>Flāvia et Titus</i> (plural) agradecem; na fr. 17, <i>avus autem</i> traz um novo sujeito singular, que vale para <i>rīdet</i> e <i>nārrat</i>. <i>Autem</i> marca a troca: as crianças agradecem; o avô, por sua vez, sorri.'),
            ('<i>dormiunt</i> (fr. 18)', '<i>Puerī</i>, nominativo plural, concordando com o verbo plural. <i>Aviae</i> não pode ser o sujeito (o lugar está ocupado); é genitivo: "na casa da avó".'),
        ]),
    ],
    exercicios=[
        exercicio('Exercício 1 · Compreensão', 'Responda em português, citando as palavras latinas que sustentam a sua resposta.', [
            ('Onde moram Flávia e Tito?', 'Na costa da Campânia: <i>in ōrā Campāniae</i> (fr. 1), <i>in</i> + ablativo de lugar e um genitivo.'),
            ('Por que as crianças vão à ilha?', 'Porque a avó mora lá: <i>nam avia in īnsulā habitat</i> (fr. 3). <i>Nam</i> introduz a explicação.'),
            ('Por que o avô fica calado enquanto as crianças cantam?', 'Porque ele vê o tempo mudar: a frase 7, aberta por <i>nam</i>, explica que <i>ventus magnus ab Āfricā venit</i>, "um vento forte vem da África".'),
            ('O que Tito e Flávia fazem durante o mau tempo?', 'Tito joga a água para fora com um balde (<i>situlā aquam ēicit</i>, fr. 10); Flávia também trabalha e protege a comida (<i>Flāvia quoque labōrat et cibum servat</i>, fr. 11).'),
            ('Na frase 14, quem é o <i>nauta</i> que a avó vê?', 'O avô. A frase 2 já disse <i>Avus nauta est</i>; o texto retoma a mesma personagem com outro nome.'),
            ('Por que a avó prepara um bom jantar?', 'Porque se alegra ao ver o marido e os netos chegarem bem: <i>gaudet</i> (fr. 14), e a frase 15 começa com <i>itaque</i>, "por isso".'),
            ('O que o avô faz depois do jantar?', 'Sorri e conta histórias sobre ventos e ondas: <i>rīdet et fābulās dē ventīs et undīs nārrat</i> (fr. 17).'),
        ]),
        exercicio('Exercício 2 · Conectivos e fronteiras', 'Para cada trecho, diga quantas orações há, que conectivo as liga e que relação ele expressa. Nas frases novas, o vocabulário é o do texto.', [
            ('<i>Flāvia timet, sed avus nōn timet.</i>', 'Duas orações (dois verbos conjugados), ligadas por <i>sed</i>: oposição. "Flávia tem medo, mas o avô não tem."'),
            ('<i>Mox undae magnae sunt, et aqua in nāviculam intrat.</i>', 'Duas orações, ligadas por <i>et</i>: adição (aqui, quase uma consequência: as ondas crescem e a água entra).'),
            ('<i>Avia puerōs videt. Itaque gaudet.</i>', 'Duas frases; <i>itaque</i> marca consequência: a avó se alegra <b>porque</b> vê as crianças. "A avó vê as crianças. Por isso se alegra."'),
            ('<i>Avia gaudet. Nam puerōs videt.</i>', 'As mesmas ideias na ordem inversa: <i>nam</i> introduz a causa. "A avó se alegra. É que vê as crianças." Compare com o item anterior: <i>itaque</i> e <i>nam</i> descrevem a mesma relação de lados opostos.'),
            ('<i>Puerī rēmōs cibumque portant.</i>', 'Uma oração só (um verbo). <i>-que</i> liga dois objetos: <i>rēmōs</i> e <i>cibum</i>. "As crianças carregam os remos e a comida."'),
            ('<i>Titus labōrat; Flāvia quoque labōrat.</i>', 'Duas orações em assíndeto (ponto e vírgula, sem conjunção). <i>Quoque</i> não é conjunção, mas um advérbio pospositivo, "também": "Tito trabalha; Flávia também trabalha."'),
        ]),
        exercicio('Exercício 3 · Quem faz?', 'Em cada trecho, diga o sujeito do verbo em destaque e explique como você o identificou.', [
            ('<i>Avus nauta est et nāviculam caeruleam <b>habet</b>.</i>', '<i>Avus</i>: é o último nominativo singular, e nenhum outro aparece antes de <i>habet</i>. (<i>Nauta</i> também é nominativo, mas é o predicativo de <i>est</i>, a mesma pessoa.)'),
            ('<i>Puerī laetī sunt et <b>cantant</b>.</i>', '<i>Puerī</i>: o verbo é plural, e <i>puerī</i> é o único nominativo plural.'),
            ('<i>Avus nāviculam ad īnsulam dūcit; ibi avia in ōrā puerōs <b>exspectat</b>.</i>', '<i>Avia</i>: um novo nominativo aparece antes do verbo e muda o sujeito. <i>Puerōs</i> é acusativo (objeto), não sujeito.'),
            ('<i>Avia nautam et puerōs videt et gaudet. Itaque cēnam bonam <b>parat</b>.</i>', '<i>Avia</i>: nenhum nominativo novo na segunda frase; o último sujeito singular é a avó. <i>Nautam</i> e <i>puerōs</i> são acusativos.'),
            ('<i>Post cēnam Flāvia et Titus avō grātiās agunt. Avus autem rīdet et fābulās <b>nārrat</b>.</i>', '<i>Avus</i>: <i>autem</i> acompanha um novo nominativo singular, que vale para <i>rīdet</i> e <i>nārrat</i>. <i>Fābulās</i> é o objeto.'),
        ]),
        exercicio('Exercício 4 · O contexto decide', 'Cada forma em destaque poderia ter mais de um caso. Diga qual é o caso aqui e o que decide.', [
            ('<i>Mox puerī in casā <b>aviae</b> dormiunt.</i>', 'Genitivo singular, "da avó". Não pode ser sujeito plural (o sujeito é <i>puerī</i>), nem dativo (ninguém dá nada a ela); depende de <i>casā</i>.'),
            ('<i>Post cēnam Flāvia et Titus <b>avō</b> grātiās agunt.</i>', 'Dativo singular, "ao avô": sem preposição, e agradece-se <b>a</b> alguém. Com <i>cum</i> (<i>cum avō</i>, fr. 3) seria ablativo.'),
            ('<i>Prīmō <b>caelum</b> serēnum est.</i>', 'Nominativo: com <i>est</i> e nenhum outro candidato, <i>caelum</i> é o sujeito, e <i>serēnum</i>, o predicativo neutro que concorda com ele.'),
            ('<i>Avus autem <b>caelum</b> spectat.</i>', 'Acusativo: o sujeito já é <i>avus</i>, e <i>spectat</i> pede um objeto.'),
            ('<i><b>Puerī</b> laetī sunt.</i>', 'Nominativo plural, não genitivo singular: o verbo <i>sunt</i> é plural e não há outro sujeito; <i>laetī</i>, nominativo plural, concorda com ele.'),
            ('<i>Titus <b>situlā</b> aquam ēicit.</i>', 'Ablativo singular (<i>situlā</i>, com <i>ā</i> longo): o sujeito é <i>Titus</i> e o objeto é <i>aquam</i>; a forma sem preposição indica o meio, "com um balde".'),
        ]),
        exercicio('Exercício 5 · Tradução do texto', 'Traduza o texto inteiro, parágrafo por parágrafo, depois de lê-lo em voz alta pelo menos duas vezes. Compare a sua tradução com a do gabarito; diferenças de estilo são normais, desde que as funções estejam corretas.', [
            ('Parágrafo 1 (frases 1–4)', '"Flávia e Tito moram na costa da Campânia. O avô é marinheiro e tem um barquinho azul. Hoje as crianças navegam com o avô até a ilha, pois a avó mora na ilha. Tito leva os remos; Flávia leva comida e água para o barquinho." Pontos de controle: <i>-que</i> (fr. 1), <i>nauta</i> predicativo (fr. 2), <i>nam</i> explicativo (fr. 3), <i>in</i> + acusativo de movimento (fr. 4).'),
            ('Parágrafo 2 (frases 5–11)', '"No início o céu está limpo, e a brisa move o barquinho pelas ondas. As crianças estão alegres e cantam; o avô, por sua vez, observa o céu e fica calado. É que um vento forte vem da África. Logo as ondas ficam grandes, e a água entra no barquinho. Flávia tem medo, mas o avô não tem: segura os remos e chama Tito. Tito joga a água para fora com um balde. Flávia também trabalha e protege a comida." Pontos de controle: <i>autem</i> (fr. 6), <i>nam</i> (fr. 7), sujeito implícito de <i>tenet</i> e <i>vocat</i> (fr. 9), ablativo de meio <i>situlā</i> (fr. 10).'),
            ('Parágrafo 3 (frases 12–18)', '"Finalmente o vento para, e as ondas já estão pequenas. O avô conduz o barquinho até a ilha; ali a avó espera as crianças na praia. A avó vê o marinheiro e as crianças e se alegra. Por isso prepara um bom jantar. Depois do jantar, Flávia e Tito agradecem ao avô. O avô, porém, sorri e conta histórias sobre ventos e ondas. Logo as crianças dormem na casa da avó." Pontos de controle: <i>in ōrā</i>, aqui "na praia, na costa" (fr. 13), <i>nautam</i> = o avô (fr. 14), <i>itaque</i> (fr. 15), dativo <i>avō</i> (fr. 16), genitivo <i>aviae</i> (fr. 18).'),
        ]),
        exercicio('Exercício 6 · Summarium', 'Escreva em latim um resumo do texto em três a cinco frases, usando só o vocabulário dele e o presente. Mantenha a ordem dos acontecimentos e prefira frases simples.', [
            ('Seu <i>summarium</i>', 'Modelo: <i lang="la">Avus cum puerīs ad īnsulam nāvigat. Ventus magnus undās movet, sed avus nōn timet. Tandem nāvicula ad īnsulam venit, et avia puerōs exspectat. Avia cēnam parat, et puerī in casā aviae dormiunt.</i> ("O avô navega com as crianças até a ilha. Um vento forte agita as ondas, mas o avô não tem medo. Finalmente o barquinho chega à ilha, e a avó espera as crianças. A avó prepara o jantar, e as crianças dormem na casa da avó.") Confira na sua versão: cada verbo concorda com o seu sujeito (<i>avus ... nāvigat</i>, <i>puerī ... dormiunt</i>); <i>cum</i>, <i>in</i> (lugar) e <i>ē/ex</i> com ablativo, <i>ad</i> e <i>in</i> (movimento) com acusativo; os conectivos dizem a relação certa (<i>sed</i> para oposição, <i>itaque</i> para consequência, <i>nam</i> para causa).'),
        ]),
    ],
    leituras=['sonnenschein-ora-maritima-a-latin-story-for-beginners', 'jones-puer-romanus', 'appleton-fabulae-virginibus-puerisque-aut-narrandae-aut-recitandae',
              'nutting-a-first-latin-reader', 'kingdon-gradatim-an-easy-latin-translation-book', 'vulgata-biblia-sacra-vulgata-editio-clementina'],
    leituras_nota='Aplique o método deste capítulo a um texto graduado por semana: os primeiros capítulos de Ora Maritima e de Puer Romanus são feitos de parágrafos curtos, no presente, com as duas primeiras declinações; as Fabulae de Appleton, o First Latin Reader de Nutting e o Gradatim de Kingdon trazem histórias breves em dificuldade crescente (nesses, glose o que ainda não estudou). Na Vulgata, os Salmos e o início dos Evangelhos oferecem versículos curtos para treinar a passagem ao texto autêntico.',
)
