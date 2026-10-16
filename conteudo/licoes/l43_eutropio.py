from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Texto latino: Eutrópio, Breviarium ab urbe condita I, 1–2, conferido na The Latin Library (eutropius1.shtml)
# e na Wikisource latina (Breviarium historiae romanae/Liber I, que declara a Latin Library como fonte),
# e comparado com a edição escolar de J. C. Hazzard (New York: American Book Company, c1898, archive.org).
# Auditoria 2026-10-15: I, 1–2 idêntico nas palavras a F. Rühl (Teubner, 1887); variantes de H. Droysen (MGH AA II, 1879)
# registradas numa observação na seção 2.
# Macrons acrescentados; frases numeradas para o comentário.
TEXTO = [
    ('1.1', 'Rōmānum imperium, quō neque ab exōrdiō ūllum ferē minus neque incrēmentīs tōtō orbe amplius hūmāna potest memoria recordārī, ā Rōmulō exōrdium habet, quī Rēae Silviae, Vestālis virginis, fīlius et, quantum putātus est, Mārtis cum Remō frātre ūnō partū ēditus est.'),
    ('1.2', 'Is cum inter pāstōrēs latrōcinārētur, decem et octō annōs nātus urbem exiguam in Palātīnō monte cōnstituit XI Kal. Māiās, Olympiadis sextae annō tertiō, post Trōiae excidium, ut quī plūrimum minimumque trādunt, annō trecentēsimō nōnāgēsimō quārtō.'),
    ('2.1', 'Conditā cīvitāte, quam ex nōmine suō Rōmam vocāvit, haec ferē ēgit.'),
    ('2.2', 'Multitūdinem fīnitimōrum in cīvitātem recēpit, centum ex seniōribus lēgit, quōrum cōnsiliō omnia ageret, quōs senātōrēs nōmināvit propter senectūtem.'),
    ('2.3', 'Tum, cum uxōrēs ipse et populus suus nōn habērent, invītāvit ad spectāculum lūdōrum vīcīnās urbī Rōmae nātiōnēs atque eārum virginēs rapuit.'),
    ('2.4', 'Commōtīs bellīs propter raptārum iniūriam Caenīnēnsēs vīcit, Antemnātēs, Crustumīnōs, Sabīnōs, Fīdēnātēs, Vēientēs.'),
    ('2.5', 'Haec omnia oppida urbem cingunt.'),
    ('2.6', 'Et cum ortā subitō tempestāte nōn compāruisset, annō rēgnī trīcēsimō septimō ad deōs trānsīsse crēditus est et cōnsecrātus.'),
    ('2.7', 'Deinde Rōmae per quīnōs diēs senātōrēs imperāvērunt et hīs rēgnantibus annus ūnus complētus est.'),
]

LICAO = dict(
    slug='43-eutropio', titulo='Eutrópio: a fundação de Roma',
    titulo_latim='Eutropius', tempo='80 min',
    resumo='Leitura comentada dos dois primeiros capítulos do Breviário de Eutrópio: o nascimento de Rômulo e Remo, a fundação de Roma, o rapto das sabinas e o desaparecimento de Rômulo. A prosa histórica simples, a passiva do perfectum na narrativa, os nomes próprios, as datas (ab urbe conditā, calendas, olimpíadas) e os números, com glosas para as construções que vêm de capítulos posteriores ao pré-requisito.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['Eutrópio', 'Breviarium ab urbe condita', 'historiografia latina', 'Rômulo e Remo', 'fundação de Roma', 'rapto das sabinas', 'passiva do perfectum em texto', 'construção pessoal com crēditus est', 'ab urbe conditā', 'calendas, nonas e idos', 'olimpíadas', 'numerais ordinais e distributivos', 'ablativo de tempo', 'locativo Rōmae', 'idade: annōs nātus', 'ablativo absoluto (glosa)', 'cum com subjuntivo (glosa)', 'relativa de finalidade (glosa)', 'leitura comentada'],
    prerequisitos=dict(texto='Capítulos 22 e 24: a sintaxe da oração simples (sujeito, predicado, objetos, adjuntos, concordâncias) e a passiva do perfectum, que é a forma verbal característica deste texto (<i>ēditus est</i>, <i>crēditus est</i>, <i>complētus est</i>). Os numerais (capítulo 19), o ablativo absoluto (capítulo 30), o subjuntivo (capítulos 32–34) e o capítulo 42, sobre Fedro, ajudam; o que vem deles está glosado aqui.',
                       licoes=['22-imperativo-e-oracao-simples', '24-a-passiva-do-perfectum']),
    referencias=[
        referencia('Eutropius, Breviarium ab urbe condita, livro I (The Latin Library)', 'Eutrópio', catalogo='eutropius-breviarium-ab-urbe-condita', url='https://www.thelatinlibrary.com/eutropius/eutropius1.shtml', nota='texto de I, 1–2 e I, 18 (anno trecentesimo et altero ab urbe condita) conferido na The Latin Library e na Wikisource latina (Breviarium historiae romanae/Liber I, que declara a Latin Library como fonte); a página não indica a edição impressa de base, mas I, 1–2 coincide palavra por palavra com Rühl (1887); macrons acrescentados', tipo='dominio_publico'),
        referencia('Eutropi Breviarium ab urbe condita, recognovit F. Ruehl (Leipzig: Teubner, 1887)', 'Franz Rühl (ed.)', url='https://archive.org/details/bub_gb_KRfgAAAAMAAJ', nota='edição crítica em domínio público; I, 1–2 conferido no scan: mesmas palavras da The Latin Library, só pontuação diferente', tipo='dominio_publico'),
        referencia('Eutropi Breviarium ab urbe condita, recensuit H. Droysen (MGH, Auctores antiquissimi II, Berlim: Weidmann, 1879)', 'Hans Droysen (ed.)', url='https://archive.org/details/cuaeutropibreviar00eutr', nota='edição crítica em domínio público, com aparato; I, 1–2 conferido no scan: diferenças em 2.3 (sem Tum; urbis Romae), 2.6 (sem et consecratus) e 2.7 (unus annus), registradas no capítulo', tipo='dominio_publico'),
        referencia('Eutropius, ed. J. C. Hazzard (New York: American Book Company, c1898)', 'J. C. Hazzard (ed.)', url='https://archive.org/details/eutropius00eutrrich', nota='edição escolar em domínio público, usada para comparar I, 1–2: mesmo texto, mas sem a relativa quō neque … recordārī e sem ut quī plūrimum minimumque trādunt; grafia Rheae', tipo='dominio_publico'),
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 79 (tabela de cardinais, ordinais e distributivos: trīcēsimus, nōnāgēsimus, trecentēsimus, quīnī), § 81.1 (compostos com et: sex et trīgintā), § 81.4 (distributivos: "tantos cada um"), § 102 (passiva do perfectum de amō), § 177 (dois acusativos com verbos de chamar: quōs senātōrēs nōmināvit), § 181.1 (acusativo de duração), § 192.1 (dativo com adjetivos de proximidade), § 217.1 (ablativo de comparação), § 227 e 227.1 (ablativo absoluto, inclusive com cōnsulibus), § 228.1.b (lugar onde sem preposição com tōtus), § 230 (ablativo de tempo: annō septuāgēsimō), § 232.1 (locativo Rōmae), § 282.2 (relativa de finalidade), § 288.1.B (cum com imperfeito e mais-que-perfeito do subjuntivo), § 332.c (construção pessoal: dīcitur vēnisse), § 371 (calendário: calendas, nonas, idos)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 305 (concordância do relativo), § 419 e 419.a (ablativo absoluto; com nome no lugar do particípio), § 420 (o ablativo absoluto equivale a uma oração temporal, causal etc.), § 423 (tempo: ablativo e acusativo), § 424.g (datas: ante diem, cônsules no ablativo absoluto), § 546 (cum com imperfeito ou mais-que-perfeito do subjuntivo: circunstâncias), § 630 (o ano ab urbe conditā; subtrair de 754), § 631 (calendas, nonas e idos; regra de conversão)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 237 (ablativo absoluto, com o exemplo nātus est Augustus cōnsulibus Cicerōne et Antōniō), apêndice "Time. The Roman Calendar" (calendas, nonas, idos)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 175 (concordância do relativo), n. 296 (ablativo absoluto: his dictis, abiit; expulsis regibus)', tipo='dominio_publico'),
    ],
    objetivos=[
        'Situar Eutrópio e o Breviário e reconhecer o estilo da prosa histórica resumida: frases curtas, sujeito constante, verbos no perfeito.',
        'Ler e traduzir Breviário I, 1–2 com o vocabulário e as notas, mantendo a sequência dos fatos.',
        'Identificar as formas da passiva do perfectum no texto, dizer com que sujeito cada particípio concorda e traduzir a construção pessoal <i>crēditus est trānsīsse</i>.',
        'Converter datas romanas: o ano <i>ab urbe conditā</i> em ano antes de Cristo, e uma data em calendas para o nosso calendário.',
        'Reconhecer, com ajuda das glosas, o ablativo absoluto e o <i>cum</i> com subjuntivo, e traduzi-los por orações portuguesas.',
    ],
    secoes=[
        ('Eutrópio e o Breviário', f'''
<p>Depois da fábula, a história. <b>Eutrópio</b> (<i>Eutropius</i>) foi um alto funcionário do Império Romano no século IV d.C., quase quatro séculos depois de Fedro. No cabeçalho da obra, ele se apresenta como <i>magister memoriae</i>, o secretário encarregado da correspondência e dos registros do imperador, e dedica o livro ao imperador <b>Valente</b>, que reinou no Oriente de 364 a 378. A obra, escrita por volta de 370, chama-se <i>Breviārium ab urbe conditā</i>, "Resumo desde a fundação da cidade": em dez livros curtos, conta a história de Roma de Rômulo até a morte do imperador Joviano, em 364. Na dedicatória, Eutrópio diz o que fez: reuniu <i>per ōrdinem temporum brevī nārrātiōne</i>, "em ordem cronológica, numa narração breve", os fatos mais notáveis da guerra e da paz.</p>
<p>Essa finalidade explica o estilo, e o estilo explica por que Eutrópio é lido logo depois de Fedro. As frases são curtas e informativas; o sujeito (quase sempre o rei ou o povo romano) fica o mesmo por várias frases e às vezes nem é repetido; os verbos estão no perfeito, que é o tempo da narração histórica; e o vocabulário gira em torno de poucas ideias: fundar, vencer, reinar, morrer, governar. Por isso o <i>Breviário</i> foi, durante séculos, um dos primeiros livros de leitura nas escolas de latim, e circulou em edições escolares como a de J. C. Hazzard (Nova York, c. 1898), que você encontra no archive.org.</p>
<p>Uma diferença importante em relação a Fedro: Eutrópio não é um autor da época clássica, e às vezes a sua língua se afasta do uso que as gramáticas dão como normal (por exemplo, <i>decem et octō</i> para "dezoito", onde Bennett, § 81.2, dá <i>duodēvīgintī</i> ou <i>octōdecim</i>). Mas a sua prosa é regular e muito próxima da norma que você estudou. Neste capítulo você vai ler os dois primeiros capítulos do livro I: as origens de Rômulo, a fundação da cidade, as primeiras instituições, o rapto das sabinas, as guerras com os vizinhos e o desaparecimento do fundador.</p>
{observacao('Uma lenda contada como história', 'Os romanos do século IV, como os de qualquer época, tratavam a história de Rômulo como o começo verdadeiro da sua cidade, embora saibamos que boa parte dela é lenda. Eutrópio registra isso com cuidado: Rômulo é filho de Marte <i>quantum putātus est</i>, "segundo se acreditou", e foi para junto dos deuses <i>crēditus est</i>, "segundo se acreditou". Repare nesses verbos ao ler: o historiador distingue o que afirma do que apenas transmite.')}
'''),
        ('O texto: Breviário I, 1–2', f'''
<p>O texto segue o da The Latin Library, idêntico ao da Wikisource latina (que o copia da Latin Library) e, palavra por palavra, ao da edição crítica de Franz Rühl (Leipzig: Teubner, 1887), em domínio público; muda só a pontuação. Para controle, ele foi comparado também com a edição escolar de Hazzard (c. 1898), em domínio público: as palavras são as mesmas, exceto em dois pontos. Hazzard omite a longa oração relativa da frase 1.1 (<i>quō neque … recordārī</i>) e a ressalva <i>ut quī plūrimum minimumque trādunt</i> da frase 1.2. Se você quiser uma primeira leitura mais fácil, pule esses dois trechos, como os alunos de Hazzard faziam, e volte a eles depois. Os macrons e a numeração das frases são acréscimos deste livro.</p>
{tabela(['Frase', 'Texto latino'], [[n, f'<span lang="la">{v}</span>'] for n, v in TEXTO], 'Eutrópio, Breviário I, 1–2', latim_cols=(1,))}
{observacao('Sobre o texto: Rühl e Droysen', 'A outra grande edição crítica antiga, a de Hans Droysen (<i>Monumenta Germaniae Historica, Auctores antiquissimi</i> II, Berlim, 1879), também em domínio público, traz as mesmas palavras em 1.1–1.2 e difere de Rühl em quatro pontos do capítulo 2, todos registrados no aparato dela como divergências entre os manuscritos: (1) em 2.3, só <i>cum uxōrēs</i>, sem <i>Tum</i>; (2) em 2.3, <i>vīcīnās urbis Rōmae nātiōnēs</i>, com genitivo ("vizinhos da cidade de Roma"), em vez do dativo <i>urbī</i>; (3) em 2.6, só <i>crēditus est</i>, sem <i>et cōnsecrātus</i>, que alguns manuscritos acrescentam; (4) em 2.7, <i>ūnus annus</i> em vez de <i>annus ūnus</i>. Este livro segue Rühl e a The Latin Library; as notas sobre o dativo <i>urbī</i> e sobre <i>cōnsecrātus</i> valem para esse texto. Com <i>vīcīnus</i>, tanto o dativo quanto o genitivo são possíveis, e o sentido não muda.')}
<p>O trecho tem duas partes. O capítulo 1 é a <b>origem</b>: o império começa com Rômulo (1.1), que funda a cidade numa data precisa (1.2). O capítulo 2 é o <b>reinado</b>, em uma série de ações, cada uma num verbo no perfeito: <i>vocāvit, ēgit, recēpit, lēgit, nōmināvit, invītāvit, rapuit, vīcit</i>. O fim do reinado (2.6) e o intervalo entre os reis (2.7) fecham o episódio. Antes de traduzir, sublinhe todos os verbos conjugados: eles são o esqueleto do texto.</p>
{dica('<b>Leia pelo sujeito.</b> Em 2.1–2.4 o sujeito é sempre Rômulo, e o texto não o repete: cada verbo na 3ª pessoa do singular é "ele (Rômulo) fez". Quando o sujeito muda, Eutrópio avisa com um nominativo novo (<i>Haec omnia oppida</i>, 2.5; <i>senātōrēs</i>, 2.7). Na narrativa histórica, procurar quem faz a ação é quase sempre perguntar se apareceu um nominativo novo.')}
'''),
        ('Vocabulário e notas', f'''
{tabela(['No texto', 'Dicionário', 'Sentido aqui', 'Nota'], [
    ['imperium', 'imperium, -ī (n.)', 'poder; império', 'aqui, o Estado romano como potência'],
    ['quō … minus … amplius', 'quī, quae, quod; comparativos de parvus e amplus', 'do qual … menor … maior', '<i>quō</i>: ablativo de comparação (capítulo 18), "do que o qual"'],
    ['ab exōrdiō; exōrdium', 'exōrdium, -ī (n.)', 'começo, origem', '<i>exōrdium habet</i>: "tem o seu começo"'],
    ['ūllum', 'ūllus, -a, -um', 'nenhum (em frase negativa), algum', 'subentende-se <i>imperium</i>'],
    ['ferē', 'advérbio', 'quase; mais ou menos', '<i>haec ferē ēgit</i>: "fez mais ou menos isto"'],
    ['incrēmentīs', 'incrēmentum, -ī (n.)', 'crescimento', 'ablativo de especificação: "em crescimento"'],
    ['tōtō orbe', 'tōtus, -a, -um; orbis, -is (m.)', 'em todo o mundo', 'lugar onde sem preposição com <i>tōtus</i> (Bennett § 228.1.b)'],
    ['potest … recordārī', 'possum; recordor, -ārī, -ātus sum', 'pode recordar', 'infinitivo de depoente (capítulo 25)'],
    ['Rēae Silviae', 'Rēa Silvia, -ae', 'Reia Sílvia', 'mãe de Rômulo; genitivo dependente de <i>fīlius</i>'],
    ['Vestālis virginis', 'Vestālis, -is; virgō, -inis (f.)', 'virgem vestal', 'aposto de <i>Rēae Silviae</i>: sacerdotisa de Vesta'],
    ['quantum putātus est', 'putō, -āre, -āvī, -ātum', 'segundo se acreditou', 'literalmente "quanto ele foi considerado"'],
    ['Mārtis', 'Mārs, Mārtis (m.)', 'de Marte', 'também depende de <i>fīlius</i>'],
    ['ūnō partū', 'partus, -ūs (m.)', 'num só parto', 'ablativo, 4ª declinação: eram gêmeos'],
    ['ēditus est', 'ēdō, -ere, ēdidī, ēditum', 'foi dado à luz, nasceu', 'passiva do perfectum (capítulo 24)'],
    ['cum … latrōcinārētur', 'latrōcinor, -ārī, -ātus sum', 'como vivia de assaltos', 'depoente; imperfeito do subjuntivo com <i>cum</i>: glosa na seção 6'],
    ['inter pāstōrēs', 'pāstor, -ōris (m.)', 'entre os pastores', '<i>inter</i> + acusativo'],
    ['decem et octō annōs nātus', 'nāscor, nāscī, nātus sum', 'com dezoito anos de idade', 'idiomático: "nascido há dezoito anos"; acusativo de duração'],
    ['exiguam', 'exiguus, -a, -um', 'pequeno, modesto', 'concorda com <i>urbem</i>'],
    ['in Palātīnō monte', 'Palātīnus, -a, -um; mōns, montis (m.)', 'no monte Palatino', 'uma das sete colinas de Roma'],
    ['cōnstituit', 'cōnstituō, -ere, -uī, -ūtum', 'fundou, estabeleceu', 'perfeito'],
    ['XI Kal. Māiās', 'Kalendae, -ārum; Māius, -a, -um', '21 de abril', 'lê-se <i>ante diem ūndecimum Kalendās Māiās</i>; seção 5'],
    ['Olympiadis sextae annō tertiō', 'Olympias, -adis (f.)', 'no 3º ano da 6ª olimpíada', 'contagem grega em períodos de quatro anos'],
    ['post Trōiae excidium', 'excidium, -ī (n.)', 'depois da destruição de Troia', '<i>post</i> + acusativo'],
    ['ut quī … trādunt', 'trādō, -ere, -didī, -ditum', 'segundo os que transmitem…', 'ressalva sobre as cronologias divergentes; ver as notas'],
    ['annō trecentēsimō nōnāgēsimō quārtō', 'ordinais', 'no ano 394º', 'ablativo de tempo (Bennett § 230)'],
    ['conditā cīvitāte', 'condō, -ere, condidī, conditum', 'fundada a cidade', 'ablativo absoluto: glosa na seção 6'],
    ['ex nōmine suō', 'nōmen, -inis (n.)', 'a partir do seu próprio nome', '<i>suō</i>: reflexivo, refere-se a Rômulo'],
    ['Rōmam vocāvit', 'vocō, -āre, -āvī, -ātum', 'chamou (de) Roma', 'dois acusativos: <i>quam</i> e <i>Rōmam</i>'],
    ['haec … ēgit', 'agō, -ere, ēgī, āctum', 'fez estas coisas', '<i>haec</i>: acusativo neutro plural'],
    ['multitūdinem fīnitimōrum', 'multitūdō, -inis (f.); fīnitimus, -a, -um', 'uma multidão de vizinhos', '<i>fīnitimī</i>: adjetivo usado como nome'],
    ['recēpit', 'recipiō, -ere, recēpī, receptum', 'acolheu, recebeu', 'perfeito'],
    ['ex seniōribus', 'senior, -ōris', 'dentre os mais velhos', 'comparativo de <i>senex</i>, usado como nome'],
    ['lēgit', 'legō, -ere, lēgī, lēctum', 'escolheu', 'perfeito com <i>ē</i> longo; o presente seria <i>legit</i>'],
    ['quōrum cōnsiliō omnia ageret', 'cōnsilium, -ī (n.)', 'para fazer tudo com o conselho deles', 'relativa com subjuntivo de finalidade: glosa na seção 6'],
    ['quōs senātōrēs nōmināvit', 'senātor, -ōris (m.); nōminō, -āre', 'aos quais chamou senadores', 'dois acusativos (Bennett § 177)'],
    ['propter senectūtem', 'senectūs, -ūtis (f.)', 'por causa da velhice', '<i>senātor</i> e <i>senectūs</i> vêm de <i>senex</i>'],
    ['cum … nōn habērent', 'habeō', 'como não tinham', 'imperfeito do subjuntivo com <i>cum</i>'],
    ['uxōrēs', 'uxor, -ōris (f.)', 'esposas', 'objeto de <i>habērent</i>'],
    ['ad spectāculum lūdōrum', 'spectāculum, -ī (n.); lūdī, -ōrum (m.)', 'a um espetáculo de jogos', '<i>lūdī</i>, no plural: jogos públicos, festas'],
    ['vīcīnās urbī Rōmae nātiōnēs', 'vīcīnus, -a, -um; nātiō, -ōnis (f.)', 'os povos vizinhos da cidade de Roma', 'dativo com adjetivo de proximidade (Bennett § 192.1)'],
    ['rapuit', 'rapiō, -ere, rapuī, raptum', 'raptou, arrebatou', 'perfeito'],
    ['commōtīs bellīs', 'commoveō, -ēre, -mōvī, -mōtum', 'tendo sido provocadas guerras', 'ablativo absoluto'],
    ['raptārum', 'rapiō (particípio raptus, -a, -um)', 'das (mulheres) raptadas', 'particípio substantivado, genitivo plural feminino'],
    ['iniūriam', 'iniūria, -ae (f.)', 'ofensa, injustiça', 'regido por <i>propter</i>'],
    ['vīcit', 'vincō, -ere, vīcī, victum', 'venceu', 'perfeito; seis objetos, os povos vizinhos'],
    ['cingunt', 'cingō, -ere, cīnxī, cīnctum', 'cercam, rodeiam', 'presente: as cidades ainda existiam na época do autor'],
    ['cum … nōn compāruisset', 'compāreō, -ēre, -uī', 'como não tinha mais aparecido', 'mais-que-perfeito do subjuntivo com <i>cum</i>'],
    ['ortā subitō tempestāte', 'orior, orīrī, ortus sum; tempestās, -ātis (f.)', 'tendo-se levantado de repente uma tempestade', 'ablativo absoluto com particípio de depoente'],
    ['annō rēgnī trīcēsimō septimō', 'rēgnum, -ī (n.)', 'no trigésimo sétimo ano do reinado', 'ablativo de tempo'],
    ['ad deōs trānsīsse', 'trānseō, -īre, -iī, -itum', 'ter passado para junto dos deuses', 'infinitivo perfeito (<i>trānsīsse</i> = <i>trānsiisse</i>)'],
    ['crēditus est', 'crēdō, -ere, crēdidī, crēditum', 'acreditou-se que ele…', 'construção pessoal: seção 4'],
    ['cōnsecrātus', 'cōnsecrō, -āre, -āvī, -ātum', 'consagrado, divinizado', 'subentende-se <i>est</i>'],
    ['Rōmae', 'Rōma, -ae (f.)', 'em Roma', 'locativo (Bennett § 232.1)'],
    ['per quīnōs diēs', 'quīnī, -ae, -a (distributivo)', 'por cinco dias cada um', 'cada senador governava cinco dias'],
    ['imperāvērunt', 'imperō, -āre, -āvī, -ātum', 'governaram, mandaram', 'perfeito, 3ª pl.'],
    ['hīs rēgnantibus', 'rēgnō, -āre', 'enquanto estes reinavam', 'ablativo absoluto com particípio presente'],
    ['complētus est', 'compleō, -ēre, -ēvī, -ētum', 'completou-se', 'passiva do perfectum'],
], 'Vocabulário de Breviário I, 1–2', latim_cols=(0, 1))}
<h3>Notas às frases</h3>
<p><b>1.1.</b> A frase de abertura é a mais longa do trecho, e a dificuldade está toda na relativa intercalada. Leia primeiro o esqueleto: <i>Rōmānum imperium … ā Rōmulō exōrdium habet, quī … fīlius … cum Remō frātre ūnō partū ēditus est</i>, "O Império Romano tem o seu começo em Rômulo, que, filho de…, nasceu num só parto com o irmão Remo". Depois volte à relativa: <i>quō</i> é ablativo de comparação ("do que o qual"), e a ideia é que a memória humana quase não consegue lembrar, no mundo inteiro, um império que tenha começado menor (<i>ab exōrdiō … minus</i>) ou crescido mais (<i>incrēmentīs … amplius</i>). <i>Fīlius</i> rege dois genitivos, um de cada lado: <i>Rēae Silviae</i> (a mãe) e <i>Mārtis</i> (o pai, com a ressalva <i>quantum putātus est</i>).</p>
<p><b>1.2.</b> <i>Is</i> retoma Rômulo. <i>Decem et octō annōs nātus</i> é a maneira latina de dar a idade: "nascido há dezoito anos", isto é, "com dezoito anos" (o acusativo indica a duração, Bennett § 181.1). A data vem em três sistemas, um depois do outro: o calendário romano (<i>XI Kal. Māiās</i>), as olimpíadas gregas e a distância desde a queda de Troia. A ressalva <i>ut quī plūrimum minimumque trādunt</i> ("conforme os que transmitem o máximo e o mínimo") parece admitir que as cronologias antigas divergiam; o sentido exato é discutido, e Hazzard simplesmente a omite.</p>
<p><b>2.1–2.2.</b> <i>Haec ferē ēgit</i>, "fez mais ou menos o seguinte", anuncia a lista de ações. <i>Haec</i> é neutro plural ("estas coisas"), não feminino. Na frase 2.2, três verbos no perfeito (<i>recēpit, lēgit, nōmināvit</i>) e duas relativas: a primeira (<i>quōrum cōnsiliō omnia ageret</i>) diz para que os cem foram escolhidos, a segunda (<i>quōs senātōrēs nōmināvit</i>) diz como foram chamados. A explicação etimológica (<i>senātōrēs … propter senectūtem</i>) é tradicional: <i>senātus</i> e <i>senectūs</i> vêm ambos de <i>senex</i>, "velho".</p>
<p><b>2.3–2.5.</b> O rapto das sabinas em uma frase: <i>cum</i> com subjuntivo dá o motivo (não tinham esposas), dois verbos no perfeito dão a ação (<i>invītāvit … rapuit</i>). <i>Eārum</i> refere-se a <i>nātiōnēs</i>: "as moças delas", dos povos convidados. Em 2.4, <i>raptārum</i> é um particípio usado como nome, "das (mulheres) raptadas". A lista de povos vencidos (<i>Caenīnēnsēs … Vēientēs</i>) está toda no acusativo plural; em 2.5, o presente <i>cingunt</i> fala da geografia ainda visível no tempo do autor.</p>
<p><b>2.6–2.7.</b> O fim de Rômulo é contado com cautela: ele desapareceu durante uma tempestade, e <i>crēditus est</i>, "acreditou-se", que tinha passado para os deuses. <i>Cōnsecrātus</i> subentende o <i>est</i> do verbo anterior. Em 2.7, <i>Rōmae</i> é locativo, "em Roma"; <i>per quīnōs diēs</i> usa o distributivo <i>quīnī</i>, "cinco de cada vez": os senadores se revezaram no poder, cada um por cinco dias, até se completar um ano (é o primeiro <i>interrēgnum</i>).</p>
'''),
        ('A passiva do perfectum na narrativa histórica', f'''
<p>O pré-requisito deste capítulo é a passiva do perfectum (capítulo 24), e ela aparece aqui num uso muito característico da prosa histórica. Eutrópio a emprega para falar de nascimento, de crença e de conclusão: coisas que <b>aconteceram a</b> alguém mais do que coisas que alguém fez. Reúna as formas do trecho:</p>
{tabela(['No texto', 'Verbo', 'Forma', 'Sujeito com que concorda', 'Tradução'], [
    ['<b>putātus est</b> (1.1)', 'putō, putāvī, <b>putātum</b>', 'perfeito passivo, 3ª sing. masc.', 'Rômulo', '"foi considerado"; com <i>quantum</i>: "segundo se acreditou"'],
    ['<b>ēditus est</b> (1.1)', 'ēdō, ēdidī, <b>ēditum</b>', 'perfeito passivo, 3ª sing. masc.', '<i>quī</i> (= Rômulo)', '"foi dado à luz", "nasceu"'],
    ['<b>crēditus est</b> (2.6)', 'crēdō, crēdidī, <b>crēditum</b>', 'perfeito passivo, 3ª sing. masc.', 'Rômulo (sujeito implícito)', '"acreditou-se que ele…"'],
    ['(est) <b>cōnsecrātus</b> (2.6)', 'cōnsecrō, cōnsecrāvī, <b>cōnsecrātum</b>', 'perfeito passivo, com <i>est</i> subentendido', 'Rômulo', '"foi divinizado"'],
    ['<b>complētus est</b> (2.7)', 'compleō, complēvī, <b>complētum</b>', 'perfeito passivo, 3ª sing. masc.', '<i>annus</i>', '"completou-se"'],
], 'A passiva do perfectum em Breviário I, 1–2')}
<p>Três coisas a observar. A primeira é a <b>concordância</b>: todos estes particípios estão no nominativo singular masculino porque os sujeitos (Rômulo, <i>annus</i>) são masculinos singulares; se o sujeito fosse <i>urbs</i>, seria <i>condita est</i>; se fosse <i>virginēs</i>, <i>raptae sunt</i>. A segunda é a <b>elipse</b> de <i>est</i>: em <i>crēditus est et cōnsecrātus</i>, o auxiliar vale para os dois particípios, um recurso comum quando duas passivas seguidas têm o mesmo sujeito. A terceira é a <b>tradução</b>: o português nem sempre gosta da passiva analítica, e <i>complētus est</i> fica melhor como "completou-se" do que como "foi completado"; <i>ēditus est</i>, como "nasceu".</p>
<p>A construção mais interessante é <i>ad deōs trānsīsse crēditus est</i>. Em português dizemos "acreditou-se <b>que ele</b> passou para junto dos deuses": o verbo "acreditar" fica impessoal e Rômulo vira sujeito da oração dependente. O latim prefere a <b>construção pessoal</b>: o próprio Rômulo é o sujeito de <i>crēditus est</i>, e o que se acreditava dele vem no infinitivo, literalmente "ele foi acreditado ter passado para os deuses". É o mesmo padrão de <i>dīcitur in Italiam vēnisse</i>, "diz-se que ele veio para a Itália" (Bennett § 332.c). O infinitivo <i>trānsīsse</i> é perfeito (forma contraída de <i>trānsiisse</i>) porque a passagem para os deuses é <b>anterior</b> ao momento em que se acreditou nela; os infinitivos e o seu tempo relativo são o assunto do capítulo 27, e a oração infinitiva, que está por trás desta construção, o do capítulo 28.</p>
{comparacao('Construção pessoal latina × impessoal portuguesa', ['Latim (pessoal)', 'Literalmente', 'Português natural'], [
    ['Rōmulus ad deōs trānsīsse <b>crēditus est</b>.', 'Rômulo foi acreditado ter passado para os deuses.', '<b>Acreditou-se que</b> Rômulo tinha passado para junto dos deuses.'],
    ['Rōmulus Mārtis fīlius <b>putātus est</b>.', 'Rômulo foi considerado filho de Marte.', '<b>Considerava-se</b> Rômulo filho de Marte. / Rômulo <b>era tido por</b> filho de Marte.'],
    ['Rēmus Rōmulī frāter <b>fuisse dīcitur</b>.', 'Remo é dito ter sido irmão de Rômulo.', '<b>Diz-se que</b> Remo foi irmão de Rômulo.'],
])}
{observacao('Depoentes no meio da passiva', 'Três verbos do trecho têm forma passiva e sentido ativo, porque são depoentes (capítulo 25): <i>recordārī</i> ("lembrar", 1.1), <i>latrōcinārētur</i> ("vivia de assaltos", 1.2) e <i>ortā</i> ("tendo surgido", 2.6, de <i>orior</i>). Não os traduza como passivos. A pista é o dicionário: <i>recordor, -ārī, -ātus sum</i> não tem forma ativa.')}
'''),
        ('Datas, números e nomes', f'''
<p>Um texto histórico romano está cheio de números, e eles seguem convenções diferentes das nossas. Eutrópio data a fundação de Roma de três maneiras na mesma frase (1.2), e depois, ao longo do livro, passa a datar os acontecimentos pelo ano da fundação. Vale a pena aprender as três.</p>
<h3>1. O ano "desde a fundação da cidade"</h3>
<p>Os romanos designavam o ano, na prática, pelos nomes dos dois cônsules daquele ano; os historiadores, porém, também contavam os anos a partir da fundação de Roma: <i>ab urbe conditā</i>, "desde a cidade fundada", ou <i>annō urbis conditae</i>, "no ano da cidade fundada", abreviado <b>a.u.c.</b> A data aceita pelos romanos para a fundação, segundo o cálculo do erudito Varrão, corresponde a 753 a.C. Daí a regra de conversão que Allen e Greenough dão no § 630: para um ano antes de Cristo, <b>subtraia de 754</b> o ano da cidade (o 1º ano da cidade é 753 a.C.); para um ano depois de Cristo, <b>subtraia 753</b> do ano da cidade. No capítulo 18 do mesmo livro I, Eutrópio usa o sistema:</p>
{exemplos([('Annō trecentēsimō et alterō ab urbe conditā imperium cōnsulāre cessāvit.', 'No ano trecentésimo segundo desde a fundação da cidade, o poder consular foi interrompido. (Breviário I, 18; <i>alter</i>, "segundo", como ordinal; 754 − 302 = 452 a.C.)')])}
<h3>2. As calendas, as nonas e os idos</h3>
<p>Os romanos não numeravam os dias do mês do primeiro ao último. Contavam <b>para trás</b>, a partir de três dias fixos: as <b>calendas</b> (<i>Kalendae</i>), o dia 1º; as <b>nonas</b> (<i>Nōnae</i>), o dia 5 (ou 7, em março, maio, julho e outubro); e os <b>idos</b> (<i>Īdūs</i>), o dia 13 (ou 15, nesses mesmos quatro meses) (Allen e Greenough § 631; Bennett § 371). A contagem era inclusiva: contavam-se o dia de partida e o de chegada. <i>XI Kal. Māiās</i>, abreviação de <i>ante diem ūndecimum Kalendās Māiās</i>, é "o 11º dia antes das calendas de maio". A regra prática (Allen e Greenough § 631.d): para uma data antes das calendas, some 2 ao número de dias do mês anterior e subtraia o número dado. Abril tem 30 dias: 30 + 2 − 11 = <b>21 de abril</b>, data em que até hoje se comemora o aniversário de Roma. O nome do mês é um adjetivo que concorda com <i>Kalendās</i>: <i>Māiās</i> (acusativo feminino plural).</p>
{tabela(['Expressão', 'Leitura por extenso', 'Data'], [
    ['Kal. Iān.', 'Kalendīs Iānuāriīs', '1º de janeiro'],
    ['Nōn. Feb.', 'Nōnīs Februāriīs', '5 de fevereiro'],
    ['Īd. Mārt.', 'Īdibus Mārtiīs', '15 de março (o dia da morte de César)'],
    ['prīdiē Kal. Māi.', 'prīdiē Kalendās Māiās', '30 de abril (a véspera das calendas)'],
    ['XI Kal. Māi.', 'ante diem ūndecimum Kalendās Māiās', '21 de abril (30 + 2 − 11)'],
], 'Datas romanas', latim_cols=(0, 1))}
<h3>3. Olimpíadas, Troia e os ordinais</h3>
<p>As <b>olimpíadas</b> eram o sistema grego: períodos de quatro anos contados a partir dos primeiros Jogos Olímpicos (776 a.C.). O "terceiro ano da sexta olimpíada" cai em 754–753 a.C., coerente com a data de Varrão. A contagem desde a queda de Troia dependia de uma data lendária, e as cronologias antigas divergiam; é provavelmente por isso que Eutrópio acrescenta a ressalva sobre "os que dão o máximo e o mínimo". Repare também na forma dos números, que você estudou no capítulo 19:</p>
{tabela(['No texto', 'Tipo', 'Valor', 'Observação'], [
    ['decem et octō', 'cardinal', '18', 'forma com <i>et</i>; Bennett dá <i>duodēvīgintī</i> ou <i>octōdecim</i> (§§ 79, 81.2)'],
    ['centum', 'cardinal', '100', 'indeclinável; aqui sem nome: "cem (homens)"'],
    ['sextae · tertiō', 'ordinais', '6º · 3º', 'concordam com <i>Olympiadis</i> e <i>annō</i>'],
    ['trecentēsimō nōnāgēsimō quārtō', 'ordinal composto', '394º', 'cada parte concorda com <i>annō</i>'],
    ['trīcēsimō septimō', 'ordinal composto', '37º', 'idem'],
    ['quīnōs', 'distributivo', 'cinco de cada vez', '"cinco para cada um" (Bennett § 81.4)'],
], 'Os números do trecho', latim_cols=(0,))}
<p>Por fim, as datas vão sempre no <b>ablativo sem preposição</b> quando dizem <i>quando</i> algo aconteceu: <i>annō tertiō</i>, <i>annō rēgnī trīcēsimō septimō</i> (Bennett § 230). O acusativo indica <i>quanto tempo</i>: <i>decem et octō annōs nātus</i>; <i>per quīnōs diēs</i>, com <i>per</i> para reforçar a duração.</p>
{dica('<b>Os nomes próprios.</b> Num texto histórico, os nomes de povos costumam vir no plural (<i>Sabīnī</i>, <i>Vēientēs</i>, "os habitantes de Veios") e se declinam como qualquer nome: <i>Sabīnōs</i> é acusativo da 2ª, <i>Vēientēs</i> e <i>Fīdēnātēs</i> são acusativos da 3ª. Não os traduza pela terminação latina: procure a forma portuguesa (sabinos, veientes, fidenates) ou explique ("os habitantes de Fidenas").')}
'''),
        ('Construções novas, análise e tradução', f'''
<p>Três construções do trecho pertencem a capítulos posteriores ao pré-requisito (24), e você talvez já as tenha estudado. Se ainda não, basta reconhecê-las e traduzi-las pelas fórmulas abaixo; os capítulos indicados as explicam a fundo.</p>
{tabela(['Construção', 'Exemplo no texto', 'Como reconhecer', 'Como traduzir', 'Capítulo'], [
    ['<b>ablativo absoluto</b>', '<i>Conditā cīvitāte</i>; <i>Commōtīs bellīs</i>; <i>ortā subitō tempestāte</i>; <i>hīs rēgnantibus</i>', 'nome + particípio no ablativo, sem ligação gramatical com o resto da frase', '"fundada a cidade", "depois que a cidade foi fundada"; "enquanto estes reinavam"', '30'],
    ['<b><i>cum</i> + subjuntivo</b>', '<i>cum … latrōcinārētur</i>; <i>cum … nōn habērent</i>; <i>cum … nōn compāruisset</i>', '<i>cum</i> com imperfeito ou mais-que-perfeito do subjuntivo', '"como / quando" + a circunstância ou o motivo: "como não tinham esposas"', '32, 34'],
    ['<b>relativa de finalidade</b>', '<i>quōrum cōnsiliō omnia ageret</i>', 'relativo + subjuntivo, exprimindo o objetivo', '"para fazer tudo com o conselho deles"', '33'],
], 'Construções glosadas', latim_cols=())}
<p>O ablativo absoluto é a construção que mais marca este texto, e Eutrópio o usa como o usam todos os historiadores: para pôr, em duas palavras, o pano de fundo de uma ação. <i>Conditā cīvitāte, … haec ferē ēgit</i>: o ablativo absoluto diz <b>depois de quê</b> Rômulo agiu. <i>Commōtīs bellīs … vīcit</i>: diz em que circunstância ele venceu. Em <i>hīs rēgnantibus</i>, o particípio presente indica simultaneidade, "enquanto estes reinavam" (Bennett § 227; Allen e Greenough §§ 419–420). Agora analise a frase 2.1, que traz um ablativo absoluto e uma relativa:</p>
{analise('Eutrópio, Breviário I, 2 (frase 2.1)', [
    ('Conditā', 'condō, -ere, condidī, conditum, fundar', 'particípio perfeito passivo, ablativo singular feminino', 'com <i>cīvitāte</i>, ablativo absoluto: "fundada a cidade"'),
    ('cīvitāte', 'cīvitās, -ātis (f.), cidade, Estado', 'ablativo singular', 'núcleo do ablativo absoluto; antecedente de <i>quam</i>'),
    ('quam', 'quī, quae, quod (relativo)', 'acusativo singular feminino', 'objeto de <i>vocāvit</i>; refere-se a <i>cīvitāte</i>'),
    ('ex', 'ex (preposição + ablativo)', 'invariável', 'origem do nome: "a partir de"'),
    ('nōmine', 'nōmen, -inis (n.), nome', 'ablativo singular', 'regido por <i>ex</i>'),
    ('suō', 'suus, -a, -um (possessivo reflexivo)', 'ablativo singular neutro', 'concorda com <i>nōmine</i>; refere-se ao sujeito, Rômulo'),
    ('Rōmam', 'Rōma, -ae (f.)', 'acusativo singular', 'predicativo do objeto: "chamou-a (de) Roma"'),
    ('vocāvit', 'vocō, -āre, -āvī, -ātum, chamar', 'perfeito do indicativo ativo, 3ª sing.', 'verbo da relativa; sujeito: Rômulo'),
    ('haec', 'hīc, haec, hōc', 'acusativo plural neutro', 'objeto de <i>ēgit</i>: "estas coisas"'),
    ('ferē', 'advérbio', 'invariável', '"mais ou menos"'),
    ('ēgit', 'agō, -ere, ēgī, āctum, fazer', 'perfeito do indicativo ativo, 3ª sing.', 'verbo principal; sujeito: Rômulo'),
])}
<p>A frase 1.2 mostra como Eutrópio empilha informações em torno de um só verbo principal. Desfeita em blocos, ela fica assim:</p>
{diagrama_frase([('Is', 'sujeito · Rômulo'), ('cum … latrōcinārētur', 'circunstância · cum + subjuntivo'), ('decem et octō annōs nātus', 'idade · predicativo do sujeito'), ('urbem exiguam', 'objeto · ac. sing. f.'), ('cōnstituit', 'verbo · perfeito'), ('XI Kal. Māiās …', 'data · três sistemas')],
    'Esqueleto de 1.2: <i>Is … urbem exiguam in Palātīnō monte cōnstituit</i>, "Ele fundou uma pequena cidade no monte Palatino", com a circunstância antes e as datas depois.')}
<p>Compare agora a sua tradução com a deste livro, feita para ser fiel à função das palavras, sem deixar de ser português:</p>
{tabela(['Frase', 'Tradução (Bibliotheca Latina)'], [
    ['1.1', 'O Império Romano (e a memória humana quase não consegue lembrar, no mundo inteiro, outro que tenha tido começo menor ou crescimento maior) tem a sua origem em Rômulo, que, filho de Reia Sílvia, virgem vestal, e, segundo se acreditou, de Marte, nasceu num só parto com o irmão Remo.'],
    ['1.2', 'Quando vivia de assaltos entre os pastores, com dezoito anos de idade, ele fundou uma pequena cidade no monte Palatino, no dia 21 de abril, no terceiro ano da sexta olimpíada, no ano trezentos e noventa e quatro depois da destruição de Troia, segundo os que transmitem o máximo e o mínimo.'],
    ['2.1', 'Fundada a cidade, que ele chamou de Roma a partir do próprio nome, fez mais ou menos o seguinte.'],
    ['2.2', 'Acolheu na cidade uma multidão de vizinhos; escolheu cem dentre os mais velhos, para fazer tudo com o conselho deles, e os chamou de senadores por causa da velhice.'],
    ['2.3', 'Depois, como nem ele nem o seu povo tinham esposas, convidou para um espetáculo de jogos os povos vizinhos da cidade de Roma e raptou as moças deles.'],
    ['2.4', 'Provocadas guerras por causa da ofensa às moças raptadas, venceu os ceninenses, os antemnates, os crustuminos, os sabinos, os fidenates e os veientes.'],
    ['2.5', 'Todas essas cidades ficam ao redor de Roma.'],
    ['2.6', 'E, como ele não apareceu mais depois de uma tempestade que se levantou de repente, no trigésimo sétimo ano do seu reinado, acreditou-se que tinha passado para junto dos deuses, e ele foi divinizado.'],
    ['2.7', 'Depois disso, em Roma, os senadores governaram cinco dias cada um, e, enquanto eles reinavam, completou-se um ano.'],
], 'Tradução de Breviário I, 1–2')}
<p>Note as escolhas: o ablativo absoluto ora fica como particípio português ("Fundada a cidade", "Provocadas guerras"), ora vira oração ("depois de uma tempestade que se levantou de repente", "enquanto eles reinavam"), conforme soa melhor. <i>Raptārum iniūriam</i> virou "a ofensa às moças raptadas": o genitivo latino indica aqui quem sofreu a ofensa. E <i>urbem cingunt</i>, que literalmente é "cercam a cidade", virou "ficam ao redor de Roma", porque se trata de geografia, não de cerco.</p>
<h3>Resumo</h3>
<ul>
<li>Eutrópio, funcionário do século IV, resumiu em dez livros a história de Roma <i>ab urbe conditā</i>; a sua prosa é curta, cronológica e regular.</li>
<li>A passiva do perfectum (<i>ēditus est</i>, <i>crēditus est</i>, <i>complētus est</i>) concorda com o sujeito; <i>est</i> pode ficar subentendido; <i>crēditus est trānsīsse</i> é construção pessoal: "acreditou-se que ele passou".</li>
<li>Ano da cidade → a.C.: 754 − ano; datas em calendas: dias do mês anterior + 2 − número (<i>XI Kal. Māiās</i> = 21 de abril).</li>
<li>Tempo em que: ablativo (<i>annō tertiō</i>); duração e idade: acusativo (<i>decem et octō annōs nātus</i>); "em Roma": locativo <i>Rōmae</i>.</li>
<li>Ablativo absoluto (<i>Conditā cīvitāte</i>) e <i>cum</i> com subjuntivo dão o pano de fundo da ação principal.</li>
</ul>
<p>No capítulo 44, César abre a sua Guerra da Gália com uma descrição geográfica que se tornou a frase mais conhecida da prosa latina.</p>
'''),
    ],
    erros_comuns=[
        ('Traduzir <i>Conditā cīvitāte</i> como sujeito ("A cidade fundada fez…") ou como objeto.', 'É um ablativo absoluto: nome e particípio no ablativo, sem função gramatical na oração principal, cujo sujeito é Rômulo (implícito em <i>ēgit</i>). Traduza como circunstância: "Fundada a cidade", "Depois de fundar a cidade". A pista é o ablativo sem preposição seguido de um verbo cujo sujeito é outro.'),
        ('Ler <i>XI Kal. Māiās</i> como "11 de maio" ou "1º de maio".', 'Os romanos contavam para trás a partir das calendas, de modo inclusivo: é o 11º dia antes de 1º de maio. Pela regra de Allen e Greenough (§ 631.d), 30 (dias de abril) + 2 − 11 = 21 de abril.'),
        ('Traduzir <i>decem et octō annōs nātus</i> como "nasceu dezoito anos" ou "nascido em dezoito anos".', 'É a fórmula latina da idade: o acusativo de duração com <i>nātus</i>, "nascido há dezoito anos", isto é, "com dezoito anos de idade". O mesmo vale para qualquer idade: <i>vīgintī annōs nātus</i>, "com vinte anos".'),
        ('Traduzir <i>trānsīsse crēditus est</i> palavra por palavra: "foi acreditado ter passado".', 'O latim usa a construção pessoal (o sujeito é Rômulo); o português prefere a impessoal: "acreditou-se que ele tinha passado". Mantenha o sentido e a relação de tempo (infinitivo perfeito = anterior), não a forma.'),
        ('Tomar <i>Rōmae</i> em 2.7 por genitivo ("de Roma") ou dativo, e <i>urbī Rōmae</i> em 2.3 por locativo.', 'Em 2.7, <i>Rōmae</i> sozinho, com um verbo de estado (<i>imperāvērunt</i>), é locativo: "em Roma" (Bennett § 232.1). Em 2.3, <i>urbī Rōmae</i> é dativo regido pelo adjetivo <i>vīcīnās</i> ("vizinhos <b>da</b> cidade de Roma"), com <i>Rōmae</i> como aposto de <i>urbī</i>. O contexto (verbo ou adjetivo que pede o caso) decide.'),
        ('Entender <i>haec ferē ēgit</i> como "esta (mulher) fez" ou ligar <i>haec</i> a <i>cīvitāte</i>.', '<i>Haec</i> é acusativo neutro plural, objeto de <i>ēgit</i>: "fez estas coisas". <i>Cīvitāte</i> está no ablativo, e <i>haec</i> não pode concordar com ele. O sujeito de <i>ēgit</i> é Rômulo, como em todas as frases de 2.1 a 2.4.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · A fundação (frase 1.2, sem as datas)',
            'Traduza: <i lang="la">Is cum inter pāstōrēs latrōcinārētur, decem et octō annōs nātus urbem exiguam in Palātīnō monte cōnstituit.</i>', [
            ('Qual é o verbo principal, e qual o seu sujeito?', '<i>Cōnstituit</i>, perfeito, 3ª sing., "fundou". O sujeito é <i>Is</i>, "ele", que retoma Rômulo da frase anterior.'),
            ('O que faz <i>cum … latrōcinārētur</i>?', '<i>Cum</i> com o imperfeito do subjuntivo (<i>latrōcinārētur</i>, de um depoente) descreve a circunstância em que a ação principal aconteceu: "quando (ou: enquanto) ele vivia de assaltos entre os pastores". O capítulo 34 estuda essa construção.'),
            ('Como traduzir <i>decem et octō annōs nātus</i>?', 'É a idade: <i>nātus</i> concorda com <i>Is</i> (nominativo masculino) e <i>annōs</i> é acusativo de duração. "Com dezoito anos de idade."'),
            ('Qual é o objeto, e onde?', '<i>Urbem exiguam</i>, acusativo singular feminino: "uma pequena cidade". <i>In Palātīnō monte</i>, <i>in</i> + ablativo: lugar onde, "no monte Palatino".'),
            ('Monte a tradução.', '"Quando vivia de assaltos entre os pastores, ele, com dezoito anos de idade, fundou uma pequena cidade no monte Palatino."'),
        ]),
        pratica_guiada('Prática guiada 2 · O desaparecimento de Rômulo (frase 2.6)',
            'Traduza: <i lang="la">Et cum ortā subitō tempestāte nōn compāruisset, annō rēgnī trīcēsimō septimō ad deōs trānsīsse crēditus est et cōnsecrātus.</i>', [
            ('Separe as orações.', 'Principal: <i>(annō …) ad deōs trānsīsse crēditus est et cōnsecrātus</i>. Subordinada: <i>cum … nōn compāruisset</i>. Dentro da subordinada, um ablativo absoluto: <i>ortā subitō tempestāte</i>.'),
            ('Traduza o ablativo absoluto.', '<i>Ortā</i> é particípio perfeito de <i>orior</i> (depoente, sentido ativo), no ablativo feminino, concordando com <i>tempestāte</i>: "tendo surgido de repente uma tempestade", ou "depois que uma tempestade se levantou de repente".'),
            ('E <i>cum … nōn compāruisset</i>?', 'Mais-que-perfeito do subjuntivo com <i>cum</i>: a circunstância anterior à ação principal. "Como ele não tinha mais aparecido".'),
            ('Que caso é <i>annō rēgnī trīcēsimō septimō</i>?', 'Ablativo de tempo, sem preposição: "no trigésimo sétimo ano do reinado". <i>Rēgnī</i> é genitivo dependente de <i>annō</i>.'),
            ('Como traduzir <i>trānsīsse crēditus est et cōnsecrātus</i>?', 'Construção pessoal com infinitivo perfeito: "acreditou-se que ele tinha passado (para junto dos deuses)". <i>Cōnsecrātus</i> subentende <i>est</i>: "e foi divinizado".'),
            ('Monte a tradução.', '"E, como ele não tinha mais aparecido depois de uma tempestade que se levantou de repente, no trigésimo sétimo ano do reinado, acreditou-se que tinha passado para junto dos deuses, e ele foi divinizado."'),
        ], 'Conclusão: numa frase longa, separe primeiro a oração principal e as subordinadas; os ablativos absolutos e as datas são blocos que você pode traduzir à parte e encaixar depois.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Compreensão', 'Responda em português, citando a passagem latina que justifica a resposta.', [
            ('Quem eram os pais de Rômulo, segundo Eutrópio?', 'Reia Sílvia, uma virgem vestal, e, segundo se acreditava, o deus Marte: <i>Rēae Silviae, Vestālis virginis, fīlius et, quantum putātus est, Mārtis</i> (1.1).'),
            ('Onde e com que idade Rômulo fundou a cidade?', 'No monte Palatino, aos dezoito anos: <i>decem et octō annōs nātus urbem exiguam in Palātīnō monte cōnstituit</i> (1.2).'),
            ('Para que Rômulo escolheu os cem senadores, e por que eles se chamavam assim?', 'Para fazer tudo com o conselho deles (<i>quōrum cōnsiliō omnia ageret</i>), e chamavam-se senadores por causa da idade (<i>propter senectūtem</i>) (2.2).'),
            ('Qual foi a causa das guerras com os povos vizinhos?', 'A ofensa do rapto das moças: <i>Commōtīs bellīs propter raptārum iniūriam</i> (2.4).'),
            ('O que aconteceu depois do desaparecimento de Rômulo?', 'Os senadores governaram em revezamento, cinco dias cada um, durante um ano: <i>per quīnōs diēs senātōrēs imperāvērunt et hīs rēgnantibus annus ūnus complētus est</i> (2.7).'),
        ]),
        exercicio('Exercício 2 · A passiva do perfectum', 'Passe para a passiva do perfectum, com o agente em <i>ā/ab</i> + ablativo, e traduza.', [
            ('<i>Rōmulus urbem condidit.</i>', '<i>Urbs ā Rōmulō condita est.</i> "A cidade foi fundada por Rômulo." O particípio vai ao feminino singular, como <i>urbs</i>.'),
            ('<i>Rōmulus centum senātōrēs lēgit.</i>', '<i>Centum senātōrēs ā Rōmulō lēctī sunt.</i> "Cem senadores foram escolhidos por Rômulo." Masculino plural; <i>lēctum</i> é o supino de <i>legō</i>.'),
            ('<i>Rōmulus virginēs rapuit.</i>', '<i>Virginēs ā Rōmulō raptae sunt.</i> "As moças foram raptadas por Rômulo." Feminino plural.'),
            ('<i>Rōmulus Sabīnōs vīcit.</i>', '<i>Sabīnī ā Rōmulō victī sunt.</i> "Os sabinos foram vencidos por Rômulo."'),
            ('<i>Rōmulus multitūdinem fīnitimōrum recēperat.</i> (mais-que-perfeito)', '<i>Multitūdō fīnitimōrum ā Rōmulō recepta erat.</i> "Uma multidão de vizinhos tinha sido acolhida por Rômulo." O mais-que-perfeito passivo usa <i>erat</i>; o particípio concorda com <i>multitūdō</i> (feminino singular), não com <i>fīnitimōrum</i>.'),
        ]),
        exercicio('Exercício 3 · Datas', 'Converta as datas, mostrando a conta.', [
            ('O ano 245 a.u.c. (o fim da realeza)', '754 − 245 = 509 a.C.'),
            ('O ano 710 a.u.c. (a morte de César)', '754 − 710 = 44 a.C.'),
            ('O ano 1229 a.u.c. (o fim do Império do Ocidente)', 'É um ano depois de Cristo: 1229 − 753 = 476 d.C.'),
            ('<i>IX Kal. Iān.</i>', 'Dezembro tem 31 dias: 31 + 2 − 9 = 24 de dezembro.'),
            ('<i>Īdibus Mārtiīs</i>', 'Em março, os idos caem no dia 15: 15 de março. Não há conta, porque o dia é o próprio idos.'),
            ('Que ano a.u.c. corresponde a 63 a.C. (o consulado de Cícero)?', '754 − 63 = 691 a.u.c. (o exemplo de Allen e Greenough no § 630).'),
        ]),
        exercicio('Exercício 4 · Sintaxe', 'Diga a função de cada expressão e justifique.', [
            ('<i>annō rēgnī trīcēsimō septimō</i> (2.6)', 'Ablativo de tempo (quando?), sem preposição; <i>rēgnī</i> é genitivo que determina <i>annō</i>.'),
            ('<i>quōs senātōrēs</i> (2.2)', 'Dois acusativos com <i>nōmināvit</i>: <i>quōs</i> é o objeto, <i>senātōrēs</i> o predicativo do objeto ("chamou-os de senadores"), como em Bennett § 177.'),
            ('<i>vīcīnās urbī Rōmae</i> (2.3)', '<i>Urbī</i> é dativo regido pelo adjetivo <i>vīcīnās</i> (adjetivo de proximidade, Bennett § 192.1); <i>Rōmae</i> é aposto de <i>urbī</i>, também no dativo.'),
            ('<i>Rōmae</i> (2.7)', 'Locativo: "em Roma". Nomes de cidades da 1ª declinação no singular fazem o lugar onde com essa forma (Bennett § 232.1).'),
            ('<i>hīs rēgnantibus</i> (2.7)', 'Ablativo absoluto com particípio presente: ação simultânea, "enquanto estes (os senadores) reinavam".'),
            ('<i>ex nōmine suō</i> (2.1)', 'Origem, <i>ex</i> + ablativo; <i>suō</i> é reflexivo e se refere ao sujeito da oração, Rômulo: "a partir do seu próprio nome".'),
        ]),
        exercicio('Exercício 5 · Leitura de outros trechos de Eutrópio', 'Traduza estas frases autênticas do mesmo livro I (texto da The Latin Library, macrons acrescentados). Vocabulário: <i>cōnsulāris, -e</i>, consular; <i>cessō, -āre</i>, parar, ser interrompido; <i>rebellō, -āre</i>, rebelar-se.', [
            ('<i>Annō trecentēsimō et alterō ab urbe conditā imperium cōnsulāre cessāvit.</i> (I, 18)', '"No ano trezentos e dois desde a fundação da cidade, o poder consular foi interrompido." <i>Alterō</i> funciona como o ordinal "segundo"; o ano é 754 − 302 = 452 a.C., segundo a conta de Varrão.'),
            ('<i>Annō trecentēsimō et quīntō decimō ab urbe conditā Fīdēnātēs contrā Rōmānōs rebellāvērunt.</i> (I, 19)', '"No ano trezentos e quinze desde a fundação da cidade, os fidenates se rebelaram contra os romanos." Ablativo de tempo com ordinal composto; <i>contrā</i> + acusativo.'),
        ]),
        exercicio('Exercício 6 · Traduza para o latim', 'Use o vocabulário do capítulo; para "foi fundada", use <i>condita est</i>.', [
            ('Roma foi fundada por Rômulo.', '<i>Rōma ā Rōmulō condita est.</i> O particípio concorda com <i>Rōma</i> (feminino singular); o agente, pessoa, vai com <i>ā</i> + ablativo.'),
            ('Rômulo e Remo nasceram num só parto.', '<i>Rōmulus et Remus ūnō partū ēditī sunt.</i> Sujeito composto: particípio no masculino plural e <i>sunt</i>.'),
            ('Acreditou-se que Rômulo era filho de Marte.', '<i>Rōmulus Mārtis fīlius esse crēditus est</i> (construção pessoal, como em 2.6), ou, mais simples, <i>Rōmulus Mārtis fīlius putātus est</i>, "Rômulo foi considerado filho de Marte".'),
            ('No trigésimo sétimo ano, Rômulo não apareceu.', '<i>Annō trīcēsimō septimō Rōmulus nōn compāruit.</i> Ablativo de tempo com ordinal; perfeito de <i>compāreō</i>.'),
        ]),
    ],
    leituras=['eutropius-breviarium-ab-urbe-condita', 'lhomond-urbis-romae-viri-illustres-selecoes', 'nepos-vita-hannibalis', 'livius-ab-urbe-condita-liber-i', 'the-latin-library', 'bennett-new-latin-grammar'],
    leituras_nota='Continue no <i>Breviário</i> (no catálogo, a edição da DCC tem notas e vocabulário em inglês): leia I, 3–8, sobre os outros seis reis, que repetem o vocabulário e as construções deste capítulo. O <i>De viris illustribus urbis Romae</i>, de Lhomond, conta as mesmas histórias em latim ainda mais simples e é uma boa leitura paralela. A <i>Vida de Aníbal</i>, de Cornélio Nepos, é o passo seguinte na prosa histórica. Quando chegar ao capítulo 49, compare este trecho com a versão longa e literária de Tito Lívio (<i>Ab urbe condita</i> I, 4–16). Para as datas, Bennett § 371 traz a tabela completa do calendário romano.',
)
