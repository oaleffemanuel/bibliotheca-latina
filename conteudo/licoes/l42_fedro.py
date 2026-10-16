from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Texto latino: Fedro, Fabulae Aesopiae 1.1 (Lupus et agnus), ed. L. Mueller (Leipzig: Teubner, 1876),
# conferido no Perseus (Perseus:text:1999.02.0118) e na The Latin Library (phaedr1.html). Macrons acrescentados.
TEXTO = [
    ('1', 'Ad rīvum eundem lupus et agnus vēnerant,'),
    ('2', 'sitī compulsī. Superior stābat lupus,'),
    ('3', 'longēque īnferior agnus. Tunc fauce improbā'),
    ('4', 'latrō incitātus iūrgiī causam intulit:'),
    ('5', '"Cūr" inquit "turbulentam fēcistī mihi'),
    ('6', 'aquam bibentī?" Lāniger contrā timēns:'),
    ('7', '"Quī possum, quaesō, facere quod quereris, lupe?'),
    ('8', 'Ā tē dēcurrit ad meōs haustūs liquor."'),
    ('9', 'Repulsus ille vēritātis vīribus:'),
    ('10', '"Ante hōs sex mēnsēs male" ait "dīxistī mihi."'),
    ('11', 'Respondit agnus: "Equidem nātus nōn eram."'),
    ('12', '"Pater hercle tuus" ille inquit "male dīxit mihi";'),
    ('13', 'atque ita correptum lacerat iniūstā nece.'),
    ('14', 'Haec propter illōs scrīpta est hominēs fābula'),
    ('15', 'quī fictīs causīs innocentēs opprimunt.'),
]

LICAO = dict(
    slug='42-fedro', titulo='Fedro: uma fábula',
    titulo_latim='Phaedrus', tempo='75 min',
    resumo='Leitura comentada de uma fábula autêntica de Fedro, O lobo e o cordeiro (Fábulas 1.1): quem foi Fedro e o que é a fábula esópica, o texto latino com vocabulário e notas, o verso (o senário iâmbico, só como noção) e a ordem das palavras na poesia, a passiva do perfectum e os particípios em ação, a moral no fim da fábula (epimítio) e a tradução.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['Fedro', 'fábula esópica', 'Esopo', 'Lupus et agnus', 'promítio e epimítio', 'moral da fábula', 'senário iâmbico (noção)', 'ordem das palavras no verso', 'hipérbato', 'elipse do verbo', 'passiva do perfectum em texto', 'particípio perfeito em texto', 'presente histórico', 'discurso direto com inquit e ait', 'dativo de referência', 'ablativo de causa', 'leitura comentada'],
    prerequisitos=dict(texto='Capítulo 24: a passiva do perfectum (<i>scrīpta est</i>, "foi escrita"), que é a construção central desta leitura, e, por meio dela, os capítulos de morfologia nominal e verbal das partes I e II. Os particípios (capítulo 29), os depoentes (capítulo 25) e a métrica (capítulo 40) ajudam, mas tudo o que vem deles está explicado ou glosado aqui.',
                       licoes=['24-a-passiva-do-perfectum']),
    referencias=[
        referencia('Phaedrus, Fabulae Aesopiae, ed. L. Mueller (Leipzig: Teubner, 1876)', 'Fedro', catalogo='phaedrus-fabulae-aesopiae', url='https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0118:book=1:poem=1', nota='texto de 1.1 (Lupus et agnus), 1.4.1 (promítio), prólogo do livro I e prólogo do livro III, v. 17 (Pierio … iugo) conferidos no Perseus, que reproduz a edição de Mueller; 1.1 conferido também na The Latin Library (texto idêntico nas palavras); ortografia mantida, macrons e aspas acrescentados', tipo='dominio_publico'),
        referencia('Phaedrus, Fabulae, liber I (The Latin Library)', 'Fedro', url='https://www.thelatinlibrary.com/phaedr1.html', nota='prólogo do livro I, vv. 1–2 (Aesopus auctor quam materiam repperit, / hanc ego polivi versibus senariis), conferido nesta página e no TEI da Perseus (PerseusDL canonical-latinLit, phi0975.phi001, ed. Mueller): mesmas palavras', tipo='dominio_publico'),
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 102 (passiva de amō: amātus sum, amātus eram), § 113 (paradigmas de depoentes), § 188.1 (dativo de referência), § 219 (ablativo de causa), § 250.1 (concordância do relativo), § 251.4.a (antecedente incorporado na relativa que vem primeiro: quam … māteriam … hanc), § 259.3 (presente histórico), § 263 (mais-que-perfeito), §§ 348–349 (ordem normal e ênfase), § 350.11.a (hipérbato), §§ 366.2 e 366.8 (pés, cesura), § 370.1–2 (trímetro iâmbico ou senário)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 305 (o relativo concorda em gênero e número; o caso vem da sua oração), § 307.b (antecedente só dentro da relativa), §§ 376–377 (dativo de referência), § 404 (ablativo de causa), § 469 (presente histórico), § 477 (mais-que-perfeito), §§ 597–598 (ordem das palavras; 598.h, ordem entrelaçada nos poetas), § 599.c (inquit sempre intercalado)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 195 (concordância do relativo), § 479 (trímetro iâmbico ou senário: seis pés, espondeu nos ímpares, tribráquio)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 175 (concordância do pronome relativo), n. 408 (presente, inclusive o presente histórico), n. 536 (o verso jâmbico; o senário "tais são os versos das fábulas de Fedro", com o prólogo do livro I como exemplo)', tipo='dominio_publico'),
    ],
    objetivos=[
        'Situar Fedro e a fábula esópica e reconhecer a moral explícita no início (promítio) ou no fim (epimítio) de uma fábula.',
        'Ler o texto latino de <i>Lupus et agnus</i> (Fábulas 1.1) com o vocabulário e as notas, entendendo o enredo e o diálogo.',
        'Desfazer a ordem poética das palavras (hipérbato, elipse do verbo) e reconstruir a ordem da prosa.',
        'Identificar e traduzir no texto as formas da passiva do perfectum e os particípios perfeitos, dizendo com que palavra cada um concorda.',
        'Produzir uma tradução própria, fiel à função das palavras, e justificar as escolhas.',
    ],
    secoes=[
        ('Fedro e a fábula esópica', f'''
<p>Até aqui, quase todo o latim que você leu foi escrito para o livro ou retirado de frases isoladas. A partir deste capítulo começa a parte IV, <i>Auctōrēs</i>: a leitura de textos inteiros, como os romanos os escreveram. O primeiro autor é <b>Fedro</b> (<i>Phaedrus</i>), e a escolha não é casual. Suas fábulas são curtas, contam uma história com começo, meio e fim, têm diálogos vivos e uma moral explícita, e o vocabulário é concreto: animais, água, comida, medo. É o tipo de texto em que o leitor iniciante pode se apoiar no enredo para resolver a gramática.</p>
<p>Fedro viveu no início do Império, aproximadamente entre o reinado de Augusto e o de Cláudio (primeira metade do século I d.C.). Os manuscritos o chamam de <i>Augustī lībertus</i>, "liberto de Augusto": foi escravo na casa do imperador e recebeu a liberdade. Ele mesmo diz ter nascido na Piéria, região do norte da Grécia (prólogo do livro III, v. 17), e quase tudo o que se sabe da sua vida vem dos prólogos e epílogos que ele mesmo escreveu. A obra, em cinco livros, chegou até nós incompleta. Fedro não inventou as histórias: retomou a tradição grega das fábulas atribuídas a <b>Esopo</b> (<i>Aesōpus</i>), figura semilendária do século VI a.C., e lhes deu forma em versos latinos. É o que ele declara nos dois primeiros versos do prólogo do livro I:</p>
{exemplos([('Aesōpus auctor quam māteriam repperit,<br>hanc ego polīvī versibus sēnāriīs.', 'O assunto que Esopo, o criador, encontrou, eu o poli em versos senários. (Fábulas 1, prólogo, 1–2)')])}
<p>Repare na construção do primeiro verso, que é típica do latim e que você vai rever em César e em Cícero: a oração relativa vem <b>antes</b>, e o substantivo a que ela se refere está <b>dentro</b> dela (<i>quam māteriam … repperit</i>, "o assunto que … encontrou"); a oração principal retoma esse substantivo com um demonstrativo (<i>hanc</i>, "este", isto é, "este assunto"). Ao traduzir, o português prefere pôr o substantivo fora: "o assunto que Esopo encontrou, eu o poli". A gramática de Bennett descreve esse padrão no § 251.4.a.</p>
<p>Toda fábula esópica tem duas camadas: uma narrativa (os animais falam e agem como pessoas) e uma <b>moral</b>, a lição que a narrativa ilustra. Na tradição antiga, a moral podia vir declarada antes da história ou depois dela. A que vem antes chama-se <b>promítio</b> (do grego <i>promȳthion</i>, "o que se diz antes da fábula"); a que vem depois, <b>epimítio</b> ("o que se diz depois"). Fedro usa os dois. Compare o primeiro verso da fábula 1.4 (o cão que atravessa o rio com um pedaço de carne e larga a carne para pegar o reflexo dela) com os dois últimos versos da fábula que você vai ler:</p>
{tabela(['Posição', 'Texto', 'Tradução'], [
    ['<b>Promítio</b> (antes da história): Fábulas 1.4.1', '<i>Āmittit meritō proprium quī aliēnum adpetit.</i>', 'Perde com justiça o que é seu quem cobiça o alheio.'],
    ['<b>Epimítio</b> (depois da história): Fábulas 1.1.14–15', '<i>Haec propter illōs scrīpta est hominēs fābula / quī fictīs causīs innocentēs opprimunt.</i>', 'Esta fábula foi escrita por causa daqueles homens que oprimem os inocentes com pretextos inventados.'],
], 'A moral antes e depois da fábula')}
<p>No promítio de I, 4, <i>adpetit</i> é a grafia da edição para <i>appetit</i> (de <i>appetō</i>, "procurar alcançar, cobiçar"): o prefixo <i>ad-</i> às vezes aparece sem assimilação. E a oração <i>quī aliēnum adpetit</i> não tem antecedente expresso: "(aquele) que cobiça". O sujeito de <i>āmittit</i> é a própria relativa. Esse uso do relativo sem antecedente, que você conheceu no capítulo 16, é o modo latino de formular uma regra geral.</p>
{observacao('Por que começar pela fábula', 'Uma fábula é curta o bastante para ser lida inteira numa sessão e relida até ficar familiar. Faça assim: leia o texto em voz alta, depois o vocabulário, depois as notas, e só então tente uma tradução sua. A tradução deste capítulo está no fim, na seção 6, de propósito: compare-a com a sua depois de terminar, não antes.')}
'''),
        ('O texto: Lupus et agnus (Fábulas 1.1)', f'''
<p>O texto abaixo é o da edição de Lucian Mueller (Leipzig: Teubner, 1876), conferido no Perseus, que reproduz essa edição, e na The Latin Library, que traz as mesmas palavras. As únicas intervenções deste livro são os <b>macrons</b> (que nenhum manuscrito antigo tem), as aspas que marcam as falas, a numeração dos versos e alguns sinais de pontuação (Mueller põe ponto e vírgula depois de <i>compulsī</i> e ponto final depois de <i>intulit</i> e do v. 12; as palavras são as dele). São quinze versos: leia-os primeiro em voz alta, do começo ao fim, sem tentar traduzir, só para ouvir o ritmo e notar onde estão as falas (<i>inquit</i>, <i>ait</i>, "diz ele", aparecem sempre depois das primeiras palavras da fala).</p>
{tabela(['Verso', 'Texto latino (ed. Mueller, 1876)'], [[n, f'<span lang="la">{v}</span>'] for n, v in TEXTO], 'Fedro, Fábulas 1.1: Lupus et agnus', latim_cols=(1,))}
<p>A fábula tem uma estrutura clara, e reconhecê-la antes de traduzir ajuda muito. Os versos 1–4 são a <b>situação</b>: dois animais no mesmo riacho, um acima e outro abaixo, e um deles com más intenções. Os versos 5–12 são o <b>diálogo</b>, em três trocas: a acusação do lobo e a defesa do cordeiro (vv. 5–8); a segunda acusação e a segunda defesa (vv. 9–11); a terceira acusação, que já não espera resposta (v. 12). O verso 13 é o <b>desfecho</b>, numa só frase. Os versos 14–15 são a <b>moral</b>, o epimítio.</p>
{tabela(['Versos', 'Parte', 'Quem fala', 'O que acontece'], [
    ['1–4', 'situação', 'narrador', 'lobo e cordeiro bebem no mesmo riacho; o lobo, mais acima, procura um pretexto'],
    ['5–6', '1ª acusação', 'lobo', '"você turvou a minha água"'],
    ['6–8', '1ª defesa', 'cordeiro', 'a água corre de cima, do lobo, para baixo, até o cordeiro'],
    ['9–10', '2ª acusação', 'lobo', '"há seis meses você falou mal de mim"'],
    ['11', '2ª defesa', 'cordeiro', '"eu nem tinha nascido"'],
    ['12', '3ª acusação', 'lobo', '"então foi seu pai"'],
    ['13', 'desfecho', 'narrador', 'o lobo agarra e despedaça o cordeiro'],
    ['14–15', 'moral (epimítio)', 'narrador', 'a fábula serve para quem oprime inocentes com pretextos inventados'],
], 'A estrutura da fábula')}
{dica('<b>As falas.</b> <i>Inquit</i> ("diz", "disse") e <i>ait</i> (do verbo defectivo <i>aiō</i>, "dizer") nunca abrem a fala: vêm intercalados depois de uma ou mais palavras dela (Allen e Greenough § 599.c). Por isso <i>"Cūr" inquit "turbulentam fēcistī …"</i> se lê "Por que, disse, você turvou …". Quando você encontrar <i>inquit</i> no meio de uma frase, saiba que a fala começou um pouco antes.')}
'''),
        ('Vocabulário e notas', f'''
<p>A tabela dá cada palavra na forma em que aparece no texto, a entrada de dicionário e o sentido aqui. As palavras que você já conhece das partes I a III (<i>et</i>, <i>lupus</i>, <i>agnus</i>, <i>aqua</i>, <i>pater</i>, <i>fābula</i> etc.) também estão na tabela, para que ela sirva de glossário completo da fábula.</p>
{tabela(['No texto', 'Dicionário', 'Sentido aqui', 'Nota'], [
    ['ad rīvum', 'rīvus, -ī (m.)', 'riacho, regato', '<i>ad</i> + acusativo: direção'],
    ['eundem', 'īdem, eadem, idem', 'o mesmo', 'acusativo masc. sing., concorda com <i>rīvum</i> (capítulo 15)'],
    ['vēnerant', 'veniō, -īre, vēnī, ventum', 'tinham chegado', 'mais-que-perfeito: a chegada é anterior à cena'],
    ['sitī', 'sitis, -is (f.)', 'sede', 'ablativo em <i>-ī</i> (tema em <i>-i</i>, capítulo 10): causa'],
    ['compulsī', 'compellō, -ere, compulī, compulsum', 'impelir, levar à força', 'particípio perfeito, nom. pl. masc.: "levados"'],
    ['superior, īnferior', 'superior, -ius; īnferior, -ius', 'mais acima; mais abaixo', 'comparativos (capítulo 18), usados como predicativos'],
    ['stābat', 'stō, stāre, stetī, statum', 'estar (de pé), ficar', 'imperfeito: descrição da cena'],
    ['longē', 'advérbio', 'muito, bem (reforça o comparativo)', '<i>longē īnferior</i>: "bem mais abaixo"'],
    ['tunc', 'advérbio', 'então', 'marca a passagem da situação à ação'],
    ['fauce improbā', 'faux, faucis (f.); improbus, -a, -um', 'goela; insaciável, perverso', 'ablativo de causa: "pela goela insaciável", isto é, pela fome'],
    ['latrō', 'latrō, -ōnis (m.)', 'bandido, salteador', 'o lobo, chamado pelo que é'],
    ['incitātus', 'incitō, -āre, -āvī, -ātum', 'instigar', 'particípio perfeito, concorda com <i>latrō</i>'],
    ['iūrgiī', 'iūrgium, -ī (n.)', 'briga, disputa', 'genitivo: "motivo <b>de briga</b>"'],
    ['causam intulit', 'causa, -ae; īnferō, īnferre, intulī, illātum', 'apresentou um motivo', '<i>ferō</i> e compostos: capítulo 26'],
    ['inquit', 'inquam (defectivo)', 'diz, disse', 'sempre intercalado na fala'],
    ['turbulentam', 'turbulentus, -a, -um', 'turvo, lamacento', 'predicativo do objeto: "tornaste a água turva"'],
    ['fēcistī', 'faciō, -ere, fēcī, factum', 'fizeste, tornaste', 'perfeito, 2ª sing.'],
    ['mihi … bibentī', 'ego; bibō, -ere, bibī', 'para mim que estou bebendo', 'dativo de referência; <i>bibentī</i> é particípio presente (capítulo 29)'],
    ['lāniger', 'lāniger, -era, -erum', 'lanígero, que tem lã', 'adjetivo usado como nome: "o lanudo", o cordeiro'],
    ['contrā', 'advérbio', 'em resposta, por sua vez', 'aqui não é preposição'],
    ['timēns', 'timeō, -ēre, timuī', 'temendo, com medo', 'particípio presente, concorda com <i>lāniger</i>; subentenda "disse"'],
    ['quī', 'advérbio interrogativo', 'como?', 'forma antiga de ablativo; não é o relativo'],
    ['possum', 'possum, posse, potuī', 'posso', 'capítulo 26'],
    ['quaesō', 'quaesō (defectivo)', 'por favor, peço', 'fórmula de cortesia intercalada'],
    ['quod', 'quī, quae, quod', 'aquilo que, o que', 'relativo sem antecedente: objeto de <i>facere</i>'],
    ['quereris', 'queror, querī, questus sum', 'queixas-te, reclamas', 'depoente (capítulo 25), presente, 2ª sing.'],
    ['lupe', 'lupus, -ī', 'ó lobo', 'vocativo'],
    ['dēcurrit', 'dēcurrō, -ere, dēcurrī, dēcursum', 'corre para baixo, desce', 'presente'],
    ['haustūs', 'haustus, -ūs (m.)', 'o beber; o lugar onde se bebe', '4ª declinação, acusativo plural (capítulo 11)'],
    ['liquor', 'liquor, -ōris (m.)', 'líquido, água', 'sujeito de <i>dēcurrit</i>, no fim do verso'],
    ['repulsus', 'repellō, -ere, reppulī, repulsum', 'repelir, rebater', 'particípio perfeito, concorda com <i>ille</i> (o lobo)'],
    ['vēritātis vīribus', 'vēritās, -ātis (f.); vīs, vīs (f.), pl. vīrēs, vīrium', 'pela força da verdade', '<i>vīribus</i>: ablativo de meio (de <i>vīrēs</i>)'],
    ['ante hōs sex mēnsēs', 'ante + ac.; hīc, haec, hōc; mēnsis, -is (m.)', 'há seis meses', 'literalmente "antes destes seis meses"'],
    ['male … dīxistī mihi', 'male dīcō + dativo', 'falaste mal de mim', 'daí <i>maldizer</i>; o dativo indica de quem se fala mal'],
    ['ait', 'aiō (defectivo)', 'diz, disse', 'intercalado como <i>inquit</i>'],
    ['equidem', 'advérbio', 'mas eu, de minha parte', 'reforça a 1ª pessoa'],
    ['nātus nōn eram', 'nāscor, nāscī, nātus sum', 'eu não tinha nascido', 'depoente: mais-que-perfeito com forma passiva e sentido ativo'],
    ['hercle', 'interjeição', 'por Hércules!', 'juramento coloquial'],
    ['correptum', 'corripiō, -ere, corripuī, correptum', 'agarrar, arrebatar', 'particípio perfeito, acusativo masc.: subentende-se <i>agnum</i>'],
    ['lacerat', 'lacerō, -āre', 'despedaça, dilacera', 'presente histórico'],
    ['iniūstā nece', 'iniūstus, -a, -um; nex, necis (f.)', 'com morte injusta', 'ablativo de modo'],
    ['propter', 'preposição + acusativo', 'por causa de', 'aqui separada do seu nome: <i>propter illōs … hominēs</i>'],
    ['scrīpta est', 'scrībō, -ere, scrīpsī, scrīptum', 'foi escrita', 'passiva do perfectum (capítulo 24), concorda com <i>fābula</i>'],
    ['fictīs causīs', 'fingō, -ere, fīnxī, fictum', 'com pretextos inventados', 'particípio perfeito como adjetivo; ablativo de meio'],
    ['innocentēs', 'innocēns, -entis', 'inocentes', 'adjetivo usado como nome; acusativo plural'],
    ['opprimunt', 'opprimō, -ere, oppressī, oppressum', 'oprimem, esmagam', 'presente de verdade geral'],
], 'Vocabulário da fábula', latim_cols=(0, 1))}
<h3>Notas aos versos</h3>
<p><b>vv. 1–2.</b> O mais-que-perfeito <i>vēnerant</i> põe a chegada antes do momento em que a cena começa: quando a história se abre, os dois já estão no riacho. <i>Sitī compulsī</i>, "levados pela sede", explica por que vieram: <i>sitī</i> é ablativo de causa (Bennett § 219), e <i>compulsī</i>, nominativo plural masculino, concorda com os dois sujeitos juntos, <i>lupus et agnus</i>. <b>vv. 2–3.</b> <i>Superior stābat lupus, longēque īnferior agnus</i>: o verbo está só na primeira oração, e a segunda o subentende ("e o cordeiro [estava] bem mais abaixo"). Esse detalhe topográfico é o eixo da fábula: a água desce do lobo para o cordeiro, e por isso a primeira acusação é absurda. <b>vv. 3–4.</b> <i>Fauce improbā</i> é a "goela insaciável": o lobo é movido pela fome, e a palavra <i>latrō</i>, "bandido", já o julga antes da fala. <i>Iūrgiī causam intulit</i>: "apresentou um motivo de briga", isto é, inventou um pretexto.</p>
<p><b>vv. 5–6.</b> <i>Turbulentam fēcistī … aquam</i>: <i>facere</i> com objeto e adjetivo predicativo significa "tornar": "tornaste a água turva". <i>Mihi bibentī</i>: dativo de referência ("para mim, que estou bebendo"), a pessoa afetada pela ação (Bennett § 188.1). <b>vv. 6–8.</b> <i>Contrā</i> é advérbio ("em resposta"), e o verbo de dizer fica subentendido. <i>Quī possum … facere</i>: <i>quī</i> é aqui o advérbio interrogativo "como?". <i>Quod quereris</i>: "aquilo de que você se queixa"; <i>quod</i> não tem antecedente, e a relativa inteira é o objeto de <i>facere</i>. O verso 8 é o argumento do cordeiro, construído para fazer ver o caminho da água: <i>Ā tē</i> (de você) <i>dēcurrit</i> (desce) <i>ad meōs haustūs</i> (até onde eu bebo) <i>liquor</i> (a água).</p>
<p><b>vv. 9–10.</b> <i>Repulsus ille vēritātis vīribus</i>: "ele, rebatido pela força da verdade". <i>Ille</i> é o lobo; o particípio <i>repulsus</i> concorda com ele, e a frase não tem verbo próprio: o verbo de dizer é o <i>ait</i> do verso seguinte. <i>Ante hōs sex mēnsēs</i>, "há seis meses", é expressão de tempo com <i>ante</i> e acusativo (capítulo 19). <b>v. 11.</b> <i>Equidem nātus nōn eram</i>: <i>nāscor</i> é depoente, e o mais-que-perfeito <i>nātus eram</i> tem forma passiva e sentido ativo, "eu tinha nascido" (capítulo 25). <b>vv. 12–13.</b> O lobo desiste de argumentar. <i>Correptum</i> é um particípio no acusativo masculino sem nome expresso: o leitor subentende o cordeiro, objeto de <i>lacerat</i> ("e assim, agarrado, o despedaça", isto é, "agarra-o e despedaça-o"). O presente <i>lacerat</i>, no meio de uma narração no passado, é o <b>presente histórico</b>, que torna o desfecho mais vivo (Bennett § 259.3; Allen e Greenough § 469).</p>
'''),
        ('Verso e ordem das palavras', f'''
<p>A fábula é um poema, e duas consequências disso afetam a leitura: o ritmo e a ordem das palavras. Comecemos pelo ritmo, mas só como noção, porque a métrica é assunto do capítulo 40.</p>
{observacao('O senário iâmbico, em uma noção', 'Fedro escreve em <b>senários iâmbicos</b> (<i>versūs sēnāriī</i>, como ele mesmo diz no prólogo): versos de <b>seis pés</b>, cujo pé básico é o <b>iambo</b>, uma sílaba breve seguida de uma longa (u –). Na prática, Fedro substitui muitos iambos por pés equivalentes, sobretudo nos lugares ímpares (1º, 3º e 5º), e por isso o verso soa mais como fala ritmada do que como canção; mas o <b>último pé</b> é sempre um iambo, e o verso termina com o compasso "breve-longa": <i>…ne-<b>rant</b></i> (v. 1), <i>…pro-<b>bā</b></i> (v. 3), <i>…pri-<b>munt</b></i> (v. 15). O Pe. Ravizza (n. 536) dá os senários de Fedro como exemplo do verso; Bennett (§ 370) e Kennedy (§ 479) descrevem as substituições permitidas. Para ler a fábula, basta saber que existe um ritmo; escandir o verso é tarefa do capítulo 40.')}
<p>A segunda consequência é mais importante para quem traduz. Na prosa, como você viu no capítulo 22, o latim tende a pôr o sujeito no início e o verbo no fim, e a manter juntas as palavras que formam um grupo (o nome e o seu adjetivo, a preposição e o seu caso). No verso, o poeta distribui as palavras pelas posições que o ritmo pede e pelas que dão ênfase, e com frequência <b>separa</b> palavras que gramaticalmente andam juntas. Essa separação chama-se <b>hipérbato</b> (Bennett § 350.11.a). O hipérbato nunca é desordem: a concordância (gênero, número e caso) diz o tempo todo o que se liga a quê. A tarefa do leitor é refazer os pares.</p>
{comparacao('Do verso à ordem da prosa', ['Verso (ordem de Fedro)', 'O que está separado', 'Ordem da prosa'], [
    ['turbulentam fēcistī mihi / aquam bibentī', '<i>turbulentam … aquam</i>; <i>mihi … bibentī</i>; o par atravessa o fim do verso', '<i>mihi bibentī aquam turbulentam fēcistī</i>'],
    ['Tunc fauce improbā / latrō incitātus iūrgiī causam intulit', 'o ablativo de causa vem antes do sujeito que ele explica', '<i>Tunc latrō, fauce improbā incitātus, causam iūrgiī intulit</i>'],
    ['Ā tē dēcurrit ad meōs haustūs liquor', 'o sujeito <i>liquor</i> fica para o fim, como uma conclusão', '<i>Liquor ā tē ad meōs haustūs dēcurrit</i>'],
    ['Pater hercle tuus … male dīxit mihi', '<i>pater … tuus</i>, com a interjeição no meio', '<i>Pater tuus mihi male dīxit</i>'],
    ['Haec propter illōs scrīpta est hominēs fābula', 'dois pares entrelaçados: <i>haec … fābula</i> e <i>propter illōs … hominēs</i>', '<i>Haec fābula scrīpta est propter illōs hominēs</i>'],
])}
<p>O último exemplo merece atenção, porque é o mais difícil e o mais bonito. <i>Haec</i> abre o verso e só encontra o seu nome, <i>fābula</i>, na última palavra; dentro desse par, <i>propter illōs</i> só encontra <i>hominēs</i> depois de <i>scrīpta est</i>. As palavras se entrelaçam (A B verbo B A), e o resultado é que a frase inteira fica "presa" entre <i>haec</i> e <i>fābula</i>, e o verso seguinte, que começa com <i>quī</i>, se liga a <i>hominēs</i>, a palavra que ficou mais perto. Para desfazer, pergunte: <i>haec</i> é nominativo feminino singular ou neutro plural; que nome feminino singular há no verso? <i>Fābula</i>. <i>Illōs</i> é acusativo masculino plural; que nome no mesmo caso, gênero e número? <i>Hominēs</i>. E <i>quī</i>, nominativo masculino plural, refere-se ao único nome masculino plural disponível: <i>hominēs</i>.</p>
{dica('<b>Procedimento para o verso.</b> (1) Ache os verbos e conte as orações. (2) Para cada adjetivo, pronome ou particípio, procure o nome com o mesmo gênero, número e caso, mesmo que esteja na linha seguinte. (3) Para cada preposição, ache o seu caso. (4) Só então escreva a frase na ordem da prosa e traduza. A elipse também é comum: em <i>Superior stābat lupus, longēque īnferior agnus</i>, o segundo membro subentende <i>stābat</i>; em <i>Lāniger contrā timēns</i>, falta o verbo de dizer, que o leitor supre pela fala que vem a seguir.')}
'''),
        ('A passiva do perfectum e os particípios na fábula', f'''
<p>O pré-requisito deste capítulo é o capítulo 24, e a razão está à vista: a fábula está cheia de <b>particípios perfeitos</b>, tanto dentro da passiva do perfectum quanto sozinhos, concordando com um nome. Reconhecê-los é o principal trabalho gramatical desta leitura. Lembre a regra do capítulo 24: o perfeito passivo é formado pelo particípio perfeito (o quarto elemento das partes principais) mais uma forma de <i>sum</i>, e o particípio concorda com o sujeito em gênero e número (<i>fābula scrīpta est</i>, "a fábula foi escrita"; <i>lupī incitātī sunt</i>, "os lobos foram instigados").</p>
{tabela(['No texto', 'Verbo (partes principais)', 'Forma', 'Concorda com', 'Tradução'], [
    ['<b>scrīpta est</b> (v. 14)', 'scrībō, scrīpsī, <b>scrīptum</b>', 'perfeito do indicativo passivo, 3ª sing., feminino', '<i>fābula</i> (sujeito)', '"foi escrita"'],
    ['<b>nātus</b> nōn <b>eram</b> (v. 11)', 'nāscor, nāscī, <b>nātus sum</b> (depoente)', 'mais-que-perfeito do indicativo, 1ª sing., masculino', 'o cordeiro, sujeito de <i>eram</i>', '"eu não tinha nascido" (sentido ativo)'],
    ['<b>compulsī</b> (v. 2)', 'compellō, compulī, <b>compulsum</b>', 'particípio perfeito, nom. pl. masc.', '<i>lupus et agnus</i>', '"levados (pela sede)"'],
    ['<b>incitātus</b> (v. 4)', 'incitō, incitāvī, <b>incitātum</b>', 'particípio perfeito, nom. sing. masc.', '<i>latrō</i>', '"instigado"'],
    ['<b>repulsus</b> (v. 9)', 'repellō, reppulī, <b>repulsum</b>', 'particípio perfeito, nom. sing. masc.', '<i>ille</i> (o lobo)', '"rebatido"'],
    ['<b>correptum</b> (v. 13)', 'corripiō, corripuī, <b>correptum</b>', 'particípio perfeito, ac. sing. masc.', 'o cordeiro, subentendido (objeto de <i>lacerat</i>)', '"agarrado"'],
    ['<b>fictīs</b> (v. 15)', 'fingō, fīnxī, <b>fictum</b>', 'particípio perfeito, abl. pl. fem.', '<i>causīs</i>', '"inventados"'],
], 'Os particípios perfeitos de Lupus et agnus')}
<p>Duas observações. Primeira: em <i>scrīpta est</i> e em <i>nātus eram</i>, o particípio é parte de uma forma verbal composta; nos outros cinco casos, ele está sozinho e funciona como um adjetivo ligado a um nome, com o sentido passivo e anterior que você conhece do capítulo 24: "levados", "instigado", "rebatido", "agarrado", "inventados". O capítulo 29 chama esse uso de <b>particípio conjunto</b> e mostra como traduzi-lo de várias maneiras; aqui, basta o particípio passado português ("rebatido pela força da verdade, ele disse"). Segunda: <i>nātus eram</i> é a exceção que confirma a regra. <i>Nāscor</i> é depoente, e por isso o seu "passivo" tem sentido ativo: <i>nātus eram</i> não é "eu tinha sido nascido", e sim "eu tinha nascido".</p>
<p>A fábula também usa os tempos do indicativo com muita precisão, e vale reparar como cada um tem a sua função na narrativa:</p>
{tabela(['Tempo', 'Exemplo', 'Função na fábula'], [
    ['mais-que-perfeito', '<i>vēnerant</i>, <i>nātus nōn eram</i>', 'o que já tinha acontecido antes do momento da cena'],
    ['imperfeito', '<i>stābat</i>', 'o cenário, a situação que dura'],
    ['perfeito', '<i>intulit</i>, <i>fēcistī</i>, <i>dīxistī</i>, <i>respondit</i>, <i>dīxit</i>', 'as ações que fazem a história avançar'],
    ['presente histórico', '<i>lacerat</i>', 'o golpe final, contado como se acontecesse diante do leitor'],
    ['presente de verdade geral', '<i>opprimunt</i> (v. 15), <i>dēcurrit</i> (v. 8)', 'o que vale sempre: a moral; o curso natural da água'],
], 'Os tempos verbais da fábula')}
{observacao('Duas formas que você ainda pode não ter visto', 'O texto traz dois <b>particípios presentes</b>: <i>bibentī</i> (dativo, "a mim que estou bebendo") e <i>timēns</i> (nominativo, "com medo"). Eles se formam do tema do presente com <i>-ns, -ntis</i> e se declinam como adjetivos da terceira declinação; o capítulo 29 os estuda. E <i>īnferō, īnferre, intulī, illātum</i> é um composto de <i>ferō</i> (capítulo 26), cujo perfeito vem de outra raiz: daí <i>intulit</i>, "apresentou", sem nenhuma semelhança com <i>īnferre</i>.')}
'''),
        ('Análise, tradução e moral', f'''
<p>Os dois versos finais, o epimítio, reúnem o que este capítulo trabalhou: a passiva do perfectum, um particípio perfeito com valor de adjetivo, o hipérbato e uma oração relativa. Analise-os palavra a palavra.</p>
{analise('Fedro, Fábulas 1.1.14–15', [
    ('Haec', 'hīc, haec, hōc, este', 'nominativo singular feminino', 'determina <i>fābula</i> (separado dele pelo hipérbato)'),
    ('propter', 'propter (preposição + acusativo)', 'invariável', 'introduz a causa: "por causa de"'),
    ('illōs', 'ille, illa, illud, aquele', 'acusativo plural masculino', 'determina <i>hominēs</i>'),
    ('scrīpta est', 'scrībō, -ere, scrīpsī, scrīptum', 'perfeito do indicativo passivo, 3ª sing.; particípio no feminino', 'verbo da oração principal: "foi escrita"'),
    ('hominēs', 'homō, hominis (m.), ser humano', 'acusativo plural', 'regido por <i>propter</i>; antecedente de <i>quī</i>'),
    ('fābula', 'fābula, -ae (f.), fábula', 'nominativo singular', 'sujeito de <i>scrīpta est</i>'),
    ('quī', 'quī, quae, quod (relativo)', 'nominativo plural masculino', 'sujeito de <i>opprimunt</i>; refere-se a <i>hominēs</i>'),
    ('fictīs', 'fingō, -ere, fīnxī, fictum, inventar', 'particípio perfeito, ablativo plural feminino', 'concorda com <i>causīs</i>: "inventados"'),
    ('causīs', 'causa, -ae (f.), causa, pretexto', 'ablativo plural', 'meio: "com pretextos"'),
    ('innocentēs', 'innocēns, -entis, inocente', 'acusativo plural, usado como nome', 'objeto de <i>opprimunt</i>'),
    ('opprimunt', 'opprimō, -ere, oppressī, oppressum, oprimir', 'presente do indicativo ativo, 3ª pl.', 'verbo da relativa; presente de verdade geral'),
])}
<p>O relativo <i>quī</i> segue a regra que você aprendeu no capítulo 16: concorda com o antecedente em gênero e número (masculino plural, como <i>hominēs</i>), mas o seu caso vem da função na própria oração (nominativo, porque é sujeito de <i>opprimunt</i>), e não do caso do antecedente, que é acusativo (Bennett § 250.1; Allen e Greenough § 305). Desfeito o hipérbato, a estrutura do período é simples:</p>
{diagrama_frase([('Haec fābula', 'sujeito · nom. sing. f.'), ('scrīpta est', 'passiva do perfectum · "foi escrita"'), ('propter illōs hominēs', 'causa · propter + acusativo'), ('quī … opprimunt', 'oração relativa · sujeito quī = hominēs')],
    'Ordem da prosa: <i>Haec fābula scrīpta est propter illōs hominēs quī fictīs causīs innocentēs opprimunt.</i>')}
<p>A moral é uma chave de leitura política. O lobo não precisa de razões: ele procura pretextos (<i>iūrgiī causam</i>, v. 4; <i>fictīs causīs</i>, v. 15), e cada vez que a verdade os desfaz, inventa outro, até desistir de fingir. A palavra <i>causa</i> volta no começo e no fim, e o eco não é acaso: a fábula é sobre o poder que finge ter motivos. Leia agora a tradução deste livro e compare-a com a sua.</p>
{tabela(['Versos', 'Tradução (Bibliotheca Latina)'], [
    ['1–4', 'Ao mesmo riacho tinham chegado um lobo e um cordeiro, levados pela sede. Mais acima estava o lobo, e bem mais abaixo o cordeiro. Então o bandido, instigado pela goela insaciável, inventou um motivo de briga.'],
    ['5–8', '"Por que", disse ele, "você turvou a água em que eu estou bebendo?" O lanudo, com medo, respondeu: "Como posso, por favor, fazer isso de que você se queixa, lobo? É de você que a água desce até onde eu bebo."'],
    ['9–11', 'Rebatido pela força da verdade, o lobo disse: "Há seis meses você falou mal de mim." O cordeiro respondeu: "Mas eu nem tinha nascido."'],
    ['12–13', '"Então, por Hércules, foi o seu pai que falou mal de mim", disse ele; e assim o agarra e o despedaça, numa morte injusta.'],
    ['14–15', 'Esta fábula foi escrita por causa daqueles homens que oprimem os inocentes com pretextos inventados.'],
], 'Tradução de Fábulas 1.1')}
<p>Algumas escolhas da tradução, para você comparar. <i>Fēcistī turbulentam</i> virou "turvou" (um só verbo português para "tornar turvo"). <i>Contrā</i> virou "respondeu", porque o português precisa do verbo que o latim subentende. <i>Equidem</i> virou "mas eu", que dá a ênfase na primeira pessoa. E <i>correptum lacerat</i> virou "o agarra e o despedaça": o particípio perfeito latino, anterior ao verbo principal, costuma virar em português um verbo coordenado. Uma tradução mais literal ("agarrado, despedaça-o") também estaria certa, mas soa menos natural.</p>
<h3>Resumo</h3>
<ul>
<li>Fedro, liberto de Augusto, pôs em senários iâmbicos latinos as fábulas da tradição de Esopo; a moral vem antes (promítio) ou depois (epimítio) da história.</li>
<li><i>Lupus et agnus</i> tem situação (vv. 1–4), diálogo em três trocas (vv. 5–12), desfecho (v. 13) e epimítio (vv. 14–15).</li>
<li>No verso, palavras que andam juntas podem ficar separadas (hipérbato); a concordância de gênero, número e caso refaz os pares.</li>
<li>A passiva do perfectum (<i>scrīpta est</i>) e os particípios perfeitos (<i>compulsī, incitātus, repulsus, correptum, fictīs</i>) concordam com o nome a que se referem; <i>nātus eram</i>, de um depoente, tem sentido ativo.</li>
<li>Os tempos organizam a narrativa: mais-que-perfeito (o antes), imperfeito (o cenário), perfeito (a ação), presente histórico (o clímax), presente de verdade geral (a moral).</li>
</ul>
<p>No próximo capítulo, a prosa histórica de Eutrópio conta a fundação de Roma em frases curtas, cheias de nomes, datas e verbos na passiva do perfectum.</p>
'''),
    ],
    erros_comuns=[
        ('Ligar <i>haec</i> a <i>hominēs</i> ou a <i>propter</i>, porque estão perto: "por causa destes homens…".', '<i>Haec</i> é feminino singular (ou neutro plural); <i>hominēs</i> é masculino plural. O par certo é <i>haec … fābula</i>, no começo e no fim do verso. No verso, a proximidade não prova nada: quem decide é a concordância. Antes de traduzir, ligue cada pronome e adjetivo ao nome com o mesmo gênero, número e caso.'),
        ('Traduzir <i>quī possum</i> como "que posso" ou "o qual posso".', 'Aqui <i>quī</i> é o advérbio interrogativo "como?", uma forma antiga de ablativo. O relativo não faz sentido, porque não há antecedente nem oração principal. A pergunta do cordeiro é "Como posso fazer…?". O contexto (uma fala que começa com uma pergunta) é a pista.'),
        ('Entender <i>nātus nōn eram</i> como passivo ("eu não tinha sido nascido") ou como presente.', '<i>Nāscor</i> é depoente: forma passiva, sentido ativo (capítulo 25). <i>Nātus eram</i> é mais-que-perfeito: "eu tinha nascido". O tempo importa para o argumento: seis meses antes, o cordeiro ainda não existia.'),
        ('Procurar um sujeito diferente para <i>lacerat</i>, ou traduzi-lo como presente ("despedaça") num texto todo no passado sem perceber a mudança.', 'O sujeito continua sendo o lobo (<i>ille</i>, v. 12). <i>Lacerat</i> é presente histórico: um presente usado na narração de um fato passado para torná-lo vivo. Em português, você pode manter o presente ("e assim o agarra e o despedaça") ou passar ao pretérito ("agarrou-o e despedaçou-o"); as duas soluções são corretas, desde que coerentes.'),
        ('Tomar <i>sitī</i> por dativo e <i>vīribus</i> por dativo: "chegaram à sede", "rebatido para as forças".', '<i>Sitis</i> é tema em <i>-i</i> (capítulo 10) e tem ablativo <i>sitī</i>; aqui o ablativo indica a causa ("levados pela sede"). <i>Vīribus</i>, de <i>vīrēs</i> (plural de <i>vīs</i>), é ablativo de meio ("pela força"). Com particípios passivos como <i>compulsī</i> e <i>repulsus</i>, um ablativo sem preposição costuma dizer por quê ou com quê a ação se deu.'),
        ('Ler <i>contrā</i> como preposição e procurar o acusativo: "contra o medo".', '<i>Contrā</i> pode ser preposição ou advérbio. Aqui não há acusativo que ele possa reger (<i>timēns</i> é nominativo e concorda com <i>lāniger</i>): é advérbio, "em resposta, por sua vez".'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · A situação (vv. 1–4)',
            'Leia os versos 1–4 e traduza seguindo os passos: <i lang="la">Ad rīvum eundem lupus et agnus vēnerant, / sitī compulsī. Superior stābat lupus, / longēque īnferior agnus. Tunc fauce improbā / latrō incitātus iūrgiī causam intulit.</i>', [
            ('Quantos verbos conjugados há, e quais são?', 'Três: <i>vēnerant</i> (mais-que-perfeito, 3ª pl.), <i>stābat</i> (imperfeito, 3ª sing.) e <i>intulit</i> (perfeito, 3ª sing., de <i>īnferō</i>). <i>Compulsī</i> e <i>incitātus</i> são particípios, não verbos conjugados. Logo, há três orações, mais uma quarta com o verbo subentendido (<i>longē īnferior agnus</i> [<i>stābat</i>]).'),
            ('Qual é o sujeito de <i>vēnerant</i>, e por que o verbo está no plural?', '<i>Lupus et agnus</i>, dois sujeitos singulares unidos por <i>et</i>, levam o verbo ao plural (capítulo 22). <i>Ad rīvum eundem</i> é a direção: "ao mesmo riacho".'),
            ('Com que concorda <i>compulsī</i>, e que caso é <i>sitī</i>?', '<i>Compulsī</i> é nominativo plural masculino: concorda com <i>lupus et agnus</i>, o sujeito composto. <i>Sitī</i> é ablativo de <i>sitis</i> (tema em <i>-i</i>), de causa: "levados pela sede".'),
            ('Como se lê <i>Superior stābat lupus, longēque īnferior agnus</i>?', 'Duas orações em paralelo, a segunda sem verbo: "O lobo estava mais acima, e o cordeiro (estava) bem mais abaixo". <i>Superior</i> e <i>īnferior</i> são comparativos usados como predicativos; <i>longē</i> intensifica o comparativo.'),
            ('Desfaça a ordem de <i>Tunc fauce improbā latrō incitātus iūrgiī causam intulit</i>.', 'Sujeito: <i>latrō</i>. Particípio que concorda com ele: <i>incitātus</i>. Ablativo que acompanha o particípio: <i>fauce improbā</i> (causa). Objeto: <i>causam</i>, com o genitivo <i>iūrgiī</i>. Prosa: <i>Tunc latrō, fauce improbā incitātus, causam iūrgiī intulit.</i>'),
            ('Monte a tradução.', '"Ao mesmo riacho tinham chegado um lobo e um cordeiro, levados pela sede. O lobo estava mais acima, e o cordeiro bem mais abaixo. Então o bandido, instigado pela goela insaciável, apresentou um motivo de briga."'),
        ]),
        pratica_guiada('Prática guiada 2 · A primeira defesa (vv. 6–8)',
            'Traduza a fala do cordeiro: <i lang="la">Lāniger contrā timēns: "Quī possum, quaesō, facere quod quereris, lupe? Ā tē dēcurrit ad meōs haustūs liquor."</i>', [
            ('Há um verbo na frase introdutória <i>Lāniger contrā timēns</i>?', 'Não há verbo conjugado. <i>Lāniger</i> (o lanígero, o cordeiro) é o sujeito; <i>timēns</i> é particípio presente que concorda com ele ("com medo"); <i>contrā</i> é advérbio. O verbo de dizer fica subentendido: "O cordeiro, com medo, (respondeu):".'),
            ('Que palavra é <i>quī</i>, e qual é o objeto de <i>facere</i>?', '<i>Quī</i> é o advérbio interrogativo "como?". O objeto de <i>facere</i> é a oração relativa <i>quod quereris</i>, "aquilo de que você se queixa": <i>quod</i> não tem antecedente expresso. <i>Quaesō</i> ("por favor") e <i>lupe</i> (vocativo) estão intercalados.'),
            ('Que forma é <i>quereris</i>?', 'Presente do indicativo, 2ª pessoa do singular, do depoente <i>queror, querī, questus sum</i>: forma passiva (<i>-ris</i>), sentido ativo, "você se queixa".'),
            ('Qual é o sujeito de <i>dēcurrit</i>?', '<i>Liquor</i>, a última palavra do verso. <i>Ā tē</i> é a origem ("de você"), <i>ad meōs haustūs</i> o destino ("até o lugar onde eu bebo"). O sujeito no fim dá ao argumento a forma de uma demonstração.'),
            ('Monte a tradução.', '"O lanudo, com medo, respondeu: Como posso, por favor, fazer isso de que você se queixa, lobo? É de você que a água desce até onde eu bebo."'),
        ], 'Conclusão: numa fala, comece pelas palavras intercaladas (<i>inquit, quaesō</i>, vocativos) e retire-as; o que sobra é uma frase comum.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Compreensão', 'Responda em português, citando a palavra ou o verso latino que justifica a resposta.', [
            ('Por que o lobo e o cordeiro foram ao riacho?', 'Por causa da sede: <i>sitī compulsī</i> (v. 2), "levados pela sede".'),
            ('Por que a primeira acusação do lobo é absurda?', 'Porque o lobo está mais acima (<i>superior</i>, v. 2) e o cordeiro bem mais abaixo (<i>longē īnferior</i>, v. 3), e a água desce do lobo para o cordeiro (<i>Ā tē dēcurrit ad meōs haustūs liquor</i>, v. 8). A água passa primeiro pelo lobo e só depois chega ao cordeiro: o cordeiro não pode turvar a água que o lobo bebe.'),
            ('Como o cordeiro desfaz a segunda acusação?', 'Dizendo que ainda não tinha nascido seis meses antes: <i>Equidem nātus nōn eram</i> (v. 11).'),
            ('O que o lobo faz quando a terceira acusação não pode ser refutada?', 'Ele nem espera resposta: agarra e despedaça o cordeiro (<i>correptum lacerat iniūstā nece</i>, v. 13).'),
            ('A moral desta fábula é um promítio ou um epimítio? Por quê?', 'Um epimítio, porque vem depois da história (vv. 14–15). Um promítio viria antes, como em 1.4: <i>Āmittit meritō proprium quī aliēnum adpetit</i>.'),
        ]),
        exercicio('Exercício 2 · Morfologia', 'Analise cada forma (classe, tempo ou caso, pessoa ou número) e dê a entrada de dicionário.', [
            ('<i>vēnerant</i>', 'Mais-que-perfeito do indicativo ativo, 3ª pl., de <i>veniō, -īre, vēnī, ventum</i>: "tinham chegado".'),
            ('<i>intulit</i>', 'Perfeito do indicativo ativo, 3ª sing., de <i>īnferō, īnferre, intulī, illātum</i>: "apresentou". O perfeito vem de outra raiz (como em <i>ferō, tulī</i>).'),
            ('<i>fēcistī</i>', 'Perfeito do indicativo ativo, 2ª sing., de <i>faciō, -ere, fēcī, factum</i>: "fizeste, tornaste".'),
            ('<i>quereris</i>', 'Presente do indicativo, 2ª sing., do depoente <i>queror, querī, questus sum</i>: "queixas-te".'),
            ('<i>scrīpta est</i>', 'Perfeito do indicativo passivo, 3ª sing., de <i>scrībō, -ere, scrīpsī, scrīptum</i>; o particípio está no feminino porque o sujeito é <i>fābula</i>: "foi escrita".'),
            ('<i>correptum</i>', 'Particípio perfeito, acusativo singular masculino, de <i>corripiō, -ere, corripuī, correptum</i>: "agarrado". Refere-se ao cordeiro, subentendido.'),
            ('<i>haustūs</i>', 'Acusativo plural de <i>haustus, -ūs</i> (m., 4ª declinação), regido por <i>ad</i>. Não é nominativo singular da 2ª: o <i>ū</i> longo e a preposição <i>ad</i> decidem.'),
            ('<i>lupe</i>', 'Vocativo singular de <i>lupus, -ī</i>: o cordeiro se dirige ao lobo.'),
        ]),
        exercicio('Exercício 3 · Sintaxe', 'Diga a função de cada expressão e justifique.', [
            ('<i>mihi … bibentī</i> (vv. 5–6)', 'Dativo de referência: a pessoa afetada pela ação de turvar a água, "para mim, que estou bebendo". <i>Bibentī</i> é particípio presente no dativo, concordando com <i>mihi</i>.'),
            ('<i>turbulentam</i> (v. 5)', 'Predicativo do objeto <i>aquam</i>: com <i>facere</i>, "tornar a água turva". Não é atributo ("a água turva"), porque a água só fica turva por efeito da ação.'),
            ('<i>vēritātis vīribus</i> (v. 9)', '<i>Vīribus</i>: ablativo de meio com o particípio passivo <i>repulsus</i> ("rebatido pela força"); <i>vēritātis</i>: genitivo que o determina ("da verdade").'),
            ('<i>quod quereris</i> (v. 7)', 'Oração relativa sem antecedente expresso, que funciona como objeto direto de <i>facere</i>: "(aquilo) de que você se queixa".'),
            ('<i>propter illōs … hominēs</i> (v. 14)', 'Adjunto adverbial de causa: preposição <i>propter</i> com acusativo, separada do seu nome pelo hipérbato.'),
            ('<i>quī</i> (v. 15)', 'Pronome relativo, nominativo plural masculino, sujeito de <i>opprimunt</i>; concorda em gênero e número com o antecedente <i>hominēs</i>, mas está no nominativo pela função na sua oração.'),
        ]),
        exercicio('Exercício 4 · Do verso à prosa', 'Reescreva na ordem da prosa (sujeito, complementos, verbo; nome junto do adjetivo) e traduza.', [
            ('<i>Ā tē dēcurrit ad meōs haustūs liquor.</i>', '<i>Liquor ā tē ad meōs haustūs dēcurrit.</i> "A água desce de você até onde eu bebo."'),
            ('<i>Pater hercle tuus male dīxit mihi.</i>', '<i>Pater tuus mihi male dīxit</i> (sem a interjeição). "Seu pai falou mal de mim."'),
            ('<i>Haec propter illōs scrīpta est hominēs fābula.</i>', '<i>Haec fābula propter illōs hominēs scrīpta est.</i> "Esta fábula foi escrita por causa daqueles homens."'),
            ('<i>Tunc fauce improbā latrō incitātus iūrgiī causam intulit.</i>', '<i>Tunc latrō, fauce improbā incitātus, causam iūrgiī intulit.</i> "Então o bandido, instigado pela goela insaciável, apresentou um motivo de briga."'),
        ]),
        exercicio('Exercício 5 · A passiva do perfectum', 'Passe para a passiva do perfectum, mantendo o tempo, e traduza. O agente vai para <i>ā/ab</i> + ablativo.', [
            ('<i>Phaedrus fābulam scrīpsit.</i>', '<i>Fābula ā Phaedrō scrīpta est.</i> "A fábula foi escrita por Fedro." O particípio vai para o feminino, como <i>fābula</i>.'),
            ('<i>Lupus agnum corripuit.</i>', '<i>Agnus ā lupō correptus est.</i> "O cordeiro foi agarrado pelo lobo."'),
            ('<i>Sitis lupum et agnum compulerat.</i> (<i>compulerat</i>: mais-que-perfeito)', '<i>Lupus et agnus sitī compulsī erant.</i> "O lobo e o cordeiro tinham sido levados pela sede." A sede é coisa, não pessoa: por isso o ablativo vai sem <i>ā</i> (meio ou causa), como no verso 2; o particípio vai para o plural porque o sujeito é composto.'),
            ('<i>Vēritās lupum reppulit.</i>', '<i>Lupus vēritāte repulsus est.</i> "O lobo foi rebatido pela verdade." De novo, coisa: ablativo sem preposição.'),
        ]),
        exercicio('Exercício 6 · Traduza para o latim', 'Use o vocabulário da fábula.', [
            ('O cordeiro tinha chegado ao riacho.', '<i>Agnus ad rīvum vēnerat.</i> Mais-que-perfeito, como em <i>vēnerant</i>, no singular.'),
            ('O lobo, levado pela fome, procura um pretexto.', '<i>Lupus, famē compulsus, causam quaerit.</i> (<i>famēs, -is</i>, fome, com ablativo irregular <i>famē</i>, Bennett § 59.2.b; <i>quaerō</i>, procurar.) <i>Compulsus</i> concorda com <i>lupus</i>; <i>famē</i> é ablativo de causa, como <i>sitī</i>.'),
            ('Esta fábula foi escrita para os homens inocentes.', '<i>Haec fābula propter hominēs innocentēs scrīpta est</i>, ou, com outra nuance, <i>Haec fābula hominibus innocentibus scrīpta est</i> (dativo: "para os inocentes"). Nas duas, <i>scrīpta est</i> concorda com <i>fābula</i>.'),
        ]),
    ],
    leituras=['phaedrus-fabulae-aesopiae', 'appleton-fabulae-virginibus-puerisque-aut-narrandae-aut-recitandae', 'the-latin-library', 'logeion', 'ravizza-gramatica-latina', 'bennett-new-latin-grammar'],
    leituras_nota='Continue em <i>Fedro</i> (no catálogo, edição de Mueller no Perseus, com análise de cada palavra a um clique): leia em seguida 1.4 (o cão e o reflexo), que é curtíssima e tem promítio, e depois as outras fábulas do livro I, sempre identificando a moral e os particípios. As <i>Fabulae virginibus puerisque</i>, de Appleton, trazem historietas e fábulas em latim mais fácil e macronizado, boas para ganhar velocidade. A The Latin Library tem o texto dos cinco livros de Fedro em páginas simples. Use o Logeion para as palavras que não estão no glossário deste capítulo. Na gramática do Pe. Ravizza, o n. 536 mostra o senário de Fedro escandido; em Bennett, o § 370 descreve o verso, e os §§ 348–350 a ordem das palavras.',
)
