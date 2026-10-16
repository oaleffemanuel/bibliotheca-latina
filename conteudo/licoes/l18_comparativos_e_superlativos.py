from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='18-comparativos-e-superlativos', titulo='Comparativos, superlativos e advérbios',
    titulo_latim='Dē gradibus comparātiōnis', tempo='70 min',
    resumo='Os graus do adjetivo: como se formam o comparativo em -ior, -ius (declinado como um tema consonantal) e o superlativo em -issimus, -errimus e -illimus; a comparação irregular (bonus, melior, optimus e os seus pares); as duas maneiras de dizer "do que" (quam e o ablativo de comparação); os sentidos do superlativo; a formação dos advérbios de modo (-ē, -iter) e a sua comparação.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['graus do adjetivo', 'comparativo em -ior, -ius', 'declinação do comparativo', 'superlativo em -issimus', 'superlativo em -errimus', 'superlativo em -illimus', 'magis e maximē', 'comparação irregular', 'plūs, plūrēs', 'comparativos sem positivo', 'quam', 'ablativo de comparação', 'ablativo de grau de diferença (multō, paulō)', 'superlativo absoluto e relativo', 'quam + superlativo', 'formação dos advérbios (-ē, -iter, -ter)', 'comparação dos advérbios', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 5 (adjetivos de primeira classe, <i>bonus, -a, -um</i>), capítulo 9 (as terminações dos temas consonantais, que são as do comparativo) e capítulo 10 (adjetivos de segunda classe, como <i>fortis, forte</i>). O capítulo 4 (preposições com ablativo) e o capítulo 9 (a análise de Lucas 2,14, com <i>altissimīs</i>) são retomados.',
                       licoes=['05-a-segunda-declinacao', '09-a-terceira-declinacao-temas-consonantais', '10-a-terceira-declinacao-temas-em-i']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 69 e 69.1 (declinação de fortior; todos os comparativos se declinam assim), § 70 (declinação de plūs), §§ 71–75 (formação do comparativo e do superlativo; -rimus; cinco adjetivos em -ilis; comparação irregular, defectiva e com magis/maximē), §§ 76–77 (formação e comparação dos advérbios), § 217 (ablativo de comparação e seus limites), § 223 (ablativo de grau de diferença), § 240 (comparativo "um tanto, demasiado"; superlativo "muito"; vel e quam com o superlativo; dois comparativos)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', url='https://dcc.dickinson.edu/grammar/latin/comparison-adjectives', nota='§ 120 (declinação dos comparativos; plūs), §§ 123–128 (formação; seis adjetivos em -lis; magis e maximē), §§ 129–131 (comparação irregular e defectiva), § 214 (formação dos advérbios), § 218 (comparação dos advérbios), § 11.d e nota (sílaba pesada antes de i consonantal: maior, peius), §§ 291–292 (sentidos do comparativo e do superlativo; quam, vel, ūnus; 292.a nota, mistura de comparativo e positivo, rara), §§ 406–407 (ablativo de comparação e quam), § 414 (grau de diferença)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§§ 76–82 (os três graus; declinação de tristior, com a observação de que o ablativo em -ī é raro e tardio; superlativo de temas em -ro-, -ri- e dos seis em -ili-; comparação irregular; plūs), §§ 85–86 (comparação dos advérbios)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='nn. 55–58 (graus; formação; comparativo com ablativo em -e, plural neutro em -a e genitivo plural em -um; seis adjetivos em -ilis; irregulares; advérbios), nn. 59–60 (sintaxe: comparativo com quam ou ablativo; multō; superlativo absoluto e relativo)', tipo='dominio_publico'),
        referencia('Horácio, Epístolas I, 1, 52', None, url='https://www.thelatinlibrary.com/horace/epist1.shtml', nota='verso da seção 6, conferido na The Latin Library; grafia u/v normalizada para v e macrons acrescentados', tipo='dominio_publico'),
        referencia('César, De bello Gallico I, 1, 3', None, catalogo='caesar-commentarii-de-bello-gallico-texto-integral', url='https://www.thelatinlibrary.com/caesar/gall1.shtml', nota='frase da seção 6, conferida na The Latin Library; macrons acrescentados', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Mateus 10,31; 22,38; 26,75', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Matthaeum', nota='frases da seção 6, conferidas na Wikisource latina; ortografia da edição mantida, macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Formar o comparativo (<i>-ior, -ius</i>) e o superlativo (<i>-issimus</i>, <i>-errimus</i>, <i>-illimus</i>) de adjetivos de primeira e de segunda classe a partir do tema.',
        'Declinar o comparativo como um tema consonantal (ablativo em <i>-e</i>, genitivo plural em <i>-um</i>, neutro plural em <i>-a</i>) e o superlativo como <i>bonus</i>.',
        'Reconhecer a comparação irregular (<i>melior, optimus; peior, pessimus; maior, maximus; minor, minimus; plūs, plūrimus</i>) e os comparativos sem positivo (<i>prior, prīmus</i>; <i>superior, summus</i>…).',
        'Traduzir o segundo termo da comparação, com <i>quam</i> ou com o ablativo de comparação, sabendo quando o ablativo não pode ser usado.',
        'Formar advérbios de modo (<i>-ē</i>, <i>-iter</i>, <i>-ter</i>) e os seus graus (<i>-ius</i>, <i>-issimē</i>), inclusive os irregulares (<i>bene, melius, optimē</i>).',
    ],
    secoes=[
        ('Os três graus e o comparativo regular', f'''
<p>Um adjetivo de qualidade pode aparecer em três <b>graus</b>. O <b>positivo</b> é o adjetivo simples, como você o conhece desde o capítulo 5: <i>longus</i>, "longo". O <b>comparativo</b> põe duas coisas em confronto e diz que uma tem a qualidade em grau maior: <i>longior</i>, "mais longo". O <b>superlativo</b> leva a qualidade ao grau mais alto: <i>longissimus</i>, "o mais longo" ou "longuíssimo". O português faz quase tudo isso com palavras à parte ("mais", "o mais", "muito"); o latim, na maioria dos adjetivos, faz com <b>sufixos</b> colados ao tema, e é por isso que você precisa saber achar o tema.</p>
<p>A regra de formação do comparativo é uma só para as duas classes de adjetivos: tome o <b>genitivo singular</b>, tire a terminação (<i>-ī</i> na primeira classe, <i>-is</i> na segunda) e acrescente <b><i>-ior</i></b> para o masculino e o feminino, <b><i>-ius</i></b> para o neutro. O genitivo é o ponto de partida pela mesma razão do capítulo 9: em adjetivos como <i>fēlīx</i> ou <i>prūdēns</i>, só ele mostra o tema (<i>fēlīc-</i>, <i>prūdent-</i>).</p>
{tabela(['Positivo (nom. · gen.)', 'Tema', 'Comparativo m./f. · n.', 'Significado'], [
    ['longus · longī', 'long-', 'long<b>ior</b> · long<b>ius</b>', 'longo → mais longo'],
    ['altus · altī', 'alt-', 'alt<b>ior</b> · alt<b>ius</b>', 'alto, profundo → mais alto'],
    ['clārus · clārī', 'clār-', 'clār<b>ior</b> · clār<b>ius</b>', 'claro, famoso → mais famoso'],
    ['līber · līberī', 'līber-', 'līber<b>ior</b> · līber<b>ius</b>', 'livre → mais livre'],
    ['pulcher · pulchrī', 'pulchr-', 'pulchr<b>ior</b> · pulchr<b>ius</b>', 'belo → mais belo'],
    ['fortis · fortis', 'fort-', 'fort<b>ior</b> · fort<b>ius</b>', 'forte, valente → mais forte'],
    ['brevis · brevis', 'brev-', 'brev<b>ior</b> · brev<b>ius</b>', 'breve → mais breve'],
    ['ācer · ācris', 'ācr-', 'ācr<b>ior</b> · ācr<b>ius</b>', 'agudo, enérgico → mais enérgico'],
    ['fēlīx · fēlīcis', 'fēlīc-', 'fēlīc<b>ior</b> · fēlīc<b>ius</b>', 'feliz → mais feliz'],
    ['prūdēns · prūdentis', 'prūdent-', 'prūdent<b>ior</b> · prūdent<b>ius</b>', 'prudente → mais prudente'],
], 'Formação do comparativo: genitivo sem a terminação + -ior, -ius', latim_cols=(0, 1, 2))}
<h3>A declinação do comparativo</h3>
<p>O comparativo tem, no nominativo, só duas formas (<i>longior</i> para o masculino e o feminino, <i>longius</i> para o neutro), como os adjetivos de segunda classe do capítulo 10 (<i>fortis, forte</i>). Mas atenção: ele <b>não</b> se declina como <i>fortis</i>. Os comparativos são <b>temas consonantais</b>: o tema real é <i>longiōr-</i>, e as terminações são exatamente as de <i>rēx</i> e <i>corpus</i>, que você aprendeu no capítulo 9. Isso dá três diferenças em relação a <i>fortis</i>: ablativo singular em <b><i>-e</i></b> (<i>longiōre</i>, não *<i>longiōrī</i>), genitivo plural em <b><i>-um</i></b> (<i>longiōrum</i>, não *<i>longiōrium</i>) e neutro plural em <b><i>-a</i></b> (<i>longiōra</i>, não *<i>longiōria</i>).</p>
{tabela_declinacao('Comparativo: longior, longius, "mais longo"', [
    ('longior', 'longius', 'longiōr<b>ēs</b>', 'longiōr<b>a</b>'), ('longiōr<b>is</b>', 'longiōr<b>is</b>', 'longiōr<b>um</b>', 'longiōr<b>um</b>'),
    ('longiōr<b>ī</b>', 'longiōr<b>ī</b>', 'longiōr<b>ibus</b>', 'longiōr<b>ibus</b>'), ('longiōr<b>em</b>', 'longius', 'longiōr<b>ēs</b>', 'longiōr<b>a</b>'),
    ('longior', 'longius', 'longiōr<b>ēs</b>', 'longiōr<b>a</b>'), ('longiōr<b>e</b>', 'longiōr<b>e</b>', 'longiōr<b>ibus</b>', 'longiōr<b>ibus</b>')],
    colunas=('m./f. · sing.', 'neutro · sing.', 'm./f. · pl.', 'neutro · pl.'))}
<p>Repare na vogal: o <i>o</i> é breve no nominativo masculino e feminino (<i>longior</i>) e longo em todos os outros casos (<i>longiōris, longiōrem</i>). O neutro <i>longius</i> conserva no nominativo e no acusativo um antigo <i>s</i> que, entre vogais, passou a <i>r</i> nos outros casos: é o mesmo rotacismo de <i>corpus, corporis</i> (capítulo 9). Por isso <i>longius</i>, apesar do <i>-us</i>, é <b>neutro</b> e não tem nada a ver com a segunda declinação: <i>iter longius</i>, "um caminho mais longo", e nunca *<i>vir longius</i>.</p>
{comparacao('fortis (capítulo 10) e o seu comparativo fortior: onde diferem', ['Caso', 'fortis, forte (tema em -i)', 'fortior, fortius (tema consonantal)'], [
    ['ablativo singular', 'fort<b>ī</b>', 'fortiōr<b>e</b>'],
    ['genitivo plural', 'fort<b>ium</b>', 'fortiōr<b>um</b>'],
    ['nom./ac. plural neutro', 'fort<b>ia</b>', 'fortiōr<b>a</b>'],
    ['nominativo singular', 'fortis · forte', 'fortior · fortius'],
])}
<p>As gramáticas registram também um ablativo em <i>-ī</i> e um acusativo plural em <i>-īs</i> para o comparativo, mas como formas raras; Kennedy (§ 77) observa que o ablativo em <i>-ī</i> é raro e de escritores tardios, e Ravizza (n. 55) recomenda o <i>-e</i>. Escreva sempre <i>-e</i>.</p>
{observacao('O comparativo nem sempre compara', 'Sem segundo termo expresso, o comparativo indica muitas vezes que a qualidade é bastante forte, ou forte demais: <i>via longior</i> pode ser "um caminho bem longo" ou "longo demais", conforme o contexto; Bennett (§ 240.1) dá o exemplo <i>senectūs est loquācior</i>, "a velhice é um tanto tagarela". Antes de pôr "mais" na tradução, pergunte: mais do que o quê?')}
'''),
        ('O superlativo', f'''
<p>O superlativo regular se forma do mesmo tema que o comparativo, com o sufixo <b><i>-issimus, -issima, -issimum</i></b>, e se declina inteiramente como <i>bonus, -a, -um</i>, nos três gêneros: <i>longissimus</i>, <i>fortissima</i>, <i>fēlīcissimum</i>, <i>prūdentissimōrum</i>. Duas famílias de adjetivos fogem a essa regra, e a terceira forma vem de outro procedimento.</p>
<h3>Adjetivos em -er: -errimus</h3>
<p>Os adjetivos com nominativo masculino em <i>-er</i>, da primeira ou da segunda classe, acrescentam <b><i>-rimus</i></b> ao próprio nominativo, e não ao tema: <i>pulcher</i> → <i>pulcherrimus</i>; <i>līber</i> → <i>līberrimus</i>; <i>miser</i> → <i>miserrimus</i>; <i>ācer</i> → <i>ācerrimus</i>; <i>celer</i> (rápido) → <i>celerrimus</i>. O comparativo deles é regular, tirado do genitivo: <i>pulchrior</i>, <i>līberior</i>, <i>miserior</i>, <i>ācrior</i>, <i>celerior</i>. Note a diferença em <i>pulcher</i> e <i>ācer</i>: o comparativo perde o <i>e</i> (<i>pulchr-ior</i>, <i>ācr-ior</i>), o superlativo o conserva (<i>pulcher-rimus</i>, <i>ācer-rimus</i>).</p>
<h3>Seis adjetivos em -lis: -illimus</h3>
<p>Seis adjetivos em <i>-lis</i> fazem o superlativo em <b><i>-limus</i></b> junto ao tema, o que dá <i>-illimus</i>: <i>facilis</i> (fácil) → <i>facillimus</i>; <i>difficilis</i> (difícil) → <i>difficillimus</i>; <i>similis</i> (semelhante) → <i>simillimus</i>; <i>dissimilis</i> (diferente) → <i>dissimillimus</i>; <i>humilis</i> (baixo, humilde) → <i>humillimus</i>; <i>gracilis</i> (delgado) → <i>gracillimus</i>. O comparativo é regular (<i>facilior</i>, <i>similior</i>). A lista de seis é a de Allen e Greenough (§ 126), Kennedy (§ 78) e Ravizza (n. 56); Bennett (§ 71.4) dá cinco, sem <i>gracilis</i>. Os outros adjetivos em <i>-ilis</i> seguem a regra geral: <i>nōbilis</i> (nobre) → <i>nōbilissimus</i>.</p>
{tabela(['Positivo', 'Comparativo', 'Superlativo', 'Herança em português'], [
    ['longus, -a, -um', 'longior, -ius', 'long<b>issimus</b>, -a, -um', 'longuíssimo'],
    ['fortis, -e', 'fortior, -ius', 'fort<b>issimus</b>', 'fortíssimo'],
    ['fēlīx, gen. fēlīcis', 'fēlīcior, -ius', 'fēlīc<b>issimus</b>', 'felicíssimo'],
    ['pulcher, -chra, -chrum', 'pulchrior, -ius', 'pulcher<b>rimus</b>', 'pulquérrimo'],
    ['miser, -era, -erum', 'miserior, -ius', 'miser<b>rimus</b>', 'misérrimo'],
    ['ācer, ācris, ācre', 'ācrior, -ius', 'ācer<b>rimus</b>', 'acérrimo'],
    ['facilis, -e', 'facilior, -ius', 'facil<b>limus</b>', 'facílimo'],
    ['difficilis, -e', 'difficilior, -ius', 'difficil<b>limus</b>', 'dificílimo'],
    ['similis, -e', 'similior, -ius', 'simil<b>limus</b>', 'simílimo'],
    ['humilis, -e', 'humilior, -ius', 'humil<b>limus</b>', 'humílimo'],
], 'Os três tipos de superlativo', latim_cols=(0, 1, 2))}
<p>A última coluna mostra que o português culto herdou esses superlativos quase intactos: "facílimo", "dificílimo", "misérrimo", "acérrimo", "pulquérrimo". Quem conhece essas formas portuguesas já tem a regra latina na memória.</p>
<h3>Magis e maximē</h3>
<p>Alguns adjetivos não têm comparativo e superlativo por sufixo e usam os advérbios <b><i>magis</i></b> ("mais") e <b><i>maximē</i></b> ("ao máximo"), como o português "mais" e "muitíssimo". São sobretudo os adjetivos em <i>-us</i> precedido de vogal (<i>-eus</i>, <i>-ius</i>, <i>-uus</i>): <i>idōneus</i> (apto) → <i>magis idōneus</i>, <i>maximē idōneus</i>; <i>dubius</i> (duvidoso) → <i>magis dubius</i>. A razão é a pronúncia: *<i>idōneior</i> juntaria vogais demais. Os adjetivos em <i>-quus</i> não entram aqui, porque o <i>u</i> deles é consonantal (<i>antīquus</i>, antigo → <i>antīquior</i>, <i>antīquissimus</i>).</p>
<h3>O que o superlativo significa</h3>
<p>O superlativo latino serve a dois usos que o português distingue. Com um termo de comparação, é o <b>superlativo relativo</b>: <i>mōns altissimus Graeciae</i>, "o monte mais alto da Grécia". Sem termo de comparação, é quase sempre o <b>superlativo absoluto</b>: <i>mōns altissimus</i>, "um monte altíssimo, muito alto". Bennett (§ 240.2) dá o exemplo <i>vir fortissimus</i>, "um homem muito valente", e é essa a leitura mais comum na prosa; a frase de Lucas 2,14 que você analisou no capítulo 9 (<i>Glōria in altissimīs Deō</i>) tem um superlativo sem termo de comparação, "nos lugares altíssimos". Para dizer "o mais … de todos", o latim usa o genitivo (<i>fortissimus omnium</i>, "o mais valente de todos") ou <i>ex</i>, <i>dē</i> com ablativo (<i>fortissimus ex omnibus</i>); o genitivo que indica o todo do qual se toma uma parte é estudado no capítulo 20.</p>
{dica('<b>Quam + superlativo.</b> Diante de um superlativo, <i>quam</i> não significa "do que", e sim "o mais … possível": <i>quam celerrimus</i>, "o mais rápido possível"; <i>quam plūrimī</i>, "o maior número possível" (Bennett § 240.3; Allen e Greenough § 291.c). <i>Vel</i> reforça o superlativo: <i>vel maximus</i>, "até o maior, o maior de todos".')}
'''),
        ('A comparação irregular', f'''
<p>Os adjetivos mais usados da língua são justamente os que fogem à regra: o comparativo e o superlativo de "bom", "mau", "grande", "pequeno" e "muito" vêm de outras raízes, como em português ("bom, melhor, ótimo"). Esses têm de ser decorados, e o português ajuda muito, porque conservou quase todos.</p>
{tabela(['Positivo', 'Comparativo m./f. · n.', 'Superlativo', 'Em português'], [
    ['bonus, -a, -um, bom', '<b>melior</b> · <b>melius</b>', '<b>optimus</b>, -a, -um', 'melhor · ótimo'],
    ['malus, -a, -um, mau', '<b>peior</b> · <b>peius</b>', '<b>pessimus</b>', 'pior · péssimo'],
    ['magnus, -a, -um, grande', '<b>maior</b> · <b>maius</b>', '<b>maximus</b>', 'maior · máximo'],
    ['parvus, -a, -um, pequeno', '<b>minor</b> · <b>minus</b>', '<b>minimus</b>', 'menor · mínimo'],
    ['multus, -a, -um, muito', '— · <b>plūs</b> (só neutro)', '<b>plūrimus</b>', '— (o português diz "mais")'],
    ['multī, -ae, -a, muitos', '<b>plūrēs</b> · <b>plūra</b>', '<b>plūrimī</b>, -ae, -a', '"plural" e "pluralidade" vêm desta raiz'],
], 'Comparação irregular', latim_cols=(0, 1, 2))}
<p><i>Melior, peior, maior, minor</i> se declinam exatamente como <i>longior</i>: <i>meliōris, meliōrī, meliōrem, meliōre</i>; <i>maiōrēs, maiōrum</i>. Em <i>peior</i> e <i>maior</i>, o <i>i</i> entre vogais soa como consoante e se pronuncia dobrado (<i>pei-ior</i>, <i>mai-ior</i>), de modo que a primeira sílaba é longa (Allen e Greenough § 11.d e nota). O plural <i>maiōrēs</i> tem ainda um sentido especial: "os antepassados", os que nasceram antes (<i>mōs maiōrum</i>, "o costume dos antepassados").</p>
<p><i>Plūs</i> é o único comparativo com declinação própria. No singular, só existe o neutro, usado como substantivo ("mais, uma quantidade maior"), e a coisa medida vem no genitivo: <i>plūs pecūniae</i>, "mais dinheiro" (literalmente "mais de dinheiro"). No plural, <i>plūrēs, plūra</i> é um adjetivo comum, "mais numerosos, vários": <i>plūrēs librī</i>, "mais livros".</p>
{tabela_declinacao('plūs, "mais" (Bennett § 70)', [
    ('—', 'plūs', 'plūr<b>ēs</b>', 'plūr<b>a</b>'), ('—', 'plūr<b>is</b>', 'plūr<b>ium</b>', 'plūr<b>ium</b>'),
    ('—', '—', 'plūr<b>ibus</b>', 'plūr<b>ibus</b>'), ('—', 'plūs', 'plūr<b>ēs</b>', 'plūr<b>a</b>'),
    ('—', '—', 'plūr<b>ēs</b>', 'plūr<b>a</b>'), ('—', 'plūr<b>e</b>', 'plūr<b>ibus</b>', 'plūr<b>ibus</b>')],
    colunas=('m./f. · sing.', 'neutro · sing.', 'm./f. · pl.', 'neutro · pl.'))}
<p>Note o genitivo plural <i>plūrium</i>, com <i>-ium</i>: é a exceção dentro dos comparativos.</p>
<h3>Comparativos e superlativos sem positivo</h3>
<p>Um grupo de comparativos indica posição no espaço ou no tempo e vem de advérbios e preposições, não de um adjetivo de uso corrente. Você não precisa decorá-los agora, mas vai reconhecê-los com facilidade, porque o português os herdou como palavras comuns:</p>
{tabela(['Origem', 'Comparativo', 'Superlativo', 'Em português'], [
    ['<i>prae, prō</i>, diante', 'prior, prius, anterior, primeiro (de dois)', 'prīmus, primeiro', 'prior · primeiro'],
    ['<i>suprā</i>, acima (<i>superus</i>)', 'superior, mais alto', 'summus <i>ou</i> suprēmus, o mais alto; último', 'superior · sumo, supremo'],
    ['<i>īnfrā</i>, abaixo (<i>īnferus</i>)', 'īnferior, mais baixo', 'īnfimus <i>ou</i> īmus, o mais baixo', 'inferior · ínfimo'],
    ['<i>prope</i>, perto', 'propior, mais próximo', 'proximus, o mais próximo, vizinho', 'próximo'],
    ['<i>ultrā</i>, além', 'ulterior, mais distante', 'ultimus, o mais distante, último', 'ulterior · último'],
    ['<i>intrā</i>, dentro', 'interior, interior', 'intimus, o mais íntimo', 'interior · íntimo'],
    ['<i>extrā</i>, fora (<i>exterus</i>)', 'exterior, exterior', 'extrēmus, o mais externo, extremo', 'exterior · extremo'],
    ['<i>post</i>, depois (<i>posterus</i>)', 'posterior, posterior', 'postrēmus, o último', 'posterior · postremo'],
], 'Comparativos sem positivo de uso corrente (Bennett § 73; Allen e Greenough § 130)', latim_cols=(1, 2))}
<p>Alguns desses superlativos indicam a <b>parte</b> de uma coisa, e não qual coisa: <i>summus mōns</i> é "o alto do monte", e não "o monte mais alto"; <i>extrēma via</i>, "o fim do caminho" (Allen e Greenough § 293). Quando a tradução literal não fizer sentido, experimente essa leitura.</p>
'''),
        ('"Do que": quam e o ablativo de comparação', f'''
<p>O comparativo pede, quase sempre, um segundo termo: mais alto <b>do que</b> quê? O latim tem duas construções para isso, e o leitor precisa reconhecer as duas.</p>
<h3>1. Quam + o mesmo caso</h3>
<p>A conjunção <b><i>quam</i></b> ("do que") liga os dois termos, e o segundo termo fica <b>no mesmo caso que o primeiro</b>, porque os dois exercem, cada um na sua oração, a mesma função. Em <i>Sōl maior est quam terra</i> ("o sol é maior do que a terra"), <i>terra</i> está no nominativo porque é, por assim dizer, o sujeito de um segundo "é" subentendido: "o sol é maior do que a terra [é]".</p>
<h3>2. O ablativo de comparação</h3>
<p>Em vez de <i>quam</i>, o segundo termo pode ir para o <b>ablativo</b>, sem preposição: <i>Sōl terrā maior est</i>, com o mesmo sentido. A explicação tradicional (Allen e Greenough § 406, nota de rodapé) é que esse ablativo é um caso de "ponto de partida": a comparação parte da terra e vai além dela. Por isso se traduz por "do que": <i>terrā</i> = "do que a terra".</p>
{exemplos([('Sōl maior est <b>quam terra</b>.', 'O sol é maior do que a terra. (<i>terra</i>, nominativo, como <i>sōl</i>)'),
           ('Sōl <b>terrā</b> maior est.', 'O sol é maior do que a terra. (<i>terrā</i>, ablativo de comparação)'),
           ('Lūna minor est <b>quam terra</b> · Lūna <b>terrā</b> minor est.', 'A lua é menor do que a terra.'),
           ('Nautae nāvem longiōrem <b>quam scapham</b> habent.', 'Os marinheiros têm um navio mais longo do que um bote. (<i>scapham</i>, acusativo, como <i>nāvem</i>; <i>nāvis</i>, navio; <i>scapha, -ae</i>, bote)')])}
<p>As duas construções não são livres em todos os casos. Bennett (§ 217.2) e Allen e Greenough (§ 407.a) dão a regra prática: o ablativo de comparação, na prosa, só substitui <i>quam</i> quando o primeiro termo está no <b>nominativo ou no acusativo</b>. Se o primeiro termo está em outro caso, <i>quam</i> é obrigatório, porque um ablativo ao lado de um dativo ou de um genitivo tornaria a frase ambígua.</p>
{exemplos([('Agricolae magis crēdō <b>quam nautae</b>.', 'Confio mais no agricultor do que no marinheiro. (<i>crēdō</i> + dativo, "confio em"; <i>agricolae</i> e <i>nautae</i> são dativos, e só <i>quam</i> é possível)'),
           ('Mārcus tē magis amat <b>quam Paulum</b>.', 'Marcos ama você mais do que [ama] Paulo. (<i>Paulum</i>, acusativo, como <i>tē</i>)'),
           ('Mārcus tē magis amat <b>quam Paulus</b>.', 'Marcos ama você mais do que Paulo [ama]. (<i>Paulus</i>, nominativo, como <i>Mārcus</i>)')])}
<p>Os dois últimos exemplos mostram por que <i>quam</i> é às vezes indispensável: <i>Mārcus tē magis amat Paulō</i> não deixaria claro se Paulo é quem ama ou quem é amado. O caso depois de <i>quam</i> resolve. Com advérbios no comparativo (seção 5), a prosa também prefere <i>quam</i> (Allen e Greenough § 407.e).</p>
<h3>Quanto mais? Multō, paulō</h3>
<p>Para dizer <b>por quanto</b> uma coisa supera a outra, o latim usa outro ablativo, o de <b>grau de diferença</b>: <i>multō</i> ("muito", literalmente "por muito") e <i>paulō</i> ("um pouco, por pouco"), além de números. <i>Sōl multō maior est quam terra</i>, "o sol é muito maior do que a terra"; <i>paulō altior</i>, "um pouco mais alto" (Bennett § 223; Allen e Greenough § 414). Repare: diante de um comparativo, "muito" se diz <i>multō</i>, e não <i>valdē</i> ou <i>multum</i>; Ravizza (n. 59.c) dá o exemplo <i>multō doctior</i>, "muito mais sábio".</p>
{observacao('Duas qualidades da mesma coisa', 'Quando se comparam duas qualidades do mesmo objeto, os dois adjetivos vão para o comparativo: <i>via longior quam lātior</i>, "um caminho mais longo do que largo" (Bennett § 240.4; Allen e Greenough § 292). Também se pode dizer com dois positivos e <i>magis</i>: <i>via magis longa quam lāta</i>. Misturar os dois tipos (um comparativo e um positivo ligados por <i>quam</i>) também ocorre, mas é raro e menos elegante (Allen e Greenough § 292.a, nota); não o imite.')}
'''),
        ('Os advérbios e a sua comparação', f'''
<p>A maioria dos advérbios de modo latinos ("bem", "corajosamente", "depressa") deriva de adjetivos, como os advérbios portugueses em "-mente". A formação depende da classe do adjetivo.</p>
<p><b>Adjetivos de primeira classe</b> (<i>bonus, -a, -um</i>): troque o <i>-ī</i> do genitivo por <b><i>-ē</i></b>. <i>Lātus</i> (largo) → <i>lātē</i>, "largamente"; <i>longus</i> → <i>longē</i>, "longe, de longe"; <i>cārus</i> → <i>cārē</i>, "caro"; <i>pulcher, pulchrī</i> → <i>pulchrē</i>, "belamente"; <i>līber, līberī</i> → <i>līberē</i>, "livremente"; <i>miser, miserī</i> → <i>miserē</i>, "miseravelmente"; <i>amārus</i> (amargo) → <i>amārē</i>, "amargamente". Allen e Greenough (§ 214.a) explicam o <i>-ē</i> como resto de um antigo ablativo.</p>
<p><b>Adjetivos de segunda classe</b> (<i>fortis, forte</i>): troque o <i>-is</i> do genitivo por <b><i>-iter</i></b>. <i>Fortis</i> → <i>fortiter</i>, "corajosamente"; <i>ācer, ācris</i> → <i>ācriter</i>, "energicamente"; <i>celer, celeris</i> → <i>celeriter</i>, "rapidamente"; <i>brevis</i> → <i>breviter</i>, "brevemente"; <i>fēlīx, fēlīcis</i> → <i>fēlīciter</i>, "felizmente". Os adjetivos em <i>-ns</i> acrescentam só <b><i>-er</i></b> ao tema: <i>prūdēns, prūdentis</i> → <i>prūdenter</i>; <i>sapiēns</i> (sábio) → <i>sapienter</i>. Note também <i>audāx, audācis</i> (ousado) → <i>audācter</i> (Bennett § 76.1).</p>
<p>Há ainda advérbios que são formas de caso fossilizadas. O <b>acusativo neutro</b> de alguns adjetivos serve de advérbio: <i>facile</i>, "facilmente"; <i>multum</i>, "muito"; <i>paulum</i>, "um pouco"; <i>prīmum</i>, "em primeiro lugar". O <b>ablativo em <i>-ō</i></b> forma outros: <i>subitō</i>, "de repente"; <i>rārō</i>, "raramente"; <i>crēbrō</i>, "frequentemente" (Bennett § 77.2–3). E os dois advérbios mais frequentes de todos são irregulares e têm <i>e</i> breve: <i>bene</i>, "bem", de <i>bonus</i>, e <i>male</i>, "mal", de <i>malus</i>.</p>
<h3>Comparativo e superlativo dos advérbios</h3>
<p>A regra é simples e se apoia no que você acabou de aprender. O <b>comparativo do advérbio</b> é o <b>acusativo neutro singular</b> do comparativo do adjetivo, em <i>-ius</i>: <i>longius</i>, "mais longe"; <i>fortius</i>, "mais corajosamente". O <b>superlativo do advérbio</b> troca o <i>-us</i> do superlativo do adjetivo por <b><i>-ē</i></b>: <i>longissimē</i>, "muito longe, o mais longe"; <i>fortissimē</i>; <i>pulcherrimē</i>; <i>facillimē</i> (Bennett § 76.2; Allen e Greenough § 218).</p>
{tabela(['Adjetivo', 'Advérbio', 'Comparativo', 'Superlativo'], [
    ['lātus, largo', 'lāt<b>ē</b>', 'lāt<b>ius</b>', 'lātissim<b>ē</b>'],
    ['pulcher, belo', 'pulchr<b>ē</b>', 'pulchr<b>ius</b>', 'pulcherrim<b>ē</b>'],
    ['fortis, valente', 'fort<b>iter</b>', 'fort<b>ius</b>', 'fortissim<b>ē</b>'],
    ['celer, rápido', 'celer<b>iter</b>', 'celer<b>ius</b>', 'celerrim<b>ē</b>'],
    ['prūdēns, prudente', 'prūdent<b>er</b>', 'prūdent<b>ius</b>', 'prūdentissim<b>ē</b>'],
    ['facilis, fácil', 'facil<b>e</b>', 'facil<b>ius</b>', 'facillim<b>ē</b>'],
    ['bonus, bom', '<b>bene</b>, bem', '<b>melius</b>', '<b>optimē</b>'],
    ['malus, mau', '<b>male</b>, mal', '<b>peius</b>', '<b>pessimē</b>'],
    ['magnus, grande', '<b>magnopere</b>, grandemente', '<b>magis</b>', '<b>maximē</b>'],
    ['multus, muito', '<b>multum</b>, muito', '<b>plūs</b>', '<b>plūrimum</b>'],
    ['parvus, pequeno', '<b>parum</b>, pouco', '<b>minus</b>', '<b>minimē</b>'],
    ['—', '<b>diū</b>, por muito tempo', '<b>diūtius</b>', '<b>diūtissimē</b>'],
    ['—', '<b>saepe</b>, muitas vezes', '<b>saepius</b>', '<b>saepissimē</b>'],
], 'Advérbios e seus graus (Bennett §§ 76–77; Allen e Greenough § 218)', latim_cols=(1, 2, 3))}
<p>Uma consequência para a leitura: formas como <i>longius</i>, <i>melius</i>, <i>fortius</i> podem ser o <b>adjetivo</b> neutro (<i>iter longius</i>, "um caminho mais longo") ou o <b>advérbio</b> (<i>longius ambulat</i>, "caminha mais longe"). A diferença está na função: se a forma concorda com um nome neutro, é adjetivo; se modifica um verbo, é advérbio. E <i>minimē</i>, que é o superlativo de <i>parum</i>, serve também, na conversa, de "de modo algum, não".</p>
{exemplos([('Mīlitēs fort<b>iter</b> pugnant.', 'Os soldados combatem corajosamente. (<i>pugnant</i>, combatem)'),
           ('Puella celer<b>ius</b> currit quam frāter.', 'A menina corre mais depressa do que o irmão. (<i>currit</i>, corre; com advérbio, <i>quam</i>)'),
           ('Poēta pulcherrim<b>ē</b> cantat.', 'O poeta canta lindamente, muitíssimo bem.'),
           ('Magister <b>bene</b> docet, sed discipulī <b>male</b> audiunt.', 'O mestre ensina bem, mas os alunos ouvem mal.')])}
'''),
        ('Análise gramatical: textos autênticos', f'''
<p>Horácio, na primeira das suas <i>Epístolas</i>, resume numa linha a escala de valores que ele critica. O verso tem dois ablativos de comparação e um verbo subentendido:</p>
{exemplos([('Vīlius argentum est aurō, virtūtibus aurum.', 'A prata vale menos do que o ouro; o ouro, menos do que as virtudes. (Horácio, <i>Ep.</i> 1.1.52)')])}
<p>O adjetivo <i>vīlis, vīle</i> (de segunda classe, como <i>fortis</i>) significa "barato, de pouco valor"; o comparativo <i>vīlior, vīlius</i> é "mais barato, de menos valor". A segunda metade do verso não repete <i>vīlius est</i>: o leitor o tira da primeira metade.</p>
{analise('Horácio, Ep. 1.1.52, palavra a palavra', [
    ('Vīlius', 'vīlis, vīle, barato, de pouco valor', 'comparativo, nominativo singular neutro (<i>vīlior, vīlius</i>)', 'predicativo: concorda com <i>argentum</i> (neutro)'),
    ('argentum', 'argentum, -ī (n.), prata', 'nominativo singular, 2ª declinação', 'sujeito da primeira oração'),
    ('est', 'sum, esse, ser', '3ª pessoa do singular, presente', 'verbo de ligação'),
    ('aurō', 'aurum, -ī (n.), ouro', 'ablativo singular', 'ablativo de comparação: "do que o ouro"'),
    ('virtūtibus', 'virtūs, virtūtis (f.), virtude', 'ablativo plural, 3ª declinação', 'ablativo de comparação da segunda oração: "do que as virtudes"'),
    ('aurum', 'aurum, -ī (n.), ouro', 'nominativo singular', 'sujeito da segunda oração (<i>vīlius est</i> subentendido)'),
])}
{diagrama_frase([('Vīlius', 'comparativo · nom. sing. neutro'), ('argentum', 'sujeito · nom. sing. neutro'), ('est', 'verbo · "é"'), ('aurō', 'ablativo · de comparação')],
    'Lendo em ordem: <i>Vīlius argentum est aurō</i> = "Mais barata é a prata do que o ouro". O ablativo sem preposição, depois de um comparativo, se lê "do que".')}
<p>Três coisas deste capítulo estão no verso. <i>Vīlius</i> não é um nominativo masculino da segunda declinação: é o neutro do comparativo, e concorda com <i>argentum</i>, neutro. <i>Aurō</i> e <i>virtūtibus</i> são ablativos sem preposição, e o que permite lê-los como "do que" é o comparativo ao lado. E o ablativo é permitido porque o primeiro termo de cada comparação (<i>argentum</i>, <i>aurum</i>) está no nominativo; em prosa, também se poderia dizer <i>vīlius argentum est quam aurum</i>.</p>
<p>O Evangelho de Mateus, na Vulgata, tem a mesma construção, agora com um comparativo irregular e um sujeito de segunda pessoa. Jesus diz aos discípulos que não tenham medo (<i>Nōlīte ergō timēre</i>, um imperativo negativo, assunto do capítulo 22) e acrescenta:</p>
{exemplos([('Multīs passeribus meliōrēs estis vōs.', 'Vós valeis mais do que muitos pardais. (Mt 10,31; <i>passer, passeris</i>, m., pardal: <i>multīs passeribus</i>, ablativo de comparação; <i>meliōrēs</i>, nominativo plural de <i>melior</i>, predicativo de <i>vōs</i>)'),
           ('Hōc est maximum, et prīmum mandātum.', 'Este é o maior e o primeiro mandamento. (Mt 22,38; <i>maximum</i>, superlativo irregular de <i>magnus</i>; <i>prīmum</i>, superlativo sem positivo, ligado a <i>prae</i>)'),
           ('Et ēgressus forās, flēvit amārē.', 'E, saindo para fora, chorou amargamente. (Mt 26,75; <i>amārē</i>, advérbio de <i>amārus</i>, amargo, em <i>-ē</i>; <i>flēvit</i>, chorou, perfeito de <i>fleō</i>)')])}
<p>César, ao descrever os povos da Gália no início da <i>Guerra da Gália</i>, usa um superlativo relativo com genitivo e, logo em seguida, superlativos de advérbios:</p>
{exemplos([('Hōrum omnium fortissimī sunt Belgae.', 'De todos estes, os mais valentes são os belgas. (César, <i>BG</i> 1.1.3; <i>hōrum omnium</i>, genitivo plural, "de todos estes": o todo do qual se tira a parte)'),
           ('… ā cultū atque hūmānitāte prōvinciae longissimē absunt …', '… estão muito longe da civilização e da cultura da província … (a mesma frase; <i>longissimē</i>, superlativo do advérbio <i>longē</i>; <i>absunt</i>, estão distantes)')])}
<p><i>Fortissimī</i> aqui é relativo ("os mais valentes"), porque há um termo de comparação (<i>hōrum omnium</i>); <i>longissimē</i>, sem termo de comparação, se traduz melhor como absoluto ("muitíssimo longe").</p>
<h3>Resumo</h3>
<ul>
<li>Comparativo: genitivo sem a terminação + <i>-ior</i> (m./f.), <i>-ius</i> (n.); declina-se como tema consonantal: <i>-ōris, -ōrī, -ōrem, -ōre</i>; <i>-ōrēs, -ōrum, -ōribus</i>; neutro plural <i>-ōra</i>.</li>
<li>Superlativo: <i>-issimus</i>; adjetivos em <i>-er</i>: <i>-errimus</i> (<i>pulcherrimus</i>); seis em <i>-lis</i>: <i>-illimus</i> (<i>facillimus</i>); declina-se como <i>bonus</i>. Em <i>-eus, -ius</i>: <i>magis, maximē</i>.</li>
<li>Irregulares: <i>melior, optimus; peior, pessimus; maior, maximus; minor, minimus; plūs, plūrimus</i>.</li>
<li>"Do que": <i>quam</i> + o mesmo caso; ou ablativo de comparação, só se o primeiro termo estiver no nominativo ou no acusativo. "Muito mais": <i>multō</i> + comparativo.</li>
<li>Superlativo relativo ("o mais") com genitivo ou <i>ex</i> + ablativo; absoluto ("muito", "-íssimo") sem termo de comparação; <i>quam</i> + superlativo = "o mais … possível".</li>
<li>Advérbios: <i>-ē</i> (1ª classe), <i>-iter</i> ou <i>-ter</i> (2ª classe); comparativo em <i>-ius</i>, superlativo em <i>-issimē</i>; <i>bene, melius, optimē</i>; <i>male, peius, pessimē</i>.</li>
</ul>
<p>No próximo capítulo, outro grupo de adjetivos com regras próprias, os numerais, e as expressões de tempo e de lugar, onde os ordinais (<i>prīmus, secundus</i>) e o ablativo voltam a aparecer.</p>
'''),
    ],
    erros_comuns=[
        ('Declinar o comparativo como <i>fortis</i>: *<i>longiōrī</i> no ablativo, *<i>meliōrium</i>, *<i>maiōria</i>.', 'O comparativo é tema consonantal: ablativo <i>longiōre</i>, genitivo plural <i>meliōrum</i>, neutro plural <i>maiōra</i>. Pense em <i>rēx</i> e <i>corpus</i> (capítulo 9), não em <i>fortis</i> (capítulo 10). A única exceção de uso corrente é <i>plūrium</i>.'),
        ('Ler <i>longius</i>, <i>melius</i>, <i>maius</i> como masculinos da segunda declinação: *<i>vir melius</i>.', 'O <i>-ius</i> do comparativo é neutro (nominativo e acusativo singular) ou advérbio. O masculino é <i>melior</i>: <i>vir melior</i>, "um homem melhor"; <i>bellum maius</i>, "uma guerra maior"; <i>melius cantat</i>, "canta melhor".'),
        ('Usar o ablativo de comparação com qualquer caso: *<i>Agricolae magis crēdō nautā</i>.', 'Na prosa, o ablativo só substitui <i>quam</i> quando o primeiro termo está no nominativo ou no acusativo. Aqui o primeiro termo (<i>agricolae</i>) é dativo: diga <i>quam nautae</i>, no mesmo caso.'),
        ('Pôr o segundo termo no caso errado depois de <i>quam</i>: *<i>Mārcus altior est quam Paulum</i>.', 'Depois de <i>quam</i>, o segundo termo fica no caso do primeiro, porque tem a mesma função: <i>Mārcus altior est quam Paulus</i> (os dois nominativos). Se puser o acusativo, a frase muda de sentido ou fica errada.'),
        ('Traduzir todo superlativo por "o mais": <i>vir fortissimus</i> = "o homem mais valente".', 'Sem termo de comparação, o superlativo latino é em geral absoluto: "um homem muito valente, valentíssimo". "O mais … " exige um termo de comparação (um genitivo como <i>omnium</i>, ou <i>ex</i> + ablativo) ou um contexto que o imponha.'),
        ('Formar advérbios de adjetivos de segunda classe com <i>-ē</i>: *<i>fortē</i>, *<i>celerē</i>; ou de <i>bonus</i>: *<i>bonē</i>.', 'Adjetivos de segunda classe fazem <i>-iter</i> (<i>fortiter, celeriter</i>) ou <i>-ter</i> (<i>prūdenter</i>). <i>Forte</i> existe, mas é o neutro do adjetivo ou o advérbio "por acaso". De <i>bonus</i> e <i>malus</i>, os advérbios são <i>bene</i> e <i>male</i>, com <i>e</i> breve.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Um ablativo que significa "do que"',
            'Analise e traduza: <i lang="la">Sōl terrā multō maior est, lūna terrā minor.</i> Vocabulário: <i>sōl, sōlis</i> (m.), sol; <i>terra, -ae</i>, terra; <i>lūna, -ae</i>, lua.', [
            ('Onde estão os verbos, e quantas orações há?', 'Há um só verbo, <i>est</i>, mas duas orações paralelas, separadas pela vírgula. Na segunda, o leitor subentende <i>est</i>, como no verso de Horácio.'),
            ('Que forma é <i>maior</i>, e com que concorda?', 'Comparativo irregular de <i>magnus</i>, nominativo singular masculino ou feminino. Concorda com <i>sōl</i> (m.), sujeito: "o sol é maior".'),
            ('<i>Terrā</i> é lugar onde, "na terra"?', 'Não: não há preposição <i>in</i>, e há um comparativo ao lado. É ablativo de comparação: "do que a terra". O primeiro termo (<i>sōl</i>) está no nominativo, por isso o ablativo é permitido.'),
            ('E <i>multō</i>?', 'Ablativo de grau de diferença: diz por quanto o sol supera a terra. Diante de comparativo, <i>multō</i> = "muito": "muito maior".'),
            ('Analise a segunda oração.', '<i>Lūna</i>, nominativo, sujeito; <i>terrā</i>, de novo ablativo de comparação; <i>minor</i>, comparativo de <i>parvus</i>, nominativo feminino, concordando com <i>lūna</i>; <i>est</i> subentendido.'),
            ('Monte a tradução e reescreva com <i>quam</i>.', '"O sol é muito maior do que a terra; a lua, menor do que a terra." Com <i>quam</i>: <i>Sōl multō maior est quam terra, lūna minor quam terra.</i> O segundo termo fica no nominativo, como o primeiro.'),
        ]),
        pratica_guiada('Prática guiada 2 · Advérbio, comparativo e quam',
            'Traduza e explique cada grau: <i lang="la">Mārcus fortiter pugnat, sed Paulus fortius, et rēx ipse fortissimē.</i> Vocabulário: <i>pugnō, -āre</i>, combater; <i>ipse</i>, ele próprio (capítulo 15).', [
            ('Que palavra é <i>fortiter</i>, e de onde vem?', 'Advérbio de modo, formado de <i>fortis</i> (segunda classe) com <i>-iter</i>: "corajosamente". Modifica <i>pugnat</i>.'),
            ('<i>Fortius</i> é adjetivo ou advérbio?', 'Advérbio: não há nome neutro com que concorde, e o sentido pede "combate" subentendido (<i>Paulus fortius [pugnat]</i>). É o comparativo do advérbio, igual ao neutro do adjetivo: "mais corajosamente".'),
            ('E <i>fortissimē</i>?', 'Superlativo do advérbio, de <i>fortissimus</i> com <i>-ē</i>. Sem termo de comparação expresso, mas depois de uma gradação, pode ser lido como "o mais corajosamente de todos" ou "corajosíssimamente".'),
            ('Monte a tradução.', '"Marcos combate corajosamente, mas Paulo, com mais coragem, e o próprio rei, com a maior coragem de todos." A gradação justifica a leitura relativa do superlativo.'),
            ('Como diria "Paulo combate mais corajosamente do que Marcos"?', '<i>Paulus fortius pugnat quam Mārcus.</i> Com advérbios no comparativo, a prosa usa <i>quam</i>; <i>Mārcus</i> fica no nominativo, como <i>Paulus</i>.'),
        ], 'Conclusão: o mesmo tema (<i>fort-</i>) dá o adjetivo nos três graus (<i>fortis, fortior, fortissimus</i>) e o advérbio nos três graus (<i>fortiter, fortius, fortissimē</i>).'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Forme os graus', 'Dê o comparativo (m./f. e n.) e o superlativo (m.) e diga qual regra usou.', [
            ('<i>clārus, -a, -um</i>, famoso', '<i>clārior, clārius</i>; <i>clārissimus</i>. Regra geral: tema <i>clār-</i> + <i>-ior/-ius</i>, <i>-issimus</i>.'),
            ('<i>brevis, -e</i>, breve', '<i>brevior, brevius</i>; <i>brevissimus</i>. Regra geral, do genitivo <i>brevis</i>.'),
            ('<i>fēlīx</i>, gen. <i>fēlīcis</i>, feliz', '<i>fēlīcior, fēlīcius</i>; <i>fēlīcissimus</i>. O tema <i>fēlīc-</i> só aparece no genitivo.'),
            ('<i>pulcher, -chra, -chrum</i>, belo', '<i>pulchrior, pulchrius</i>; <i>pulcherrimus</i>. Adjetivo em <i>-er</i>: o superlativo se faz sobre o nominativo, com <i>-rimus</i>.'),
            ('<i>ācer, ācris, ācre</i>, enérgico', '<i>ācrior, ācrius</i>; <i>ācerrimus</i>. Também em <i>-er</i>: o comparativo perde o <i>e</i>, o superlativo o mantém.'),
            ('<i>similis, -e</i>, semelhante', '<i>similior, similius</i>; <i>simillimus</i>. Um dos seis adjetivos em <i>-lis</i> com <i>-illimus</i>.'),
            ('<i>nōbilis, -e</i>, nobre', '<i>nōbilior, nōbilius</i>; <i>nōbilissimus</i>. Não está entre os seis: segue a regra geral.'),
            ('<i>idōneus, -a, -um</i>, apto', '<i>magis idōneus</i>; <i>maximē idōneus</i>. Adjetivo em <i>-eus</i>: comparação com advérbios.'),
        ]),
        exercicio('Exercício 2 · Reconheça as formas irregulares', 'Diga o positivo, o grau, e o caso e o número possíveis (ou "advérbio").', [
            ('<i>meliōrem</i>', 'De <i>bonus</i>: comparativo, acusativo singular masculino ou feminino, "melhor".'),
            ('<i>pessimī</i>', 'De <i>malus</i>: superlativo, genitivo singular masculino ou neutro, ou nominativo plural masculino.'),
            ('<i>maiōra</i>', 'De <i>magnus</i>: comparativo, nominativo ou acusativo plural neutro. Não é feminino: o <i>-a</i> é do neutro plural dos temas consonantais.'),
            ('<i>minimē</i>', 'Advérbio, superlativo de <i>parum</i>: "muitíssimo pouco", "de modo algum".'),
            ('<i>plūrēs</i>', 'De <i>multī</i>: comparativo, nominativo ou acusativo plural masculino ou feminino, "mais numerosos, vários".'),
            ('<i>optimē</i>', 'Advérbio, superlativo de <i>bene</i> (de <i>bonus</i>): "muito bem, otimamente".'),
            ('<i>peius</i>', 'De <i>malus</i>: comparativo neutro (nominativo ou acusativo singular), "pior"; ou advérbio comparativo de <i>male</i>, "pior".'),
            ('<i>summō</i>', 'Superlativo sem positivo corrente (<i>superior, summus</i>): dativo ou ablativo singular masculino ou neutro, "o mais alto" ou "o alto de".'),
        ]),
        exercicio('Exercício 3 · Faça concordar o comparativo', 'Escreva o adjetivo entre parênteses no comparativo, concordando com o nome, e explique.', [
            ('<i>in viā ___</i> (longus)', '<i>longiōre</i>: ablativo singular feminino, com <i>-e</i>, não *<i>longiōrī</i>.'),
            ('<i>rēgum ___</i> (fortis)', '<i>fortiōrum</i>: genitivo plural masculino, com <i>-um</i>; o positivo faria <i>fortium</i>.'),
            ('<i>carmina ___</i> (pulcher), como objeto', '<i>pulchriōra</i>: acusativo plural neutro, com <i>-a</i>.'),
            ('<i>iter ___</i> (brevis), como sujeito', '<i>brevius</i>: nominativo singular neutro. <i>Iter, itineris</i> (caminho) é neutro, por isso não *<i>brevior</i>.'),
            ('<i>puellae ___</i> (bonus), dativo singular', '<i>meliōrī</i>: dativo singular feminino de <i>melior</i>.'),
            ('<i>mīlitēs ___</i> (multī), como sujeito', '<i>plūrēs</i>: nominativo plural masculino, "mais soldados, vários soldados".'),
        ]),
        exercicio('Exercício 4 · Quam ou ablativo?', 'Reescreva com o ablativo de comparação quando for possível; quando não for, explique por quê.', [
            ('<i>Aurum cārius est quam argentum.</i> (<i>cārus</i>, caro)', '<i>Aurum argentō cārius est.</i> O primeiro termo (<i>aurum</i>) é nominativo, então o ablativo é possível: "o ouro é mais caro do que a prata".'),
            ('<i>Puer frātrem altiōrem quam patrem habet.</i>', 'Os termos comparados são <i>frātrem</i> e <i>patrem</i>, os dois no acusativo; o ablativo é possível: <i>Puer frātrem patre altiōrem habet</i>, "o menino tem um irmão mais alto do que o pai".'),
            ('<i>Fīliae plūs pecūniae dō quam fīliō.</i> (<i>dō</i>, dou)', 'Não é possível: <i>fīliae</i> e <i>fīliō</i> são dativos, e o ablativo de comparação só substitui <i>quam</i> depois de nominativo ou acusativo. "Dou mais dinheiro à filha do que ao filho."'),
            ('<i>Mārcus celerius currit quam Paulus.</i>', 'Com advérbio no comparativo (<i>celerius</i>), a prosa usa <i>quam</i>; o ablativo é raro e poético. Fica como está: "Marcos corre mais depressa do que Paulo".'),
            ('<i>Nihil est melius quam sapientia.</i> (<i>nihil</i>, nada)', '<i>Nihil est sapientiā melius.</i> O primeiro termo (<i>nihil</i>) é nominativo; numa frase negativa como esta, o ablativo é até a construção mais comum (Allen e Greenough § 407.b): "nada é melhor do que a sabedoria".'),
        ]),
        exercicio('Exercício 5 · Os advérbios', 'Forme o advérbio no positivo, no comparativo e no superlativo; depois traduza a frase.', [
            ('<i>lātus</i>, largo · <i>Flūmen lātē patet.</i> (<i>patet</i>, estende-se)', '<i>lātē, lātius, lātissimē</i>. "O rio estende-se largamente." Primeira classe: <i>-ē</i>.'),
            ('<i>celer</i>, rápido · <i>Nūntius celerrimē venit.</i> (<i>nūntius</i>, mensageiro)', '<i>celeriter, celerius, celerrimē</i>. "O mensageiro chega muito depressa." O superlativo do advérbio vem de <i>celerrimus</i>.'),
            ('<i>sapiēns</i>, sábio · <i>Rēx sapienter rēgnat.</i> (<i>rēgnat</i>, reina)', '<i>sapienter, sapientius, sapientissimē</i>. "O rei reina sabiamente." Adjetivo em <i>-ns</i>: só <i>-er</i>.'),
            ('<i>bonus</i> · <i>Discipulī melius legunt quam scrībunt.</i>', '<i>bene, melius, optimē</i>. "Os alunos leem melhor do que escrevem." <i>Melius</i> é aqui advérbio: modifica <i>legunt</i>.'),
            ('<i>multus</i> · <i>Puer plūrimum dormit.</i>', '<i>multum, plūs, plūrimum</i>. "O menino dorme muitíssimo."'),
        ]),
        exercicio('Exercício 6 · Traduza e retroverta', 'Traduza as três primeiras para o português e as três últimas para o latim. Vocabulário: <i>īnsula, -ae</i>, ilha; <i>mōns, montis</i> (m.), monte; <i>urbs, urbis</i> (f.), cidade; <i>omnium</i>, de todos.', [
            ('<i>Haec īnsula multō maior est quam illa.</i> (<i>haec · illa</i>, esta · aquela)', '"Esta ilha é muito maior do que aquela." <i>Multō</i>: grau de diferença; <i>illa</i>, nominativo como <i>īnsula</i>.'),
            ('<i>Rōma urbs pulcherrima est.</i>', '"Roma é uma cidade belíssima." Superlativo absoluto: não há termo de comparação.'),
            ('<i>Mārcus omnium discipulōrum dīligentissimus est.</i> (<i>dīligēns</i>, diligente)', '"Marcos é o mais diligente de todos os alunos." Superlativo relativo, com o genitivo <i>omnium discipulōrum</i>.'),
            ('A menina é mais prudente do que o irmão.', '<i>Puella prūdentior est quam frāter</i> ou <i>Puella frātre prūdentior est.</i> Os dois termos no nominativo, então as duas construções servem.'),
            ('Este monte é altíssimo.', '<i>Hīc mōns altissimus est.</i> Superlativo absoluto, masculino, concordando com <i>mōns</i>.'),
            ('Os soldados combatem o mais corajosamente possível.', '<i>Mīlitēs quam fortissimē pugnant.</i> <i>Quam</i> + superlativo do advérbio = "o mais … possível".'),
        ]),
    ],
    leituras=['d-ooge-latin-for-beginners', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'caesar-commentarii-de-bello-gallico-selecoes', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'ravizza-gramatica-latina', 'greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc'],
    leituras_nota='Latin for Beginners, de D\'Ooge, tem lições e exercícios graduados sobre a comparação de adjetivos e advérbios. Em Familia Romana, de Ørberg, observe como o texto apresenta os comparativos e superlativos em contexto, sem tradução. Nas seleções da Guerra da Gália, leia o capítulo 1 do livro I até o fim: ele traz <i>fortissimī</i>, <i>longissimē</i>, <i>minimē</i> e <i>proximī</i>. Na Vulgata, procure em Mateus 10,29–31 e 22,34–40 os comparativos e superlativos. Ravizza (nn. 55–60) e Allen e Greenough (§§ 120–131, 291–292, 406–407) servem para consulta.',
)
