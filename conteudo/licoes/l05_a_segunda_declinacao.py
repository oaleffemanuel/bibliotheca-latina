from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='05-a-segunda-declinacao', titulo='A segunda declinação e os adjetivos de primeira classe', titulo_latim='Dē secundā dēclīnātiōne', tempo='60 min',
    resumo='A segunda família de nomes do latim (dominus, puer, ager, bellum), o vocativo em -e e em -ī, a regra dos neutros e os adjetivos de primeira classe (bonus, pulcher, līber), com a concordância em gênero, número e caso, a posição do adjetivo e uma frase do Evangelho analisada palavra a palavra.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['2ª declinação', 'masculinos em -us', 'nomes em -er e -ir', 'neutros em -um', 'vocativo em -e e em -ī', 'genitivo de -ius/-ium', 'gênero na 2ª declinação', 'adjetivos de primeira classe', 'concordância nominal', 'posição do adjetivo', 'adjetivos substantivados', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulos 3 e 4: os seis casos, a primeira declinação completa (inclusive os masculinos como nauta) e as preposições com acusativo e com ablativo.', licoes=['03-introducao-aos-casos', '04-a-primeira-declinacao']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 15 (gênero pela significação), § 19 (formas iguais; regra dos neutros), §§ 23–26 (2ª declinação: hortus, bellum, puer, ager, vir; -ius/-ium; deus; exceções de gênero), §§ 62–65 (adjetivos de 1ª e 2ª declinação: bonus, tener, sacer), § 234 (concordância), §§ 236–237 (adjetivos substantivados), § 350.4 (posição do adjetivo)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§§ 45–48 (tema em -o, paradigmas e gênero), § 49 (genitivo e vocativo de -ius; deus), §§ 50–51 (nomes em -er que mantêm ou perdem o e), §§ 110–112 (adjetivos bonus, miser, niger/pulcher), §§ 285–286 (adjetivo atributivo e predicativo; concordância)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='nn. 22–24 (segunda declinação: dominus, fīlius, magister, puer, vir, templum; vocativo dos nomes em -ius), nn. 51–52 (adjetivos de primeira classe: bonus, pulcher, līber)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 35 (segunda declinação: annus, puer, magister, bellum; gênero), § 71 (adjetivos de três terminações em -us, -a, -um e -er, -a, -um)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Mateus 12,35 e 7,17', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', nota='frase analisada na seção 6 (Mt 12,35) e leitura do exercício 5 (Mt 7,17), conferidas em la.wikisource.org, "Vulgata Clementina/Evangelium Secundum Matthaeum"; macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Declinar nomes da segunda declinação em <i>-us</i>, <i>-er</i>/<i>-ir</i> e <i>-um</i>, distinguindo pelo genitivo do dicionário os que conservam o <i>e</i> (<i>puer, puerī</i>) dos que o perdem (<i>ager, agrī</i>).',
        'Formar o vocativo em <i>-e</i> (<i>Mārce</i>) e em <i>-ī</i> (<i>fīlī, Iūlī</i>) e reconhecer o genitivo em <i>-ī</i> ou <i>-iī</i> dos nomes em <i>-ius</i> e <i>-ium</i>.',
        'Aplicar a regra dos neutros (nominativo = acusativo; plural em <i>-a</i>) para não confundir <i>bella</i> e <i>dōna</i> com femininos singulares.',
        'Declinar os adjetivos de primeira classe (<i>bonus, -a, -um</i>; <i>pulcher, -chra, -chrum</i>; <i>līber, -era, -erum</i>) e fazê-los concordar em gênero, número e caso, inclusive com masculinos da primeira declinação (<i>nauta bonus</i>).',
        'Usar a concordância para resolver formas ambíguas e analisar palavra a palavra uma frase autêntica da Vulgata.',
    ],
    secoes=[
        ('A família de dominus: os masculinos em -us', f'''
<p>No capítulo 4 você viu que uma declinação se reconhece pelo <b>genitivo singular</b>: <i>-ae</i> é a primeira. A <b>segunda declinação</b> reúne os nomes cujo genitivo singular termina em <b><i>-ī</i></b>. É por isso que o dicionário os registra em pares como <i>dominus, -ī</i>; <i>puer, -ī</i>; <i>ager, agrī</i>; <i>bellum, -ī</i>. O nominativo varia (<i>-us</i>, <i>-er</i>, <i>-ir</i>, <i>-um</i>), mas o genitivo é sempre <i>-ī</i>, e é ele que diz qual jogo de terminações usar. O grupo mais numeroso é o dos masculinos em <i>-us</i>, como <i>dominus</i>, "senhor".</p>
{tabela_declinacao('Segunda declinação, masculinos em -us: dominus, -ī (m.), "senhor"', [
    ('domin<b>us</b>', 'domin<b>ī</b>'), ('domin<b>ī</b>', 'domin<b>ōrum</b>'), ('domin<b>ō</b>', 'domin<b>īs</b>'),
    ('domin<b>um</b>', 'domin<b>ōs</b>'), ('domin<b>e</b>', 'domin<b>ī</b>'), ('domin<b>ō</b>', 'domin<b>īs</b>')])}
<p>Compare com <i>rosa</i> e você verá um parentesco: o genitivo plural <i>-ōrum</i> corresponde a <i>-ārum</i>, o acusativo plural <i>-ōs</i> a <i>-ās</i>, o dativo e ablativo plural <i>-īs</i> são idênticos nas duas declinações. A vogal característica da primeira é o <i>a</i>; a da segunda é o <i>o</i>, que no nominativo e no acusativo singular se enfraqueceu em <i>u</i> (o latim antigo dizia <i>dominos</i>, <i>dominom</i>). Por isso os gramáticos chamam esta família de "temas em <i>-o</i>". Recite em voz alta, como no capítulo anterior: <i>dominus, dominī, dominō, dominum, domine, dominō; dominī, dominōrum, dominīs, dominōs, dominī, dominīs</i>.</p>
<h3>O vocativo em -e, e os nomes em -ius</h3>
<p>Aqui aparece a única exceção à regra "vocativo = nominativo" que você conheceu no capítulo 3: os nomes em <i>-us</i> fazem o vocativo singular em <b><i>-e</i></b>. O motivo é histórico: o tema terminava numa vogal que alternava entre <i>o</i> e <i>e</i>, e o vocativo conservou a variante em <i>e</i>. Assim, <i>Mārcus</i> → <i>Mārce</i>, <i>amīcus</i> → <i>amīce</i>, <i>dominus</i> → <i>domine</i>. Os nomes próprios em <b><i>-ius</i></b> e o comum <i>fīlius</i> contraem o vocativo em <b><i>-ī</i></b>: <i>Iūlius</i> → <i>Iūlī</i>, <i>Cornēlius</i> → <i>Cornēlī</i>, <i>fīlius</i> → <i>fīlī</i>.</p>
{exemplos([('Salvē, Mārc<b>e</b>!', 'Olá, Marco! (vocativo de <i>Mārcus</i>)'), ('Domin<b>e</b>, servus in hortō est.', 'Senhor, o escravo está no jardim.'), ('Iūl<b>ī</b>, Mārcus in viā est.', 'Júlio, Marco está na rua. (vocativo de <i>Iūlius</i>)'), ('Fīl<b>ī</b>, magister puerōs vocat.', 'Filho, o professor está chamando os meninos.')])}
<p>Os nomes em <i>-ius</i> e <i>-ium</i> têm ainda uma particularidade no <b>genitivo singular</b>. Até a época de Augusto, ele se escrevia com um só <i>-ī</i>: <i>fīlī</i> ("do filho"), <i>cōnsilī</i> ("do conselho"); depois, generalizou-se a forma com <i>-iī</i>: <i>fīliī</i>, <i>cōnsiliī</i>. Os dicionários e este livro usam <i>-iī</i>, mas em Cícero você encontrará <i>-ī</i>; são a mesma forma, e o contexto (um nome do qual o genitivo depende) mostra que não se trata de vocativo.</p>
{tabela_declinacao('fīlius, -ī (m.), "filho"', [
    ('fīli<b>us</b>', 'fīli<b>ī</b>'), ('fīli<b>ī</b> (antigo fīl<b>ī</b>)', 'fīli<b>ōrum</b>'), ('fīli<b>ō</b>', 'fīli<b>īs</b>'),
    ('fīli<b>um</b>', 'fīli<b>ōs</b>'), ('fīl<b>ī</b>', 'fīli<b>ī</b>'), ('fīli<b>ō</b>', 'fīli<b>īs</b>')])}
<h3>O gênero</h3>
<p>Os nomes em <i>-us</i> e em <i>-er</i>/<i>-ir</i> são <b>masculinos</b>; os em <i>-um</i> são <b>neutros</b>. As exceções são poucas e quase todas previsíveis pelo sentido: são femininos os nomes de <b>árvores</b> e muitos nomes de <b>cidades, ilhas e países</b> em <i>-us</i> (<i>Corinthus</i>, <i>Rhodus</i>, <i>Aegyptus</i>), além de alguns nomes isolados como <i>humus</i>, "chão". Três nomes em <i>-us</i> são neutros: <i>vulgus</i> (multidão), <i>vīrus</i> (veneno), <i>pelagus</i> (mar). Você não precisa decorá-los agora; precisa só lembrar o caso de <i>nauta</i>: o gênero vem do dicionário, não da terminação, e se revela no adjetivo.</p>
{observacao('Deus', 'O nome <i>deus, -ī</i> segue <i>dominus</i> no singular, mas não tem vocativo clássico; na Vulgata, o vocativo é igual ao nominativo (<i>Deus</i>). No plural, ao lado das formas regulares <i>deī, deīs</i>, são mais comuns <i>dī</i> (nominativo e vocativo) e <i>dīs</i> (dativo e ablativo). No capítulo 4 você viu <i>deābus et deīs</i>: as duas formas existem.')}
'''),
        ('Os nomes em -er e -ir: puer, ager, vir', f'''
<p>Alguns masculinos da segunda declinação não têm terminação no nominativo singular: terminam em <i>-er</i> (<i>puer</i>, "menino"; <i>ager</i>, "campo") ou em <i>-ir</i> (<i>vir</i>, "homem, varão", o único, com seus compostos). A partir do genitivo, recebem as mesmas terminações de <i>dominus</i>. O vocativo é igual ao nominativo: <i>puer!</i>, "menino!".</p>
<p>A questão é o <i>e</i>. Em <i>puer</i>, ele faz parte do tema e fica em todas as formas: <i>puer, puerī, puerō</i>. Em <i>ager</i>, o tema é <i>agr-</i>; o <i>e</i> só aparece no nominativo e vocativo singular, para tornar a palavra pronunciável (um nominativo <i>agr</i> não seria possível), e desaparece no resto: <i>ager, agrī, agrō</i>. Como saber? <b>Pelo genitivo do dicionário</b>: <i>puer, puerī</i>, mas <i>ager, agrī</i>. Por isso o genitivo se aprende junto com o nominativo, sempre.</p>
{tabela_declinacao('puer, puerī (m.), "menino" · ager, agrī (m.), "campo" · vir, virī (m.), "homem"', [
    ('puer', 'puer<b>ī</b>', 'ager', 'agr<b>ī</b>', 'vir', 'vir<b>ī</b>'),
    ('puer<b>ī</b>', 'puer<b>ōrum</b>', 'agr<b>ī</b>', 'agr<b>ōrum</b>', 'vir<b>ī</b>', 'vir<b>ōrum</b>'),
    ('puer<b>ō</b>', 'puer<b>īs</b>', 'agr<b>ō</b>', 'agr<b>īs</b>', 'vir<b>ō</b>', 'vir<b>īs</b>'),
    ('puer<b>um</b>', 'puer<b>ōs</b>', 'agr<b>um</b>', 'agr<b>ōs</b>', 'vir<b>um</b>', 'vir<b>ōs</b>'),
    ('puer', 'puer<b>ī</b>', 'ager', 'agr<b>ī</b>', 'vir', 'vir<b>ī</b>'),
    ('puer<b>ō</b>', 'puer<b>īs</b>', 'agr<b>ō</b>', 'agr<b>īs</b>', 'vir<b>ō</b>', 'vir<b>īs</b>')],
    colunas=('puer · sing.', 'puer · pl.', 'ager · sing.', 'ager · pl.', 'vir · sing.', 'vir · pl.'))}
<p>A maioria dos nomes em <i>-er</i> segue <i>ager</i>: <i>magister, magistrī</i> (mestre, professor), <i>liber, librī</i> (livro). Conservam o <i>e</i>, como <i>puer</i>, poucos nomes: <i>gener</i> (genro), <i>socer</i> (sogro), <i>vesper</i> (tarde) e os compostos em <i>-fer</i> e <i>-ger</i> (<i>armiger</i>, escudeiro).</p>
{dica('<b>O português guarda o tema.</b> As palavras portuguesas derivadas do latim costumam mostrar se o <i>e</i> fica ou cai: <i>puer</i> deu "pueril" (com <i>e</i>); <i>ager</i> deu "agrário" e "agrícola" (sem <i>e</i>); <i>magister</i> deu "magistral"; <i>liber</i>, "livraria" e "livro". Use isso como lembrete, mas a palavra final é sempre a do genitivo no dicionário.')}
'''),
        ('Os neutros: bellum e a regra que vale para sempre', f'''
<p>A terceira classe da segunda declinação são os <b>neutros em <i>-um</i></b>, como <i>bellum</i>, "guerra". No genitivo, dativo e ablativo eles se declinam como <i>dominus</i>; a diferença está no nominativo, no acusativo e no vocativo.</p>
{tabela_declinacao('Segunda declinação, neutros: bellum, -ī (n.), "guerra"', [
    ('bell<b>um</b>', 'bell<b>a</b>'), ('bell<b>ī</b>', 'bell<b>ōrum</b>'), ('bell<b>ō</b>', 'bell<b>īs</b>'),
    ('bell<b>um</b>', 'bell<b>a</b>'), ('bell<b>um</b>', 'bell<b>a</b>'), ('bell<b>ō</b>', 'bell<b>īs</b>')])}
<p>Repare em duas coisas, que valem para <b>todos os neutros do latim</b>, em qualquer declinação: (1) o nominativo, o acusativo e o vocativo são <b>sempre iguais</b> entre si; (2) no plural, esses três casos terminam em <b><i>-a</i></b>. A explicação que os linguistas costumam dar é histórica: o neutro designava originalmente sobretudo coisas, que raramente "agem" ou são chamadas, e por isso não marcava a diferença entre sujeito e objeto. É a regra mais rentável que você vai aprender neste livro: quando chegar à terceira declinação, <i>tempus</i> e <i>tempora</i> seguirão o mesmo princípio.</p>
<p>A regra tem duas consequências para a leitura. Primeiro, um neutro no nominativo/acusativo não diz sozinho se é sujeito ou objeto: decide-se pelo verbo e pelas outras palavras, como você fez com <i>caelum</i> no Gênesis (capítulo 3). Segundo, o <i>-a</i> do neutro plural pode ser confundido com o <i>-a</i> da primeira declinação. <i>Dōna</i> não é "uma dádiva" feminina: é "presentes", plural de <i>dōnum</i>. E, ao contrário do grego, o latim põe o verbo no <b>plural</b> com um sujeito neutro plural:</p>
{exemplos([('Templ<b>um</b> in oppidō est.', 'O templo está na cidade. (<i>templum</i>, nominativo: o único candidato a sujeito)'), ('Puer templ<b>um</b> spectat.', 'O menino olha o templo. (<i>templum</i>, acusativo: o sujeito já é <i>puer</i>)'), ('Dōn<b>a</b> in mēnsā <b>sunt</b>.', 'Os presentes estão na mesa. (neutro plural, verbo no plural)'), ('Poēta verb<b>a</b> pulchra amat.', 'O poeta ama palavras belas. (<i>verba</i>, acusativo plural)')])}
{comparacao('Terminações da 2ª declinação que se repetem', ['Terminação', 'Pode ser', 'Como decidir'], [
    ['-ī', 'genitivo sing. · nominativo/vocativo pl. (masc.) · vocativo sing. (fīlī, Iūlī)', 'o número do verbo; um nome vizinho de que dependa ("de"); uma pessoa a quem se fala'],
    ['-ō', 'dativo sing. · ablativo sing.', 'uma preposição pede ablativo (<i>in hortō, cum amīcō</i>); um verbo de dar ou dizer pede dativo'],
    ['-īs', 'dativo pl. · ablativo pl.', 'como na 1ª declinação: preposição → ablativo; "a quem" → dativo'],
    ['-um', 'acusativo sing. (masc.) · nominativo/acusativo sing. (neutro)', 'o gênero do dicionário; se for neutro, a função que falta na frase'],
    ['-a', 'neutro plural (nom./ac./voc.) · 1ª declinação (nom. sing.; com macron, abl. sing.)', 'o dicionário (<i>bellum</i> ou <i>puella</i>?) e o número do verbo'],
])}
<h3>Vocabulário da segunda declinação</h3>
<p>Estes nomes, junto com os do capítulo 4, são o vocabulário dos exemplos e exercícios. Todos estão entre as palavras mais frequentes do latim.</p>
{tabela(['Nome', 'Significado', 'Nome', 'Significado'], [
    ['dominus, -ī (m.)', 'senhor, dono', 'puer, puerī (m.)', 'menino'], ['servus, -ī (m.)', 'escravo', 'vir, virī (m.)', 'homem, varão'],
    ['amīcus, -ī (m.)', 'amigo', 'ager, agrī (m.)', 'campo'], ['fīlius, -ī (m.)', 'filho', 'magister, magistrī (m.)', 'mestre, professor'],
    ['hortus, -ī (m.)', 'jardim', 'liber, librī (m.)', 'livro'], ['equus, -ī (m.)', 'cavalo', 'bellum, -ī (n.)', 'guerra'],
    ['lupus, -ī (m.)', 'lobo', 'dōnum, -ī (n.)', 'presente, dádiva'], ['deus, -ī (m.)', 'deus', 'verbum, -ī (n.)', 'palavra'],
    ['discipulus, -ī (m.)', 'aluno, discípulo', 'oppidum, -ī (n.)', 'cidade (fortificada)'], ['mūrus, -ī (m.)', 'muro', 'templum, -ī (n.)', 'templo'],
    ['caelum, -ī (n.)', 'céu', 'cōnsilium, -ī (n.)', 'conselho, plano'],
], 'Nomes da segunda declinação', latim_cols=(0, 2))}
'''),
        ('Os adjetivos de primeira classe: bonus, pulcher, līber', f'''
<p>Um <b>adjetivo</b> latino se declina como um nome, mas tem formas para os três gêneros, porque precisa acompanhar nomes masculinos, femininos e neutros. Os <b>adjetivos de primeira classe</b> (a denominação é a da gramática do Pe. Ravizza) tomam emprestadas as duas declinações que você já conhece: o <b>masculino</b> se declina como <i>dominus</i> (ou <i>puer</i>, ou <i>ager</i>), o <b>feminino</b> como <i>rosa</i>, o <b>neutro</b> como <i>bellum</i>. O dicionário os registra com as três terminações do nominativo: <i>bonus, -a, -um</i>.</p>
{tabela_declinacao('bonus, bona, bonum, "bom" · singular', [
    ('bon<b>us</b>', 'bon<b>a</b>', 'bon<b>um</b>'), ('bon<b>ī</b>', 'bon<b>ae</b>', 'bon<b>ī</b>'), ('bon<b>ō</b>', 'bon<b>ae</b>', 'bon<b>ō</b>'),
    ('bon<b>um</b>', 'bon<b>am</b>', 'bon<b>um</b>'), ('bon<b>e</b>', 'bon<b>a</b>', 'bon<b>um</b>'), ('bon<b>ō</b>', 'bon<b>ā</b>', 'bon<b>ō</b>')],
    colunas=('Masculino', 'Feminino', 'Neutro'))}
{tabela_declinacao('bonus, bona, bonum, "bom" · plural', [
    ('bon<b>ī</b>', 'bon<b>ae</b>', 'bon<b>a</b>'), ('bon<b>ōrum</b>', 'bon<b>ārum</b>', 'bon<b>ōrum</b>'), ('bon<b>īs</b>', 'bon<b>īs</b>', 'bon<b>īs</b>'),
    ('bon<b>ōs</b>', 'bon<b>ās</b>', 'bon<b>a</b>'), ('bon<b>ī</b>', 'bon<b>ae</b>', 'bon<b>a</b>'), ('bon<b>īs</b>', 'bon<b>īs</b>', 'bon<b>īs</b>')],
    colunas=('Masculino', 'Feminino', 'Neutro'))}
<p>Não há nada novo para decorar: são as terminações de <i>dominus</i>, <i>rosa</i> e <i>bellum</i>, lado a lado. Note que o masculino faz o vocativo em <i>-e</i>, como os nomes (<i>bone amīce</i>, "bom amigo!"), e que o neutro obedece à regra da seção anterior.</p>
<h3>Os adjetivos em -er</h3>
<p>Alguns adjetivos têm o masculino em <i>-er</i>, e aqui volta a questão do <i>e</i>. A maioria o <b>perde</b> fora do nominativo masculino, como <i>ager</i>: é o tipo <i>pulcher, pulchra, pulchrum</i>, "belo" (assim também <i>sacer</i>, sagrado; <i>niger</i>, negro; <i>aeger</i>, doente). Uma minoria o <b>conserva</b>, como <i>puer</i>: é o tipo <i>līber, lībera, līberum</i>, "livre" (assim também <i>miser</i>, infeliz; <i>asper</i>, áspero; <i>tener</i>, tenro). O dicionário mostra a diferença no feminino: <i>pulcher, -chra, -chrum</i>, mas <i>līber, -era, -erum</i>.</p>
{tabela_declinacao('pulcher, pulchra, pulchrum, "belo" (tipo ager) · līber, lībera, līberum, "livre" (tipo puer) · singular', [
    ('pulcher', 'pulchr<b>a</b>', 'pulchr<b>um</b>', 'līber', 'līber<b>a</b>', 'līber<b>um</b>'),
    ('pulchr<b>ī</b>', 'pulchr<b>ae</b>', 'pulchr<b>ī</b>', 'līber<b>ī</b>', 'līber<b>ae</b>', 'līber<b>ī</b>'),
    ('pulchr<b>ō</b>', 'pulchr<b>ae</b>', 'pulchr<b>ō</b>', 'līber<b>ō</b>', 'līber<b>ae</b>', 'līber<b>ō</b>'),
    ('pulchr<b>um</b>', 'pulchr<b>am</b>', 'pulchr<b>um</b>', 'līber<b>um</b>', 'līber<b>am</b>', 'līber<b>um</b>'),
    ('pulcher', 'pulchr<b>a</b>', 'pulchr<b>um</b>', 'līber', 'līber<b>a</b>', 'līber<b>um</b>'),
    ('pulchr<b>ō</b>', 'pulchr<b>ā</b>', 'pulchr<b>ō</b>', 'līber<b>ō</b>', 'līber<b>ā</b>', 'līber<b>ō</b>')],
    colunas=('m.', 'f.', 'n.', 'm.', 'f.', 'n.'))}
<p>No plural, ambos seguem <i>bonus</i> sobre o tema que já se vê no feminino: <i>pulchrī, pulchrae, pulchra; pulchrōrum, pulchrārum, pulchrōrum</i>... e <i>līberī, līberae, lībera; līberōrum</i>... O plural masculino <i>līberī</i>, usado como nome, quer dizer também "os filhos" (os "nascidos livres" da casa, em oposição aos escravos). O português conserva o tema nos derivados: "pulcritude" (sem <i>e</i>), "liberdade" e "miserável" (com <i>e</i>).</p>
{tabela(['Adjetivo', 'Significado', 'Adjetivo', 'Significado'], [
    ['bonus, -a, -um', 'bom', 'malus, -a, -um', 'mau'], ['magnus, -a, -um', 'grande', 'parvus, -a, -um', 'pequeno'],
    ['multus, -a, -um', 'muito; pl. muitos', 'novus, -a, -um', 'novo'], ['longus, -a, -um', 'longo', 'altus, -a, -um', 'alto, profundo'],
    ['clārus, -a, -um', 'claro; famoso', 'laetus, -a, -um', 'alegre, contente'], ['Rōmānus, -a, -um', 'romano', 'doctus, -a, -um', 'sábio, culto'],
    ['pulcher, -chra, -chrum', 'belo', 'līber, -era, -erum', 'livre'], ['miser, -era, -erum', 'infeliz, desgraçado', 'sacer, -cra, -crum', 'sagrado'],
], 'Adjetivos de primeira classe', latim_cols=(0, 2))}
'''),
        ('Concordância, posição e adjetivos substantivados', f'''
<p>A regra de ouro é curta: <b>o adjetivo concorda com o nome em gênero, número e caso</b>. Gênero, número e caso, e não declinação nem terminação. Quando o nome é da segunda declinação masculina, as terminações coincidem e a frase "rima": <i>dominus bonus</i>, <i>dominī bonī</i>, <i>dominō bonō</i>. Mas basta o nome ser de outra família para a rima desaparecer, e é aí que se vê quem entendeu a regra.</p>
{exemplos([('naut<b>a</b> bon<b>us</b>', 'o marinheiro bom: <i>nauta</i> é masculino, então o adjetivo vai para o masculino, mesmo com o nome em <i>-a</i>'),
          ('naut<b>ae</b> bon<b>ī</b> · naut<b>ārum</b> bon<b>ōrum</b> · naut<b>īs</b> bon<b>īs</b>', 'os marinheiros bons · dos marinheiros bons · aos (com os) marinheiros bons'),
          ('Puellae poēt<b>ae</b> clār<b>ō</b> rosās dant.', 'As meninas dão rosas ao poeta famoso. (dativo singular masculino: <i>clārō</i> resolve a dúvida de <i>poētae</i>)'),
          ('puell<b>a</b> pulchr<b>a</b> · dōn<b>um</b> pulchr<b>um</b> · dōn<b>a</b> pulchr<b>a</b>', 'a menina bela · o presente belo · os presentes belos')])}
<p>Repare no terceiro exemplo: <i>poētae</i>, sozinho, poderia ser genitivo, dativo ou nominativo plural; <i>clārō</i> só pode ser dativo ou ablativo singular masculino ou neutro. A única leitura que serve aos dois é o <b>dativo singular</b>. O adjetivo, portanto, não é só enfeite: ele confirma o caso do nome, e às vezes é ele que o revela.</p>
<p>O adjetivo pode ser <b>atributivo</b>, ligado diretamente ao nome (<i>hortus magnus</i>, "o jardim grande"), ou <b>predicativo</b>, ligado ao sujeito pelo verbo <i>esse</i> (<i>hortus magnus est</i>, "o jardim é grande"). A concordância é a mesma nos dois casos: o predicativo fica no nominativo, como o sujeito (<i>Dōna pulchra sunt</i>, "os presentes são belos").</p>
{diagrama_frase([('Agricola bonus', 'nominativo sing. masc. · quem dá'), ('fīliō parvō', 'dativo sing. masc. · a quem dá'), ('dōnum pulchrum', 'acusativo sing. neutro · o que dá'), ('dat', 'verbo · "dá"')],
    'Cada grupo nome + adjetivo funciona como uma unidade, ligada pela concordância: <i>Agricola bonus fīliō parvō dōnum pulchrum dat</i> = O bom agricultor dá um belo presente ao filho pequeno.')}
<h3>Onde fica o adjetivo?</h3>
<p>Não há regra fixa. Os adjetivos aparecem antes do nome com um pouco mais de frequência do que depois, mas a posição serve sobretudo à <b>ênfase</b>: o que vem primeiro chama mais atenção. Duas tendências merecem registro: os adjetivos de <b>quantidade</b> (<i>multus</i>, os numerais) costumam vir antes (<i>multī servī</i>, "muitos escravos"), e <i>Rōmānus</i> costuma vir depois (<i>populus Rōmānus</i>, "o povo romano"). Nos poetas, o adjetivo pode até se separar do nome por várias palavras; a concordância é o fio que os reconecta. Por isso, ao ler, não procure o adjetivo "ao lado" do nome: procure a forma que concorda com ele.</p>
<h3>Adjetivos usados como nomes</h3>
<p>Um adjetivo pode dispensar o nome e ocupar o lugar dele, sobretudo no <b>plural</b>: o <b>masculino</b> designa pessoas, o <b>neutro</b> designa coisas. <i>Bonī</i> são "os bons" (homens); <i>Rōmānī</i>, "os romanos"; <i>multī</i>, "muitos"; mas <i>bona</i> são "as coisas boas, os bens", <i>multa</i>, "muitas coisas". No singular, o neutro também é comum: <i>bonum</i>, "o bem"; <i>malum</i>, "o mal". O português faz o mesmo ("os bons", "o belo"), mas com o artigo; em latim, quem indica o sentido é o gênero.</p>
{exemplos([('Bon<b>ī</b> patriam amant.', 'Os bons (homens) amam a pátria.'), ('Magister mult<b>a</b> nārrat.', 'O professor conta muitas coisas. (neutro plural: "coisas")'), ('Poēta bon<b>um</b> laudat.', 'O poeta elogia o bem. (neutro singular: "o bem")')])}
'''),
        ('Análise gramatical: uma frase do Evangelho', f'''
<p>Com a segunda declinação e os adjetivos, você já pode ler uma frase inteira de Jesus no Evangelho de Mateus, na tradução de São Jerônimo. Ela é quase toda feita do material deste capítulo:</p>
{exemplos([('Bonus homō dē bonō thēsaurō prōfert bona: et malus homō dē malō thēsaurō prōfert mala.', 'O homem bom tira coisas boas do bom tesouro, e o homem mau tira coisas más do mau tesouro. (Mt 12,35, Vulgata Clementina; macrons acrescentados)')])}
<p>Duas palavras são novas: <i>homō</i>, "homem, ser humano", é da terceira declinação (capítulo 9), e por enquanto basta saber que aqui é nominativo singular masculino; <i>prōfert</i>, "tira para fora, apresenta", é a terceira pessoa do singular do presente de <i>prōferō</i>, um composto do verbo irregular <i>ferō</i>, "levar". A preposição <i>dē</i>, que no capítulo 4 você viu como "de cima de; sobre", indica aqui a origem: "de (dentro de)".</p>
{analise('Mt 12,35, palavra a palavra', [
    ('Bonus', 'bonus, -a, -um, bom', 'nominativo singular masculino', 'atributo de <i>homō</i>'),
    ('homō', 'homō, hominis (m.), homem (3ª declinação)', 'nominativo singular', 'sujeito da primeira oração'),
    ('dē', 'dē (preposição + ablativo)', 'invariável', 'introduz a origem'),
    ('bonō', 'bonus, -a, -um', 'ablativo singular masculino', 'atributo de <i>thēsaurō</i>'),
    ('thēsaurō', 'thēsaurus, -ī (m.), tesouro', 'ablativo singular, 2ª declinação', '<i>dē</i> + ablativo: "do tesouro"'),
    ('prōfert', 'prōferō, prōferre, tirar para fora', 'presente, 3ª pessoa do singular', 'verbo da primeira oração'),
    ('bona', 'bonus, -a, -um, usado como nome', 'acusativo plural neutro', 'objeto direto: "coisas boas"'),
    ('et', 'et (conjunção)', 'invariável', 'liga as duas orações'),
    ('malus homō', 'malus, -a, -um, mau · homō', 'nominativo singular masculino', 'sujeito da segunda oração'),
    ('dē malō thēsaurō', 'dē · malus · thēsaurus', 'ablativo singular masculino', 'origem: "do mau tesouro"'),
    ('prōfert', 'prōferō', 'presente, 3ª pessoa do singular', 'verbo da segunda oração'),
    ('mala', 'malus, -a, -um, usado como nome', 'acusativo plural neutro', 'objeto direto: "coisas más"'),
])}
<p>O ponto delicado é <i>bona</i>. A forma poderia ser feminino singular (nominativo, "boa") ou neutro plural (nominativo ou acusativo, "coisas boas"). Feminino não pode ser: não há nenhum nome feminino na frase com que concordar. Resta o neutro plural, que, sem nome expresso, quer dizer "coisas boas". E nominativo também não pode ser, porque o sujeito de <i>prōfert</i> já existe (<i>bonus homō</i>, singular, como o verbo) e o verbo precisa de um objeto. Logo, acusativo: "tira coisas boas". O mesmo raciocínio vale para <i>mala</i>. Repare também na construção: as duas metades são simétricas, palavra por palavra, e só os adjetivos mudam. A frase inteira é um exercício de concordância.</p>
<h3>Em resumo</h3>
<ul>
<li>Segunda declinação = genitivo singular em <i>-ī</i>. Masculinos: <i>-us, -ī, -ō, -um, -e, -ō</i> / <i>-ī, -ōrum, -īs, -ōs, -ī, -īs</i>. Neutros: <i>-um</i> no nominativo, acusativo e vocativo singular; <i>-a</i> nos mesmos casos do plural.</li>
<li>Nomes em <i>-er</i>: o genitivo mostra se o <i>e</i> fica (<i>puer, puerī</i>) ou cai (<i>ager, agrī</i>). O vocativo deles é igual ao nominativo.</li>
<li>Vocativo: <i>-us</i> → <i>-e</i> (<i>Mārce</i>); nomes próprios em <i>-ius</i> e <i>fīlius</i> → <i>-ī</i> (<i>Iūlī, fīlī</i>). Genitivo de <i>-ius/-ium</i>: <i>-iī</i> (antigo <i>-ī</i>).</li>
<li>Neutros, em qualquer declinação: nominativo = acusativo (= vocativo); plural em <i>-a</i>.</li>
<li>Adjetivos de primeira classe: <i>bonus, -a, -um</i>; <i>pulcher, -chra, -chrum</i> (perde o <i>e</i>); <i>līber, -era, -erum</i> (conserva o <i>e</i>).</li>
<li>Concordância em gênero, número e caso, não em terminação: <i>nauta bonus</i>. Plural substantivado: masculino = pessoas, neutro = coisas.</li>
</ul>
<p>No próximo capítulo, o verbo entra em cena por inteiro: as seis pessoas do presente do indicativo, das quais até aqui você usou só a terceira.</p>
'''),
    ],
    erros_comuns=[
        ('Fazer o adjetivo "rimar" com o nome: <i>nauta bona</i>, <i>agricolae bonae</i>.', 'O adjetivo concorda em gênero, e <i>nauta</i> e <i>agricola</i> são masculinos: <i>nauta bonus</i>, <i>agricolae bonī</i>. Antes de escolher a forma do adjetivo, pergunte o gênero do nome no dicionário, não a terminação.'),
        ('Ler todo <i>-a</i> como feminino singular.', '<i>Bella</i>, <i>dōna</i>, <i>verba</i> são neutros plurais (nominativo ou acusativo). Confira a forma de dicionário (<i>bellum</i>, não <i>bella, -ae</i>) e o número do verbo: <i>Dōna in mēnsā sunt</i>, com <i>sunt</i> no plural.'),
        ('Ler todo <i>-um</i> como acusativo.', 'No neutro, <i>-um</i> é também nominativo: em <i>Templum in oppidō est</i>, <i>templum</i> é o sujeito. Quando o nome é neutro, decida pela função que falta na frase.'),
        ('Errar o <i>e</i> dos nomes em <i>-er</i>: <i>agerī</i>, <i>pulcherum</i>, <i>purī</i>.', 'Aprenda sempre o genitivo (ou o feminino do adjetivo) junto com o nominativo: <i>ager, agrī</i>; <i>pulcher, -chra, -chrum</i>; mas <i>puer, puerī</i> e <i>līber, -era, -erum</i>. O <i>e</i> do nominativo não prova nada.'),
        ('Confundir <i>liber</i>, <i>līber</i> e <i>līberī</i>.', '<i>Liber, librī</i> (i breve) é "livro" e perde o <i>e</i>; <i>līber, -era, -erum</i> (ī longo) é "livre" e o conserva; <i>līberī, -ōrum</i> é "os filhos". O genitivo (<i>librī</i> × <i>līberī</i>) e a quantidade da vogal os distinguem.'),
        ('Usar o nominativo para chamar alguém (<i>Salvē, Mārcus!</i>) ou formar <i>fīlie</i>.', 'Os nomes em <i>-us</i> fazem o vocativo em <i>-e</i> (<i>Mārce</i>, <i>amīce</i>); os nomes próprios em <i>-ius</i> e <i>fīlius</i>, em <i>-ī</i> (<i>Iūlī</i>, <i>fīlī</i>). Os nomes em <i>-er</i> não mudam: <i>puer!</i>'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Três grupos de nome e adjetivo',
            'Leia em voz alta e analise, na ordem latina: <i lang="la">Fīlius dominī cum amīcīs laetīs in agrō magnō ambulat.</i> Vocabulário: <i>ambulat</i>, passeia, caminha; os demais nomes e adjetivos estão nas tabelas do capítulo.', [
            ('Qual é o verbo, e que sujeito ele pede?', '<i>Ambulat</i>, "passeia", 3ª pessoa do singular: espera-se um sujeito no nominativo singular. Como "passear" não tem objeto, não procure acusativo sem preposição.'),
            ('<i>Fīlius</i> e <i>dominī</i>: que casos são?', '<i>Fīlius</i> é nominativo singular, o único sujeito possível. <i>Dominī</i> pode ser genitivo singular ou nominativo plural; como o verbo é singular e o sujeito já existe, é genitivo, ligado a <i>fīlius</i>: "o filho <b>do senhor</b>".'),
            ('<i>cum amīcīs laetīs</i>: que caso, e com que concorda <i>laetīs</i>?', '<i>Cum</i> pede ablativo; <i>amīcīs</i> é ablativo plural, e <i>laetīs</i> (ablativo plural masculino) concorda com ele: "com os amigos alegres". Companhia.'),
            ('<i>in agrō magnō</i>: movimento ou lugar?', '<i>In</i> + ablativo (<i>agrō</i>, de <i>ager, agrī</i>, sem o <i>e</i>) indica lugar onde: "no campo grande". <i>Magnō</i> é ablativo singular masculino, como <i>agrō</i>.'),
            ('Monte a tradução.', '"O filho do senhor passeia com os amigos alegres no campo grande."'),
        ]),
        pratica_guiada('Prática guiada 2 · O adjetivo como detetive',
            'Nas duas frases, <i>nautae</i> é ambíguo (genitivo ou dativo singular, nominativo plural). Use o adjetivo para decidir. Vocabulário: <i>dat</i>, dá; <i>spectat</i>, olha.', [
            ('<i lang="la">Puer dōna nautae Rōmānō dat.</i>', '<i>Rōmānō</i> só pode ser dativo ou ablativo singular masculino ou neutro. Das leituras de <i>nautae</i>, a única compatível é o <b>dativo singular</b>. O verbo "dar" confirma: "O menino dá os presentes ao marinheiro romano."'),
            ('<i lang="la">Puer dōna nautae Rōmānī spectat.</i>', '<i>Rōmānī</i> pode ser genitivo singular ou nominativo plural masculino. Nominativo plural não serve, porque o verbo é singular e o sujeito é <i>puer</i>. Fica o <b>genitivo singular</b>: "O menino olha os presentes do marinheiro romano."'),
            ('E <i>dōna</i>, nas duas frases?', 'Neutro plural; o sujeito já é <i>puer</i> (o verbo está no singular), então <i>dōna</i> é acusativo, o objeto. A regra dos neutros não decide sozinha; a função livre decide.'),
        ], 'Conclusão: quando o nome é ambíguo, olhe para o adjetivo que concorda com ele. As duas formas precisam estar no mesmo caso, e a interseção das possibilidades costuma deixar uma só.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Caso, número e função', 'Diga o caso e o número da palavra destacada e sua função na frase. Vocabulário novo: <i>ambulat</i> = passeia.', [
            ('<i><b>Fīliī</b> dominī in hortō sunt.</i>', 'Nominativo plural: sujeito de <i>sunt</i> (plural). Os filhos do senhor estão no jardim.'),
            ('<i>Fīliī <b>dominī</b> in hortō sunt.</i>', 'Genitivo singular: "do senhor", ligado a <i>fīliī</i>. Poderia ser nominativo plural, mas o sujeito já é <i>fīliī</i> e a posição ao lado dele indica dependência.'),
            ('<i>Puer <b>equō</b> aquam dat.</i>', 'Dativo singular: destinatário de <i>dat</i>. O menino dá água ao cavalo. A forma <i>-ō</i> também é ablativo, mas não há preposição e "dar" pede "a quem".'),
            ('<i>Servus cum <b>equō</b> ambulat.</i>', 'Ablativo singular, com <i>cum</i>: companhia. O escravo passeia com o cavalo.'),
            ('<i>Poēta <b>bella</b> nōn amat.</i>', 'Acusativo plural neutro (de <i>bellum</i>): objeto direto. O poeta não ama as guerras. Não é feminino singular: <i>bellum</i> é neutro, e o sujeito já é <i>poēta</i>.'),
            ('<i>Magister <b>puerīs</b> fābulam nārrat.</i>', 'Dativo plural: destinatário de <i>nārrat</i>. O professor conta uma história aos meninos.'),
            ('<i>Salvē, <b>amīce</b>!</i>', 'Vocativo singular (de <i>amīcus</i>, com <i>-e</i>): a pessoa a quem se fala. Olá, amigo!'),
            ('<i><b>Templum</b> in oppidō est.</i>', 'Nominativo singular neutro: sujeito de <i>est</i>, o único candidato. A forma é igual à do acusativo; decide a função que falta.'),
        ]),
        exercicio('Exercício 2 · Decline', 'Decline no singular e no plural, em voz alta e por escrito.', [
            ('<i>ager, agrī</i> (m.), campo', 'ager, agrī, agrō, agrum, ager, agrō; agrī, agrōrum, agrīs, agrōs, agrī, agrīs. O <i>e</i> só aparece no nominativo e no vocativo singular.'),
            ('<i>dōnum, -ī</i> (n.), presente', 'dōnum, dōnī, dōnō, dōnum, dōnum, dōnō; dōna, dōnōrum, dōnīs, dōna, dōna, dōnīs. Nominativo, acusativo e vocativo iguais nos dois números.'),
            ('<i>agricola bonus</i>, o bom agricultor', 'agricola bonus, agricolae bonī, agricolae bonō, agricolam bonum, agricola bone, agricolā bonō; agricolae bonī, agricolārum bonōrum, agricolīs bonīs, agricolās bonōs, agricolae bonī, agricolīs bonīs. O nome segue <i>rosa</i>, o adjetivo segue <i>dominus</i>: concordância em gênero, não em terminação. Note o vocativo <i>agricola bone</i>.'),
            ('<i>puer miser</i>, o menino infeliz', 'puer miser, puerī miserī, puerō miserō, puerum miserum, puer miser, puerō miserō; puerī miserī, puerōrum miserōrum, puerīs miserīs, puerōs miserōs, puerī miserī, puerīs miserīs. Os dois conservam o <i>e</i>.'),
        ]),
        exercicio('Exercício 3 · Concordância', 'Escreva a forma correta do adjetivo entre parênteses e explique.', [
            ('<i>nauta ___</i> (bonus), nominativo', '<i>bonus</i>: <i>nauta</i> é masculino.'),
            ('<i>puellae ___ cantant</i> (pulcher; <i>cantant</i> = cantam)', '<i>pulchrae</i>: nominativo plural feminino; <i>pulcher</i> perde o <i>e</i>.'),
            ('<i>Puer dōnum ___ portat</i> (magnus)', '<i>magnum</i>: acusativo singular neutro, como <i>dōnum</i>.'),
            ('<i>cum agricolā ___</i> (laetus)', '<i>laetō</i>: ablativo singular masculino. <i>Agricolā</i> termina em <i>-ā</i>, mas o adjetivo vai para o masculino.'),
            ('<i>Rēgīna poētae ___ rosās dat</i> (clārus)', '<i>clārō</i>: dativo singular masculino; <i>poētae</i> é o destinatário.'),
            ('<i>Servī in agrīs ___ sunt</i> (parvus)', '<i>parvīs</i>: ablativo plural masculino, como <i>agrīs</i>. "Os escravos estão nos campos pequenos." (Também é gramatical <i>parvī</i>, predicativo de <i>servī</i>, "os escravos, nos campos, são pequenos"; mas o sentido natural é o adjetivo junto de <i>agrīs</i>.)'),
            ('<i>Puerī ___ nōn sunt</i> (līber)', '<i>līberī</i>: nominativo plural masculino, predicativo; <i>līber</i> conserva o <i>e</i>. "Os meninos não são livres."'),
            ('<i>Poēta verba ___ amat</i> (novus)', '<i>nova</i>: acusativo plural neutro. Não é feminino: <i>verbum</i> é neutro.'),
        ]),
        exercicio('Exercício 4 · Do singular para o plural, e do português para o latim', 'Nas quatro primeiras, passe para o plural todos os nomes, adjetivos e verbos. Nas demais, traduza para o latim usando só o vocabulário dos capítulos 4 e 5 (verbos na 3ª pessoa do presente).', [
            ('<i>Servus bonus in agrō est.</i>', '<i>Servī bonī in agrīs sunt.</i> Os escravos bons estão nos campos.'),
            ('<i>Puer miser dōnum parvum portat.</i>', '<i>Puerī miserī dōna parva portant.</i> O neutro plural vai para <i>-a</i>; o verbo, para <i>-nt</i>.'),
            ('<i>Magister clārus librum novum laudat.</i>', '<i>Magistrī clārī librōs novōs laudant.</i> <i>Magistrī</i> e <i>librōs</i> sem o <i>e</i>.'),
            ('<i>Nauta Rōmānus in oppidō magnō habitat.</i>', '<i>Nautae Rōmānī in oppidīs magnīs habitant.</i> O nome segue a 1ª declinação, o adjetivo masculino a 2ª.'),
            ('O senhor dá um livro novo ao filho.', '<i>Dominus fīliō librum novum dat.</i> <i>Fīliō</i>: dativo, destinatário.'),
            ('Os presentes da rainha são belos.', '<i>Dōna rēgīnae pulchra sunt.</i> <i>Pulchra</i>: nominativo plural neutro, predicativo de <i>dōna</i>; verbo no plural.'),
            ('Marco, o professor está no templo!', '<i>Mārce, magister in templō est.</i> Vocativo em <i>-e</i>; <i>in</i> + ablativo, lugar onde.'),
            ('Os bons marinheiros navegam até a ilha grande.', '<i>Nautae bonī ad īnsulam magnam nāvigant.</i> (também <i>Bonī nautae</i>: a posição do adjetivo é livre.)'),
        ]),
        exercicio('Exercício 5 · Leitura de uma frase autêntica', 'Mt 7,17, Vulgata Clementina (macrons acrescentados): <i lang="la">Sīc omnis arbor bona frūctūs bonōs facit: mala autem arbor malōs frūctūs facit.</i> Vocabulário: <i>sīc</i>, assim; <i>omnis</i>, todo (adjetivo da 3ª declinação, capítulo 10); <i>arbor, arboris</i> (f.), árvore (3ª declinação); <i>frūctūs</i>, frutos (acusativo plural de <i>frūctus</i>, m., da 4ª declinação); <i>facit</i>, faz, produz; <i>autem</i>, mas, porém (vem sempre depois da primeira palavra).', [
            ('Com que nome concorda <i>bona</i>, e em que gênero, número e caso?', 'Com <i>arbor</i>: nominativo singular feminino. <i>Arbor</i> termina em <i>-or</i>, mas é feminino (os nomes de árvores são femininos), e o adjetivo mostra o gênero. Aqui <i>bona</i> não é neutro plural, como em Mt 12,35, porque há um nome feminino com que concordar.'),
            ('Você ainda não conhece a 4ª declinação. Como saber o caso de <i>frūctūs</i>?', 'Pelo adjetivo: <i>bonōs</i> é acusativo plural masculino, então <i>frūctūs</i> também é. Objeto direto de <i>facit</i>: "produz frutos bons".'),
            ('Qual é o sujeito de cada oração?', '<i>Omnis arbor bona</i> na primeira, <i>mala arbor</i> na segunda: nominativos singulares, com verbo no singular (<i>facit</i>).'),
            ('Compare a posição dos adjetivos nas duas metades.', 'Na primeira, os adjetivos vêm depois dos nomes (<i>arbor bona, frūctūs bonōs</i>); na segunda, antes (<i>mala arbor, malōs frūctūs</i>). A inversão forma um <b>quiasmo</b> (cruzamento ABBA): <i>arbor bona … frūctūs bonōs</i> e depois <i>mala arbor … malōs frūctūs</i>, e o cruzamento destaca o contraste entre as duas metades do versículo. A posição do adjetivo serve à ênfase; a concordância garante que cada um se ligue ao seu nome.'),
            ('Traduza.', '"Assim, toda árvore boa produz frutos bons; mas a árvore má produz frutos maus."'),
        ]),
        exercicio('Exercício 6 · Leitura', 'Leia o texto em voz alta, duas vezes, e responda em português. Texto escrito para este capítulo. Vocabulário novo: <i>ambulant</i>, passeiam; <i>labōrant</i>, trabalham; <i>sed</i>, mas.<br><br><i lang="la">Mārcus est puer Rōmānus. Mārcus et Iūlius, fīlius poētae clārī, in hortō magnō ambulant. In hortō sunt rosae pulchrae et equī parvī. Magister, vir bonus et doctus, puerīs fābulās longās dē bellīs Rōmānīs nārrat. Puerī laetī sunt et magistrum laudant. Servī in agrīs labōrant; agrī dominī magnī sunt, sed servī miserī sunt. Mārcus servōs spectat et amīcum vocat: "Iūlī, servī nōn sunt līberī."</i>', [
            ('Quem é Júlio? Que caso é <i>poētae clārī</i>?', 'O filho de um poeta famoso. <i>Poētae clārī</i> poderia ser nominativo plural ("os poetas famosos") ou genitivo singular; a concordância aceita as duas leituras, e <i>clārī</i>, masculino, só confirma que <i>poēta</i> é masculino. Decide a função: o grupo depende de <i>fīlius</i> ("filho de quem?"), e um nominativo plural não teria papel na frase. Logo, genitivo: "filho do poeta famoso".'),
            ('Onde os meninos passeiam, e o que há lá?', 'Num jardim grande (<i>in hortō magnō</i>, ablativo com <i>in</i>). Há rosas belas (<i>rosae pulchrae</i>, feminino) e cavalos pequenos (<i>equī parvī</i>, masculino): o mesmo adjetivo mudaria de forma conforme o gênero.'),
            ('O que faz o professor, e para quem?', 'Conta aos meninos (<i>puerīs</i>, dativo plural) histórias longas sobre as guerras romanas (<i>dē bellīs Rōmānīs</i>, ablativo plural neutro com <i>dē</i>).'),
            ('Em <i>agrī dominī magnī sunt</i>, com que concorda <i>magnī</i>?', 'Gramaticalmente, <i>magnī</i> poderia concordar com <i>agrī</i> (nominativo plural) ou com <i>dominī</i> (genitivo singular). Mas <i>sunt</i> precisa de um predicativo, e a oração introduzida por <i>sed</i> lhe opõe <i>miserī</i>: <i>magnī</i> é predicativo de <i>agrī</i>. "Os campos do senhor são grandes."'),
            ('Que forma é <i>Iūlī</i>, e por quê?', 'Vocativo de <i>Iūlius</i>: nome próprio em <i>-ius</i>, vocativo em <i>-ī</i>. Marco está chamando o amigo.'),
            ('Em <i>servī nōn sunt līberī</i>, <i>līberī</i> quer dizer "filhos" ou "livres"?', '"Livres": é o adjetivo <i>līber, -era, -erum</i>, no nominativo plural masculino, predicativo de <i>servī</i>. "Os escravos não são livres." O sentido de "filhos" só aparece quando <i>līberī</i> funciona como nome.'),
        ]),
    ],
    leituras=['sonnenschein-ora-maritima-a-latin-story-for-beginners', 'jones-puer-romanus', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'ravizza-gramatica-latina', 'bennett-new-latin-grammar'],
    leituras_nota='Em Ora Maritima, os capítulos seguintes aos que você leu no capítulo 4 introduzem os nomes da segunda declinação e os adjetivos: continue de onde parou. Puer Romanus e os primeiros capítulos de Familia Romana (com seus servī, fīliī e o adjetivo Rōmānus em toda página) mostram a concordância em uso. Na Vulgata, leia o capítulo 7 de Mateus, de onde vem o exercício 5. Em Ravizza (nn. 22–24 e 51–52) e em Bennett (§§ 23–25 e 63–65) estão as tabelas completas para consulta.',
)
