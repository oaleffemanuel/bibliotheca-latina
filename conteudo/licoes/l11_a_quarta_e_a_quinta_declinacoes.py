from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

_CASOS = ('Nom.', 'Gen.', 'Dat.', 'Ac.', 'Voc.', 'Abl.')

LICAO = dict(
    slug='11-a-quarta-e-a-quinta-declinacoes', titulo='Quarta e quinta declinações; quadro das cinco declinações',
    titulo_latim='Dē quārtā et quīntā dēclīnātiōne', tempo='60 min',
    resumo='As duas últimas declinações, pequenas mas cheias de palavras frequentes: a quarta, de genitivo em -ūs (frūctus, manus, cornū e a casa mista de domus, com domī, domum e domō), e a quinta, de genitivo em -ēī ou -eī (diēs, rēs, fidēs, spēs); os muitos sentidos de rēs; e o quadro completo das cinco declinações, com as coincidências que valem para todas e um procedimento para identificar a declinação a partir do dicionário.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['4ª declinação', 'genitivo em -ūs', 'paradigma frūctus e manus', 'neutros em -ū (cornū, genū)', 'dativo e ablativo plural em -ubus', 'gênero na 4ª declinação', 'domus e o locativo domī', 'domum e domō sem preposição', '5ª declinação', 'genitivo em -ēī e -eī', 'diēs: masculino e feminino', 'rēs e seus sentidos (rēs pūblica, rēs gestae)', 'fidēs e spēs: plural defectivo', 'quadro das cinco declinações', 'coincidências entre casos', 'identificar a declinação pelo dicionário', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulos 9 e 10: a terceira declinação inteira (temas consonantais e temas em <i>-i</i>), com a ideia de que o genitivo do dicionário revela o tema. Também os capítulos 4 e 5 (primeira e segunda declinações; adjetivos como <i>bonus, -a, -um</i>) e o capítulo 7, sobre como ler uma entrada de dicionário.',
                       licoes=['04-a-primeira-declinacao', '05-a-segunda-declinacao', '07-como-usar-o-dicionario', '09-a-terceira-declinacao-temas-consonantais', '10-a-terceira-declinacao-temas-em-i']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 18 (as cinco declinações e o genitivo singular de cada uma), § 19 (casos iguais na forma: vocativo = nominativo; dativo = ablativo plural; neutros com N = Ac e plural em -a; Ac pl = N pl na 3ª, 4ª e 5ª), § 40.1.a (nūbēs, nūbis: 3ª declinação), § 48 (frūctus, cornū), § 49 (genitivo arcaico em -ī; dativo em -ū; -ubus em tribus, lacus, arcus; domus com formas da 2ª: domī, domō, domum; neutros cornū, genū, verū), § 50 (femininos da 4ª: acus, domus, manus, porticus, tribus, Īdūs), §§ 51–53 (diēs, rēs; -ĕī depois de consoante; plural de spēs, aciēs e outros só no N e Ac; gênero de diēs), § 182.1.b e nota (domum sem preposição; in domum quando é o edifício), § 229.1.b (domō), § 232.2 (locativo domī)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 37 (as cinco declinações e o genitivo singular), § 38 (regras gerais: vocativo, neutros, acusativo em -m e -s, dativo = ablativo plural, genitivo plural sempre em -um), § 39 (quadro das terminações das cinco declinações), §§ 88–91 (4ª declinação: tema em u-, paradigmas manus, lacus, genū; gênero), § 92 (particularidades: -ubus em tribus, artus, lacus; portus com -ubus e -ibus), § 93 (domus: formas da 4ª e da 2ª; locativo domī), § 94 (cāsus de cadō), §§ 95–97 (5ª declinação: rēs, diēs, fidēs; ē breve no genitivo e dativo de fidēs, spēs, rēs; diēs feminino: cōnstitūtā diē, longa diēs), § 98 (só diēs e rēs se declinam por inteiro; spēs, aciēs, faciēs no N e Ac plural; locativo em -ē: hodiē)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 55 (4ª declinação: gradus, genū), § 56 (declinam-se como gradus: frūctus, senātus, manus; femininos e neutros; -ubus; domus), § 57 (5ª declinação: rēs; diēs; rēs e diēs são os únicos com genitivo, dativo e ablativo plural; fidēs só no singular; gênero de diēs)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 37 (4ª declinação: sensus, manus, domus com o locativo domī e o sentido de domī, domum, domō; genū), n. 38 (dativo e ablativo plural em -ubus: arcus, lacus, tribus), n. 39 (outras particularidades: genitivo arcaico senātī, dativo contraído em -ū), n. 40 (5ª declinação: diēs masculino ou feminino no singular, sempre masculino no plural; -ēī depois de vogal, -eī depois de consoante; paradigmas diēs e rēs), n. 41 (só diēs e rēs têm todo o plural; spēs e aciēs só nos casos em -ēs)', tipo='dominio_publico'),
        referencia('A Latin Dictionary (Lewis & Short)', 'Charlton T. Lewis e Charles Short', catalogo='short-a-latin-dictionary-lewis-short', nota='verbete rēs, conferido na edição Perseus: rēs pūblica ("o bem comum, o Estado"), rēs gestae ("feitos"), rēs novae ("mudanças políticas, revolução"), rēs secundae e adversae ("boa e má fortuna"); verbete cāsus (sentido gramatical de "caso")', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Lucas 23,46 e Mateus 6,34', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Lucam', nota='frases autênticas da seção 6, conferidas na Wikisource latina (Lucas, cap. 23, v. 46; Mateus, cap. 6, v. 34); macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Reconhecer pelo genitivo singular os nomes da quarta declinação (<i>-ūs</i>) e da quinta (<i>-ēī</i> ou <i>-eī</i>), mesmo quando o nominativo parece da segunda ou da terceira.',
        'Declinar <i>frūctus</i>, <i>manus</i>, <i>cornū</i>, <i>diēs</i> e <i>rēs</i>, e usar corretamente as formas especiais <i>domī</i>, <i>domum</i> e <i>domō</i>.',
        'Fazer concordar os adjetivos com os nomes destas declinações, inclusive os femininos em <i>-us</i> (<i>manus bona</i>) e o masculino <i>diēs</i>.',
        'Traduzir <i>rēs</i> e as expressões <i>rēs pūblica</i> e <i>rēs gestae</i> pelo sentido que o contexto pede, e não sempre por "coisa".',
        'Usar o quadro das cinco declinações e suas coincidências para identificar a declinação de qualquer entrada de dicionário e as leituras possíveis de uma terminação.',
    ],
    secoes=[
        ('A quarta declinação: o genitivo em -ūs', f'''
<p>Você já leu um nome da quarta declinação sem saber: no capítulo 5, em Mt 7,17, o adjetivo <i>bonōs</i> mostrou que <i>frūctūs</i> era acusativo plural, embora a terminação não se parecesse com nada conhecido. Agora é hora de conhecer a declinação inteira. Ela é pequena em número de palavras, mas essas palavras são frequentes: <i>manus</i> (mão), <i>exercitus</i> (exército), <i>senātus</i> (senado), <i>domus</i> (casa), <i>spīritus</i> (sopro, espírito), e o próprio <i>cāsus</i>, "queda", de onde vem a palavra "caso" que você conheceu no capítulo 3.</p>
<p>A marca da quarta declinação é o <b>genitivo singular em <i>-ūs</i></b>, com <i>u</i> longo: o dicionário registra <i>frūctus, -ūs</i> (m.), e é esse <i>-ūs</i> que diz "quarta". O tema termina em <i>u</i> (<i>frūctu-</i>), e esse <i>u</i> aparece em quase todas as formas; ele só se enfraquece em <i>i</i> diante de <i>-bus</i> (<i>frūctibus</i>), como explicam Allen e Greenough (§ 88). Por isso a declinação é fácil de reconhecer: um <i>u</i> antes da terminação (<i>-uī, -uum</i>) ou um <i>u</i> longo no fim (<i>-ūs, -ū</i>) quase sempre indica a quarta.</p>
{tabela_declinacao('Quarta declinação, masculino e feminino: frūctus, -ūs (m.), "fruto" · manus, -ūs (f.), "mão"', [
    ('frūct<b>us</b>', 'frūct<b>ūs</b>', 'man<b>us</b>', 'man<b>ūs</b>'), ('frūct<b>ūs</b>', 'frūct<b>uum</b>', 'man<b>ūs</b>', 'man<b>uum</b>'),
    ('frūct<b>uī</b>', 'frūct<b>ibus</b>', 'man<b>uī</b>', 'man<b>ibus</b>'), ('frūct<b>um</b>', 'frūct<b>ūs</b>', 'man<b>um</b>', 'man<b>ūs</b>'),
    ('frūct<b>us</b>', 'frūct<b>ūs</b>', 'man<b>us</b>', 'man<b>ūs</b>'), ('frūct<b>ū</b>', 'frūct<b>ibus</b>', 'man<b>ū</b>', 'man<b>ibus</b>')],
    colunas=('frūctus · sing.', 'frūctus · pl.', 'manus · sing.', 'manus · pl.'))}
<p>Repare na forma <i>frūctūs</i>: ela aparece quatro vezes no paradigma, como genitivo singular e como nominativo, acusativo e vocativo plural. Nos textos com macrons, o nominativo singular (<i>frūctus</i>, <i>u</i> breve) se distingue dela; nos textos sem macrons, que são a maioria, <i>fructus</i> pode ser qualquer uma dessas cinco formas. Quem decide, como sempre, é a frase: o número do verbo, a preposição, as funções já ocupadas e, sobretudo, o adjetivo (<i>frūctūs bonī</i>, <i>frūctūs bonōs</i>). Duas variantes menores, para reconhecer: o dativo singular aparece às vezes contraído em <i>-ū</i> (<i>frūctū</i> por <i>frūctuī</i>, Bennett § 49.2), e alguns nomes conservam o dativo e ablativo plural antigo em <i>-ubus</i>: <i>tribus</i> (tribo) faz sempre <i>tribubus</i>, e <i>lacus</i> (lago) faz em regra <i>lacubus</i>: Allen e Greenough (§ 92.c) dizem "regularmente", e Kennedy (§ 56, nota 1), "sempre"; Bennett (§ 49.3) admite também <i>lacibus</i>.</p>
<p><b>O gênero.</b> Os nomes em <i>-us</i> da quarta declinação são quase todos <b>masculinos</b>. As exceções femininas são poucas e vale decorá-las, porque duas delas estão entre as palavras mais comuns do latim: <i>manus</i> (mão) e <i>domus</i> (casa); as outras são <i>tribus</i> (tribo), <i>porticus</i> (pórtico), <i>acus</i> (agulha) e o plural <i>Īdūs</i>, os Idos do calendário (Bennett § 50; Allen e Greenough § 90). A consequência está no adjetivo: diz-se <i>manus bona</i> e <i>domus magna</i>, com o adjetivo no feminino, embora o nome termine em <i>-us</i>. É a mesma regra do capítulo 9: o adjetivo copia o gênero, o número e o caso, não a terminação.</p>
{tabela(['Nome', 'Significado', 'Nome', 'Significado'], [
    ['frūctus, -ūs (m.)', 'fruto; proveito', 'manus, -ūs (f.)', 'mão; grupo armado'], ['exercitus, -ūs (m.)', 'exército', 'domus, -ūs (f.)', 'casa, lar (seção 2)'],
    ['senātus, -ūs (m.)', 'senado', 'cornū, -ūs (n.)', 'chifre; ala do exército'], ['spīritus, -ūs (m.)', 'sopro, alento, espírito', 'genū, -ūs (n.)', 'joelho'],
    ['cāsus, -ūs (m.)', 'queda; acaso; caso gramatical', 'lacus, -ūs (m.)', 'lago'], ['portus, -ūs (m.)', 'porto', 'gradus, -ūs (m.)', 'passo, degrau'],
], 'Vocabulário: nomes da quarta declinação', latim_cols=(0, 2))}
{dica('<b>O português ajuda.</b> Quase toda a lista sobrevive: <i>frūctus</i> deu "fruto", <i>exercitus</i> "exército", <i>senātus</i> "senado", <i>spīritus</i> "espírito", <i>cāsus</i> "caso", <i>portus</i> "porto", <i>lacus</i> "lago", <i>gradus</i> "grau", <i>cornū</i> "corno", <i>manus</i> "mão" (e "manual", "manuscrito"), <i>domus</i> "doméstico" e "domicílio". Repare que o português perdeu o <i>-us</i> em todas elas, exatamente como nos nomes da segunda declinação ("lobo", de <i>lupus</i>). A semelhança com o português, portanto, não distingue as declinações; só o genitivo distingue.')}
'''),
        ('Os neutros em -ū e a casa de duas declinações: domus', f'''
<p>A quarta declinação tem também alguns <b>neutros</b>, terminados em <i>-ū</i> longo. São pouquíssimos em uso: <i>cornū</i> (chifre), <i>genū</i> (joelho) e <i>verū</i> (espeto), segundo Bennett (§ 49.5). Eles seguem a regra dos neutros que você já aplicou na segunda e na terceira declinações: nominativo, acusativo e vocativo iguais, e plural em <i>-a</i> (aqui <i>-ua</i>). No singular, a forma <i>-ū</i> serve a todos os casos menos o genitivo:</p>
{tabela_declinacao('Quarta declinação, neutro: cornū, -ūs (n.), "chifre" · genū, -ūs (n.), "joelho"', [
    ('corn<b>ū</b>', 'corn<b>ua</b>', 'gen<b>ū</b>', 'gen<b>ua</b>'), ('corn<b>ūs</b>', 'corn<b>uum</b>', 'gen<b>ūs</b>', 'gen<b>uum</b>'),
    ('corn<b>ū</b>', 'corn<b>ibus</b>', 'gen<b>ū</b>', 'gen<b>ibus</b>'), ('corn<b>ū</b>', 'corn<b>ua</b>', 'gen<b>ū</b>', 'gen<b>ua</b>'),
    ('corn<b>ū</b>', 'corn<b>ua</b>', 'gen<b>ū</b>', 'gen<b>ua</b>'), ('corn<b>ū</b>', 'corn<b>ibus</b>', 'gen<b>ū</b>', 'gen<b>ibus</b>')],
    colunas=('cornū · sing.', 'cornū · pl.', 'genū · sing.', 'genū · pl.'))}
<p>Não confunda <i>genū</i> (joelho, quarta declinação, neutro) com <i>genus, generis</i> (gênero, origem), da terceira, que você viu no capítulo 9. O português guarda as duas famílias separadas: de <i>genū</i>, "genuflexão" (dobrar o joelho); de <i>genus</i>, "gênero" e "genérico".</p>
<h3>Domus: formas da quarta e da segunda</h3>
<p><i>Domus</i> (f.), "casa", tem dois temas, um em <i>u</i> e outro em <i>o</i>, e por isso mistura formas da quarta e da segunda declinações (Allen e Greenough § 93; Bennett § 49.4). O quadro abaixo segue Allen e Greenough; entre parênteses vão as formas menos usadas. As gramáticas divergem um pouco no plural: Allen e Greenough (§ 93, nota 2) consideram <i>domōrum</i> tardio ou poético, Kennedy (§ 56) dá <i>domōrum</i> ou <i>domuum</i> e <i>domūs</i> ou <i>domōs</i> sem marcar preferência, e Ravizza (n. 37) dá <i>domōs</i>, "raro <i>domūs</i>". Não é preciso decorá-lo de uma vez: o que importa é reconhecer as formas da segunda (<i>domō</i>, <i>domōs</i>) quando aparecerem, e saber de cor as três expressões que vêm logo depois.</p>
{tabela_declinacao('domus, -ūs (f.), "casa": formas da 4ª e da 2ª declinação', [
    ('dom<b>us</b>', 'dom<b>ūs</b>'), ('dom<b>ūs</b>', 'dom<b>uum</b> (dom<b>ōrum</b>)'),
    ('dom<b>uī</b> (dom<b>ō</b>)', 'dom<b>ibus</b>'), ('dom<b>um</b>', 'dom<b>ōs</b> (dom<b>ūs</b>)'),
    ('dom<b>us</b>', 'dom<b>ūs</b>'), ('dom<b>ō</b> (dom<b>ū</b>)', 'dom<b>ibus</b>')])}
<p>Há ainda uma forma que não cabe no quadro de seis casos: <i>domī</i>, "em casa". É um resto do <b>locativo</b>, um antigo caso de lugar que o latim perdeu quase por inteiro e conservou em algumas palavras (Bennett § 232.2; Allen e Greenough § 93, nota 1). Com ele, <i>domus</i> forma um pequeno sistema de três expressões, todas <b>sem preposição</b>, que respondem às três perguntas de lugar:</p>
{tabela(['Forma', 'Caso', 'Pergunta', 'Sentido', 'Exemplo'], [
    ['domī', 'locativo', 'onde?', 'em casa', '<i>Puer domī manet.</i> O menino fica em casa.'],
    ['domum', 'acusativo', 'para onde?', 'para casa', '<i>Pater domum venit.</i> O pai vem para casa.'],
    ['domō', 'ablativo', 'de onde?', 'de casa', '<i>Servus domō fugit.</i> O escravo foge de casa.'],
], 'Domī, domum, domō', latim_cols=(0,))}
<p>Por que sem preposição, se no capítulo 4 você aprendeu <i>in</i> e <i>ad</i> com acusativo para o movimento e <i>in</i> com ablativo para o lugar? Porque <i>domus</i>, no sentido de "o lar, a própria casa", se comporta como os nomes de cidade, que dispensam a preposição (Bennett § 182.1.b e § 229.1.b; o assunto volta, completo, no capítulo 19). Quando <i>domus</i> designa o <b>edifício</b>, sobretudo acompanhado de um adjetivo, a preposição volta: Bennett (§ 182, nota) cita <i>in domum veterem remigrāre</i>, "mudar-se de volta para uma casa velha". Na prática: "ir para casa" é <i>domum</i>; "entrar numa casa grande" é <i>in domum magnam</i>.</p>
{observacao('Por que domī se parece com um genitivo da 2ª', 'No singular da primeira e da segunda declinações, o locativo tem a mesma forma do genitivo: <i>Rōmae</i>, "em Roma"; <i>Corinthī</i>, "em Corinto" (Bennett § 232.1). <i>Domī</i> é desse tipo, porque vem do tema em <i>o</i> de <i>domus</i>. Mas o genitivo usual de <i>domus</i> é <i>domūs</i> (o genitivo <i>domī</i> só aparece em Plauto, segundo Allen e Greenough § 93, nota 2). Por isso, ao encontrar <i>domī</i> num texto clássico, leia "em casa", e não "da casa".')}
'''),
        ('A quinta declinação: rēs e diēs', f'''
<p>A quinta declinação é a menor de todas. Seu tema termina em <i>ē</i>, que aparece em todos os casos (Allen e Greenough § 95), e o nominativo se forma acrescentando <i>-s</i>: <i>rē-s</i>, <i>diē-s</i>. A marca no dicionário é o <b>genitivo singular em <i>-ēī</i> ou <i>-eī</i></b>: <i>diēs, diēī</i>; <i>rēs, reī</i>. Só dois nomes se declinam por inteiro, nos dois números: <i>diēs</i> (dia) e <i>rēs</i> (coisa). Os outros têm o singular completo e pouco ou nada do plural.</p>
{tabela_declinacao('Quinta declinação: diēs, diēī (m.), "dia" · rēs, reī (f.), "coisa"', [
    ('di<b>ēs</b>', 'di<b>ēs</b>', 'r<b>ēs</b>', 'r<b>ēs</b>'), ('di<b>ēī</b>', 'di<b>ērum</b>', 'r<b>eī</b>', 'r<b>ērum</b>'),
    ('di<b>ēī</b>', 'di<b>ēbus</b>', 'r<b>eī</b>', 'r<b>ēbus</b>'), ('di<b>em</b>', 'di<b>ēs</b>', 'r<b>em</b>', 'r<b>ēs</b>'),
    ('di<b>ēs</b>', 'di<b>ēs</b>', 'r<b>ēs</b>', 'r<b>ēs</b>'), ('di<b>ē</b>', 'di<b>ēbus</b>', 'r<b>ē</b>', 'r<b>ēbus</b>')],
    colunas=('diēs · sing.', 'diēs · pl.', 'rēs · sing.', 'rēs · pl.'))}
<p>Compare as duas colunas do singular. O genitivo e o dativo de <i>diēs</i> têm <i>ē</i> longo (<i>diēī</i>); os de <i>rēs</i> têm <i>e</i> breve (<i>reī</i>). A regra é de pronúncia: o <i>ē</i> fica longo quando vem depois de uma <b>vogal</b> (<i>di-ēī</i>, <i>faci-ēī</i>, <i>aci-ēī</i>) e se abrevia depois de uma <b>consoante</b> (<i>r-eī</i>, <i>fid-eī</i>, <i>sp-eī</i>), como dizem Bennett (§ 52.1) e o Pe. Ravizza (n. 40). No acusativo singular o <i>e</i> é sempre breve: <i>diem</i>, <i>rem</i> (Allen e Greenough § 96, nota). Note também que o genitivo e o dativo singulares são iguais (<i>reī</i> = "da coisa" ou "à coisa"), e que <i>rēs</i> sozinho pode ser nominativo singular, nominativo ou acusativo plural, ou vocativo: são quatro leituras para a mesma forma, e a frase escolhe.</p>
<h3>O gênero: feminino, menos diēs</h3>
<p>Os nomes da quinta declinação são <b>femininos</b>, com uma exceção importante: <i>diēs</i> é normalmente <b>masculino</b> (e o seu composto <i>merīdiēs</i>, "meio-dia", sempre). Por isso se diz <i>diēs longus</i>, "um dia longo", e <i>diēs longī</i> no plural. Mas <i>diēs</i> pode ser feminino no singular, sobretudo quando significa um <b>dia marcado</b>, uma data, ou o tempo em geral: Allen e Greenough (§ 97.a) citam <i>cōnstitūtā diē</i>, "no dia combinado", e <i>longa diēs</i>, "um longo tempo"; Bennett (§ 53) registra a mesma nuance. No plural, segundo o Pe. Ravizza (n. 40), é sempre masculino. Para o iniciante, a regra prática é: <i>diēs</i> masculino, salvo quando o adjetivo feminino mostrar o contrário.</p>
<h3>Os nomes de plural incompleto: fidēs e spēs</h3>
<p>Fora <i>diēs</i> e <i>rēs</i>, os nomes da quinta declinação não se usam no plural, ou se usam só no nominativo e no acusativo (Bennett § 52.4; Allen e Greenough § 98.a; Ravizza n. 41). Dois deles, muito frequentes, merecem atenção. <i>Spēs, speī</i> (esperança) tem plural só em <i>-ēs</i>: <i>spēs</i>, "as esperanças", como sujeito ou objeto; formas como "das esperanças" não se usam na prosa clássica. <i>Fidēs, fideī</i> (fé, confiança, lealdade, palavra dada) fica no singular; Kennedy (§ 57) o dá como nome "só do singular". Cuidado com um homônimo: existe outro <i>fidēs</i>, usado na prosa clássica só no plural, que significa "lira" (Bennett § 56). O contexto, e o dicionário, separam os dois.</p>
{tabela_declinacao('fidēs, fideī (f.), "fé, lealdade" · spēs, speī (f.), "esperança" · faciēs, faciēī (f.), "rosto, aspecto"', [
    ('fid<b>ēs</b>', 'sp<b>ēs</b>', 'faci<b>ēs</b>'), ('fid<b>eī</b>', 'sp<b>eī</b>', 'faci<b>ēī</b>'), ('fid<b>eī</b>', 'sp<b>eī</b>', 'faci<b>ēī</b>'),
    ('fid<b>em</b>', 'sp<b>em</b>', 'faci<b>em</b>'), ('fid<b>ēs</b>', 'sp<b>ēs</b>', 'faci<b>ēs</b>'), ('fid<b>ē</b>', 'sp<b>ē</b>', 'faci<b>ē</b>')],
    colunas=('fidēs · sing.', 'spēs · sing.', 'faciēs · sing.'))}
{tabela(['Nome', 'Significado', 'Plural'], [
    ['diēs, diēī (m.; às vezes f.)', 'dia; data; tempo', 'completo'], ['rēs, reī (f.)', 'coisa, assunto, fato (seção 4)', 'completo'],
    ['fidēs, fideī (f.)', 'fé, confiança, lealdade, palavra dada', 'não se usa'], ['spēs, speī (f.)', 'esperança', 'só nominativo e acusativo (<i>spēs</i>)'],
    ['faciēs, faciēī (f.)', 'rosto, aspecto, forma', 'só nominativo e acusativo'], ['aciēs, aciēī (f.)', 'gume; linha de batalha', 'só nominativo e acusativo'],
    ['merīdiēs, merīdiēī (m.)', 'meio-dia', 'não se usa'],
], 'Vocabulário: nomes da quinta declinação', latim_cols=(0,))}
{observacao('Um locativo escondido em "hoje"', 'A quinta declinação também teve um locativo, em <i>-ē</i>, que sobreviveu só em advérbios e expressões de tempo (Allen e Greenough § 98.b). O mais conhecido é <i>hodiē</i>, "hoje", formado com esse <i>diē</i>, de onde vem o português "hoje". O mesmo <i>diē</i> está em <i>prīdiē</i>, "na véspera". Você não precisa produzir essas formas; basta saber que <i>hodiē</i> é uma palavra só, e não um ablativo de <i>diēs</i> com algo à frente.')}
'''),
        ('Os muitos sentidos de rēs', f'''
<p><i>Rēs</i> é uma das palavras mais frequentes do latim justamente porque significa quase nada por si mesma: é "coisa" no sentido mais amplo, como o português "coisa", "assunto", "caso", "fato", "situação", "negócio" e até "bens". O dicionário de Lewis e Short abre o verbete com uma lista assim: coisa, objeto, assunto, acontecimento, fato, circunstância, feito, condição. Na prática, isso quer dizer que <b>"coisa" quase nunca é a melhor tradução</b>. O sentido exato vem do contexto e, muitas vezes, do adjetivo que acompanha <i>rēs</i>, formando expressões fixas que você deve aprender como unidades:</p>
{tabela(['Expressão', 'Literalmente', 'Sentido usual'], [
    ['rēs pūblica', 'a coisa pública', 'o Estado, a república, os negócios públicos'],
    ['rēs gestae (plural)', 'as coisas feitas', 'os feitos, as façanhas, a história de alguém'],
    ['rēs novae (plural)', 'coisas novas', 'mudança política, revolução'],
    ['rēs secundae · rēs adversae', 'coisas favoráveis · contrárias', 'a boa fortuna · a adversidade'],
    ['rēs mīlitāris', 'a coisa militar', 'a arte da guerra, os assuntos militares'],
], 'Expressões com rēs (sentidos conferidos em Lewis e Short)', latim_cols=(0,))}
<p><i>Rēs pūblica</i> merece um comentário à parte. São duas palavras, e as duas se declinam: o nome pela quinta declinação, o adjetivo pela primeira, sempre em concordância. Por isso o genitivo é <i>reī pūblicae</i>, "da república", e o acusativo <i>rem pūblicam</i>. É a mesma situação de <i>bonae voluntātis</i>, que você analisou no capítulo 9: duas declinações diferentes, um só gênero, número e caso. A expressão é tão fixa que às vezes se escreve numa palavra só, <i>rēspūblica</i>, mas o interior continua mudando: <i>reīpūblicae</i>, <i>rempūblicam</i>.</p>
{tabela_declinacao('rēs pūblica (f.), "o Estado, a república" · só singular', [
    ('r<b>ēs</b> pūblic<b>a</b>',), ('r<b>eī</b> pūblic<b>ae</b>',), ('r<b>eī</b> pūblic<b>ae</b>',), ('r<b>em</b> pūblic<b>am</b>',), ('r<b>ēs</b> pūblic<b>a</b>',), ('r<b>ē</b> pūblic<b>ā</b>',)],
    colunas=('Singular',))}
{exemplos([('Senātus rem pūblic<b>am</b> regit.', 'O senado governa o Estado. (<i>rem pūblicam</i>: acusativo singular, objeto; <i>regit</i>, de <i>regō</i>, "governar, dirigir")'),
           ('Poēta rēs gest<b>ās</b> rēgis nārrat.', 'O poeta narra os feitos do rei. (<i>rēs gestās</i>: acusativo plural feminino; o adjetivo em <i>-ās</i> desfaz a ambiguidade de <i>rēs</i>)'),
           ('Rēs nov<b>a</b> est.', 'A coisa é nova; isto é novidade. (<i>rēs</i> no singular, sujeito; <i>nova</i> predicativo)'),
           ('Hominēs rēs nov<b>ās</b> timent.', 'Os homens temem uma revolução. (<i>rēs novās</i>: expressão fixa; "coisas novas" seria uma tradução fraca)')])}
{dica('<b>Como traduzir rēs.</b> Primeiro identifique o caso e o número; depois pergunte que "coisa" o contexto pede. Diante de uma expressão com adjetivo, procure-a no dicionário como unidade: os dicionários registram <i>rēs pūblica</i>, <i>rēs gestae</i> e <i>rēs novae</i> dentro do verbete <i>rēs</i>. A palavra <i>gestae</i> é um particípio (capítulo 29), mas aqui basta tratá-la como um adjetivo que concorda com <i>rēs</i>.')}
'''),
        ('O quadro das cinco declinações', f'''
<p>Com este capítulo, você conhece as cinco declinações do latim. É o momento de vê-las lado a lado. As gramáticas as distinguem por dois critérios que andam juntos: a letra final do tema e a terminação do <b>genitivo singular</b> (Bennett § 18; Allen e Greenough § 37). Para quem lê, o segundo critério é o que importa, porque é ele que o dicionário mostra.</p>
{tabela(['Declinação', 'Genitivo sing.', 'Nominativo sing.', 'Gênero', 'Entrada de dicionário'], [
    ['1ª', '<b>-ae</b>', '<i>-a</i>', 'feminino (alguns m.: <i>nauta</i>)', '<i>rosa, -ae</i> (f.)'],
    ['2ª', '<b>-ī</b>', '<i>-us</i>, <i>-er</i>; <i>-um</i>', 'masculino; neutro em <i>-um</i>', '<i>lupus, -ī</i> (m.); <i>bellum, -ī</i> (n.)'],
    ['3ª', '<b>-is</b>', 'vários', 'os três', '<i>rēx, rēgis</i> (m.); <i>corpus, corporis</i> (n.)'],
    ['4ª', '<b>-ūs</b>', '<i>-us</i>; <i>-ū</i>', 'masculino (alguns f.); neutro em <i>-ū</i>', '<i>frūctus, -ūs</i> (m.); <i>cornū, -ūs</i> (n.)'],
    ['5ª', '<b>-ēī</b>, <b>-eī</b>', '<i>-ēs</i>', 'feminino (<i>diēs</i> m.)', '<i>rēs, reī</i> (f.); <i>diēs, diēī</i> (m.)'],
], 'O genitivo singular identifica a declinação', latim_cols=())}
<p>Agora as terminações das cinco declinações completas, para os nomes masculinos e femininos. Para caber na tela, o quadro está dividido em singular e plural, e cada coluna traz no cabeçalho o modelo que você já declinou por inteiro: <i>rosa</i> (1ª), <i>lupus</i> (2ª), <i>rēx</i> (3ª), <i>manus</i> (4ª) e <i>rēs</i> (5ª). Para obter a forma completa, junte a terminação ao tema: <i>ros-ārum</i>, <i>lup-ōrum</i>, <i>rēg-um</i>, <i>man-uum</i>, <i>r-ērum</i>. Leia cada linha da esquerda para a direita e observe o que se repete.</p>
{tabela_declinacao('As cinco declinações · singular (masculino e feminino; na 5ª, -ēī depois de vogal: diēī)', [
    ('<b>-a</b>', '<b>-us</b>', 'vários', '<b>-us</b>', '<b>-ēs</b>'),
    ('<b>-ae</b>', '<b>-ī</b>', '<b>-is</b>', '<b>-ūs</b>', '<b>-eī</b>'),
    ('<b>-ae</b>', '<b>-ō</b>', '<b>-ī</b>', '<b>-uī</b>', '<b>-eī</b>'),
    ('<b>-am</b>', '<b>-um</b>', '<b>-em</b>', '<b>-um</b>', '<b>-em</b>'),
    ('<b>-a</b>', '<b>-e</b>', '= nom.', '<b>-us</b>', '<b>-ēs</b>'),
    ('<b>-ā</b>', '<b>-ō</b>', '<b>-e</b>', '<b>-ū</b>', '<b>-ē</b>')],
    casos=_CASOS, colunas=('1ª rosa', '2ª lupus', '3ª rēx', '4ª manus', '5ª rēs'))}
{tabela_declinacao('As cinco declinações · plural (masculino e feminino)', [
    ('<b>-ae</b>', '<b>-ī</b>', '<b>-ēs</b>', '<b>-ūs</b>', '<b>-ēs</b>'),
    ('<b>-ārum</b>', '<b>-ōrum</b>', '<b>-um</b>', '<b>-uum</b>', '<b>-ērum</b>'),
    ('<b>-īs</b>', '<b>-īs</b>', '<b>-ibus</b>', '<b>-ibus</b>', '<b>-ēbus</b>'),
    ('<b>-ās</b>', '<b>-ōs</b>', '<b>-ēs</b>', '<b>-ūs</b>', '<b>-ēs</b>'),
    ('<b>-ae</b>', '<b>-ī</b>', '<b>-ēs</b>', '<b>-ūs</b>', '<b>-ēs</b>'),
    ('<b>-īs</b>', '<b>-īs</b>', '<b>-ibus</b>', '<b>-ibus</b>', '<b>-ēbus</b>')],
    casos=_CASOS, colunas=('1ª rosa', '2ª lupus', '3ª rēx', '4ª manus', '5ª rēs'))}
<p>Na terceira coluna, lembre que os temas em <i>-i</i> do capítulo 10 fazem o genitivo plural em <i>-ium</i> (e alguns o acusativo plural também em <i>-īs</i>), e os neutros desse tipo fazem o plural em <i>-ia</i>; o quadro mostra o tema consonantal. Os neutros têm só três declinações, e seguem todos a mesma regra:</p>
{tabela_declinacao('Terminações dos neutros: bellum (2ª) · corpus (3ª) · cornū (4ª)', [
    ('<b>-um</b>', '<b>-a</b>', 'vários', '<b>-a</b>', '<b>-ū</b>', '<b>-ua</b>'),
    ('<b>-ī</b>', '<b>-ōrum</b>', '<b>-is</b>', '<b>-um</b>', '<b>-ūs</b>', '<b>-uum</b>'),
    ('<b>-ō</b>', '<b>-īs</b>', '<b>-ī</b>', '<b>-ibus</b>', '<b>-ū</b>', '<b>-ibus</b>'),
    ('<b>-um</b>', '<b>-a</b>', '= nom.', '<b>-a</b>', '<b>-ū</b>', '<b>-ua</b>'),
    ('<b>-um</b>', '<b>-a</b>', '= nom.', '<b>-a</b>', '<b>-ū</b>', '<b>-ua</b>'),
    ('<b>-ō</b>', '<b>-īs</b>', '<b>-e</b>', '<b>-ibus</b>', '<b>-ū</b>', '<b>-ibus</b>')],
    casos=_CASOS, colunas=('2ª sing.', '2ª pl.', '3ª sing.', '3ª pl.', '4ª sing.', '4ª pl.'))}
<h3>O que vale para todas as declinações</h3>
<p>Olhando os quadros, aparecem regularidades que atravessam as cinco declinações. Bennett (§ 19) e Allen e Greenough (§ 38) as registram como "regras gerais", e elas economizam muito trabalho, porque reduzem o número de formas que você precisa realmente distinguir:</p>
<ul>
<li><b>Dativo e ablativo plural são sempre iguais</b>: <i>rosīs, lupīs, rēgibus, manibus, rēbus</i>. Diante de qualquer uma dessas formas, a pergunta é sempre "dativo ou ablativo?", e quem responde é a preposição ou o verbo.</li>
<li><b>O vocativo é igual ao nominativo</b>, com uma única exceção: o singular dos nomes em <i>-us</i> da segunda declinação (<i>lupe</i>). <i>Manus</i> e <i>rēs</i> não mudam.</li>
<li><b>Nos neutros, nominativo, acusativo e vocativo são iguais</b>, e no plural terminam em <i>-a</i> (<i>bella, corpora, cornua</i>).</li>
<li><b>Na 3ª, na 4ª e na 5ª, o acusativo plural é igual ao nominativo plural</b> (<i>rēgēs, manūs, rēs</i>). Só a 1ª e a 2ª distinguem sujeito e objeto no plural (<i>rosae/rosās</i>, <i>lupī/lupōs</i>), e por isso os adjetivos de primeira classe são tão úteis.</li>
<li><b>O acusativo singular masculino e feminino termina em <i>-m</i></b> e o acusativo plural em <i>-s</i>, em todas as declinações (<i>rosam, lupum, rēgem, manum, rem</i>).</li>
<li><b>O genitivo plural termina sempre em <i>-um</i></b> (<i>-ārum, -ōrum, -um</i> ou <i>-ium, -uum, -ērum</i>), segundo Allen e Greenough (§ 38.f). Um <i>-rum</i> indica 1ª, 2ª ou 5ª; um <i>-uum</i>, a 4ª.</li>
</ul>
<p>O lado difícil é o inverso: a mesma terminação pode pertencer a declinações diferentes, com valores diferentes. O quadro abaixo junta as coincidências que mais enganam. Nenhuma delas se resolve olhando só a terminação; todas se resolvem sabendo a que declinação pertence a palavra, isto é, conhecendo o seu genitivo.</p>
{comparacao('Terminações que se repetem entre as declinações', ['Terminação', 'Onde aparece', 'Exemplos', 'Como decidir'], [
    ['-us', 'nom. sing. da 2ª e da 4ª; nom./ac. sing. de neutros da 3ª', '<i>lupus</i>; <i>manus</i>; <i>corpus</i>', 'o genitivo do dicionário: <i>-ī</i>, <i>-ūs</i> ou <i>-oris</i>'],
    ['-ūs', 'gen. sing. e nom./ac./voc. pl. da 4ª', '<i>manūs</i>', 'o adjetivo e o verbo (<i>manūs bonae</i>, <i>manūs bonās</i>)'],
    ['-um', 'ac. sing. da 2ª e da 4ª; neutro da 2ª; gen. pl. da 3ª', '<i>lupum, manum, bellum, rēgum</i>', 'a declinação da palavra; "dos reis", mas "o lobo"'],
    ['-ēs', 'nom./ac. pl. da 3ª; nom. sing. e nom./ac. pl. da 5ª', '<i>rēgēs</i>; <i>rēs, diēs</i>', 'o genitivo: <i>rēgis</i> ou <i>reī</i>; o número do verbo'],
    ['-ī', 'gen. sing. e nom. pl. da 2ª; dat. sing. da 3ª; final de <i>-uī</i> e <i>-eī</i>', '<i>lupī, rēgī, manuī, reī</i>', 'olhe a vogal antes do <i>-ī</i>'],
    ['-ibus', 'dat./abl. pl. da 3ª e da 4ª', '<i>rēgibus, manibus</i>', 'o tema: <i>rēg-</i> ou <i>manu-</i>'],
    ['-e, -ē', 'voc. sing. da 2ª (<i>-e</i>); abl. sing. da 3ª (<i>-e</i>); abl. sing. da 5ª (<i>-ē</i>)', '<i>lupe, rēge, rē, diē</i>', 'a declinação; nos textos com macrons, a quantidade'],
])}
<p>Leia uma frase que junta três declinações num só período. Nenhuma das formas é ambígua dentro da frase, mas cada uma pertence a uma família diferente:</p>
{diagrama_frase([('Rēx', 'nominativo sing. (3ª) · sujeito'), ('exercituī', 'dativo sing. (4ª) · "ao exército"'), ('spem', 'acusativo sing. (5ª) · objeto'), ('dat', 'verbo · "dá"')],
    'Lendo em ordem: <i>Rēx exercituī spem dat</i> = O rei dá esperança ao exército.')}
<p><i>Rēx</i> é nominativo singular (o genitivo seria <i>rēgis</i>): o sujeito. <i>Exercituī</i> tem o <i>u</i> do tema da quarta declinação e a terminação <i>-ī</i> do dativo, que você viu na terceira (<i>rēgī</i>): "ao exército". <i>Spem</i> tem o <i>-m</i> de todo acusativo singular e o <i>e</i> da quinta: o objeto, "esperança". O verbo <i>dat</i>, singular, confirma <i>rēx</i> como sujeito.</p>
<h3>Procedimento: de que declinação é esta palavra?</h3>
<p>Diante de uma entrada de dicionário, siga estes passos, sempre nesta ordem:</p>
<ol>
<li><b>Leia o genitivo</b>, a segunda forma da entrada. Ignore, por enquanto, o nominativo.</li>
<li><b>Compare com o quadro</b>: <i>-ae</i> → 1ª; <i>-ī</i> → 2ª; <i>-is</i> → 3ª; <i>-ūs</i> → 4ª; <i>-ēī</i> ou <i>-eī</i> → 5ª. Muitos dicionários abreviam o genitivo (<i>frūctus, -ūs</i>); nos que não marcam macrons, <i>fructus, -us</i> (4ª) se distingue de <i>dominus, -i</i> (2ª) justamente por essa abreviatura.</li>
<li><b>Desconfie do nominativo.</b> Nominativos em <i>-us</i> existem na 2ª (<i>lupus, -ī</i>), na 3ª (<i>corpus, corporis</i>; <i>virtūs, virtūtis</i>) e na 4ª (<i>frūctus, -ūs</i>); nominativos em <i>-ēs</i>, na 3ª (<i>mīles, mīlitis</i>; <i>nūbēs, nūbis</i>, nuvem, Bennett § 40.1.a) e na 5ª (<i>rēs, reī</i>).</li>
<li><b>Leia o gênero</b>, a abreviatura <i>m.</i>, <i>f.</i> ou <i>n.</i>: ele decide o adjetivo e, nos neutros, as formas iguais do nominativo e do acusativo. Atenção às exceções que este capítulo mostrou: <i>manus</i> e <i>domus</i> femininas, <i>diēs</i> masculino.</li>
<li><b>Ache o tema e aplique o modelo.</b> Na 3ª declinação, verifique também se é tema em <i>-i</i> (genitivo plural em <i>-ium</i>, capítulo 10).</li>
</ol>
'''),
        ('Análise gramatical: uma frase autêntica', f'''
<p>No Evangelho de Lucas, na Vulgata, as últimas palavras de Jesus na cruz contêm dois nomes da quarta declinação, um no plural e outro no singular, cada um com um possessivo que concorda com ele:</p>
{exemplos([('Pater, in manūs tuās commendō spīritum meum.', 'Pai, em tuas mãos entrego o meu espírito. (Lc 23,46, Vulgata Clementina)')])}
<p>Antes da análise, duas palavras novas. <i>Commendō, -āre</i> (1ª conjugação) é "confiar, entregar aos cuidados de alguém"; aqui está na 1ª pessoa do singular do presente, "eu entrego". <i>Tuus, -a, -um</i> ("teu") e <i>meus, -a, -um</i> ("meu") são os <b>possessivos</b>, que você estudará no capítulo 14; por ora basta saber que se declinam exatamente como <i>bonus</i> e concordam com o nome a que se referem.</p>
{analise('Lc 23,46, palavra a palavra', [
    ('Pater', 'pater, patris (m.), pai', 'vocativo singular, 3ª declinação (igual ao nominativo)', 'invocação: a quem se fala'),
    ('in', 'in (preposição)', 'aqui com acusativo', 'direção: "em, para dentro de"'),
    ('manūs', 'manus, -ūs (f.), mão', 'acusativo plural, 4ª declinação', 'complemento de <i>in</i>: "nas mãos" (para dentro delas)'),
    ('tuās', 'tuus, -a, -um, teu', 'acusativo plural feminino', 'concorda com <i>manūs</i>'),
    ('commendō', 'commendō, -āre (1ª), confiar, entregar', '1ª pessoa do singular, presente', 'verbo: "entrego"; o sujeito "eu" está na desinência'),
    ('spīritum', 'spīritus, -ūs (m.), sopro, espírito', 'acusativo singular, 4ª declinação', 'objeto direto de <i>commendō</i>'),
    ('meum', 'meus, -a, -um, meu', 'acusativo singular masculino', 'concorda com <i>spīritum</i>'),
])}
<p>Três pontos deste capítulo aparecem aqui. Primeiro, a ambiguidade de <i>-ūs</i>: sozinho, <i>manūs</i> poderia ser genitivo singular ou nominativo, acusativo ou vocativo plural. A preposição <i>in</i> exclui o genitivo e o nominativo, e o possessivo <i>tuās</i>, que só pode ser acusativo plural, fecha a questão. Segundo, o gênero: <i>tuās</i> está no <b>feminino</b>, e é ele que mostra, numa frase autêntica, que <i>manus</i> é feminino apesar do <i>-us</i>; se fosse masculino, teríamos <i>tuōs</i>. Terceiro, a comparação entre os dois nomes da quarta: <i>manūs</i> (plural, feminino) e <i>spīritum</i> (singular, masculino) pertencem à mesma declinação, mas os adjetivos que os acompanham têm formas bem diferentes (<i>tuās</i>, <i>meum</i>), porque concordam em gênero, número e caso, não em terminação. Note também a ordem: o latim põe o lugar (<i>in manūs tuās</i>) antes do verbo e do objeto, dando-lhe destaque; o português pode conservá-la.</p>
<p>No Evangelho de Mateus, o fim do capítulo 6 traz uma frase curta com um nome da quinta declinação. Você já consegue lê-la: <i>sufficit</i>, de <i>sufficiō, -ere</i> (3ª em <i>-iō</i>), é "basta"; <i>malitia, -ae</i> é "maldade, mal"; <i>sua</i> é o possessivo "seu", que concorda com <i>malitia</i>.</p>
{exemplos([('Sufficit diēī malitia sua.', 'Basta ao dia o seu (próprio) mal. (Mt 6,34, Vulgata Clementina; <i>diēī</i>: dativo singular de <i>diēs</i>, com <i>ē</i> longo porque vem depois de vogal; <i>malitia</i>: nominativo, sujeito de <i>sufficit</i>)')])}
<p>Repare que <i>diēī</i> poderia ser genitivo ou dativo: as duas formas são iguais na quinta declinação. O verbo decide: "bastar" pede a pessoa ou coisa <b>para quem</b> algo basta, que vai em dativo. "A cada dia basta o seu mal" é o sentido; a tradução literal mostra a função.</p>
<h3>Resumo</h3>
<ul>
<li>4ª declinação: genitivo em <i>-ūs</i>. Masculino e feminino: <i>-us, -ūs, -uī, -um, -us, -ū</i> / <i>-ūs, -uum, -ibus, -ūs, -ūs, -ibus</i>. Neutro: <i>-ū, -ūs, -ū, -ū, -ū, -ū</i> / <i>-ua, -uum, -ibus, -ua, -ua, -ibus</i>.</li>
<li>Quase todos os nomes em <i>-us</i> da 4ª são masculinos; <i>manus</i> e <i>domus</i> são femininos (<i>manus bona</i>).</li>
<li><i>Domus</i> mistura formas da 4ª e da 2ª; sem preposição, <i>domī</i> = em casa, <i>domum</i> = para casa, <i>domō</i> = de casa.</li>
<li>5ª declinação: genitivo em <i>-ēī</i> (depois de vogal) ou <i>-eī</i> (depois de consoante). <i>-ēs, -ēī, -ēī, -em, -ēs, -ē</i> / <i>-ēs, -ērum, -ēbus, -ēs, -ēs, -ēbus</i>. Feminina, exceto <i>diēs</i> (normalmente masculino).</li>
<li>Só <i>diēs</i> e <i>rēs</i> têm o plural completo; <i>spēs</i> só tem <i>spēs</i> no plural; <i>fidēs</i> fica no singular.</li>
<li><i>Rēs</i> se traduz pelo contexto: <i>rēs pūblica</i>, o Estado; <i>rēs gestae</i>, os feitos; <i>rēs novae</i>, revolução.</li>
<li>Em todas as declinações: dativo = ablativo plural; vocativo = nominativo (exceto <i>-us</i> da 2ª); neutros com N = Ac = V e plural em <i>-a</i>; na 3ª, 4ª e 5ª, acusativo plural = nominativo plural. A declinação se identifica pelo genitivo singular.</li>
</ul>
<p>Com as cinco declinações completas, o próximo passo da gramática nominal são os pronomes (capítulos 14 a 17) e os usos dos casos (capítulos 20 e 21). No capítulo seguinte, o 12, a atenção volta ao verbo, com o imperfeito e o futuro.</p>
'''),
    ],
    erros_comuns=[
        ('Declinar um nome da 4ª como se fosse da 2ª: *<i>frūctī</i>, *<i>exercitōs</i>, *<i>senātō</i>.', 'O nominativo em <i>-us</i> engana; o genitivo do dicionário, não. <i>Frūctus, -ūs</i> é da quarta: genitivo <i>frūctūs</i>, acusativo plural <i>frūctūs</i>, dativo <i>senātuī</i>. Antes de declinar qualquer nome em <i>-us</i>, confira se o genitivo é <i>-ī</i> (2ª), <i>-ūs</i> (4ª) ou <i>-oris/-eris</i> (3ª).'),
        ('Fazer masculino o adjetivo de <i>manus</i> e <i>domus</i>: *<i>manus bonus</i>, *<i>domus magnus</i>.', 'São femininos da quarta declinação, apesar do <i>-us</i>: <i>manus bona</i>, <i>domus magna</i>, <i>in manūs tuās</i>. O adjetivo copia o gênero do nome, que vem do dicionário (<i>manus, -ūs, f.</i>), não da terminação.'),
        ('Ler <i>manūs</i> ou <i>exercitūs</i> sempre como nominativo singular.', 'Com <i>u</i> longo, <i>-ūs</i> é genitivo singular ou nominativo, acusativo e vocativo plural, nunca nominativo singular (que tem <i>u</i> breve). Nos textos sem macrons, considere todas as leituras e deixe o verbo, a preposição e o adjetivo decidir: <i>exercitūs ducis</i> pode ser "os exércitos do general" (com verbo no plural) ou, junto de outro nome, "do exército".'),
        ('Usar preposição com <i>domus</i> no sentido de "lar": *<i>in domō manet</i>, *<i>ad domum venit</i>.', '"Em casa" é <i>domī</i>, "para casa" é <i>domum</i>, "de casa" é <i>domō</i>, sem preposição, como os nomes de cidade. A preposição volta quando <i>domus</i> é o edifício, sobretudo com adjetivo: <i>in domum magnam</i>, "para dentro de uma casa grande".'),
        ('Traduzir <i>rēs</i> sempre por "coisa": "a coisa pública", "as coisas feitas", "coisas novas".', '<i>Rēs</i> é a palavra mais vaga do latim e ganha sentido no contexto e nas expressões fixas: <i>rēs pūblica</i>, o Estado; <i>rēs gestae</i>, os feitos; <i>rēs novae</i>, revolução; <i>rēs adversae</i>, a adversidade. Identifique a forma, depois procure a expressão inteira no dicionário.'),
        ('Confundir <i>-ēs</i> da 5ª com <i>-ēs</i> da 3ª, e <i>reī</i> com <i>rēgī</i>.', '<i>Rēs</i> (5ª) e <i>rēgēs</i> (3ª, plural de <i>rēx</i>) terminam ambos em <i>-ēs</i>, mas são palavras diferentes; <i>reī</i> é genitivo ou dativo de <i>rēs</i>, <i>rēgī</i> é dativo de <i>rēx</i>. Volte ao dicionário: <i>rēs, reī</i> × <i>rēx, rēgis</i>. O mesmo vale para <i>nūbēs, nūbis</i> (3ª), que não é da quinta apesar do nominativo em <i>-ēs</i>.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · As várias leituras de -ūs',
            'Leia em voz alta e analise, na ordem latina: <i lang="la">Senātus exercituī frūctūs agrōrum dat.</i> Vocabulário: <i>senātus, -ūs</i> (m.), senado; <i>exercitus, -ūs</i> (m.), exército; <i>frūctus, -ūs</i> (m.), fruto; <i>ager, agrī</i> (m.), campo; <i>dat</i>, dá.', [
            ('Qual é o verbo, e o que ele faz esperar?', '<i>Dat</i>, "dá", 3ª pessoa do singular. Espera-se um sujeito singular, o que é dado (acusativo) e a quem se dá (dativo).'),
            ('Que formas <i>senātus</i> pode ter?', 'Com <i>u</i> breve, só nominativo ou vocativo singular. (Se fosse <i>senātūs</i>, com <i>u</i> longo, poderia ser genitivo singular ou nominativo e acusativo plural.) O verbo é singular e ninguém é chamado: é o sujeito, "o senado".'),
            ('E <i>exercituī</i>?', 'O <i>u</i> antes da terminação denuncia a quarta declinação, e <i>-uī</i> é o dativo singular: "ao exército". É o destinatário que <i>dat</i> fazia esperar.'),
            ('<i>Frūctūs</i>: que caso?', 'Pode ser genitivo singular ou nominativo, acusativo e vocativo plural. O sujeito já está ocupado por <i>senātus</i>, e nenhum genitivo singular faria sentido ligado aos outros nomes; falta o objeto de <i>dat</i>: acusativo plural, "os frutos".'),
            ('<i>Agrōrum</i>?', 'Genitivo plural da 2ª declinação (<i>ager, agrī</i>): "dos campos". Liga-se ao nome mais próximo que admite um complemento: <i>frūctūs agrōrum</i>, "os frutos dos campos".'),
            ('Monte a tradução.', '"O senado dá ao exército os frutos dos campos."'),
        ], 'Conclusão: a mesma terminação <i>-ūs</i> tem quatro leituras possíveis; o verbo e as funções já ocupadas eliminam três.'),
        pratica_guiada('Prática guiada 2 · Rēs pūblica e a quinta declinação',
            'Analise e traduza: <i lang="la">Rēs pūblica spem in fidē mīlitum habet.</i> Vocabulário: <i>rēs pūblica</i>, o Estado; <i>spēs, speī</i> (f.), esperança; <i>fidēs, fideī</i> (f.), lealdade; <i>mīles, mīlitis</i> (m.), soldado; <i>habet</i>, tem, deposita.', [
            ('Qual é o sujeito? Pode <i>rēs</i> ser plural?', '<i>Rēs</i> sozinho poderia ser nominativo singular ou nominativo e acusativo plural, mas <i>pūblica</i>, que concorda com ele, só pode ser nominativo (ou vocativo) singular feminino. E o verbo <i>habet</i> é singular. Sujeito: <i>rēs pūblica</i>, "o Estado".'),
            ('Que forma é <i>spem</i>?', 'Acusativo singular de <i>spēs</i>: o <i>-m</i> de todo acusativo singular, com o <i>e</i> breve da quinta. Objeto de <i>habet</i>: "tem esperança".'),
            ('E <i>in fidē</i>?', '<i>Fidē</i> é ablativo singular da quinta declinação (<i>ē</i> longo); <i>in</i> + ablativo indica onde algo está: "na lealdade". Não é vocativo da 2ª nem ablativo da 3ª: o dicionário dá <i>fidēs, fideī</i>.'),
            ('<i>Mīlitum</i>?', 'Genitivo plural da 3ª declinação (<i>mīles, mīlitis</i>): "dos soldados", ligado a <i>fidē</i>.'),
            ('Monte a tradução.', '"O Estado tem esperança na lealdade dos soldados", ou, mais natural, "O Estado deposita a sua esperança na lealdade dos soldados."'),
        ]),
    ],
    exercicios=[
        exercicio('Exercício 1 · Qual é a declinação?', 'Para cada entrada de dicionário, diga a declinação e o que a revela. Atenção ao nominativo, que pode enganar.', [
            ('<i>exercitus, -ūs</i> (m.), exército', '4ª declinação: o genitivo em <i>-ūs</i>. O nominativo em <i>-us</i> não decide nada.'),
            ('<i>corpus, corporis</i> (n.), corpo', '3ª declinação: o genitivo em <i>-is</i>. É neutro, por isso o nominativo serve também de acusativo.'),
            ('<i>faciēs, faciēī</i> (f.), rosto', '5ª declinação: genitivo em <i>-ēī</i>, com <i>ē</i> longo porque vem depois de vogal.'),
            ('<i>virtūs, virtūtis</i> (f.), coragem', '3ª declinação: o genitivo em <i>-is</i>. O nominativo em <i>-ūs</i> longo parece um genitivo da 4ª, mas é só a forma de dicionário de um tema em dental (capítulo 9).'),
            ('<i>genū, -ūs</i> (n.), joelho', '4ª declinação, neutro: genitivo em <i>-ūs</i>, nominativo em <i>-ū</i>.'),
            ('<i>nūbēs, nūbis</i> (f.), nuvem', '3ª declinação: o genitivo em <i>-is</i>. O nominativo em <i>-ēs</i> lembra a 5ª, mas o genitivo da 5ª seria <i>-ēī</i> ou <i>-eī</i>.'),
            ('<i>spēs, speī</i> (f.), esperança', '5ª declinação: genitivo em <i>-eī</i>, com <i>e</i> breve depois de consoante.'),
            ('<i>agricola, -ae</i> (m.), agricultor', '1ª declinação: genitivo em <i>-ae</i>. É masculino por designar homens, mas a declinação não muda.'),
            ('<i>dominus, -ī</i> (m.), senhor', '2ª declinação: genitivo em <i>-ī</i>.'),
            ('<i>portus, -ūs</i> (m.), porto', '4ª declinação: genitivo em <i>-ūs</i>.'),
        ]),
        exercicio('Exercício 2 · Caso e número', 'Dê o caso e o número de cada forma (todas as possibilidades) e o nominativo de dicionário.', [
            ('<i>frūctuum</i>', 'Genitivo plural de <i>frūctus, -ūs</i>: "dos frutos". O <i>-uum</i> só existe na 4ª.'),
            ('<i>manū</i>', 'Ablativo singular de <i>manus, -ūs</i> (f.); mais raramente, dativo singular contraído (por <i>manuī</i>).'),
            ('<i>cornua</i>', 'Nominativo, acusativo ou vocativo plural de <i>cornū, -ūs</i> (n.).'),
            ('<i>reī</i>', 'Genitivo ou dativo singular de <i>rēs, reī</i> (f.).'),
            ('<i>diēbus</i>', 'Dativo ou ablativo plural de <i>diēs, diēī</i>.'),
            ('<i>exercitūs</i>', 'Genitivo singular, ou nominativo, acusativo ou vocativo plural de <i>exercitus, -ūs</i>.'),
            ('<i>spem</i>', 'Acusativo singular de <i>spēs, speī</i> (f.).'),
            ('<i>domī</i>', 'Locativo de <i>domus</i>: "em casa". (O genitivo de <i>domus</i> é <i>domūs</i>; <i>domī</i> como genitivo só ocorre em Plauto.)'),
            ('<i>rē</i>', 'Ablativo singular de <i>rēs</i>.'),
            ('<i>portibus</i>', 'Dativo ou ablativo plural de <i>portus, -ūs</i> (que admite também <i>portubus</i>).'),
            ('<i>senātum</i>', 'Acusativo singular de <i>senātus, -ūs</i> (m.). Não é genitivo plural: esse seria <i>senātuum</i>.'),
            ('<i>diē</i>', 'Ablativo singular de <i>diēs</i>.'),
        ]),
        exercicio('Exercício 3 · Decline com o adjetivo', 'Decline nome e adjetivo juntos, em voz alta e por escrito.', [
            ('<i>exercitus magnus</i> (<i>exercitus, -ūs</i>, m.), "o grande exército"', 'Singular: exercitus magnus, exercitūs magnī, exercituī magnō, exercitum magnum, exercitus magne, exercitū magnō. Plural: exercitūs magnī, exercituum magnōrum, exercitibus magnīs, exercitūs magnōs, exercitūs magnī, exercitibus magnīs. No vocativo singular, o nome fica igual ao nominativo e só o adjetivo muda para <i>-e</i>.'),
            ('<i>diēs longus</i> (<i>diēs, diēī</i>, m.), "o dia longo"', 'Singular: diēs longus, diēī longī, diēī longō, diem longum, diēs longe, diē longō. Plural: diēs longī, diērum longōrum, diēbus longīs, diēs longōs, diēs longī, diēbus longīs. O adjetivo é masculino porque <i>diēs</i>, no sentido de "dia", é masculino.'),
            ('<i>rēs pūblica</i> (f.), só no singular', 'rēs pūblica, reī pūblicae, reī pūblicae, rem pūblicam, rēs pūblica, rē pūblicā. As duas palavras se declinam, cada uma pela sua declinação (5ª e 1ª).'),
            ('<i>cornū longum</i> (<i>cornū, -ūs</i>, n.), "o chifre longo"', 'Singular: cornū longum, cornūs longī, cornū longō, cornū longum, cornū longum, cornū longō. Plural: cornua longa, cornuum longōrum, cornibus longīs, cornua longa, cornua longa, cornibus longīs. Neutro: nominativo, acusativo e vocativo iguais, no nome e no adjetivo.'),
        ]),
        exercicio('Exercício 4 · Passe para o plural', 'Passe sujeito, predicativo, objeto e verbo para o plural, e explique as mudanças. Vocabulário: <i>parvus, -a, -um</i>, pequeno; <i>videt · vident</i>, vê · veem.', [
            ('<i>Exercitus portum videt.</i>', '<i>Exercitūs portūs vident.</i> Na 4ª, o nominativo e o acusativo plural são iguais (<i>-ūs</i>); quem distingue sujeito e objeto é a ordem e o sentido. "Os exércitos veem os portos."'),
            ('<i>Rēs nova est.</i>', '<i>Rēs novae sunt.</i> O nome não muda (<i>rēs</i> serve aos dois números); o adjetivo e o verbo mostram o plural.'),
            ('<i>Diēs longus est.</i>', '<i>Diēs longī sunt.</i> Adjetivo masculino plural, porque <i>diēs</i> é masculino.'),
            ('<i>Manus puellae parva est.</i>', '<i>Manūs puellārum parvae sunt.</i> "As mãos das meninas são pequenas." O adjetivo é feminino porque <i>manus</i> é feminino.'),
            ('<i>Fidēs servī magna est.</i>', '<i>Fidēs</i> não se usa no plural (Kennedy § 57). Passa-se só o que pode ir para o plural: <i>Fidēs servōrum magna est</i>, "A lealdade dos escravos é grande". Reconhecer esse limite faz parte da resposta.'),
        ]),
        exercicio('Exercício 5 · Traduza lendo em ordem', 'Anote caso e número de cada palavra antes de traduzir. Vocabulário: <i>manent</i>, ficam; <i>venit · veniunt</i>, vem · vêm; <i>fugiunt</i>, fogem; <i>regit</i>, governa; <i>rēs gestae</i>, os feitos; <i>nārrat</i>, narra; <i>portat</i>, carrega; <i>timent</i>, temem.', [
            ('<i>Puerī domī manent; pater domum venit.</i>', '<i>Domī</i>, locativo, "em casa"; <i>domum</i>, acusativo sem preposição, "para casa": Os meninos ficam em casa; o pai vem para casa.'),
            ('<i>Servī domō in silvam fugiunt.</i>', '<i>Domō</i>, ablativo sem preposição, "de casa"; <i>in silvam</i>, acusativo com <i>in</i>, direção: Os escravos fogem de casa para a floresta.'),
            ('<i>Senātus rem pūblicam regit.</i>', '<i>Senātus</i> nominativo (4ª); <i>rem pūblicam</i> acusativo, objeto: O senado governa o Estado.'),
            ('<i>Poēta rēs gestās ducis nārrat.</i>', '<i>Rēs gestās</i> acusativo plural (o adjetivo em <i>-ās</i> exclui o nominativo); <i>ducis</i> genitivo da 3ª: O poeta narra os feitos do general.'),
            ('<i>Agricola frūctūs agrī in manibus portat.</i>', '<i>Frūctūs</i> acusativo plural (o sujeito é <i>agricola</i>); <i>agrī</i> genitivo singular da 2ª; <i>in manibus</i>, ablativo plural da 4ª com <i>in</i>, lugar onde: O agricultor carrega nas mãos os frutos do campo.'),
            ('<i>Hominēs exercitūs rēgis timent.</i>', 'Ambiguidade real: <i>exercitūs</i> pode ser acusativo plural (objeto: "Os homens temem os exércitos do rei") ou genitivo singular (e então faltaria o objeto). Como <i>timent</i> pede objeto e não há outro acusativo, a leitura é: Os homens temem os exércitos do rei. Com macrons ou sem eles, é a estrutura da frase que decide.'),
        ]),
        exercicio('Exercício 6 · Do português para o latim', 'Traduza, usando o vocabulário do capítulo e verbos no presente. Vocabulário: <i>videt</i>, vê; <i>est · sunt</i>, é, está · são, estão; <i>laudat</i>, elogia; <i>veniunt</i>, vêm.', [
            ('O exército vê o lago.', '<i>Exercitus lacum videt.</i> <i>Lacum</i>: acusativo singular da 4ª, como <i>manum</i>.'),
            ('A esperança dos soldados é grande.', '<i>Spēs mīlitum magna est.</i> <i>Spēs</i> é feminino: o predicativo vai para <i>magna</i>.'),
            ('O senado elogia os feitos do rei.', '<i>Senātus rēs gestās rēgis laudat.</i> <i>Rēs gestās</i>: acusativo plural feminino, expressão fixa.'),
            ('As meninas estão em casa.', '<i>Puellae domī sunt.</i> "Em casa" é o locativo <i>domī</i>, sem preposição.'),
            ('Os soldados vêm para casa.', '<i>Mīlitēs domum veniunt.</i> "Para casa" é <i>domum</i>, sem preposição.'),
            ('A mão do menino é pequena.', '<i>Manus puerī parva est.</i> <i>Parva</i>, feminino, porque <i>manus</i> é feminino.'),
        ]),
    ],
    leituras=['d-ooge-latin-for-beginners', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'lhomond-epitome-historiae-sacrae', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'ravizza-gramatica-latina', 'short-a-latin-dictionary-lewis-short'],
    leituras_nota='Latin for Beginners, de D\'Ooge, traz exercícios graduados sobre a quarta e a quinta declinações, bons para fixar os paradigmas deste capítulo. Em Familia Romana, de Ørberg, nomes como manus, domus, rēs e diēs aparecem com frequência; ao encontrá-los, identifique o caso pelo quadro da seção 5. O Epitome Historiae Sacrae, de Lhomond, em frases curtas, é um bom lugar para reconhecer as cinco declinações misturadas. Na Vulgata, leia Lc 23,44–46 e Mt 6,25–34, procurando os nomes da quarta e da quinta declinações. Ravizza (n. 37–41) serve para consultar os paradigmas em português, e o verbete rēs de Lewis e Short mostra a variedade de sentidos da palavra.',
)
