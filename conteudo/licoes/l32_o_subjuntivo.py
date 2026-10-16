from conteudo.util import (tabela, tabela_conjugacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='32-o-subjuntivo', titulo='O subjuntivo: formas e usos independentes',
    titulo_latim='Dē coniūnctīvō', tempo='75 min',
    resumo='O quarto modo do verbo latino: o que o subjuntivo exprime, como se formam os seus quatro tempos na ativa e na passiva (a troca de vogal do presente, o infinitivo + terminação do imperfeito, -erim e -issem no perfectum), o subjuntivo de sum, possum e dos irregulares, e os usos em oração principal: exortativo, jussivo, proibição com nē, optativo com utinam, deliberativo e potencial.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['subjuntivo', 'modo verbal', 'presente do subjuntivo', 'imperfeito do subjuntivo', 'perfeito do subjuntivo', 'mais-que-perfeito do subjuntivo',
             'subjuntivo passivo', 'subjuntivo de sum e possum', 'subjuntivo de volō, nōlō, mālō, eō, ferō, fīō', 'subjuntivo exortativo', 'subjuntivo jussivo',
             'proibição com nē + perfeito do subjuntivo', 'subjuntivo optativo (utinam)', 'subjuntivo deliberativo', 'subjuntivo potencial',
             'negação nē × nōn', 'subjuntivo latino × subjuntivo português', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 13: o perfeito, o tema do perfeito e as partes principais (o perfectum do subjuntivo se forma sobre eles). Você também precisa dos tempos do indicativo dos capítulos 6 e 12, porque o subjuntivo se aprende por contraste com eles. A passiva (capítulos 23 e 24) e os verbos irregulares (capítulo 26) são usados nas seções 3 e 4; se ainda não os estudou, leia essas partes depois.',
                       licoes=['06-o-presente-do-indicativo', '12-o-imperfeito-e-o-futuro', '13-o-perfeito-e-as-partes-principais', '23-a-voz-passiva-infectum', '24-a-passiva-do-perfectum', '26-verbos-irregulares']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 100 (subjuntivo de sum), §§ 101–102, 103, 105, 107 (subjuntivo ativo e passivo de amō, moneō, regō, audiō), § 126 (possum), § 129 (ferō), § 130 (volō, nōlō, mālō), § 131 (fīō), § 132 (eō), § 266 (tempos do subjuntivo em orações independentes), §§ 272–280 (usos independentes: exortativo § 274, jussivo § 275, proibitivo § 276, deliberativo § 277, concessivo § 278, optativo § 279, potencial § 280)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 168.e–f (formação do presente e do imperfeito do subjuntivo; sim, velim como antigos optativos), § 169.d–e (perfeito em -erim e mais-que-perfeito em -issem), § 170 (sum), §§ 197–199 (possum; volō, nōlō, mālō), §§ 200, 202–203 (ferō; eō), § 438 (o subjuntivo em geral), §§ 439–440 (exortativo e concessivo), §§ 441–442 (optativo; utinam), §§ 443–444 (deliberativo), §§ 445–447 (potencial), § 450 (proibições: nōlī + infinitivo, cavē + subjuntivo, nē + perfeito do subjuntivo)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 347 (proibição: nōlī com infinitivo ou nē com perfeito do conjuntivo), §§ 351–354 (o conjuntivo: usos independente e dependente), § 356 (potencial), § 357 (concessivo), § 358 (deliberativo), § 359 (optativo, utinam), § 360 (exortativo), §§ 361–362 (jussivo)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 85 (presente do subjuntivo formado do presente: -em na 1ª, -am nas demais), n. 86 (perfeito do subjuntivo em -erim e mais-que-perfeito em -issem, formados do perfeito), n. 88 (imperfeito do subjuntivo = infinitivo presente + m, s, t, mus, tis, nt), nn. 366–374 (subjuntivo nas orações independentes: potencial, optativo, dubitativo, exortativo, concessivo; o mandado negativo)', tipo='dominio_publico'),
        referencia("D'Ooge, Latin for Beginners", "Benjamin L. D'Ooge", catalogo='d-ooge-latin-for-beginners', nota='lições LXI, LXIII e LXIV (flexão do subjuntivo nos quatro tempos), LXV (subjuntivo de possum) e LXVII–LXVIII (volō, nōlō, mālō; fīō); conferidas no sumário da edição do Projeto Gutenberg', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Gênesis 1,3 e 1,26; Mateus 6,9–10 e 6,13', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Matthaeum', nota='frases autênticas das seções 5 e 6 e dos exercícios, conferidas no texto da Wikisource latina (Liber Genesis, cap. 1; Evangelium Secundum Matthaeum, cap. 6); ortografia adaptada (ae por æ, i por j) e macrons acrescentados', tipo='dominio_publico'),
        referencia('Catulo, Carmina 5.1', 'Gaius Valerius Catullus', catalogo='catullus-catulli-carmina', url='https://www.thelatinlibrary.com/catullus.shtml', nota='verso analisado no exercício 5, conferido no texto da Latin Library; macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Explicar a diferença entre o indicativo (o fato) e o subjuntivo (a ação querida, desejada ou apenas possível), comparando-a com o subjuntivo português.',
        'Formar e reconhecer os quatro tempos do subjuntivo, na ativa e na passiva, nas quatro conjugações, sem confundi-los com o presente e o futuro do indicativo.',
        'Conjugar o presente e o imperfeito do subjuntivo de <i>sum, possum, volō, nōlō, mālō, eō, ferō</i> e <i>fīō</i>.',
        'Identificar e traduzir os usos do subjuntivo em oração principal: exortativo, jussivo, proibição com <i>nē</i>, optativo, deliberativo e potencial, escolhendo a negação correta (<i>nē</i> ou <i>nōn</i>).',
        'Analisar palavra a palavra frases autênticas da Vulgata e de Catulo construídas com o subjuntivo.',
    ],
    secoes=[
        ('O que o subjuntivo exprime', f'''
<p>Até aqui todos os verbos deste livro estiveram no <b>indicativo</b>, o modo de quem afirma ou pergunta sobre um fato: <i>puer venit</i>, "o menino vem"; <i>puer vēnit</i>, "o menino veio". Neste capítulo entra o <b>subjuntivo</b> (em latim, <i>modus coniūnctīvus</i> ou <i>subiūnctīvus</i>), o modo de quem não afirma um fato, mas apresenta a ação como algo <b>querido</b>, <b>desejado</b> ou <b>apenas possível</b>. É essa a divisão que Bennett usa para os usos em oração independente: o subjuntivo volitivo (a vontade), o optativo (o desejo) e o potencial (a possibilidade) (§ 272); Allen &amp; Greenough dizem o mesmo de outro modo: o subjuntivo exprime a ideia verbal "com alguma modificação", e não como simples realidade (§ 438).</p>
<p>O falante de português tem aqui uma vantagem enorme, porque a nossa língua conservou o subjuntivo latino. Compare: "o menino <b>vem</b>" (fato) e "que o menino <b>venha</b>!" (vontade); "talvez ele <b>diga</b>" (possibilidade); "quem dera ele <b>estivesse</b> aqui!" (desejo irrealizável). Em todos esses casos o português põe o verbo no subjuntivo pelas mesmas razões que o latim. A diferença principal é de frequência e de lugar. O português usa o subjuntivo quase só em orações subordinadas ("quero <b>que</b> venha", "embora <b>chova</b>"); o latim o usa muito nas subordinadas (capítulos 33 a 38) e também, com bastante frequência, em <b>orações principais</b>, sem nenhuma conjunção. Este capítulo trata das formas e desses usos independentes.</p>
<p>O subjuntivo latino tem só <b>quatro tempos</b>: presente, imperfeito, perfeito e mais-que-perfeito. Não há futuro nem futuro perfeito do subjuntivo (o que o latim faz quando precisa de um futuro numa oração subordinada é assunto do capítulo 34). E há um aviso que vale para todo o capítulo: o nome do tempo latino <b>não</b> manda no tempo da tradução. O imperfeito do subjuntivo pode significar um desejo irrealizável no presente (<i>utinam adesset</i>, "quem dera ele estivesse aqui <b>agora</b>"), e o perfeito do subjuntivo, numa proibição, não tem nada de passado (<i>nē timuerīs</i>, "não tenhas medo"). Cada uso tem a sua tradução, e é ela que você deve aprender junto com a forma.</p>
{comparacao('Indicativo e subjuntivo: o fato e a ação vista de outro modo', ['Latim', 'Modo e valor', 'Português'], [
    ['Puer venit.', 'indicativo: fato', 'O menino vem.'],
    ['Puer veniat!', 'subjuntivo: vontade (jussivo)', 'Que o menino venha! Venha o menino!'],
    ['Veniāmus!', 'subjuntivo: exortação', 'Venhamos! Vamos!'],
    ['Utinam puer veniat!', 'subjuntivo: desejo possível', 'Tomara que o menino venha!'],
    ['Quid faciam?', 'subjuntivo: deliberação', 'Que hei de fazer? Que faço?'],
    ['Dīcat aliquis…', 'subjuntivo: possibilidade', 'Alguém poderia dizer…'],
])}
'''),
        ('O presente do subjuntivo: a troca de vogal', f'''
<p>O presente do subjuntivo se forma sobre o tema do presente e se reconhece por uma <b>troca de vogal</b> antes das terminações pessoais que você já conhece (<i>-m, -s, -t, -mus, -tis, -nt</i>; atenção: no subjuntivo a primeira pessoa é sempre em <i>-m</i>, nunca em <i>-ō</i>). A regra prática cabe numa frase: <b>a primeira conjugação troca o seu <i>ā</i> por <i>ē</i>; todas as outras põem um <i>ā</i></b> (Ravizza n. 85; A&amp;G § 168.e; Bennett §§ 101, 103, 105, 107).</p>
{tabela(['Pessoa', '1ª · amō', '2ª · moneō', '3ª · regō', '3ª em -iō · capiō', '4ª · audiō'], [
    ['1ª sing.', 'am<b>em</b>', 'mone<b>am</b>', 'reg<b>am</b>', 'capi<b>am</b>', 'audi<b>am</b>'],
    ['2ª sing.', 'am<b>ēs</b>', 'mone<b>ās</b>', 'reg<b>ās</b>', 'capi<b>ās</b>', 'audi<b>ās</b>'],
    ['3ª sing.', 'am<b>et</b>', 'mone<b>at</b>', 'reg<b>at</b>', 'capi<b>at</b>', 'audi<b>at</b>'],
    ['1ª pl.', 'am<b>ēmus</b>', 'mone<b>āmus</b>', 'reg<b>āmus</b>', 'capi<b>āmus</b>', 'audi<b>āmus</b>'],
    ['2ª pl.', 'am<b>ētis</b>', 'mone<b>ātis</b>', 'reg<b>ātis</b>', 'capi<b>ātis</b>', 'audi<b>ātis</b>'],
    ['3ª pl.', 'am<b>ent</b>', 'mone<b>ant</b>', 'reg<b>ant</b>', 'capi<b>ant</b>', 'audi<b>ant</b>'],
], 'Presente do subjuntivo ativo', latim_cols=(1, 2, 3, 4, 5))}
<p>Repare que a vogal é longa em <i>-ēs, -ēmus, -ētis</i> e <i>-ās, -āmus, -ātis</i>, e breve antes de <i>-m</i>, <i>-t</i> e <i>-nt</i>, como já acontecia no indicativo (capítulo 6). Na 2ª, na 3ª em <i>-iō</i> e na 4ª, o <i>e</i> ou o <i>i</i> do tema continua visível antes do <i>a</i>: <i>mone-am</i>, <i>capi-am</i>, <i>audi-am</i>; na 3ª comum o <i>a</i> se junta direto à raiz: <i>reg-am</i>.</p>
{observacao('A mesma troca em português', 'O português herdou essa troca de vogal sem alteração. Verbos em <b>-ar</b> fazem o presente do subjuntivo em <b>-e</b>: amar → "que eu am<b>e</b>", cantar → "que ele cant<b>e</b>"; verbos em <b>-er</b> e <b>-ir</b> fazem em <b>-a</b>: vender → "que eu vend<b>a</b>", partir → "que ele part<b>a</b>", ouvir → "que eu ouç<b>a</b>". É exatamente a regra latina: <i>amet</i> / "ame", <i>regat</i> / "reja", <i>audiat</i> / "ouça". Se você conjuga o subjuntivo português sem pensar, já sabe a regra latina.')}
<h3>Duas armadilhas de reconhecimento</h3>
<p><b>Primeira: o <i>-ē-</i> não é exclusivo do subjuntivo.</b> Na 1ª conjugação o <i>ē</i> marca o subjuntivo (<i>amēs</i>, "que ames"), mas na 2ª ele é a vogal do próprio tema no indicativo (<i>monēs</i>, "advertes"), e na 3ª e na 4ª ele marca o <b>futuro</b> do indicativo (<i>regēs</i>, "regerás"; <i>audiēs</i>, "ouvirás", capítulo 12). Por isso nunca leia a vogal antes de saber a conjugação: primeiro o dicionário, depois a terminação.</p>
<p><b>Segunda: <i>regam, capiam, audiam</i> são ambíguos.</b> Na 3ª e na 4ª conjugações, a 1ª pessoa do singular do futuro do indicativo é igual à do presente do subjuntivo: <i>regam</i> pode ser "regerei" ou "que eu reja". Nas outras pessoas as formas se separam (<i>regēs</i> × <i>regās</i>, <i>reget</i> × <i>regat</i>), e na 1ª pessoa o contexto decide: uma pergunta deliberativa (<i>quid agam?</i>) ou uma conjunção que pede subjuntivo resolve a dúvida.</p>
{tabela(['Conjugação', 'Pres. indicativo', 'Futuro indicativo', 'Pres. subjuntivo'], [
    ['1ª', 'amās, amat', 'amābis, amābit', 'am<b>ē</b>s, am<b>e</b>t'],
    ['2ª', 'monēs, monet', 'monēbis, monēbit', 'mone<b>ā</b>s, mone<b>a</b>t'],
    ['3ª', 'regis, regit', 'reg<b>ē</b>s, reg<b>e</b>t', 'reg<b>ā</b>s, reg<b>a</b>t'],
    ['4ª', 'audīs, audit', 'audi<b>ē</b>s, audi<b>e</b>t', 'audi<b>ā</b>s, audi<b>a</b>t'],
], '2ª e 3ª pessoas do singular: indicativo, futuro e subjuntivo lado a lado', latim_cols=(1, 2, 3))}
<h3>O presente do subjuntivo passivo</h3>
<p>Na passiva a troca de vogal é a mesma; mudam só as terminações, que são as da passiva do capítulo 23 (<i>-r, -ris, -tur, -mur, -minī, -ntur</i>): <i>amer, amēris, amētur, amēmur, amēminī, amentur</i>; <i>regar, regāris, regātur, regāmur, regāminī, regantur</i>; <i>audiar, audiāris, audiātur</i> (Bennett § 102). A forma <i>-ēris/-āris</i> tem a variante <i>-ēre/-āre</i>, como no indicativo.</p>
{exemplos([('Puer veni<b>at</b>.', 'Que o menino venha. (3ª sing., presente do subjuntivo de <i>veniō</i>, 4ª)'), ('Librōs leg<b>āmus</b>.', 'Leiamos os livros. (1ª pl. de <i>legō</i>, 3ª)'), ('Magister puerōs mone<b>at</b>.', 'Que o professor advirta os meninos. (<i>moneat</i>, e não <i>monet</i>)'), ('Lēgēs serv<b>entur</b>.', 'Que as leis sejam observadas. (passiva de <i>servō, -āre</i>, "guardar, observar")')])}
'''),
        ('Imperfeito, perfeito e mais-que-perfeito', f'''
<p>Os outros três tempos são mais fáceis de formar do que o presente, porque seguem uma única regra em todas as conjugações.</p>
<h3>Imperfeito: o infinitivo + as terminações</h3>
<p>Tome o <b>infinitivo presente ativo</b> e acrescente <i>-m, -s, -t, -mus, -tis, -nt</i>, alongando o <i>e</i> final do infinitivo em <i>-ēs, -ēmus, -ētis</i>: <i>amāre</i> → <i>amārem</i>; <i>regere</i> → <i>regerem</i>. É a regra de Ravizza (n. 88), e Allen &amp; Greenough descrevem o mesmo tempo como o tema do presente seguido de <i>-rem, -rēs</i> (§ 168.f). A vantagem prática é enorme: quem sabe o infinitivo sabe o imperfeito do subjuntivo, inclusive, como você verá na seção 4, o dos verbos irregulares.</p>
{tabela(['Pessoa', 'amō, amāre', 'moneō, monēre', 'regō, regere', 'capiō, capere', 'audiō, audīre'], [
    ['1ª sing.', 'amāre<b>m</b>', 'monēre<b>m</b>', 'regere<b>m</b>', 'capere<b>m</b>', 'audīre<b>m</b>'],
    ['2ª sing.', 'amārē<b>s</b>', 'monērē<b>s</b>', 'regerē<b>s</b>', 'caperē<b>s</b>', 'audīrē<b>s</b>'],
    ['3ª sing.', 'amāre<b>t</b>', 'monēre<b>t</b>', 'regere<b>t</b>', 'capere<b>t</b>', 'audīre<b>t</b>'],
    ['1ª pl.', 'amārē<b>mus</b>', 'monērē<b>mus</b>', 'regerē<b>mus</b>', 'caperē<b>mus</b>', 'audīrē<b>mus</b>'],
    ['2ª pl.', 'amārē<b>tis</b>', 'monērē<b>tis</b>', 'regerē<b>tis</b>', 'caperē<b>tis</b>', 'audīrē<b>tis</b>'],
    ['3ª pl.', 'amāre<b>nt</b>', 'monēre<b>nt</b>', 'regere<b>nt</b>', 'capere<b>nt</b>', 'audīre<b>nt</b>'],
], 'Imperfeito do subjuntivo ativo', latim_cols=(1, 2, 3, 4, 5))}
<p>Na passiva, o mesmo tema recebe as terminações passivas: <i>amārer, amārēris, amārētur, amārēmur, amārēminī, amārentur</i>; <i>regerer, regerēris, regerētur</i> (Bennett § 102). Note que <i>capere</i> dá <i>caperem</i>, sem o <i>i</i> de <i>capiam</i>: o imperfeito sai do infinitivo, e o infinitivo de <i>capiō</i> é <i>capere</i>.</p>
<h3>Perfeito e mais-que-perfeito: o tema do perfeito</h3>
<p>Os dois tempos do perfectum se formam sobre o <b>tema do perfeito</b>, que você aprendeu a tirar da terceira parte principal no capítulo 13 (<i>amāvī</i> → <i>amāv-</i>; <i>monuī</i> → <i>monu-</i>; <i>rēxī</i> → <i>rēx-</i>; <i>cēpī</i> → <i>cēp-</i>; <i>audīvī</i> → <i>audīv-</i>). O <b>perfeito</b> acrescenta <i>-erim, -erīs, -erit, -erīmus, -erītis, -erint</i>; o <b>mais-que-perfeito</b>, <i>-issem, -issēs, -isset, -issēmus, -issētis, -issent</i> (A&amp;G § 169.d–e; Ravizza n. 86). Um atalho para o mais-que-perfeito: é o <b>infinitivo perfeito</b> + as terminações, <i>amāvisse</i> → <i>amāvissem</i>, do mesmo modo que o imperfeito é o infinitivo presente + as terminações.</p>
{tabela(['Pessoa', 'Perfeito', 'Mais-que-perfeito'], [
    ['1ª sing.', 'amāv<b>erim</b>', 'amāv<b>issem</b>'],
    ['2ª sing.', 'amāv<b>erīs</b>', 'amāv<b>issēs</b>'],
    ['3ª sing.', 'amāv<b>erit</b>', 'amāv<b>isset</b>'],
    ['1ª pl.', 'amāv<b>erīmus</b>', 'amāv<b>issēmus</b>'],
    ['2ª pl.', 'amāv<b>erītis</b>', 'amāv<b>issētis</b>'],
    ['3ª pl.', 'amāv<b>erint</b>', 'amāv<b>issent</b>'],
], 'O perfectum do subjuntivo ativo: amō, amāvī', latim_cols=(1, 2))}
<p>O perfeito do subjuntivo é quase idêntico ao <b>futuro perfeito</b> do indicativo (capítulo 13): só a 1ª pessoa do singular difere sempre (<i>amāverim</i> × <i>amāverō</i>); <i>amāverit</i> e <i>amāverint</i> têm a mesma grafia nos dois tempos. Bennett marca longo o <i>ī</i> de <i>-erīs, -erīmus, -erītis</i> no subjuntivo e breve no futuro perfeito (§§ 100–101), e este livro segue essa grafia. Allen &amp; Greenough imprimem breve também no subjuntivo (<i>-eris</i>) e explicam por quê: o <i>ī</i> era originalmente longo (é o sinal do antigo optativo), formas com <i>-īs, -īmus, -ītis</i> ainda se encontram, e a abreviação vem da confusão com o futuro perfeito (§ 169.d, nota). É uma variante de notação, não um erro de nenhuma das duas gramáticas. Na leitura, quem decide é o contexto.</p>
<p>Na <b>passiva</b>, o perfectum do subjuntivo é o particípio perfeito com o subjuntivo de <i>sum</i>, exatamente como no indicativo (capítulo 24), trocando <i>sum</i> por <i>sim</i> e <i>eram</i> por <i>essem</i>: <i>amātus sim</i> (perfeito), <i>amātus essem</i> (mais-que-perfeito). O particípio concorda com o sujeito: <i>puellae laudātae sint</i>, <i>urbs capta esset</i>.</p>
{tabela(['Tempo', '1ª · amō', '2ª · moneō', '3ª · regō', '3ª -iō · capiō', '4ª · audiō'], [
    ['Presente', 'amet', 'moneat', 'regat', 'capiat', 'audiat'],
    ['Imperfeito', 'amāret', 'monēret', 'regeret', 'caperet', 'audīret'],
    ['Perfeito', 'amāverit', 'monuerit', 'rēxerit', 'cēperit', 'audīverit'],
    ['Mais-que-perf.', 'amāvisset', 'monuisset', 'rēxisset', 'cēpisset', 'audīvisset'],
    ['Pres. passivo', 'amētur', 'moneātur', 'regātur', 'capiātur', 'audiātur'],
    ['Imperf. passivo', 'amārētur', 'monērētur', 'regerētur', 'caperētur', 'audīrētur'],
    ['Perf. passivo', 'amātus sit', 'monitus sit', 'rēctus sit', 'captus sit', 'audītus sit'],
    ['M.-q.-perf. passivo', 'amātus esset', 'monitus esset', 'rēctus esset', 'captus esset', 'audītus esset'],
], 'Quadro-resumo: a 3ª pessoa do singular de todos os tempos do subjuntivo', latim_cols=(1, 2, 3, 4, 5))}
{dica('Para reconhecer o tempo de um subjuntivo, procure três sinais: a vogal trocada (<i>amet, regat</i>) é presente; <i>-re-</i>/<i>-rē-</i> depois do tema do presente (<i>amāret, regerētur</i>) é imperfeito; <i>-eri-</i> depois do tema do perfeito (<i>rēxerit</i>) é perfeito; <i>-isse-</i> (<i>rēxisset</i>) é mais-que-perfeito.')}
'''),
        ('Sum, possum e os verbos irregulares', f'''
<p>O verbo <i>sum</i> tem um presente do subjuntivo próprio, em <i>-im</i>, que é uma forma muito antiga (A&amp;G § 168.e, nota 2, a chama de antigo optativo). O imperfeito obedece à regra do infinitivo: <i>esse</i> → <i>essem</i>. O perfectum se forma sobre <i>fu-</i>, como qualquer verbo (Bennett § 100; A&amp;G § 170).</p>
{tabela(['Pessoa', 'Presente', 'Imperfeito', 'Perfeito', 'Mais-que-perfeito'], [
    ['1ª sing.', 'si<b>m</b>', 'esse<b>m</b>', 'fu<b>erim</b>', 'fu<b>issem</b>'],
    ['2ª sing.', 'sī<b>s</b>', 'essē<b>s</b>', 'fu<b>erīs</b>', 'fu<b>issēs</b>'],
    ['3ª sing.', 'si<b>t</b>', 'esse<b>t</b>', 'fu<b>erit</b>', 'fu<b>isset</b>'],
    ['1ª pl.', 'sī<b>mus</b>', 'essē<b>mus</b>', 'fu<b>erīmus</b>', 'fu<b>issēmus</b>'],
    ['2ª pl.', 'sī<b>tis</b>', 'essē<b>tis</b>', 'fu<b>erītis</b>', 'fu<b>issētis</b>'],
    ['3ª pl.', 'si<b>nt</b>', 'esse<b>nt</b>', 'fu<b>erint</b>', 'fu<b>issent</b>'],
], 'Subjuntivo de sum, esse, fuī', latim_cols=(1, 2, 3, 4))}
<p>Em vez de <i>essem, essēs, esset, essent</i>, os autores usam às vezes <i>forem, forēs, foret, forent</i>, com o mesmo valor (A&amp;G § 170.a); vale reconhecê-las, sobretudo nos poetas. <b>Possum</b> segue <i>sum</i> com o prefixo <i>pos-</i>: presente <i>possim, possīs, possit, possīmus, possītis, possint</i>; imperfeito <i>possem</i> (de <i>posse</i>); perfeito <i>potuerim</i>; mais-que-perfeito <i>potuissem</i> (Bennett § 126; A&amp;G § 198.b).</p>
<h3>Os outros irregulares</h3>
<p>No capítulo 26 você estudou o indicativo de <i>volō, nōlō, mālō, eō, ferō</i> e <i>fīō</i>. O subjuntivo deles é mais regular do que parece: <i>volō, nōlō, mālō</i> fazem o presente em <i>-im</i>, como <i>sim</i>; <i>eō, ferō, fīō</i> fazem o presente em <i>-am</i>, como a 3ª e a 4ª conjugações; e o imperfeito de todos sai do infinitivo, com a única exceção de <i>fīō</i> (<i>fierem</i>, e não sobre <i>fierī</i>). O perfectum é sempre regular sobre o tema do perfeito: <i>voluerim, voluissem</i>; <i>īverim</i> ou <i>ierim</i>; <i>tulerim, tulissem</i>.</p>
{tabela(['Verbo', 'Infinitivo', 'Pres. subjuntivo', 'Imperf. subjuntivo'], [
    ['volō, querer', 'velle', 'vel<b>im</b>, velīs, velit, velīmus, velītis, velint', 'velle<b>m</b>, vellēs, vellet…'],
    ['nōlō, não querer', 'nōlle', 'nōl<b>im</b>, nōlīs, nōlit…', 'nōlle<b>m</b>, nōllēs…'],
    ['mālō, preferir', 'mālle', 'māl<b>im</b>, mālīs, mālit…', 'mālle<b>m</b>, māllēs…'],
    ['eō, ir', 'īre', 'e<b>am</b>, eās, eat, eāmus, eātis, eant', 'īre<b>m</b>, īrēs, īret…'],
    ['ferō, levar', 'ferre', 'fer<b>am</b>, ferās, ferat, ferāmus, ferātis, ferant', 'ferre<b>m</b>, ferrēs, ferret…'],
    ['fīō, tornar-se, ser feito', 'fierī', 'fī<b>am</b>, fīās, fīat, fīāmus, fīātis, fīant', 'fiere<b>m</b>, fierēs, fieret…'],
    ['possum, poder', 'posse', 'poss<b>im</b>, possīs, possit…', 'posse<b>m</b>, possēs…'],
], 'Presente e imperfeito do subjuntivo dos verbos irregulares (Bennett §§ 126, 129–132)', latim_cols=(1, 2, 3))}
<p>Duas formas aparecem a toda hora nos textos e merecem ser decoradas já: <i>fīat</i>, "faça-se, aconteça, seja feito", e <i>eāmus</i>, "vamos!". Note ainda que <i>feram</i> e <i>eam</i> não se confundem com o indicativo: <i>feram</i> é também a 1ª pessoa do futuro (como <i>regam</i>), mas <i>eam</i> não, porque o futuro de <i>eō</i> é <i>ībō</i>.</p>
'''),
        ('Usos independentes (I): a vontade — exortação, ordem e proibição', f'''
<p>Quando o subjuntivo aparece numa oração principal, sem conjunção que o explique, ele exprime uma atitude do falante. A primeira família de usos é a da <b>vontade</b> (subjuntivo volitivo): quem fala exorta, ordena ou proíbe. A negação desses usos é sempre <b><i>nē</i></b>, e não <i>nōn</i> (Bennett §§ 273–276; A&amp;G § 439).</p>
<h3>Exortativo: "façamos!"</h3>
<p>Na <b>1ª pessoa do plural do presente</b>, o subjuntivo convida o próprio grupo do falante a agir: <i>eāmus</i>, "vamos!"; <i>amēmus patriam</i>, "amemos a pátria"; <i>nē dēspērēmus</i>, "não desesperemos" (exemplos de Bennett § 274). O português faz igual, com o mesmo tempo: "amemos", "não desesperemos", ou, mais coloquial, "vamos amar".</p>
<h3>Jussivo: "que ele faça!"</h3>
<p>Na <b>3ª pessoa</b> (singular e plural), o presente do subjuntivo dá uma ordem a alguém que não é o interlocutor: <i>dīcat</i>, "que ele diga, diga ele"; <i>dīcant</i>, "que digam" (Bennett § 275). Para a 2ª pessoa o latim tem o imperativo (capítulo 22), e por isso o jussivo na 2ª pessoa é raro e costuma ter sujeito indeterminado ("a gente", "quem quer que seja"). O português usa a mesma construção, às vezes com "que": "venha o teu reino", "que entrem os próximos".</p>
<p>É aqui que está a frase mais famosa da Bíblia latina, logo no terceiro versículo do Gênesis:</p>
{diagrama_frase([('Dīxit Deus', 'indicativo · fato narrado'), ('Fīat', 'subjuntivo de fīō · ordem (jussivo)'), ('lūx', 'nominativo · sujeito de fīat'), ('facta est lūx', 'indicativo · fato cumprido')],
    '<i>Dīxitque Deus: Fīat lūx. Et facta est lūx</i> (Gênesis 1,3) = E Deus disse: Faça-se a luz. E a luz foi feita. A ordem vem no subjuntivo; o seu cumprimento, no indicativo, com o perfeito passivo do mesmo verbo.')}
<p>O versículo mostra com perfeição a diferença entre os dois modos. <i>Fīat</i> não diz que a luz existe; diz que Deus a quer. Logo depois, <i>facta est</i> (perfeito do indicativo, "foi feita") registra o fato. Três versículos mais tarde, o mesmo capítulo usa o exortativo: <i>Faciāmus hominem</i>, "Façamos o homem" (Gênesis 1,26).</p>
<h3>Proibição: nē + perfeito do subjuntivo</h3>
<p>Para proibir algo a quem se fala, a prosa clássica tem três construções (A&amp;G § 450): <b><i>nōlī</i> / <i>nōlīte</i> + infinitivo</b>, que você conheceu no capítulo 22 (<i>nōlī timēre</i>, "não tenhas medo"), a mais cerimoniosa e a mais frequente; <b><i>cavē</i> + presente do subjuntivo</b> (<i>cavē putēs</i>, "não vás pensar"); e <b><i>nē</i> + perfeito do subjuntivo</b>, mais seca e peremptória: <i>nē timuerīs</i>, "não tenhas medo"; <i>hōc nē fēcerīs</i>, "não faças isto" (exemplos de A&amp;G § 450; a mesma regra em Kennedy § 347). Atenção à tradução: nessa construção o perfeito <b>não tem valor de passado</b>; traduza por um imperativo negativo ("não faças", "não faça você").</p>
{exemplos([('Nē timuerīs.', 'Não tenhas medo. (= <i>Nōlī timēre</i>.)'), ('Nē hōc dīxerītis.', 'Não digais isto. Não digam isto.'), ('Nē dēspērēmus.', 'Não desesperemos. (exortativo negativo, com <i>nē</i>)'), ('Servī nē dormiant.', 'Que os escravos não durmam. (jussivo negativo)')])}
{observacao('E o nē com o presente?', 'Na poesia e no latim posterior, a proibição também aparece com <i>nē</i> + <b>presente</b> do subjuntivo (A&amp;G § 450, nota 3; Bennett § 276 diz que os dois tempos ocorrem "sem diferença apreciável de sentido"). É o caso do Pai-Nosso na Vulgata: <i>Et nē nōs indūcās in tentātiōnem</i>, "e não nos deixeis cair em tentação" (Mateus 6,13; literalmente, "não nos induzas"). Na prosa de Cícero e César, prefira o perfeito.')}
'''),
        ('Usos independentes (II): desejo, deliberação e possibilidade', f'''
<h3>Optativo: o desejo, com ou sem utinam</h3>
<p>O subjuntivo <b>optativo</b> exprime um desejo, muitas vezes introduzido pela partícula <i>utinam</i>, "oxalá, tomara, quem dera". A negação é <i>nē</i> (<i>utinam nē</i>). O tempo, aqui, tem um sentido preciso, e é o que mais engana o falante de português (Bennett § 279; A&amp;G §§ 441–442; Kennedy § 359):</p>
{tabela(['Tempo', 'O desejo é…', 'Exemplo', 'Tradução'], [
    ['Presente', 'possível (pode realizar-se)', '(Utinam) valeās!', 'Tomara que estejas bem! Que estejas bem!'],
    ['Imperfeito', 'irrealizável no presente', 'Utinam adessēs!', 'Quem dera estivesses aqui (agora)!'],
    ['Mais-que-perfeito', 'irrealizável no passado', 'Utinam vēnissēs!', 'Quem dera tivesses vindo!'],
], 'O tempo do optativo e o valor do desejo', latim_cols=(2,))}
<p>Repare que o imperfeito latino se refere ao <b>presente</b>, e o mais-que-perfeito, ao <b>passado</b>: é a mesma lógica do português "quem dera <b>estivesses</b> aqui" (agora) e "quem dera <b>tivesses</b> vindo" (ontem). Um exemplo autêntico, citado por Allen &amp; Greenough (§ 442) e por Bennett (§ 279): <i>Falsus utinam vātēs sim!</i>, "Oxalá eu seja um falso profeta!" (Tito Lívio 21.10.10), presente porque o desejo ainda pode cumprir-se. E é optativo (ou jussivo; a fronteira entre os dois é tênue na oração) o Pai-Nosso, analisado abaixo.</p>
<h3>Deliberativo: "que hei de fazer?"</h3>
<p>Em perguntas que o falante faz a si mesmo, cheias de dúvida ou de indignação, o latim usa o subjuntivo <b>deliberativo</b>: <i>Quid faciam?</i>, "que hei de fazer? que faço?"; no passado, o imperfeito: <i>Quid facerem?</i>, "que havia eu de fazer?". A negação é <i>nōn</i>: <i>Hunc ego nōn dīligam?</i>, "e eu não havia de estimar este homem?" (Bennett § 277; A&amp;G § 444; Kennedy § 358). O português coloquial costuma responder com o presente do indicativo ("que faço agora?") ou com "hei de", "devo".</p>
<h3>Potencial: "alguém poderia dizer"</h3>
<p>Por fim, o subjuntivo <b>potencial</b> apresenta a ação como apenas possível, para atenuar uma afirmação. As fórmulas mais comuns são <i>dīcat aliquis</i> ou <i>dīxerit aliquis</i>, "alguém poderia dizer" (o perfeito, de novo, sem valor de passado), <i>velim</i>, "eu gostaria", em vez do seco <i>volō</i>, e, no passado, o imperfeito de 2ª pessoa com sujeito indeterminado: <i>vidērēs</i>, "poderias ver, ter-se-ia visto"; <i>crēderēs</i>, "dir-se-ia" (Bennett § 280; A&amp;G §§ 446–447; Kennedy § 356). A negação é <i>nōn</i>.</p>
{tabela(['Uso', 'Pessoa e tempo típicos', 'Negação', 'Exemplo', 'Português'], [
    ['Exortativo', '1ª pl., presente', 'nē', 'Eāmus! Nē dēspērēmus!', 'Vamos! Não desesperemos!'],
    ['Jussivo', '3ª pessoa, presente', 'nē', 'Veniat! Nē veniant!', 'Que venha! Que não venham!'],
    ['Proibição', '2ª pessoa, perfeito', 'nē', 'Nē fēcerīs!', 'Não faças!'],
    ['Optativo', 'pres. / imperf. / m.-q.-perf., muitas vezes com utinam', 'nē', 'Utinam adesset!', 'Quem dera ele estivesse aqui!'],
    ['Deliberativo', 'pergunta; presente ou imperfeito', 'nōn', 'Quid faciam?', 'Que hei de fazer?'],
    ['Potencial', 'presente ou perfeito; imperf. no passado', 'nōn', 'Dīxerit aliquis…', 'Alguém poderia dizer…'],
], 'Os usos independentes do subjuntivo: quadro geral', latim_cols=(3,))}
{dica('Regra da negação, em uma linha: se a frase exprime <b>vontade ou desejo</b> (exortar, ordenar, proibir, desejar), a negação é <i>nē</i>; se exprime <b>dúvida ou possibilidade</b> (deliberar, supor), a negação é <i>nōn</i>.')}
<h3>Análise gramatical: o Pai-Nosso</h3>
<p>A oração que Jesus ensina no Evangelho de Mateus reúne, em três frases curtas, três subjuntivos independentes de vontade e desejo. O texto é o da Vulgata Clementina (Mateus 6,9–10):</p>
{exemplos([('Pater noster, quī es in caelīs, sānctificētur nōmen tuum. Adveniat rēgnum tuum; fīat voluntās tua, sīcut in caelō et in terrā.', 'Pai nosso, que estás nos céus, santificado seja o teu nome. Venha o teu reino; seja feita a tua vontade, assim no céu como na terra.')])}
{analise('Mateus 6,9–10, palavra a palavra', [
    ('Pater', 'pater, patris (m.), pai', 'vocativo singular, 3ª declinação', 'a quem se fala: "Pai"'),
    ('noster', 'noster, nostra, nostrum, nosso', 'vocativo singular masculino', 'concorda com <i>Pater</i>'),
    ('quī', 'quī, quae, quod, que (relativo)', 'nominativo singular masculino', 'sujeito de <i>es</i>; antecedente <i>Pater</i> (capítulo 16)'),
    ('es', 'sum, esse, fuī, ser, estar', '2ª sing., presente do <b>indicativo</b>', 'fato: "que estás"'),
    ('in caelīs', 'caelum, -ī (n.), céu', '<i>in</i> + ablativo plural', 'lugar onde'),
    ('sānctificētur', 'sānctificō, -āre, santificar', '3ª sing., presente do <b>subjuntivo passivo</b> (1ª conj.: <i>ā</i> → <i>ē</i>)', 'desejo/ordem: "seja santificado"'),
    ('nōmen tuum', 'nōmen, nōminis (n.), nome', 'nominativo singular neutro', 'sujeito de <i>sānctificētur</i>'),
    ('Adveniat', 'adveniō, -īre, -vēnī, -ventum, chegar', '3ª sing., presente do <b>subjuntivo</b> ativo (4ª: + <i>a</i>)', 'jussivo/optativo: "venha"'),
    ('rēgnum tuum', 'rēgnum, -ī (n.), reino', 'nominativo singular neutro', 'sujeito de <i>adveniat</i>'),
    ('fīat', 'fīō, fierī, factus sum, ser feito, acontecer', '3ª sing., presente do <b>subjuntivo</b>', 'jussivo/optativo: "seja feita"'),
    ('voluntās tua', 'voluntās, -ātis (f.), vontade', 'nominativo singular feminino', 'sujeito de <i>fīat</i>'),
    ('sīcut … et', 'sīcut, assim como; et, também', 'advérbio e conjunção', 'comparação: "assim no céu como na terra"'),
])}
<p>Observe o contraste dentro da mesma frase: <i>es</i> está no indicativo porque diz um fato (o Pai <b>está</b> nos céus); os três verbos principais estão no subjuntivo porque dizem o que se <b>deseja</b>. Note também que os três subjuntivos vêm antes do sujeito, posição de destaque, e que a tradução portuguesa tradicional conserva o subjuntivo nos três ("seja", "venha", "seja feita"). Se você trocasse <i>adveniat</i> por <i>advenit</i>, a frase passaria a afirmar que o reino <b>vem</b>.</p>
<h3>Resumo</h3>
<ul>
<li>Formas: presente com troca de vogal (<i>amem</i>; <i>moneam, regam, capiam, audiam</i>); imperfeito = infinitivo + terminações (<i>amārem, regerem</i>); perfeito = tema do perfeito + <i>-erim</i>; mais-que-perfeito = tema do perfeito + <i>-issem</i>; passiva do perfectum com <i>sim</i> e <i>essem</i>.</li>
<li><i>Sum</i>: <i>sim, essem, fuerim, fuissem</i>; <i>possum</i>: <i>possim, possem</i>; <i>velim, nōlim, mālim</i>; <i>eam, feram, fīam</i>; imperfeitos <i>vellem, īrem, ferrem, fierem</i>.</li>
<li>Usos de vontade e desejo (negação <i>nē</i>): exortativo, jussivo, proibição (<i>nē</i> + perfeito), optativo.</li>
<li>Usos de dúvida e possibilidade (negação <i>nōn</i>): deliberativo e potencial.</li>
<li>O tempo do subjuntivo não se traduz mecanicamente: o perfeito da proibição e do potencial não é passado; o imperfeito do optativo fala do presente.</li>
</ul>
<p>No próximo capítulo o subjuntivo desce para as orações subordinadas: com <i>ut</i> e <i>nē</i> ele exprime a finalidade, a consequência e o conteúdo de ordens, pedidos e temores.</p>
'''),
    ],
    erros_comuns=[
        ('Ler toda forma com <i>-ē-</i> como subjuntivo: *<i>monēs</i> = "que advirtas", *<i>reget</i> = "que ele reja".', 'O <i>ē</i> só marca o subjuntivo na 1ª conjugação (<i>amēs</i>). Na 2ª ele é a vogal do tema (<i>monēs</i>, indicativo; subjuntivo <i>moneās</i>), e na 3ª e 4ª é o sinal do futuro (<i>reget</i>, "regerá"; subjuntivo <i>regat</i>). Identifique a conjugação pelo infinitivo do dicionário antes de interpretar a vogal.'),
        ('Tomar <i>regam, audiam, capiam, feram</i> sempre como presente do subjuntivo (ou sempre como futuro).', 'Na 1ª pessoa do singular da 3ª e da 4ª conjugações, futuro do indicativo e presente do subjuntivo coincidem. Olhe o contexto: numa pergunta deliberativa (<i>quid agam?</i>) ou depois de <i>ut</i>/<i>nē</i> é subjuntivo; numa narração do que acontecerá, é futuro.'),
        ('Proibir com <i>nōn</i>: *<i>Nōn fēcerīs!</i>, *<i>Nōn dēspērēmus!</i>', 'Usos de vontade (exortativo, jussivo, proibição, optativo) negam-se com <i>nē</i>: <i>Nē fēcerīs!</i>, <i>Nē dēspērēmus!</i>, <i>Utinam nē…</i> O <i>nōn</i> fica para o deliberativo e o potencial, que exprimem dúvida ou possibilidade, não vontade.'),
        ('Traduzir <i>nē timuerīs</i> por "não tenhas temido" e <i>dīxerit aliquis</i> por "alguém terá dito".', 'Na proibição e no potencial, o perfeito do subjuntivo não indica passado: é só uma variante de aspecto, sem diferença de tempo (Bennett §§ 276, 280). Traduza "não tenhas medo" e "alguém poderia dizer".'),
        ('Traduzir <i>utinam adessēs</i> por "tomara que estivesses" (no passado) ou por "tomara que estejas".', 'O imperfeito optativo exprime um desejo <b>irrealizável no presente</b>: "quem dera estivesses aqui (agora, e não estás)". O desejo possível usa o presente (<i>utinam adsīs</i>, "tomara que estejas"), e o irrealizável no passado, o mais-que-perfeito (<i>utinam adfuissēs</i>, "quem dera tivesses estado").'),
        ('Formar o imperfeito do subjuntivo de <i>capiō</i> e dos irregulares pelo presente: *<i>capierem</i>, *<i>volerem</i>, *<i>eerem</i>.', 'O imperfeito sai do infinitivo: <i>capere</i> → <i>caperem</i>; <i>velle</i> → <i>vellem</i>; <i>īre</i> → <i>īrem</i>; <i>ferre</i> → <i>ferrem</i>; <i>esse</i> → <i>essem</i>; <i>posse</i> → <i>possem</i>. A única exceção é <i>fīō</i>, que faz <i>fierem</i>.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Três verbos, três atitudes',
            'Identifique modo, tempo e uso de cada verbo e traduza: <i lang="la">Eāmus in agrum; servī labōrent; tū nē dormīverīs!</i> Vocabulário: <i>eō, īre</i>, ir; <i>ager, agrī</i> (m.), campo; <i>servus, -ī</i>, escravo; <i>labōrō, -āre</i>, trabalhar; <i>dormiō, -īre, -īvī</i>, dormir.', [
            ('Que forma é <i>eāmus</i>, e o que ela exprime?', '1ª pessoa do plural do presente do subjuntivo de <i>eō</i> (o indicativo seria <i>īmus</i>). 1ª do plural + presente do subjuntivo numa oração principal = exortativo: "vamos" (literalmente "vamos nós").'),
            ('E <i>labōrent</i>?', '<i>Labōrō</i> é da 1ª conjugação; o <i>ā</i> do tema virou <i>e</i>: <i>labōr-e-nt</i>, 3ª do plural do presente do subjuntivo (o indicativo seria <i>labōrant</i>). Ordem a uma 3ª pessoa: jussivo, "que os escravos trabalhem".'),
            ('Que forma é <i>dormīverīs</i>?', 'Tema do perfeito <i>dormīv-</i> + <i>-erīs</i>: 2ª do singular do perfeito do subjuntivo. Precedido de <i>nē</i> e dirigido a "tu", é uma proibição; o perfeito não tem valor de passado.'),
            ('Monte a tradução.', '"Vamos para o campo; que os escravos trabalhem; e tu, não durmas!" (Ou: "tu, nada de dormir!")'),
        ], 'Conclusão: o mesmo modo serve para três atitudes, e a pessoa do verbo ajuda a distingui-las: 1ª plural (exortativo), 3ª pessoa (jussivo), 2ª com <i>nē</i> + perfeito (proibição).'),
        pratica_guiada('Prática guiada 2 · Do português para o latim',
            'Traduza para o latim: "Quem dera o pai estivesse em casa! Que hei de dizer aos meninos?" Vocabulário: <i>pater, patris</i>, pai; <i>domī</i>, em casa; <i>dīcō, -ere, dīxī</i>, dizer; <i>puer, -ī</i>, menino.', [
            ('Que uso pede "quem dera o pai estivesse em casa"?', 'Um desejo irrealizável no presente (o pai não está em casa): optativo com <i>utinam</i> e o <b>imperfeito</b> do subjuntivo.'),
            ('Qual a forma de "estivesse"?', 'Imperfeito do subjuntivo de <i>sum</i>, 3ª do singular: <i>esset</i>. Frase: <i>Utinam pater domī esset!</i>'),
            ('E "que hei de dizer"?', 'Pergunta deliberativa do falante a si mesmo, no presente: presente do subjuntivo, 1ª do singular de <i>dīcō</i> (3ª conj., + <i>a</i>): <i>dīcam</i>. Objeto: <i>quid</i>. Dativo: <i>puerīs</i>.'),
            ('Monte a frase.', '<i>Utinam pater domī esset! Quid puerīs dīcam?</i> Repare que <i>dīcam</i> também poderia ser futuro ("direi"); a pergunta deliberativa é que faz dele um subjuntivo.'),
        ]),
    ],
    exercicios=[
        exercicio('Exercício 1 · Indicativo ou subjuntivo?', 'Diga se a forma é do indicativo ou do subjuntivo (ou se pode ser as duas coisas), com tempo, pessoa e número. Use a conjugação dada.', [
            ('<i>amet</i> (<i>amō, -āre</i>)', 'Subjuntivo presente, 3ª sing.: o <i>ā</i> da 1ª conjugação virou <i>e</i>. O indicativo seria <i>amat</i>.'),
            ('<i>monet</i> (<i>moneō, -ēre</i>)', 'Indicativo presente, 3ª sing. Na 2ª conjugação o <i>e</i> é do tema; o subjuntivo seria <i>moneat</i>.'),
            ('<i>reget</i> (<i>regō, -ere</i>)', 'Indicativo <b>futuro</b>, 3ª sing., "regerá". O subjuntivo presente seria <i>regat</i>.'),
            ('<i>audiam</i> (<i>audiō, -īre</i>)', 'Ambígua: futuro do indicativo ("ouvirei") ou presente do subjuntivo ("que eu ouça"), 1ª sing. Só o contexto decide.'),
            ('<i>capiant</i> (<i>capiō, -ere</i>)', 'Subjuntivo presente, 3ª pl. O indicativo seria <i>capiunt</i>; o futuro, <i>capient</i>.'),
            ('<i>essent</i>', 'Subjuntivo imperfeito de <i>sum</i>, 3ª pl. (de <i>esse</i> + <i>-nt</i>).'),
            ('<i>vēnerit</i> (<i>veniō, vēnī</i>)', 'Ambígua: perfeito do subjuntivo ou futuro perfeito do indicativo, 3ª sing.; a grafia é a mesma.'),
            ('<i>possīmus</i>', 'Subjuntivo presente de <i>possum</i>, 1ª pl. O indicativo seria <i>possumus</i>.'),
            ('<i>laudārētur</i> (<i>laudō, -āre</i>)', 'Subjuntivo imperfeito passivo, 3ª sing.: infinitivo <i>laudāre</i> + terminação passiva <i>-tur</i>.'),
            ('<i>dūxissēmus</i> (<i>dūcō, dūxī</i>)', 'Subjuntivo mais-que-perfeito ativo, 1ª pl.: tema do perfeito <i>dūx-</i> + <i>-issēmus</i>.'),
        ]),
        exercicio('Exercício 2 · Conjugue', 'Dê a 3ª pessoa do singular e a 3ª do plural do presente e do imperfeito do subjuntivo ativo.', [
            ('<i>laudō, laudāre</i> (1ª)', 'Presente <i>laudet, laudent</i>; imperfeito <i>laudāret, laudārent</i>.'),
            ('<i>videō, vidēre</i> (2ª)', 'Presente <i>videat, videant</i>; imperfeito <i>vidēret, vidērent</i>.'),
            ('<i>dūcō, dūcere</i> (3ª)', 'Presente <i>dūcat, dūcant</i>; imperfeito <i>dūceret, dūcerent</i>.'),
            ('<i>faciō, facere</i> (3ª em -iō)', 'Presente <i>faciat, faciant</i> (com o <i>i</i>, como <i>capiat</i>); imperfeito <i>faceret, facerent</i> (do infinitivo, sem <i>i</i>).'),
            ('<i>veniō, venīre</i> (4ª)', 'Presente <i>veniat, veniant</i>; imperfeito <i>venīret, venīrent</i>.'),
            ('<i>sum, esse</i>', 'Presente <i>sit, sint</i>; imperfeito <i>esset, essent</i>.'),
            ('<i>volō, velle</i>', 'Presente <i>velit, velint</i>; imperfeito <i>vellet, vellent</i>.'),
            ('<i>ferō, ferre</i>', 'Presente <i>ferat, ferant</i>; imperfeito <i>ferret, ferrent</i>.'),
        ]),
        exercicio('Exercício 3 · Identifique o uso e traduza', 'Diga qual é o uso do subjuntivo (exortativo, jussivo, proibição, optativo, deliberativo, potencial) e traduza. Vocabulário: <i>patria, -ae</i>, pátria; <i>adsum, adesse</i>, estar presente; <i>dēspērō, -āre</i>, desesperar; <i>aliquis</i>, alguém.', [
            ('<i>Amēmus patriam.</i>', 'Exortativo (1ª pl., presente): "Amemos a pátria."'),
            ('<i>Magister veniat.</i>', 'Jussivo (3ª sing., presente): "Que o professor venha", "venha o professor".'),
            ('<i>Nē timuerīs.</i>', 'Proibição (<i>nē</i> + perfeito, 2ª sing.): "Não tenhas medo." Não é "não tenhas temido".'),
            ('<i>Utinam amīcus adesset!</i>', 'Optativo, imperfeito: desejo irrealizável no presente. "Quem dera o amigo estivesse aqui!"'),
            ('<i>Utinam nē vēnissem!</i>', 'Optativo, mais-que-perfeito, negado com <i>nē</i>: desejo irrealizável no passado. "Quem dera eu não tivesse vindo!"'),
            ('<i>Quid faciāmus?</i>', 'Deliberativo (pergunta, presente): "Que havemos de fazer?", "que fazemos?"'),
            ('<i>Dīcat aliquis…</i>', 'Potencial: "Alguém poderia dizer…"'),
            ('<i>Nē dēspērent puerī.</i>', 'Jussivo negativo (3ª pl., com <i>nē</i>): "Que os meninos não desesperem."'),
        ]),
        exercicio('Exercício 4 · Transforme', 'Reescreva no subjuntivo pedido e traduza.', [
            ('<i>Labōrāmus.</i> → exortativo', '<i>Labōrēmus.</i> "Trabalhemos." A 1ª conjugação troca <i>ā</i> por <i>ē</i>.'),
            ('<i>Venīte!</i> (imperativo, 2ª pl.) → jussivo de 3ª pl.', '<i>Veniant!</i> "Que venham!"'),
            ('<i>Nōlī clāmāre!</i> → <i>nē</i> + perfeito do subjuntivo (<i>clāmō, -āre, -āvī</i>, gritar)', '<i>Nē clāmāverīs!</i> "Não grites!" Tema do perfeito <i>clāmāv-</i> + <i>-erīs</i>.'),
            ('<i>Puer bonus est.</i> → desejo possível com <i>utinam</i>', '<i>Utinam puer bonus sit!</i> "Tomara que o menino seja bom!" Presente, porque o desejo pode realizar-se.'),
            ('<i>Quid dīcō?</i> → deliberativo no passado', '<i>Quid dīcerem?</i> "Que havia eu de dizer?" O deliberativo passado usa o imperfeito.'),
            ('<i>Lēx servātur.</i> → jussivo (passiva)', '<i>Lēx servētur.</i> "Que a lei seja observada." Presente do subjuntivo passivo, 1ª conj.'),
        ]),
        exercicio('Exercício 5 · Leitura de frases autênticas', 'Analise o subjuntivo e traduza. Os textos foram conferidos na fonte indicada; macrons acrescentados.', [
            ('<i>Vīvāmus, mea Lesbia, atque amēmus.</i> (Catulo, <i>Carmina</i> 5.1; <i>vīvō, -ere</i>, viver; <i>atque</i>, e)', '<i>Vīvāmus</i> (3ª conj., <i>vīv-</i> + <i>āmus</i>) e <i>amēmus</i> (1ª, <i>ā</i> → <i>ē</i>): presente do subjuntivo, 1ª pl., exortativos. <i>Mea Lesbia</i> é vocativo. "Vivamos, minha Lésbia, e amemos."'),
            ('<i>Faciāmus hominem ad imāginem et similitūdinem nostram.</i> (Gênesis 1,26; <i>imāgō, -inis</i>, imagem; <i>similitūdō, -inis</i>, semelhança)', '<i>Faciāmus</i>: presente do subjuntivo de <i>faciō</i> (3ª em -iō), 1ª pl., exortativo. <i>Hominem</i> é o objeto. "Façamos o homem à nossa imagem e semelhança."'),
            ('<i>Et nē nōs indūcās in tentātiōnem.</i> (Mateus 6,13; <i>indūcō, -ere</i>, conduzir, induzir; <i>tentātiō, -ōnis</i>, tentação)', '<i>Indūcās</i>: presente do subjuntivo (3ª conj., + <i>a</i>), 2ª sing., com <i>nē</i>: proibição (ou súplica negativa) com o presente, uso da Vulgata e da poesia; a prosa clássica preferiria <i>nē indūxerīs</i>. "E não nos induzas à tentação."'),
            ('<i>Falsus utinam vātēs sim!</i> (Tito Lívio 21.10.10, citado por A&amp;G § 442; <i>falsus</i>, falso; <i>vātēs, -is</i>, profeta)', '<i>Sim</i>: presente do subjuntivo de <i>sum</i>, com <i>utinam</i>: optativo de desejo possível. <i>Falsus vātēs</i> é predicativo. "Oxalá eu seja um falso profeta!"'),
        ]),
        exercicio('Exercício 6 · Do português para o latim', 'Traduza usando o subjuntivo. Vocabulário: <i>legō, -ere</i>, ler; <i>liber, librī</i>, livro; <i>scrībō, -ere, scrīpsī</i>, escrever; <i>epistula, -ae</i>, carta; <i>maneō, -ēre, mānsī</i>, ficar; <i>hīc</i>, aqui; <i>an</i>, ou (em pergunta).', [
            ('Leiamos os livros.', '<i>Legāmus librōs.</i> Exortativo: 1ª pl. do presente do subjuntivo de <i>legō</i> (3ª: + <i>a</i>).'),
            ('Que os meninos escrevam cartas.', '<i>Puerī epistulās scrībant.</i> Jussivo: 3ª pl. do presente do subjuntivo.'),
            ('Não escrevas a carta!', '<i>Nē epistulam scrīpserīs!</i> Proibição: <i>nē</i> + perfeito do subjuntivo (tema <i>scrīps-</i> + <i>-erīs</i>). Também correto: <i>Nōlī epistulam scrībere!</i>'),
            ('Quem dera eu tivesse ficado aqui!', '<i>Utinam hīc mānsissem!</i> Optativo com mais-que-perfeito: desejo irrealizável no passado (<i>maneō, mānsī</i>).'),
            ('Devo ficar ou ir? (literalmente: fique eu ou vá?)', '<i>Maneam an eam?</i> Deliberativo: presente do subjuntivo de <i>maneō</i> (2ª: <i>mane-am</i>) e de <i>eō</i> (<i>eam</i>); <i>an</i>, "ou", introduz a segunda alternativa de uma pergunta dupla.'),
        ]),
    ],
    leituras=['vulgata-biblia-sacra-vulgata-editio-clementina', 'catullus-catulli-carmina', 'd-ooge-latin-for-beginners', 'lhomond-epitome-historiae-sacrae', 'bennett-new-latin-grammar', 'greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc'],
    leituras_nota='Na Vulgata, leia Gênesis 1 inteiro, contando os subjuntivos jussivos (Fīat, Congregentur, Germinet, Producant), e o Pai-Nosso de Mateus 6,9–13. O poema 5 de Catulo (Vīvāmus, mea Lesbia, atque amēmus) é um exercício de exortativos; leia-o com uma edição anotada quando chegar ao capítulo 45. Latin for Beginners, de D\'Ooge, traz a flexão do subjuntivo nas lições LXI, LXIII e LXIV, com exercícios graduados. O Epitome Historiae Sacrae, de Lhomond, permite ver o subjuntivo em narrativa simples. Para consulta, Bennett §§ 272–280 e Allen & Greenough §§ 438–450 reúnem todos os usos independentes.',
)
