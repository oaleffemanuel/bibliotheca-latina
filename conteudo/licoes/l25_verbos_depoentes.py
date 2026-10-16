from conteudo.util import (tabela, tabela_conjugacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='25-verbos-depoentes', titulo='Verbos depoentes e semidepoentes',
    titulo_latim='Dē verbīs dēpōnentibus', tempo='60 min',
    resumo='Os verbos de forma passiva e sentido ativo: como reconhecê-los pela entrada de dicionário (hortor, hortārī, hortātus sum), como conjugá-los nas quatro conjugações com o que você já sabe da passiva, como traduzi-los, quais formas eles têm com aparência ativa, os cinco depoentes que pedem ablativo (ūtor, fruor, fungor, potior, vescor) e os semidepoentes audeō, gaudeō, soleō e fīdō.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['verbos depoentes', 'forma passiva, sentido ativo', 'entrada de dicionário com três partes', 'depoentes das quatro conjugações', 'depoentes em -ior (patior)', 'orior',
             'tradução ativa', 'depoentes transitivos com acusativo', 'imperativo dos depoentes (menção)', 'formas de aparência ativa (menção)', 'particípio perfeito com sentido ativo',
             'ūtor, fruor, fungor, potior, vescor + ablativo', 'semidepoentes: audeō, gaudeō, soleō, fīdō', 'fīō (menção)', 'análise de frases autênticas'],
    prerequisitos=dict(texto='Capítulos 23 e 24: as terminações da voz passiva no infectum (<i>-or, -ris, -tur, -mur, -minī, -ntur</i>; <i>-bar</i>, <i>-bor</i>, <i>-ar</i>; infinitivo em <i>-rī</i> e <i>-ī</i>) e a passiva do perfectum (particípio perfeito + <i>sum</i>, com concordância). Também o capítulo 13 (partes principais) e o capítulo 21 (ablativo de meio).',
                       licoes=['13-o-perfeito-e-as-partes-principais', '21-usos-do-acusativo-e-do-ablativo', '23-a-voz-passiva-infectum', '24-a-passiva-do-perfectum']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 109.2.c (gradior, morior, patior seguem capiō), § 112 (depoentes: forma passiva, sentido ativo; formas ativas: infinitivo futuro, particípios presente e futuro, gerúndio, supino; gerundivo passivo), § 113 (paradigmas mīror, vereor, sequor, largior, patior), § 114.1–3 (semidepoentes audeō, gaudeō, soleō, fīdō; particípios perfeitos de sentido ativo como cēnātus; revertor), § 123.VII (orior segue em geral a 3ª conjugação: oreris, oritur), § 218.1 (ūtor, fruor, fungor, potior, vescor + ablativo), § 219.1.a (fīdō, cōnfīdō + dativo da pessoa)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', url='https://dcc.dickinson.edu/grammar/latin/deponent-verbs', nota='§ 190 (definição; a–g: particípios das duas vozes, particípio perfeito ativo, infinitivo futuro ativo, gerundivo passivo, sentido médio ou reflexivo), § 191 (mais da metade dos depoentes são da 1ª conjugação; lista dos irregulares: loquor, morior, nāscor, orior, patior, proficīscor, sequor, ūtor…), § 192 (semidepoentes; 192.b, fierī entre os verbos de forma ativa e sentido passivo), § 410 (ablativo com ūtor, fruor, fungor, potior, vescor; 410.a, potīrī rērum)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 109 (definição de depoente), § 110 (depoentes transitivos e intransitivos: hortor vos; loquor), § 126 (particípios perfeitos de depoentes usados também em sentido passivo), § 127 (semidepoentes), § 128 (verbos de forma ativa e sentido passivo, entre eles fīō), § 129 (cēnātus, iūrātus), § 242 (fungor, fruor, vescor, ūtor, potior + ablativo), § 391 (Caesar milites hortatus castra movit, com a sigla CAES.; não localizada literalmente em César), § 392 nota 1 (só os depoentes têm particípio perfeito ativo)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 110 (definição de depoente; formas ativas conservadas; particípio perfeito ativo, "imitatus, tendo imitado", e, na observação, os particípios também passivos, como adeptus e expertus), n. 115 (os quatro semidepoentes), nn. 122–125 (listas de depoentes por conjugação), n. 126 (semidepoentes), n. 208 (frui, fungi, uti, vesci, potiri com ablativo; potiri rerum)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Mt 5,12; Jo 8,12; Sl 121,1 (122,1)', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Matthaeum', nota='frases autênticas da seção 6, conferidas na Wikisource latina (páginas "Evangelium Secundum Matthaeum", "Evangelium Secundum Joannem" e "Liber Psalmorum"); ortografia adaptada (ae por æ) e macrons acrescentados', tipo='dominio_publico'),
        referencia('Ab urbe condita, livro XXII, cap. 51', 'Tito Lívio', catalogo='the-latin-library', url='https://www.thelatinlibrary.com/livy/liv.22.shtml', nota='fala de Maarbal a Aníbal depois de Canas (Lívio 22.51.4), conferida no texto da Latin Library e nas edições Perseus de Weissenborn e Müller (Teubner, domínio público) e de Conway e Walters (Oxford, 1929), ambas com a frase na subseção 4; o capítulo segue a pontuação de Conway e Walters e da Latin Library ("vincere scis, Hannibal; victoria uti nescis"); Weissenborn e Müller pontuam com vírgula ("vincere scis, Hannibal, victoria uti nescis"), variante só de pontuação; ortografia adaptada (v por u consonantal) e macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Reconhecer um verbo depoente pela entrada de dicionário (<i>hortor, hortārī, hortātus sum</i>), sem confundi-lo com a passiva de um verbo comum.',
        'Conjugar depoentes das quatro conjugações e do tipo <i>patior</i> nos seis tempos do indicativo, reaproveitando as terminações passivas dos capítulos 23 e 24.',
        'Traduzir depoentes sempre na voz ativa, inclusive os transitivos com objeto no acusativo (<i>Dux mīlitēs hortātur</i>).',
        'Usar o ablativo com <i>ūtor, fruor, fungor, potior</i> e <i>vescor</i>, entendendo por que esse caso aparece.',
        'Conjugar os semidepoentes <i>audeō, gaudeō, soleō, fīdō</i> e reconhecer o particípio perfeito ativo dos depoentes (<i>hortātus</i>, "tendo exortado").',
    ],
    secoes=[
        ('Forma passiva, sentido ativo', f'''
<p>Nos capítulos 23 e 24 você aprendeu que <i>hortātur</i>, se viesse de um verbo comum, seria uma passiva: o sujeito <b>sofre</b> a ação ("é exortado"). Agora vem a surpresa. O latim tem algumas centenas de verbos que só existem com essas terminações passivas e que, apesar disso, têm sentido <b>ativo</b>: <i>hortātur</i> quer dizer "ele exorta", <i>sequitur</i> quer dizer "ele segue", <i>loquimur</i> quer dizer "nós falamos". Esses verbos se chamam <b>depoentes</b>. A definição das gramáticas é sempre a mesma: forma passiva, significado ativo (Bennett § 112; Allen e Greenough § 190; Ravizza n. 110).</p>
<p>O nome vem do particípio <i>dēpōnēns</i>, de <i>dēpōnere</i>, "pôr de lado, depor". O termo é dos gramáticos latinos tardios (Carísio, Diomedes, Prisciano; Lewis & Short, s.v. <i>dēpōnō</i>), e a explicação tradicional, registrada por Lewis & Short, é que esses verbos teriam "deposto" o sentido passivo e ficado só com o ativo. A explicação histórica é um pouco diferente, e ajuda a entendê-los: muitos depoentes exprimem uma ação que o sujeito pratica <b>em si mesmo</b> ou no seu próprio interesse, aquilo que a gramática grega chama de voz média (Allen e Greenough § 190.e). <i>Laetor</i> é "alegro-me"; <i>vescor</i>, "alimento-me"; <i>ūtor</i>, "sirvo-me de". O português faz algo parecido com os verbos pronominais: dizemos "eu <b>me</b> queixo", "ele <b>se</b> alegra", e ninguém entende "se alegra" como passiva. Em latim, essa nuance ficou na terminação: <i>queror</i>, "queixo-me"; <i>laetātur</i>, "alegra-se".</p>
<h3>Como reconhecer um depoente: a entrada de dicionário</h3>
<p>Você não precisa adivinhar se um verbo é depoente: o dicionário diz. Um verbo comum tem quatro partes principais (capítulo 13): <i>amō, amāre, amāvī, amātum</i>. Um depoente tem <b>três</b>, todas de forma passiva: a primeira pessoa do presente em <i>-or</i>, o infinitivo presente passivo e o perfeito composto com <i>sum</i>.</p>
{tabela(['Verbo comum (quatro partes)', 'Depoente (três partes)', 'O que cada parte é'], [
    ['amō', 'hort<b>or</b>', '1ª pessoa do singular do presente: <i>-ō</i> no verbo comum, <i>-or</i> no depoente'],
    ['amāre', 'hortā<b>rī</b>', 'infinitivo presente: ativo em <i>-re</i>, passivo em <i>-rī</i> (ou <i>-ī</i> na 3ª conjugação)'],
    ['amāvī', 'hortā<b>tus sum</b>', 'perfeito: ativo em <i>-ī</i>; no depoente, particípio + <i>sum</i>, como na passiva do capítulo 24'],
    ['amātum', '—', 'o supino ou particípio, que no depoente já aparece dentro da terceira parte'],
], 'A entrada de dicionário de um depoente', latim_cols=(0, 1))}
<p>A regra prática é, portanto, uma só: <b>se a entrada do dicionário começa em <i>-or</i> e termina em <i>sum</i>, o verbo é depoente</b>, e todas as suas formas pessoais, embora pareçam passivas, se traduzem pela ativa. Não existe *<i>hortō</i>, nem *<i>sequō</i>, nem *<i>loquit</i>: essas formas ativas simplesmente não existem, e quem procura *<i>hortō</i> no dicionário não encontra nada.</p>
{comparacao('Mesma terminação, sentido oposto', ['Forma', 'Verbo', 'É depoente?', 'Tradução'], [
    ['laud<b>ātur</b>', 'laudō, laudāre, laudāvī, laudātum', 'não (verbo comum)', 'ele <b>é elogiado</b> (passiva)'],
    ['hort<b>ātur</b>', 'hortor, hortārī, hortātus sum', 'sim', 'ele <b>exorta</b> (ativa)'],
    ['reg<b>itur</b>', 'regō, regere, rēxī, rēctum', 'não', 'ele <b>é governado</b>'],
    ['sequ<b>itur</b>', 'sequor, sequī, secūtus sum', 'sim', 'ele <b>segue</b>'],
    ['laudā<b>tus est</b>', 'laudō', 'não', 'ele <b>foi elogiado</b>'],
    ['hortā<b>tus est</b>', 'hortor', 'sim', 'ele <b>exortou</b>'],
])}
{dica('<b>Decore com a entrada completa.</b> Recite sempre as três partes juntas, como você faz com <i>rēx, rēgis</i>: <i>hortor, hortārī, hortātus sum</i>; <i>sequor, sequī, secūtus sum</i>. A terceira parte é indispensável, porque o particípio de muitos depoentes é imprevisível (<i>patior → passus</i>, <i>ūtor → ūsus</i>, <i>nāscor → nātus</i>). O português guarda vários desses particípios: <i>paixão</i> e <i>passivo</i> (de <i>passus</i>), <i>uso</i> (de <i>ūsus</i>), <i>nato</i> e <i>nação</i> (de <i>nātus</i>), <i>locução</i> (de <i>locūtus</i>), <i>consecutivo</i> (de <i>secūtus</i>).')}
'''),
        ('A conjugação: o que você já sabe da passiva', f'''
<p>A boa notícia é que um depoente não traz nenhuma terminação nova. Ele se conjuga exatamente como a passiva de um verbo comum da mesma conjugação: as terminações <i>-or, -ris, -tur, -mur, -minī, -ntur</i> do capítulo 23 no presente, no imperfeito e no futuro, e o particípio perfeito com <i>sum</i> do capítulo 24 no perfeito, no mais-que-perfeito e no futuro perfeito. Os modelos tradicionais são um verbo de cada conjugação, mais um da terceira em <i>-ior</i> (Bennett § 113 usa <i>mīror</i>, <i>vereor</i>, <i>sequor</i>, <i>largior</i> e <i>patior</i>; aqui o modelo da 1ª é <i>hortor</i> e o da 4ª é <i>partior</i>):</p>
{tabela(['Pessoa', 'hortor (1ª) · exortar', 'vereor (2ª) · temer', 'sequor (3ª) · seguir', 'partior (4ª) · repartir', 'patior (3ª em -ior) · sofrer'], [
    ['1ª sing.', 'hort<b>or</b>', 'vere<b>or</b>', 'sequ<b>or</b>', 'parti<b>or</b>', 'pati<b>or</b>'],
    ['2ª sing.', 'hortā<b>ris</b>', 'verē<b>ris</b>', 'sequ<b>eris</b>', 'partī<b>ris</b>', 'pat<b>eris</b>'],
    ['3ª sing.', 'hortā<b>tur</b>', 'verē<b>tur</b>', 'sequ<b>itur</b>', 'partī<b>tur</b>', 'pat<b>itur</b>'],
    ['1ª pl.', 'hortā<b>mur</b>', 'verē<b>mur</b>', 'sequ<b>imur</b>', 'partī<b>mur</b>', 'pat<b>imur</b>'],
    ['2ª pl.', 'hortā<b>minī</b>', 'verē<b>minī</b>', 'sequ<b>iminī</b>', 'partī<b>minī</b>', 'pat<b>iminī</b>'],
    ['3ª pl.', 'horta<b>ntur</b>', 'vere<b>ntur</b>', 'sequ<b>untur</b>', 'parti<b>untur</b>', 'pati<b>untur</b>'],
    ['Infinitivo', 'hortā<b>rī</b>', 'verē<b>rī</b>', 'sequ<b>ī</b>', 'partī<b>rī</b>', 'pat<b>ī</b>'],
], 'Presente do indicativo e infinitivo presente dos depoentes', latim_cols=(1, 2, 3, 4, 5))}
<p>Compare com o capítulo 23: <i>hortātur</i> se forma como <i>amātur</i>, <i>verētur</i> como <i>monētur</i>, <i>sequitur</i> como <i>regitur</i>, <i>partītur</i> como <i>audītur</i>, e <i>patitur, patiuntur</i> como <i>capitur, capiuntur</i>. O infinitivo também é o passivo: <i>-rī</i> na 1ª, 2ª e 4ª conjugações, só <i>-ī</i> na 3ª (<i>sequī</i>, <i>patī</i>, <i>loquī</i>, <i>ūtī</i>). Esse infinitivo curto da 3ª é a forma que mais engana: <i>sequī</i> não é um genitivo da 2ª declinação nem um perfeito em <i>-ī</i>; é "seguir".</p>
<h3>Os outros tempos</h3>
<p>Imperfeito e futuro seguem o mesmo princípio, e o perfectum é o do capítulo 24: particípio perfeito + <i>sum</i>, <i>eram</i>, <i>erō</i>, com o particípio concordando com o sujeito em gênero e número (<i>Rēgīna hortāta est</i>, "a rainha exortou"; <i>Mīlitēs secūtī sunt</i>, "os soldados seguiram").</p>
{tabela(['Tempo', 'hortor (1ª)', 'vereor (2ª)', 'sequor (3ª)', 'partior (4ª)', 'patior (3ª em -ior)'], [
    ['Imperfeito', 'hortā<b>bar</b>, hortā<b>bāris</b>, hortā<b>bātur</b>…', 'verē<b>bar</b>, verē<b>bāris</b>…', 'sequē<b>bar</b>, sequē<b>bāris</b>…', 'partiē<b>bar</b>, partiē<b>bāris</b>…', 'patiē<b>bar</b>, patiē<b>bāris</b>…'],
    ['Futuro', 'hortā<b>bor</b>, hortā<b>beris</b>, hortā<b>bitur</b>…', 'verē<b>bor</b>, verē<b>beris</b>…', 'sequ<b>ar</b>, sequ<b>ēris</b>, sequ<b>ētur</b>…', 'parti<b>ar</b>, parti<b>ēris</b>…', 'pati<b>ar</b>, pati<b>ēris</b>…'],
    ['Perfeito', 'hortātus <b>sum</b>', 'veritus <b>sum</b>', 'secūtus <b>sum</b>', 'partītus <b>sum</b>', 'passus <b>sum</b>'],
    ['Mais-que-perfeito', 'hortātus <b>eram</b>', 'veritus <b>eram</b>', 'secūtus <b>eram</b>', 'partītus <b>eram</b>', 'passus <b>eram</b>'],
    ['Futuro perfeito', 'hortātus <b>erō</b>', 'veritus <b>erō</b>', 'secūtus <b>erō</b>', 'partītus <b>erō</b>', 'passus <b>erō</b>'],
], 'Os seis tempos do indicativo (1ª pessoa, e o começo do imperfeito e do futuro)', latim_cols=(1, 2, 3, 4, 5))}
<p>Um detalhe de pronúncia separa dois tempos na 3ª conjugação: <i>sequ<b>e</b>ris</i>, com <i>e</i> breve, é presente ("tu segues"); <i>sequ<b>ē</b>ris</i>, com <i>ē</i> longo, é futuro ("tu seguirás"), como <i>regeris</i> e <i>regēris</i> na passiva comum. Nos textos sem macrons, só o contexto decide.</p>
<h3>Vocabulário: depoentes frequentes</h3>
<p>Mais da metade dos depoentes é da 1ª conjugação, e todos esses são regulares (Allen e Greenough § 191). Os da 3ª são menos numerosos, mas muito frequentes, e têm particípios que precisam ser aprendidos um a um.</p>
{tabela(['Conjugação', 'Entrada de dicionário', 'Significado'], [
    ['1ª', 'hortor, hortārī, hortātus sum', 'exortar, encorajar'],
    ['1ª', 'cōnor, cōnārī, cōnātus sum', 'tentar, esforçar-se'],
    ['1ª', 'mīror, mīrārī, mīrātus sum', 'admirar-se de, admirar'],
    ['1ª', 'laetor, laetārī, laetātus sum', 'alegrar-se'],
    ['1ª', 'moror, morārī, morātus sum', 'demorar(-se), deter'],
    ['1ª', 'precor, precārī, precātus sum', 'rogar, pedir em oração'],
    ['1ª', 'imitor, imitārī, imitātus sum', 'imitar'],
    ['2ª', 'vereor, verērī, veritus sum', 'temer; respeitar'],
    ['2ª', 'polliceor, pollicērī, pollicitus sum', 'prometer'],
    ['2ª', 'fateor, fatērī, fassus sum', 'confessar, reconhecer'],
    ['3ª', 'sequor, sequī, secūtus sum', 'seguir'],
    ['3ª', 'loquor, loquī, locūtus sum', 'falar'],
    ['3ª', 'queror, querī, questus sum', 'queixar-se, lamentar'],
    ['3ª', 'nāscor, nāscī, nātus sum', 'nascer'],
    ['3ª', 'proficīscor, proficīscī, profectus sum', 'partir, pôr-se a caminho'],
    ['3ª', 'ūtor, ūtī, ūsus sum', 'usar, servir-se de (+ ablativo)'],
    ['3ª em -ior', 'patior, patī, passus sum', 'sofrer, suportar; permitir'],
    ['3ª em -ior', 'morior, morī, mortuus sum', 'morrer'],
    ['3ª em -ior', 'ingredior, ingredī, ingressus sum', 'entrar, avançar'],
    ['4ª', 'partior, partīrī, partītus sum', 'repartir, dividir'],
    ['4ª', 'experior, experīrī, expertus sum', 'experimentar, pôr à prova'],
    ['4ª', 'mentior, mentīrī, mentītus sum', 'mentir'],
    ['4ª (com formas da 3ª)', 'orior, orīrī, ortus sum', 'levantar-se, surgir, nascer (o sol)'],
], 'Vocabulário do capítulo: depoentes por conjugação', latim_cols=(1,))}
{observacao('Orior, um depoente de duas conjugações', 'A entrada <i>orior, orīrī, ortus sum</i> parece da 4ª conjugação, e o infinitivo de fato é <i>orīrī</i>. Mas no presente o verbo segue em geral a 3ª: <i>oreris, oritur, orimur</i>, com <i>i</i> breve (Bennett § 123.VII; Allen e Greenough § 191). A frase <i>Sōl oritur</i>, "o sol nasce", é a que você mais vai encontrar; da mesma família vêm, em português, <i>oriente</i> (do particípio presente <i>oriēns</i>) e <i>origem</i> (de <i>orīgō</i>). Do mesmo modo, <i>morior</i> tem infinitivo <i>morī</i> no latim clássico; <i>morīrī</i> existe, mas é forma antiga e poética (Plauto, Ovídio; Lewis & Short, s.v. <i>morior</i>; Allen e Greenough § 191 a registra entre parênteses).')}
'''),
        ('Como ler e traduzir um depoente', f'''
<p>Traduzir um depoente pela ativa é fácil; o difícil é lembrar de fazê-lo quando o olho, treinado nos capítulos 23 e 24, vê <i>-tur</i> e pensa "passiva". O procedimento que evita o erro tem dois passos: diante de uma forma passiva, procure o verbo no dicionário <b>antes</b> de traduzir; se a entrada for em <i>-or</i>, traduza pela ativa e trate a frase como uma frase ativa qualquer. Isso tem uma consequência importante: muitos depoentes são <b>transitivos</b> e levam objeto direto no acusativo, coisa que uma passiva verdadeira nunca faz (Kennedy § 110 dá justamente <i>hortor vōs</i>, "exorto-vos").</p>
{diagrama_frase([('Dux', 'nominativo sing. · sujeito'), ('mīlitēs', 'acusativo pl. · objeto'), ('verbīs', 'ablativo pl. · meio'), ('hortātur', 'depoente, 3ª sing. · "exorta"')],
    '<i>Dux mīlitēs verbīs hortātur</i> = O general exorta os soldados com palavras. Se <i>hortātur</i> fosse passiva, <i>mīlitēs</i> não poderia ser objeto; como é depoente, a frase é ativa e o acusativo é o objeto.')}
<p>Repare que a frase acima não tem, nem pode ter, um agente da passiva com <i>ā</i> / <i>ab</i>: não há "por alguém" num verbo de sentido ativo. Um ablativo como <i>verbīs</i> é ablativo de meio (capítulo 21), "com palavras". Se você vir um depoente acompanhado de <i>ā</i> + ablativo, esse ablativo terá o valor normal da preposição (afastamento, origem): <i>Ā patre proficīscitur</i>, "parte de junto do pai".</p>
{exemplos([('Puerī magistrum <b>sequuntur</b>.', 'Os meninos seguem o professor. (<i>magistrum</i>, acusativo, é objeto: <i>sequor</i> é transitivo)'),
           ('Rōmānī Graecōs <b>imitābantur</b>.', 'Os romanos imitavam os gregos. (imperfeito de <i>imitor</i>)'),
           ('Fīlia mātrī multa <b>pollicita est</b>.', 'A filha prometeu muitas coisas à mãe. (perfeito; <i>pollicita</i>, feminino, concorda com <i>fīlia</i>)'),
           ('Cūr <b>quereris</b>? Nēmō tē <b>verētur</b>?', 'Por que te queixas? Ninguém te respeita? (<i>quereris</i>: presente da 3ª, <i>e</i> breve)'),
           ('Crās <b>proficīscēmur</b>.', 'Amanhã partiremos. (futuro da 3ª: <i>-ēmur</i>)'),
           ('Multī in bellō <b>mortuī sunt</b>.', 'Muitos morreram na guerra. (<i>mortuus sum</i>, de <i>morior</i>: "morri", não "fui morto")')])}
<h3>O particípio perfeito com sentido ativo</h3>
<p>O particípio perfeito de um verbo comum é passivo: <i>laudātus</i> é "elogiado", alguém que recebeu o elogio. O dos depoentes, como a forma pessoal de que faz parte, costuma ter <b>sentido ativo</b>: <i>hortātus</i> é "tendo exortado", <i>secūtus</i> é "tendo seguido", <i>locūtus</i> é "tendo falado" (Ravizza n. 110: "<i>imitatus</i>, tendo imitado"). É uma vantagem que os verbos comuns não têm: o latim não possui um particípio ativo do passado para <i>laudō</i> (não se pode dizer "tendo elogiado" numa palavra), mas possui para todos os depoentes (Kennedy § 392, nota 1). Kennedy (§ 391) traz, com a indicação "CAES.", uma frase que mostra o uso (não a localizamos literalmente nos comentários de César; pode ser exemplo adaptado):</p>
{exemplos([('Caesar mīlitēs hortātus castra mōvit.', 'César, tendo exortado os soldados, levantou o acampamento. (frase citada por Kennedy § 391; <i>hortātus</i> concorda com <i>Caesar</i> e tem objeto, <i>mīlitēs</i>)')])}
<p>Como o particípio é assunto do capítulo 29, aqui basta reconhecê-lo e traduzi-lo. Duas ressalvas. Alguns particípios de depoentes também se usam em sentido passivo, como <i>adeptus</i>, "obtido" ou "tendo obtido", e <i>expertus</i>, "experimentado" (Allen e Greenough § 190.b; Ravizza n. 110, observação; Kennedy § 126 dá outros, como <i>confessus</i> e <i>pollicitus</i>). E uns poucos verbos comuns têm, ao contrário, um particípio perfeito de sentido ativo: <i>cēnātus</i>, "tendo jantado", <i>prānsus</i>, "tendo almoçado", <i>pōtus</i>, "tendo bebido" (Bennett § 114.2).</p>
<h3>Formas de aparência ativa</h3>
<p>Os depoentes não são passivos em tudo. Algumas formas nominais do verbo que a passiva não possui, eles as tomam emprestadas da ativa, com forma ativa e sentido ativo (Bennett § 112.a; Allen e Greenough § 190.a, c): o particípio presente (<i>hortāns</i>, "exortando") e o particípio futuro (<i>hortātūrus</i>, "que vai exortar"), que você estudará no capítulo 29; o infinitivo futuro (<i>hortātūrus esse</i>, "haver de exortar"), no capítulo 27; o gerúndio (<i>hortandī</i>, "de exortar") e o supino (<i>hortātum</i>), no capítulo 31. O gerundivo (<i>hortandus</i>, "que deve ser exortado") é a única forma do depoente com sentido sempre passivo (Bennett § 112.b), também no capítulo 31. Por enquanto, basta saber que essas formas existem e que, ao encontrá-las, você não deve pensar que o verbo "deixou de ser depoente".</p>
{observacao('O imperativo dos depoentes', 'Você viu o imperativo dos verbos comuns no capítulo 22 (<i>laudā, laudāte</i>). O depoente usa as formas passivas correspondentes, com sentido ativo: no singular, terminação <i>-re</i>; no plural, <i>-minī</i>, igual à 2ª pessoa do plural do presente. <i>Hortāre!</i>, "exorta!"; <i>Verēre!</i>, "teme!"; <i>Sequere mē!</i>, "segue-me!"; <i>Loquiminī!</i>, "falai!". Cuidado: <i>sequere</i> parece um infinitivo ativo da 3ª conjugação, e não é; o infinitivo de <i>sequor</i> é <i>sequī</i>.')}
'''),
        ('Os cinco depoentes que pedem ablativo', f'''
<p>Cinco depoentes muito frequentes, e seus compostos, constroem o complemento no <b>ablativo</b>, e não no acusativo (Bennett § 218.1; Allen e Greenough § 410; Kennedy § 242; Ravizza n. 208): <i>ūtor</i>, "usar"; <i>fruor</i>, "desfrutar"; <i>fungor</i>, "desempenhar, cumprir"; <i>potior</i>, "apoderar-se de"; <i>vescor</i>, "alimentar-se de". Em português todos parecem transitivos ("uso a espada", "desfruto a paz"), e por isso o erro de pôr o complemento no acusativo é inevitável no começo.</p>
{tabela(['Entrada de dicionário', 'Significado', 'Exemplo', 'Tradução'], [
    ['ūtor, ūtī, ūsus sum', 'usar, servir-se de', 'Gladi<b>ō</b> ūtitur.', 'Usa a espada.'],
    ['fruor, fruī, frūctus sum', 'desfrutar, gozar de', 'Pāc<b>e</b> fruimur.', 'Desfrutamos a paz.'],
    ['fungor, fungī, fūnctus sum', 'desempenhar, cumprir', 'Officiō suō fūnctus est.', 'Cumpriu o seu dever.'],
    ['potior, potīrī, potītus sum', 'apoderar-se de', 'Rōmānī oppid<b>ō</b> potītī sunt.', 'Os romanos apoderaram-se da cidade.'],
    ['vescor, vescī (sem perfeito)', 'alimentar-se de, comer', 'Lact<b>e</b> et carn<b>e</b> vescuntur.', 'Alimentam-se de leite e de carne.'],
], 'Ūtor, fruor, fungor, potior, vescor + ablativo', latim_cols=(0, 2))}
<p>Por que o ablativo? Porque esses verbos guardam o sentido médio da seção 1, e o complemento deles é, na origem, um <b>ablativo de meio</b>, o mesmo do capítulo 21. As gramáticas dão a tradução literal: <i>ūtor gladiō</i> é "sirvo-me por meio da espada"; <i>vescor carne</i>, "alimento-me por meio de carne"; <i>fruor pāce</i>, "deleito-me com a paz"; <i>potior oppidō</i>, "torno-me poderoso por meio da cidade" (Bennett § 218.1; Allen e Greenough § 410, nota). Pensando assim, o ablativo deixa de ser uma exceção a decorar e passa a ser o caso esperado. O português, aliás, ainda diz "<b>servir-se de</b>", "<b>alimentar-se de</b>", "<b>apoderar-se de</b>", "<b>gozar de</b>": a preposição "de" é a pista.</p>
{observacao('Potīrī rērum', '<i>Potior</i> às vezes leva genitivo, e sempre na expressão <i>potīrī rērum</i>, "apoderar-se do poder, assumir o governo" (Bennett § 218.1.a; Allen e Greenough § 410.a; Ravizza n. 208). É uma expressão fixa; fora dela, use o ablativo.')}
<p>Tito Lívio põe na boca de Maarbal, comandante da cavalaria cartaginesa, uma frase célebre dita a Aníbal depois da vitória de Canas, quando o general hesitou em marchar imediatamente sobre Roma:</p>
{exemplos([('Vincere scīs, Hannibal; victōriā ūtī nescīs.', 'Vencer, sabes, Aníbal; usar a vitória, não sabes. (Lívio 22.51.4)')])}
<p><i>Scīs</i> e <i>nescīs</i> são "sabes" e "não sabes" (<i>sciō, scīre</i>; <i>nesciō, nescīre</i>, 4ª conjugação), e cada um tem como complemento um infinitivo: <i>vincere</i>, ativo da 3ª conjugação, e <i>ūtī</i>, o infinitivo do depoente <i>ūtor</i>. O complemento de <i>ūtī</i> está no ablativo, <i>victōriā</i>: "servir-se da vitória". A frase toda é construída sobre o contraste das duas metades, e o leitor só a entende se reconhecer <i>ūtī</i> (curto como todo infinitivo de depoente da 3ª) e se esperar o ablativo.</p>
{dica('<b>Como lembrar os cinco.</b> Muitos estudantes decoram a sequência na ordem das gramáticas, <i>ūtor, fruor, fungor, potior, vescor</i>, como se fosse um verso. Ao encontrar qualquer um deles numa frase, procure logo um ablativo por perto: ele é o complemento do verbo, não um adjunto solto.')}
'''),
        ('Os semidepoentes', f'''
<p>Entre os verbos comuns e os depoentes há um pequeno grupo misto: os <b>semidepoentes</b>, que são ativos nos tempos do infectum e depoentes nos tempos do perfectum (Bennett § 114.1; Allen e Greenough § 192; Kennedy § 127; Ravizza n. 115). O sentido é ativo do começo ao fim; o que muda é só a forma: o presente é <i>audeō</i>, "ouso", e o perfeito é <i>ausus sum</i>, "ousei". A explicação histórica é que esses verbos não tinham um perfeito ativo próprio, e a língua o supriu com o particípio e <i>sum</i>, como num depoente (Allen e Greenough § 192). São quatro:</p>
{tabela(['Entrada de dicionário', 'Significado', 'Infectum (forma ativa)', 'Perfectum (forma depoente)'], [
    ['audeō, audēre, ausus sum', 'ousar, atrever-se', 'aude<b>ō</b>, audē<b>bam</b>, audē<b>bō</b>', 'ausus <b>sum</b>, ausus <b>eram</b>, ausus <b>erō</b>'],
    ['gaudeō, gaudēre, gāvīsus sum', 'alegrar-se', 'gaude<b>ō</b>, gaudē<b>bam</b>, gaudē<b>bō</b>', 'gāvīsus <b>sum</b>, gāvīsus <b>eram</b>, gāvīsus <b>erō</b>'],
    ['soleō, solēre, solitus sum', 'costumar, ter o hábito de', 'sole<b>ō</b>, solē<b>bam</b>, solē<b>bō</b>', 'solitus <b>sum</b>, solitus <b>eram</b>, solitus <b>erō</b>'],
    ['fīdō, fīdere, fīsus sum', 'confiar (em)', 'fīd<b>ō</b>, fīdē<b>bam</b>, fīd<b>am</b>', 'fīsus <b>sum</b>, fīsus <b>eram</b>, fīsus <b>erō</b>'],
], 'Os quatro semidepoentes', latim_cols=(0, 2, 3))}
<p>Três desses verbos são da 2ª conjugação e se conjugam no infectum exatamente como <i>moneō</i>; <i>fīdō</i> é da 3ª, como <i>regō</i>, e tem os compostos <i>cōnfīdō</i>, "confiar", e <i>diffīdō</i>, "desconfiar". <i>Audeō</i> e <i>soleō</i> costumam vir com um infinitivo: <i>Nōn audeō loquī</i>, "não ouso falar"; <i>Māne surgere solet</i>, "costuma levantar-se cedo". <i>Fīdō</i> e <i>cōnfīdō</i> levam dativo da pessoa em quem se confia (Bennett § 219.1.a): <i>Amīcīs cōnfīdō</i>, "confio nos amigos". No perfectum, como em qualquer depoente, o particípio concorda com o sujeito: <i>Puella gāvīsa est</i>, "a menina alegrou-se"; <i>Mīlitēs nōn ausī sunt</i>, "os soldados não ousaram".</p>
{exemplos([('Nautae in marī nāvigāre <b>audent</b>.', 'Os marinheiros ousam navegar no mar. (presente, forma ativa)'),
           ('Nēmō rēgī resistere <b>ausus est</b>.', 'Ninguém ousou resistir ao rei. (perfeito, forma depoente; <i>nēmō</i>, ninguém; <i>resistō</i> + dativo)'),
           ('Avus in hortō ambulāre <b>solēbat</b>.', 'O avô costumava passear no jardim. (imperfeito, forma ativa)'),
           ('Māter fīliī victōriā <b>gāvīsa est</b>.', 'A mãe alegrou-se com a vitória do filho. (perfeito; <i>victōriā</i>, ablativo de causa)')])}
{observacao('E fīō?', 'Há também o movimento contrário: verbos de forma ativa e sentido passivo, que a gramática de Allen e Greenough chama de "neutros passivos" (§ 192.b) e Kennedy de "quase-passivos" (§ 128). O principal é <i>fīō</i>, "sou feito, torno-me", que serve de passiva a <i>faciō</i>: <i>fit</i> é "é feito, acontece", mas <i>factus est</i>, no perfeito, já tem forma passiva. Ele é irregular e será estudado com os outros verbos irregulares no capítulo 26.')}
<p>Bennett (§ 114.3) registra ainda um caso inverso: <i>revertor</i>, "voltar", é depoente no infectum (<i>revertitur</i>, "volta") mas, na prosa clássica, faz o perfeito ativo <i>revertī</i>, "voltei". É raro o bastante para ficar como curiosidade; o dicionário o indica.</p>
'''),
        ('Análise gramatical: frases autênticas', f'''
<p>O Sermão da Montanha, no Evangelho de Mateus, termina as bem-aventuranças com uma frase em que um depoente tem objeto no acusativo e um semidepoente aparece no imperativo:</p>
{exemplos([('Gaudēte, et exsultāte, quoniam mercēs vestra cōpiōsa est in caelīs. Sīc enim persecūtī sunt prophētās, quī fuērunt ante vōs.', 'Alegrai-vos e exultai, porque a vossa recompensa é grande nos céus. Pois assim perseguiram os profetas que existiram antes de vós. (Mt 5,12, Vulgata Clementina)')])}
<p>A primeira palavra, <i>gaudēte</i>, é o imperativo plural de <i>gaudeō</i>, com forma ativa, porque o infectum do semidepoente é ativo. A segunda frase é a que interessa analisar palavra a palavra:</p>
{analise('Mt 5,12b, palavra a palavra', [
    ('Sīc', 'sīc (advérbio), assim', 'invariável', 'modo: "assim", do mesmo modo'),
    ('enim', 'enim (conjunção), pois', 'invariável, posposta à primeira palavra', 'explica a frase anterior'),
    ('persecūtī sunt', 'persequor, persequī, persecūtus sum, perseguir (depoente, composto de <i>sequor</i>)', 'perfeito do indicativo, 3ª pl.; particípio no nominativo pl. masculino', 'verbo: "perseguiram" (ativo), sujeito implícito "eles"'),
    ('prophētās', 'prophēta, -ae (m.), profeta', 'acusativo plural, 1ª declinação (masculino, como <i>nauta</i>)', 'objeto direto de <i>persecūtī sunt</i>'),
    ('quī', 'quī, quae, quod, que (relativo)', 'nominativo plural masculino', 'sujeito da oração relativa; antecedente <i>prophētās</i>'),
    ('fuērunt', 'sum, esse, fuī, ser, estar, existir', 'perfeito do indicativo, 3ª pl.', 'verbo da relativa: "existiram, viveram"'),
    ('ante', 'ante (preposição + acusativo), antes de', 'invariável', 'tempo: "antes de"'),
    ('vōs', 'vōs, vestrum (pronome pessoal), vós', 'acusativo plural (regido por <i>ante</i>)', '"antes de vós"'),
])}
<p>O ponto central é <i>persecūtī sunt prophētās</i>. Quem lê <i>persecūtī sunt</i> como passiva traduz "foram perseguidos" e fica sem saber o que fazer com o acusativo <i>prophētās</i>; quem reconhece o depoente lê "perseguiram os profetas", e o acusativo é simplesmente o objeto. O particípio <i>persecūtī</i> está no masculino plural porque concorda com o sujeito implícito ("eles", os perseguidores), exatamente como na passiva do capítulo 24. O composto <i>per-sequor</i> segue o simples <i>sequor</i> em tudo; o português herdou o verbo com o mesmo prefixo: <i>perseguir</i>.</p>
<p>Duas frases ainda mais curtas mostram outros depoentes num contexto autêntico. No Evangelho de João, Jesus diz:</p>
{exemplos([('Ego sum lūx mundī: quī <b>sequitur</b> mē, nōn ambulat in tenebrīs.', 'Eu sou a luz do mundo: quem me segue não anda nas trevas. (Jo 8,12; <i>sequitur</i>, presente de <i>sequor</i>, com objeto <i>mē</i>)'),
           ('<b>Laetātus sum</b> in hīs quae dicta sunt mihi.', 'Alegrei-me com as coisas que me foram ditas. (Sl 121,1 (122,1), na numeração da Vulgata; <i>laetātus sum</i>, perfeito de <i>laetor</i>, ao lado de <i>dicta sunt</i>, passiva verdadeira de <i>dīcō</i>)')])}
<p>A frase do Salmo é um bom teste: tem duas formas com particípio e <i>sum</i>, lado a lado. <i>Dicta sunt</i> vem de <i>dīcō, dīcere, dīxī, dictum</i>, verbo comum: é passiva, "foram ditas". <i>Laetātus sum</i> vem de <i>laetor, laetārī, laetātus sum</i>, depoente: é ativa, "alegrei-me". A forma é a mesma; o dicionário é que decide.</p>
<h3>Resumo</h3>
<ul>
<li>Depoente = forma passiva, sentido ativo. A entrada tem três partes: <i>hortor, hortārī, hortātus sum</i>. Não existem formas pessoais ativas (*<i>hortō</i>).</li>
<li>Conjugação: as terminações passivas dos capítulos 23 e 24, sem nada de novo. Infinitivo presente em <i>-rī</i> (1ª, 2ª, 4ª) ou <i>-ī</i> (3ª: <i>sequī, patī, ūtī</i>).</li>
<li>Tradução sempre ativa; muitos depoentes são transitivos e levam acusativo (<i>Dux mīlitēs hortātur</i>); não há agente da passiva.</li>
<li>Particípio perfeito em geral ativo: <i>hortātus</i>, "tendo exortado". Têm forma ativa: particípios presente e futuro, infinitivo futuro, gerúndio e supino (capítulos 27, 29 e 31).</li>
<li><i>Ūtor, fruor, fungor, potior, vescor</i> + ablativo (originalmente ablativo de meio).</li>
<li>Semidepoentes: ativos no infectum, depoentes no perfectum: <i>audeō/ausus sum, gaudeō/gāvīsus sum, soleō/solitus sum, fīdō/fīsus sum</i>.</li>
</ul>
<p>No próximo capítulo, os verbos irregulares (<i>sum, possum, volō, nōlō, mālō, eō, ferō, fīō</i>) completam a morfologia do verbo no indicativo.</p>
'''),
    ],
    erros_comuns=[
        ('Traduzir o depoente pela passiva: <i>hortātur</i> = *"é exortado"; <i>locūtus est</i> = *"foi falado".', 'A forma é passiva, mas o sentido é ativo: "exorta", "falou". Diante de qualquer forma passiva, confira a entrada no dicionário; se ela começar em <i>-or</i> e terminar em <i>sum</i>, traduza pela ativa.'),
        ('Inventar formas ativas: *<i>sequō</i>, *<i>loquit</i>, *<i>hortāre</i> como infinitivo.', 'Os depoentes não têm formas pessoais ativas. O infinitivo presente é passivo na forma: <i>hortārī</i>, <i>sequī</i>, <i>loquī</i>. (<i>Hortāre</i> existe, mas é imperativo singular ou 2ª pessoa alternativa do presente, não infinitivo.)'),
        ('Pôr o complemento de <i>ūtor, fruor, fungor, potior, vescor</i> no acusativo: *<i>ūtitur gladium</i>.', 'Esses cinco verbos pedem ablativo, um antigo ablativo de meio: <i>gladiō ūtitur</i>, "serve-se da espada". O "de" do português ("servir-se de", "gozar de") ajuda a lembrar.'),
        ('Ler <i>sequēris</i> (futuro) como presente, ou <i>sequeris</i> (presente) como futuro.', 'Na 3ª conjugação, o presente tem <i>e</i> breve (<i>sequeris</i>, "segues") e o futuro tem <i>ē</i> longo (<i>sequēris</i>, "seguirás"), como na passiva comum (<i>regeris</i> × <i>regēris</i>). Sem macrons, decida pelo contexto e pelas outras pessoas (<i>sequitur</i> × <i>sequētur</i>).'),
        ('Esquecer a concordância do particípio no perfeito: *<i>Rēgīna hortātus est</i>; *<i>Mīlitēs secūtus est</i>.', 'O perfectum dos depoentes funciona como o da passiva do capítulo 24: o particípio concorda com o sujeito em gênero e número. <i>Rēgīna hortāta est</i>; <i>Mīlitēs secūtī sunt</i>.'),
        ('Conjugar semidepoentes como verbos comuns no perfeito: *<i>audēvit</i>, *<i>gauduit</i>; ou traduzir <i>gāvīsus sum</i> como passiva.', 'Os semidepoentes não têm perfeito ativo. O perfeito é <i>ausus sum</i>, "ousei"; <i>gāvīsus sum</i>, "alegrei-me"; <i>solitus sum</i>, "costumei"; <i>fīsus sum</i>, "confiei", sempre com sentido ativo.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Depoente ou passiva?',
            'Leia e analise, na ordem latina: <i lang="la">Mīlitēs ā duce laudātī sunt; deinde hostēs secūtī sunt.</i> Vocabulário: <i>mīles, mīlitis</i> (m.), soldado; <i>dux, ducis</i> (m.), general; <i>hostis, hostis</i> (m.), inimigo; <i>deinde</i>, depois; <i>laudō, laudāre, laudāvī, laudātum</i>, elogiar; <i>sequor, sequī, secūtus sum</i>, seguir.', [
            ('As duas orações terminam com particípio + <i>sunt</i>. Basta isso para traduzir?', 'Não. A forma é a mesma (perfeito com particípio no masculino plural), mas é preciso saber de que verbo cada particípio vem. <i>Laudātī</i> vem de <i>laudō</i>, verbo comum; <i>secūtī</i> vem de <i>sequor</i>, depoente.'),
            ('Como se traduz <i>Mīlitēs ā duce laudātī sunt</i>?', '<i>Laudō</i> é verbo comum, então <i>laudātī sunt</i> é passiva verdadeira, "foram elogiados". <i>Mīlitēs</i> é o sujeito paciente e <i>ā duce</i> é o agente da passiva (capítulo 23): "Os soldados foram elogiados pelo general."'),
            ('E <i>hostēs</i>, na segunda oração?', 'Nominativo ou acusativo plural da 3ª declinação. <i>Secūtī sunt</i> é depoente, logo ativo e transitivo ("seguiram"); o sujeito continua sendo os soldados (o particípio masculino plural concorda com eles), e <i>hostēs</i> é o objeto: "seguiram os inimigos".'),
            ('Por que não traduzir "os inimigos foram seguidos"?', 'Porque isso exigiria uma passiva de <i>sequor</i>, que não existe: <i>secūtī sunt</i> só pode ser ativo. Se <i>hostēs</i> fosse o sujeito, a frase estaria dizendo "os inimigos seguiram", e o contexto (os soldados elogiados avançam) torna mais natural manter o mesmo sujeito.'),
            ('Monte a tradução.', '"Os soldados foram elogiados pelo general; depois, seguiram os inimigos."'),
        ], 'Conclusão: particípio + <i>sum</i> pode ser passiva (verbo comum) ou ativa (depoente). O dicionário decide, e o resto da frase (agente com <i>ā</i> / <i>ab</i>, ou objeto no acusativo) confirma a leitura.'),
        pratica_guiada('Prática guiada 2 · Um depoente com ablativo',
            'Traduza para o latim: "Os agricultores usam os bois e desfrutam a paz." Vocabulário: <i>agricola, -ae</i> (m.), agricultor; <i>bōs, bovis</i> (m.), boi (dat./abl. pl. <i>bōbus</i> ou <i>būbus</i>); <i>pāx, pācis</i> (f.), paz; <i>ūtor</i>; <i>fruor</i>.', [
            ('Que forma de <i>ūtor</i> e de <i>fruor</i> você precisa?', 'Presente, 3ª do plural: <i>ūtuntur</i> e <i>fruuntur</i> (3ª conjugação, como <i>sequuntur</i>).'),
            ('Em que caso vão "os bois" e "a paz"?', 'No ablativo, porque são complementos de <i>ūtor</i> e de <i>fruor</i>: <i>bōbus</i> (ablativo plural irregular de <i>bōs</i>) e <i>pāce</i> (ablativo singular).'),
            ('Monte a frase.', '<i>Agricolae bōbus ūtuntur et pāce fruuntur.</i> O sujeito no nominativo plural, os dois complementos no ablativo, cada verbo no fim do seu membro.'),
        ]),
    ],
    exercicios=[
        exercicio('Exercício 1 · Depoente ou passiva verdadeira?', 'Para cada forma, diga se vem de um depoente ou de um verbo comum (as entradas estão entre parênteses) e traduza.', [
            ('<i>laudātur</i> (<i>laudō, laudāre, laudāvī, laudātum</i>)', 'Verbo comum: passiva, "é elogiado".'),
            ('<i>mīrātur</i> (<i>mīror, mīrārī, mīrātus sum</i>)', 'Depoente: "admira-se, admira".'),
            ('<i>loquimur</i> (<i>loquor, loquī, locūtus sum</i>)', 'Depoente: "falamos".'),
            ('<i>regēbantur</i> (<i>regō, regere, rēxī, rēctum</i>)', 'Verbo comum: passiva, imperfeito, "eram governados".'),
            ('<i>profectī sunt</i> (<i>proficīscor, proficīscī, profectus sum</i>)', 'Depoente: perfeito, "partiram".'),
            ('<i>missī sunt</i> (<i>mittō, mittere, mīsī, missum</i>)', 'Verbo comum: passiva do perfeito, "foram enviados".'),
            ('<i>cōnābitur</i> (<i>cōnor, cōnārī, cōnātus sum</i>)', 'Depoente: futuro, "tentará".'),
            ('<i>patiuntur</i> (<i>patior, patī, passus sum</i>)', 'Depoente: presente, "sofrem, suportam".'),
        ]),
        exercicio('Exercício 2 · Forme o que se pede', 'Escreva a forma pedida e traduza.', [
            ('<i>hortor</i>: 3ª pl. do futuro', '<i>hortābuntur</i>, "exortarão" (1ª conjugação: <i>-bor, -beris, -bitur, -bimur, -biminī, -buntur</i>).'),
            ('<i>sequor</i>: 3ª pl. do presente', '<i>sequuntur</i>, "seguem" (3ª conjugação: <i>-untur</i>).'),
            ('<i>vereor</i>: 1ª pl. do imperfeito', '<i>verēbāmur</i>, "temíamos".'),
            ('<i>loquor</i>: 2ª sing. do presente e do futuro', 'Presente <i>loqueris</i> (<i>e</i> breve), "falas"; futuro <i>loquēris</i> (<i>ē</i> longo), "falarás".'),
            ('<i>partior</i>: 3ª sing. do futuro', '<i>partiētur</i>, "repartirá" (4ª conjugação: <i>-iar, -iēris, -iētur</i>).'),
            ('<i>patior</i>: infinitivo presente', '<i>patī</i>, "sofrer" (3ª conjugação: só <i>-ī</i>).'),
            ('<i>morior</i>: 3ª sing. do perfeito, sujeito feminino', '<i>mortua est</i>, "morreu" (particípio irregular <i>mortuus</i>, no feminino para concordar com o sujeito).'),
            ('<i>polliceor</i>: 1ª sing. do mais-que-perfeito, sujeito masculino', '<i>pollicitus eram</i>, "eu tinha prometido".'),
        ]),
        exercicio('Exercício 3 · Ūtor, fruor, fungor, potior, vescor', 'Complete com o nome entre parênteses no caso correto e traduza.', [
            ('<i>Puerī ___ ūtuntur.</i> (<i>librī</i>, plural)', '<i>librīs</i>: <i>Puerī librīs ūtuntur</i>, "os meninos usam os livros". Ablativo plural, porque <i>ūtor</i> pede ablativo.'),
            ('<i>Senex ___ fruitur.</i> (<i>ōtium, -ī</i>, n., descanso)', '<i>ōtiō</i>: "o velho desfruta o descanso".'),
            ('<i>Cōnsul ___ suō fūnctus est.</i> (<i>officium, -ī</i>, dever)', '<i>officiō</i>: "o cônsul cumpriu o seu dever". Ablativo singular; <i>suō</i> concorda com ele.'),
            ('<i>Hostēs ___ potītī sunt.</i> (<i>castra, -ōrum</i>, n. pl., acampamento)', '<i>castrīs</i>: "os inimigos apoderaram-se do acampamento".'),
            ('<i>Lupī ___ vescuntur.</i> (<i>carō, carnis</i>, f., carne)', '<i>carne</i>: "os lobos alimentam-se de carne".'),
        ]),
        exercicio('Exercício 4 · Semidepoentes', 'Traduza e diga se a forma do verbo é ativa ou depoente.', [
            ('<i>Puer in silvam intrāre nōn audet.</i>', '"O menino não ousa entrar na floresta." Presente: forma ativa (infectum).'),
            ('<i>Puer in silvam intrāre nōn ausus est.</i>', '"O menino não ousou entrar na floresta." Perfeito: forma depoente (<i>ausus est</i>), sentido ativo.'),
            ('<i>Cīvēs victōriā gāvīsī sunt.</i>', '"Os cidadãos alegraram-se com a vitória." Perfeito de <i>gaudeō</i>, forma depoente; <i>gāvīsī</i> no plural concorda com <i>cīvēs</i>; <i>victōriā</i>, ablativo de causa, como no exemplo da seção 5.'),
            ('<i>Agricola prīmā lūce surgere solet.</i>', '"O agricultor costuma levantar-se ao raiar do dia." <i>Solet</i>: presente, forma ativa, com infinitivo.'),
            ('<i>Mīlitēs ducī suō fīsī sunt.</i>', '"Os soldados confiaram no seu general." Perfeito de <i>fīdō</i>, forma depoente; dativo da pessoa, <i>ducī</i>.'),
        ]),
        exercicio('Exercício 5 · Traduza lendo em ordem', 'Identifique cada depoente antes de traduzir. Vocabulário: <i>Rōmānus, -a, -um</i>, romano; <i>Graecus, -a, -um</i>, grego; <i>verbum, -ī</i>, palavra; <i>urbs, urbis</i> (f.), cidade; <i>lingua, -ae</i>, língua.', [
            ('<i>Rōmānī multōs annōs Graecōs imitātī sunt.</i>', '"Os romanos imitaram os gregos durante muitos anos." <i>Imitātī sunt</i>: perfeito de <i>imitor</i>, ativo, com objeto <i>Graecōs</i>; <i>multōs annōs</i>, acusativo de duração (capítulo 19).'),
            ('<i>Puella Latīnē loquī cōnātur.</i>', '"A menina tenta falar latim." <i>Cōnātur</i> (presente de <i>cōnor</i>) com o infinitivo <i>loquī</i> (de <i>loquor</i>); <i>Latīnē</i>, advérbio, "em latim".'),
            ('<i>Dux mīlitēs paucīs verbīs hortātus est.</i>', '"O general exortou os soldados com poucas palavras." Perfeito de <i>hortor</i>; <i>paucīs verbīs</i>, ablativo de meio.'),
            ('<i>Crās ex urbe proficīscēmur.</i>', '"Amanhã partiremos da cidade." Futuro de <i>proficīscor</i> (3ª: <i>-ēmur</i>).'),
            ('<i>Cūr semper quereris?</i>', '"Por que te queixas sempre?" <i>Quereris</i>: presente, 2ª do singular, de <i>queror</i> (com <i>e</i> breve; o futuro seria <i>querēris</i>).'),
            ('<i>Nautae nāvibus ūtēbantur.</i>', '"Os marinheiros usavam os navios." Imperfeito de <i>ūtor</i>, com ablativo <i>nāvibus</i>.'),
        ]),
        exercicio('Exercício 6 · Do português para o latim', 'Traduza usando o vocabulário do capítulo.', [
            ('O menino segue o pai.', '<i>Puer patrem sequitur.</i> <i>Sequor</i> é depoente e transitivo: forma passiva, objeto no acusativo.'),
            ('As meninas falaram com a mãe.', '<i>Puellae cum mātre locūtae sunt.</i> Perfeito de <i>loquor</i>; <i>locūtae</i>, feminino plural, concorda com <i>puellae</i>.'),
            ('Os soldados não temem os inimigos.', '<i>Mīlitēs hostēs nōn verentur.</i> Presente de <i>vereor</i>, 3ª do plural.'),
            ('Usaremos as palavras dos poetas.', '<i>Verbīs poētārum ūtēmur.</i> Futuro de <i>ūtor</i> (3ª: <i>-ēmur</i>), com ablativo <i>verbīs</i>.'),
            ('A rainha ousou falar.', '<i>Rēgīna loquī ausa est.</i> Perfeito do semidepoente <i>audeō</i>, no feminino, com o infinitivo do depoente <i>loquor</i>.'),
        ]),
    ],
    leituras=['d-ooge-latin-for-beginners', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'phaedrus-fabulae-aesopiae', 'nepos-vita-hannibalis', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'bennett-new-latin-grammar'],
    leituras_nota='Latin for Beginners, de D\'Ooge, e a Familia Romana, de Ørberg, apresentam os depoentes depois da passiva e oferecem muita prática de leitura com eles. As fábulas de Fedro e a vida de Aníbal de Cornélio Nepos são os primeiros textos autênticos em que você vai encontrar depoentes a cada poucas linhas (<i>loquor, sequor, ūtor, proficīscor, morior</i>); a vida de Aníbal é também o contexto da frase de Lívio analisada na seção 4. Na Vulgata, releia Mateus 5,1–12 e João 8,12–20 procurando os depoentes e os semidepoentes. Para consulta, Bennett traz os paradigmas completos no § 113 e os semidepoentes no § 114.',
)
