from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='31-gerundio-e-gerundivo', titulo='Gerúndio, gerundivo, perifrásticas e supino', titulo_latim='Dē gerundiō et gerundīvō', tempo='75 min',
    resumo='As formas em -nd- e o supino: o gerúndio, substantivo verbal que dá ao infinitivo os casos que lhe faltam (ars scrībendī, ad discendum); o gerundivo, adjetivo verbal passivo de obrigação, que substitui o gerúndio com objeto (ad urbem capiendam); as conjugações perifrásticas passiva (Carthāgō dēlenda est, com dativo de agente) e ativa (-ūrus sum); e os dois supinos (vēnit spectātum; mīrābile dictū). Com tabelas e um procedimento para decidir, diante de uma forma em -nd-, qual delas é.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['gerúndio', 'declinação do gerúndio', 'ad + gerúndio', 'causā + genitivo do gerúndio', 'gerundivo', 'construção gerundiva', 'conjugação perifrástica passiva', 'dativo de agente', 'perifrástica impessoal', 'conjugação perifrástica ativa', 'supino em -um', 'supino em -ū', 'como reconhecer as formas em -nd-', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 29 (os particípios: o gerundivo é a quarta forma participial, e o particípio futuro em -ūrus forma a perifrástica ativa). Ajudam o capítulo 20 (o dativo de posse, de onde vem o dativo de agente) e o capítulo 27 (o infinitivo como substantivo verbal, que o gerúndio completa).',
                       licoes=['20-usos-do-genitivo-e-do-dativo', '27-os-infinitivos', '29-os-participios']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 101 (gerúndio, gerundivo e supinos de amō), § 112.a–b (depoentes: gerúndio e supino ativos, gerundivo passivo), § 115 (as duas conjugações perifrásticas), § 116.2 (gerundivo em -undus), § 189.1 (dativo de agente com o gerundivo; 189.1.a ā + ablativo para evitar ambiguidade), § 337.4 (particípio futuro fora da perifrástica), § 337.8 (gerundivo atributivo e predicativo; perifrástica impessoal; cūrō + gerundivo), § 338 (os casos do gerúndio), § 339.1–5 (construção gerundiva; quando é obrigatória; só verbos transitivos; suī servandī causā), § 340 (supinos em -um e em -ū)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 158.d (o gerundivo), § 159 (gerúndio e supino; o nominativo é suprido pelo infinitivo), §§ 193–196 (conjugações perifrásticas), § 374 (dativo de agente; nota 1, ab + ablativo), § 500 (gerundivo: obrigação; perifrástica impessoal; com verbos de dar e cuidar), §§ 501–503 (gerúndio; construção gerundiva), §§ 504–507 (os casos do gerúndio e do gerundivo; nota sobre a origem do gerúndio românico), §§ 508–510 (o supino)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 107 (definições de gerúndio, gerundivo e supinos), a seção "Periphrastic Conjugation" depois do § 113, § 222 (dativo de agente), §§ 374–384 (gerúndio e gerundivo; quadro petendī pācem / petendae pācis), §§ 385–388 (supinos)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 117 (conjugação perifrástica ativa e passiva comparada com "haver de", "ter de"), n. 398 (particípio futuro passivo ou gerundivo; dativo da pessoa; uso impessoal em -dum), nn. 401–402 (gerúndio e construção com o gerundivo, com os casos em que é obrigatória), nn. 405–406 (supino ativo em -um e passivo em -u)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Eclesiastes 3,1–4; Lucas 1,79; Marcos 3,15', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Liber_Ecclesiastes', nota='frases autênticas da seção 6 e do exercício 6, conferidas na Wikisource latina; ortografia adaptada (i por j, ae por æ) e macrons acrescentados', tipo='dominio_publico'),
        referencia('Catão e Cartago: Plínio, NH 15.74; Floro 1.31 (2.15); De viris illustribus 47.8; Plutarco, Catão, o Velho 27.1', None, url='https://github.com/PerseusDL/canonical-latinLit/tree/master/data/phi0978/phi001', nota='Plínio na edição de Mayhoff (Teubner, 1892–1909), TEI da Perseus (PerseusDL); Floro e De viris illustribus no texto da The Latin Library (florus1.html; victor/victor.ill.html), edição não identificada na página; Plutarco no grego da Perseus (ed. Perrin, Loeb, 1914) e na tradução de Perrin em LacusCurtius. Citações breves; macrons acrescentados', tipo='dominio_publico'),
        referencia('Virgílio, Geórgicas 2.30–31; Horácio, Odes 1.7.27', None, url='https://www.thelatinlibrary.com/vergil/geo2.shtml', nota='mīrābile dictū e nīl dēspērandum, conferidos na Latin Library (Horácio em https://www.thelatinlibrary.com/horace/carm1.shtml); macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Formar e declinar o gerúndio e o gerundivo de qualquer verbo, inclusive depoentes, e formar os dois supinos.',
        'Traduzir o gerúndio em cada caso (genitivo, dativo, <i>ad</i> + acusativo, ablativo) e com <i>causā</i>.',
        'Reconhecer o gerundivo como adjetivo passivo de obrigação e usar a construção gerundiva no lugar do gerúndio com objeto (<i>ad urbem capiendam</i>).',
        'Traduzir as conjugações perifrásticas passiva (com dativo de agente e na forma impessoal) e ativa.',
        'Aplicar um procedimento para decidir, diante de uma forma em <i>-nd-</i>, em <i>-tum</i> ou em <i>-tū</i>, de que construção se trata.',
    ],
    secoes=[
        ('As formas: gerúndio, gerundivo e supino', f'''
<p>No capítulo 27 você viu o infinitivo funcionando como substantivo: <i>Errāre hūmānum est</i>, "errar é humano". Mas o infinitivo latino é quase indeclinável: serve de sujeito e de objeto direto, e para por aí. Quando o latim precisa de "a arte <b>de</b> escrever", "<b>para</b> aprender", "<b>aprendendo</b>", ele usa um substantivo verbal com casos, o <b>gerúndio</b>. Ao lado do gerúndio vive uma forma adjetiva muito parecida, o <b>gerundivo</b>, e um pequeno substantivo verbal de uso restrito, o <b>supino</b>. Este capítulo reúne os três, porque os três se confundem facilmente.</p>
{tabela(['Forma', 'Natureza', 'Terminações', 'Exemplo', 'Sentido básico'], [
    ['<b>gerúndio</b>', 'substantivo verbal neutro, voz ativa, só casos oblíquos', '<i>-ndī, -ndō, -ndum, -ndō</i>', '<i>amandī</i>', '"de amar"'],
    ['<b>gerundivo</b>', 'adjetivo verbal, voz passiva, sentido de obrigação', '<i>-ndus, -nda, -ndum</i>', '<i>amandus</i>', '"que deve ser amado"'],
    ['<b>supino</b>', 'substantivo verbal da 4ª declinação, só dois casos', '<i>-tum</i> (<i>-sum</i>) e <i>-tū</i> (<i>-sū</i>)', '<i>amātum</i>, <i>amātū</i>', '"para amar"; "de amar"'],
], 'As três formas deste capítulo')}
<p>O gerúndio e o gerundivo formam-se do tema do presente com <i>-nd-</i>, com a mesma vogal do particípio presente: <i>ama-nd-</i>, <i>mone-nd-</i>, <i>reg-end-</i>, <i>audi-end-</i>, <i>capi-end-</i>. O verbo <i>eō</i> faz <i>eundī</i>; textos antigos às vezes trazem <i>-undus</i> por <i>-endus</i> (<i>faciundus</i>). O supino tem a forma do particípio perfeito trocando <i>-us</i> por <i>-um</i> ou <i>-ū</i> (<i>amāt-um</i>, <i>amāt-ū</i>); é por isso que muitos dicionários dão como quarta parte principal o supino <i>amātum</i>, e não o particípio.</p>
{tabela(['Verbo', 'Gerúndio (gen.)', 'Gerundivo', 'Supino em -um', 'Supino em -ū'], [
    ['<i>amō, amāre</i>', '<i>amandī</i>', '<i>amandus, -a, -um</i>', '<i>amātum</i>', '<i>amātū</i>'],
    ['<i>moneō, monēre</i>', '<i>monendī</i>', '<i>monendus</i>', '<i>monitum</i>', '<i>monitū</i>'],
    ['<i>regō, regere</i>', '<i>regendī</i>', '<i>regendus</i>', '<i>rēctum</i>', '<i>rēctū</i>'],
    ['<i>audiō, audīre</i>', '<i>audiendī</i>', '<i>audiendus</i>', '<i>audītum</i>', '<i>audītū</i>'],
    ['<i>capiō, capere</i>', '<i>capiendī</i>', '<i>capiendus</i>', '<i>captum</i>', '<i>captū</i>'],
    ['<i>sequor, sequī</i> (dep.)', '<i>sequendī</i> (ativo)', '<i>sequendus</i> (passivo!)', '<i>secūtum</i>', '(pouco usado)'],
], 'Gerúndio, gerundivo e supinos dos verbos-modelo', latim_cols=(1, 2, 3, 4))}
<p>Repare na linha do depoente: o gerúndio e o supino de <i>sequor</i> têm sentido ativo ("de seguir"), mas o gerundivo é passivo ("que deve ser seguido"). O gerundivo é a única forma dos depoentes com sentido passivo garantido.</p>
'''),
        ('O gerúndio: um infinitivo com casos', f'''
<p>O gerúndio é o substantivo verbal que completa o infinitivo. No nominativo, e como objeto direto, continua-se usando o infinitivo (<i>Scrībere est ūtile</i>, "escrever é útil"); nos outros casos, entra o gerúndio, que se declina como um neutro da 2ª declinação, sem plural e sem nominativo. Por ser verbo, aceita advérbios (<i>bene vīvendī</i>, "de viver bem") e, no genitivo e no ablativo sem preposição, até um objeto direto.</p>
{tabela_declinacao('O gerúndio de discō, discere, "aprender"', [
    ('discend<b>ī</b>', 'ars discendī, "a arte de aprender"; discendī causā, "para aprender"'),
    ('discend<b>ō</b>', 'aptus discendō, "apto para aprender" (raro)'),
    ('(ad) discend<b>um</b>', 'ad discendum, "para aprender" (só com preposição)'),
    ('discend<b>ō</b>', 'discendō, "aprendendo, por aprender"; in discendō, "no aprender"'),
], casos=('Genitivo', 'Dativo', 'Acusativo', 'Ablativo'), colunas=('Forma', 'Uso típico'))}
<h3>Genitivo: "de" + infinitivo</h3>
<p>Depende de nomes (<i>ars, cupiditās, studium, tempus, occāsiō, spēs</i>) e de adjetivos que pedem genitivo (<i>cupidus</i>, "desejoso"; <i>perītus</i>, "perito"). Com <i>causā</i> ou <i>grātiā</i>, que vêm <b>depois</b> do genitivo, exprime finalidade: <i>discendī causā</i>, "por causa de aprender", isto é, "para aprender".</p>
{exemplos([('ars <b>scrībendī</b>', 'a arte de escrever'), ('cupidus <b>audiendī</b>', 'desejoso de ouvir'), ('Rōmam vēnī <b>discendī</b> causā.', 'Vim a Roma para estudar (por causa de aprender).')])}
<h3>Acusativo: só depois de preposição, sobretudo ad</h3>
<p><i>Ad</i> + gerúndio é a maneira mais comum de exprimir finalidade sem oração: <i>ad discendum</i>, "para aprender". Outras preposições são raras (<i>inter cēnandum</i>, "durante o jantar").</p>
{exemplos([('Puer <b>ad discendum</b> in lūdum it.', 'O menino vai à escola para aprender. (<i>lūdus</i>, escola)'), ('Nōn <b>ad dormiendum</b>, sed <b>ad labōrandum</b> vīvimus.', 'Não vivemos para dormir, mas para trabalhar.')])}
<h3>Ablativo: meio, causa, e depois de in, dē, ex, ab</h3>
<p>Sem preposição, o ablativo do gerúndio diz o meio ou o modo: "fazendo", "por fazer". Com <i>in</i> diz a ocupação ("no fazer"); com <i>dē</i>, o assunto ("sobre fazer").</p>
{exemplos([('<b>Errandō</b> discimus.', 'Aprendemos errando.'), ('Corpus <b>exercendō</b> firmātur.', 'O corpo se fortalece com o exercício (exercitando-se). (<i>exerceō</i>, exercitar; <i>firmō</i>, fortalecer)'), ('Multum tempus <b>in legendō</b> cōnsūmit.', 'Gasta muito tempo lendo. (<i>cōnsūmō</i>, gastar)')])}
<h3>Dativo: raro</h3>
<p>Aparece com alguns adjetivos de aptidão e em fórmulas (<i>aptus bibendō</i>, "próprio para beber"). Na prosa clássica, é muito menos frequente que <i>ad</i> + acusativo.</p>
{observacao('O gerúndio português vem do latino', 'O nosso gerúndio em <i>-ndo</i> (<i>amando, vendo, partindo</i>) não vem do particípio presente latino, mas do <b>ablativo do gerúndio</b>: <i>amandō</i> → amando. No latim tardio e medieval o ablativo do gerúndio já se usava quase como um particípio presente (A&G § 507, nota de rodapé 5, que cita as formas italianas e espanholas). Por isso o ablativo do gerúndio traduz-se tão naturalmente pelo nosso gerúndio ("aprendemos errando"), mas os outros casos não: o genitivo pede "de + infinitivo", o acusativo com <i>ad</i> pede "para + infinitivo".')}
'''),
        ('O gerundivo e a construção gerundiva', f'''
<p>O gerundivo é um adjetivo verbal <b>passivo</b> que exprime obrigação, necessidade ou conveniência: <i>amandus</i>, "que deve ser amado, digno de ser amado". Declina-se como <i>bonus, -a, -um</i> e concorda com o seu nome. As gramáticas o chamam também de particípio futuro passivo, mas o sentido central é de dever, não de futuro.</p>
{exemplos([('liber <b>legendus</b>', 'um livro que deve ser lido, que merece ser lido'), ('vir <b>laudandus</b>', 'um homem digno de louvor'), ('lēgēs <b>servandae</b>', 'leis que devem ser observadas (<i>servō</i>, observar, guardar)')])}
<h3>O gerundivo no lugar do gerúndio com objeto</h3>
<p>É o uso mais frequente do gerundivo, e aquele em que ele <b>não</b> exprime obrigação. Quando o gerúndio teria um objeto direto ("o desejo de ver a cidade"), o latim prefere outra construção: o objeto passa para o caso que o gerúndio teria, e o gerundivo concorda com ele. Em vez de <i>cupidus urbem videndī</i>, diz-se <i>cupidus urbis videndae</i>, literalmente "desejoso da cidade a ser vista". A tradução é a mesma; a construção é outra.</p>
{comparacao('Gerúndio com objeto e construção gerundiva', ['Construção gerundiva (preferida)', 'Gerúndio com objeto', 'Tradução'], [
    ['<i>cupidus urbis videndae</i>', '<i>cupidus urbem videndī</i>', 'desejoso de ver a cidade'],
    ['<i>pācis petendae causā</i>', '<i>pācem petendī causā</i>', 'para pedir a paz'],
    ['<i>ad urbem capiendam</i>', '(não se usa)', 'para tomar a cidade'],
    ['<i>in librīs legendīs</i>', '(não se usa)', 'na leitura dos livros, ao ler os livros'],
    ['<i>lēgibus mūtandīs</i>', '<i>lēgēs mūtandō</i>', 'mudando as leis, pela mudança das leis'],
])}
<p>A regra prática tem duas partes. No <b>genitivo</b> e no <b>ablativo sem preposição</b>, as duas construções são possíveis, e a gerundiva é mais comum. No <b>dativo</b> e <b>depois de preposição</b> (<i>ad, in, dē, ex</i>), a construção gerundiva é obrigatória: nunca *<i>ad capiendum urbem</i>, sempre <i>ad urbem capiendam</i>. Como o gerundivo é passivo, só verbos transitivos o admitem nesse uso; os intransitivos ficam no gerúndio (<i>ad currendum</i>, "para correr"). Duas exceções: quando o objeto é um adjetivo neutro substantivado (<i>vērum investīgandī</i>, "de investigar a verdade") e os depoentes <i>ūtor, fruor, fungor, potior</i>, que admitem o gerundivo apesar do ablativo.</p>
<h3>Gerundivo com verbos de dar e de cuidar</h3>
<p>Com verbos como <i>cūrō</i> ("providenciar"), <i>dō</i>, <i>trādō</i> ("entregar"), o gerundivo concordando com o objeto indica o que se manda fazer ou se entrega para ser feito:</p>
{exemplos([('Dux pontem <b>faciendum</b> cūrāvit.', 'O comandante mandou fazer uma ponte. (lit. "providenciou a ponte a ser feita"; <i>pōns, pontis</i>, ponte)'), ('Puerum magistrō <b>docendum</b> trādidit.', 'Entregou o menino ao professor para ser educado. (<i>doceō</i>, ensinar)')])}
'''),
        ('As conjugações perifrásticas', f'''
<p>"Perifrástica" quer dizer "dita com rodeio": em vez de uma forma simples, o latim junta um particípio às formas de <i>sum</i>. Há duas, e uma é o espelho da outra.</p>
<h3>A perifrástica passiva: gerundivo + sum (obrigação)</h3>
<p>Com as formas de <i>sum</i>, o gerundivo predica uma obrigação do sujeito: <i>Liber legendus est</i>, "o livro deve ser lido". O tempo de <i>sum</i> dá o tempo da obrigação: <i>legendus erat</i>, "devia ser lido"; <i>legendus erit</i>, "deverá ser lido". A pessoa que tem o dever vai para o <b>dativo</b>, o chamado <b>dativo de agente</b>, parente do dativo de posse do capítulo 20: <i>mihi liber est</i>, "eu tenho um livro"; <i>mihi liber legendus est</i>, "eu tenho um livro a ser lido", isto é, "<b>eu devo ler</b> o livro".</p>
{exemplos([
    ('<b>Mihi</b> epistula <b>scrībenda est</b>.', 'Eu devo escrever uma carta. (lit. "para mim uma carta deve ser escrita")'),
    ('<b>Nōbīs</b> lēgēs <b>servandae sunt</b>.', 'Nós devemos observar as leis.'),
    ('Haec <b>agenda erant</b>.', 'Estas coisas deviam ser feitas.'),
    ('Carthāgō <b>dēlenda est</b>.', 'Cartago deve ser destruída. (<i>dēleō</i>, destruir)'),
])}
<p>A última frase é a mais famosa da perifrástica passiva, mas, nessa forma exata, não está nas fontes antigas que contam a história; também a forma longa que se costuma citar, <i>Cēterum cēnseō Carthāginem esse dēlendam</i>, não aparece assim nos textos antigos conferidos para este capítulo. Os antigos atribuem a ideia a Catão, o Velho, que a repetia no senado, e a transmitem em discurso indireto, com o gerundivo no acusativo (a oração infinitiva do capítulo 28): Plínio, o Velho, conta que Catão <i>clāmāret omnī senātū Carthāginem dēlendam</i>, "clamava em todas as sessões do senado que Cartago devia ser destruída" (<i>NH</i> 15.74); Floro escreve <i>Catō inexpiābilī odiō dēlendam esse Carthāginem … prōnūntiābat</i>, "Catão, com ódio implacável, declarava que Cartago devia ser destruída" (1.31 [2.15]); o <i>Dē virīs illūstribus</i> atribuído a Aurélio Victor resume: <i>Carthāginem dēlendam cēnsuit</i>, "votou que Cartago fosse destruída" (47.8); e Plutarco, em grego, dá a fórmula com que Catão fechava todos os seus votos: "parece-me também que Cartago não deve existir" (<i>Catão, o Velho</i> 27.1). Como ilustração gramatical, porém, a frase moderna é perfeita: sujeito no nominativo, gerundivo concordando com ele (feminino singular), <i>est</i>.</p>
<p>Com verbos <b>intransitivos</b> (ou transitivos sem objeto), a perifrástica é <b>impessoal</b>: o gerundivo fica no neutro singular, o verbo na 3ª pessoa do singular, e o complemento do verbo conserva o seu caso.</p>
{exemplos([
    ('<b>Mihi eundum est.</b>', 'Eu devo ir. (lit. "por mim deve ser ido")'),
    ('Omnibus <b>moriendum est</b>.', 'Todos devem morrer.'),
    ('Lēgibus <b>pārendum est</b>.', 'Deve-se obedecer às leis. (<i>pāreō</i> + dativo, obedecer)'),
])}
{observacao('Quando o dativo de agente vira ā + ablativo', 'Em <i>Lēgibus pārendum est</i>, <i>lēgibus</i> é o dativo pedido por <i>pāreō</i>. Se quiséssemos dizer "<b>vós</b> deveis obedecer às leis", um segundo dativo (<i>vōbīs</i>) ficaria ambíguo. Nesse caso o agente vai para <i>ā</i> + ablativo: <i>Lēgibus ā vōbīs pārendum est</i>. É a única situação comum em que a perifrástica passiva usa o agente da passiva normal.')}
<h3>A perifrástica ativa: particípio futuro + sum (intenção, iminência)</h3>
<p>Com o particípio futuro em <i>-ūrus</i> (capítulo 29), as formas de <i>sum</i> exprimem o que o sujeito está para fazer ou tem a intenção de fazer: <i>amātūrus sum</i>, "estou para amar, vou amar, hei de amar". Também aqui <i>sum</i> dá o tempo: <i>scrīptūrus eram</i>, "eu ia escrever, estava para escrever".</p>
{exemplos([('Epistulam <b>scrīptūrus sum</b>.', 'Vou escrever (estou para escrever) uma carta.'), ('Nautae <b>nāvigātūrī erant</b>.', 'Os marinheiros estavam para navegar (iam navegar).')])}
{comparacao('As duas perifrásticas lado a lado', ['Latim', 'Construção', 'Tradução'], [
    ['Epistulam scrīptūrus sum.', 'perifrástica ativa (<i>-ūrus</i> + <i>sum</i>)', 'Vou escrever a carta. (intenção)'],
    ['Mihi epistula scrībenda est.', 'perifrástica passiva (<i>-ndus</i> + <i>sum</i>)', 'Devo escrever a carta. (obrigação)'],
    ['Epistula scrībētur.', 'futuro passivo simples (capítulo 23)', 'A carta será escrita. (simples futuro, sem dever)'],
])}
'''),
        ('O supino', f'''
<p>O supino é um substantivo verbal da 4ª declinação que só sobreviveu em dois casos, cada um com um uso fixo.</p>
<h3>Supino em -um: finalidade depois de verbos de movimento</h3>
<p>Depois de verbos como <i>eō, veniō, mittō</i>, o supino em <i>-um</i> diz <b>para que</b> alguém vai ou é mandado. Pode ter objeto direto, porque continua sendo verbo.</p>
{exemplos([('Spectātum vēnērunt.', 'Vieram para ver (assistir). (<i>spectō</i>, olhar, assistir)'), ('Lēgātī auxilium <b>petītum</b> ad rēgem vēnērunt.', 'Os embaixadores vieram ao rei pedir ajuda. (<i>lēgātus</i>, embaixador; <i>auxilium</i>, ajuda; <i>petō, petītum</i>, pedir)'), ('Eō <b>dormītum</b>.', 'Vou dormir.')])}
<h3>Supino em -ū: "de" + infinitivo depois de adjetivos</h3>
<p>Com adjetivos como <i>facilis, difficilis, mīrābilis, incrēdibilis, optimus, horribilis</i> e com <i>fās</i> e <i>nefās</i>, o supino em <i>-ū</i> diz <b>em relação a que ação</b> a qualidade vale. É sempre curto e nunca tem objeto; só uns poucos verbos o usam com frequência: <i>dictū, factū, vīsū, audītū, cognitū, memorātū, inventū</i>.</p>
{exemplos([('mīrābile <b>dictū</b>', 'admirável de dizer, espantoso de contar'), ('rēs facilis <b>factū</b>', 'uma coisa fácil de fazer'), ('horribile <b>vīsū</b>', 'horrível de ver'), ('Hōc fās est <b>dictū</b>?', 'É lícito dizer isto?')])}
<p>Note que o português traduz o supino em <i>-ū</i> exatamente como o genitivo do gerúndio, com "de" + infinitivo. A diferença está do lado latino: o supino em <i>-ū</i> depende de um <b>adjetivo</b> de qualidade e não aceita objeto. Mesmo com <i>facilis</i> e <i>difficilis</i>, a prosa prefere muitas vezes <i>ad</i> + gerúndio (<i>facilis ad intellegendum</i>).</p>
{observacao('Outras maneiras de dizer finalidade', 'Você já tem três maneiras de dizer "para fazer": <i>ad</i> + gerúndio ou gerundivo (<i>ad pācem petendam</i>), o genitivo com <i>causā</i> (<i>pācis petendae causā</i>) e, depois de verbos de movimento, o supino (<i>pācem petītum</i>). A quarta, e a mais comum de todas, é a oração final com <i>ut</i> e o subjuntivo, que você verá no capítulo 33.')}
'''),
        ('Como decidir, e uma leitura autêntica', f'''
<p>As formas deste capítulo se parecem muito: <i>amandum</i> pode ser gerúndio ou gerundivo; <i>amātum</i> pode ser supino ou particípio. O procedimento a seguir resolve quase todos os casos.</p>
{tabela(['Pergunta', 'Se sim', 'Exemplo'], [
    ['1. A forma em <i>-nd-</i> está com uma forma de <i>sum</i> (expressa ou subentendida)?', '<b>perifrástica passiva</b>: obrigação; procure o dativo de agente', '<i>Mihi eundum est.</i> Devo ir.'],
    ['2. A forma em <i>-nd-</i> concorda com um nome (gênero, número, caso)?', '<b>gerundivo</b>: construção gerundiva (traduza como "de/para + infinitivo + objeto") ou adjetivo de obrigação', '<i>ad urbem capiendam</i>; <i>liber legendus</i>'],
    ['3. A forma em <i>-ndī, -ndō, -ndum</i> está sozinha, neutra, no singular, sem nominativo?', '<b>gerúndio</b>: traduza pelo caso (de + inf., para + inf., gerúndio português)', '<i>ars scrībendī</i>; <i>errandō discimus</i>'],
    ['4. Uma forma em <i>-tum/-sum</i> segue um verbo de movimento, sem concordar com nada?', '<b>supino em -um</b>: finalidade', '<i>spectātum vēnērunt</i>'],
    ['5. Uma forma em <i>-tū/-sū</i> segue um adjetivo ou <i>fās/nefās</i>?', '<b>supino em -ū</b>: "de + infinitivo"', '<i>mīrābile dictū</i>'],
    ['6. <i>-ūrus</i> com uma forma de <i>sum</i>?', '<b>perifrástica ativa</b>: intenção, iminência', '<i>scrīptūrus sum</i>'],
], 'Procedimento de decisão')}
<p>O livro do Eclesiastes, na Vulgata, tem uma das sequências de gerúndios mais conhecidas da literatura latina:</p>
{exemplos([('Omnia tempus habent, et suīs spatiīs trānseunt ūniversa sub caelō. Tempus nāscendī, et tempus moriendī; tempus plantandī, et tempus ēvellendī quod plantātum est.', 'Tudo tem o seu tempo, e todas as coisas passam debaixo do céu nos seus prazos. Tempo de nascer, e tempo de morrer; tempo de plantar, e tempo de arrancar o que foi plantado. (Eclesiastes 3,1–2, Vulgata Clementina)')])}
{analise('Eclesiastes 3,2, palavra a palavra', [
    ('Tempus', 'tempus, temporis (n.), tempo', 'nominativo singular, 3ª declinação', 'núcleo da expressão (há um tempo...); verbo <i>est</i> subentendido'),
    ('nāscendī', 'nāscor, nāscī, nātus sum, nascer', 'gerúndio, genitivo; depoente, mas o gerúndio tem forma e sentido ativos', 'adjunto de <i>tempus</i>: "de nascer"'),
    ('et', 'et (conjunção)', 'invariável', 'liga os dois membros'),
    ('tempus', 'tempus, temporis (n.)', 'nominativo singular', 'segundo núcleo'),
    ('moriendī', 'morior, morī, mortuus sum, morrer', 'gerúndio, genitivo (verbo em <i>-ior</i>: <i>-iend-</i>)', '"de morrer"'),
    ('plantandī', 'plantō, plantāre, plantar', 'gerúndio, genitivo, 1ª conjugação', '"de plantar"'),
    ('ēvellendī', 'ēvellō, ēvellere, ēvellī, ēvulsum, arrancar', 'gerúndio, genitivo, 3ª conjugação', '"de arrancar"; tem como objeto a oração relativa seguinte'),
    ('quod', 'quī, quae, quod', 'pronome relativo, nominativo singular neutro', 'sujeito de <i>plantātum est</i>; com o antecedente "aquilo" subentendido, é o objeto de <i>ēvellendī</i>'),
    ('plantātum est', 'plantō', 'perfeito passivo, 3ª pessoa do singular, neutro', '"foi plantado"'),
])}
<p>Repare em três coisas. Todos os genitivos dependem de <i>tempus</i>, como em <i>ars scrībendī</i>: é o uso básico do gerúndio genitivo com nome. Os dois primeiros são de depoentes (<i>nāscor</i>, <i>morior</i>), e mesmo assim o gerúndio é ativo: "de nascer", "de morrer". E <i>ēvellendī</i> tem um objeto, a oração <i>quod plantātum est</i>: como o objeto é uma oração e não um nome, não há com que fazer concordar um gerundivo, e o gerúndio fica.</p>
{diagrama_frase([('Lēgātī', 'nominativo · sujeito'), ('ad amīcitiam petendam', 'ad + ac. + gerundivo · finalidade'), ('Rōmam', 'acusativo · para onde'), ('vēnērunt', 'verbo · "vieram"')],
    'A construção gerundiva com <i>ad</i>: <i>Lēgātī ad amīcitiam petendam Rōmam vēnērunt</i> = Os embaixadores vieram a Roma para pedir amizade (<i>amīcitia</i>, amizade). Com supino: <i>amīcitiam petītum</i>; com <i>causā</i>: <i>amīcitiae petendae causā</i>.')}
<p>Dois versos célebres fecham o capítulo. Virgílio, ao falar dos enxertos e das estacas, interrompe a frase para se espantar: <i>quīn et caudicibus sectīs (mīrābile dictū) / trūditur ē siccō rādīx oleāgina lignō</i>, "e até de troncos cortados (espantoso de dizer!) brota de um lenho seco uma raiz de oliveira" (<i>Geórgicas</i> 2.30–31). Há ali um supino em <i>-ū</i> (<i>dictū</i>) e um ablativo absoluto (<i>caudicibus sectīs</i>, capítulo 30). E Horácio, no verso que você leu no capítulo 30, junta um gerundivo impessoal a dois ablativos absolutos: <i>Nīl dēspērandum Teucrō duce et auspice Teucrō</i>, "não se deve desesperar de nada, sendo Teucro o guia e o áugure" (<i>Odes</i> 1.7.27; subentende-se <i>est</i>).</p>
<h3>Resumo</h3>
<ul>
<li><b>Gerúndio</b> (<i>-ndī, -ndō, -ndum, -ndō</i>): substantivo verbal ativo; genitivo "de + inf." (também com <i>causā</i>), <i>ad</i> + acusativo "para + inf.", ablativo "fazendo, por fazer".</li>
<li><b>Gerundivo</b> (<i>-ndus, -a, -um</i>): adjetivo passivo de obrigação; substitui o gerúndio com objeto (<i>ad urbem capiendam</i>), obrigatoriamente no dativo e depois de preposição.</li>
<li><b>Perifrástica passiva</b>: gerundivo + <i>sum</i> = dever; agente no dativo; impessoal com intransitivos (<i>mihi eundum est</i>).</li>
<li><b>Perifrástica ativa</b>: <i>-ūrus</i> + <i>sum</i> = intenção, iminência.</li>
<li><b>Supino</b>: <i>-um</i> depois de verbos de movimento (finalidade); <i>-ū</i> depois de adjetivos (<i>mīrābile dictū</i>).</li>
</ul>
'''),
    ],
    erros_comuns=[
        ('Traduzir todo gerúndio latino pelo gerúndio português: <i>ars scrībendī</i> → *"a arte escrevendo".', 'Só o ablativo do gerúndio se traduz bem pelo nosso gerúndio. O genitivo pede "de + infinitivo" ("a arte de escrever"), e <i>ad</i> + acusativo pede "para + infinitivo". Identifique o caso antes de traduzir.'),
        ('Traduzir o gerundivo como ativo: <i>liber legendus</i> → *"um livro que lê", <i>vir laudandus</i> → *"um homem que louva".', 'O gerundivo é passivo e exprime dever: "um livro que deve ser lido", "um homem digno de ser louvado". Na construção gerundiva (<i>ad urbem capiendam</i>), a tradução portuguesa usa o infinitivo ativo ("para tomar a cidade"), mas é só porque o português não tem essa construção.'),
        ('Ler o dativo da perifrástica passiva como objeto indireto: <i>Mihi epistula scrībenda est</i> → *"Uma carta deve ser escrita para mim".', 'Com o gerundivo, o dativo indica quem tem o dever: "<b>eu</b> devo escrever uma carta". Transforme sempre a frase em ativa com "dever": o dativo vira o sujeito português.'),
        ('Confundir a perifrástica passiva com o futuro passivo: <i>Carthāgō dēlenda est</i> → *"Cartago será destruída".', 'O gerundivo com <i>sum</i> diz obrigação, não futuro: "Cartago deve ser destruída". O futuro passivo é <i>dēlēbitur</i> (capítulo 23). E <i>dēlētūra est</i> seria a perifrástica ativa ("está para destruir"), outra coisa.'),
        ('Escrever o gerúndio com objeto depois de preposição: *<i>ad capiendum urbem</i>, *<i>in legendō librōs</i>.', 'Depois de preposição (e no dativo), a construção gerundiva é obrigatória: o objeto vai para o caso do gerúndio e o gerundivo concorda com ele: <i>ad urbem capiendam</i>, <i>in librīs legendīs</i>.'),
        ('Tomar o supino em <i>-um</i> por um objeto direto ou por um particípio: <i>Spectātum vēnērunt</i> → *"Vieram o espetáculo" ou *"vieram vistos".', 'Depois de um verbo de movimento, uma forma em <i>-tum</i> que não concorda com nada é supino de finalidade: "vieram para ver". O particípio concordaria com algum nome; o supino é invariável.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Três formas em -nd- numa só passagem',
            'Classifique cada forma em <i>-nd-</i> e traduza: <i lang="la">Mīlitēs ad oppidum oppugnandum missī sunt; nam Rōmānīs oppidum capiendum erat, et dux pugnandī cupidus erat.</i> Vocabulário: <i>oppidum</i>, cidade fortificada; <i>oppugnō</i>, atacar; <i>mittō, missum</i>, enviar; <i>nam</i>, pois; <i>capiō</i>, tomar; <i>pugnō</i>, combater; <i>cupidus</i> + genitivo, desejoso de.', [
            ('<i>ad oppidum oppugnandum</i>: gerúndio ou gerundivo?', '<i>Oppugnandum</i> concorda com <i>oppidum</i> (acusativo singular neutro), regido por <i>ad</i>: é a <b>construção gerundiva</b> de finalidade, obrigatória depois de preposição. "Para atacar a cidade."'),
            ('<i>Rōmānīs oppidum capiendum erat</i>: que construção é?', 'Gerundivo + forma de <i>sum</i> (<i>erat</i>): <b>perifrástica passiva</b> no imperfeito. <i>Capiendum</i> concorda com o sujeito <i>oppidum</i>; <i>Rōmānīs</i> é dativo de agente. "Os romanos tinham de tomar a cidade."'),
            ('<i>pugnandī cupidus</i>?', '<i>Pugnandī</i> está sozinho, no genitivo, sem nome com que concordar, regido pelo adjetivo <i>cupidus</i>: <b>gerúndio</b>. <i>Pugnō</i> é intransitivo, por isso não poderia haver gerundivo. "Desejoso de combater."'),
            ('E <i>missī sunt</i>?', 'Perfeito passivo de <i>mittō</i> (capítulo 24), concordando com <i>mīlitēs</i>: "foram enviados". Não confunda com a perifrástica: aqui é o particípio perfeito, não o gerundivo.'),
            ('Monte a tradução.', '"Os soldados foram enviados para atacar a cidade; pois os romanos tinham de tomá-la, e o comandante estava desejoso de combater."'),
        ]),
        pratica_guiada('Prática guiada 2 · Do "dever" português à perifrástica latina',
            'Passe para o latim com a perifrástica passiva. Vocabulário: <i>liber, librī</i>, livro; <i>legō</i>, ler; <i>labōrō</i>, trabalhar; <i>parentēs, -um</i>, os pais; <i>pāreō</i> + dativo, obedecer.', [
            ('"Eu devo ler este livro."', 'Transforme em passiva com "dever": "este livro deve ser lido por mim". Sujeito: <i>hīc liber</i>; gerundivo concordando: <i>legendus</i>; agente no dativo: <i>mihi</i>. <i>Mihi hīc liber legendus est.</i>'),
            ('"Tu deves trabalhar."', '<i>Labōrō</i> é intransitivo: perifrástica impessoal, gerundivo no neutro singular. <i>Tibi labōrandum est.</i>'),
            ('"Os filhos deviam obedecer aos pais."', '<i>Pāreō</i> pede dativo (<i>parentibus</i>), e um segundo dativo para o agente seria ambíguo: o agente vai para <i>ā</i> + ablativo. Impessoal no imperfeito: <i>Parentibus ā fīliīs pārendum erat.</i>'),
        ], 'Conclusão: na perifrástica passiva, o sujeito português ("eu", "tu") vira dativo; o objeto português, se houver, vira sujeito latino; e com verbos intransitivos tudo fica impessoal, no neutro.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Identifique a forma', 'Diga se a forma destacada é gerúndio, gerundivo, supino ou particípio futuro, e o seu caso e uso. Vocabulário: <i>ars</i>, arte; <i>canō</i>, cantar; <i>currō</i>, correr; <i>parātus</i>, pronto; <i>lūdī, -ōrum</i>, os jogos; <i>spectō</i>, olhar, assistir; <i>īmus</i>, vamos (de <i>eō</i>); <i>horribilis</i>, horrível; <i>mittō, missum</i>, enviar.', [
            ('<i>ars <b>canendī</b></i>', 'Gerúndio, genitivo, dependendo de <i>ars</i>: "a arte de cantar".'),
            ('<i>Puerī <b>ad currendum</b> parātī sunt.</i>', 'Gerúndio, acusativo com <i>ad</i>: "Os meninos estão prontos para correr." <i>Currō</i> é intransitivo: só gerúndio.'),
            ('<i>Haec epistula <b>legenda est</b>.</i>', 'Gerundivo, nominativo singular feminino, com <i>est</i>: perifrástica passiva. "Esta carta deve ser lida."'),
            ('<i>Lūdōs <b>spectātum</b> īmus.</i>', 'Supino em <i>-um</i> depois de verbo de movimento (<i>īmus</i>): "Vamos assistir aos jogos." Tem objeto, <i>lūdōs</i>.'),
            ('<i>rēs horribilis <b>audītū</b></i>', 'Supino em <i>-ū</i> com adjetivo: "uma coisa horrível de ouvir".'),
            ('<i>Lēgātōs <b>missūrus</b> est.</i>', 'Particípio futuro com <i>est</i>: perifrástica ativa. "Ele está para enviar (vai enviar) embaixadores."'),
            ('<i>in <b>librīs legendīs</b></i>', 'Gerundivo, ablativo plural masculino, concordando com <i>librīs</i>, depois de <i>in</i>: construção gerundiva. "Na leitura dos livros, lendo livros."'),
        ]),
        exercicio('Exercício 2 · O gerúndio', 'Traduza. Vocabulário: <i>cupiditās, -ātis</i>, desejo; <i>vincō</i>, vencer; <i>fugiō</i>, fugir; <i>lūdus</i>, escola; <i>legō</i>, ler; <i>dīligentia</i>, diligência; <i>scrībō</i>, escrever; <i>exerceō</i>, exercitar; <i>memoria</i>, memória.', [
            ('<i>Cupiditās vincendī mīlitēs incitābat.</i> (<i>incitō</i>, estimular)', '"O desejo de vencer estimulava os soldados." Gerúndio genitivo dependendo de <i>cupiditās</i>.'),
            ('<i>Fugiendō salūtem petīvērunt.</i> (<i>salūs, -ūtis</i>, salvação)', '"Buscaram a salvação fugindo." Ablativo de meio: o gerúndio português vai bem.'),
            ('<i>Puer in lūdum vēnit legendī et scrībendī causā.</i>', '"O menino veio à escola para ler e escrever" (lit. "por causa de ler e de escrever"). <i>Causā</i> + genitivo do gerúndio: finalidade.'),
            ('<i>Memoria exercendō augētur.</i> (<i>augeō</i>, aumentar)', '"A memória aumenta com o exercício (exercitando-se)." Ablativo do gerúndio, meio.'),
            ('<i>Dē bene vīvendō disputābant.</i> (<i>disputō</i>, discutir)', '"Discutiam sobre viver bem." <i>Dē</i> + ablativo do gerúndio; o advérbio <i>bene</i> modifica o gerúndio, que continua sendo verbo.'),
        ]),
        exercicio('Exercício 3 · Do gerúndio ao gerundivo', 'Reescreva com a construção gerundiva e traduza. Diga se a troca era opcional ou obrigatória.', [
            ('<i>cupidus urbem videndī</i>', '<i>cupidus urbis videndae</i>, "desejoso de ver a cidade". Opcional (genitivo), mas a gerundiva é mais comum.'),
            ('<i>ad capiendum castra</i> (forma incorreta)', '<i>ad castra capienda</i>, "para tomar o acampamento". Obrigatória: depois de preposição o gerúndio não leva objeto. <i>Castra</i> é neutro plural, e o gerundivo também: <i>capienda</i>.'),
            ('<i>lēgēs mūtandō</i>', '<i>lēgibus mūtandīs</i>, "mudando as leis". Opcional (ablativo sem preposição).'),
            ('<i>pācem petendī causā</i>', '<i>pācis petendae causā</i>, "para pedir a paz". Opcional (genitivo com <i>causā</i>).'),
            ('<i>in servandō patriam</i> (forma incorreta)', '<i>in patriā servandā</i>, "em salvar a pátria". Obrigatória: depois de <i>in</i>.'),
        ]),
        exercicio('Exercício 4 · As perifrásticas', 'Traduza, distinguindo obrigação (passiva) de intenção (ativa). Vocabulário: <i>pūniō</i>, punir; <i>servō</i>, salvar; <i>proficīscor, profectus sum</i>, partir; <i>pugnō</i>, combater; <i>cīvis</i>, cidadão.', [
            ('<i>Hīc mīles pūniendus est.</i>', '"Este soldado deve ser punido." Perifrástica passiva pessoal.'),
            ('<i>Nōbīs patria servanda est.</i>', '"Nós devemos salvar a pátria." <i>Nōbīs</i>, dativo de agente, vira sujeito em português.'),
            ('<i>Cōnsul profectūrus erat.</i>', '"O cônsul estava para partir (ia partir)." Perifrástica ativa com particípio futuro do depoente <i>proficīscor</i>.'),
            ('<i>Cīvibus pugnandum erit.</i>', '"Os cidadãos deverão combater." Perifrástica impessoal (verbo intransitivo), no futuro.'),
            ('<i>Mihi multa eō diē agenda erant.</i> (<i>multa</i>, muitas coisas; <i>eō diē</i>, naquele dia)', '"Eu tinha de fazer muitas coisas naquele dia." <i>Multa</i> (neutro plural) é o sujeito, e <i>agenda</i> concorda com ele; por isso <i>erant</i> está no plural.'),
        ]),
        exercicio('Exercício 5 · O supino e as maneiras de dizer finalidade', 'Traduza para o latim de duas maneiras: com supino e com <i>ad</i> + gerundivo (ou gerúndio, se o verbo for intransitivo). Vocabulário: <i>veniō</i>, vir; <i>salūtō</i>, saudar; <i>rēx, rēgis</i>, rei; <i>mittō</i>, enviar; <i>auxilium</i>, ajuda; <i>petō, petītum</i>, pedir; <i>eō</i>, ir; <i>cubō, cubitum</i>, deitar-se.', [
            ('Vieram saudar o rei.', 'Supino: <i>Rēgem salūtātum vēnērunt.</i> Gerundivo: <i>Ad rēgem salūtandum vēnērunt.</i> O supino conserva o objeto no acusativo; o gerundivo concorda com ele.'),
            ('Enviaram mensageiros para pedir ajuda.', 'Supino: <i>Nūntiōs auxilium petītum mīsērunt.</i> Gerundivo: <i>Nūntiōs ad auxilium petendum mīsērunt.</i> (<i>nūntius</i>, mensageiro.) <i>Mittō</i> é verbo de movimento (fazer ir), por isso admite o supino.'),
            ('Vou deitar-me.', 'Supino: <i>Eō cubitum.</i> Com gerúndio (o verbo é intransitivo, não há gerundivo): <i>Eō ad cubandum</i>. Com verbos de ir e vir e sem objeto, o supino é a forma mais curta e idiomática.'),
            ('Isto é fácil de fazer.', '<i>Hōc facile est factū.</i> Supino em <i>-ū</i> depois de adjetivo. Também se diz <i>Hōc facile est ad faciendum</i>, e a prosa usa as duas.'),
        ]),
        exercicio('Exercício 6 · Leitura autêntica', 'Identifique cada forma em <i>-nd-</i>, diga se é gerúndio ou gerundivo e traduza. Vocabulário: <i>potestās, -ātis</i>, poder; <i>cūrō</i>, curar; <i>īnfirmitās, -ātis</i>, doença; <i>ēiciō</i>, expulsar; <i>daemonium</i>, demônio; <i>dīrigō</i>, dirigir; <i>pēs, pedis</i>, pé; <i>via</i>, caminho; <i>pāx, pācis</i>, paz.', [
            ('<i>Et dedit illīs potestātem cūrandī īnfirmitātēs et ēiciendī daemonia.</i> (Marcos 3,15)', '<i>Cūrandī</i> e <i>ēiciendī</i>: gerúndios no genitivo, dependendo de <i>potestātem</i>, cada um com um objeto direto (<i>īnfirmitātēs</i>, <i>daemonia</i>). O gerúndio com objeto é possível no genitivo, embora a construção gerundiva (<i>īnfirmitātum cūrandārum</i>) também existisse. "E deu-lhes o poder de curar as doenças e de expulsar os demônios."'),
            ('<i>... ad dīrigendōs pedēs nostrōs in viam pācis.</i> (Lucas 1,79, fim do versículo)', '<i>Dīrigendōs</i>: gerundivo, acusativo plural masculino, concordando com <i>pedēs</i>, regido por <i>ad</i>: construção gerundiva obrigatória depois de preposição. "Para dirigir os nossos pés no caminho da paz."'),
            ('<i>Nīl dēspērandum Teucrō duce et auspice Teucrō.</i> (Horácio, <i>Odes</i> 1.7.27)', '<i>Dēspērandum</i>: gerundivo neutro em perifrástica impessoal, com <i>est</i> subentendido; <i>nīl</i> funciona como complemento ("de nada"). "Não se deve desesperar de nada, sendo Teucro o guia e o protetor." <i>Teucrō duce</i> e <i>auspice Teucrō</i> são ablativos absolutos nominais (capítulo 30).'),
        ]),
    ],
    leituras=['d-ooge-latin-for-beginners', 'kingdon-gradatim-an-easy-latin-translation-book', 'lhomond-urbis-romae-viri-illustres-selecoes', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'phaedrus-fabulae-aesopiae', 'bennett-new-latin-grammar'],
    leituras_nota='Os exercícios de gerúndio e gerundivo de <i>Latin for Beginners</i>, de D\'Ooge, e as frases graduadas de <i>Gradatim</i> fixam as formas. Nas vidas do <i>De viris illustribus</i> de Lhomond, procure <i>ad</i> + gerundivo e <i>causā</i> + genitivo, a cada página. Na Vulgata, leia Eclesiastes 3,1–8 inteiro (uma lista de gerúndios) e o cântico de Zacarias, Lucas 1,68–79. As fábulas de Fedro (capítulo 42) são uma boa primeira leitura autêntica para reencontrar estas formas em contexto. Bennett (§§ 337.8–340) resume tudo em quatro páginas.',
)
