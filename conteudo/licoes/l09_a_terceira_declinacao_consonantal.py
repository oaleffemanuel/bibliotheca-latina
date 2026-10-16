from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='09-a-terceira-declinacao-temas-consonantais', titulo='A terceira declinação: temas consonantais',
    titulo_latim='Dē tertiā dēclīnātiōne (I)', tempo='60 min',
    resumo='A declinação dos nominativos imprevisíveis: por que ela só se aprende pelo genitivo, as terminações dos temas consonantais (masculino e feminino, e neutro), os três tipos principais de nominativo, as tendências de gênero e a concordância com os adjetivos de primeira classe, que é onde o iniciante mais erra.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['3ª declinação', 'temas consonantais', 'genitivo e tema', 'paradigma masculino/feminino', 'paradigma neutro', 'regra dos neutros', 'temas em muda', 'temas em líquida e nasal', 'temas em -s e rotacismo', 'gênero na 3ª declinação', 'concordância com adjetivos de primeira classe', 'temas em -i (menção)', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulos 3 a 5: os seis casos, a primeira e a segunda declinações e os adjetivos de primeira classe (<i>bonus, -a, -um</i>). Ajuda ter feito o capítulo 7, sobre como ler uma entrada de dicionário.',
                       licoes=['03-introducao-aos-casos', '04-a-primeira-declinacao', '05-a-segunda-declinacao', '07-como-usar-o-dicionario']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 8.1 (rotacismo: genus, generis), § 19.1, 3–4 (vocativo = nominativo; neutros com N = Ac e plural em -a; Ac pl = N pl na 3ª), §§ 28–36 (temas consonantais: prīnceps, dux, mīles, victor, leō, nōmen, mōs, genus, honor), §§ 37–40 (temas em -i e mistos, só para a menção), §§ 43–46 (gênero e exceções: sal, sōl, arbor), § 234 (concordância do adjetivo)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 15.4 (rotacismo), §§ 53–55 (classes de temas; o nominativo deriva do tema: rēx, rēgis), §§ 56–57 (temas em muda m./f.), §§ 61–62 (temas em líquida e nasal m./f.: pater, legiō, virgō), §§ 63–64 (neutros: nōmen, genus, opus), §§ 84–87 (gênero), § 286 (concordância)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§§ 38–42 (temas em gutural, dental, labial, -s e líquida; rēx, rēg-; corpus, corpor-); § 43 (temas nasais: leō, virgō, nōmen; homō, homin-); §§ 51–53 (gênero dos temas consonantais)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 27 (desinências da 3ª declinação; genitivo sempre em -is), n. 28 (imparissílabos: lex, legis; arbor, arboris)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Lucas 2,14 e Mateus 5,13–14', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Lucam', nota='frases autênticas da seção 6, conferidas na Wikisource latina; ortografia adaptada (ae por æ) e macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Explicar por que um nome da terceira declinação só pode ser declinado a partir do genitivo, e extrair o tema de uma entrada de dicionário (<i>rēx, rēgis</i> → <i>rēg-</i>).',
        'Declinar nomes masculinos, femininos e neutros de tema consonantal, aplicando a regra dos neutros.',
        'Reconhecer os três tipos principais de nominativo (muda + <i>-s</i>; líquida e nasal; tema em <i>-s</i> com rotacismo).',
        'Usar as tendências de gênero com cautela, conferindo sempre o dicionário.',
        'Fazer concordar um adjetivo de primeira classe com um nome da terceira declinação (<i>rēx bonus</i>, <i>lēx bona</i>, <i>corpus magnum</i>) e usar essa concordância para ler frases ambíguas.',
    ],
    secoes=[
        ('Por que a terceira declinação exige o genitivo', f'''
<p>Nas duas primeiras declinações, o nominativo já entrega quase tudo: quem vê <i>rosa</i> ou <i>dominus</i> sabe declinar a palavra inteira. A terceira declinação não é assim. Ela reúne nomes com nominativos de todo tipo, terminados em <i>-x</i>, <i>-s</i>, <i>-r</i>, <i>-ō</i>, <i>-n</i>, <i>-us</i> e outros, e o nominativo, muitas vezes, <b>esconde o tema</b> da palavra. O tema é a parte que fica constante e à qual se juntam as terminações dos casos. Em <i>rēx</i> ("rei"), por exemplo, nada indica que o tema seja <i>rēg-</i>; isso só aparece no genitivo <i>rēgis</i>, e todas as outras formas seguem o genitivo: <i>rēgī, rēgem, rēge, rēgēs, rēgum, rēgibus</i>.</p>
<p>É por isso que o dicionário dá sempre o nominativo <b>e</b> o genitivo, e é por isso que você deve aprender os dois juntos, como uma unidade. O procedimento é sempre o mesmo: tome o genitivo singular, tire a terminação <i>-is</i> e o que sobra é o tema. A maioria desses nomes é o que a gramática do Pe. Ravizza chama de <b>imparissílabos</b>, porque o genitivo tem uma sílaba a mais que o nominativo (<i>lēx</i>, uma sílaba; <i>lē-gis</i>, duas). Veja como o genitivo revela o que o nominativo esconde:</p>
{tabela(['Nominativo', 'Genitivo', 'Tema', 'Significado', 'O que o nominativo escondia'], [
    ['rēx', 'rēg<b>is</b>', 'rēg-', 'rei', 'o <i>g</i> (fundido com o <i>-s</i> em <i>x</i>)'],
    ['lēx', 'lēg<b>is</b>', 'lēg-', 'lei', 'o <i>g</i>'],
    ['vōx', 'vōc<b>is</b>', 'vōc-', 'voz', 'o <i>c</i>'],
    ['mīles', 'mīlit<b>is</b>', 'mīlit-', 'soldado', 'o <i>t</i>, e a vogal <i>i</i>'],
    ['pater', 'patr<b>is</b>', 'patr-', 'pai', 'a perda do <i>e</i> fora do nominativo'],
    ['labor', 'labōr<b>is</b>', 'labōr-', 'trabalho, fadiga', 'a vogal longa <i>ō</i>'],
    ['homō', 'homin<b>is</b>', 'homin-', 'ser humano, homem', 'o <i>n</i> e a vogal <i>i</i>'],
    ['nōmen', 'nōmin<b>is</b>', 'nōmin-', 'nome', 'a vogal <i>i</i>'],
    ['flūmen', 'flūmin<b>is</b>', 'flūmin-', 'rio', 'a vogal <i>i</i>'],
    ['corpus', 'corpor<b>is</b>', 'corpor-', 'corpo', 'o <i>r</i> e a vogal <i>o</i>'],
], 'Do genitivo ao tema', latim_cols=(0, 1, 2))}
<p>O genitivo em <i>-is</i> é também a marca que identifica a declinação, assim como <i>-ae</i> identifica a primeira e <i>-ī</i> a segunda. Diante de uma entrada como <i>corpus, corporis</i>, o <i>-is</i> diz "terceira declinação", e o <i>-us</i> do nominativo, que parece da segunda, não decide nada.</p>
{dica('<b>Como memorizar.</b> Recite sempre em par: <i>rēx, rēgis</i>; <i>homō, hominis</i>; <i>corpus, corporis</i>. Quem decora só <i>rēx</i> terá de adivinhar o resto; quem decora <i>rēx, rēgis</i> já sabe declinar a palavra inteira. O português ajuda: muitas palavras portuguesas vêm do tema, não do nominativo latino: <i>régio</i> (de <i>rēg-</i>), <i>legal</i> (de <i>lēg-</i>), <i>vocal</i> (de <i>vōc-</i>), <i>militar</i> (de <i>mīlit-</i>), <i>corporal</i> (de <i>corpor-</i>), <i>nominal</i> (de <i>nōmin-</i>).')}
'''),
        ('As terminações: masculino e feminino, e neutro', f'''
<p>Encontrado o tema, as terminações são poucas e regulares. Os nomes masculinos e femininos têm um único jogo de terminações; os neutros diferem só em três casos de cada número. Primeiro os modelos masculinos: <i>rēx</i> e <i>mīles</i>.</p>
{tabela_declinacao('Terceira declinação, masculino e feminino: rēx, rēgis (m.), "rei" · mīles, mīlitis (m.), "soldado"', [
    ('rēx', 'rēg<b>ēs</b>', 'mīles', 'mīlit<b>ēs</b>'), ('rēg<b>is</b>', 'rēg<b>um</b>', 'mīlit<b>is</b>', 'mīlit<b>um</b>'),
    ('rēg<b>ī</b>', 'rēg<b>ibus</b>', 'mīlit<b>ī</b>', 'mīlit<b>ibus</b>'), ('rēg<b>em</b>', 'rēg<b>ēs</b>', 'mīlit<b>em</b>', 'mīlit<b>ēs</b>'),
    ('rēx', 'rēg<b>ēs</b>', 'mīles', 'mīlit<b>ēs</b>'), ('rēg<b>e</b>', 'rēg<b>ibus</b>', 'mīlit<b>e</b>', 'mīlit<b>ibus</b>')],
    colunas=('rēx · sing.', 'rēx · pl.', 'mīles · sing.', 'mīles · pl.'))}
<p>Um feminino declina-se exatamente igual: <i>lēx, lēgis</i> faz <i>lēgī, lēgem, lēge</i>; <i>lēgēs, lēgum, lēgibus</i>. Agora os neutros, <i>corpus</i> e <i>nōmen</i>:</p>
{tabela_declinacao('Terceira declinação, neutro: corpus, corporis (n.), "corpo" · nōmen, nōminis (n.), "nome"', [
    ('corpus', 'corpor<b>a</b>', 'nōmen', 'nōmin<b>a</b>'), ('corpor<b>is</b>', 'corpor<b>um</b>', 'nōmin<b>is</b>', 'nōmin<b>um</b>'),
    ('corpor<b>ī</b>', 'corpor<b>ibus</b>', 'nōmin<b>ī</b>', 'nōmin<b>ibus</b>'), ('corpus', 'corpor<b>a</b>', 'nōmen', 'nōmin<b>a</b>'),
    ('corpus', 'corpor<b>a</b>', 'nōmen', 'nōmin<b>a</b>'), ('corpor<b>e</b>', 'corpor<b>ibus</b>', 'nōmin<b>e</b>', 'nōmin<b>ibus</b>')],
    colunas=('corpus · sing.', 'corpus · pl.', 'nōmen · sing.', 'nōmen · pl.'))}
<p>Compare as duas tabelas: genitivo, dativo e ablativo são idênticos nos dois gêneros. A diferença está toda no nominativo, no acusativo e no vocativo, e segue a <b>regra dos neutros</b>, que você já conhece da segunda declinação (<i>bellum, bella</i>): em todo neutro, de qualquer declinação, <b>nominativo, acusativo e vocativo são iguais</b>, e no plural esses três casos terminam em <b><i>-a</i></b>. Por isso o acusativo singular de <i>corpus</i> é <i>corpus</i>, e não *<i>corporem</i>. Uma explicação tradicional é que o neutro designava sobretudo coisas, que raramente agem, e por isso a língua não precisou distinguir nelas, pela forma, o sujeito do objeto; seja qual for a origem, a regra não tem exceções.</p>
{tabela(['Caso', 'Masc. e fem. · sing.', 'Neutro · sing.', 'Masc. e fem. · pl.', 'Neutro · pl.'], [
    ['Nominativo', 'vários (<i>rēx, mīles, pater, homō</i>)', 'vários (<i>corpus, nōmen</i>)', '<b>-ēs</b>', '<b>-a</b>'],
    ['Genitivo', '<b>-is</b>', '<b>-is</b>', '<b>-um</b>', '<b>-um</b>'],
    ['Dativo', '<b>-ī</b>', '<b>-ī</b>', '<b>-ibus</b>', '<b>-ibus</b>'],
    ['Acusativo', '<b>-em</b>', 'igual ao nominativo', '<b>-ēs</b>', '<b>-a</b>'],
    ['Vocativo', 'igual ao nominativo', 'igual ao nominativo', '<b>-ēs</b>', '<b>-a</b>'],
    ['Ablativo', '<b>-e</b>', '<b>-e</b>', '<b>-ibus</b>', '<b>-ibus</b>'],
], 'Terminações dos temas consonantais')}
<p>Três coincidências merecem atenção. No plural masculino e feminino, <i>-ēs</i> serve ao nominativo, ao acusativo e ao vocativo (<i>rēgēs</i> pode ser sujeito ou objeto). <i>-ibus</i> serve ao dativo e ao ablativo, como <i>-īs</i> nas duas primeiras declinações. E, nos neutros, <i>corpus</i> ou <i>corpora</i> podem ser sujeito ou objeto. Como sempre, quem decide é a frase: o número do verbo, as preposições, as funções já ocupadas e, como você verá na seção 5, o adjetivo.</p>
{comparacao('Terminações da 3ª que parecem de outra declinação', ['Forma', 'Na 3ª declinação', 'Pode lembrar', 'Como não confundir'], [
    ['rēg<b>ī</b>', 'dativo singular', 'genitivo sing. ou nominativo pl. da 2ª (<i>dominī</i>)', 'veja o genitivo do dicionário: <i>rēx, rēgis</i> é da 3ª'],
    ['rēg<b>um</b>', 'genitivo plural', 'acusativo sing. da 2ª (<i>dominum</i>) ou neutro (<i>bellum</i>)', 'idem; "dos reis", não "o rei"'],
    ['rēg<b>is</b>', 'genitivo singular (<i>i</i> breve)', 'dativo/ablativo pl. da 1ª e 2ª (<i>rosīs, dominīs</i>, <i>ī</i> longo)', 'nos textos com macron, a vogal; sem macron, o tema'],
    ['corpor<b>a</b>, nōmin<b>a</b>', 'nom./ac./voc. plural neutro', 'nominativo sing. da 1ª (<i>rosa</i>)', 'o tema <i>corpor-</i> não é da 1ª; o adjetivo vem em <i>-a</i> neutro plural'],
    ['corp<b>us</b>', 'nom./ac./voc. sing. neutro', 'nominativo sing. da 2ª (<i>dominus</i>)', 'genitivo <i>corporis</i>; o adjetivo vem em <i>-um</i> (<i>corpus magnum</i>)'],
])}
{observacao('Há outra família na terceira declinação', 'Alguns nomes da terceira declinação têm o genitivo plural em <i>-ium</i> (e não em <i>-um</i>) e, os neutros, o plural em <i>-ia</i>: são os <b>temas em <i>-i</i></b>, como <i>cīvis</i> (cidadão) ou <i>mare</i> (mar). Eles são o assunto do capítulo 10. Neste capítulo, todos os nomes usados são temas consonantais e fazem o genitivo plural em <i>-um</i>.')}
'''),
        ('Os tipos de nominativo', f'''
<p>O nominativo parece imprevisível, mas, olhado a partir do tema, segue poucas regras. Elas não servem para adivinhar o genitivo (isso o dicionário faz), e sim para <b>reconhecer</b> a palavra quando você a encontra num caso oblíquo e precisa voltar ao nominativo para procurá-la no dicionário. Há três tipos principais.</p>
<h3>1. Temas em consoante muda: o nominativo acrescenta -s</h3>
<p>As consoantes mudas são as oclusivas: <i>c, g</i> (guturais), <i>t, d</i> (dentais), <i>p, b</i> (labiais). Nos masculinos e femininos desses temas, o nominativo se forma com <b><i>-s</i></b>, e o encontro da consoante com o <i>-s</i> produz mudanças regulares: gutural + <i>s</i> se escreve <i>x</i> (<i>rēg-s</i> → <i>rēx</i>; <i>duc-s</i> → <i>dux</i>; <i>vōc-s</i> → <i>vōx</i>); dental cai diante do <i>s</i> (<i>mīlit-s</i> → <i>mīles</i>, com <i>e</i> no lugar do <i>i</i>; <i>ped-s</i> → <i>pēs</i>; <i>virtūt-s</i> → <i>virtūs</i>); labial se conserva (<i>prīncip-s</i> → <i>prīnceps</i>, "chefe, o primeiro"). Por isso, quase todo nominativo em <i>-x</i> esconde um <i>c</i> ou um <i>g</i>, e quem encontra <i>ducem</i> num texto procura <i>dux</i>.</p>
<h3>2. Temas em líquida e em nasal: o nominativo não leva -s</h3>
<p>Líquidas são <i>l</i> e <i>r</i>; nasal, aqui, é o <i>n</i>. Esses temas fazem o nominativo <b>sem terminação</b>, às vezes com uma pequena alteração. Os temas em <i>-r</i> mostram o próprio tema: <i>labor, labōris</i>; <i>amor, amōris</i>; <i>soror, sorōris</i> (a vogal longa do tema se abrevia diante do <i>-r</i> final do nominativo). Os temas em <i>-tr-</i> fazem o nominativo em <i>-ter</i>: <i>pater, patris</i>; <i>māter, mātris</i>; <i>frāter, frātris</i>. Os temas em <i>-n-</i> perdem o <i>n</i> e terminam em <i>-ō</i>: <i>homō, hominis</i>; <i>leō, leōnis</i> (leão); <i>ōrātiō, ōrātiōnis</i> (discurso); <i>virgō, virginis</i> (moça, virgem). Os neutros em <i>-min-</i> fazem o nominativo em <i>-men</i>: <i>nōmen, nōminis</i>; <i>flūmen, flūminis</i>; <i>carmen, carminis</i> (canção, poema).</p>
<h3>3. Temas em -s: o rotacismo</h3>
<p>O terceiro tipo engana mais, porque o nominativo tem um <i>s</i> que desaparece nos outros casos. Em latim antigo, um <i>s</i> entre duas vogais passou a <i>r</i>: é o <b>rotacismo</b>. O tema de "corpo" era <i>corpos-</i>; no nominativo, sem terminação, o <i>s</i> ficou no fim da palavra e se conservou (<i>corpus</i>); no genitivo, *<i>corpos-is</i> pôs o <i>s</i> entre vogais e virou <i>corporis</i>. Do mesmo modo, <i>genus, generis</i> (gênero, origem); <i>tempus, temporis</i> (tempo); <i>opus, operis</i> (obra, trabalho); <i>flōs, flōris</i> (flor); <i>mōs, mōris</i> (costume). Em alguns nomes o <i>r</i> dos outros casos passou também ao nominativo: <i>honor, honōris</i> (honra), que nos textos antigos e na poesia aparece ainda como <i>honōs</i>. O português guarda os dois lados da mudança: <i>corpo</i> e <i>corporal</i>, <i>tempo</i> e <i>temporal</i>, <i>gênero</i> e <i>genérico</i>.</p>
{tabela(['Nominativo, genitivo', 'Gênero', 'Tema', 'Tipo', 'Significado'], [
    ['rēx, rēgis', 'm.', 'rēg-', 'muda (gutural) + <i>s</i> → <i>x</i>', 'rei'], ['dux, ducis', 'm. (ou f.)', 'duc-', 'muda (gutural) + <i>s</i> → <i>x</i>', 'líder, general'],
    ['lēx, lēgis', 'f.', 'lēg-', 'muda (gutural) + <i>s</i> → <i>x</i>', 'lei'], ['vōx, vōcis', 'f.', 'vōc-', 'muda (gutural) + <i>s</i> → <i>x</i>', 'voz'],
    ['pāx, pācis', 'f.', 'pāc-', 'muda (gutural) + <i>s</i> → <i>x</i>', 'paz'], ['mīles, mīlitis', 'm.', 'mīlit-', 'muda (dental) cai diante de <i>s</i>', 'soldado'],
    ['virtūs, virtūtis', 'f.', 'virtūt-', 'muda (dental) cai diante de <i>s</i>', 'coragem, virtude'], ['pēs, pedis', 'm.', 'ped-', 'muda (dental) cai diante de <i>s</i>', 'pé'],
    ['pater, patris', 'm.', 'patr-', 'líquida (<i>-tr-</i> → <i>-ter</i>)', 'pai'], ['māter, mātris', 'f.', 'mātr-', 'líquida (<i>-tr-</i> → <i>-ter</i>)', 'mãe'],
    ['frāter, frātris', 'm.', 'frātr-', 'líquida (<i>-tr-</i> → <i>-ter</i>)', 'irmão'], ['soror, sorōris', 'f.', 'sorōr-', 'líquida (<i>-r</i>)', 'irmã'],
    ['labor, labōris', 'm.', 'labōr-', 'líquida (<i>-r</i>)', 'trabalho, fadiga'], ['amor, amōris', 'm.', 'amōr-', 'líquida (<i>-r</i>)', 'amor'],
    ['homō, hominis', 'm.', 'homin-', 'nasal (o <i>n</i> cai; <i>-ō</i>)', 'ser humano, homem'], ['ōrātiō, ōrātiōnis', 'f.', 'ōrātiōn-', 'nasal (o <i>n</i> cai; <i>-ō</i>)', 'discurso'],
    ['nōmen, nōminis', 'n.', 'nōmin-', 'nasal (<i>-min-</i> → <i>-men</i>)', 'nome'], ['flūmen, flūminis', 'n.', 'flūmin-', 'nasal (<i>-min-</i> → <i>-men</i>)', 'rio'],
    ['carmen, carminis', 'n.', 'carmin-', 'nasal (<i>-min-</i> → <i>-men</i>)', 'canção, poema'], ['corpus, corporis', 'n.', 'corpor-', 'tema em <i>-s</i>, rotacismo', 'corpo'],
    ['tempus, temporis', 'n.', 'tempor-', 'tema em <i>-s</i>, rotacismo', 'tempo'], ['genus, generis', 'n.', 'gener-', 'tema em <i>-s</i>, rotacismo', 'gênero, origem'],
    ['opus, operis', 'n.', 'oper-', 'tema em <i>-s</i>, rotacismo', 'obra, trabalho'], ['flōs, flōris', 'm.', 'flōr-', 'tema em <i>-s</i>, rotacismo', 'flor'],
], 'Vocabulário do capítulo: vinte e quatro nomes de tema consonantal', latim_cols=(0, 2))}
{dica('<b>Do caso oblíquo ao dicionário.</b> Ao encontrar <i>lēgibus</i>, tire a terminação (<i>-ibus</i>) e fique com o tema <i>lēg-</i>; um tema em <i>g</i> faz o nominativo em <i>-x</i>: procure <i>lēx</i>. Ao encontrar <i>temporum</i>, o tema é <i>tempor-</i>; um <i>r</i> entre vogais pode vir de <i>s</i>: procure <i>tempus</i>. Ao encontrar <i>virginem</i>, o tema <i>virgin-</i> pode ter nominativo em <i>-ō</i>: procure <i>virgō</i>.')}
'''),
        ('O gênero: tendências, com cautela', f'''
<p>Na primeira e na segunda declinações, a terminação quase sempre indica o gênero. Na terceira, isso não acontece: há masculinos, femininos e neutros com todo tipo de nominativo, e a regra prática é uma só: <b>aprenda o gênero com a palavra</b>, como parte da entrada (<i>rēx, rēgis, m.</i>). Ainda assim, algumas tendências ajudam a lembrar e a desconfiar, desde que você as trate como tendências, não como leis.</p>
<p>A primeira tendência vale para todas as declinações e vem antes de qualquer outra: nomes de <b>pessoas</b> têm o gênero do sexo da pessoa. Por isso <i>rēx</i>, <i>dux</i>, <i>pater</i>, <i>frāter</i> e <i>homō</i> são masculinos, e <i>māter</i>, <i>soror</i> e <i>virgō</i> são femininos, seja qual for a terminação. Para as coisas e as ideias, as gramáticas registram estas tendências (Bennett §§ 43–46; Allen e Greenough §§ 84–87):</p>
{tabela(['Terminação do nominativo', 'Tendência', 'Exemplos', 'Exceções que você já pode encontrar'], [
    ['<i>-or</i>, <i>-ōs</i>, <i>-er</i>; <i>-ō</i> (fora <i>-iō, -dō, -gō</i>)', 'masculino', '<i>labor, amor, honor, flōs, mōs, leō</i>', '<i>soror</i> e <i>māter</i> (f., por serem mulheres); <i>arbor</i>, árvore (f.); <i>iter</i>, caminho (n.)'],
    ['<i>-x</i>', 'feminino', '<i>lēx, vōx, pāx, lūx</i> (luz)', '<i>rēx</i> e <i>dux</i> (m., por designarem homens)'],
    ['<i>-tās</i>, <i>-tūs</i>, <i>-iō</i>, <i>-dō</i>, <i>-gō</i>', 'feminino', '<i>virtūs, voluntās</i> (vontade), <i>ōrātiō, virgō</i>', '<i>ōrdō</i>, ordem (m.)'],
    ['<i>-men</i>; <i>-us</i> (gen. <i>-oris</i>, <i>-eris</i>); <i>-l</i>', 'neutro', '<i>nōmen, flūmen, carmen, corpus, tempus, genus, opus</i>', '<i>sal, salis</i>, sal, e <i>sōl, sōlis</i>, sol (m.)'],
], 'Tendências de gênero nos temas consonantais', latim_cols=())}
<p>A tabela tem exceções em todas as linhas de propósito: é assim que a terceira declinação funciona. O exemplo de <i>sal</i> é útil porque aparece num texto que você vai ler na seção 6 (<i>Vōs estis sal terrae</i>): terminações em <i>-l</i> costumam ser neutras, mas <i>sal, salis</i> é masculino. Quem confia só na terminação erra; quem consulta o dicionário, não.</p>
{observacao('O português não serve de guia', 'O gênero da palavra portuguesa nem sempre coincide com o latino. <i>Flōs</i> e <i>amor</i> são masculinos como "o amor", mas "a flor" é feminina em português; <i>dolor</i> (dor) é masculino em latim e "a dor" é feminina; <i>corpus</i> e <i>tempus</i> são neutros, gênero que o português perdeu, e viraram masculinos ("o corpo", "o tempo"). Por isso se diz <i>flōs pulcher</i>, e não *<i>flōs pulchra</i>, e <i>corpus magnum</i>, e não *<i>corpus magnus</i>.')}
'''),
        ('A concordância com os adjetivos de primeira classe', f'''
<p>Esta é a seção mais importante do capítulo. Você aprendeu no capítulo 5 que o adjetivo concorda com o nome em <b>gênero, número e caso</b>. Até agora, nomes e adjetivos eram quase sempre "rimas" (<i>puella bona</i>, <i>dominus bonus</i>, <i>bellum magnum</i>), e era fácil confundir concordância com repetição da terminação. A terceira declinação desfaz essa ilusão: o adjetivo <i>bonus, -a, -um</i> continua se declinando pela primeira e segunda declinações, enquanto o nome segue a terceira. O adjetivo copia o <b>gênero, o número e o caso</b> do nome, não a terminação.</p>
{tabela_declinacao('Nome da 3ª declinação com adjetivo de primeira classe: rēx bonus (m.), "o bom rei" · corpus magnum (n.), "o corpo grande"', [
    ('rēx bon<b>us</b>', 'rēgēs bon<b>ī</b>', 'corpus magn<b>um</b>', 'corpora magn<b>a</b>'),
    ('rēgis bon<b>ī</b>', 'rēgum bon<b>ōrum</b>', 'corporis magn<b>ī</b>', 'corporum magn<b>ōrum</b>'),
    ('rēgī bon<b>ō</b>', 'rēgibus bon<b>īs</b>', 'corporī magn<b>ō</b>', 'corporibus magn<b>īs</b>'),
    ('rēgem bon<b>um</b>', 'rēgēs bon<b>ōs</b>', 'corpus magn<b>um</b>', 'corpora magn<b>a</b>'),
    ('rēx bon<b>e</b>', 'rēgēs bon<b>ī</b>', 'corpus magn<b>um</b>', 'corpora magn<b>a</b>'),
    ('rēge bon<b>ō</b>', 'rēgibus bon<b>īs</b>', 'corpore magn<b>ō</b>', 'corporibus magn<b>īs</b>')],
    colunas=('rēx bonus · sing.', 'rēx bonus · pl.', 'corpus magnum · sing.', 'corpus magnum · pl.'))}
<p>Observe as formas lado a lado: <i>rēgem bonum</i> (<i>-em</i> e <i>-um</i>), <i>rēgis bonī</i> (<i>-is</i> e <i>-ī</i>), <i>rēgī bonō</i>, <i>rēgēs bonōs</i>. Nenhuma terminação se repete, e todas estão certas. Repare também no vocativo: o nome fica igual ao nominativo (<i>rēx</i>), mas o adjetivo masculino em <i>-us</i> faz <i>-e</i>, como na segunda declinação: <i>rēx bone!</i>, "ó bom rei!". Nos neutros, o adjetivo segue a mesma regra do nome: <i>corpus magnum</i> serve ao nominativo e ao acusativo, e <i>corpora magna</i> termina em <i>-a</i> no plural.</p>
<p>Para o feminino, o adjetivo toma as formas da primeira declinação: <i>lēx bona</i>, <i>lēgis bonae</i>, <i>lēgem bonam</i>, <i>lēge bonā</i>; no plural, <i>lēgēs bonae</i> (nominativo) e <i>lēgēs bonās</i> (acusativo). E aqui está a grande vantagem para o leitor: o adjetivo <b>desfaz as ambiguidades</b> do nome. <i>Lēgēs</i>, sozinho, pode ser nominativo ou acusativo; <i>lēgēs bonae</i> só pode ser nominativo (ou vocativo), e <i>lēgēs bonās</i> só pode ser acusativo.</p>
{exemplos([('Rēx bon<b>us</b> lēgēs nov<b>ās</b> dat.', 'O bom rei dá novas leis. (<i>bonus</i>: nom. sing. m.; <i>novās</i>: ac. pl. f., logo <i>lēgēs</i> é objeto)'),
           ('Lēgēs nov<b>ae</b> rēgī placent.', 'As novas leis agradam ao rei. (<i>novae</i>: nom. pl. f., logo <i>lēgēs</i> é sujeito; <i>placent</i> = agradam)'),
           ('Māter carmina long<b>a</b> cantat.', 'A mãe canta longas canções. (<i>carmina</i> e <i>longa</i>: ac. pl. neutro, e não nominativos da 1ª)'),
           ('Fīlia mīlitis Rōmān<b>ī</b> flōrēs pulchr<b>ōs</b> amat.', 'A filha do soldado romano ama as belas flores. (<i>Rōmānī</i> concorda com <i>mīlitis</i>, gen. sing. m.; <i>pulchrōs</i> com <i>flōrēs</i>, ac. pl. m.)')])}
<p>Leia agora uma frase em que o adjetivo resolve uma dúvida que o nome deixa em aberto:</p>
{diagrama_frase([('Mīlitēs', 'nom. ou ac. pl. · em suspenso'), ('rēgis bonī', 'genitivo sing. m. · "do bom rei"'), ('lēgēs novās', 'acusativo pl. f. · objeto'), ('laudant', 'verbo · "elogiam"')],
    'Lendo em ordem: <i>Mīlitēs rēgis bonī lēgēs novās laudant</i> = Os soldados elogiam as novas leis do bom rei.')}
<p><i>Mīlitēs</i> pode ser nominativo ou acusativo plural: fica em suspenso. <i>Rēgis bonī</i>: genitivo singular, "do bom rei"; o adjetivo em <i>-ī</i> confirma que <i>rēgis</i> é genitivo, não outra coisa. <i>Lēgēs novās</i>: o nome sozinho seria ambíguo, mas <i>novās</i> só pode ser acusativo: é o objeto. Se o objeto já está ocupado, <i>mīlitēs</i> é o sujeito, e <i>laudant</i>, plural, confirma. O adjetivo de primeira classe, cujas formas você já domina, funciona como uma etiqueta de caso pendurada no nome da terceira declinação.</p>
'''),
        ('Análise gramatical: uma frase autêntica', f'''
<p>O canto dos anjos no Evangelho de Lucas, na Vulgata, reúne num só verso três nomes da terceira declinação e adjetivos de primeira classe: <i>bonae</i>, concordando com um desses nomes, e o superlativo <i>altissimīs</i> (capítulo 18), que se declina como <i>bonus</i>:</p>
{exemplos([('Glōria in altissimīs Deō, et in terrā pāx hominibus bonae voluntātis.', 'Glória a Deus nas alturas, e na terra paz aos homens de boa vontade. (Lc 2,14, Vulgata Clementina)')])}
<p>Duas observações antes da análise. Não há verbo: em aclamações como esta, o latim subentende o verbo "ser, estar" ("glória <i>seja</i> a Deus"), e os dois membros se organizam em paralelo, com nominativo, dativo e uma expressão de lugar em cada um. E <i>altissimīs</i> é o superlativo de <i>altus</i> ("altíssimo"), usado como substantivo, "nos lugares mais altos"; os superlativos são assunto do capítulo 18. Basta, por ora, reconhecer o ablativo plural em <i>-īs</i> depois de <i>in</i>.</p>
{analise('Lc 2,14, palavra a palavra', [
    ('Glōria', 'glōria, -ae (f.), glória', 'nominativo singular, 1ª declinação', 'sujeito do primeiro membro (verbo subentendido)'),
    ('in', 'in (preposição)', 'aqui com ablativo', 'lugar onde'),
    ('altissimīs', 'altissimus, -a, -um, superlativo de altus', 'ablativo plural', '<i>in altissimīs</i>: "nas alturas"'),
    ('Deō', 'deus, -ī (m.), Deus', 'dativo singular, 2ª declinação', 'a quem se dá a glória: "a Deus"'),
    ('et', 'et (conjunção)', 'invariável', 'liga os dois membros'),
    ('in terrā', 'terra, -ae (f.), terra', '<i>in</i> + ablativo singular, 1ª declinação', 'lugar onde: "na terra"'),
    ('pāx', 'pāx, pācis (f.), paz', 'nominativo singular, 3ª declinação; tema <i>pāc-</i> + <i>s</i> → <i>x</i>', 'sujeito do segundo membro'),
    ('hominibus', 'homō, hominis (m.), ser humano, homem', 'dativo plural, 3ª declinação; tema <i>homin-</i> + <i>-ibus</i>', 'a quem se dá a paz: "aos homens" (paralelo a <i>Deō</i>)'),
    ('bonae', 'bonus, -a, -um, bom', 'genitivo singular feminino', 'concorda com <i>voluntātis</i>'),
    ('voluntātis', 'voluntās, voluntātis (f.), vontade', 'genitivo singular, 3ª declinação; tema <i>voluntāt-</i>', 'qualifica <i>hominibus</i>: "de boa vontade"'),
])}
<p>Três coisas deste capítulo aparecem aqui. Primeiro, o tema: <i>hominibus</i> e <i>voluntātis</i> só são reconhecíveis por quem sabe que <i>homō</i> tem o tema <i>homin-</i> e que <i>voluntās</i> tem o tema <i>voluntāt-</i> (uma dental que cai no nominativo, como em <i>virtūs</i>). Segundo, a ambiguidade: <i>-ibus</i> pode ser dativo ou ablativo, mas não há preposição diante de <i>hominibus</i>, e o paralelo com <i>Deō</i> (dativo inequívoco) decide: é dativo. Terceiro, a concordância: <i>bonae voluntātis</i> junta uma terminação da primeira declinação a uma da terceira, e as duas palavras estão no mesmo gênero (feminino), no mesmo número (singular) e no mesmo caso (genitivo). É exatamente a regra da seção 5, numa frase que se lê há dezesseis séculos.</p>
<p>O Evangelho de Mateus traz duas frases curtíssimas, uma seguida da outra, que você já consegue ler sozinho; <i>vōs estis</i> é "vós sois":</p>
{exemplos([('Vōs estis sal terrae.', 'Vós sois o sal da terra. (Mt 5,13; <i>sal, salis</i>, m., nominativo predicativo)'),
           ('Vōs estis lūx mundī.', 'Vós sois a luz do mundo. (Mt 5,14; <i>lūx, lūcis</i>, f., nominativo predicativo; <i>mundī</i>, genitivo da 2ª)')])}
<h3>Resumo</h3>
<ul>
<li>A terceira declinação tem genitivo singular em <i>-is</i>. O nominativo é imprevisível; o <b>tema</b> se obtém tirando <i>-is</i> do genitivo: <i>rēx, rēgis</i> → <i>rēg-</i>.</li>
<li>Masculino e feminino: —, <i>-is, -ī, -em</i>, —, <i>-e</i> / <i>-ēs, -um, -ibus, -ēs, -ēs, -ibus</i>.</li>
<li>Neutro: nominativo = acusativo = vocativo, e no plural <i>-a</i>: <i>corpus, corporis, corporī, corpus, corpus, corpore</i> / <i>corpora, corporum, corporibus, corpora, corpora, corporibus</i>.</li>
<li>Nominativos: muda + <i>s</i> (<i>rēx, mīles</i>); líquida e nasal sem <i>s</i> (<i>pater, labor, homō, nōmen</i>); tema em <i>-s</i> com rotacismo (<i>corpus, corporis</i>; <i>flōs, flōris</i>).</li>
<li>Gênero: o sexo, para pessoas; para o resto, tendências com exceções; na dúvida, o dicionário.</li>
<li>Concordância: o adjetivo de primeira classe copia gênero, número e caso, não a terminação: <i>rēx bonus, lēx bona, corpus magnum</i>.</li>
</ul>
<p>No próximo capítulo, os temas em <i>-i</i> (genitivo plural em <i>-ium</i>) completam a terceira declinação e trazem os adjetivos de segunda classe, como <i>fortis, forte</i>, que se declinam por ela.</p>
'''),
    ],
    erros_comuns=[
        ('Usar o nominativo como tema: *<i>rēxis</i>, *<i>corpī</i>, *<i>homōnem</i>.', 'Na terceira declinação, o nominativo muitas vezes esconde o tema. Tire <i>-is</i> do genitivo do dicionário e junte as terminações ao que sobrar: <i>rēg-is</i> → <i>rēgem</i>; <i>corpor-is</i> → <i>corpore</i>; <i>homin-is</i> → <i>hominem</i>. Por isso nunca se aprende só o nominativo.'),
        ('Tratar todo nome em <i>-us</i> como da segunda declinação: *<i>corpī</i>, *<i>corpus bonus</i>.', '<i>Corpus, tempus, genus, opus</i> são neutros da terceira (genitivo em <i>-oris</i> ou <i>-eris</i>). O genitivo do dicionário decide a declinação, e o gênero neutro pede o adjetivo em <i>-um</i>: <i>corpus magnum</i>, <i>tempus longum</i>.'),
        ('Fazer o adjetivo "rimar" com o nome: *<i>rēgem bonem</i>, *<i>lēgis bonis</i>, *<i>mīlitēs bonēs</i>.', 'A concordância é de gênero, número e caso, não de terminação. O adjetivo <i>bonus, -a, -um</i> continua declinando-se pela 1ª e 2ª declinações: <i>rēgem bonum</i>, <i>lēgis bonae</i>, <i>mīlitēs bonī</i>. Para achar a forma, pergunte: qual o gênero do nome (dicionário)? qual o caso e o número desta forma? Depois tome essa forma em <i>bonus</i>.'),
        ('Ler <i>corpora</i>, <i>nōmina</i>, <i>carmina</i> como femininos singulares da primeira declinação.', 'Terminam em <i>-a</i> porque são neutros plurais (nominativo, acusativo ou vocativo). O verbo no plural (se forem sujeito) e o adjetivo neutro plural (<i>carmina longa</i>, <i>nōmina clāra</i>) confirmam. A tradução é plural: "os corpos", "os nomes", "as canções".'),
        ('Confundir <i>rēgum</i> com um acusativo singular e <i>rēgī</i> com um nominativo plural.', 'Na terceira declinação, <i>-um</i> é genitivo plural ("dos reis") e <i>-ī</i> é dativo singular ("ao rei"). As mesmas letras têm outro valor na segunda (<i>dominum</i>, <i>dominī</i>). Identifique primeiro a declinação pelo tema e só depois leia a terminação.'),
        ('Deduzir o gênero latino do português ou só da terminação: *<i>flōs pulchra</i>, *<i>soror bonus</i>.', '"A flor" é feminino em português, mas <i>flōs, flōris</i> é masculino: <i>flōs pulcher</i>. <i>Soror</i> termina em <i>-or</i>, tendência masculina, mas designa uma mulher e é feminino: <i>soror bona</i>. O gênero vem do dicionário, e o sexo da pessoa prevalece sobre a terminação.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Uma frase com neutro plural',
            'Leia em voz alta e analise, na ordem latina: <i lang="la">Frāter mātris carmina longa puerīs cantat.</i> Vocabulário: <i>frāter, frātris</i> (m.), irmão; <i>māter, mātris</i> (f.), mãe; <i>carmen, carminis</i> (n.), canção; <i>longus, -a, -um</i>, longo; <i>puer, puerī</i> (m.), menino; <i>cantat</i>, canta.', [
            ('Qual é o verbo, e o que ele faz esperar?', '<i>Cantat</i>, "canta", 3ª pessoa do singular. Espera-se um sujeito singular, aquilo que é cantado (acusativo) e, talvez, para quem se canta (dativo).'),
            ('Que forma é <i>frāter</i>?', 'Nominativo (ou vocativo) singular: é a forma de dicionário, e o genitivo seria <i>frātris</i>. Abre a frase e o verbo é singular: é o sujeito, "o irmão".'),
            ('E <i>mātris</i>?', 'O tema de <i>māter</i> é <i>mātr-</i>; <i>mātr-is</i> é genitivo singular. Liga-se ao nome vizinho: "o irmão <b>da mãe</b>". Não confunda com o dativo/ablativo plural <i>-īs</i> da 1ª e 2ª declinações: aqui o <i>i</i> é breve e o tema é da terceira.'),
            ('<i>Carmina longa</i> é um feminino singular?', 'Não. <i>Carmen, carminis</i> é neutro da terceira; <i>carmina</i> é nominativo, acusativo ou vocativo plural. <i>Longa</i> concorda com ele: neutro plural. O sujeito já é <i>frāter</i>, então <i>carmina longa</i> é o objeto: "longas canções".'),
            ('Que caso é <i>puerīs</i>?', 'Dativo ou ablativo plural da 2ª declinação. Não há preposição, e o verbo admite um destinatário (cantar <i>para</i> alguém): dativo, "aos meninos".'),
            ('Monte a tradução.', '"O irmão da mãe canta longas canções para os meninos." (Ou, mais natural: "O tio materno canta longas canções para os meninos.")'),
        ]),
        pratica_guiada('Prática guiada 2 · Achar os pares nome e adjetivo',
            'Ligue cada adjetivo ao seu nome e traduza: <i lang="la">Mīles fīliam rēgis clārī in flūmine magnō videt.</i> Vocabulário: <i>mīles, mīlitis</i> (m.), soldado; <i>fīlia, -ae</i>, filha; <i>rēx, rēgis</i> (m.), rei; <i>clārus, -a, -um</i>, famoso; <i>flūmen, flūminis</i> (n.), rio; <i>magnus, -a, -um</i>, grande; <i>videt</i>, vê.', [
            ('Com que nome concorda <i>clārī</i>?', '<i>Clārī</i> pode ser genitivo singular masculino ou neutro, ou nominativo plural masculino. O único nome vizinho com que ele pode concordar é <i>rēgis</i>, genitivo singular masculino: "do rei famoso". As terminações diferem (<i>-is</i>, <i>-ī</i>), mas gênero, número e caso coincidem.'),
            ('E <i>magnō</i>?', '<i>Magnō</i> é dativo ou ablativo singular masculino ou neutro. Concorda com <i>flūmine</i>, ablativo singular de <i>flūmen</i> (neutro), regido por <i>in</i>: "no grande rio". Note <i>-e</i> no nome e <i>-ō</i> no adjetivo.'),
            ('Quem é o sujeito, e qual o objeto?', '<i>Mīles</i>, nominativo singular, é o sujeito de <i>videt</i>. <i>Fīliam</i>, acusativo da 1ª, é o objeto.'),
            ('Monte a tradução.', '"O soldado vê a filha do rei famoso no grande rio." (Isto é, dentro do rio ou sobre ele: <i>in</i> + ablativo é lugar onde.)'),
        ], 'Conclusão: para achar o par, não procure terminações iguais; procure o nome com o mesmo gênero, número e caso que o adjetivo pode ter.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Caso e número', 'Dê o caso e o número de cada forma (todas as possibilidades) e o nominativo de dicionário. Use a tabela de vocabulário da seção 3.', [
            ('<i>rēgum</i>', 'Genitivo plural de <i>rēx, rēgis</i>: "dos reis". Não é acusativo singular: esse seria <i>rēgem</i>.'),
            ('<i>corpora</i>', 'Nominativo, acusativo ou vocativo plural de <i>corpus, corporis</i> (n.): os três casos são iguais nos neutros.'),
            ('<i>mīlitī</i>', 'Dativo singular de <i>mīles, mīlitis</i>: "ao soldado".'),
            ('<i>lēgem</i>', 'Acusativo singular de <i>lēx, lēgis</i> (f.).'),
            ('<i>nōmine</i>', 'Ablativo singular de <i>nōmen, nōminis</i> (n.).'),
            ('<i>patrēs</i>', 'Nominativo, acusativo ou vocativo plural de <i>pater, patris</i>. A frase decide qual.'),
            ('<i>temporibus</i>', 'Dativo ou ablativo plural de <i>tempus, temporis</i> (n.).'),
            ('<i>vōcis</i>', 'Genitivo singular de <i>vōx, vōcis</i> (f.): "da voz".'),
            ('<i>flūmen</i>', 'Nominativo, acusativo ou vocativo singular de <i>flūmen, flūminis</i> (n.). Num neutro, a forma de dicionário também serve de acusativo.'),
            ('<i>hominēs</i>', 'Nominativo, acusativo ou vocativo plural de <i>homō, hominis</i> (m.).'),
        ]),
        exercicio('Exercício 2 · Do dicionário ao tema', 'Para cada entrada, dê o tema, diga a que tipo de nominativo pertence e escreva o genitivo plural.', [
            ('<i>dux, ducis</i> (m.), líder', 'Tema <i>duc-</i>; muda gutural + <i>s</i> → <i>x</i>. Genitivo plural <i>ducum</i>.'),
            ('<i>virtūs, virtūtis</i> (f.), coragem', 'Tema <i>virtūt-</i>; muda dental que cai diante do <i>-s</i> do nominativo. Genitivo plural <i>virtūtum</i>.'),
            ('<i>frāter, frātris</i> (m.), irmão', 'Tema <i>frātr-</i>; líquida, com nominativo em <i>-ter</i>. Genitivo plural <i>frātrum</i>.'),
            ('<i>ōrātiō, ōrātiōnis</i> (f.), discurso', 'Tema <i>ōrātiōn-</i>; nasal, o <i>n</i> cai no nominativo. Genitivo plural <i>ōrātiōnum</i>.'),
            ('<i>carmen, carminis</i> (n.), canção', 'Tema <i>carmin-</i>; nasal neutro, <i>-min-</i> → <i>-men</i> no nominativo. Genitivo plural <i>carminum</i>.'),
            ('<i>opus, operis</i> (n.), obra', 'Tema <i>oper-</i>, antigo <i>opes-</i>: tema em <i>-s</i>, com rotacismo nos casos oblíquos. Genitivo plural <i>operum</i>.'),
        ]),
        exercicio('Exercício 3 · Decline com o adjetivo', 'Decline no singular e no plural, em voz alta e por escrito, nome e adjetivo juntos.', [
            ('<i>lēx bona</i> (<i>lēx, lēgis</i>, f.), "a boa lei"', 'Singular: lēx bona, lēgis bonae, lēgī bonae, lēgem bonam, lēx bona, lēge bonā. Plural: lēgēs bonae, lēgum bonārum, lēgibus bonīs, lēgēs bonās, lēgēs bonae, lēgibus bonīs. O nome é feminino, por isso o adjetivo segue a 1ª declinação; as terminações do nome são as da 3ª.'),
            ('<i>tempus longum</i> (<i>tempus, temporis</i>, n.), "o tempo longo"', 'Singular: tempus longum, temporis longī, temporī longō, tempus longum, tempus longum, tempore longō. Plural: tempora longa, temporum longōrum, temporibus longīs, tempora longa, tempora longa, temporibus longīs. Nominativo, acusativo e vocativo iguais, nos dois números, no nome e no adjetivo.'),
        ]),
        exercicio('Exercício 4 · Faça concordar', 'Escreva o adjetivo entre parênteses na forma que concorda com o nome, e explique.', [
            ('<i>rēgem ___</i> (bonus)', '<i>bonum</i>: <i>rēgem</i> é acusativo singular masculino.'),
            ('<i>lēgēs ___</i> (novus), como objeto da frase', '<i>novās</i>: acusativo plural feminino (<i>lēx</i> é f.). Como sujeito, seria <i>novae</i>.'),
            ('<i>corpore ___</i> (magnus)', '<i>magnō</i>: ablativo singular neutro.'),
            ('<i>nōmina ___</i> (clārus)', '<i>clāra</i>: nominativo ou acusativo plural neutro.'),
            ('<i>mātris ___</i> (bonus)', '<i>bonae</i>: genitivo singular feminino. Não *<i>bonis</i>: o adjetivo não copia a terminação <i>-is</i>.'),
            ('<i>mīlitum ___</i> (Rōmānus)', '<i>Rōmānōrum</i>: genitivo plural masculino, "dos soldados romanos".'),
            ('<i>flōrēs ___</i> (pulcher), como objeto da frase', '<i>pulchrōs</i>: acusativo plural <b>masculino</b>, porque <i>flōs</i> é masculino em latim, apesar de "a flor" em português.'),
            ('<i>soror ___</i> (bonus)', '<i>bona</i>: nominativo singular feminino. A terminação <i>-or</i> tende ao masculino, mas <i>soror</i> designa uma mulher.'),
        ]),
        exercicio('Exercício 5 · Traduza lendo em ordem', 'Anote caso e número de cada palavra antes de traduzir. Vocabulário além da seção 3: <i>populus, -ī</i> (m.), povo; <i>laudant</i>, elogiam; <i>audit</i>, ouve; <i>clārus</i>, famoso; <i>pulcher, -chra, -chrum</i>, belo; <i>dant</i>, dão; <i>amant</i>, amam.', [
            ('<i>Rēx lēgēs novās populō dat.</i>', '<i>Rēx</i> (nom. sing., sujeito), <i>lēgēs novās</i> (ac. pl. f.: o adjetivo exclui o nominativo), <i>populō</i> (dat. sing., 2ª), <i>dat</i>: O rei dá novas leis ao povo.'),
            ('<i>Mīlitēs ducem bonum laudant.</i>', '<i>Mīlitēs</i> (nom. pl., sujeito; o verbo é plural e <i>ducem</i> já é o objeto), <i>ducem bonum</i> (ac. sing. m.): Os soldados elogiam o bom general.'),
            ('<i>Pater puerī carmina longa audit.</i>', '<i>Pater</i> (nom. sing.), <i>puerī</i> (gen. sing., 2ª, "do menino"; não pode ser sujeito plural, porque <i>audit</i> é singular), <i>carmina longa</i> (ac. pl. neutro): O pai do menino ouve longas canções.'),
            ('<i>Nōmen rēgis clārum est.</i>', '<i>Nōmen</i> (nom. sing. n., sujeito), <i>rēgis</i> (gen. sing.), <i>clārum</i> (nom. sing. n., predicativo; concorda com <i>nōmen</i>, não com <i>rēgis</i>, que pediria <i>clārī</i>): O nome do rei é famoso.'),
            ('<i>Puellae flōrēs pulchrōs mātrī dant.</i>', '<i>Puellae</i> (nom. pl., verbo em <i>-nt</i>), <i>flōrēs pulchrōs</i> (ac. pl. m.), <i>mātrī</i> (dat. sing. de <i>māter</i>): As meninas dão belas flores à mãe.'),
            ('<i>Hominēs pācem amant.</i>', '<i>Hominēs</i> (nom. pl.; <i>pācem</i> é o acusativo, então <i>hominēs</i> é o sujeito), <i>pācem</i> (ac. sing. de <i>pāx</i>): Os homens amam a paz.'),
        ]),
        exercicio('Exercício 6 · Do português para o latim', 'Traduza, usando o vocabulário do capítulo e verbos na 3ª pessoa do presente. Vocabulário: <i>amat</i>, ama; <i>nārrat</i>, conta; <i>vident</i>, veem; <i>est · sunt</i>, é · são; <i>fābula, -ae</i>, história; <i>fīlius, -ī</i>, filho; <i>fēmina, -ae</i>, mulher.', [
            ('O bom rei ama a paz.', '<i>Rēx bonus pācem amat.</i> <i>Bonus</i> concorda com <i>rēx</i> (nom. sing. m.); <i>pācem</i> é acusativo de <i>pāx, pācis</i>.'),
            ('A mãe conta histórias aos filhos do soldado.', '<i>Māter fīliīs mīlitis fābulās nārrat.</i> <i>Fīliīs</i>: dativo plural; <i>mīlitis</i>: genitivo singular, formado do tema <i>mīlit-</i>.'),
            ('As leis do rei são longas.', '<i>Lēgēs rēgis longae sunt.</i> O predicativo concorda com o sujeito <i>lēgēs</i>: nominativo plural feminino, <i>longae</i>.'),
            ('Os soldados veem o grande rio.', '<i>Mīlitēs flūmen magnum vident.</i> <i>Flūmen</i> é neutro: o acusativo é igual ao nominativo, e o adjetivo vai para <i>magnum</i>.'),
            ('O nome da mulher é famoso.', '<i>Nōmen fēminae clārum est.</i> <i>Clārum</i> concorda com <i>nōmen</i> (nom. sing. neutro), não com <i>fēminae</i>.'),
        ]),
    ],
    leituras=['d-ooge-latin-for-beginners', 'sonnenschein-pro-patria-a-latin-story-for-beginners', 'lhomond-epitome-historiae-sacrae', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'ravizza-gramatica-latina', 'bennett-new-latin-grammar'],
    leituras_nota='Latin for Beginners, de D\'Ooge, traz exercícios graduados sobre os temas consonantais e é bom para praticar o que este capítulo explicou. Pro Patria continua Ora Maritima com muito mais nomes da terceira declinação, e o Epitome Historiae Sacrae, de Lhomond, conta histórias bíblicas em frases curtas, com muitos nomes da terceira declinação. Na Vulgata, leia Mt 5,13–16 e Lc 2,8–14 procurando os nomes da terceira declinação. Ravizza (n. 27–28) e Bennett (§§ 29–36) servem para consultar os paradigmas.',
)
