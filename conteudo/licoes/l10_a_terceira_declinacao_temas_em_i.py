from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='10-a-terceira-declinacao-temas-em-i', titulo='Temas em -i e adjetivos de segunda classe',
    titulo_latim='Dē tertiā dēclīnātiōne (II)', tempo='60 min',
    resumo='A segunda metade da terceira declinação: o que é um tema em -i, as três regras práticas para reconhecê-lo pelo dicionário, as poucas formas em que ele difere de um tema consonantal (genitivo plural em -ium, neutros em -ī e -ia), os temas "puros" com acusativo em -im, e os adjetivos de segunda classe (ācer, fortis, fēlīx), que se declinam pela terceira declinação e concordam com nomes de qualquer declinação.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['3ª declinação', 'temas em -i', 'parissílabos e imparissílabos', 'genitivo plural em -ium', 'neutros em -e, -al, -ar', 'temas mistos e temas puros', 'acusativo em -im e ablativo em -ī', 'vīs, vīrēs', 'adjetivos de segunda classe', 'adjetivos de três, duas e uma terminação', 'ablativo do adjetivo em -ī', 'vetus, dīves, pauper', 'concordância entre declinações diferentes', 'adjetivo neutro plural substantivado', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 9, sobre os temas consonantais da terceira declinação: este capítulo parte das terminações de <i>rēx</i> e <i>corpus</i> e só mostra o que muda. Do capítulo 5, a concordância do adjetivo de primeira classe (<i>bonus, -a, -um</i>) em gênero, número e caso.',
                       licoes=['05-a-segunda-declinacao', '09-a-terceira-declinacao-temas-consonantais']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 37 (temas em -i m./f.: genitivo plural sempre em -ium; -im, -ī, -īs antigos, substituídos em geral por -em, -e, -ēs), § 38 (tussis, īgnis, hostis; 38.1 acusativo em -im e ablativo em -ī: sitis, turris, secūris, nomes de rios e cidades; 38.2 canis e iuvenis são consonantais; 38.3 pars, mors, nox, ars, gēns, mēns), § 39 (neutros em -e, -al, -ar: sedīle, animal, calcar; 39.2 mare às vezes com ablativo mare), § 40 (consonantais com formas de -i no plural: caedēs, arx, linter; 40.1 nūbēs, urbs, mōns, cliēns, cīvitās), § 41 (vīs; nāvis com ablativo frequente em -ī), §§ 43 e 45 (gênero: -is, -ēs femininos; -nis, collis, mēnsis, mōns, dēns masculinos), § 67 (adjetivos da 3ª: três classes; flexão de tema em -i), § 68 (ācer; 68.2 celer, sem genitivo plural), § 69 (fortis), § 70 (fēlīx, prūdēns, vetus; 70.1 dīves, pauper, prīnceps como consonantais; 70.3 particípios), § 234 (concordância), § 236 (adjetivos neutros plurais como substantivos)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 65 (classes de temas em -i: parissílabos em -is; neutros em -e, -al, -ar; mistos), §§ 66–67 (temas puros m./f.: sitis, turris, īgnis, imber), §§ 68–69 (neutros: mare; animal, exemplar; ablativo -ī, plural -ia, genitivo -ium), §§ 70–72 (temas mistos: nūbēs, urbs, nox, cliēns, aetās), §§ 73–78 (resumo das formas de -i: 75 acusativo em -im, sitis, vīs, nomes de rios; 76 ablativo em -ī; 77 acusativo plural -īs; 78 genitivo plural em -um: canis, iuvenis, sēdēs, mare), § 79 (nāvis declinado como turris), §§ 114–119 (adjetivos da 3ª: ācer, levis, atrōx, egēns, vetus), § 121 (ablativo -ī ou -e: ingēns em -ī; dīves, pauper, prīnceps em -e; genitivo plural em -um em dīves e prīnceps; vetus), § 286 (concordância)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 44 (cīvis, imber; nota 1: -im e -ī em sitis, Tiberis, turris; nota 2: vīs), § 45 (nūbēs), § 46 (mōns, urbs, ars, dēns), § 47 (neutros: cubīle, animal, calcar, exemplar; mare), § 49 (regra prática do genitivo plural: parissílabos em -ium, imparissílabos em -um, com as exceções nox, canis, iuvenis, pater, māter, frāter, sēdēs); § 73 (trīstis, omnis; ācer; celer), § 74 (fēlīx, ingēns), § 75 (dīves, pauper, vetus, consonantais)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 28 (imparissílabos de tema em duas consoantes, nox, urbs, ars, e parissílabos, cīvis, ovis, nūbēs: genitivo plural em -ium), n. 29 (acusativo em -im e ablativo em -ī: Tiberis, sitis, vīs, turris; cīvis, īgnis, nāvis com ablativo em -e ou -ī), n. 30 (genitivo plural: canis e iuvenis em -um), n. 31 (acusativo plural em -īs), n. 32 (neutros em -e, -al, -ar: cubīle, animal), n. 34–35 (vīs; mare, plural maria, genitivo raro), n. 53 (adjetivos da segunda classe: ācer, brevis, fēlīx, prūdēns; exceções dīves, pauper, vetus)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Mateus 19,26; Salmo 144,9; Eclesiastes 1,2', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Matthaeum', nota='frases autênticas da seção 6, conferidas na Wikisource latina (Mateus, cap. 19; Liber Psalmorum, cap. 144; Liber Ecclesiastes, cap. 1); ortografia adaptada (ae por æ) e macrons acrescentados; do Salmo e do Eclesiastes cita-se só um trecho do versículo', tipo='dominio_publico'),
    ],
    objetivos=[
        'Explicar o que é um tema em <i>-i</i> e em que formas ele difere de um tema consonantal (genitivo plural <i>-ium</i>; nos neutros, ablativo <i>-ī</i> e plural <i>-ia</i>).',
        'Decidir, a partir da entrada de dicionário, se um nome da terceira declinação faz o genitivo plural em <i>-um</i> ou em <i>-ium</i>, usando as três regras práticas e conhecendo as exceções principais.',
        'Declinar nomes de tema em <i>-i</i> masculinos, femininos e neutros (<i>cīvis, urbs, animal, mare</i>) e reconhecer as formas raras em <i>-im</i>, <i>-ī</i> e <i>-īs</i> (<i>turrim, sitī, vim, cīvīs</i>).',
        'Declinar os adjetivos de segunda classe de três, duas e uma terminação (<i>ācer</i>, <i>fortis</i>, <i>fēlīx</i>), com ablativo singular em <i>-ī</i>, e reconhecer os que se declinam como consonantais (<i>vetus, dīves, pauper</i>).',
        'Fazer concordar um adjetivo de segunda classe com nomes de qualquer declinação (<i>fēmina fortis, puer fortis, rēx fortis, corpus forte</i>) e usar a concordância para ler uma frase autêntica.',
    ],
    secoes=[
        ('O que é um tema em -i', f'''
<p>No capítulo 9 você aprendeu a declinar <i>rēx, rēgis</i> e <i>corpus, corporis</i>: tira-se <i>-is</i> do genitivo, e ao tema que sobra (<i>rēg-</i>, <i>corpor-</i>) juntam-se as terminações. Esses nomes têm um tema terminado em consoante. Ao lado deles, a terceira declinação abriga uma segunda família, cujo tema terminava originalmente na vogal <b><i>-i</i></b>: o tema de <i>cīvis</i> ("cidadão") é <i>cīvi-</i>, o de <i>mare</i> ("mar") é <i>mari-</i>. São os <b>temas em <i>-i</i></b>. As gramáticas os estudam junto com os consonantais porque, ao longo da história da língua, as duas famílias se misturaram tanto que já os romanos as confundiam: os nomes foram perdendo as formas com <i>i</i> e adotando as dos consonantais, enquanto os adjetivos, ao contrário, foram ganhando formas com <i>i</i> (Allen e Greenough § 73).</p>
<p>O resultado prático é uma boa notícia: você não precisa decorar uma declinação nova. Um tema em <i>-i</i> usa quase todas as terminações que você já conhece e se distingue em <b>poucos pontos fixos</b>, sempre os mesmos, onde o <i>i</i> do tema resistiu. O mais importante, que vale para todos eles, é o genitivo plural: <i>cīv<b>ium</b></i>, "dos cidadãos", contra <i>rēg<b>um</b></i>, "dos reis". Nos neutros, o <i>i</i> aparece ainda no ablativo singular e no plural: <i>marī</i>, <i>animālia</i>.</p>
{comparacao('Os pontos em que o tema em -i aparece', ['Forma', 'Tema consonantal (cap. 9)', 'Tema em -i', 'O que mudou'], [
    ['Genitivo plural', 'rēg<b>um</b>, corpor<b>um</b>', 'cīv<b>ium</b>, urb<b>ium</b>, animāl<b>ium</b>', 'sempre <i>-ium</i>, em todos os gêneros'],
    ['Acusativo plural m./f.', 'rēg<b>ēs</b>', 'cīv<b>ēs</b> ou cīv<b>īs</b>', '<i>-īs</i> é uma variante antiga, comum nos textos clássicos'],
    ['Ablativo singular neutro', 'corpor<b>e</b>', 'mar<b>ī</b>, animāl<b>ī</b>', 'nos neutros em <i>-e, -al, -ar</i>, em regra <i>-ī</i> (<i>mare</i> tem às vezes <i>mare</i>)'],
    ['Nom., ac. e voc. plural neutro', 'corpor<b>a</b>', 'mar<b>ia</b>, animāl<b>ia</b>', '<i>-ia</i> em vez de <i>-a</i>'],
])}
<p>Por que isso importa para quem lê? Porque <i>-ium</i> e <i>-ia</i> são inconfundíveis: quando você encontra <i>urbium</i> ou <i>animālia</i>, já sabe o caso e o número sem hesitar. E importa para quem escreve, porque um genitivo plural trocado (*<i>cīvum</i>, *<i>rēgium</i>) é um erro que o leitor latino perceberia imediatamente. Repare também que a diferença está quase toda no plural: no singular, <i>cīvis</i> declina-se como <i>rēx</i> (<i>cīvis, cīvī, cīvem, cīve</i>), só que com o nominativo igual ao genitivo.</p>
{observacao('Um i que o português conserva', 'Algumas palavras portuguesas, formadas sobre o tema, mostram o <i>i</i> que o nominativo latino escondia: de <i>mari-</i> vem <i>marítimo</i>, e de <i>cīvi-</i> vêm <i>cívico</i> e <i>civil</i>. Não é uma regra, só uma ajuda para a memória.')}
'''),
        ('Como reconhecer um tema em -i: três regras práticas', f'''
<p>O dicionário não diz "tema em <i>-i</i>"; ele dá o nominativo, o genitivo e o gênero. Felizmente, essas três informações bastam na grande maioria dos casos. As gramáticas não classificam esses nomes exatamente da mesma maneira (Bennett chama vários deles de consonantais que "adotaram" formas de <i>-i</i>; Allen e Greenough os chamam de temas mistos), mas concordam nas regras práticas, que são estas.</p>
<h3>Regra 1. Os parissílabos em -is e -ēs</h3>
<p>Um nome é <b>parissílabo</b> quando o nominativo e o genitivo singular têm o mesmo número de sílabas: <i>cī-vis</i>, <i>cī-vis</i>; <i>nū-bēs</i>, <i>nū-bis</i>. Os parissílabos com nominativo em <i>-is</i> ou <i>-ēs</i> são temas em <i>-i</i> e fazem o genitivo plural em <i>-ium</i>: <i>cīvium</i>, <i>hostium</i>, <i>nāvium</i>, <i>nūbium</i>. O motivo é visível: o nominativo conservou o <i>i</i> do tema (<i>cīvi-s</i>), e por isso não "cresce" no genitivo, ao contrário de <i>rēx, rē-gis</i>, que ganha uma sílaba.</p>
<h3>Regra 2. Os imparissílabos com duas consoantes antes do -is do genitivo</h3>
<p>A maioria dos imparissílabos é consonantal, como você viu no capítulo 9. Mas há um grupo que não é: os nomes cujo tema, visto no genitivo, termina em <b>duas consoantes</b>, quase todos monossílabos no nominativo: <i>urbs, urb-is</i>; <i>mōns, mont-is</i>; <i>pars, part-is</i>; <i>ars, art-is</i>; <i>nox, noct-is</i>; <i>gēns, gent-is</i>; <i>mors, mort-is</i>. É a formulação do Pe. Ravizza (n. 28), e é a mais fácil de aplicar: olhe o genitivo, tire <i>-is</i> e conte as consoantes que sobram no fim. Uma consoante (<i>rēg-</i>, <i>mīlit-</i>) dá <i>-um</i>; duas (<i>urb-</i>, <i>noct-</i>) dão <i>-ium</i>. Historicamente, muitos desses nomes perderam o <i>i</i> no nominativo: <i>pars</i> vem de um antigo <i>par(ti)s</i> (Bennett § 38.3). Note que a regra vale só para imparissílabos: <i>pater, patris</i> tem duas consoantes em <i>patr-</i>, mas não é imparissílabo (<i>pa-ter</i>, <i>pa-tris</i>), nem tem nominativo em <i>-is</i> ou <i>-ēs</i>, e por isso fica entre os consonantais.</p>
<h3>Regra 3. Os neutros em -e, -al e -ar</h3>
<p>Os neutros com nominativo em <i>-e</i>, <i>-al</i> ou <i>-ar</i> são temas em <i>-i</i>, e são os que mais conservaram o <i>i</i>: ablativo singular em <i>-ī</i>, plural em <i>-ia</i>, genitivo plural em <i>-ium</i>. Exemplos: <i>mare, maris</i> (mar); <i>animal, animālis</i> (animal); <i>exemplar, exemplāris</i> (modelo); <i>cubīle, cubīlis</i> (leito, toca). No nominativo, <i>mari-</i> trocou o <i>i</i> final por <i>e</i>, e <i>animāli-</i> perdeu a vogal e abreviou o <i>ā</i>: por isso <i>animal</i> tem <i>a</i> breve, e <i>animālis</i>, longo.</p>
{tabela(['Nominativo, genitivo', 'Gênero', 'Regra', 'Genitivo plural', 'Significado'], [
    ['cīvis, cīvis', 'm. e f.', '1 (parissílabo em <i>-is</i>)', 'cīv<b>ium</b>', 'cidadão, cidadã'],
    ['hostis, hostis', 'm. (e f.)', '1', 'host<b>ium</b>', 'inimigo (de guerra)'],
    ['nāvis, nāvis', 'f.', '1', 'nāv<b>ium</b>', 'navio'],
    ['avis, avis', 'f.', '1', 'av<b>ium</b>', 'ave'],
    ['ovis, ovis', 'f.', '1', 'ov<b>ium</b>', 'ovelha'],
    ['fīnis, fīnis', 'm.', '1', 'fīn<b>ium</b>', 'fim, limite'],
    ['īgnis, īgnis', 'm.', '1', 'īgn<b>ium</b>', 'fogo'],
    ['collis, collis', 'm.', '1', 'coll<b>ium</b>', 'colina'],
    ['nūbēs, nūbis', 'f.', '1 (parissílabo em <i>-ēs</i>)', 'nūb<b>ium</b>', 'nuvem'],
    ['urbs, urbis', 'f.', '2 (<i>urb-</i>)', 'urb<b>ium</b>', 'cidade'],
    ['mōns, montis', 'm.', '2 (<i>mont-</i>)', 'mont<b>ium</b>', 'monte, montanha'],
    ['pars, partis', 'f.', '2 (<i>part-</i>)', 'part<b>ium</b>', 'parte'],
    ['ars, artis', 'f.', '2 (<i>art-</i>)', 'art<b>ium</b>', 'arte, habilidade'],
    ['nox, noctis', 'f.', '2 (<i>noct-</i>)', 'noct<b>ium</b>', 'noite'],
    ['gēns, gentis', 'f.', '2 (<i>gent-</i>)', 'gent<b>ium</b>', 'povo, clã'],
    ['mors, mortis', 'f.', '2 (<i>mort-</i>)', 'mort<b>ium</b>', 'morte'],
    ['dēns, dentis', 'm.', '2 (<i>dent-</i>)', 'dent<b>ium</b>', 'dente'],
    ['mare, maris', 'n.', '3 (<i>-e</i>)', '(quase inexistente)', 'mar'],
    ['cubīle, cubīlis', 'n.', '3 (<i>-e</i>)', 'cubīl<b>ium</b>', 'leito, toca'],
    ['animal, animālis', 'n.', '3 (<i>-al</i>)', 'animāl<b>ium</b>', 'animal'],
    ['exemplar, exemplāris', 'n.', '3 (<i>-ar</i>)', 'exemplār<b>ium</b>', 'modelo, exemplo'],
], 'Vocabulário do capítulo: nomes de tema em -i', latim_cols=(0, 3))}
<p>Quanto ao gênero, a tendência dos parissílabos em <i>-is</i> e <i>-ēs</i> é o feminino, mas os terminados em <i>-nis</i> (<i>fīnis, īgnis</i>) e alguns outros (<i>collis</i>) são masculinos, assim como <i>mōns</i> e <i>dēns</i> (Bennett §§ 43 e 45). Os neutros em <i>-e, -al, -ar</i> são sempre neutros. Como no capítulo 9, aprenda o gênero com a palavra.</p>
{observacao('As exceções que você vai encontrar', 'Toda regra prática da terceira declinação tem exceções, e estas são as que aparecem cedo nos textos. <b>Parecem parissílabos, mas fazem <i>-um</i></b>: <i>canis, canis</i> (cão), gen. pl. <i>canum</i>; <i>iuvenis, iuvenis</i> (jovem), gen. pl. <i>iuvenum</i> (Bennett § 38.2: são, na verdade, consonantais); <i>pater, māter, frāter</i>, que só parecem parissílabos porque o <i>e</i> do nominativo cai nos outros casos: <i>patrum, mātrum, frātrum</i>; e <i>sēdēs</i> (assento, morada), que faz em geral <i>sēdum</i>. <b>Parecem imparissílabos de uma consoante, mas fazem <i>-ium</i></b>: alguns monossílabos como <i>mūs, mūris</i> (rato), gen. pl. <i>mūrium</i>. E nos nomes em <i>-tās</i> as gramáticas registram as duas formas: <i>cīvitās</i> (cidade-estado) faz <i>cīvitātum</i> ou <i>cīvitātium</i>: Allen e Greenough (§ 71) dão para os nomes em <i>-tās</i> "em geral <i>-um</i>", Bennett (§ 40.1.e) diz que <i>cīvitās</i> faz "em geral" <i>cīvitātium</i>, e Kennedy (§ 49) observa que Lívio escreve sempre <i>cīvitātium</i> e Cícero sobretudo <i>cīvitātum</i>.')}
{dica('<b>O teste em dois segundos.</b> Diante de uma entrada da terceira declinação, faça duas perguntas. É neutro em <i>-e, -al, -ar</i>? Então é tema em <i>-i</i>. Não é? Compare o nominativo com o genitivo: mesmo número de sílabas, com <i>-is</i> ou <i>-ēs</i> (<i>cīvis, cīvis</i>), ou duas consoantes antes de <i>-is</i> (<i>urbis, noctis</i>), também é tema em <i>-i</i>. O resto é consonantal. Depois, confira a lista de exceções.')}
'''),
        ('Os paradigmas: masculino e feminino, e neutro', f'''
<p>Veja agora as formas completas. Nos masculinos e femininos, tome como modelos <i>cīvis</i> (regra 1) e <i>urbs</i> (regra 2). Compare com <i>rēx</i>, do capítulo 9: só o genitivo plural é obrigatoriamente diferente.</p>
{tabela_declinacao('Tema em -i, masculino e feminino: cīvis, cīvis (m. e f.), "cidadão" · urbs, urbis (f.), "cidade"', [
    ('cīvis', 'cīv<b>ēs</b>', 'urbs', 'urb<b>ēs</b>'), ('cīv<b>is</b>', 'cīv<b>ium</b>', 'urb<b>is</b>', 'urb<b>ium</b>'),
    ('cīv<b>ī</b>', 'cīv<b>ibus</b>', 'urb<b>ī</b>', 'urb<b>ibus</b>'), ('cīv<b>em</b>', 'cīv<b>ēs</b> (-<b>īs</b>)', 'urb<b>em</b>', 'urb<b>ēs</b> (-<b>īs</b>)'),
    ('cīvis', 'cīv<b>ēs</b>', 'urbs', 'urb<b>ēs</b>'), ('cīv<b>e</b> (-<b>ī</b>)', 'cīv<b>ibus</b>', 'urb<b>e</b>', 'urb<b>ibus</b>')],
    colunas=('cīvis · sing.', 'cīvis · pl.', 'urbs · sing.', 'urbs · pl.'))}
<p>Duas observações. O ablativo de <i>cīvis</i> é em geral <i>cīve</i>, mas <i>cīvī</i> também ocorre (Ravizza n. 29; Kennedy § 44); o mesmo vale para <i>avis</i>, <i>nāvis</i> e outros parissílabos (em <i>īgnis</i>, o ablativo <i>īgnī</i> é até o mais comum: Kennedy § 44, nota 1), enquanto <i>urbs</i> e os nomes da regra 2 têm sempre <i>-e</i>. E o acusativo plural em <i>-īs</i>, com <i>ī</i> longo, é a forma antiga do tema em <i>-i</i>: os textos do período clássico ainda trazem muitas vezes <i>cīvīs</i>, <i>urbīs</i>, <i>omnīs</i> (Ravizza n. 31; Allen e Greenough § 77). Quando escrever, use <i>-ēs</i>; quando ler, reconheça <i>-īs</i>. Agora os neutros, <i>animal</i> e <i>mare</i>:</p>
{tabela_declinacao('Tema em -i, neutro: animal, animālis (n.), "animal" · mare, maris (n.), "mar"', [
    ('animal', 'animāl<b>ia</b>', 'mare', 'mar<b>ia</b>'), ('animāl<b>is</b>', 'animāl<b>ium</b>', 'mar<b>is</b>', '(quase inexistente)'),
    ('animāl<b>ī</b>', 'animāl<b>ibus</b>', 'mar<b>ī</b>', 'mar<b>ibus</b> (raro)'), ('animal', 'animāl<b>ia</b>', 'mare', 'mar<b>ia</b>'),
    ('animal', 'animāl<b>ia</b>', 'mare', 'mar<b>ia</b>'), ('animāl<b>ī</b>', 'animāl<b>ibus</b>', 'mar<b>ī</b>', 'mar<b>ibus</b> (raro)')],
    colunas=('animal · sing.', 'animal · pl.', 'mare · sing.', 'mare · pl.'))}
<p>A regra dos neutros continua valendo: nominativo, acusativo e vocativo iguais, e no plural terminados em <i>-a</i>, aqui precedido do <i>i</i> do tema: <i>-ia</i>. O ablativo singular em <i>-ī</i> é o traço mais firme desses neutros (<i>in marī</i>, "no mar"; <i>cum animālī</i>, "com o animal"). <i>Mare</i> tem uma particularidade que vale a pena saber desde já: o plural <i>maria</i> é comum, mas o genitivo plural praticamente não existe nos textos (Allen e Greenough, § 78, dizem que ocorre uma única vez; Kennedy, § 47, nota, dá a forma: <i>marum</i>), e o dativo e ablativo <i>maribus</i> são raros (Ravizza n. 35). Por isso, nos exercícios, o modelo de neutro completo é <i>animal</i>. Ocasionalmente se encontra também o ablativo <i>mare</i> (Bennett § 39.2).</p>
{tabela(['Caso', 'Consonantal m./f.', 'Tema em -i m./f.', 'Consonantal n.', 'Tema em -i n.'], [
    ['Nominativo sing.', 'vários', '<i>-is, -ēs</i> ou vários (<i>urbs, nox</i>)', 'vários', '<i>-e, -al, -ar</i>'],
    ['Genitivo sing.', '<b>-is</b>', '<b>-is</b>', '<b>-is</b>', '<b>-is</b>'],
    ['Dativo sing.', '<b>-ī</b>', '<b>-ī</b>', '<b>-ī</b>', '<b>-ī</b>'],
    ['Acusativo sing.', '<b>-em</b>', '<b>-em</b> (raro <b>-im</b>)', 'igual ao nominativo', 'igual ao nominativo'],
    ['Ablativo sing.', '<b>-e</b>', '<b>-e</b> (às vezes <b>-ī</b>)', '<b>-e</b>', '<b>-ī</b>'],
    ['Nom. e voc. plural', '<b>-ēs</b>', '<b>-ēs</b>', '<b>-a</b>', '<b>-ia</b>'],
    ['Genitivo plural', '<b>-um</b>', '<b>-ium</b>', '<b>-um</b>', '<b>-ium</b>'],
    ['Dativo e ablativo plural', '<b>-ibus</b>', '<b>-ibus</b>', '<b>-ibus</b>', '<b>-ibus</b>'],
    ['Acusativo plural', '<b>-ēs</b>', '<b>-ēs</b> ou <b>-īs</b>', '<b>-a</b>', '<b>-ia</b>'],
], 'Quadro comparativo: tema consonantal e tema em -i')}
<p>Leia o quadro na vertical e repare como as colunas são parecidas: só as linhas do ablativo, do genitivo plural e dos neutros plurais mudam de verdade. Essa é a razão de este capítulo vir logo depois do anterior: quem sabe <i>rēx</i> e <i>corpus</i> já sabe quase tudo de <i>cīvis</i> e <i>animal</i>.</p>
'''),
        ('Temas puros: acusativo em -im e ablativo em -ī; a palavra vīs', f'''
<p>Alguns poucos nomes conservaram também no singular as formas antigas do tema em <i>-i</i>: acusativo em <b><i>-im</i></b> e ablativo em <b><i>-ī</i></b>. Pertencem ao grupo que Allen e Greenough chamam de temas em <i>-i</i> "puros" (os parissílabos em <i>-is</i>, como <i>cīvis</i> e <i>turris</i>, e os neutros em <i>-e, -al, -ar</i>; § 65), por oposição aos "mistos", como <i>urbs</i> e <i>nūbēs</i>, que no singular se declinam como consonantais; mas, mesmo entre os puros, só esses poucos conservam o <i>-im</i> e o <i>-ī</i>. São poucos, mas aparecem em textos famosos, e quem não os conhece toma <i>turrim</i> por um erro de cópia:</p>
{tabela(['Nome', 'Acusativo sing.', 'Ablativo sing.', 'Observação'], [
    ['<i>sitis, sitis</i> (f.), sede', '<i>sit<b>im</b></i>', '<i>sit<b>ī</b></i>', 'sempre assim; não tem plural'],
    ['<i>turris, turris</i> (f.), torre', '<i>turr<b>im</b></i> ou <i>turr<b>em</b></i>', '<i>turr<b>ī</b></i> ou <i>turr<b>e</b></i>', 'as duas formas ocorrem'],
    ['<i>Tiberis, Tiberis</i> (m.), o rio Tibre', '<i>Tiber<b>im</b></i>', '<i>Tiber<b>ī</b></i>', 'nomes de rios em <i>-is</i> fazem assim'],
    ['<i>nāvis, nāvis</i> (f.), navio', '<i>nāv<b>em</b></i>', '<i>nāv<b>e</b></i> ou <i>nāv<b>ī</b></i>', 'ablativo frequentemente em <i>-ī</i>'],
], 'Nomes com formas em -im e -ī no singular (Bennett § 38.1; Allen e Greenough §§ 75–76; Ravizza n. 29)')}
<p>Não é preciso memorizar mais do que isso agora: diante de um acusativo em <i>-im</i> ou de um ablativo em <i>-ī</i> num nome da terceira declinação, pense num tema em <i>-i</i> e procure no dicionário o nominativo em <i>-is</i>.</p>
<h3>A palavra vīs, "força"</h3>
<p>Um tema em <i>-i</i> merece atenção especial porque é muito frequente e muito irregular: <i>vīs</i>, "força, violência". No singular, só se usam três formas: nominativo <i>vīs</i>, acusativo <i>vim</i> e ablativo <i>vī</i> (o genitivo e o dativo praticamente não ocorrem). O plural se faz de outro tema, <i>vīr-</i>, e significa sobretudo "forças" no sentido de capacidade física ou de tropas: <i>vīrēs, vīrium, vīribus</i> (Bennett § 41; Kennedy § 44, nota 2).</p>
{tabela_declinacao('vīs (f.), "força"; plural vīrēs, "forças"', [
    ('vīs', 'vīr<b>ēs</b>'), ('(não se usa)', 'vīr<b>ium</b>'), ('(não se usa)', 'vīr<b>ibus</b>'),
    ('v<b>im</b>', 'vīr<b>ēs</b>'), ('vīs', 'vīr<b>ēs</b>'), ('v<b>ī</b>', 'vīr<b>ibus</b>')])}
{comparacao('Não confunda: vīs e vir', ['Forma', 'Palavra', 'Análise', 'Tradução'], [
    ['vīr<b>ēs</b>', '<i>vīs</i> (f., 3ª)', 'nom./ac. plural, <i>ī</i> longo', '"as forças"'],
    ['vir<b>ī</b>', '<i>vir, virī</i> (m., 2ª)', 'gen. sing. ou nom. plural, <i>i</i> breve', '"do homem", "os homens"'],
    ['vīr<b>ibus</b>', '<i>vīs</i>', 'dat./abl. plural', '"às forças", "com as forças"'],
    ['vir<b>īs</b>', '<i>vir</i>', 'dat./abl. plural', '"aos homens", "pelos homens"'],
    ['v<b>im</b>', '<i>vīs</i>', 'acusativo singular', '"a força"'],
])}
<p>A primeira sílaba é a pista: em <i>vīs</i> e <i>vīrēs</i> o <i>i</i> é longo; em <i>vir</i> é breve. Num texto sem macrons, olhe as terminações: <i>-ēs, -ium, -ibus</i> são da terceira declinação, logo de <i>vīs</i>; <i>-ī, -ōrum, -īs</i> são da segunda, logo de <i>vir</i>.</p>
'''),
        ('Os adjetivos de segunda classe', f'''
<p>Até aqui, todos os adjetivos que você usou eram de <b>primeira classe</b>: declinam-se pela primeira e pela segunda declinações (<i>bonus, bona, bonum</i>; <i>pulcher, pulchra, pulchrum</i>). Os adjetivos de <b>segunda classe</b> são os que se declinam pela <b>terceira</b> declinação. A gramática do Pe. Ravizza (n. 53) usa esse nome, e ele é cômodo porque divide os adjetivos latinos em apenas dois grupos. O ponto central é este: quase todos os adjetivos de segunda classe seguem a flexão dos <b>temas em <i>-i</i></b>, mesmo quando o tema termina em consoante. Por isso eles têm (Bennett § 67.a; Allen e Greenough §§ 114 e 117):</p>
<ul>
<li>ablativo singular em <b><i>-ī</i></b>, nos três gêneros: <i>fortī</i>, <i>ācrī</i>, <i>fēlīcī</i>;</li>
<li>genitivo plural em <b><i>-ium</i></b>: <i>fortium</i>;</li>
<li>neutro plural em <b><i>-ia</i></b>: <i>fortia</i>;</li>
<li>acusativo plural masculino e feminino em <i>-ēs</i> ou <i>-īs</i>: <i>fortēs</i> ou <i>fortīs</i>.</li>
</ul>
<p>Eles se dividem em três grupos, conforme o número de formas diferentes que têm no nominativo singular.</p>
<h3>Duas terminações: fortis, forte</h3>
<p>É o grupo mais numeroso. O masculino e o feminino são iguais em todos os casos (<i>fortis</i>), e o neutro tem nominativo em <i>-e</i> (<i>forte</i>), como os nomes neutros em <i>-e</i> da seção 2. O dicionário dá as duas formas: <i>fortis, forte</i>, "forte, corajoso". Assim também <i>omnis, omne</i> (todo, cada; no plural, todos), <i>brevis, breve</i> (breve, curto), <i>facilis, facile</i> (fácil), <i>trīstis, trīste</i> (triste), <i>suāvis, suāve</i> (suave, agradável).</p>
{tabela_declinacao('Duas terminações: fortis (m. e f.), forte (n.), "forte, corajoso"', [
    ('fort<b>is</b>', 'fort<b>e</b>', 'fort<b>ēs</b>', 'fort<b>ia</b>'), ('fort<b>is</b>', 'fort<b>is</b>', 'fort<b>ium</b>', 'fort<b>ium</b>'),
    ('fort<b>ī</b>', 'fort<b>ī</b>', 'fort<b>ibus</b>', 'fort<b>ibus</b>'), ('fort<b>em</b>', 'fort<b>e</b>', 'fort<b>ēs</b> (-<b>īs</b>)', 'fort<b>ia</b>'),
    ('fort<b>is</b>', 'fort<b>e</b>', 'fort<b>ēs</b>', 'fort<b>ia</b>'), ('fort<b>ī</b>', 'fort<b>ī</b>', 'fort<b>ibus</b>', 'fort<b>ibus</b>')],
    colunas=('m. e f. · sing.', 'n. · sing.', 'm. e f. · pl.', 'n. · pl.'))}
<h3>Três terminações: ācer, ācris, ācre</h3>
<p>Um pequeno grupo tem uma forma para cada gênero no nominativo singular: masculino em <i>-er</i>, feminino em <i>-is</i>, neutro em <i>-e</i>. Fora do nominativo e do vocativo singular, masculino e feminino coincidem, exatamente como em <i>fortis</i>. O tema perde o <i>e</i> fora do nominativo masculino (<i>ācer</i>, mas <i>ācris, ācrī, ācrem</i>), como <i>pater, patris</i> ou <i>pulcher, pulchrī</i>. <i>Ācer</i> significa "agudo, penetrante; enérgico, impetuoso". Como ele: <i>celeber, celebris, celebre</i> (célebre, frequentado), <i>equester, equestris, equestre</i> (equestre) e os nomes de meses em <i>-ber</i> (<i>September</i>). <i>Celer, celeris, celere</i> (rápido) conserva o <i>e</i> em todas as formas e não tem genitivo plural de adjetivo (Bennett § 68.2).</p>
{tabela_declinacao('Três terminações: ācer (m.), ācris (f.), ācre (n.), "agudo, impetuoso"', [
    ('ācer', 'ācr<b>is</b>', 'ācr<b>e</b>', 'ācr<b>ēs</b>', 'ācr<b>ia</b>'), ('ācr<b>is</b>', 'ācr<b>is</b>', 'ācr<b>is</b>', 'ācr<b>ium</b>', 'ācr<b>ium</b>'),
    ('ācr<b>ī</b>', 'ācr<b>ī</b>', 'ācr<b>ī</b>', 'ācr<b>ibus</b>', 'ācr<b>ibus</b>'), ('ācr<b>em</b>', 'ācr<b>em</b>', 'ācr<b>e</b>', 'ācr<b>ēs</b> (-<b>īs</b>)', 'ācr<b>ia</b>'),
    ('ācer', 'ācr<b>is</b>', 'ācr<b>e</b>', 'ācr<b>ēs</b>', 'ācr<b>ia</b>'), ('ācr<b>ī</b>', 'ācr<b>ī</b>', 'ācr<b>ī</b>', 'ācr<b>ibus</b>', 'ācr<b>ibus</b>')],
    colunas=('m. · sing.', 'f. · sing.', 'n. · sing.', 'm. e f. · pl.', 'n. · pl.'))}
<h3>Uma terminação: fēlīx, ingēns, prūdēns</h3>
<p>O terceiro grupo tem uma só forma de nominativo singular para os três gêneros. Como o nominativo esconde o tema (é a mesma situação de <i>rēx</i>), o dicionário dá o <b>genitivo</b>: <i>fēlīx, fēlīcis</i> (feliz, afortunado); <i>ingēns, ingentis</i> (enorme); <i>prūdēns, prūdentis</i> (sensato, prudente); <i>audāx, audācis</i> (ousado). Quando a entrada traz um nominativo e um genitivo, e não duas ou três formas de nominativo, você sabe que é um adjetivo de uma terminação. O neutro só se distingue no acusativo singular (igual ao nominativo) e no nominativo, acusativo e vocativo plural (em <i>-ia</i>).</p>
{tabela_declinacao('Uma terminação: fēlīx, gen. fēlīcis, "feliz"', [
    ('fēlīx', 'fēlīx', 'fēlīc<b>ēs</b>', 'fēlīc<b>ia</b>'), ('fēlīc<b>is</b>', 'fēlīc<b>is</b>', 'fēlīc<b>ium</b>', 'fēlīc<b>ium</b>'),
    ('fēlīc<b>ī</b>', 'fēlīc<b>ī</b>', 'fēlīc<b>ibus</b>', 'fēlīc<b>ibus</b>'), ('fēlīc<b>em</b>', 'fēlīx', 'fēlīc<b>ēs</b> (-<b>īs</b>)', 'fēlīc<b>ia</b>'),
    ('fēlīx', 'fēlīx', 'fēlīc<b>ēs</b>', 'fēlīc<b>ia</b>'), ('fēlīc<b>ī</b>', 'fēlīc<b>ī</b>', 'fēlīc<b>ibus</b>', 'fēlīc<b>ibus</b>')],
    colunas=('m. e f. · sing.', 'n. · sing.', 'm. e f. · pl.', 'n. · pl.'))}
<p>Do mesmo modo: <i>ingēns, ingentis, ingentī, ingentem</i> (neutro <i>ingēns</i>), <i>ingentī</i>; plural <i>ingentēs</i> (neutro <i>ingentia</i>), <i>ingentium, ingentibus</i>. E <i>prūdēns, prūdentis</i>, plural <i>prūdentēs, prūdentia, prūdentium</i>.</p>
{observacao('Os que se declinam como consonantais', 'Alguns adjetivos de uma terminação não seguem os temas em <i>-i</i>: fazem o ablativo singular em <i>-e</i> e o genitivo plural em <i>-um</i>. Os mais comuns são <i>vetus, veteris</i> (velho, antigo: <i>vetere</i>, <i>veterum</i>, neutro plural <i>vetera</i>), <i>dīves, dīvitis</i> (rico: <i>dīvite</i>, <i>dīvitum</i>), <i>pauper, pauperis</i> (pobre: <i>paupere</i>, <i>pauperum</i>) e <i>prīnceps, prīncipis</i> (o primeiro: <i>prīncipe</i>, <i>prīncipum</i>). Bennett (§ 70.1) e Allen e Greenough (§ 121) os listam; o Pe. Ravizza (n. 53) acrescenta que quase todos são usados como substantivos. Os <b>comparativos</b> (<i>fortior</i>, "mais forte") também seguem a flexão consonantal, e são assunto do capítulo 18. Os <b>particípios presentes</b> (<i>amāns</i>, "que ama"), que se declinam como <i>prūdēns</i>, ficam para o capítulo 29.')}
{dica('<b>Como ler a entrada de um adjetivo.</b> Três formas de nominativo (<i>ācer, ācris, ācre</i>): três terminações. Duas formas (<i>fortis, forte</i>): duas terminações. Um nominativo e um genitivo (<i>fēlīx, -īcis</i>; <i>ingēns, -entis</i>): uma terminação, e o tema está no genitivo. E se a entrada for <i>bonus, -a, -um</i> ou <i>pulcher, -chra, -chrum</i>, é de primeira classe, o assunto do capítulo 5.')}
'''),
        ('A concordância entre declinações diferentes e uma frase autêntica', f'''
<p>No capítulo 9 você viu que um adjetivo de primeira classe não "rima" com um nome da terceira declinação (<i>rēgem bonum</i>). Com os adjetivos de segunda classe acontece o mesmo, na direção contrária: o adjetivo segue sempre a <b>sua</b> declinação, a terceira, qualquer que seja a declinação do nome. A concordância continua sendo de <b>gênero, número e caso</b> (Bennett § 234), nunca de terminação. Veja <i>fortis</i> com nomes de três declinações e dos três gêneros:</p>
{tabela_declinacao('Singular: fēmina fortis (1ª, f.) · puer fortis (2ª, m.) · rēx fortis (3ª, m.) · corpus forte (3ª, n.)', [
    ('fēmina fort<b>is</b>', 'puer fort<b>is</b>', 'rēx fort<b>is</b>', 'corpus fort<b>e</b>'),
    ('fēminae fort<b>is</b>', 'puerī fort<b>is</b>', 'rēgis fort<b>is</b>', 'corporis fort<b>is</b>'),
    ('fēminae fort<b>ī</b>', 'puerō fort<b>ī</b>', 'rēgī fort<b>ī</b>', 'corporī fort<b>ī</b>'),
    ('fēminam fort<b>em</b>', 'puerum fort<b>em</b>', 'rēgem fort<b>em</b>', 'corpus fort<b>e</b>'),
    ('fēmina fort<b>is</b>', 'puer fort<b>is</b>', 'rēx fort<b>is</b>', 'corpus fort<b>e</b>'),
    ('fēminā fort<b>ī</b>', 'puerō fort<b>ī</b>', 'rēge fort<b>ī</b>', 'corpore fort<b>ī</b>')],
    colunas=('fēmina fortis', 'puer fortis', 'rēx fortis', 'corpus forte'))}
{tabela_declinacao('Plural: fēminae fortēs · puerī fortēs · rēgēs fortēs · corpora fortia', [
    ('fēminae fort<b>ēs</b>', 'puerī fort<b>ēs</b>', 'rēgēs fort<b>ēs</b>', 'corpora fort<b>ia</b>'),
    ('fēminārum fort<b>ium</b>', 'puerōrum fort<b>ium</b>', 'rēgum fort<b>ium</b>', 'corporum fort<b>ium</b>'),
    ('fēminīs fort<b>ibus</b>', 'puerīs fort<b>ibus</b>', 'rēgibus fort<b>ibus</b>', 'corporibus fort<b>ibus</b>'),
    ('fēminās fort<b>ēs</b>', 'puerōs fort<b>ēs</b>', 'rēgēs fort<b>ēs</b>', 'corpora fort<b>ia</b>'),
    ('fēminae fort<b>ēs</b>', 'puerī fort<b>ēs</b>', 'rēgēs fort<b>ēs</b>', 'corpora fort<b>ia</b>'),
    ('fēminīs fort<b>ibus</b>', 'puerīs fort<b>ibus</b>', 'rēgibus fort<b>ibus</b>', 'corporibus fort<b>ibus</b>')],
    colunas=('fēmina fortis', 'puer fortis', 'rēx fortis', 'corpus forte'))}
<p>Por que as terminações não "rimam"? Porque cada palavra traz a sua declinação do dicionário: <i>fēmina</i> é da primeira, <i>fortis</i> é da terceira, e nenhuma das duas muda de família para acompanhar a outra. O que o adjetivo copia é a informação gramatical: <i>fēminam</i> é acusativo singular feminino, então o adjetivo vai para o acusativo singular feminino da <b>sua</b> declinação, <i>fortem</i>. Repare em duas armadilhas da tabela: <i>rēge fortī</i> (o nome consonantal faz <i>-e</i>, o adjetivo faz <i>-ī</i>) e <i>rēgum fortium</i> (o nome faz <i>-um</i>, o adjetivo faz <i>-ium</i>). As duas formas estão certas, cada uma na sua declinação. Nome e adjetivo só coincidem por acaso: nas formas em que as duas declinações têm a mesma terminação (<i>rēgis fortis</i>, <i>rēgibus fortibus</i>) ou quando ambos são temas em <i>-i</i> (<i>cīvis fortis</i>, <i>animālia ingentia</i>).</p>
{exemplos([('Fēmina fort<b>is</b> nāvem ingent<b>em</b> videt.', 'A mulher corajosa vê o navio enorme. (<i>fortis</i>: nom. sing. f., com <i>fēmina</i>, da 1ª; <i>ingentem</i>: ac. sing. f., com <i>nāvem</i>)'),
           ('Puer fēlīx in collibus cum ovibus habitat.', 'O menino feliz mora nas colinas com as ovelhas. (<i>fēlīx</i> com <i>puer</i>, da 2ª; <i>collibus</i> e <i>ovibus</i>: ablativos plurais; <i>cum</i> = com; <i>habitat</i> = mora)'),
           ('Rēx omn<b>ēs</b> cīvēs urbis convocat.', 'O rei convoca todos os cidadãos da cidade. (<i>omnēs</i>: ac. pl. m., com <i>cīvēs</i>; <i>convocat</i> = convoca)'),
           ('Agricola ācer bellum ācr<b>e</b> nōn timet.', 'O agricultor enérgico não teme uma guerra violenta. (<i>ācer</i>: nom. sing. m., com <i>agricola</i>, masculino da 1ª; <i>ācre</i>: ac. sing. n., com <i>bellum</i>; <i>timet</i> = teme)')])}
<p>Há uma consequência para a leitura. Os adjetivos de segunda classe desfazem menos ambiguidades que os de primeira: <i>fortēs</i> pode ser nominativo ou acusativo plural, exatamente como <i>cīvēs</i>. Às vezes é o nome que ajuda o adjetivo, e não o contrário:</p>
{diagrama_frase([('Cīvēs fortēs', 'nom. ou ac. pl. · em suspenso'), ('urbis', 'genitivo sing. · "da cidade"'), ('portās ingentēs', 'ac. pl. f. · objeto'), ('claudunt', 'verbo · "fecham"')],
    'Lendo em ordem: <i>Cīvēs fortēs urbis portās ingentēs claudunt</i> = Os cidadãos corajosos fecham as enormes portas da cidade.')}
<p><i>Cīvēs fortēs</i>: nome e adjetivo da terceira, nominativo ou acusativo plural; fica em suspenso. <i>Urbis</i>: genitivo singular, "da cidade". <i>Portās ingentēs</i>: <i>ingentēs</i>, sozinho, seria tão ambíguo quanto <i>fortēs</i>, mas <i>portās</i> (<i>porta, -ae</i>, porta, da primeira declinação) só pode ser acusativo: é o objeto, e o adjetivo vai junto. Ocupado o objeto, <i>cīvēs fortēs</i> é o sujeito, e o verbo plural <i>claudunt</i> confirma.</p>
<h3>Análise gramatical: Mt 19,26</h3>
<p>No Evangelho de Mateus, depois de dizer que é mais fácil um camelo passar pelo buraco de uma agulha do que um rico entrar no Reino, Jesus responde ao espanto dos discípulos com uma frase em dois membros paralelos. Ela reúne dois adjetivos de segunda classe, um no singular e outro no plural, e um adjetivo neutro plural usado como substantivo:</p>
{exemplos([('Apud hominēs hōc impossibile est: apud Deum autem omnia possibilia sunt.', 'Para os homens isto é impossível; para Deus, porém, todas as coisas são possíveis. (Mt 19,26, Vulgata Clementina)')])}
<p>Três palavras merecem uma glosa: <i>apud</i>, preposição de acusativo, "junto de, diante de" e, aqui, "para, aos olhos de"; <i>hōc</i>, "isto", nominativo neutro do demonstrativo <i>hīc, haec, hōc</i> (capítulo 15); e <i>autem</i>, "porém", conjunção que se coloca em segundo lugar no seu membro.</p>
{analise('Mt 19,26, palavra a palavra', [
    ('Apud', 'apud (preposição com acusativo)', 'invariável', 'introduz <i>hominēs</i>: "para os homens"'),
    ('hominēs', 'homō, hominis (m.), ser humano', 'acusativo plural, 3ª consonantal', 'regido por <i>apud</i>'),
    ('hōc', 'hīc, haec, hōc, este, isto (cap. 15)', 'nominativo singular neutro', 'sujeito do primeiro membro'),
    ('impossibile', 'impossibilis, impossibile, impossível (2ª classe, duas terminações)', 'nominativo singular neutro, em <i>-e</i> como <i>forte</i>', 'predicativo: concorda com <i>hōc</i>'),
    ('est', 'sum, esse, ser', '3ª pessoa do singular do presente', 'verbo de ligação'),
    ('apud Deum', 'deus, -ī (m.), Deus', '<i>apud</i> + acusativo singular, 2ª', '"para Deus", em paralelo a <i>apud hominēs</i>'),
    ('autem', 'autem (conjunção)', 'invariável, posposta', 'opõe o segundo membro ao primeiro: "porém"'),
    ('omnia', 'omnis, omne, todo (2ª classe, duas terminações)', 'nominativo plural neutro, em <i>-ia</i>', 'sujeito, usado como substantivo: "todas as coisas"'),
    ('possibilia', 'possibilis, possibile, possível (2ª classe)', 'nominativo plural neutro, em <i>-ia</i>', 'predicativo: concorda com <i>omnia</i>'),
    ('sunt', 'sum, esse, ser', '3ª pessoa do plural do presente', 'verbo de ligação, plural como o sujeito'),
])}
<p>A frase é um exercício de concordância em miniatura. No primeiro membro, o sujeito <i>hōc</i> é neutro singular, e o predicativo vai para o neutro singular de <i>impossibilis</i>: <i>impossibile</i>, com o <i>-e</i> de <i>forte</i>. No segundo, o sujeito <i>omnia</i> é neutro plural, e o predicativo vai para o neutro plural: <i>possibilia</i>, com o <i>-ia</i> dos temas em <i>-i</i>, e o verbo passa a <i>sunt</i>. <i>Omnia</i>, sem nome expresso, é um uso muito comum: o neutro plural de um adjetivo, sozinho, designa "coisas" com aquela qualidade, e <i>omnia</i> é "todas as coisas, tudo" (Bennett § 236). Repare ainda que nenhum desses <i>-ia</i> é feminino singular da primeira declinação: o tema <i>omni-</i> e o verbo plural mostram que são neutros plurais.</p>
<p>Dois trechos curtos da Vulgata mostram a mesma gramática; você já pode lê-los sozinho:</p>
{exemplos([('Suāvis Dominus ūniversīs.', 'O Senhor é bondoso para com todos. (Sl 144,9 (145,9), na numeração da Vulgata, início do versículo; <i>suāvis</i>, de 2ª classe, concorda com <i>Dominus</i>, da 2ª declinação, em nominativo singular masculino; o verbo <i>est</i> fica subentendido; <i>ūniversīs</i>, dativo plural de <i>ūniversus, -a, -um</i>, "todos")'),
           ('Vānitās vānitātum, et omnia vānitās.', 'Vaidade das vaidades, e tudo é vaidade. (Ecl 1,2, fim do versículo; <i>vānitās, vānitātis</i>, f., é consonantal: genitivo plural <i>vānitātum</i>, em <i>-um</i>; <i>omnia</i> é o neutro plural "todas as coisas", sujeito de <i>est</i> subentendido)')])}
<p>No segundo exemplo, compare as duas formas lado a lado: <i>vānitātum</i>, genitivo plural de um nome consonantal, em <i>-um</i>, e <i>omnia</i>, neutro plural de um adjetivo de tema em <i>-i</i>, em <i>-ia</i>. É o contraste deste capítulo numa linha. E repare que <i>vānitās</i>, predicativo de <i>omnia</i>, fica no feminino singular: um <b>nome</b> predicativo não muda de gênero nem de número para concordar; só o adjetivo concorda.</p>
<h3>Resumo</h3>
<ul>
<li>Temas em <i>-i</i>: parissílabos em <i>-is</i> e <i>-ēs</i> (<i>cīvis, nūbēs</i>); imparissílabos com duas consoantes antes do <i>-is</i> do genitivo (<i>urbs, urbis</i>; <i>nox, noctis</i>); neutros em <i>-e, -al, -ar</i> (<i>mare, animal, exemplar</i>).</li>
<li>Diferem dos consonantais no genitivo plural (<i>-ium</i>), no acusativo plural opcional em <i>-īs</i> e, nos neutros, no ablativo singular (<i>-ī</i>) e no plural (<i>-ia</i>).</li>
<li>Exceções a guardar: <i>canis, iuvenis, pater, māter, frāter</i> fazem <i>-um</i>; <i>sitis, turris, Tiberis</i> têm acusativo em <i>-im</i>; <i>vīs</i> faz <i>vim, vī</i> e o plural <i>vīrēs, vīrium, vīribus</i>.</li>
<li>Adjetivos de segunda classe: três terminações (<i>ācer, ācris, ācre</i>), duas (<i>fortis, forte</i>), uma (<i>fēlīx, -īcis</i>); ablativo em <i>-ī</i>, genitivo plural em <i>-ium</i>, neutro plural em <i>-ia</i>. Consonantais: <i>vetus, dīves, pauper, prīnceps</i>.</li>
<li>Concordância: gênero, número e caso, nunca terminação: <i>fēmina fortis, puer fortis, rēx fortis, corpus forte</i>.</li>
</ul>
<p>No próximo capítulo, a quarta e a quinta declinações fecham o quadro dos nomes latinos, e as cinco declinações aparecem lado a lado.</p>
'''),
    ],
    erros_comuns=[
        ('Fazer o genitivo plural em <i>-um</i> num tema em <i>-i</i> (*<i>cīvum</i>, *<i>urbum</i>, *<i>animālum</i>) ou em <i>-ium</i> num consonantal (*<i>rēgium</i>, *<i>mīlitium</i>).', 'O genitivo plural é justamente a forma que separa as duas famílias. Antes de escrevê-lo, aplique o teste da seção 2 à entrada do dicionário: parissílabo em <i>-is/-ēs</i>, duas consoantes antes de <i>-is</i> ou neutro em <i>-e, -al, -ar</i> dão <i>-ium</i> (<i>cīvium, urbium, animālium</i>); o resto dá <i>-um</i> (<i>rēgum, mīlitum</i>). Depois confira as exceções (<i>canum, iuvenum, patrum</i>).'),
        ('Fazer o plural dos neutros de tema em <i>-i</i> em <i>-a</i> (*<i>animāla</i>, *<i>mara</i>) ou o ablativo singular em <i>-e</i> (*<i>animāle</i>; <i>in mare</i> em vez do normal <i>in marī</i>).', 'Os neutros em <i>-e, -al, -ar</i> são os temas em <i>-i</i> mais fiéis ao <i>i</i>: plural <i>animālia, maria</i>, ablativo <i>animālī, marī</i>. "No mar" é <i>in marī</i> (Allen e Greenough § 68.a; Bennett § 39). O ablativo <i>mare</i> existe, mas é raro (Bennett § 39.2; Kennedy § 47, nota); fora dele, o <i>-e</i> de <i>mare</i> é do nominativo, acusativo e vocativo singular.'),
        ('Dar ao adjetivo de segunda classe o ablativo <i>-e</i> do nome (*<i>cum mīlite forte</i>, *<i>in urbe ingente</i>).', 'O nome consonantal ou misto faz <i>-e</i>, mas o adjetivo de segunda classe faz <i>-ī</i>: <i>cum mīlite fortī</i>, <i>in urbe ingentī</i>. As terminações diferentes, lado a lado, são o normal. A exceção são os poucos adjetivos consonantais (<i>vetere, dīvite, paupere</i>), que você reconhece pela lista da seção 5.'),
        ('Fazer o adjetivo de segunda classe "rimar" com o nome: *<i>fēmina forta</i>, *<i>puer fortus</i>, *<i>bellum fortum</i>, *<i>puella ācra</i>.', 'O adjetivo segue a sua declinação, não a do nome. <i>Fortis</i> só tem as formas <i>fortis</i> (m. e f.) e <i>forte</i> (n.) no nominativo: <i>fēmina fortis</i>, <i>puer fortis</i>, <i>bellum forte</i>. Com <i>ācer</i>, o feminino é <i>ācris</i>: <i>puella ācris</i>. Pergunte qual é o gênero, o número e o caso do nome e tome essa forma no paradigma do adjetivo.'),
        ('Confundir <i>vīrēs</i> (forças) com <i>virī</i> (homens), ou <i>vīribus</i> com <i>virīs</i>.', 'São palavras diferentes: <i>vīs</i> (f., 3ª, "força"), plural <i>vīrēs, vīrium, vīribus</i>; e <i>vir, virī</i> (m., 2ª, "homem"), plural <i>virī, virōrum, virīs</i>. Terminações de terceira declinação (<i>-ēs, -ium, -ibus</i>) apontam para <i>vīs</i>; de segunda (<i>-ī, -ōrum, -īs</i>), para <i>vir</i>. Com macrons, o <i>ī</i> longo de <i>vīrēs</i> também resolve.'),
        ('Ler <i>cīvīs</i>, <i>omnīs</i> ou <i>fortīs</i> como dativo ou ablativo plural, por causa do <i>-īs</i> de <i>bonīs, rosīs</i>.', 'Num nome ou adjetivo da terceira declinação, <i>-īs</i> é a variante antiga do <b>acusativo plural</b> (<i>cīvīs</i> = <i>cīvēs</i>); o dativo e ablativo plural são sempre <i>-ibus</i>. E não confunda com o nominativo e genitivo singular <i>cīvis</i>, de <i>i</i> breve. Identifique primeiro a declinação; só depois leia a terminação.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Uma frase com três declinações',
            'Leia em voz alta e analise, na ordem latina: <i lang="la">In marī ingentī nāvis parva nautās fortēs portat.</i> Vocabulário: <i>mare, maris</i> (n.), mar; <i>ingēns, ingentis</i>, enorme; <i>nāvis, nāvis</i> (f.), navio; <i>parvus, -a, -um</i>, pequeno; <i>nauta, -ae</i> (m.), marinheiro; <i>fortis, forte</i>, corajoso; <i>portat</i>, leva, transporta.', [
            ('Qual é o verbo, e o que ele faz esperar?', '<i>Portat</i>, 3ª pessoa do singular: espera-se um sujeito singular e um objeto no acusativo (quem ou o que é levado).'),
            ('Que forma é <i>marī</i>, e com que palavra concorda <i>ingentī</i>?', '<i>Mare</i> é neutro em <i>-e</i>, tema em <i>-i</i>: o ablativo singular é <i>marī</i>. Regido por <i>in</i>, indica o lugar onde: "no mar". <i>Ingentī</i> é dativo ou ablativo singular de <i>ingēns</i>; concorda com <i>marī</i>: "no mar enorme". Aqui nome e adjetivo coincidem na terminação porque ambos são temas em <i>-i</i> da terceira declinação.'),
            ('<i>Nāvis</i> é nominativo ou genitivo?', 'Sozinho, <i>nāvis</i> pode ser as duas coisas (nos parissílabos, nominativo = genitivo). Quem decide é <i>parva</i>, com <i>a</i> breve: nominativo (ou vocativo) singular feminino, ou neutro plural, que não serve para <i>nāvis</i>, feminino; o ablativo seria <i>parvā</i>. Logo, <i>nāvis parva</i> é nominativo, o sujeito singular que o verbo pedia: "um navio pequeno".'),
            ('E <i>nautās fortēs</i>?', '<i>Fortēs</i>, sozinho, seria nominativo ou acusativo plural. Mas <i>nautās</i>, da primeira declinação, só pode ser acusativo plural, e <i>fortēs</i> concorda com ele: masculino, porque <i>nauta</i> é masculino, embora seja da primeira declinação. É o objeto: "marinheiros corajosos".'),
            ('Monte a tradução.', '"No mar enorme, um navio pequeno leva marinheiros corajosos." Nenhuma terminação "rima" em <i>nāvis parva</i> nem em <i>nautās fortēs</i>, e todas estão certas.'),
        ]),
        pratica_guiada('Prática guiada 2 · Do dicionário ao genitivo plural',
            'Para cada entrada, decida se o genitivo plural termina em <i>-um</i> ou em <i>-ium</i>, aplicando o teste da seção 2 passo a passo.', [
            ('<i>hostis, hostis</i> (m.), inimigo', 'Não é neutro. Nominativo e genitivo têm duas sílabas cada (<i>hos-tis</i>, <i>hos-tis</i>): parissílabo em <i>-is</i>, regra 1. Não está na lista de exceções. Genitivo plural <i>hostium</i>, "dos inimigos".'),
            ('<i>mōns, montis</i> (m.), monte', 'Não é neutro. Imparissílabo (<i>mōns</i>, uma sílaba; <i>mon-tis</i>, duas). Tirando <i>-is</i> do genitivo, sobra <i>mont-</i>, com duas consoantes no fim: regra 2. Genitivo plural <i>montium</i>.'),
            ('<i>lēx, lēgis</i> (f.), lei', 'Imparissílabo; tirando <i>-is</i>, sobra <i>lēg-</i>, com uma só consoante. Nenhuma das regras se aplica: é consonantal, como no capítulo 9. Genitivo plural <i>lēgum</i>.'),
            ('<i>exemplar, exemplāris</i> (n.), modelo', 'Neutro em <i>-ar</i>: regra 3. Genitivo plural <i>exemplārium</i>; e, além disso, ablativo singular <i>exemplārī</i> e plural <i>exemplāria</i>.'),
            ('<i>canis, canis</i> (m. e f.), cão', 'Pela regra 1 seria <i>-ium</i>, mas <i>canis</i> está na lista de exceções: na verdade é consonantal (Bennett § 38.2). Genitivo plural <i>canum</i>. É por isso que a conferência das exceções é o último passo do teste.'),
            ('<i>fēlīx, fēlīcis</i>, feliz (adjetivo)', 'É um adjetivo de segunda classe, e os adjetivos de segunda classe seguem os temas em <i>-i</i>, embora o tema <i>fēlīc-</i> tenha uma só consoante: genitivo plural <i>fēlīcium</i>. As regras de contar consoantes valem para os <b>nomes</b>; para os adjetivos, a regra é <i>-ium</i>, salvo os consonantais da lista (<i>vetus, dīves, pauper, prīnceps</i>).'),
        ], 'Conclusão: o teste tem sempre a mesma ordem: é adjetivo? é neutro em -e, -al, -ar? é parissílabo? tem duas consoantes antes de -is? e, por fim, está entre as exceções?'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Genitivo plural', 'Dê o genitivo plural de cada nome e diga por quê (regra ou exceção).', [
            ('<i>nūbēs, nūbis</i> (f.), nuvem', '<i>nūbium</i>: parissílabo em <i>-ēs</i> (regra 1).'),
            ('<i>mīles, mīlitis</i> (m.), soldado', '<i>mīlitum</i>: imparissílabo de uma só consoante antes de <i>-is</i> (<i>mīlit-</i>); consonantal.'),
            ('<i>nox, noctis</i> (f.), noite', '<i>noctium</i>: duas consoantes antes de <i>-is</i> (<i>noct-</i>), regra 2.'),
            ('<i>animal, animālis</i> (n.), animal', '<i>animālium</i>: neutro em <i>-al</i> (regra 3).'),
            ('<i>pater, patris</i> (m.), pai', '<i>patrum</i>: não tem nominativo em <i>-is</i> ou <i>-ēs</i>, e a regra 2 não se aplica porque não é imparissílabo (<i>pa-ter</i>, <i>pa-tris</i>); é consonantal. Kennedy (§ 49) o lista entre as exceções aparentes.'),
            ('<i>corpus, corporis</i> (n.), corpo', '<i>corporum</i>: neutro, mas não em <i>-e, -al, -ar</i>; tema consonantal <i>corpor-</i> (capítulo 9).'),
            ('<i>ars, artis</i> (f.), arte', '<i>artium</i>: <i>art-</i>, duas consoantes (regra 2).'),
            ('<i>iuvenis, iuvenis</i> (m.), jovem', '<i>iuvenum</i>: exceção à regra 1, como <i>canis</i>.'),
            ('<i>cīvis, cīvis</i> (m. e f.), cidadão', '<i>cīvium</i>: parissílabo em <i>-is</i> (regra 1).'),
            ('<i>flūmen, flūminis</i> (n.), rio', '<i>flūminum</i>: neutro em <i>-men</i>, consonantal (capítulo 9).'),
        ]),
        exercicio('Exercício 2 · Caso e número', 'Dê o caso e o número de cada forma (todas as possibilidades) e o nominativo de dicionário.', [
            ('<i>urbium</i>', 'Genitivo plural de <i>urbs, urbis</i> (f.): "das cidades".'),
            ('<i>marī</i>', 'Dativo ou ablativo singular de <i>mare, maris</i> (n.). Com <i>in</i>, ablativo: <i>in marī</i>, "no mar".'),
            ('<i>animālia</i>', 'Nominativo, acusativo ou vocativo plural de <i>animal, animālis</i> (n.). Não é feminino singular da 1ª.'),
            ('<i>cīvīs</i> (com <i>ī</i> longo)', 'Acusativo plural de <i>cīvis</i>, variante de <i>cīvēs</i>. Não é dativo/ablativo plural (seria <i>cīvibus</i>) nem nominativo singular (<i>cīvis</i>, com <i>i</i> breve).'),
            ('<i>nocte</i>', 'Ablativo singular de <i>nox, noctis</i> (f.). Os nomes da regra 2 fazem o ablativo em <i>-e</i>.'),
            ('<i>vim</i>', 'Acusativo singular de <i>vīs</i> (f.), "força".'),
            ('<i>turrim</i>', 'Acusativo singular de <i>turris, turris</i> (f.), torre; variante de <i>turrem</i>.'),
            ('<i>montēs</i>', 'Nominativo, acusativo ou vocativo plural de <i>mōns, montis</i> (m.).'),
            ('<i>vīribus</i>', 'Dativo ou ablativo plural de <i>vīs</i>, com o tema do plural <i>vīr-</i>: "às forças, com as forças". Não confunda com <i>virīs</i>, de <i>vir</i>.'),
            ('<i>fortī</i>', 'Dativo ou ablativo singular de <i>fortis, forte</i>, em qualquer gênero. Só o nome com que concorda decide o gênero.'),
        ]),
        exercicio('Exercício 3 · Decline com o adjetivo', 'Decline no singular e no plural, em voz alta e por escrito, nome e adjetivo juntos.', [
            ('<i>cīvis fēlīx</i> (<i>cīvis, cīvis</i>, m.; <i>fēlīx, fēlīcis</i>), "o cidadão feliz"', 'Singular: cīvis fēlīx, cīvis fēlīcis, cīvī fēlīcī, cīvem fēlīcem, cīvis fēlīx, cīve (cīvī) fēlīcī. Plural: cīvēs fēlīcēs, cīvium fēlīcium, cīvibus fēlīcibus, cīvēs (-īs) fēlīcēs (-īs), cīvēs fēlīcēs, cīvibus fēlīcibus. Note o ablativo: o nome tem em geral <i>-e</i>, o adjetivo sempre <i>-ī</i>.'),
            ('<i>animal ingēns</i> (<i>animal, animālis</i>, n.; <i>ingēns, ingentis</i>), "o animal enorme"', 'Singular: animal ingēns, animālis ingentis, animālī ingentī, animal ingēns, animal ingēns, animālī ingentī. Plural: animālia ingentia, animālium ingentium, animālibus ingentibus, animālia ingentia, animālia ingentia, animālibus ingentibus. Neutro dos dois lados: nominativo = acusativo = vocativo, plural em <i>-ia</i>, ablativo em <i>-ī</i>.'),
            ('<i>fīlia prūdēns</i> (<i>fīlia, -ae</i>, f.; <i>prūdēns, prūdentis</i>), "a filha sensata"', 'Singular: fīlia prūdēns, fīliae prūdentis, fīliae prūdentī, fīliam prūdentem, fīlia prūdēns, fīliā prūdentī. Plural: fīliae prūdentēs, fīliārum prūdentium, fīliīs prūdentibus, fīliās prūdentēs, fīliae prūdentēs, fīliīs prūdentibus. O nome é da 1ª, o adjetivo da 3ª; nenhuma terminação se repete, e todas concordam.'),
        ]),
        exercicio('Exercício 4 · Faça concordar', 'Escreva o adjetivo entre parênteses na forma que concorda com o nome, e explique.', [
            ('<i>fēminam ___</i> (fortis)', '<i>fortem</i>: acusativo singular feminino da 3ª declinação, embora <i>fēminam</i> seja da 1ª.'),
            ('<i>puerō ___</i> (fēlīx), dativo', '<i>fēlīcī</i>: dativo singular masculino; o tema <i>fēlīc-</i> vem do genitivo.'),
            ('<i>corpora ___</i> (omnis)', '<i>omnia</i>: nominativo ou acusativo plural neutro, em <i>-ia</i> (o nome consonantal faz <i>-a</i>).'),
            ('<i>agricolae ___</i> (ācer), nominativo plural', '<i>ācrēs</i>: <i>agricola</i> é masculino, embora da 1ª; plural masculino de <i>ācer</i>.'),
            ('<i>puer ___</i> (ācer)', '<i>ācer</i>: nominativo singular masculino, a forma de dicionário.'),
            ('<i>puellae ___</i> (ācer), genitivo singular', '<i>ācris</i>: genitivo singular, igual nos três gêneros. Não *<i>ācrae</i>: o adjetivo não passa para a 1ª declinação.'),
            ('<i>in bellō ___</i> (ingēns)', '<i>ingentī</i>: ablativo singular neutro; os adjetivos de segunda classe fazem o ablativo em <i>-ī</i>.'),
            ('<i>rēgum ___</i> (prūdēns)', '<i>prūdentium</i>: genitivo plural masculino; o nome consonantal faz <i>-um</i>, o adjetivo, <i>-ium</i>.'),
            ('<i>cum virō ___</i> (vetus), "com o homem velho"', '<i>vetere</i>: ablativo singular masculino. <i>Vetus</i> é um dos adjetivos que se declinam como consonantais, com ablativo em <i>-e</i> (Bennett § 70.1).'),
            ('<i>urbem ___</i> (omnis), "cada cidade" / "a cidade inteira"', '<i>omnem</i>: acusativo singular feminino.'),
        ]),
        exercicio('Exercício 5 · Traduza lendo em ordem', 'Anote caso e número de cada palavra antes de traduzir. Vocabulário além das tabelas do capítulo: <i>timent</i>, temem; <i>habitat</i>, mora; <i>nāvigant</i>, navegam; <i>dat</i>, dá; <i>praemium, -ī</i> (n.), prêmio, recompensa; <i>rēgīna, -ae</i>, rainha; <i>nōn</i>, não.', [
            ('<i>Nautae fortēs mare nōn timent.</i>', '<i>Nautae</i> (nom. pl., 1ª, m.), <i>fortēs</i> (concorda com <i>nautae</i>: nom. pl. m.), <i>mare</i> (ac. sing. n.; nos neutros, ac. = nom.), <i>timent</i>: Os marinheiros corajosos não temem o mar.'),
            ('<i>Puer animālia omnia amat.</i>', '<i>Puer</i> (nom. sing., sujeito de <i>amat</i>), <i>animālia omnia</i> (ac. pl. n., o objeto; os dois em <i>-ia</i>): O menino ama todos os animais.'),
            ('<i>In marī ingentī nāvēs parvae nāvigant.</i>', '<i>In marī ingentī</i> (abl. sing. n., lugar onde), <i>nāvēs parvae</i> (nom. pl. f.; <i>parvae</i> exclui o acusativo), <i>nāvigant</i>: Navios pequenos navegam no mar enorme.'),
            ('<i>Pars cīvium in monte habitat.</i>', '<i>Pars</i> (nom. sing., sujeito; por isso o verbo no singular), <i>cīvium</i> (gen. pl., "dos cidadãos"), <i>in monte</i> (abl. sing. de <i>mōns</i>, em <i>-e</i>): Uma parte dos cidadãos mora no monte.'),
            ('<i>Hostēs vim urbis timent.</i>', '<i>Hostēs</i> (nom. pl.: <i>vim</i> já é o acusativo, e <i>timent</i> é plural), <i>vim</i> (ac. sing. de <i>vīs</i>), <i>urbis</i> (gen. sing.): Os inimigos temem a força da cidade.'),
            ('<i>Rēgīna prūdēns cīvibus fortibus praemia dat.</i>', '<i>Rēgīna prūdēns</i> (nom. sing. f.), <i>cīvibus fortibus</i> (dat. pl., a quem se dá; sem preposição, não é ablativo de lugar), <i>praemia</i> (ac. pl. n., 2ª): A rainha sensata dá recompensas aos cidadãos corajosos.'),
        ]),
        exercicio('Exercício 6 · Do português para o latim', 'Traduza, usando o vocabulário do capítulo e verbos na 3ª pessoa do presente. Vocabulário: <i>amat</i>, ama; <i>videt</i>, vê; <i>timent</i>, temem; <i>nāvigat</i>, navega; <i>cantat</i>, canta; <i>patria, -ae</i>, pátria; <i>silva, -ae</i>, floresta; <i>poēta, -ae</i> (m.), poeta.', [
            ('O soldado corajoso ama a pátria.', '<i>Mīles fortis patriam amat.</i> <i>Fortis</i> concorda com <i>mīles</i> (nom. sing. m.); <i>patriam</i>, acusativo.'),
            ('Os animais da floresta temem o fogo.', '<i>Animālia silvae īgnem timent.</i> <i>Animālia</i>: nom. pl. n. em <i>-ia</i>; <i>silvae</i>: genitivo; <i>īgnem</i>: ac. sing. de <i>īgnis</i>.'),
            ('A menina feliz vê o mar.', '<i>Puella fēlīx mare videt.</i> <i>Fēlīx</i> serve aos três gêneros no nominativo; <i>mare</i>, neutro, tem o acusativo igual ao nominativo.'),
            ('O poeta canta as artes dos cidadãos.', '<i>Poēta artēs cīvium cantat.</i> <i>Artēs</i>: ac. pl. de <i>ars</i>; <i>cīvium</i>: gen. pl. em <i>-ium</i> (parissílabo).'),
            ('O marinheiro corajoso navega num navio enorme.', '<i>Nauta fortis in nāve ingentī nāvigat</i> (ou <i>in nāvī ingentī</i>: <i>nāvis</i> admite os dois ablativos). O adjetivo é sempre <i>ingentī</i>; <i>fortis</i> é masculino porque <i>nauta</i> é masculino.'),
        ]),
    ],
    leituras=['d-ooge-latin-for-beginners', 'sonnenschein-pro-patria-a-latin-story-for-beginners', 'lhomond-epitome-historiae-sacrae', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'ravizza-gramatica-latina', 'bennett-new-latin-grammar'],
    leituras_nota='Latin for Beginners, de D\'Ooge, tem lições próprias sobre os temas em -i e os adjetivos da terceira declinação, com exercícios graduados para praticar o que este capítulo explicou. Pro Patria e o Epitome Historiae Sacrae, de Lhomond, são boas leituras corridas neste ponto: procure nelas os genitivos plurais em -ium e os ablativos em -ī de adjetivos como omnis e fortis. Na Vulgata, leia Mt 19,23–26 e os primeiros versículos do Eclesiastes. Para consultar os paradigmas, Ravizza (n. 28–32 e 53) e Bennett (§§ 37–41 e 67–70).',
)
