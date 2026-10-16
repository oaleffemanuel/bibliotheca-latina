from conteudo.util import (tabela, tabela_conjugacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='23-a-voz-passiva-infectum', titulo='A voz passiva nos tempos do infectum', titulo_latim='Dē vōce passīvā', tempo='70 min',
    resumo='Quando o sujeito sofre a ação: as terminações passivas (-r, -ris, -tur, -mur, -minī, -ntur), o presente, o imperfeito e o futuro passivos das quatro conjugações e dos verbos em -iō, o infinitivo presente passivo (-rī, -ī), o agente com ā/ab e o meio no ablativo simples, a passagem da ativa para a passiva e as armadilhas amāris/amāberis e regeris/regēris.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['voz passiva', 'infectum e perfectum', 'terminações passivas', 'presente passivo', 'imperfeito passivo', 'futuro passivo', 'verbos em -iō na passiva',
             '2ª pessoa em -ris e -re', 'amāris × amāberis', 'regeris × regēris', 'infinitivo presente passivo', 'agente da passiva (ā/ab + ablativo)',
             'ablativo de meio', 'per + acusativo', 'ativa ↔ passiva', 'sentido reflexivo da passiva', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulos 13 e 21: os tempos do indicativo ativo e as partes principais (13) e os usos do ablativo, em especial o de meio (21). O capítulo 22 (sujeito, objeto, predicativo, verbos transitivos e intransitivos) é a base da passagem da ativa para a passiva.',
                       licoes=['13-o-perfeito-e-as-partes-principais', '21-usos-do-acusativo-e-do-ablativo', '22-imperativo-e-oracao-simples']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 94 (as duas vozes), § 96 (terminações pessoais passivas: -r, -ris/-re, -tur, -mur, -minī, -ntur), § 97 (tempos formados do tema do presente, ativos e passivos), § 102 (amor: presente, imperfeito e futuro passivos; infinitivo amārī; nota 38, o imperativo passivo só se usa nos depoentes), §§ 104, 106, 108, 111 (moneor, regor, audior, capior), § 116.4.a (infinitivo arcaico em -ier), § 216 (ablativo de agente com ā/ab; 216.1 coletivos e personificados; 216.2 animais), § 218 (ablativo de meio), § 256.1 (resto do sentido médio ou reflexivo)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 154.a (duas vozes), § 156.a (passiva com sentido reflexivo: Turnus vertitur), § 163 (terminações pessoais, ativas e passivas; nota 2, a passiva como antiga voz média), §§ 165–167 (terminações verbais; § 167, vogal longa abreviada antes de -r, -t, -nt, -ntur), § 168 (tempos do sistema do presente), § 176.b (na 3ª conjugação a vogal temática aparece como i, mas e se conserva em tegeris, tegere), § 183 (infinitivo passivo arcaico em -ier), § 405 (ablativo de agente com ā/ab; nota 2, agente × instrumento; 405.b, per + acusativo), § 409 (ablativo de meio)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 108 (voz ativa e passiva), § 113 (2ª sing. passiva em -ris ou -re; no presente do indicativo, -re é raro), § 110 (só os verbos transitivos têm a passiva completa), § 112 (formas básicas da passiva: amor, amārī), §§ 120–123 (paradigmas passivos das quatro conjugações), §§ 239–240 (agente com a/ab; instrumento sem preposição), §§ 296–298 (passagem da ativa para a passiva; verbos factitivos tornam-se copulativos), § 302 (intransitivos com dativo conservam o dativo na passiva)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 80 (as vozes; transitivos e intransitivos; a voz reflexa portuguesa vertida pela passiva latina), n. 89 (regra A: formação da passiva do presente, imperfeito e futuro; desinências das quatro conjugações; verbos em -iō, caperis), n. 92 (infinitivo presente passivo: -rī, e -ī na 3ª), e a regra da "Aplicação prática" após o n. 17 (agente com a/ab se for pessoa; sem preposição se for coisa)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Mateus 14,24; Lucas 5,20, 6,37–38 e 6,44', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', nota='frases autênticas das seções 1, 5 e 6, conferidas na Wikisource latina (Vulgata Clementina, Evangelium secundum Matthaeum e secundum Lucam); grafia normalizada (ae por æ, i por j) e macrons acrescentados por este livro', tipo='dominio_publico'),
    ],
    objetivos=[
        'Explicar o que muda numa oração quando o verbo passa da voz ativa para a passiva, e por que só os verbos transitivos têm passiva pessoal completa.',
        'Conjugar e reconhecer o presente, o imperfeito e o futuro passivos de <i>amō, moneō, regō, audiō</i> e <i>capiō</i>, inclusive a 2ª pessoa em <i>-re</i>.',
        'Distinguir pela forma e pela quantidade as armadilhas <i>amāris</i> (presente) / <i>amāberis</i> (futuro) e <i>regeris</i> (presente) / <i>regēris</i> (futuro).',
        'Formar o infinitivo presente passivo (<i>amārī, monērī, regī, audīrī, capī</i>) e não confundi-lo com o ativo.',
        'Exprimir o agente (<i>ā/ab</i> + ablativo) e o meio (ablativo simples), e transformar frases da ativa para a passiva e vice-versa.',
    ],
    secoes=[
        ('O que é a voz passiva', f'''
<p>Compare "o mestre elogia o aluno" com "o aluno é elogiado pelo mestre". O fato é o mesmo; muda o ponto de vista. Na primeira frase o sujeito <b>pratica</b> a ação: é a voz <b>ativa</b>. Na segunda o sujeito <b>sofre</b> a ação: é a voz <b>passiva</b> (Bennett § 94; Kennedy § 108; Ravizza n. 80). Quem praticou a ação continua na frase, se o falante quiser, como <b>agente da passiva</b> ("pelo mestre").</p>
{exemplos([('Magister discipulum <b>laudat</b>.', 'O mestre elogia o aluno. (ativa)'), ('Discipulus ā magistrō <b>laudātur</b>.', 'O aluno é elogiado pelo mestre. (passiva)')])}
<p>O português forma a passiva com duas palavras, o verbo "ser" e o particípio ("é elogiado"). O latim, nos tempos que este capítulo estuda, faz tudo numa palavra só, trocando as terminações pessoais: <i>laudat</i> → <i>laudātur</i>. É como se o verbo latino tivesse dois jogos de terminações, um para quando o sujeito age e outro para quando o sujeito sofre. O português também tem uma passiva de uma palavra só, a <b>passiva com "se"</b>: "vende-se a casa", "elogia-se o aluno". Muitas vezes ela é a melhor tradução de uma passiva latina sem agente.</p>
<h3>Infectum e perfectum</h3>
<p>No capítulo 13 você viu que o verbo latino tem dois grandes conjuntos de tempos. Os do <b>infectum</b> (ação vista em curso, "não acabada") são o presente, o imperfeito e o futuro, formados com o tema do presente (<i>ama-</i>, <i>rege-</i>). Os do <b>perfectum</b> (ação acabada) são o perfeito, o mais-que-perfeito e o futuro perfeito, formados com o tema do perfeito (<i>amāv-</i>, <i>rēx-</i>) (Bennett § 97). A divisão é importante aqui, porque a passiva se forma de modo diferente nos dois grupos: no infectum, com terminações próprias, numa só palavra (este capítulo); no perfectum, com o particípio e o verbo <i>esse</i>, como em português (capítulo 24).</p>
<h3>Quem pode ir para a passiva</h3>
<p>Só um verbo que tem objeto direto pode transformá-lo em sujeito. Por isso só os verbos <b>transitivos</b> têm a passiva completa, em todas as pessoas (Kennedy § 110; Ravizza n. 80). <i>Laudō</i> tem passiva pessoal (<i>laudor</i>, "sou elogiado"); <i>currō</i>, "corro", não tem um *"sou corrido". Os intransitivos aparecem na passiva só na 3ª pessoa do singular, sem sujeito, numa construção impessoal que é assunto do capítulo 24 (<i>curritur</i>, "corre-se").</p>
{observacao('A passiva com sentido reflexivo', 'A passiva latina descende de uma antiga voz <b>média</b>, em que o sujeito age sobre si mesmo ou em seu próprio interesse (A&amp;G § 163, nota 2). Restos desse sentido continuam vivos: <i>Turnus vertitur</i>, "Turno vira-se" (A&amp;G § 156.a); <i>lavor</i>, "lavo-me". O Pe. Ravizza observa que a "voz reflexa" portuguesa ("eu me exercito") se traduz muitas vezes pela passiva latina (<i>exerceor</i>) (n. 80). Se a tradução "sou X-ado" soar estranha, experimente "X-o-me".')}
'''),
        ('As terminações passivas e o presente', f'''
<p>A passiva do infectum usa as mesmas formas da ativa até a terminação pessoal; só a terminação muda (Bennett § 96). O Pe. Ravizza resume a regra assim: <b>onde a ativa termina em <i>-ō</i>, acrescenta-se <i>-r</i>; onde termina em <i>-m</i>, troca-se o <i>-m</i> por <i>-r</i></b>; as outras pessoas trocam a terminação ativa pela passiva correspondente (n. 89).</p>
{tabela(['Pessoa', 'Ativa', 'Passiva', 'Exemplo ativo → passivo'], [
    ['1ª sing.', '-ō / -m', '<b>-r</b> (-or / -ar)', 'amō → amo<b>r</b> · amābam → amāba<b>r</b>'],
    ['2ª sing.', '-s', '<b>-ris</b> ou <b>-re</b>', 'amās → amā<b>ris</b>'],
    ['3ª sing.', '-t', '<b>-tur</b>', 'amat → amā<b>tur</b>'],
    ['1ª pl.', '-mus', '<b>-mur</b>', 'amāmus → amā<b>mur</b>'],
    ['2ª pl.', '-tis', '<b>-minī</b>', 'amātis → amā<b>minī</b>'],
    ['3ª pl.', '-nt', '<b>-ntur</b>', 'amant → aman<b>tur</b>'],
], 'Terminações pessoais: ativa e passiva')}
<p>Três detalhes. A 2ª pessoa do plural, <i>-minī</i>, não se parece com nenhuma outra terminação: é provavelmente um resto de uma forma de particípio (A&amp;G § 163, nota 1), e por isso precisa ser decorada à parte. A 2ª pessoa do singular tem duas formas, <i>-ris</i> e <i>-re</i>; os paradigmas de Bennett registram a forma em <i>-re</i> no imperfeito e no futuro (<i>amābāris</i> ou <i>amābāre</i>; <i>amāberis</i> ou <i>amābere</i>, § 102), e Kennedy (§ 113) observa que no presente do indicativo a forma em <i>-re</i> é rara. E as vogais longas se abreviam antes de <i>-r</i> final e de <i>-ntur</i>, como antes de <i>-t</i> e <i>-nt</i> na ativa (A&amp;G § 167): <i>amor</i>, <i>amantur</i>, <i>monentur</i>; mas <i>amātur</i>, <i>monētur</i>, <i>audītur</i> conservam a longa antes de <i>-tur</i>.</p>
<h3>O presente passivo</h3>
<p>Aplicando as terminações ao tema do presente, temos o presente passivo das quatro conjugações (Bennett §§ 102, 104, 106, 108, 111; Kennedy §§ 120–123):</p>
{tabela(['Pessoa', '1ª · amor', '2ª · moneor', '3ª · regor', '4ª · audior', '3ª em -iō · capior'], [
    ['1ª sing.', 'am<b>or</b>', 'mone<b>or</b>', 'reg<b>or</b>', 'audi<b>or</b>', 'capi<b>or</b>'],
    ['2ª sing.', 'amā<b>ris</b>', 'monē<b>ris</b>', 'reg<b>eris</b>', 'audī<b>ris</b>', 'cap<b>eris</b>'],
    ['3ª sing.', 'amā<b>tur</b>', 'monē<b>tur</b>', 'reg<b>itur</b>', 'audī<b>tur</b>', 'cap<b>itur</b>'],
    ['1ª pl.', 'amā<b>mur</b>', 'monē<b>mur</b>', 'reg<b>imur</b>', 'audī<b>mur</b>', 'cap<b>imur</b>'],
    ['2ª pl.', 'amā<b>minī</b>', 'monē<b>minī</b>', 'reg<b>iminī</b>', 'audī<b>minī</b>', 'cap<b>iminī</b>'],
    ['3ª pl.', 'aman<b>tur</b>', 'monen<b>tur</b>', 'reg<b>untur</b>', 'audi<b>untur</b>', 'capi<b>untur</b>'],
], 'Presente do indicativo passivo', latim_cols=(1, 2, 3, 4, 5))}
<p>A tradução é "sou amado", "és aconselhado", "é governado"; e, como o presente latino também descreve a ação em curso, "estou sendo amado" (Kennedy § 120: <i>I am or I am being loved</i>). A única forma que foge do esperado é a <b>2ª pessoa do singular da 3ª conjugação</b>: <i>regeris</i> e <i>caperis</i>, com <i>e</i>, e não *<i>regiris</i>, *<i>capiris</i>. A vogal breve do tema, que no resto do presente aparece como <i>i</i> (<i>regitur, regimur</i>), conserva diante do <i>r</i> a forma <i>e</i>, como no infinitivo <i>regere</i> (A&amp;G § 176.b: <i>tegeris, tegere</i>). Ravizza chama a atenção para o caso dos verbos em <i>-iō</i>: <i>cap-eris</i>, e não *<i>capiēris</i> (n. 89). Guarde <i>regeris</i>: na seção seguinte ele terá um gêmeo traiçoeiro.</p>
{exemplos([('Epistula ā Mārcō <b>scrībitur</b>.', 'A carta é escrita (está sendo escrita) por Marco.'), ('Ā magistrō <b>monēminī</b>, puerī.', 'Vós sois advertidos pelo mestre, meninos.'), ('Vōx tua nōn <b>audītur</b>.', 'A tua voz não é ouvida (não se ouve).'), ('In hōc oppidō multī librī <b>vēnduntur</b>.', 'Nesta cidade vendem-se muitos livros. (<i>vēndō, -ere</i>, vender)')])}
'''),
        ('O imperfeito e o futuro passivos; as duas armadilhas', f'''
<p>O <b>imperfeito</b> passivo não traz surpresas: ao sinal <i>-bā-</i> do imperfeito ativo (capítulo 12) juntam-se as terminações passivas. O singular faz <i>-bar, -bāris (-bāre), -bātur</i>, e o plural <i>-bāmur, -bāminī, -bantur</i>. Traduz-se por "era amado", "estava sendo amado".</p>
{tabela(['Pessoa', 'amō', 'moneō', 'regō', 'audiō', 'capiō'], [
    ['1ª sing.', 'amā<b>bar</b>', 'monē<b>bar</b>', 'regē<b>bar</b>', 'audiē<b>bar</b>', 'capiē<b>bar</b>'],
    ['2ª sing.', 'amā<b>bāris</b> (-bāre)', 'monē<b>bāris</b>', 'regē<b>bāris</b>', 'audiē<b>bāris</b>', 'capiē<b>bāris</b>'],
    ['3ª sing.', 'amā<b>bātur</b>', 'monē<b>bātur</b>', 'regē<b>bātur</b>', 'audiē<b>bātur</b>', 'capiē<b>bātur</b>'],
    ['1ª pl.', 'amā<b>bāmur</b>', 'monē<b>bāmur</b>', 'regē<b>bāmur</b>', 'audiē<b>bāmur</b>', 'capiē<b>bāmur</b>'],
    ['2ª pl.', 'amā<b>bāminī</b>', 'monē<b>bāminī</b>', 'regē<b>bāminī</b>', 'audiē<b>bāminī</b>', 'capiē<b>bāminī</b>'],
    ['3ª pl.', 'amā<b>bantur</b>', 'monē<b>bantur</b>', 'regē<b>bantur</b>', 'audiē<b>bantur</b>', 'capiē<b>bantur</b>'],
], 'Imperfeito do indicativo passivo', latim_cols=(1, 2, 3, 4, 5))}
<p>O <b>futuro</b> passivo segue as duas maneiras de fazer o futuro que você aprendeu no capítulo 12. Na 1ª e na 2ª conjugações, o futuro tem o sinal <i>-b-</i>: <i>amābō, amābis, amābit</i>; na passiva, <i>amābor, amāberis (-bere), amābitur, amābimur, amābiminī, amābuntur</i>. Na 3ª e na 4ª, o futuro tem <i>-a-</i> na 1ª pessoa e <i>-ē-</i> nas outras: <i>regam, regēs, reget</i>; na passiva, <i>regar, regēris (-ēre), regētur, regēmur, regēminī, regentur</i>.</p>
{tabela(['Pessoa', 'amō', 'moneō', 'regō', 'audiō', 'capiō'], [
    ['1ª sing.', 'amā<b>bor</b>', 'monē<b>bor</b>', 'reg<b>ar</b>', 'audi<b>ar</b>', 'capi<b>ar</b>'],
    ['2ª sing.', 'amā<b>beris</b> (-bere)', 'monē<b>beris</b>', 'reg<b>ēris</b> (-ēre)', 'audi<b>ēris</b>', 'capi<b>ēris</b>'],
    ['3ª sing.', 'amā<b>bitur</b>', 'monē<b>bitur</b>', 'reg<b>ētur</b>', 'audi<b>ētur</b>', 'capi<b>ētur</b>'],
    ['1ª pl.', 'amā<b>bimur</b>', 'monē<b>bimur</b>', 'reg<b>ēmur</b>', 'audi<b>ēmur</b>', 'capi<b>ēmur</b>'],
    ['2ª pl.', 'amā<b>biminī</b>', 'monē<b>biminī</b>', 'reg<b>ēminī</b>', 'audi<b>ēminī</b>', 'capi<b>ēminī</b>'],
    ['3ª pl.', 'amā<b>buntur</b>', 'monē<b>buntur</b>', 'reg<b>entur</b>', 'audi<b>entur</b>', 'capi<b>entur</b>'],
], 'Futuro do indicativo passivo', latim_cols=(1, 2, 3, 4, 5))}
<h3>Duas armadilhas</h3>
<p><b>Primeira: <i>amāris</i> e <i>amāberis</i>.</b> Na 1ª e na 2ª conjugações, a 2ª pessoa do singular do futuro passivo não é *<i>amābiris</i>, como faria supor <i>amābis, amābitur</i>, mas <b><i>amāberis</i></b>, com <i>e</i>, pela mesma razão que dá <i>regeris</i>: diante do <i>r</i> a vogal breve aparece como <i>e</i>, e não como <i>i</i>. Assim, <i>amāris</i> é presente ("és amado") e <i>amāberis</i> é futuro ("serás amado"); <i>monēris</i>, presente, e <i>monēberis</i>, futuro. A sílaba <i>-be-</i> é a marca do futuro.</p>
<p><b>Segunda: <i>regeris</i> e <i>regēris</i>.</b> Na 3ª conjugação, o presente <i>regeris</i> ("és governado") e o futuro <i>regēris</i> ("serás governado") se escrevem com as mesmas letras. Só a <b>quantidade</b> do <i>e</i> os distingue: breve no presente, longo no futuro. Com a pronúncia muda também o acento: <i><u>RE</u>-ge-ris</i> no presente, <i>re-<u>GĒ</u>-ris</i> no futuro. O mesmo vale para <i>dūceris / dūcēris</i>, <i>mitteris / mittēris</i>, e para a 2ª pessoa do plural: <i>regiminī</i> (presente) contra <i>regēminī</i> (futuro), aqui com vogais diferentes.</p>
{comparacao('Formas que se parecem', ['Forma', 'Análise', 'Como reconhecer'], [
    ['amāris · amāberis', 'presente · futuro (2ª sing.)', 'o futuro da 1ª e 2ª tem <i>-be-</i>'],
    ['regeris · regēris', 'presente · futuro (2ª sing.)', 'só a quantidade: <i>e</i> breve no presente, <i>ē</i> longo no futuro; num texto sem macrons, o contexto'],
    ['regiminī · regēminī', 'presente · futuro (2ª pl.)', '<i>-i-</i> no presente, <i>-ē-</i> no futuro'],
    ['regitur · regētur', 'presente · futuro (3ª sing.)', '<i>-i-</i> no presente, <i>-ē-</i> no futuro'],
    ['amābere · amāre', 'futuro passivo (2ª sing., forma em -re) · infinitivo ativo', 'o <i>-be-</i> do futuro; e o infinitivo não tem pessoa'],
    ['regēre · regere', 'futuro passivo (2ª sing., forma em -re) · infinitivo ativo', 'outra vez a quantidade do <i>e</i>; o contexto decide'],
])}
{dica('<b>Num texto sem macrons</b>, como a maior parte das edições antigas, <i>regeris</i>/<i>regēris</i> e <i>regere</i>/<i>regēre</i> se distinguem pelo contexto: um advérbio de tempo (<i>crās</i>, "amanhã"; <i>mox</i>, "logo"), outro verbo no futuro na mesma frase, o sentido. É uma boa razão para aprender os paradigmas em voz alta, com a quantidade certa: o ouvido romano não confundia as duas formas.')}
'''),
        ('O infinitivo presente passivo', f'''
<p>O infinitivo ativo termina em <i>-re</i>: <i>amāre, monēre, regere, audīre, capere</i>. O infinitivo presente <b>passivo</b> troca o <i>-re</i> por <b><i>-rī</i></b> na 1ª, 2ª e 4ª conjugações, e, na 3ª, troca o <i>-ere</i> inteiro por <b><i>-ī</i></b> (Bennett §§ 102, 106, 111; Ravizza n. 92):</p>
{tabela(['Conjugação', 'Infinitivo ativo', 'Infinitivo passivo', 'Tradução'], [
    ['1ª', 'amā<b>re</b>', 'amā<b>rī</b>', 'ser amado'],
    ['2ª', 'monē<b>re</b>', 'monē<b>rī</b>', 'ser aconselhado'],
    ['3ª', 'reg<b>ere</b>', 'reg<b>ī</b>', 'ser governado'],
    ['4ª', 'audī<b>re</b>', 'audī<b>rī</b>', 'ser ouvido'],
    ['3ª em -iō', 'cap<b>ere</b>', 'cap<b>ī</b>', 'ser pego, ser tomado'],
], 'Infinitivo presente: ativo e passivo', latim_cols=(1, 2))}
<p>A forma curta da 3ª conjugação é a que mais engana. <i>Regī</i> é "ser governado", e não deve ser confundido com <i>rēgī</i>, dativo de <i>rēx</i>, "ao rei" (com <i>ē</i> longo); <i>dūcī</i> é "ser conduzido", <i>mittī</i> "ser enviado", <i>capī</i> "ser pego". Ao ver uma forma em <i>-ī</i> de um verbo da 3ª, pergunte se ela pode ser infinitivo passivo antes de procurar um caso.</p>
<p>Por ora, use o infinitivo passivo como complemento de verbos que você já conhece e que pedem infinitivo, como <i>dēbeō</i>, "dever", e <i>cupiō</i>, "desejar"; os demais usos ficam para os capítulos 27 e 28.</p>
{exemplos([('Lēgēs <b>servārī</b> dēbent.', 'As leis devem ser observadas.'), ('Puer ā patre <b>laudārī</b> cupit.', 'O menino deseja ser elogiado pelo pai.'), ('Mīlitēs in castra <b>dūcī</b> dēbent.', 'Os soldados devem ser conduzidos ao acampamento.')])}
{observacao('Duas formas que você não vai precisar agora', 'Na poesia e no latim arcaico aparece um infinitivo passivo em <i>-ier</i>: <i>amārier</i>, <i>dīcier</i> por <i>amārī</i>, <i>dīcī</i> (Bennett § 116.4.a; A&amp;G § 183). E existe um imperativo passivo (<i>amāre</i>, "sê amado"; <i>amāminī</i>, "sede amados"), mas, como observa Bennett (§ 102, nota 38), na prática ele só se usa nos verbos depoentes, que têm forma passiva e sentido ativo; você o encontrará no capítulo 25.')}
'''),
        ('O agente e o meio; da ativa para a passiva', f'''
<p>Na passiva, quem pratica a ação pode ser dito de duas maneiras, conforme seja uma <b>pessoa</b> ou uma <b>coisa</b>:</p>
<ul>
<li>O <b>agente pessoal</b> vai para o <b>ablativo com <i>ā</i></b> (só antes de consoante) ou <b><i>ab</i></b> (antes de vogal e de <i>h</i>, e também antes de algumas consoantes): <i>ā Caesare accūsātur</i>, "é acusado por César" (Bennett § 216; A&amp;G § 405; Kennedy § 239).</li>
<li>O <b>meio ou instrumento</b> vai para o <b>ablativo sem preposição</b>, o ablativo de meio do capítulo 21: <i>sagittā vulnerātur</i>, "é ferido por uma flecha" (Bennett § 218; A&amp;G § 409; Kennedy § 240).</li>
</ul>
<p>O português usa "por" nos dois casos ("ferido pelo inimigo", "ferido por uma flecha"); o latim não. A&amp;G (§ 405, nota 2) põe lado a lado <i>occīsus gladiō</i>, "morto pela espada", e <i>occīsus ab hoste</i>, "morto pelo inimigo". A regra prática do Pe. Ravizza diz tudo: o agente vai para o ablativo "com <i>a</i> ou <i>ab</i>, se for pessoa; sem preposição, se for cousa". Há só três nuances. Os nomes coletivos de pessoas (<i>multitūdō</i>, <i>exercitus</i>) e as coisas <b>personificadas</b> podem levar <i>ā/ab</i>: <i>hostēs ā fortūnā dēserēbantur</i>, "os inimigos eram abandonados pela Fortuna" (Bennett § 216.1). Os animais oscilam: às vezes são tratados como agentes, com <i>ab</i>, às vezes como meio (Bennett § 216.2; A&amp;G § 405, nota 2). E uma pessoa usada como intermediária, "por meio de alguém", vai para <i>per</i> + acusativo: <i>per explōrātōrēs</i>, "por meio de batedores" (A&amp;G § 405.b).</p>
{exemplos([('Urbs <b>ā mīlitibus</b> dēfenditur.', 'A cidade é defendida pelos soldados. (agente: pessoas)'), ('Urbs <b>mūrīs</b> dēfenditur.', 'A cidade é defendida pelas muralhas. (meio: coisas)'), ('Urbs <b>ā mīlitibus mūrīs</b> dēfenditur.', 'A cidade é defendida pelos soldados com as muralhas. (os dois juntos)')])}
<h3>Da ativa para a passiva, passo a passo</h3>
<p>Transformar uma frase ativa em passiva é o melhor exercício para dominar as duas vozes. São quatro passos (Kennedy §§ 296–297):</p>
<ol>
<li>O <b>objeto direto</b> da ativa (acusativo) passa a <b>sujeito</b> da passiva (nominativo).</li>
<li>O <b>verbo</b> vai para a passiva no <b>mesmo tempo</b>, concordando em pessoa e número com o novo sujeito.</li>
<li>O <b>sujeito</b> da ativa, se for mantido, vira <b>agente</b>: <i>ā/ab</i> + ablativo se for pessoa, ablativo simples se for coisa.</li>
<li>O resto da frase (dativos, adjuntos) fica como está. Se havia um <b>predicativo do objeto</b> (<i>Rōmulum rēgem appellant</i>, o duplo acusativo dos capítulos 21 e 22), ele acompanha o objeto e passa ao nominativo: <i>Rōmulus rēx appellātur</i>, "Rômulo é chamado rei". O verbo de chamar, eleger ou considerar torna-se então verbo de ligação (Kennedy § 297; Bennett § 168.2.b).</li>
</ol>
{diagrama_frase([('Discipulī', 'nominativo pl. · sujeito (sofre)'), ('ā magistrō', 'ā + ablativo · agente'), ('saepe', 'advérbio · adjunto'), ('laudantur', 'presente passivo · 3ª pl.')], 'A ativa <i>Magister discipulōs saepe laudat</i> (o mestre elogia muitas vezes os alunos) vira <i>Discipulī ā magistrō saepe laudantur</i> = Os alunos são muitas vezes elogiados pelo mestre: o acusativo vira nominativo, o nominativo vira agente, o verbo concorda com o novo sujeito.')}
<p>O caminho inverso, da passiva para a ativa, é o mesmo ao contrário: o agente volta a ser sujeito (nominativo), o sujeito volta a ser objeto (acusativo), o verbo volta à ativa no mesmo tempo, concordando com o novo sujeito. Se a passiva não tem agente, a ativa precisa de um sujeito indeterminado: <i>Librī vēnduntur</i> → "vendem livros", "alguém vende livros". Note que um verbo intransitivo com dativo, como <i>noceō</i>, "prejudicar", conserva o dativo na passiva, que então fica impessoal (Kennedy § 302); essa construção é estudada no capítulo 24.</p>
<p>Não ache que a passiva latina é só um exercício de transformação. Os autores a preferem quando o agente é desconhecido, óbvio ou sem importância, ou quando querem manter o mesmo sujeito numa série de frases. Num relato de batalha, <i>oppidum capitur</i>, "a cidade é tomada", diz o que importa; quem tomou já está claro pelo contexto.</p>
'''),
        ('Leitura: duas passagens dos Evangelhos', f'''
<p>A Vulgata tem passivas do infectum em quase todas as páginas. Comecemos por uma frase curta do Evangelho de Mateus, na cena da tempestade que você leu no capítulo 22:</p>
{exemplos([('Nāvicula autem in mediō marī iactābātur flūctibus.', 'O barco, porém, era sacudido pelas ondas no meio do mar. (Mt 14,24, Vulgata)')])}
<p><i>Iactābātur</i> é imperfeito passivo, 3ª pessoa do singular, de <i>iactō, -āre</i>, "lançar, sacudir": <i>iactā-bā-tur</i>. O imperfeito descreve a ação que durava, "era sacudido, estava sendo sacudido". Quem sacudia? <i>Flūctibus</i>, ablativo plural de <i>flūctus, -ūs</i> (4ª declinação, capítulo 11), "onda", <b>sem preposição</b>: as ondas são coisas, e por isso aparecem como meio, não como agente com <i>ab</i>. Na mesma página, uma passiva do presente com o vocativo do capítulo 22: <i>Homo, remittuntur tibi peccāta tua</i>, "Homem, são-te perdoados os teus pecados" (Lc 5,20), com <i>remittuntur</i> (3ª conj., 3ª pl.) concordando com o sujeito neutro plural <i>peccāta</i>.</p>
<p>A segunda passagem, do Evangelho de Lucas, parece feita para este capítulo. Ela alterna imperativos e futuros passivos:</p>
{exemplos([('Nōlīte iūdicāre, et nōn iūdicābiminī: nōlīte condemnāre, et nōn condemnābiminī. Dīmittite, et dīmittēminī. Date, et dabitur vōbīs.', 'Não julgueis, e não sereis julgados; não condeneis, e não sereis condenados. Perdoai, e sereis perdoados. Dai, e dar-se-vos-á. (Lc 6,37–38, Vulgata)')])}
{analise('Lc 6,37–38, palavra a palavra (formas verbais e pronomes)', [
    ('Nōlīte iūdicāre', 'nōlō + iūdicō, -āre, julgar', '<i>nōlīte</i>: imperativo de <i>nōlō</i>, 2ª pl.; <i>iūdicāre</i>: infinitivo presente ativo', 'proibição (capítulo 22): "não julgueis"'),
    ('et nōn', 'conjunções e advérbio', 'invariáveis', '"e não": liga a promessa à ordem'),
    ('iūdicābiminī', 'iūdicō, -āre (1ª)', 'futuro passivo, 2ª pl.: <i>iūdicā-bi-minī</i>', '"sereis julgados"; sujeito "vós", sem agente expresso'),
    ('condemnābiminī', 'condemnō, -āre (1ª), condenar', 'futuro passivo, 2ª pl.', '"sereis condenados"; mesma estrutura'),
    ('Dīmittite', 'dīmittō, -ere (3ª), soltar, perdoar', 'imperativo presente, 2ª pl. (3ª conj.: <i>-ite</i>)', 'ordem positiva: "perdoai"'),
    ('dīmittēminī', 'dīmittō, -ere (3ª)', 'futuro passivo, 2ª pl.: <i>dīmitt-ē-minī</i>', '"sereis perdoados"; o <i>-ē-</i> é a marca do futuro da 3ª'),
    ('Date', 'dō, dare, dedī, datum, dar', 'imperativo presente, 2ª pl.', '"dai"'),
    ('dabitur', 'dō, dare (1ª; <i>a</i> breve)', 'futuro passivo, 3ª sing.: <i>da-bi-tur</i>', '"será dado"; o sujeito não vem expresso ("algo")'),
    ('vōbīs', 'vōs (pronome pessoal)', 'dativo plural', 'objeto indireto: "a vós"'),
])}
<p>A passagem é um pequeno exercício de reconhecimento. As três promessas da 1ª e da 3ª conjugações mostram as duas maneiras de fazer o futuro: <i>iūdicā-<b>bi</b>-minī</i>, <i>condemnā-<b>bi</b>-minī</i>, com o <i>-b-</i> da 1ª, e <i>dīmitt-<b>ē</b>-minī</i>, com o <i>-ē-</i> da 3ª. E <i>dīmittēminī</i> tem um gêmeo perigoso: <i>dīmittiminī</i>, com <i>-i-</i>, seria o presente, "sois perdoados". Uma só vogal separa a promessa ("sereis") da constatação ("sois"). Repare ainda que nenhuma das passivas tem agente: quem julga, condena e perdoa fica implícito, como é natural numa sentença geral; o português diz o mesmo com "sereis julgados" ou com a passiva com "se".</p>
<p>Para terminar, uma frase do mesmo capítulo de Lucas, um provérbio na passiva do presente: <i>Ūnaquaeque enim arbor dē frūctū suō cognōscitur</i>, "pois cada árvore se conhece (é conhecida) pelo seu fruto" (Lc 6,44). O presente passivo de valor geral, sem agente, pede em português a passiva com "se".</p>
<h3>Resumo</h3>
<ul>
<li><b>Passiva</b>: o sujeito sofre a ação; só os transitivos têm passiva pessoal completa.</li>
<li><b>Terminações</b>: <i>-r, -ris/-re, -tur, -mur, -minī, -ntur</i>, acrescentadas às formas do infectum.</li>
<li><b>Presente</b> <i>amor, moneor, regor (regeris), audior, capior (caperis)</i>; <b>imperfeito</b> <i>-bar</i>; <b>futuro</b> <i>-bor, -beris</i> (1ª, 2ª) e <i>-ar, -ēris</i> (3ª, 4ª).</li>
<li><b>Armadilhas</b>: <i>amāris/amāberis</i>; <i>regeris/regēris</i>; <i>regiminī/regēminī</i>.</li>
<li><b>Infinitivo</b>: <i>amārī, monērī, audīrī</i>; na 3ª, <i>regī, capī</i>.</li>
<li><b>Agente</b>: <i>ā/ab</i> + ablativo (pessoas); <b>meio</b>: ablativo simples (coisas).</li>
</ul>
<p>No capítulo 24 você verá a passiva dos três tempos do perfectum (<i>amātus sum, amātus eram, amātus erō</i>), em que o latim, como o português, usa o particípio com o verbo "ser", e a passiva impessoal dos verbos intransitivos.</p>
'''),
    ],
    erros_comuns=[
        ('Traduzir a passiva como ativa, sem perceber o <i>-r</i> final: <i>laudātur</i> como "elogia".', 'A diferença entre <i>laudat</i> e <i>laudātur</i> é toda a diferença entre agir e sofrer. Antes de traduzir, olhe o fim do verbo: <i>-r, -ris, -tur, -mur, -minī, -ntur</i> indicam passiva. Depois procure o sujeito no nominativo: é ele quem <b>sofre</b>.'),
        ('Ler <i>amāberis</i> ou <i>regēris</i> como presentes, ou <i>regeris</i> como futuro.', '<i>Amāris</i> é presente e <i>amāberis</i> futuro (o <i>-be-</i> marca o futuro da 1ª e 2ª). <i>Regeris</i> (e breve) é presente e <i>regēris</i> (ē longo) futuro: aprenda as formas com a quantidade e, sem macrons, decida pelo contexto.'),
        ('Usar <i>ā/ab</i> com coisas, ou deixar a pessoa sem preposição: *<i>ā gladiō occīsus</i>, *<i>hoste occīsus</i>.', 'Pessoa que age → <i>ā/ab</i> + ablativo (<i>ab hoste</i>); coisa que serve de meio → ablativo simples (<i>gladiō</i>). O "por" do português não decide; pergunte se é alguém ou algo.'),
        ('Deixar o novo sujeito no acusativo ao passar para a passiva: *<i>Discipulōs ā magistrō laudantur</i>.', 'O objeto da ativa vira sujeito da passiva, e sujeito é nominativo: <i>Discipulī ā magistrō laudantur</i>. Confira a concordância: o verbo passivo concorda com o nominativo.'),
        ('Confundir as formas em <i>-re</i> e em <i>-ī</i> com outras palavras: <i>amābere</i> com um infinitivo, <i>regī</i> com o dativo <i>rēgī</i>.', '<i>Amābere</i> (= <i>amāberis</i>) é 2ª pessoa do futuro passivo; o <i>-be-</i> o denuncia. <i>Regī</i> é o infinitivo passivo de <i>regō</i> ("ser governado"); <i>rēgī</i>, com <i>ē</i> longo, é "ao rei". Na 3ª conjugação, toda forma em <i>-ī</i> pode ser infinitivo passivo: teste essa hipótese.'),
        ('Escrever *<i>regiris</i>, *<i>capiris</i> ou *<i>amābiris</i>.', 'Diante do <i>r</i> da terminação <i>-ris</i>, a vogal breve aparece como <i>e</i>, e não como <i>i</i>: <i>regeris</i>, <i>caperis</i>, <i>amāberis</i>. É a mesma vogal que se vê no infinitivo <i>regere</i>.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Da ativa para a passiva',
            'Passe para a passiva e traduza: <i lang="la">Rōmānī urbem mūrīs altīs dēfendēbant.</i> Vocabulário: <i>dēfendō, -ere</i> (3ª), defender; <i>mūrus, -ī</i>, muralha; <i>altus, -a, -um</i>, alto.', [
            ('Qual é o verbo, em que tempo, e quem é o sujeito?', '<i>Dēfendēbant</i>: imperfeito ativo, 3ª pl., de <i>dēfendō</i> (3ª conj.: <i>dēfend-ē-ba-nt</i>). Sujeito: <i>Rōmānī</i>, nominativo plural. "Os romanos defendiam a cidade com altas muralhas."'),
            ('Qual é o objeto direto, e o que ele vira?', '<i>Urbem</i>, acusativo singular de <i>urbs</i>. Na passiva vira o sujeito: <i>urbs</i>, nominativo singular.'),
            ('Ponha o verbo na passiva, no mesmo tempo, concordando com o novo sujeito.', 'Imperfeito passivo, 3ª sing.: <i>dēfendēbātur</i>, "era defendida".'),
            ('O que acontece com <i>Rōmānī</i> e com <i>mūrīs altīs</i>?', '<i>Rōmānī</i> são pessoas: tornam-se agente, <i>ā Rōmānīs</i>. <i>Mūrīs altīs</i> já é ablativo de meio (coisas) e fica como está, sem preposição.'),
            ('Monte a frase e traduza.', '<i>Urbs ā Rōmānīs mūrīs altīs dēfendēbātur.</i> "A cidade era defendida pelos romanos com altas muralhas."'),
        ]),
        pratica_guiada('Prática guiada 2 · Presente ou futuro?',
            'Analise as formas destacadas, decidindo entre presente e futuro, e traduza. Vocabulário: <i>crās</i>, amanhã; <i>nunc</i>, agora; <i>mittō, -ere</i> (3ª), enviar; <i>vocō, -āre</i>, chamar; <i>ad</i> + acusativo, para.', [
            ('<i lang="la">Crās, Mārce, ad rēgem <b>mittēris</b>.</i>', 'Futuro passivo, 2ª sing., da 3ª conjugação: <i>mitt-ē-ris</i>, com <i>ē</i> longo; o advérbio <i>crās</i> confirma. "Amanhã, Marco, serás enviado ao rei."'),
            ('<i lang="la">Nunc, Mārce, ad rēgem <b>mitteris</b>.</i>', 'Presente passivo, 2ª sing.: <i>mitt-e-ris</i>, com <i>e</i> breve (como <i>regeris</i>); <i>nunc</i> confirma. "Agora, Marco, és enviado (estás sendo enviado) ao rei."'),
            ('<i lang="la">Ā magistrō <b>vocāberis</b>.</i>', 'Futuro passivo, 2ª sing., da 1ª conjugação: <i>vocā-be-ris</i>. O presente seria <i>vocāris</i>. "Serás chamado pelo mestre."'),
            ('<i lang="la">Ā magistrō <b>vocāminī</b>, puerī.</i>', 'Presente passivo, 2ª pl.: <i>vocā-minī</i>. O futuro seria <i>vocābiminī</i>. "Sois chamados pelo mestre, meninos."'),
        ], 'Nas conjugações em <i>-b-</i> (1ª e 2ª), o futuro se denuncia pelo <i>-b-</i>; na 3ª, pela vogal <i>ē</i>, que muitas vezes só a quantidade ou o contexto revelam.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Analise a forma', 'Dê o tempo (presente, imperfeito ou futuro), a pessoa e o número, e traduza. Todos os verbos já foram vistos: <i>laudō</i> (1ª), <i>moneō</i> (2ª), <i>regō, dūcō, mittō</i> (3ª), <i>audiō</i> (4ª), <i>capiō</i> (3ª em <i>-iō</i>).', [
            ('<i>laudāris</i>', 'Presente, 2ª sing.: "és elogiado". O futuro seria <i>laudāberis</i>.'),
            ('<i>laudāberis</i>', 'Futuro, 2ª sing.: "serás elogiado". O <i>-be-</i> é a marca do futuro da 1ª conjugação.'),
            ('<i>regeris</i> e <i>regēris</i>', '<i>Regeris</i> (e breve): presente, 2ª sing., "és governado". <i>Regēris</i> (ē longo): futuro, 2ª sing., "serás governado".'),
            ('<i>audiēbantur</i>', 'Imperfeito, 3ª pl.: "eram ouvidos". <i>Audi-ē-ba-ntur</i>, com o <i>-iē-</i> da 4ª no imperfeito.'),
            ('<i>capiētur</i>', 'Futuro, 3ª sing.: "será pego (tomado)". Verbo em <i>-iō</i>: futuro como <i>audiētur</i>.'),
            ('<i>monēminī</i>', 'Presente, 2ª pl.: "sois advertidos". O futuro seria <i>monēbiminī</i>.'),
            ('<i>dūcuntur</i>', 'Presente, 3ª pl.: "são conduzidos". O futuro seria <i>dūcentur</i>, o imperfeito <i>dūcēbantur</i>.'),
            ('<i>mittar</i>', 'Futuro, 1ª sing.: "serei enviado". Na 3ª conjugação, a 1ª pessoa do futuro tem <i>-a-</i>: <i>mitt-a-r</i>.'),
        ]),
        exercicio('Exercício 2 · Conjugue', 'Conjugue nas seis pessoas e traduza a primeira e a última.', [
            ('<i>vocō</i>, presente passivo', '<i>vocor, vocāris, vocātur, vocāmur, vocāminī, vocantur</i>. "Sou chamado" … "são chamados".'),
            ('<i>videō</i>, imperfeito passivo', '<i>vidēbar, vidēbāris (-bāre), vidēbātur, vidēbāmur, vidēbāminī, vidēbantur</i>. "Era visto" … "eram vistos". (No capítulo 22 você viu que <i>videor</i> também significa "pareço".)'),
            ('<i>mittō</i>, futuro passivo', '<i>mittar, mittēris (-ēre), mittētur, mittēmur, mittēminī, mittentur</i>. "Serei enviado" … "serão enviados".'),
            ('<i>capiō</i>, presente passivo', '<i>capior, caperis, capitur, capimur, capiminī, capiuntur</i>. "Sou pego" … "são pegos". Note <i>caperis</i>, sem <i>i</i>, e <i>capiuntur</i>, com <i>i</i>, como <i>audiuntur</i>.'),
        ]),
        exercicio('Exercício 3 · Da ativa para a passiva', 'Passe para a passiva, mantendo o tempo, e traduza. Decida entre <i>ā/ab</i> + ablativo e ablativo simples. Vocabulário: <i>vincō, -ere</i>, vencer; <i>terreō, -ēre</i>, aterrorizar; <i>tempestās, -ātis</i> (f.), tempestade; <i>nauta</i>, marinheiro; <i>necō, -āre</i>, matar; <i>sagitta</i>, flecha; <i>hostis, -is</i>, inimigo.', [
            ('<i>Caesar Gallōs vincit.</i>', '<i>Gallī ā Caesare vincuntur.</i> "Os gauleses são vencidos por César." <i>Gallōs</i> vira <i>Gallī</i>; o verbo passa a 3ª pl.; César é pessoa: <i>ā Caesare</i>.'),
            ('<i>Tempestās nautās terrēbat.</i>', '<i>Nautae tempestāte terrēbantur.</i> "Os marinheiros eram aterrorizados pela tempestade." A tempestade é coisa: ablativo simples, sem <i>ā</i>.'),
            ('<i>Hostēs mīlitem sagittīs necābunt.</i>', '<i>Mīles ab hostibus sagittīs necābitur.</i> "O soldado será morto pelos inimigos com flechas." Futuro passivo, 3ª sing.; <i>ab</i> diante de vogal (<i>hostibus</i>); <i>sagittīs</i> continua como meio.'),
            ('<i>Puerī vōcem magistrī audiunt.</i>', '<i>Vōx magistrī ā puerīs audītur.</i> "A voz do mestre é ouvida pelos meninos." O genitivo <i>magistrī</i> acompanha o seu nome e não muda.'),
            ('<i>Populus Numam rēgem creat.</i>', '<i>Numa ā populō rēx creātur.</i> "Numa é eleito rei pelo povo." O predicativo do objeto (<i>rēgem</i>) passa ao nominativo junto com o objeto: <i>rēx</i> (Kennedy § 297).'),
        ]),
        exercicio('Exercício 4 · Da passiva para a ativa', 'Passe para a ativa, mantendo o tempo, e traduza. Se não houver agente, use um sujeito indeterminado.', [
            ('<i>Epistula ā Iūliā scrībētur.</i>', '<i>Iūlia epistulam scrībet.</i> "Júlia escreverá a carta." O agente <i>ā Iūliā</i> volta a ser sujeito (nominativo); <i>epistula</i> vira objeto (acusativo); futuro ativo, 3ª sing.'),
            ('<i>Ā servīs aqua portābātur.</i>', '<i>Servī aquam portābant.</i> "Os escravos carregavam água." Imperfeito ativo, 3ª pl., concordando com <i>servī</i>.'),
            ('<i>Lēgēs ā cīvibus nōn servantur.</i>', '<i>Cīvēs lēgēs nōn servant.</i> "Os cidadãos não observam as leis." Note que <i>lēgēs</i> tem a mesma forma no nominativo e no acusativo plural: só a construção mostra a mudança de função.'),
            ('<i>In forō multa dīcuntur.</i>', 'Sem agente: <i>In forō multa dīcunt.</i> "No fórum dizem muitas coisas" (sujeito indeterminado, "eles", "as pessoas"). Em português, também "dizem-se muitas coisas no fórum".'),
        ]),
        exercicio('Exercício 5 · Leitura e tradução', 'Traduza, identificando cada passiva e dizendo se a palavra no ablativo é agente ou meio. Vocabulário: <i>exercitus, -ūs</i>, exército; <i>dux, ducis</i>, comandante; <i>flūmen, -inis</i>, rio; <i>prohibeō, -ēre</i>, impedir, deter; <i>lupus</i>, lobo; <i>ovis, -is</i>, ovelha; <i>pāstor, -ōris</i>, pastor; <i>custōdiō, -īre</i>, guardar.', [
            ('<i>Exercitus ā duce in Galliam dūcēbātur.</i>', '"O exército era conduzido pelo comandante para a Gália." <i>Dūcēbātur</i>: imperfeito passivo; <i>ā duce</i>: agente (pessoa).'),
            ('<i>Hostēs flūmine prohibentur.</i>', '"Os inimigos são detidos pelo rio." <i>Prohibentur</i>: presente passivo, 3ª pl.; <i>flūmine</i>: meio (coisa), sem preposição.'),
            ('<i>Ovēs ā pāstōre custōdiuntur, sed ā lupīs capientur.</i>', '"As ovelhas são guardadas pelo pastor, mas serão apanhadas pelos lobos." <i>Custōdiuntur</i>: presente (4ª); <i>capientur</i>: futuro (verbo em <i>-iō</i>). <i>Ā lupīs</i>: os animais tratados como agentes, com <i>ā</i> (Bennett § 216.2).'),
            ('<i>Puer ā mātre vocārī nōn vult.</i> (<i>vult</i>, quer)', '"O menino não quer ser chamado pela mãe." <i>Vocārī</i>: infinitivo presente passivo, complemento de <i>vult</i>; <i>ā mātre</i>: agente.'),
        ]),
        exercicio('Exercício 6 · Retroversão', 'Passe para o latim. Vocabulário: <i>liber, librī</i>, livro; <i>legō, -ere</i>, ler; <i>discipulus</i>, aluno; <i>terreō, -ēre</i>, assustar; <i>clāmor, -ōris</i>, grito; <i>porta</i>, porta; <i>aperiō, -īre</i>, abrir.', [
            ('O livro é lido pelos alunos.', '<i>Liber ā discipulīs legitur.</i> Presente passivo, 3ª sing., da 3ª conjugação: <i>leg-i-tur</i>; agente pessoal com <i>ā</i>.'),
            ('As meninas eram assustadas pelos gritos.', '<i>Puellae clāmōribus terrēbantur.</i> Imperfeito passivo, 3ª pl.; os gritos são coisa: ablativo simples.'),
            ('A porta será aberta amanhã.', '<i>Porta crās aperiētur.</i> Futuro passivo, 3ª sing., da 4ª conjugação: <i>aperi-ē-tur</i>.'),
            ('Serás ouvido, Marco.', '<i>Audiēris, Mārce.</i> Futuro passivo, 2ª sing., da 4ª: <i>audi-ē-ris</i> (ou <i>audiēre</i>). O presente seria <i>audīris</i>.'),
        ]),
    ],
    leituras=['d-ooge-latin-for-beginners', 'kirtland-ritchie-s-fabulae-faciles', 'lhomond-epitome-historiae-sacrae', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'bennett-new-latin-grammar'],
    leituras_nota='Latin for Beginners, de D\'Ooge, traz lições e exercícios graduados sobre a passiva dos tempos do presente, úteis para fixar os paradigmas. As Fabulae Faciles (Perseu, Hércules, Jasão, Ulisses) e o Epitome Historiae Sacrae de Lhomond narram em frases curtas, com muitas passivas do tipo "era levado", "foi morto"; leia procurando o sujeito de cada passiva e perguntando se há agente. Em Familia Romana, quando a passiva aparecer, compare cada frase passiva com a ativa correspondente, como na seção 5. Na Vulgata, leia Lucas 6,27–45, de onde vêm as frases da seção 6. Para os paradigmas completos, Bennett §§ 102–111.',
)
