from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Textos: Catulo 5 e 85 segundo E. T. Merrill (Boston, Ginn, 1893); Horácio, Odes I,11 segundo P. Shorey e G. J. Laing
# (Chicago, Sanborn, 1919); ambos na Perseus Digital Library (canonical-latinLit). Macrons acrescentados por nós.

def _poema(versos, traducao, inicio=1):
    linhas = []
    for i, v in enumerate(versos):
        n = inicio + i
        linhas.append(v + (f' <small>({n})</small>' if n % 5 == 0 else ''))
    return exemplos([('<br>'.join(linhas), traducao)])

CATULO_5 = [
    'Vīvāmus, mea Lesbia, atque amēmus,',
    'rūmōrēsque senum sevēriōrum',
    'omnēs ūnius aestimēmus assis.',
    'sōlēs occidere et redīre possunt:',
    'nōbīs, cum semel occidit brevis lūx,',
    'nox est perpetua ūna dormienda.',
    'dā mī bāsia mīlle, deinde centum,',
    'dein mīlle altera, dein secunda centum,',
    'deinde usque altera mīlle, deinde centum,',
    'dein, cum mīlia multa fēcerīmus,',
    'conturbābimus illa, nē sciāmus,',
    'aut nē quis malus invidēre possit,',
    'cum tantum sciat esse bāsiōrum.',
]
CATULO_5_PT = ('Vivamos, minha Lésbia, e amemos, / e os falatórios dos velhos mais severos, / todos eles, avaliemos em um único asse. / '
               'Os sóis podem pôr-se e voltar: / para nós, quando de uma vez se põe a breve luz, / resta dormir uma única noite sem fim. / '
               'Dá-me mil beijos, depois cem, / depois outros mil, depois mais cem, / depois, sem parar, outros mil, depois cem. / '
               'Depois, quando tivermos feito muitos milhares, / vamos embaralhar a conta, para não sabermos quantos são, / '
               'ou para que nenhum malvado possa pôr-nos mau-olhado / quando souber que há tantos beijos. '
               '<small>(Tradução nossa, literal, para acompanhar a leitura.)</small>')

HORACIO_1_11 = [
    'Tū nē quaesierīs, scīre nefās, quem mihi, quem tibi',
    'fīnem dī dederint, Leuconoē, nec Babylōniōs',
    'temptārīs numerōs. ut melius, quidquid erit, patī.',
    'seu plūrīs hiemēs seu tribuit Iuppiter ultimam,',
    'quae nunc oppositīs dēbilitat pūmicibus mare',
    'Tyrrhēnum: sapiās, vīna liquēs et spatiō brevī',
    'spem longam resecēs. dum loquimur, fūgerit invida',
    'aetās: carpe diem quam minimum crēdula posterō.',
]
HORACIO_1_11_PT = ('Não procures saber (saber é proibido) que fim os deuses deram a mim, que fim a ti, / Leucônoe, nem consultes os cálculos / '
                   'babilônicos. Como é melhor suportar o que vier, seja o que for! / Quer Júpiter nos tenha concedido mais invernos, quer este como o último, / '
                   'este que agora cansa o mar Tirreno contra os rochedos que se lhe opõem: / sê sensata, coa o vinho e, sendo breve o espaço, / '
                   'corta a esperança longa. Enquanto falamos, terá fugido o tempo / invejoso: colhe o dia, confiando o menos possível no amanhã. '
                   '<small>(Tradução nossa, literal; as barras marcam o fim dos versos latinos.)</small>')

LICAO = dict(
    slug='45-catulo-e-horacio', titulo='Catulo e Horácio: dois poemas líricos',
    titulo_latim='Catullus et Horātius', tempo='90 min',
    resumo='Leitura comentada de dois poemas líricos completos: o poema 5 de Catulo (Vīvāmus, mea Lesbia), em hendecassílabos, e a ode I,11 de Horácio (carpe diem), em asclepiadeus maiores. Texto em edição de domínio público, vocabulário, notas verso a verso, escansão em tabelas, o subjuntivo exortativo, jussivo e proibitivo em ação, figuras de linguagem, análise palavra a palavra e tradução própria.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['Catulo', 'Horácio', 'poesia lírica', 'Catulo 5 (Vīvāmus, mea Lesbia)', 'Catulo 85 (Ōdī et amō)', 'Odes I,11 (carpe diem)',
             'hendecassílabo falécio', 'dístico elegíaco', 'asclepiadeu maior', 'estrofe sáfica (menção)', 'escansão', 'elisão', 'sinizese',
             'subjuntivo exortativo', 'subjuntivo jussivo na 2ª pessoa', 'proibição com nē + perfeito do subjuntivo', 'perfeitos sincopados',
             'genitivo de valor', 'hipérbato', 'anáfora', 'antítese', 'leitura comentada', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 32 (o subjuntivo e os seus usos independentes: exortativo, jussivo, proibição) e capítulo 40 (quantidade das sílabas, pés, elisão e escansão; figuras de linguagem). Ajudam também os capítulos 8 (técnica de leitura), 20 (genitivo de valor), 31 (gerundivo) e 33 (orações finais), que este capítulo só relembra.',
                       licoes=['32-o-subjuntivo', '40-metrica-e-figuras', '08-da-frase-ao-paragrafo', '20-usos-do-genitivo-e-do-dativo', '31-gerundio-e-gerundivo', '33-oracoes-finais-e-consecutivas']),
    referencias=[
        referencia('Catullus, ed. Elmer Truesdell Merrill (Boston: Ginn and Company, 1893)', 'Gaius Valerius Catullus', url='https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0003', nota='texto dos poemas 5 e 85 conferido no arquivo TEI da Perseus (canonical-latinLit, phi0472.phi001.perseus-lat2), que declara a edição de Merrill e o metro de cada poema (Phalaecean; Elegiac); comparado com The Latin Library (thelatinlibrary.com/catullus.shtml), que só difere na pontuação. Macrons acrescentados por nós.', tipo='dominio_publico'),
        referencia('Horace, Odes and Epodes, ed. Paul Shorey e Gordon J. Laing (Chicago: Benj. H. Sanborn, 1919)', 'Quintus Horatius Flaccus', url='https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0025', nota='texto da ode I,11 (e do verso I,22,1) conferido no arquivo TEI da Perseus (phi0893.phi001.perseus-lat2), que indica o metro "Fifth (Greater) Asclepiadean"; comparado com The Latin Library (horace/carm1.shtml), que só difere na pontuação. Macrons acrescentados por nós.', tipo='dominio_publico'),
        referencia('Catulli Carmina', 'Gaius Valerius Catullus', catalogo='catullus-catulli-carmina', nota='edição de Robinson Ellis (Oxford, 1904) indicada no catálogo para a leitura dos demais poemas', tipo='dominio_publico'),
        referencia('Carmina et Epodi (Odes e Epodos)', 'Quintus Horatius Flaccus', catalogo='flaccus-carmina-et-epodi-odes-e-epodos', nota='a mesma edição Shorey e Laing, no Project Gutenberg', tipo='dominio_publico'),
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 5 (quantidade das vogais e das sílabas; sílaba longa por posição; sílabas comuns), § 101 (3ª pl. do perfeito em -ēre), § 116.1 (perfeitos sincopados: amārim por amāverim), § 189.1 (dativo de agente com o gerundivo), § 274 (exortativo), § 275 (jussivo; 275.2 na 2ª pessoa: modestē vīvās), § 276 (proibição com nē, presente ou perfeito), § 350.11 (hipérbato, anáfora, quiasmo, sínquise), § 361 (o verso latino baseado na quantidade), § 362.1.a (ūnius com i breve na poesia), § 363.2.d e 363.3 (nē longo; mihi, tibi com i breve), § 363.4.b (o final breve na 1ª pessoa do verbo), § 364.2 e 364.5.b (-ās longo; -īs longo no perfeito do subjuntivo), § 366 (pés, ictus, elisão, cesura, sílaba final anceps), § 367.1 (sinérese: deinde), §§ 368–369 (hexâmetro, pentâmetro e dístico elegíaco), § 375.2 (oximoro)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 181.a–b (formas contraídas do perfectum: amārim, audieram), § 439 (exortativo; nota 2: exortativo e jussivo são a mesma construção; 439.a: 2ª pessoa com sujeito definido só em proibições, no latim arcaico e na poesia), § 450 (proibições: nōlī + infinitivo, cavē + subjuntivo, nē + perfeito do subjuntivo), § 603 (regras gerais de quantidade; 603.c nota: sinérese em deinde), § 604 (quantidade das sílabas finais; 604.g: o final comum; 604.i.5: -is longo às vezes em -eris). A edição DCC consultada não traz a parte de versificação (metros líricos), por isso os metros foram conferidos em Bennett, Kennedy e Ravizza.', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 347 (proibições), § 474 (pés; elisão), §§ 475–476 (metro, escansão, cesura forte e fraca), § 477 (hexâmetro), § 478 (pentâmetro e dístico elegíaco), § 481 (metros estróficos; base), § 482 (estrofe sáfica). Números lidos no OCR local.', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 371 (subjuntivo exortativo; observação: na 2ª pessoa do singular, "mais que uma ordem, se dá conselho"), n. 533 (pés: espondeu, dáctilo, coriambo), n. 534 (cesura), n. 535 (elisão, sinérese, sístole), n. 536 (espécies de versos: hexâmetro, pentâmetro e dístico; asclepiadeu maior, com a escansão de "Tu ne quaesieris"; falécio ou hendecassílabo, com um verso de Catulo; sáfico e adônio, com "Integer vitae"). Números lidos no OCR local, que às vezes os deforma (552 por 532, 555 por 533).', tipo='dominio_publico'),
    ],
    objetivos=[
        'Situar Catulo e Horácio na história da poesia latina e reconhecer o tema comum aos dois poemas: a brevidade da vida e o que fazer com ela.',
        'Ler e traduzir o poema 5 de Catulo e a ode I,11 de Horácio com a ajuda do vocabulário e das notas, justificando cada escolha de tradução pela forma latina.',
        'Escandir um hendecassílabo falécio, um asclepiadeu maior e um dístico elegíaco, marcando elisões e sílabas longas por natureza e por posição.',
        'Identificar nos dois poemas o subjuntivo exortativo, o jussivo de 2ª pessoa e a proibição com nē + perfeito, e distingui-los do indicativo futuro e futuro perfeito que os cercam.',
        'Reconhecer figuras (anáfora, antítese, hipérbato, metáfora) e explicar o efeito delas no sentido do poema.',
    ],
    secoes=[
        ('Dois poetas e uma pergunta', f'''
<p>Os dois poemas deste capítulo foram escritos com cerca de trinta anos de distância e respondem, cada um a seu modo, à mesma pergunta: se a vida é curta, como vivê-la? <b>Caio Valério Catulo</b> (<i>Gāius Valerius Catullus</i>, c. 84–54 a.C.), nascido em Verona, viveu em Roma nos últimos anos da República, no círculo de jovens poetas que imitavam os alexandrinos gregos: poemas curtos, muito trabalhados, cheios de erudição e de sentimento pessoal. Restou dele um único livro, com os poemas numerados de 1 a 116, em metros variados, sobre amizades, inimizades, viagens, a morte de um irmão e, sobretudo, o amor por uma mulher que ele chama <b>Lésbia</b>. O nome é um pseudônimo poético, uma homenagem à poetisa grega Safo, da ilha de Lesbos; a identidade da mulher é discutida desde a Antiguidade e não importa para a leitura.</p>
<p><b>Quinto Horácio Flaco</b> (<i>Quīntus Horātius Flaccus</i>, 65–8 a.C.), filho de um ex-escravo de Venúsia, estudou em Roma e em Atenas, lutou do lado perdedor na guerra civil e acabou amigo de Mecenas e do imperador Augusto. Os três primeiros livros das <i>Odes</i> (<i>Carmina</i>), publicados em 23 a.C., são o projeto mais ambicioso da lírica latina: adaptar ao latim os metros de Safo e Alceu, poetas gregos de seis séculos antes. As odes de Horácio são curtas, densas, de uma ordem de palavras difícil e calculada, e falam de amizade, vinho, política, religião e, sempre, do tempo que passa.</p>
<p>"Lírico" quer dizer, na origem, poesia cantada com a lira; em Roma, esses poemas eram lidos, mas conservaram os metros da canção. Por isso, além do sentido, este capítulo vai ler o <b>ritmo</b>, com as noções de quantidade e escansão do capítulo 40. Os textos são os das edições de domínio público de E. T. Merrill (Catulo, 1893) e de P. Shorey e G. J. Laing (Horácio, 1919), conferidos na Perseus Digital Library; os macrons foram acrescentados por nós, e as traduções são nossas.</p>
{tabela(['', 'Catulo 5', 'Horácio, Odes I,11'], [
    ['Data', 'anos 60–50 a.C. (data exata incerta)', 'publicada em 23 a.C., no livro I das <i>Odes</i>'],
    ['Destinatária', 'Lésbia, a amada', 'Leucônoe, uma jovem (nome grego inventado)'],
    ['Metro', 'hendecassílabo falécio (13 versos)', 'asclepiadeu maior (8 versos)'],
    ['Tom', 'apaixonado, provocador, quase infantil na contagem', 'calmo, de conselho, filosófico'],
    ['Modo verbal dominante', 'subjuntivo exortativo (1ª pl.) e imperativo', 'subjuntivo de proibição e jussivo de 2ª pessoa, e um imperativo final'],
    ['Resposta à brevidade da vida', 'amar agora, sem dar ouvidos a ninguém', 'não querer saber o futuro; aproveitar o dia presente'],
], 'Os dois poemas lado a lado')}
{observacao('Por que ler poemas inteiros', 'Nos capítulos de gramática, as frases autênticas vinham recortadas. Aqui os dois textos são lidos <b>completos</b>, porque um poema lírico curto é uma unidade: o fim responde ao começo (em Catulo, o <i>sciāmus</i> e o <i>sciat</i> do fim retomam a ideia de "avaliar" do verso 3; em Horácio, <i>carpe diem</i> resolve a proibição de saber do verso 1). Leia cada poema três vezes: uma em voz alta, sem traduzir; uma com as notas; e uma última, de novo em voz alta, já entendendo.')}
'''),
        ('Catulo 5: Vīvāmus, mea Lesbia', f'''
<p>O poema começa com três subjuntivos de 1ª pessoa do plural e termina com uma conta de beijos que ninguém pode conferir. No meio, nos versos 4 a 6, está o argumento: o sol se põe e volta todos os dias; nós, uma vez apagada a nossa breve luz, não voltamos. Leia primeiro o texto inteiro:</p>
{_poema(CATULO_5, CATULO_5_PT)}
{tabela(['v.', 'Palavra', 'Dicionário', 'Sentido e nota'], [
    ['1', 'vīvāmus, amēmus', 'vīvō, -ere, vīxī; amō, -āre', 'presente do subjuntivo, 1ª pl.: exortativo, "vivamos, amemos"'],
    ['2', 'rūmōrēs', 'rūmor, -ōris (m.)', 'boato, falatório; acusativo plural, objeto de <i>aestimēmus</i>'],
    ['2', 'senum sevēriōrum', 'senex, senis (m.); sevērus, -a, -um', 'genitivo plural; <i>sevēriōrum</i> é comparativo: "mais severos (do que deviam)"'],
    ['3', 'ūnius … assis', 'ūnus, -a, -um (gen. ūnīus); as, assis (m.)', 'genitivo de valor (capítulo 20): "em um único asse", a moeda de cobre de menor valor; <i>ūnius</i> com <i>i</i> breve, licença poética'],
    ['3', 'aestimēmus', 'aestimō, -āre', 'avaliar, dar preço; subjuntivo exortativo'],
    ['4', 'sōlēs', 'sōl, sōlis (m.)', 'sol; no plural, "os sóis", isto é, os dias que se sucedem'],
    ['4', 'occidere', 'occidō, -ere, occidī (de <i>ob</i> + <i>cadō</i>)', 'cair, pôr-se (o sol); não confundir com <i>occīdō</i>, "matar"'],
    ['4', 'redīre', 'redeō, -īre, rediī', 'voltar; infinitivo complementar de <i>possunt</i> (capítulo 27)'],
    ['5', 'semel', 'advérbio', 'uma vez; aqui, "uma vez por todas"'],
    ['5', 'cum … occidit', 'cum + indicativo', '"quando se põe": <i>cum</i> temporal com indicativo (capítulo 34)'],
    ['6', 'dormienda', 'dormiō, -īre', 'gerundivo: <i>nox est dormienda</i>, "a noite deve ser dormida"; <i>nōbīs</i> é o dativo de agente da perifrástica passiva (capítulo 31)'],
    ['7', 'dā mī', 'dō, dare; mī = mihi', 'imperativo singular; <i>mī</i> é a forma curta do dativo, frequente na poesia'],
    ['7', 'bāsia', 'bāsium, -ī (n.)', 'beijo; palavra afetiva, frequente em Catulo, de onde vem o português "beijo"'],
    ['7–9', 'mīlle; centum', 'indeclináveis', 'mil; cem'],
    ['7–10', 'deinde, dein', 'advérbio', 'depois; <i>dein</i> é a forma abreviada, de uma sílaba'],
    ['8–9', 'altera', 'alter, altera, alterum', 'outro (de dois), segundo; neutro plural, concorda com o <i>mīlia</i> subentendido de <i>mīlle</i>'],
    ['9', 'usque', 'advérbio', 'sem parar, continuamente'],
    ['10', 'mīlia', 'mīlia, -ium (n. pl.)', 'milhares; substantivo, plural de <i>mīlle</i>'],
    ['10', 'fēcerīmus', 'faciō, -ere, fēcī', 'futuro perfeito, 1ª pl.: "quando tivermos feito"'],
    ['11', 'conturbābimus', 'conturbō, -āre', 'misturar, embaralhar; termo de contabilidade, "confundir as contas"; futuro do indicativo'],
    ['11', 'nē sciāmus', 'sciō, -īre', 'oração final negativa, "para não sabermos" (capítulo 33)'],
    ['12', 'nē quis', 'quis = aliquis depois de <i>nē</i>', '"para que ninguém" (capítulo 17)'],
    ['12', 'invidēre', 'invideō, -ēre, invīdī', 'olhar com maus olhos, lançar mau-olhado; invejar'],
    ['13', 'tantum … bāsiōrum', 'tantum (n.) + genitivo', '"tanta quantidade de beijos": genitivo partitivo (capítulo 20); <i>tantum</i> é o sujeito do infinitivo <i>esse</i> (capítulo 28)'],
], 'Vocabulário e notas: Catulo 5', latim_cols=(1,))}
<h3>Notas de leitura</h3>
<p><b>Versos 1–3.</b> O poema abre com um convite que inclui quem fala: <i>vīvāmus</i>, <i>amēmus</i>, <i>aestimēmus</i>. É o subjuntivo exortativo do capítulo 32, sempre na 1ª pessoa do plural do presente. O terceiro verbo transforma o amor em uma questão de contas: os comentários dos velhos moralistas valem, todos juntos, <i>ūnius assis</i>, um único asse, o tostão romano. O genitivo de valor e o verbo <i>aestimāre</i> pertencem à linguagem do comércio, e essa linguagem volta no fim do poema.</p>
<p><b>Versos 4–6.</b> O argumento está numa <b>antítese</b> rigorosa: <i>sōlēs</i> (plural, que voltam) contra <i>nōbīs</i>; <i>occidere et redīre</i> contra <i>semel occidit</i>; <i>brevis lūx</i> contra <i>nox perpetua</i>. O mesmo verbo, <i>occidere</i>, serve ao pôr do sol e à morte humana. O verso 6 é pesado de propósito: <i>nox est perpetua ūna dormienda</i> junta "noite", "perpétua" e "única" numa perifrástica passiva, "uma única noite perpétua tem de ser dormida (por nós)". Na tradução, "resta dormir" ou "temos de dormir" dá a obrigação sem forçar o português.</p>
<p><b>Versos 7–9.</b> Do raciocínio o poema passa ao pedido: <i>dā mī bāsia</i>. A repetição de <i>deinde</i> e <i>dein</i> no começo de cada membro é uma <b>anáfora</b>, e a falta de conjunções (assíndeto) dá pressa à contagem: mil, cem, mil, cem, mil, cem. Os números são de propósito banais; o que importa é a impressão de excesso.</p>
<p><b>Versos 10–13.</b> No fim, a contabilidade volta. Quando a soma for grande (<i>cum mīlia multa fēcerīmus</i>, futuro perfeito: a ação estará concluída antes da outra), os amantes vão <i>conturbāre</i>, "embaralhar as contas", por dois motivos, cada um numa oração final com <i>nē</i>: para que eles mesmos não saibam o total, e para que nenhum invejoso possa lançar mau-olhado (<i>invidēre</i>, literalmente "olhar contra"), coisa que, na crença popular, exigia saber o número exato do que se queria atingir. O verbo <i>sciāmus</i> (v. 11) e o <i>sciat</i> do último verso fecham o poema sobre a ideia de "saber a conta", que o verso 3 tinha aberto.</p>
'''),
        ('O hendecassílabo de Catulo (e um dístico elegíaco)', f'''
<p>Catulo escreveu o poema 5 em <b>hendecassílabos falécios</b> (de Faleco, poeta grego; Ravizza n. 536 os chama "falêucios"). Como o nome diz, são versos de <b>onze sílabas</b>, e o esquema é fixo, sem as substituições do hexâmetro: uma <b>base</b> de duas sílabas (em Catulo quase sempre duas longas) e depois uma sequência invariável de longas e breves. Nas tabelas, <b>–</b> marca a sílaba longa, <b>˘</b> a breve e <b>×</b> a sílaba final, que pode ser longa ou breve (Bennett § 366.10).</p>
{tabela(['Parte', 'Posições', 'Esquema'], [
    ['Base', '1–2', '× × (em Catulo, quase sempre – –)'],
    ['Núcleo', '3–11', '– ˘ ˘ – ˘ – ˘ – ×'],
], 'O hendecassílabo falécio')}
<p>Primeiro verso. Duas elisões (Bennett § 366.7; capítulo 40): o <i>-a</i> final de <i>Lesbia</i> desaparece diante de <i>atque</i>, e o <i>-que</i> de <i>atque</i> desaparece diante de <i>amēmus</i>. Lido em voz alta: <i>vī-vā-mus-me-a-Les-bi-at-qua-mē-mus</i>, onze sílabas.</p>
{tabela(['Posição', 'Sílaba', 'Quantidade', 'Por quê'], [
    ['1', 'Vī', '–', '<i>ī</i> longo por natureza (<i>vīvō</i>)'],
    ['2', 'vā', '–', '<i>ā</i> longo por natureza: é a vogal do subjuntivo (<i>vīvāmus</i>)'],
    ['3', 'mus', '–', 'longa por posição: <i>u</i> breve seguido de <i>s</i> + <i>m</i> (<i>mus mea</i>)'],
    ['4', 'me', '˘', 'vogal breve seguida de vogal'],
    ['5', 'a', '˘', '<i>-a</i> final do vocativo, breve'],
    ['6', 'Les', '–', 'longa por posição (<i>s</i> + <i>b</i>)'],
    ['7', 'bi(a)', '˘', '<i>i</i> breve antes de vogal; o <i>-a</i> é elidido diante de <i>atque</i>'],
    ['8', 'at', '–', 'longa por posição (<i>t</i> + <i>qu</i>)'],
    ['9', 'qu(e) a', '˘', '<i>-que</i> elidido; fica o <i>a-</i> breve de <i>amēmus</i>'],
    ['10', 'mē', '–', '<i>ē</i> longo por natureza: vogal do subjuntivo da 1ª conjugação'],
    ['11', 'mus', '×', 'sílaba final, indiferente'],
], 'Escansão de Catulo 5,1: Vīvāmus, mea Lesbia, atque amēmus')}
<p>Quarto verso, com uma elisão no meio (<i>occider(e) et</i>):</p>
{tabela(['Posição', 'Sílaba', 'Quantidade', 'Por quê'], [
    ['1', 'Sō', '–', '<i>ō</i> longo por natureza (<i>sōl, sōlis</i>)'],
    ['2', 'lēs', '–', '<i>-ēs</i> do nominativo plural, longo'],
    ['3', 'oc', '–', 'longa por posição (<i>c</i> + <i>c</i>)'],
    ['4', 'ci', '˘', '<i>i</i> breve de <i>occĭdō</i> ("cair"); o verbo "matar", <i>occīdō</i>, teria <i>ī</i> longo e não caberia aqui'],
    ['5', 'de', '˘', 'vogal breve'],
    ['6', 'r(e) et', '–', 'o <i>-e</i> final de <i>occidere</i> é elidido; <i>et</i> fica longo por posição (<i>t</i> + <i>r</i> de <i>redīre</i>)'],
    ['7', 're', '˘', 'prefixo <i>re-</i>, breve'],
    ['8', 'dī', '–', '<i>ī</i> longo do infinitivo <i>redīre</i>'],
    ['9', 're', '˘', 'vogal breve'],
    ['10', 'pos', '–', 'longa por posição (<i>s</i> + <i>s</i>)'],
    ['11', 'sunt', '×', 'sílaba final'],
], 'Escansão de Catulo 5,4: sōlēs occidere et redīre possunt')}
{dica('<b>A métrica confirma a gramática.</b> No verso 4, o metro distingue <i>occĭdere</i> ("pôr-se") de <i>occīdere</i> ("matar"). No verso 3, <i>ūnius</i> precisa ter o <i>i</i> breve (<i>ū-nĭ-us</i>), uma licença que Bennett § 362.1.a registra para a poesia. No verso 10, <i>fēcerīmus</i> precisa do <i>ī</i> longo na posição 8; a quantidade desse <i>i</i> oscila na poesia, no futuro perfeito e no perfeito do subjuntivo (A&amp;G § 604.i.5 registra a mesma oscilação em <i>-eris</i>). E <i>dein</i>, nos versos 8 e 10, vale uma sílaba só: é a sinizese (ou sinérese, capítulo 40), que Bennett § 367.1 exemplifica justamente com <i>deinde</i>.')}
<h3>Um dístico elegíaco: Catulo 85</h3>
<p>O mesmo livro de Catulo tem poemas em <b>dístico elegíaco</b>: um hexâmetro seguido de um pentâmetro (Bennett § 369; Kennedy § 478; Ravizza n. 536). O mais famoso tem dois versos e é uma pequena aula de subjuntivo e de antítese:</p>
{exemplos([('Ōdī et amō. quārē id faciam, fortasse requīris.<br>nesciō, sed fierī sentiō et excrucior.', 'Odeio e amo. Por que faço isso, talvez perguntes. / Não sei, mas sinto que acontece, e sou torturado. (Catulo 85; tradução nossa)')])}
<p><i>Quārē id faciam</i> é uma interrogativa indireta, com o verbo no subjuntivo (capítulo 35), dependente de <i>requīris</i>; <i>fierī</i> é o infinitivo de <i>fīō</i> ("acontecer"), numa oração infinitiva com sujeito subentendido (<i>id</i>) depois de <i>sentiō</i> (capítulo 28). O par <i>ōdī et amō</i>, dois sentimentos contrários afirmados ao mesmo tempo, aproxima-se do <b>oximoro</b> (Bennett § 375.2). A escansão mostra o hexâmetro (seis pés) e o pentâmetro (duas metades de dois pés e meio):</p>
{tabela(['Pé', 'Hexâmetro', 'Esquema', 'Pentâmetro', 'Esquema'], [
    ['1', 'Ō | de | ta (<i>Ōd(ī) et a-</i>)', '– ˘ ˘', 'nes | ci | ŏ', '– ˘ ˘'],
    ['2', 'mō | quā', '– –', 'sed | fi | e', '– ˘ ˘'],
    ['3', 'r(ē) id | fa | ci', '– ˘ ˘', 'rī ‖', '– (meio pé; pausa obrigatória)'],
    ['4', 'am | for', '– –', 'sen | ti(ō) | e', '– ˘ ˘'],
    ['5', 'tas | se | re', '– ˘ ˘', 'tex | cru | ci', '– ˘ ˘'],
    ['6', 'quī | ris', '– ×', 'or', '× (meio pé)'],
], 'Escansão de Catulo 85')}
<p>Três detalhes. Em <i>Ōd(ī) et amō</i>, o <i>-ī</i> longo de <i>ōdī</i> se elide, e o <i>t</i> de <i>et</i> passa para a sílaba seguinte (<i>e-ta-mō</i>). Em <i>nesciŏ</i>, o <i>-ō</i> final do verbo é lido breve, licença registrada por Bennett § 363.4.b e por A&amp;G § 604.g (o <i>o</i> final é "comum"). E <i>fĭerī</i> tem o <i>i</i> breve, como manda a regra de <i>fīō</i> diante de <i>-er-</i> (Bennett § 362.1.c).</p>
'''),
        ('Horácio, Odes I,11: carpe diem', f'''
<p>A ode é dirigida a <b>Leucônoe</b>, uma jovem de nome grego, provavelmente inventado, que consulta os "cálculos babilônicos", isto é, os horóscopos dos astrólogos orientais, muito procurados em Roma, para saber quantos anos de vida ela e o poeta ainda têm. Horácio responde com uma proibição, um conselho em três verbos e uma imagem tirada do campo: <i>carpe diem</i>, "colhe o dia", como se colhe um fruto maduro antes que apodreça.</p>
{_poema(HORACIO_1_11, HORACIO_1_11_PT)}
{tabela(['v.', 'Palavra', 'Dicionário', 'Sentido e nota'], [
    ['1', 'quaesierīs', 'quaerō, -ere, quaesīvī, quaesītum', 'perfeito do subjuntivo sincopado (= <i>quaesīverīs</i>): com <i>nē</i>, proibição, "não procures"'],
    ['1', 'scīre nefās', 'sciō, -īre; nefās (n., indecl.)', 'parêntese: "[é] proibido [pela lei divina] saber"; <i>est</i> subentendido'],
    ['1–2', 'quem … fīnem', 'quī, quae, quod (interrogativo adjetivo); fīnis, -is (m.)', '"que fim": acusativo, objeto de <i>dederint</i>; o adjetivo está separado do nome (hipérbato)'],
    ['2', 'dī dederint', 'deus, -ī (nom. pl. dī); dō, dare, dedī', 'perfeito do subjuntivo: interrogativa indireta dependente de <i>quaesierīs</i> (capítulo 35)'],
    ['2', 'Leuconoē', 'Leuconoē, -ēs (f.)', 'vocativo de um nome grego, com <i>-ē</i> longo'],
    ['2–3', 'Babylōniōs … numerōs', 'Babylōnius, -a, -um; numerus, -ī (m.)', '"os cálculos babilônicos": os horóscopos dos astrólogos'],
    ['3', 'temptārīs', 'temptō, -āre', 'perfeito do subjuntivo sincopado (= <i>temptāverīs</i>): segunda proibição, ligada por <i>nec</i>'],
    ['3', 'ut melius … patī', 'ut (exclamativo); patior, patī (depoente)', '"como é melhor suportar…!": exclamação sem verbo finito; <i>patī</i> é o infinitivo presente do depoente (capítulo 25)'],
    ['3', 'quidquid erit', 'quisquis, quidquid', '"o que quer que seja (venha a ser)": relativo indefinido com futuro'],
    ['4', 'seu … seu', 'conjunção', 'quer… quer'],
    ['4', 'plūrīs hiemēs', 'plūrēs, plūra; hiems, hiemis (f.)', 'acusativo plural (<i>plūrīs</i> = <i>plūrēs</i>, forma de tema em <i>-i</i>, capítulo 10): "mais invernos", isto é, mais anos'],
    ['4', 'tribuit', 'tribuō, -ere, tribuī', 'perfeito do indicativo: "concedeu"'],
    ['4', 'ultimam', 'ultimus, -a, -um', 'concorda com <i>hiemem</i> subentendido: "[este inverno] como o último"'],
    ['5', 'oppositīs … pūmicibus', 'oppōnō, -ere, -posuī, -positum; pūmex, -icis (m.)', 'ablativo: "contra os rochedos (de pedra porosa) postos à frente"; <i>oppositīs</i> é particípio perfeito (capítulo 29)'],
    ['5', 'dēbilitat', 'dēbilitō, -āre', 'enfraquecer, quebrar; o inverno "cansa" o mar, arremessando-o contra as rochas'],
    ['5–6', 'mare Tyrrhēnum', 'mare, -is (n.); Tyrrhēnus, -a, -um', 'o mar Tirreno, a oeste da Itália; o adjetivo começa o verso seguinte (enjambement)'],
    ['6', 'sapiās', 'sapiō, -ere', 'ter juízo, ser sensato; presente do subjuntivo, 2ª sing.: jussivo, "sê sensata"'],
    ['6', 'vīna liquēs', 'vīnum, -ī (n.); liquō, -āre', 'coar o vinho (para tirar a borra e servi-lo logo); jussivo'],
    ['6', 'spatiō brevī', 'spatium, -ī (n.); brevis, -e', 'ablativo: "sendo breve o espaço (da vida)"'],
    ['7', 'spem longam resecēs', 'spēs, speī (f.); resecō, -āre', '"corta, poda a esperança longa": imagem do vinhateiro que poda a videira; jussivo'],
    ['7', 'dum loquimur', 'loquor, loquī (depoente)', '"enquanto falamos": <i>dum</i> com presente'],
    ['7', 'fūgerit', 'fugiō, -ere, fūgī', 'futuro perfeito do indicativo: "terá fugido" (antes que acabemos de falar)'],
    ['7–8', 'invida aetās', 'invidus, -a, -um; aetās, -ātis (f.)', '"o tempo invejoso", que não quer que aproveitemos; hipérbato entre os dois versos'],
    ['8', 'carpe', 'carpō, -ere, carpsī', 'imperativo: "colhe", como se colhem flores e frutos'],
    ['8', 'quam minimum', 'quam + superlativo', '"o menos possível" (capítulo 18)'],
    ['8', 'crēdula posterō', 'crēdulus, -a, -um (+ dat.); posterus, -a, -um', '"confiando no (dia) seguinte"; <i>crēdula</i> é nominativo feminino e concorda com o sujeito, Leucônoe; <i>posterō</i> é dativo, com <i>diēī</i> subentendido'],
], 'Vocabulário e notas: Horácio, Odes I,11', latim_cols=(1,))}
<h3>Notas de leitura</h3>
<p><b>Versos 1–3.</b> A ode começa por uma <b>proibição</b>: <i>nē quaesierīs</i>, e, coordenada a ela por <i>nec</i>, <i>temptārīs</i>. Os dois verbos estão no perfeito do subjuntivo, na forma <b>sincopada</b> que o perfectum admite quando perde o <i>-v-</i> (<i>quaesierīs</i> por <i>quaesīverīs</i>, <i>temptārīs</i> por <i>temptāverīs</i>; Bennett § 116.1; A&amp;G § 181). É a construção de proibição do capítulo 32, e o perfeito, aqui, não tem valor de passado. O objeto de <i>quaesierīs</i> é uma pergunta indireta, <i>quem mihi, quem tibi fīnem dī dederint</i>, "que fim os deuses deram a mim, que fim a ti", com a anáfora de <i>quem</i> separando o adjetivo do seu nome <i>fīnem</i>. No verso 3, depois da proibição, a alternativa: <i>ut melius, quidquid erit, patī!</i>, "como é melhor suportar o que vier!".</p>
<p><b>Versos 4–6.</b> A frase com <i>seu… seu</i> admite as duas hipóteses e as declara indiferentes: talvez Júpiter nos tenha dado muitos invernos, talvez este seja o último. Repare que Horácio conta a vida em <b>invernos</b>, e que este inverno, descrito com o mar batendo nas rochas da costa, é real e presente (<i>nunc</i>). A imagem do mar que se cansa contra a pedra prepara os conselhos que vêm em seguida.</p>
<p><b>Versos 6–8.</b> Três subjuntivos de 2ª pessoa do singular dão o conselho: <i>sapiās</i>, <i>liquēs</i>, <i>resecēs</i>. É o jussivo do capítulo 32, mas com uma diferença que vale a pena notar: na prosa, o jussivo de 2ª pessoa costuma ter sujeito indeterminado; na poesia, ele se dirige a uma pessoa definida, aqui Leucônoe (A&amp;G § 439.a; Bennett § 275.2, com o exemplo <i>modestē vīvās</i>, "vive com moderação"). Ravizza (n. 371, observação) diz bem o tom: na 2ª pessoa, "mais que uma ordem, se dá conselho". Só no fim vem o imperativo seco, <i>carpe</i>, e a mudança de modo marca o ponto alto do poema. Entre os conselhos, a frase <i>dum loquimur, fūgerit invida aetās</i> usa o <b>futuro perfeito</b> para dizer que o tempo terá fugido antes que a própria conversa acabe: o poema inteiro, lido em voz alta, já consumiu um pouco do dia que manda colher.</p>
{observacao('Carpe diem não é "faça o que quiser"', 'A expressão virou lema publicitário, mas no poema ela tem um sentido preciso. <i>Carpere</i> é o verbo da colheita: colhe-se o que está maduro, no momento certo, sem esperar que apodreça. O contrário de <i>carpe diem</i> não é a disciplina, e sim a <b>ansiedade pelo futuro</b>: os horóscopos de Leucônoe, a "esperança longa" (<i>spem longam</i>) que é preciso podar. O conselho de Horácio, de inspiração epicurista, pede sobriedade (<i>sapiās</i>) e atenção ao presente. Um leitor cristão pode compará-lo com "não vos inquieteis com o dia de amanhã" (Mateus 6,34), sem confundir as duas visões de mundo: em Horácio não há Providência, só a sensatez diante do acaso.')}
'''),
        ('O asclepiadeu maior e a ordem das palavras de Horácio', f'''
<p>A ode I,11 está escrita em <b>asclepiadeus maiores</b> (de Asclepíades, poeta grego), versos de dezesseis sílabas formados por um espondeu inicial, <b>três coriambos</b> e um final de duas sílabas: é o asclepiadeu menor do capítulo 40 com um coriambo a mais. O <b>coriambo</b> é o pé <b>– ˘ ˘ –</b> (Ravizza n. 533), uma longa, duas breves e outra longa. Ravizza (n. 536) escande justamente o primeiro verso desta ode como exemplo do metro. Uma pausa de fim de palavra (diérese) separa o primeiro coriambo do segundo e o segundo do terceiro, de modo que o verso se ouve em três blocos.</p>
{tabela(['Parte', 'Esquema', 'v. 1: sílabas', 'v. 8: sílabas'], [
    ['Espondeu', '– –', 'Tū | nē', 'ae | tās'],
    ['1º coriambo', '– ˘ ˘ –', 'quae | si | e | rīs ‖', 'car | pe | di | em ‖'],
    ['2º coriambo', '– ˘ ˘ –', 'scī | re | ne | fās ‖', 'quam | mi | ni | mum ‖'],
    ['3º coriambo', '– ˘ ˘ –', 'quem | mi | hi | quem', 'crē | du | la | pos'],
    ['Final', '˘ ×', 'ti | bi', 'te | rō'],
], 'Escansão de Horácio, Odes I,11, versos 1 e 8 (‖ = pausa de fim de palavra)')}
<p>Confira algumas quantidades do verso 1. <i>Tū</i> e <i>nē</i> são monossílabos terminados em vogal, longos (Bennett § 363.2.d). Em <i>quaesierīs</i>, o <i>-rīs</i> do perfeito do subjuntivo é longo (Bennett § 364.5.b), além de longo por posição antes de <i>sc-</i>. <i>Nefās</i> termina em <i>-ās</i>, longo (Bennett § 364.2). Em <i>mihi</i> e <i>tibi</i>, o <i>i</i> final é breve (Bennett § 363.3). No verso 8, <i>diem</i> não se elide, porque a palavra seguinte, <i>quam</i>, começa por consoante; e o <i>-em</i>, seguido de <i>m</i> + <i>q</i>, é longo por posição. Pratique os outros versos: todos seguem o mesmo esquema, sem substituições.</p>
{observacao('Outro metro de Horácio: a estrofe sáfica', 'Horácio usa mais de uma dezena de metros. O mais conhecido, depois do asclepiadeu, é a <b>estrofe sáfica</b> (Kennedy § 482; Ravizza n. 536): três hendecassílabos sáficos (<b>– ˘ – × – ˘ ˘ – ˘ – ×</b>) e um verso curto, o adônio (<b>– ˘ ˘ – ×</b>). Exemplo, Odes I,22,1: <i>In-te-ger vī-tae sce-le-ris-que pū-rus</i>, "o íntegro de vida e puro de crime". Note que o sáfico e o falécio de Catulo têm ambos onze sílabas, mas a ordem das longas e breves é outra; o nome "hendecassílabo", sozinho, designa o de Catulo.')}
<h3>A ordem das palavras</h3>
<p>A ordem das palavras de Horácio é a mais difícil da poesia latina, e a razão é que ela é <b>calculada</b>: o metro obriga, mas o poeta aproveita a obrigação para criar efeitos. A figura principal é o <b>hipérbato</b>, a separação de palavras que normalmente andam juntas (Bennett § 350.11.a). Em <i>quem mihi, quem tibi / fīnem</i>, o adjetivo interrogativo fica no verso 1 e o nome no verso 2; em <i>invida / aetās</i>, o adjetivo fecha o verso 7 e o nome abre o 8, de modo que o "tempo invejoso" literalmente atravessa a linha. Quando dois pares se cruzam numa ordem a-b-a-b, a figura se chama sínquise (Bennett § 350.11.d). A técnica de leitura é a do capítulo 8: avance pelo texto, anote o caso de cada adjetivo e deixe-o "em suspenso" até encontrar o nome com que concorda.</p>
{diagrama_frase([('Tū', 'nom. · sujeito (Leucônoe)'), ('nē quaesierīs', 'nē + perf. subj. · proibição'), ('quem … fīnem', 'ac. · objeto da pergunta'), ('dī dederint', 'perf. subj. · pergunta indireta')],
    'O período do verso 1, reduzido ao essencial: <i>Tū nē quaesierīs quem fīnem dī dederint</i> = Não procures saber que fim os deuses (te) deram. A proibição governa a pergunta indireta; <i>mihi, tibi</i> (dativos) e o parêntese <i>scīre nefās</i> ficaram de fora do esquema.')}
{tabela(['Figura', 'Onde', 'Efeito'], [
    ['Anáfora', '<i>deinde … dein … deinde</i> (Catulo 5,7–10); <i>quem … quem</i> (Horácio, v. 1)', 'ritmo de contagem; insistência'],
    ['Antítese', '<i>sōlēs … redīre</i> × <i>nōbīs … semel</i>; <i>brevis lūx</i> × <i>nox perpetua</i> (Catulo 5,4–6)', 'o sol volta, nós não'],
    ['Oximoro', '<i>Ōdī et amō</i> (Catulo 85)', 'dois sentimentos contrários no mesmo instante'],
    ['Hipérbato', '<i>quem … fīnem</i>; <i>invida … aetās</i> (Horácio, vv. 1–2, 7–8)', 'a ordem das palavras imita o sentido ou cria expectativa'],
    ['Metáfora', '<i>lūx</i> e <i>nox</i> por vida e morte (Catulo); <i>carpe</i>, <i>resecēs</i> (Horácio)', 'a vida como dia; o tempo como colheita e poda'],
    ['Assíndeto', '<i>dā mī bāsia mīlle, deinde centum, dein mīlle altera…</i>', 'pressa, acúmulo sem pausa'],
], 'Figuras de linguagem nos dois poemas (capítulo 40)', latim_cols=())}
'''),
        ('O subjuntivo nos dois poemas; análise palavra a palavra', f'''
<p>Os dois poemas são um pequeno catálogo dos usos independentes do subjuntivo que o capítulo 32 apresentou, cercados de formas do indicativo que é preciso não confundir com eles. O quadro abaixo junta todos os verbos finitos dos dois textos:</p>
{tabela(['Forma', 'Onde', 'Modo, tempo, pessoa', 'Uso', 'Tradução'], [
    ['vīvāmus, amēmus, aestimēmus', 'Catulo 5,1.3', 'subj. presente, 1ª pl.', 'exortativo', 'vivamos, amemos, avaliemos'],
    ['dā', 'Catulo 5,7', 'imperativo, 2ª sing.', 'ordem direta', 'dá'],
    ['fēcerīmus', 'Catulo 5,10', 'ind. futuro perfeito, 1ª pl.', 'com <i>cum</i> temporal', 'quando tivermos feito'],
    ['conturbābimus', 'Catulo 5,11', 'ind. futuro, 1ª pl.', 'afirmação', 'embaralharemos'],
    ['sciāmus; possit', 'Catulo 5,11–12', 'subj. presente', 'orações finais com <i>nē</i> (capítulo 33)', 'para não sabermos; para que ninguém possa'],
    ['sciat', 'Catulo 5,13', 'subj. presente, 3ª sing.', '<i>cum</i> dentro de uma oração no subjuntivo (capítulo 34)', 'quando souber'],
    ['nē quaesierīs; nec temptārīs', 'Horácio, vv. 1–3', 'subj. perfeito, 2ª sing.', 'proibição', 'não procures; nem consultes'],
    ['dederint', 'Horácio, v. 2', 'subj. perfeito, 3ª pl.', 'interrogativa indireta (capítulo 35)', '(que fim) deram'],
    ['sapiās, liquēs, resecēs', 'Horácio, vv. 6–7', 'subj. presente, 2ª sing.', 'jussivo (conselho)', 'sê sensata, coa, corta'],
    ['fūgerit', 'Horácio, v. 7', 'ind. futuro perfeito, 3ª sing.', 'afirmação', 'terá fugido'],
    ['carpe', 'Horácio, v. 8', 'imperativo, 2ª sing.', 'ordem direta', 'colhe'],
], 'Os verbos finitos dos dois poemas', latim_cols=(0,))}
{dica('<b>Futuro perfeito ou perfeito do subjuntivo?</b> <i>Fūgerit</i> e <i>fēcerīmus</i> têm a mesma cara do perfeito do subjuntivo (<i>fūgerit</i>, <i>fēcerimus</i>): as duas séries só diferem na 1ª pessoa do singular (<i>fūgerō</i> × <i>fūgerim</i>). Quem decide é a construção. Em Horácio, <i>fūgerit</i> está numa oração principal sem <i>nē</i>, ao lado de <i>dum loquimur</i>: é uma afirmação sobre o futuro, "terá fugido". Em <i>nē quaesierīs</i>, ao contrário, o <i>nē</i> mostra que se trata de uma proibição, e portanto de subjuntivo.')}
<p>Agora, a análise palavra a palavra do começo de Catulo, que reúne o exortativo, o vocativo e o genitivo de valor:</p>
{analise('Catulo 5,1–3, palavra a palavra', [
    ('Vīvāmus', 'vīvō, -ere, vīxī, vīctum, viver', 'presente do subjuntivo ativo, 1ª pl.', 'exortativo: "vivamos"'),
    ('mea', 'meus, -a, -um, meu', 'vocativo singular feminino', 'concorda com <i>Lesbia</i>'),
    ('Lesbia', 'Lesbia, -ae (f.)', 'vocativo singular', 'a quem se fala'),
    ('atque', 'atque (conjunção)', 'invariável', 'liga <i>vīvāmus</i> e <i>amēmus</i>'),
    ('amēmus', 'amō, -āre, amāvī, amātum, amar', 'presente do subjuntivo ativo, 1ª pl.', 'exortativo: "amemos"'),
    ('rūmōrēsque', 'rūmor, rūmōris (m.), boato + -que', 'acusativo plural', 'objeto de <i>aestimēmus</i>'),
    ('senum', 'senex, senis (m.), velho', 'genitivo plural', 'de quem são os boatos'),
    ('sevēriōrum', 'sevērus, -a, -um; comparativo sevērior, -ius', 'genitivo plural masculino', 'concorda com <i>senum</i>: "mais severos"'),
    ('omnēs', 'omnis, -e, todo', 'acusativo plural masculino', 'concorda com <i>rūmōrēs</i>, separado dele (hipérbato)'),
    ('ūnius', 'ūnus, -a, -um, um só', 'genitivo singular (<i>i</i> breve, licença poética)', 'concorda com <i>assis</i>'),
    ('aestimēmus', 'aestimō, -āre, avaliar', 'presente do subjuntivo ativo, 1ª pl.', 'exortativo: "avaliemos"'),
    ('assis', 'as, assis (m.), asse (moeda)', 'genitivo singular', 'genitivo de valor: "em (o preço de) um asse"'),
])}
<p>E o centro da ode de Horácio, com o jussivo, o futuro perfeito e o imperativo lado a lado:</p>
{analise('Horácio, Odes I,11,6–8 (sapiās … posterō), palavra a palavra', [
    ('sapiās', 'sapiō, -ere, ter juízo', 'presente do subjuntivo, 2ª sing.', 'jussivo de conselho: "sê sensata"'),
    ('vīna', 'vīnum, -ī (n.), vinho', 'acusativo plural neutro', 'objeto de <i>liquēs</i>'),
    ('liquēs', 'liquō, -āre, coar', 'presente do subjuntivo, 2ª sing. (1ª conj.: <i>-ā-</i> → <i>-ē-</i>)', 'jussivo: "coa"'),
    ('et', 'et (conjunção)', 'invariável', 'liga o terceiro conselho'),
    ('spatiō brevī', 'spatium, -ī (n.); brevis, -e', 'ablativo singular neutro', 'circunstância: "sendo breve o espaço"'),
    ('spem longam', 'spēs, speī (f.); longus, -a, -um', 'acusativo singular feminino', 'objeto de <i>resecēs</i>'),
    ('resecēs', 'resecō, -āre, cortar, podar', 'presente do subjuntivo, 2ª sing.', 'jussivo: "corta"'),
    ('dum', 'dum (conjunção)', 'invariável', '"enquanto", com o presente'),
    ('loquimur', 'loquor, loquī, locūtus sum, falar', 'presente do indicativo, 1ª pl. (depoente)', 'oração temporal'),
    ('fūgerit', 'fugiō, -ere, fūgī, fugitum, fugir', 'futuro perfeito do indicativo, 3ª sing.', 'verbo principal: "terá fugido"'),
    ('invida aetās', 'invidus, -a, -um; aetās, -ātis (f.)', 'nominativo singular feminino', 'sujeito de <i>fūgerit</i>'),
    ('carpe', 'carpō, -ere, carpsī, carptum, colher', 'imperativo presente, 2ª sing.', 'ordem direta'),
    ('diem', 'diēs, diēī (m.), dia', 'acusativo singular', 'objeto de <i>carpe</i>'),
    ('quam minimum', 'quam + minimum (superlativo de parum)', 'advérbio', '"o menos possível"'),
    ('crēdula', 'crēdulus, -a, -um, que confia', 'nominativo singular feminino', 'predicativo do sujeito (Leucônoe): "confiando"'),
    ('posterō', 'posterus, -a, -um, seguinte', 'dativo singular masculino (<i>diēī</i> subentendido)', 'complemento de <i>crēdula</i>: "no (dia) seguinte"'),
])}
<h3>Resumo</h3>
<ul>
<li>Catulo 5 convida (exortativo de 1ª pl.: <i>vīvāmus, amēmus</i>), argumenta por antítese (o sol volta, nós não) e termina numa conta de beijos impossível de conferir.</li>
<li>Horácio I,11 proíbe (<i>nē quaesierīs</i>, perfeito do subjuntivo sincopado), aconselha (jussivo de 2ª pessoa: <i>sapiās, liquēs, resecēs</i>) e ordena (<i>carpe diem</i>).</li>
<li>Hendecassílabo falécio: base de duas sílabas + <b>– ˘ ˘ – ˘ – ˘ – ×</b>. Asclepiadeu maior: espondeu + três coriambos (<b>– ˘ ˘ –</b>) + <b>˘ ×</b>. Dístico elegíaco: hexâmetro + pentâmetro.</li>
<li>A métrica confirma formas e quantidades (<i>occĭdere</i>, <i>ūnĭus</i>, <i>dein</i> monossílabo por sinizese), e o hipérbato pede leitura com adjetivos "em suspenso".</li>
</ul>
<p>No próximo capítulo, Ovídio leva a leitura poética ao hexâmetro narrativo, com a criação do mundo no início das <i>Metamorfoses</i>.</p>
'''),
    ],
    erros_comuns=[
        ('Traduzir <i>vīvāmus, amēmus</i> como futuro ("viveremos, amaremos") ou como indicativo.', 'A vogal <i>-ā-</i> em <i>vīvāmus</i> (verbo da 3ª conjugação) e o <i>-ē-</i> em <i>amēmus</i> (1ª conjugação) são marcas do presente do subjuntivo; na 1ª pessoa do plural, numa oração principal, é o exortativo: "vivamos, amemos". O futuro seria <i>vīvēmus</i>, <i>amābimus</i>, e o próprio poema mostra um futuro de verdade no verso 11, <i>conturbābimus</i>.'),
        ('Ler <i>nē quaesierīs</i> como passado ("não procuraste") e <i>fūgerit</i> como subjuntivo.', 'Na proibição com <i>nē</i>, o perfeito do subjuntivo não tem valor de passado: "não procures" (capítulo 32). Já <i>fūgerit</i>, sem <i>nē</i> e numa oração principal, é futuro perfeito do indicativo: "terá fugido". As formas coincidem fora da 1ª pessoa do singular; decide a construção.'),
        ('Ligar cada adjetivo ao nome mais próximo: <i>invida</i> com <i>aetās</i> está certo, mas <i>omnēs</i> com <i>senum</i> ou <i>quem</i> com <i>mihi</i> está errado.', 'Na poesia, o hipérbato separa as palavras que concordam. <i>Omnēs</i> (acusativo plural) só pode concordar com <i>rūmōrēs</i>; <i>quem</i> (acusativo masculino singular) só com <i>fīnem</i>. Anote o caso de cada adjetivo e procure o nome com o mesmo gênero, número e caso, mesmo no verso seguinte.'),
        ('Escandir contando só as vogais escritas, sem elidir: <i>Vī-vā-mus-me-a-Les-bi-a-at-que-a-mē-mus</i> (13 sílabas).', 'Uma vogal final (ou vogal + <i>m</i>) diante de palavra iniciada por vogal ou <i>h</i> se elide (Bennett § 366.7). Em Catulo 5,1, <i>Lesbi(a) atqu(e) amēmus</i> perde duas sílabas, e o verso fica com as onze do hendecassílabo. Antes de escandir, marque todas as elisões.'),
        ('Achar que toda vogal seguida de duas consoantes é longa por natureza, e pronunciá-la longa: *<i>ēst</i>, *<i>īn</i>.', 'A sílaba é longa por posição, mas a vogal continua breve (A&amp;G § 603.f: pronuncie as vogais com a quantidade natural). Em <i>et redīre</i>, a sílaba <i>et</i> conta como longa no verso, e o <i>e</i> continua breve. Na leitura em voz alta, alongue o tempo da sílaba, não a vogal.'),
        ('Entender <i>carpe diem</i> como "goza a vida sem pensar nas consequências".', 'O contexto do poema mostra outra coisa: o que se rejeita é a ansiedade de saber o futuro (os horóscopos, a "esperança longa"), e o que se pede é sensatez (<i>sapiās</i>) e atenção ao presente. Traduza <i>carpe</i> pelo verbo da colheita, "colhe", e deixe a imagem trabalhar.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Ler e traduzir Catulo 5,4–6',
            'Leia em voz alta e traduza, na ordem latina: <i lang="la">sōlēs occidere et redīre possunt: nōbīs, cum semel occidit brevis lūx, nox est perpetua ūna dormienda.</i> Use o vocabulário da seção 2.', [
            ('Qual é o primeiro verbo finito, e qual o seu sujeito?', '<i>Possunt</i>, 3ª pl. de <i>possum</i>. O sujeito, no nominativo plural, é <i>sōlēs</i>: "os sóis podem". <i>Occidere</i> e <i>redīre</i> são infinitivos complementares de <i>possunt</i> (capítulo 27): "podem pôr-se e voltar".'),
            ('Que caso é <i>nōbīs</i>, e por que fica em suspenso?', 'Dativo ou ablativo plural de <i>nōs</i>. Não há preposição; fica em suspenso até aparecer a construção que o explique. Ele contrasta com <i>sōlēs</i>: "mas para nós…" (a ausência de "mas" é um assíndeto adversativo).'),
            ('O que faz a oração <i>cum semel occidit brevis lūx</i>?', '<i>Cum</i> com indicativo é temporal: "quando de uma vez se põe a breve luz". <i>Lūx</i> é o sujeito, <i>brevis</i> concorda com ele (nominativo singular feminino). <i>Occidit</i> pode ser presente ou perfeito (as duas formas coincidem); o paralelo com <i>occidere</i> do verso 4 e o valor geral da frase pedem o presente.'),
            ('Analise a oração principal <i>nox est perpetua ūna dormienda</i>.', '<i>Nox</i>, nominativo singular, é o sujeito; <i>perpetua</i> e <i>ūna</i> concordam com ele; <i>est dormienda</i> é a perifrástica passiva (gerundivo + <i>sum</i>, capítulo 31): "a noite deve ser dormida". E agora <i>nōbīs</i> se explica: é o dativo de agente da perifrástica, "por nós".'),
            ('Monte a tradução.', 'Literal: "Os sóis podem pôr-se e voltar; por nós, quando de uma vez se põe a breve luz, uma única noite perpétua deve ser dormida." Mais natural: "Os sóis podem pôr-se e voltar: nós, quando se apaga de uma vez a breve luz, temos de dormir uma única noite sem fim."'),
        ]),
        pratica_guiada('Prática guiada 2 · Escandir Horácio, Odes I,11,3',
            'Escanda o verso <i lang="la">temptārīs numerōs. ut melius, quidquid erit, patī.</i> sabendo que ele é um asclepiadeu maior (– – | – ˘ ˘ – | – ˘ ˘ – | – ˘ ˘ – | ˘ ×).', [
            ('Há elisões?', 'Não. Em <i>numerōs ut</i>, a primeira palavra termina em consoante; em <i>melius quidquid</i> e <i>erit patī</i>, a segunda palavra começa por consoante. Sem elisões, o verso deve ter exatamente dezesseis sílabas: <i>temp-tā-rīs-nu-me-rōs-ut-me-li-us-quid-quid-e-rit-pa-tī</i>.'),
            ('Quais são as duas primeiras sílabas?', '<i>temp</i> (longa por posição: <i>e</i> + <i>mpt</i>) e <i>tā</i> (longa por natureza: o <i>ā</i> de <i>temptāre</i>). Espondeu.'),
            ('Escanda o primeiro coriambo.', '<i>rīs</i> (–: <i>-īs</i> longo do perfeito do subjuntivo, Bennett § 364.5.b), <i>nu</i> (˘), <i>me</i> (˘), <i>rōs</i> (–: acusativo plural em <i>-ōs</i>). Fim de palavra depois de <i>numerōs</i>: é a primeira pausa.'),
            ('E o segundo?', '<i>ut</i> (–: longa por posição, <i>t</i> + <i>m</i>), <i>me</i> (˘), <i>li</i> (˘: vogal antes de vogal), <i>us</i> (–: <i>s</i> + <i>qu</i>). Fim de palavra depois de <i>melius</i>: segunda pausa.'),
            ('Termine o verso.', 'Terceiro coriambo: <i>quid</i> (–: <i>d</i> + <i>qu</i>), <i>qui</i> (˘), <i>de</i> (˘: o <i>d</i> passa para a sílaba seguinte, <i>qui-de-rit</i>), <i>rit</i> (–: <i>t</i> + <i>p</i>). Final: <i>pa</i> (˘), <i>tī</i> (×).'),
        ], 'Conclusão: as quantidades do verso confirmam a forma sincopada <i>temptārīs</i> (com <i>ā</i> e <i>ī</i> longos) e mostram que o ritmo de Horácio é regular: o que parece difícil é a ordem das palavras, não o metro.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Compreensão', 'Responda em português, apoiando cada resposta numa palavra ou expressão latina.', [
            ('Em Catulo 5, quanto valem os comentários dos velhos, e que palavra diz isso?', 'Valem um asse, a menor moeda: <i>ūnius aestimēmus assis</i>, genitivo de valor. Isto é, não valem nada.'),
            ('Qual é, em Catulo 5,4–6, a diferença entre os sóis e nós?', 'Os sóis "podem pôr-se e voltar" (<i>occidere et redīre possunt</i>); nós, quando a breve luz se põe "uma vez" (<i>semel</i>), temos uma "noite perpétua" (<i>nox perpetua</i>). O sol volta; a vida humana não.'),
            ('Por que os amantes vão "embaralhar" a conta dos beijos?', 'Por dois motivos, em duas orações finais: <i>nē sciāmus</i>, para que eles mesmos não saibam o total, e <i>nē quis malus invidēre possit</i>, para que nenhum malvado possa lançar mau-olhado, o que, na crença antiga, exigia saber o número exato.'),
            ('O que Leucônoe estava fazendo, segundo Horácio?', 'Consultando os "cálculos babilônicos" (<i>Babylōniōs numerōs</i>), isto é, horóscopos, para saber "que fim os deuses deram" a ela e ao poeta (<i>quem mihi, quem tibi fīnem dī dederint</i>).'),
            ('Que estação do ano é o "agora" da ode, e como se sabe?', 'O inverno: o poeta fala do inverno "que agora (<i>nunc</i>) cansa o mar Tirreno contra os rochedos" (vv. 4–6). <i>Quae</i> retoma <i>ultimam</i> (<i>hiemem</i>).'),
        ]),
        exercicio('Exercício 2 · Morfologia dos verbos', 'Dê o modo, o tempo, a pessoa e o número, e a forma de dicionário.', [
            ('<i>aestimēmus</i>', 'Presente do subjuntivo ativo, 1ª pessoa do plural, de <i>aestimō, -āre</i>. O <i>-ē-</i> no lugar do <i>-ā-</i> é a marca do subjuntivo na 1ª conjugação.'),
            ('<i>conturbābimus</i>', 'Futuro do indicativo ativo, 1ª pessoa do plural, de <i>conturbō, -āre</i> (sufixo <i>-bi-</i> da 1ª e 2ª conjugações).'),
            ('<i>fēcerīmus</i>', 'Futuro perfeito do indicativo ativo, 1ª pessoa do plural, de <i>faciō, -ere, fēcī</i>. Com <i>cum</i>: "quando tivermos feito".'),
            ('<i>quaesierīs</i>', 'Perfeito do subjuntivo ativo, 2ª pessoa do singular, de <i>quaerō, -ere, quaesīvī</i>, em forma sincopada (= <i>quaesīverīs</i>).'),
            ('<i>liquēs</i>', 'Presente do subjuntivo ativo, 2ª pessoa do singular, de <i>liquō, -āre</i>. Cuidado: não é presente do indicativo da 2ª conjugação; o dicionário mostra que o verbo é da 1ª, e então <i>-ē-</i> é subjuntivo.'),
            ('<i>fūgerit</i>', 'Futuro perfeito do indicativo ativo, 3ª pessoa do singular, de <i>fugiō, -ere, fūgī</i>. A forma é idêntica à do perfeito do subjuntivo; o contexto (oração principal, sem <i>nē</i>, ao lado de <i>dum loquimur</i>) decide.'),
            ('<i>patī</i>', 'Infinitivo presente de <i>patior, patī, passus sum</i>, verbo depoente: forma passiva, sentido ativo, "suportar".'),
        ]),
        exercicio('Exercício 3 · Sintaxe', 'Explique a construção destacada.', [
            ('<i>nōbīs</i> … <i>nox est perpetua ūna <b>dormienda</b></i> (Catulo 5,5–6)', 'Perifrástica passiva (gerundivo + <i>sum</i>), que exprime obrigação: "deve ser dormida". <i>Nōbīs</i> é o dativo de agente, próprio dessa construção: "por nós" (capítulo 31).'),
            ('<i>omnēs ūnius aestimēmus <b>assis</b></i> (Catulo 5,3)', 'Genitivo de valor com verbo de avaliar (<i>aestimāre</i>): "avaliemos em um asse" (capítulo 20).'),
            ('<i><b>nē quaesierīs</b> … nec <b>temptārīs</b></i> (Horácio, vv. 1–3)', 'Proibição: <i>nē</i> + perfeito do subjuntivo, 2ª pessoa, continuada por <i>nec</i> + outro perfeito do subjuntivo. O perfeito não tem valor de passado (capítulo 32; A&amp;G § 450).'),
            ('<i><b>sapiās</b>, vīna <b>liquēs</b> … <b>resecēs</b></i> (Horácio, vv. 6–7)', 'Subjuntivo jussivo de 2ª pessoa, dirigido a uma pessoa definida, uso próprio da poesia (A&amp;G § 439.a), com tom de conselho (Ravizza n. 371).'),
            ('<i><b>crēdula</b> posterō</i> (Horácio, v. 8)', 'Adjetivo no nominativo feminino singular, predicativo do sujeito de <i>carpe</i> (Leucônoe): "(tu,) confiando o menos possível no amanhã". <i>Posterō</i> é o dativo regido por <i>crēdula</i>.'),
        ]),
        exercicio('Exercício 4 · Métrica', 'Responda e justifique com as regras de quantidade.', [
            ('Escanda Catulo 5,7: <i>dā mī bāsia mīlle, deinde centum</i>.', '<i>dā</i> (–) <i>mī</i> (–) | <i>bā</i> (–) <i>si</i> (˘) <i>a</i> (˘) <i>mīl</i> (–) <i>le</i> (˘) <i>dein</i> (–) <i>de</i> (˘) <i>cen</i> (–) <i>tum</i> (×). Onze sílabas, sem elisão (<i>mīlle</i> termina em vogal, mas <i>deinde</i> começa por consoante); <i>dein-</i> é uma só sílaba por sinizese.'),
            ('Quantas sílabas tem Horácio, Odes I,11,2 (<i>fīnem dī dederint, Leuconoē, nec Babylōniōs</i>), e onde caem as pausas?', 'Dezesseis: <i>fī-nem | dī-de-de-rint ‖ Leu-co-no-ē ‖ nec-Ba-by-lō | ni-ōs</i>. As pausas de fim de palavra caem depois de <i>dederint</i> e de <i>Leuconoē</i>, isto é, depois do 1º e do 2º coriambo, como manda o asclepiadeu maior.'),
            ('Por que a primeira sílaba de <i>occidere</i> é longa, se o <i>o</i> é breve?', 'Porque o <i>o</i> é seguido de duas consoantes (<i>cc</i>): a sílaba é longa por posição (Bennett § 5.B.1.c), embora a vogal continue breve.'),
            ('No pentâmetro de Catulo 85, como se lê <i>sentiō et excrucior</i>?', 'O <i>-ō</i> final de <i>sentiō</i> se elide diante de <i>et</i>: <i>sen-ti-e-tex-cru-ci-or</i>, dois dáctilos (<i>sen-ti-e</i>, <i>tex-cru-ci</i>) e o meio pé final (<i>or</i>), como na segunda metade de todo pentâmetro.'),
        ]),
        exercicio('Exercício 5 · Tradução e reflexão', 'Traduza com as suas palavras e responda.', [
            ('Traduza Horácio, vv. 3–4: <i>ut melius, quidquid erit, patī. seu plūrīs hiemēs seu tribuit Iuppiter ultimam</i>.', '"Como é melhor suportar o que vier! Quer Júpiter (nos) tenha concedido mais invernos, quer (este) como o último…". <i>Ut</i> é exclamativo; <i>patī</i> é o infinitivo do depoente <i>patior</i>; <i>plūrīs</i> é acusativo plural (= <i>plūrēs</i>) e <i>ultimam</i> concorda com <i>hiemem</i> subentendido.'),
            ('Traduza Catulo 5,10–11: <i>dein, cum mīlia multa fēcerīmus, conturbābimus illa, nē sciāmus</i>.', '"Depois, quando tivermos feito muitos milhares, vamos embaralhá-los, para não sabermos (quantos são)." <i>Illa</i> (neutro plural) retoma <i>mīlia</i>; <i>nē sciāmus</i> é oração final.'),
            ('Em que os dois poemas concordam, e em que diferem? Responda em três ou quatro linhas, citando o latim.', 'Concordam no ponto de partida: a vida é breve (<i>brevis lūx</i> em Catulo; <i>spatiō brevī</i> em Horácio) e o presente é o que temos. Diferem no tom e na resposta: Catulo convida, com exortativos de 1ª pessoa (<i>vīvāmus, amēmus</i>), a um amor que ignora os outros e multiplica sem medida; Horácio aconselha, com jussivos de 2ª pessoa (<i>sapiās, resecēs</i>), a renunciar ao saber do futuro e a moderar a esperança. Em Catulo a resposta é a intensidade; em Horácio, a sensatez.'),
        ]),
    ],
    leituras=['catullus-catulli-carmina', 'flaccus-carmina-et-epodi-odes-e-epodos', 'naso-amores-liber-i', 'ravizza-gramatica-latina', 'bennett-new-latin-grammar'],
    leituras_nota='Depois deste capítulo, continue em Catulo com poemas curtos do mesmo livro (na edição de Ellis, <i>Catulli Carmina</i>): o 101, a despedida ao irmão morto, em dísticos, e os poemas 2 e 3, sobre o pardal de Lésbia, em hendecassílabos. Nas <i>Odes</i> de Horácio (Shorey e Laing), leia I,9 (o monte Soracte coberto de neve, com outro <i>carpe diem</i>) e I,22 (<i>Integer vitae</i>, em estrofes sáficas), sempre com o vocabulário ao lado. Para treinar a escansão do dístico elegíaco antes de Ovídio, o livro I dos <i>Amores</i> na edição comentada do DCC traz vocabulário, notas e áudio. As regras de métrica estão em Ravizza (nn. 533–536) e em Bennett (§§ 360–369).',
)
