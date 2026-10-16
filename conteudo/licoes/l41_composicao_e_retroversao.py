from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='41-composicao-e-retroversao', titulo='Do latim lido ao latim escrito: composição e retroversão',
    titulo_latim='Dē compositiōne', tempo='80 min',
    resumo='Um método para passar do português ao latim: entender o sentido antes das palavras, escolher a construção (oração infinitiva, ut/nē, ablativo absoluto, gerundivo, interrogativa indireta), ordenar a frase e pôr os conectivos no lugar certo, evitar os decalques do português (artigos, o "que" para tudo, possessivos demais, o "seu") e usar as expressões idiomáticas latinas. Com uma frase de César como modelo e exercícios graduados de retroversão com respostas-modelo e alternativas comentadas.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['retroversão', 'composição latina', 'método de retroversão', 'escolha da construção', 'oração infinitiva', 'finalidade sem infinitivo', 'ut e nē', 'ablativo absoluto × particípio conjunto',
             'gerundivo', 'ordem das palavras', 'período latino', 'sujeito comum antes da subordinada', 'conectivos pospositivos', 'itaque, igitur, enim, nam, autem, tamen',
             'decalques do português', 'artigo', 'os vários "que"', 'possessivo', 'suus × eius', 'o "seu" português', 'expressões idiomáticas', 'grātiās agere', 'poenās dare', 'in animō habēre', 'estilo', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Toda a sintaxe das partes II e III, em especial a oração infinitiva (capítulo 28), o ablativo absoluto (30), o gerúndio e o gerundivo (31), as orações com ut e nē (33), cum e a sequência dos tempos (34), a interrogativa indireta (35), as condicionais (36), as causais e concessivas (37) e o discurso indireto (38). Os pronomes reflexivos e possessivos do capítulo 14 e o relativo de ligação do capítulo 16 são usados o tempo todo.',
                       licoes=['14-os-pronomes-pessoais', '16-o-pronome-relativo', '28-a-oracao-infinitiva', '30-o-ablativo-absoluto', '31-gerundio-e-gerundivo', '33-oracoes-finais-e-consecutivas', '34-cum-e-sequencia-dos-tempos', '38-o-discurso-indireto']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar',
                   nota='§ 243.1 (possessivos só por clareza; 243.1a posição) e 243.3 (ipsōrum de ênfase); § 244 (sē e suus: reflexivo direto e indireto); § 251.6 (relativo no início da frase, como conectivo); § 282 (orações finais: ut, quō, nē); § 331 (oração infinitiva depois de verbos de dizer e pensar); § 337.8 (gerundivo de obrigação); §§ 343–345 (sed, autem pospositivo, tamen; itaque, igitur pospositivo, 344.2: igitur nunca com et; nam, enim pospositivo); § 346 (assíndeto); §§ 348–349 (ordem normal e enfática); § 350.7b (magnā cum cūrā), 350.8 (autem, enim, igitur em segundo lugar), 350.9 (palavras que retomam a frase anterior vêm primeiro); § 351.1–2 (unidade de sujeito; sujeito ou objeto comum antes das duas orações) e 351.5 (o período); §§ 352–359 (dicas de estilo: 353.1 plural, 353.3 concretude, 353.5 sem locução prepositiva junto do nome; 356.2 como suprir o particípio perfeito ativo; 357.2 sujeito e objeto com o mesmo infinitivo; 358.1–2 "para" = prō, ad; 359.1 genitivo de posse × dativo de posse)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc',
                   nota='§§ 299–301 (reflexivo), § 302 (possessivos); § 419 e nota (ablativo absoluto; o seu substantivo raramente designa alguém mencionado na mesma oração); §§ 500–507 (gerúndio e gerundivo); §§ 530–531 (orações finais com ut, nē, relativo); § 533 (a finalidade nunca se exprime pelo infinitivo simples; as formas possíveis); §§ 577–579 (discurso indireto); §§ 595–599 (ordem das palavras: 596 sujeito no início e verbo no fim; 597 a palavra mais importante primeiro; 599.b itaque primeiro; enim, autem, vērō, quoque nunca primeiro; igitur em geral segundo)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 400 e nota 3 (conjunções coordenativas; autem, enim, quidem, vērō nunca começam a frase), § 423 (orações finais com ut, nē)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 491 (ordem normal da proposição; lugar de cada conjunção: sed primeiro, autem e vērō depois de uma ou duas palavras, itaque primeiro, igitur e enim em geral em segundo); n. 492 (ênfase no início ou no fim); n. 493 (a subordinada condicional, temporal, causal etc. em geral antes da principal; o OCR lê "495")', tipo='dominio_publico'),
        referencia('César, Commentarii de bello Gallico 1.1.1', None, catalogo='caesar-commentarii-de-bello-gallico-texto-integral', url='https://www.thelatinlibrary.com/caesar/gall1.shtml', nota='frase autêntica analisada na seção 6 (texto conferido em The Latin Library; macrons acrescentados)', tipo='dominio_publico'),
    ],
    objetivos=[
        'Aplicar um método em cinco passos para verter uma frase portuguesa ao latim, começando pelo sentido e não pelas palavras.',
        'Escolher, para cada estrutura do português ("disse que", "para", "depois de", "é preciso", "perguntou se"), a construção latina adequada e as suas alternativas.',
        'Ordenar uma frase e um período ao modo latino e colocar corretamente os conectivos, inclusive os pospositivos (<i>autem, enim, igitur</i>).',
        'Reconhecer e evitar os decalques mais comuns do português: artigo, "que" para tudo, possessivo desnecessário, "seu", infinitivo de finalidade.',
        'Usar expressões idiomáticas latinas (<i>grātiās agere, poenās dare, in animō habēre</i>…) e verter um parágrafo curto com coesão.',
    ],
    secoes=[
        ('Por que escrever em latim, e por onde começar', f'''
<p>Ler latim é reconhecer; escrever latim é escolher. Quem só lê pode adivinhar que <i>ut</i> introduz alguma coisa e seguir em frente; quem escreve precisa decidir se é <i>ut</i> com subjuntivo, <i>ad</i> com gerundivo ou uma oração relativa, em que tempo e com que ordem das palavras. Por isso a <b>retroversão</b>, a tradução do português para o latim, foi durante séculos o principal exercício das escolas: ela obriga a saber exatamente o que se sabe só de vista. Este capítulo não pretende fazer de você um prosador ciceroniano. O objetivo é mais modesto e mais útil: que você consiga escrever frases corretas e naturais, e que, ao fazê-lo, leia os autores com mais precisão.</p>
<p>O erro de quem começa é traduzir palavra por palavra, na ordem do português, procurando cada termo no dicionário. O resultado é português com terminações latinas. O caminho certo começa antes das palavras:</p>
{tabela(['Passo', 'Pergunta', 'Exemplo: "Os embaixadores disseram que o rei viria logo."'], [
    ['1. Sentido', 'O que a frase quer dizer, e quais são as relações lógicas (tempo, causa, finalidade, fala relatada)?', 'uma fala relatada: alguém afirmou algo'],
    ['2. Construção', 'Que construção latina exprime essa relação?', 'verbo de dizer → oração infinitiva (capítulo 28)'],
    ['3. Formas', 'Que tempos e modos a construção pede?', '"viria" é posterior ao dizer → infinitivo futuro <i>ventūrum esse</i>'],
    ['4. Palavras', 'Que palavras latinas dizem isso, com que regência?', '<i>lēgātus</i>, <i>rēx</i>, <i>veniō</i>, <i>mox</i>, <i>dīcō</i>'],
    ['5. Ordem e conferência', 'Como um romano ordenaria a frase? Todas as concordâncias estão certas?', '<i>Lēgātī rēgem mox ventūrum esse dīxērunt.</i> (<i>ventūrum</i> concorda com <i>rēgem</i>)'],
], 'O método em cinco passos')}
<p>O passo 1 é o mais importante e o mais esquecido. O português e o latim raramente dizem a mesma coisa com a mesma estrutura: "disse que" não é <i>dīxit quod</i>, "para ver" não é <i>vidēre</i>, "depois de ouvir" não é <i>post audīre</i>. Só quem pergunta "que relação é esta?" chega à construção latina.</p>
{dica('<b>Use o dicionário nos dois sentidos.</b> Achou uma palavra latina num dicionário português-latim? Confira-a num dicionário latim-português ou no Lewis &amp; Short (capítulo 7): veja a regência, os exemplos dos autores e se o sentido é mesmo o que você quer. Muitos erros de composição são palavras certas no sentido errado.')}
'''),
        ('Escolher a construção', f'''
<p>Toda a sintaxe das partes II e III serve agora ao contrário. A tabela reúne as estruturas portuguesas mais frequentes e as construções latinas que as exprimem; os exemplos são originais e cada linha remete ao capítulo onde a construção foi estudada.</p>
{tabela(['Em português', 'Em latim', 'Exemplo'], [
    ['"disse / sabe / julga que…"', 'oração infinitiva (cap. 28)', '<i>Nūntius dīxit hostēs adesse.</i> O mensageiro disse que os inimigos estavam ali.'],
    ['"para / para que…" (finalidade)', '<i>ut</i> / <i>nē</i> + subjuntivo; relativa final; <i>ad</i> + gerundivo; <i>causā</i> + genitivo (caps. 31 e 33)', '<i>Vēnērunt ut auxilium peterent.</i> Vieram para pedir ajuda.'],
    ['"mandou / pediu / exortou que…"', '<i>ut</i> / <i>nē</i> + subjuntivo; com <i>iubeō</i> e <i>vetō</i>, infinitivo (caps. 28 e 33)', '<i>Cōnsul cīvēs ōrāvit nē urbem relinquerent.</i> O cônsul pediu aos cidadãos que não deixassem a cidade.'],
    ['"tão… que…" (consequência)', '<i>tam, ita, tantus… ut</i> / <i>ut nōn</i> (cap. 33)', '<i>Tam fessī erant ut ambulāre nōn possent.</i> Estavam tão cansados que não podiam andar.'],
    ['"depois de fazer", "feito isso", "tendo feito"', 'ablativo absoluto; particípio conjunto; <i>cum</i> + subjuntivo (caps. 29, 30, 34)', '<i>Hīs rēbus cognitīs, dux profectus est.</i> Conhecidos esses fatos, o general partiu.'],
    ['"é preciso / deve-se…"', 'perifrástica passiva com gerundivo (cap. 31)', '<i>Lēgēs servandae sunt.</i> As leis devem ser respeitadas.'],
    ['"perguntou quem / se / por que…"', 'interrogativa indireta (cap. 35)', '<i>Rogāvit quis vēnisset.</i> Perguntou quem tinha vindo.'],
    ['"se…", "embora…", "porque…"', 'condicionais; concessivas e causais (caps. 36 e 37)', '<i>Quamquam aeger erat, labōrābat.</i> Embora estivesse doente, trabalhava.'],
], 'Do português ao latim: as escolhas principais', latim_cols=())}
<h3>A finalidade nunca é um infinitivo</h3>
<p>Este ponto merece destaque, porque o português (e o inglês) exprimem a finalidade com um infinitivo: "vieram <b>para pedir</b>". O latim clássico não faz isso. Allen &amp; Greenough são categóricos: a finalidade nunca se exprime pelo infinitivo simples, salvo em expressões idiomáticas e, raramente, em poesia (§ 533). As alternativas são muitas, e escolher entre elas é questão de estilo:</p>
{exemplos([
    ('Vēnērunt <b>ut</b> auxilium <b>peterent</b>.', '<i>ut</i> + subjuntivo: a forma mais comum e sempre segura (Bennett § 282; A&amp;G § 531).'),
    ('Vēnērunt <b>quī</b> auxilium <b>peterent</b>.', 'relativa final: "vieram, (homens) que pedissem ajuda".'),
    ('Vēnērunt <b>ad</b> auxilium <b>petendum</b>.', '<i>ad</i> + gerundivo, que concorda com o objeto (capítulo 31).'),
    ('Vēnērunt auxiliī <b>petendī causā</b>.', 'genitivo do gerundivo + <i>causā</i>, posposto.'),
])}
<h3>Como suprir o particípio que falta</h3>
<p>O português diz "tendo ouvido", "depois de ouvir", "ouvido isso". O latim não tem particípio perfeito ativo (só os depoentes o têm: <i>hortātus</i>, "tendo exortado"). Bennett resume as soluções (§ 356.2): o particípio perfeito de um depoente, o ablativo absoluto ou uma subordinada (<i>cum</i>, <i>postquam</i>, relativa). Há uma condição para o ablativo absoluto que o português não ensina: o seu substantivo <b>raramente</b> designa alguém ou algo mencionado na mesma oração (A&amp;G § 419, nota). Se a pessoa reaparece como objeto do verbo principal, use o particípio conjunto:</p>
{comparacao('Ablativo absoluto ou particípio conjunto?', ['Latim', 'Comentário'], [
    ['<i>Cīvēs, <b>cōnsule audītō</b>, domum rediērunt.</i>', 'Certo: o cônsul não volta a aparecer na oração principal. "Ouvido o cônsul, os cidadãos voltaram para casa."'],
    ['<i>Dux, <b>mīlitibus convocātīs</b>, eōs laudāvit.</i>', 'Evite: os soldados são retomados por <i>eōs</i> na mesma oração.'],
    ['<i>Dux <b>mīlitēs convocātōs</b> laudāvit.</i>', 'Melhor: particípio conjunto, concordando com o objeto. "O general reuniu os soldados e os louvou."'],
])}
'''),
        ('Ordem das palavras e conectivos', f'''
<p>A ordem latina é livre no sentido de que as terminações, e não a posição, dizem a função (capítulo 2). Mas não é arbitrária. Na frase neutra, o sujeito vem primeiro, depois os complementos, e o verbo fecha a oração (Bennett § 348; A&amp;G § 596; Ravizza n. 491): <i>Magister puerīs fābulam nārrat.</i> Qualquer desvio dessa ordem chama a atenção para a palavra deslocada, que vai para o início ou para o fim (Bennett § 349; A&amp;G § 597; Ravizza n. 492): <i>Fābulam magister nārrat, nōn carmen</i>, "é uma história que o professor conta, não um poema". Escrever em latim é, portanto, escolher a ênfase pela posição, como o português faz com a entonação ou com "é… que".</p>
<p>Algumas regras de colocação valem quase sempre. Os advérbios precedem a palavra que modificam (<i>valdē dīligēns</i>, Bennett § 350.6); as preposições precedem o seu caso, mas um adjetivo pode vir antes delas: <i>magnā cum cūrā</i> (Bennett § 350.7b). As palavras que retomam a frase anterior vêm no começo da nova frase (§ 350.9), e é por isso que o latim gosta tanto do relativo de ligação do capítulo 16: <i>Quae cum rēx audīvisset, rīsit</i>, "quando o rei ouviu isso, riu".</p>
<h3>O período: o que é comum vem antes</h3>
<p>Num período com subordinada, a palavra que serve de sujeito (ou de objeto) às duas orações fica <b>antes de ambas</b> (Bennett § 351.2), e as subordinadas de tempo, causa, condição e concessão costumam vir antes da principal (Bennett § 351.3; Ravizza n. 493). O resultado é o período latino típico: o sujeito abre, as circunstâncias se encaixam no meio, e o verbo principal fecha o pensamento.</p>
{diagrama_frase([('Mīlitēs', 'sujeito comum · abre o período'), ('cum … vīdissent', 'subordinada · encaixada no meio'), ('ad arma', 'complemento · para onde'), ('cucurrērunt', 'verbo principal · fecha')], '<i>Mīlitēs, cum hostēs appropinquāre vīdissent, ad arma cucurrērunt.</i> = Os soldados, ao verem que os inimigos se aproximavam, correram às armas. (Frase original; dentro da subordinada há uma oração infinitiva.)')}
<p>Compare com a ordem portuguesa, "Quando os soldados viram que os inimigos se aproximavam, correram às armas": aqui o sujeito entra na subordinada. Em latim, <i>Cum mīlitēs hostēs appropinquāre vīdissent, ad arma cucurrērunt</i> não é errado, mas a ordem com <i>Mīlitēs</i> à frente é a mais natural, porque mostra desde o início de quem se fala nas duas orações. Bennett chama a essa preferência <b>unidade de sujeito</b> (§ 351.1).</p>
<h3>Os conectivos e o seu lugar</h3>
<p>Um texto latino raramente começa uma frase sem algo que a ligue à anterior: um conectivo, um relativo de ligação, um demonstrativo. Ao escrever, faça o mesmo. E respeite a posição de cada conectivo, porque vários deles são <b>pospositivos</b>: nunca abrem a frase (Bennett § 350.8; A&amp;G § 599.b; Kennedy § 400, nota 3; Ravizza n. 491).</p>
{tabela(['Conectivo', 'Sentido', 'Posição'], [
    ['<i>itaque</i>', 'por isso, e assim', '1º lugar'],
    ['<i>igitur</i>', 'portanto, então', 'em geral 2º lugar; nunca junto de <i>et, -que, atque, neque</i> (Bennett § 344.2)'],
    ['<i>nam</i>', 'pois, é que', '1º lugar'],
    ['<i>enim</i>', 'pois, com efeito', '2º lugar (3º depois de <i>est</i>: <i>ita est enim</i>)'],
    ['<i>sed</i>', 'mas', '1º lugar'],
    ['<i>autem</i>', 'por sua vez, porém', '2º lugar; põe em contraste a palavra anterior'],
    ['<i>tamen</i>', 'contudo, mesmo assim', 'em geral depois da palavra enfatizada, mas pode abrir a frase (Bennett § 343.1f)'],
], 'Conectivos frequentes e sua posição')}
<p><i>Nam</i> e <i>enim</i> dizem o mesmo, "pois", e diferem só na posição: <i>Nam pluit</i> = <i>Pluit enim</i>. O mesmo vale, em parte, para <i>itaque</i> e <i>igitur</i>: <i>itaque</i> narra a consequência ("e assim"), <i>igitur</i> tira uma conclusão ("portanto").</p>
'''),
        ('Os decalques do português', f'''
<p>Um <b>decalque</b> é a cópia de uma estrutura de uma língua em outra. Quem escreve latim a partir do português tende a reproduzir, sem perceber, hábitos que o latim não tem. Os mais comuns são estes.</p>
<h3>Artigos</h3>
<p>O latim não tem artigo. "O rei" é <i>rēx</i>, "um servo" é <i>servus</i>. Não use <i>ille</i> para "o" nem <i>ūnus</i> para "um": <i>ille rēx</i> é "aquele rei" (ou "o famoso rei") e <i>ūnus servus</i>, "um só servo". Quando o português "um" quer dizer "um certo", o latim tem <i>quīdam</i>: <i>viātor quīdam</i>, "um viajante (que não preciso nomear)".</p>
<h3>Os muitos "que"</h3>
<p>O português usa "que" para quase tudo. O latim tem uma construção diferente para cada função, e a primeira tarefa é descobrir qual é:</p>
{tabela(['"que" português', 'Função', 'Em latim'], [
    ['"o livro <b>que</b> li"', 'pronome relativo', '<i>liber quem lēgī</i>'],
    ['"disse <b>que</b> viria"', 'conteúdo de uma fala ou pensamento', 'oração infinitiva: <i>dīxit sē ventūrum esse</i>'],
    ['"pediu <b>que</b> viesse"', 'ordem, pedido', '<i>ut</i> + subjuntivo: <i>rogāvit ut venīret</i>'],
    ['"tão alto <b>que</b>…"', 'consequência', '<i>tam altus ut…</i>'],
    ['"maior <b>que</b> o pai"', 'comparação', '<i>quam</i> (ou ablativo): <i>maior quam pater</i>, <i>maior patre</i>'],
    ['"temo <b>que</b> venha"', 'temor', '<i>nē</i> + subjuntivo: <i>timeō nē veniat</i> (capítulo 33)'],
], 'Um "que", seis construções')}
<p>O caso mais traiçoeiro é o segundo. <i>Dīxit quod hostēs venīrent</i> é um decalque do português; no latim clássico a fala relatada vai em oração infinitiva: <i>dīxit hostēs venīre</i>. A construção com <i>quod</i> ou <i>quia</i> existe, mas é do latim tardio e cristão (capítulo 28); se você está escrevendo latim clássico, evite-a.</p>
<h3>Possessivos, e o "seu"</h3>
<p>O latim só usa o possessivo quando ele é necessário para a clareza ou para a ênfase (Bennett § 243.1). "Marco ama a sua mãe" é simplesmente <i>Mārcus mātrem amat</i>; de quem mais seria a mãe? <i>Mātrem suam</i> só se houver contraste ("a <b>própria</b> mãe, não a de outro"), e então o possessivo tende a vir antes do nome (§ 243.1a).</p>
<p>Quando o possessivo é necessário, o "seu" português esconde três palavras latinas diferentes, como você viu no capítulo 14. <i>Suus</i> refere-se ao sujeito da oração (ou, numa subordinada, ao sujeito da principal: Bennett § 244; A&amp;G §§ 299–301); <i>eius</i> e <i>eōrum</i> referem-se a outra pessoa; e, no português do Brasil, "seu" muitas vezes quer dizer "de você", e então é <i>tuus</i> (ou <i>vester</i>).</p>
{comparacao('Três "seus"', ['Latim', 'Português'], [
    ['<i>Mārcus Iūliam et patrem <b>suum</b> vīdit.</i>', 'Marco viu Júlia e o seu pai (o pai de Marco).'],
    ['<i>Mārcus Iūliam et patrem <b>eius</b> vīdit.</i>', 'Marco viu Júlia e o pai dela.'],
    ['<i>Librumne <b>tuum</b> attulistī?</i>', 'Você trouxe o seu livro? (o livro de você)'],
])}
<h3>Outros decalques</h3>
{comparacao('Decalque e latim idiomático', ['Decalque', 'Latim idiomático', 'Por quê'], [
    ['<i>Vēnit vidēre amīcum.</i>', '<i>Vēnit ut amīcum vidēret.</i>', 'a finalidade não se exprime por infinitivo (A&amp;G § 533)'],
    ['<i>urbs dē marī</i>', '<i>urbs maritima</i>', 'o latim evita locução prepositiva presa a um nome; prefere adjetivo ou genitivo (Bennett § 353.5)'],
    ['<i>Ītalia ducem benignē accēpit.</i>', '<i>Ītalī ducem benignē accēpērunt.</i>', 'não é erro, mas o latim é menos ousado que o português em personificar: prefere as pessoas às abstrações e aos nomes de lugar como sujeitos de ações humanas (Bennett § 353.3)'],
    ['<i>pugnāre lībertātī</i>', '<i>pugnāre prō lībertāte</i>', '"lutar por, em defesa de" é <i>prō</i> + ablativo, não dativo (Bennett § 358.1)'],
    ['<i>Imperāvit ut mīlitēs veniant.</i>', '<i>Imperāvit ut mīlitēs venīrent.</i>', 'depois de um tempo passado, o subjuntivo vai para o imperfeito (sequência dos tempos, capítulo 34)'],
])}
<p>Um último cuidado, de estilo mais que de gramática: o latim é mais concreto e mais exato no número que o português. "Os germanos cuidam do corpo" é <i>corpora cūrant</i>, no plural, porque cada um tem o seu (Bennett § 353.1); "todas as coisas estão perdidas" é <i>omnia</i>, neutro plural, onde o português diz "tudo" (§ 353.2).</p>
'''),
        ('Expressões idiomáticas e estilo', f'''
<p>Toda língua tem combinações fixas que não se traduzem palavra por palavra: em português "tomar uma decisão", "prestar atenção", "fazer as pazes". O latim tem as suas, e usá-las é o que mais distingue um latim natural de um latim decalcado. Aprenda estas como unidades, com a regência:</p>
{tabela(['Expressão', 'Literalmente', 'Sentido', 'Exemplo original'], [
    ['<i>grātiās agere</i> + dat.', 'render graças', 'agradecer', '<i>Deīs grātiās agimus.</i>'],
    ['<i>poenās dare</i>', 'dar (pagar) as penas', 'ser punido', '<i>Prōditōrēs poenās dedērunt.</i>'],
    ['<i>in animō habēre</i> + inf.', 'ter no espírito', 'ter a intenção de', '<i>In animō habeō Rōmam vīsere.</i>'],
    ['<i>operam dare</i> + dat.', 'dar trabalho', 'dedicar-se a', '<i>Studiīs operam dā!</i>'],
    ['<i>cōnsilium capere</i>', 'tomar um plano', 'decidir', '<i>Dux novum cōnsilium cēpit.</i>'],
    ['<i>certiōrem facere</i> (dē)', 'fazer mais certo', 'informar', '<i>Cōnsulem dē adventū hostium certiōrem fēcit.</i>'],
    ['<i>iter facere</i>', 'fazer caminho', 'viajar, marchar', '<i>Exercitus per Alpēs iter faciēbat.</i>'],
    ['<i>proelium committere</i>', 'juntar o combate', 'travar batalha', '<i>Cum Gallīs proelium commīsērunt.</i>'],
    ['<i>bellum gerere</i>', 'conduzir a guerra', 'fazer guerra', '<i>Rōmānī multa bella gessērunt.</i>'],
    ['<i>sē recipere</i>', 'receber-se de volta', 'retirar-se', '<i>Hostēs in silvās sē recēpērunt.</i>'],
], 'Expressões idiomáticas frequentes')}
<p>Repare em <i>certiōrem facere</i>: o adjetivo concorda com a pessoa informada (<i>cōnsulem … certiōrem</i>; para várias pessoas, <i>certiōrēs</i>). E em <i>poenās dare</i>: o sujeito é quem sofre a pena, não quem a aplica.</p>
<h3>Cinco conselhos de estilo</h3>
<ul>
<li><b>Prefira verbos a substantivos abstratos.</b> "Após a chegada do cônsul, …" fica mais latino como <i>cum cōnsul advēnisset, …</i> do que como <i>post adventum cōnsulis</i>, embora esta forma também seja correta.</li>
<li><b>Mantenha o mesmo sujeito</b> ao longo do período (unidade de sujeito, Bennett § 351.1) e ponha-o à frente.</li>
<li><b>Subordine.</b> Onde o português enfileira "e… e… e", o latim prefere um particípio ou uma subordinada e um só verbo principal.</li>
<li><b>Ligue as frases</b> com conectivos e relativos de ligação; não deixe frases soltas.</li>
<li><b>Desconfie do que soa igual ao português.</b> Se a sua frase latina tem a mesma ordem e as mesmas palavras de ligação que a portuguesa, provavelmente é um decalque.</li>
</ul>
{observacao('Imitar, não inventar', 'A melhor fonte de latim idiomático é a leitura. Quando um autor resolve bem uma ideia que você quer exprimir, anote a frase inteira num caderno de expressões. Os bons manuais antigos de composição eram, no fundo, coleções organizadas dessas imitações.')}
'''),
        ('Um modelo autêntico: a primeira frase de César', f'''
<p>A primeira frase da <i>Guerra da Gália</i> é um pequeno manual de composição. Leia-a pensando não no que ela diz, mas em <b>como</b> César escolheu dizê-lo:</p>
{exemplos([('Gallia est omnis dīvīsa in partēs trēs, quārum ūnam incolunt Belgae, aliam Aquītānī, tertiam quī ipsōrum linguā Celtae, nostrā Gallī appellantur.', 'A Gália, em seu conjunto, está dividida em três partes, das quais uma é habitada pelos belgas, outra pelos aquitanos, a terceira pelos que na sua própria língua se chamam celtas, na nossa, gauleses. (César, <i>Guerra da Gália</i> 1.1.1)')])}
{analise('César, De bello Gallico 1.1.1', [
    ('Gallia', 'Gallia, -ae (f.), Gália', 'nominativo singular', 'sujeito'),
    ('est … dīvīsa', 'dīvidō, -ere, dīvīsī, dīvīsum, dividir', 'particípio perfeito passivo com <i>est</i>', 'predicado: "está dividida" (estado)'),
    ('omnis', 'omnis, -e, todo', 'nominativo singular feminino', 'concorda com <i>Gallia</i>: "no seu conjunto"'),
    ('in partēs trēs', 'pars, partis (f.), parte; trēs, tria, três', '<i>in</i> + acusativo plural', 'resultado da divisão: "em três partes"'),
    ('quārum', 'quī, quae, quod', 'genitivo plural feminino', 'relativo; antecedente <i>partēs</i>: "das quais"'),
    ('ūnam', 'ūnus, -a, -um, um', 'acusativo singular feminino', 'objeto de <i>incolunt</i> (subentende-se <i>partem</i>)'),
    ('incolunt', 'incolō, -ere, habitar', 'presente, 3ª pessoa do plural', 'verbo, dito uma vez e subentendido duas'),
    ('Belgae', 'Belgae, -ārum (m. pl.), belgas', 'nominativo plural', 'sujeito de <i>incolunt</i>'),
    ('aliam', 'alius, -a, -ud, outro', 'acusativo singular feminino', 'objeto de <i>incolunt</i> subentendido'),
    ('Aquītānī', 'Aquītānī, -ōrum (m. pl.), aquitanos', 'nominativo plural', 'sujeito de <i>incolunt</i> subentendido'),
    ('tertiam', 'tertius, -a, -um, terceiro', 'acusativo singular feminino', 'objeto de <i>incolunt</i> subentendido'),
    ('quī', 'quī, quae, quod', 'nominativo plural masculino', 'relativo sem antecedente: "(aqueles) que"; sujeito de <i>incolunt</i> subentendido e de <i>appellantur</i>'),
    ('ipsōrum', 'ipse, ipsa, ipsum', 'genitivo plural masculino', '"deles próprios", liga-se a <i>linguā</i>'),
    ('linguā', 'lingua, -ae (f.), língua', 'ablativo singular', 'meio: "na língua"'),
    ('Celtae', 'Celtae, -ārum (m. pl.), celtas', 'nominativo plural', 'predicativo de <i>quī</i>'),
    ('nostrā', 'noster, -tra, -trum, nosso', 'ablativo singular feminino', 'subentende-se <i>linguā</i>: "na nossa"'),
    ('Gallī', 'Gallī, -ōrum (m. pl.), gauleses', 'nominativo plural', 'predicativo de <i>quī</i>'),
    ('appellantur', 'appellō, -āre, chamar', 'presente passivo, 3ª pessoa do plural', 'verbo da relativa: "são chamados", fecha a frase'),
])}
<p>Seis lições de composição saem desta frase. <b>(1)</b> Não há um único artigo, e nada falta. <b>(2)</b> César não começa uma frase nova para cada parte: o relativo <i>quārum</i> pendura as três partes na primeira oração. <b>(3)</b> O verbo <i>incolunt</i> aparece uma vez e serve aos três membros, cada um reduzido a "objeto + sujeito" (<i>ūnam … Belgae, aliam Aquītānī, tertiam quī…</i>): é a economia que o capítulo 40 chamou de zeugma no sentido amplo. <b>(4)</b> Onde o português traduz com a passiva ("é habitada pelos belgas"), César usa a ativa com o objeto à frente; ao escrever, não transforme automaticamente em passiva o que o latim diz melhor na ativa. <b>(5)</b> "Na língua deles" não é <i>suā</i> nem <i>eōrum</i>, mas <i>ipsōrum</i>, "deles próprios", o genitivo de <i>ipse</i>, que sublinha o contraste com <i>nostrā</i> (compare Bennett § 243.3). <b>(6)</b> O verbo vai para o fim de cada oração: <i>est … dīvīsa</i> abre a principal com uma ordem enfática (<i>est</i> logo depois do sujeito), mas <i>incolunt</i> e <i>appellantur</i> fecham as suas.</p>
{dica('<b>Exercício de imitação.</b> Escreva, no modelo de César, uma frase sobre a sua cidade ou o seu estado: "<i>X est omnis dīvīsa in partēs trēs, quārum ūnam incolunt…, aliam…, tertiam…</i>". Mudar o conteúdo e manter a estrutura é o exercício de composição mais antigo e um dos mais eficazes.')}
'''),
    ],
    erros_comuns=[
        ('Exprimir a finalidade com o infinitivo: <i>Vēnērunt petere pācem</i> ("vieram para pedir a paz").', 'O latim clássico não usa o infinitivo de finalidade (A&amp;G § 533). Use <i>ut</i> + subjuntivo (<i>ut pācem peterent</i>), uma relativa final (<i>quī pācem peterent</i>), <i>ad</i> + gerundivo (<i>ad pācem petendam</i>) ou <i>causā</i> (<i>pācis petendae causā</i>).'),
        ('Traduzir "disse que" por <i>dīxit quod</i> ou <i>dīxit quia</i>.', 'No latim clássico, a fala e o pensamento relatados vão em oração infinitiva: <i>dīxit hostēs adesse</i>. A construção com <i>quod/quia</i> é do latim tardio e cristão (capítulo 28); use-a só se estiver imitando esse latim.'),
        ('Pôr um conectivo pospositivo no início: <i>Enim mīlitēs fessī erant</i>; <i>Autem puella cantat</i>; ou juntar <i>et igitur</i>.', '<i>Enim, autem, igitur</i> (e <i>vērō, quoque, quidem</i>) nunca abrem a frase: vêm depois da primeira palavra (Bennett § 350.8; A&amp;G § 599.b). Escreva <i>Mīlitēs enim fessī erant</i>, <i>Puella autem cantat</i>. E <i>igitur</i> nunca vai junto de <i>et</i> (Bennett § 344.2): use <i>itaque</i> ou só <i>igitur</i>.'),
        ('Usar <i>suus</i> para todo "seu" (ou <i>eius</i> quando o dono é o próprio sujeito).', 'Pergunte de quem é a coisa. Se é do sujeito, <i>suus</i>; se é de outra pessoa, <i>eius / eōrum</i>; se "seu" quer dizer "de você", <i>tuus</i>. <i>Mārcus Iūliam et patrem eius vīdit</i> = "o pai dela"; com <i>suum</i> seria o pai de Marco (capítulo 14; Bennett § 244).'),
        ('Encher a frase de possessivos e de artigos disfarçados (<i>ille, ūnus</i>).', 'O latim não tem artigo e só usa possessivo por clareza ou ênfase (Bennett § 243.1). <i>Ille rēx ūnum servum suum vocāvit</i> vira <i>Rēx servum vocāvit</i>: tudo o que se perdeu estava sobrando.'),
        ('Esquecer a sequência dos tempos: <i>Imperāvit ut veniant</i>.', 'Depois de um verbo principal no passado, o subjuntivo da subordinada vai para o imperfeito (simultaneidade ou posterioridade) ou para o mais-que-perfeito (anterioridade): <i>imperāvit ut venīrent</i> (capítulo 34). Confira sempre o tempo do verbo principal antes de escolher o da subordinada.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Uma frase, cinco soluções',
            'Verta para o latim: "Os camponeses foram à cidade para comprar trigo." Vocabulário: <i>agricola, -ae</i> (m.), camponês; <i>oppidum, -ī</i> (n.), cidade; <i>eō, īre, iī, itum</i>, ir; <i>emō, -ere, ēmī, ēmptum</i>, comprar; <i>frūmentum, -ī</i> (n.), trigo.', [
            ('Passo 1: qual é a relação lógica de "para comprar"?', 'Finalidade: a compra é o objetivo da ida. Logo, nada de infinitivo (<i>emere</i>), por mais natural que pareça em português (A&amp;G § 533).'),
            ('Passo 2: quais construções latinas exprimem a finalidade?', 'Quatro, todas corretas: <i>ut frūmentum emerent</i> (ut + subjuntivo); <i>quī frūmentum emerent</i> (relativa final); <i>ad frūmentum emendum</i> (ad + gerundivo concordando com <i>frūmentum</i>); <i>frūmentī emendī causā</i> (genitivo do gerundivo + <i>causā</i>). Com verbos de movimento há ainda o supino: <i>frūmentum ēmptum</i> (capítulo 31).'),
            ('Passo 3: em que tempo vai o subjuntivo?', '"Foram" é passado (perfeito <i>iērunt</i>), tempo secundário; a compra é posterior à ida, e por isso o subjuntivo vai no imperfeito: <i>emerent</i> (capítulo 34).'),
            ('Passo 4: "à cidade" precisa de preposição?', 'Sim: com nomes comuns de lugar, o movimento para dentro se diz <i>in</i> + acusativo, <i>in oppidum</i>. Só nomes de cidades (<i>Rōmam</i>) e <i>domum</i> dispensam a preposição.'),
            ('Passo 5: monte a frase na ordem latina.', '<i>Agricolae in oppidum iērunt ut frūmentum emerent.</i> Alternativa elegante, com a finalidade à frente do verbo: <i>Agricolae frūmentī emendī causā in oppidum iērunt.</i> O verbo principal fecha a frase; a final com <i>ut</i> costuma vir depois dele (Bennett § 351.3).'),
        ]),
        pratica_guiada('Prática guiada 2 · Um parágrafo com conectivos',
            'Verta: "O general soube que os inimigos tinham atravessado o rio. Por isso reuniu os soldados e proibiu-os de sair do acampamento. Temia, pois, que os inimigos atacassem o acampamento à noite." Vocabulário: <i>dux, ducis</i> (m.), general; <i>cognōscō, -ere, cognōvī</i>, ficar sabendo; <i>trānseō, -īre, -iī</i>, atravessar; <i>flūmen, -inis</i> (n.), rio; <i>convocō, -āre</i>, reunir; <i>vetō, -āre, vetuī</i> + ac. e inf., proibir; <i>excēdō, -ere</i> + abl., sair de; <i>castra, -ōrum</i> (n. pl.), acampamento; <i>vereor, -ērī</i>, temer; <i>noctū</i>, à noite; <i>oppugnō, -āre</i>, atacar.', [
            ('Frase 1: que construção pede "soube que"?', 'Um verbo de conhecimento: oração infinitiva. "Tinham atravessado" é anterior a "soube": infinitivo perfeito <i>trānsīsse</i> (forma contraída de <i>trānsiisse</i>). <i>Dux hostēs flūmen trānsīsse cognōvit.</i> Há dois acusativos com o mesmo infinitivo, o que Bennett desaconselha por ambiguidade (§ 357.2); aqui o sentido resolve, porque um rio não atravessa inimigos. Se os dois fossem pessoas, use a passiva.'),
            ('Frase 2: como ligar à frase anterior e como dizer "reuniu… e proibiu"?', '"Por isso" narra a consequência: <i>Itaque</i>, em primeiro lugar. Em vez de dois verbos coordenados, subordine com um particípio. O ablativo absoluto <i>mīlitibus convocātīs</i> seria pouco elegante, porque os soldados são o objeto de <i>vetuit</i> (A&amp;G § 419, nota); use o particípio conjunto: <i>Itaque mīlitēs convocātōs castrīs excēdere vetuit.</i>'),
            ('Frase 3: que conectivo traduz "pois", e onde ele fica?', 'A frase explica a anterior: <i>enim</i>, na segunda posição, ou <i>nam</i>, na primeira. "Temia que…" é uma oração de temor: <i>nē</i> + subjuntivo, no imperfeito porque <i>verēbātur</i> é passado (capítulo 33). <i>Verēbātur enim nē hostēs noctū castra oppugnārent.</i>'),
            ('Leia o parágrafo inteiro e confira a coesão.', '<i>Dux hostēs flūmen trānsīsse cognōvit. Itaque mīlitēs convocātōs castrīs excēdere vetuit. Verēbātur enim nē hostēs noctū castra oppugnārent.</i> O sujeito (<i>dux</i>) é dito uma vez e continua nas frases seguintes, sem pronome (capítulo 8); cada frase começa ligada à anterior; nenhum verbo fica fora do fim da sua oração.'),
        ], 'Alternativas também corretas: <i>Nam verēbātur nē…</i>; <i>Cum dux hostēs flūmen trānsīsse cognōvisset, mīlitēs convocātōs…</i> (fundindo as duas primeiras frases num período). A versão em três frases é mais próxima do original e igualmente latina.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Escolha a construção', 'Diga que construção latina a frase pede e verta-a. Vocabulário: <i>altus, -a, -um</i>, profundo; <i>emō, -ere</i>, comprar; <i>capiō, -ere, cēpī, captum</i>, tomar; <i>fugiō, -ere, fūgī</i>, fugir; <i>habitō, -āre</i>, morar; <i>crās</i>, amanhã; <i>forum, -ī</i>, foro; <i>adveniō, -īre, advēnī</i>, chegar; <i>lēgātus, -ī</i>, embaixador.', [
            ('Os soldados disseram que o rio era profundo.', 'Oração infinitiva: <i>Mīlitēs dīxērunt flūmen altum esse.</i> O predicativo <i>altum</i> concorda com <i>flūmen</i>, neutro, no acusativo.'),
            ('O pai mandou o filho à cidade para comprar livros.', 'Finalidade: <i>Pater fīlium in urbem mīsit ut librōs emeret.</i> Alternativas: <i>quī librōs emeret</i>; <i>ad librōs emendōs</i>; <i>librōrum emendōrum causā</i>. Nunca <i>librōs emere</i>.'),
            ('Tomada a cidade, os inimigos fugiram.', 'Ablativo absoluto: <i>Urbe captā, hostēs fūgērunt.</i> A cidade não reaparece na oração principal, por isso a construção é natural.'),
            ('Devemos defender a pátria.', 'Perifrástica passiva com dativo de agente: <i>Patria nōbīs dēfendenda est.</i> Literalmente, "a pátria deve ser defendida por nós".'),
            ('Perguntei ao menino onde ele morava.', 'Interrogativa indireta, com subjuntivo e sequência secundária: <i>Puerum rogāvī ubi habitāret.</i> <i>Rogō</i> leva a pessoa no acusativo; "ele" não se traduz.'),
            ('Se você vier amanhã, veremos o foro.', 'Condicional de futuro, com futuro perfeito na prótase (capítulo 36): <i>Sī crās vēneris, forum vidēbimus.</i> O português "vier" corresponde ao latim "tiver vindo".'),
            ('Quando César chegou, os gauleses enviaram embaixadores.', '<i>Cum</i> histórico com mais-que-perfeito do subjuntivo: <i>Cum Caesar advēnisset, Gallī lēgātōs mīsērunt.</i> Alternativa: <i>Caesare adveniente</i> (ablativo absoluto, "enquanto César chegava").'),
        ]),
        exercicio('Exercício 2 · Conectivos no lugar', 'Ligue ou corrija as frases, pondo o conectivo indicado no lugar certo. Vocabulário: <i>lūdō, -ere</i>, brincar; <i>domī</i>, em casa; <i>pluit</i>, chove; <i>vincō, -ere, vīcī</i>, vencer; <i>fessus, -a, -um</i>, cansado; <i>redeō, -īre, rediī</i>, voltar; <i>pauper, -eris</i>, pobre.', [
            ('<i>Puerī lūdunt. Puellae legunt.</i> (ligue com <i>autem</i>)', '<i>Puerī lūdunt; puellae autem legunt.</i> <i>Autem</i> vem depois de <i>puellae</i> e é essa palavra que ele põe em contraste com <i>puerī</i>.'),
            ('<i>Domī manēmus. Pluit.</i> (ligue com "pois", de duas maneiras)', '<i>Domī manēmus; pluit enim.</i> ou <i>Domī manēmus; nam pluit.</i> <i>Enim</i> em segundo lugar, <i>nam</i> em primeiro.'),
            ('<i>Hostēs fugiunt. Vīcimus.</i> (ligue com "portanto")', '<i>Hostēs fugiunt; vīcimus igitur.</i> (ou <i>itaque vīcimus</i>). <i>Igitur</i> tira a conclusão e fica em segundo lugar.'),
            ('Corrija: <i>Enim mīlitēs fessī erant.</i>', '<i>Mīlitēs enim fessī erant.</i> <i>Enim</i> é pospositivo e nunca abre a frase.'),
            ('Corrija: <i>Et igitur Rōmam rediit.</i>', '<i>Igitur</i> não se combina com <i>et</i> (Bennett § 344.2). Escreva <i>Rōmam igitur rediit</i> ou <i>Itaque Rōmam rediit</i>.'),
            ('Ponha <i>tamen</i>: <i>Pauperēs erant; laetī vīvēbant.</i>', '<i>Pauperēs erant; laetī tamen vīvēbant</i> (depois da palavra enfatizada) ou <i>tamen laetī vīvēbant</i>. As duas posições são possíveis (Bennett § 343.1f).'),
        ]),
        exercicio('Exercício 3 · Desfaça os decalques', 'Cada frase latina é correta na morfologia, mas copia o português. Reescreva-a em latim idiomático e explique. Vocabulário: <i>afferō, afferre, attulī</i>, trazer.', [
            ('<i>Ille rēx ūnum servum vocāvit.</i> ("O rei chamou um servo.")', '<i>Rēx servum vocāvit.</i> Sem artigos: <i>ille</i> é "aquele" e <i>ūnus</i>, "um só". Se "um" quiser dizer "um certo", <i>servum quendam</i>.'),
            ('<i>Nūntius dīxit quod hostēs venīrent.</i> ("O mensageiro disse que os inimigos vinham.")', '<i>Nūntius dīxit hostēs venīre.</i> Fala relatada = oração infinitiva no latim clássico.'),
            ('<i>Mārcus suam mātrem amat.</i> ("Marco ama a sua mãe.")', '<i>Mārcus mātrem amat.</i> O possessivo é óbvio e sobra (Bennett § 243.1). <i>Mātrem suam</i> só com ênfase ou contraste.'),
            ('<i>Mārcus Iūliam et patrem suum vīdit.</i> ("Marco viu Júlia e o pai dela.")', '<i>Mārcus Iūliam et patrem eius vīdit.</i> <i>Suum</i> remeteria a Marco, o sujeito; o pai é de Júlia, outra pessoa: <i>eius</i>.'),
            ('<i>Librumne suum attulistī?</i> ("Você trouxe o seu livro?")', '<i>Librumne tuum attulistī?</i> O "seu" brasileiro aqui é "de você", segunda pessoa: <i>tuus</i>. (Sem ênfase, basta <i>Librumne attulistī?</i>)'),
            ('<i>Vēnit vidēre amīcum.</i> ("Veio para ver o amigo.")', '<i>Vēnit ut amīcum vidēret</i> (ou <i>ad amīcum videndum</i>; ou o supino <i>amīcum vīsum</i>). Finalidade não é infinitivo.'),
            ('<i>Imperāvit ut mīlitēs veniant.</i> ("Mandou que os soldados viessem.")', '<i>Imperāvit ut mīlitēs venīrent.</i> Verbo principal no passado → imperfeito do subjuntivo. Com <i>imperō</i>, a pessoa costuma ir no dativo: <i>Mīlitibus imperāvit ut venīrent.</i>'),
        ]),
        exercicio('Exercício 4 · Expressões idiomáticas', 'Verta usando a expressão idiomática da seção 5. Vocabulário: <i>prōditor, -ōris</i>, traidor; <i>vīsō, -ere</i>, visitar; <i>Alpēs, -ium</i> (f. pl.), Alpes; <i>adventus, -ūs</i>, chegada.', [
            ('Agradecemos aos deuses.', '<i>Deīs grātiās agimus.</i> <i>Grātiās agere</i> pede dativo da pessoa a quem se agradece.'),
            ('Os traidores foram punidos.', '<i>Prōditōrēs poenās dedērunt.</i> Ativa em latim, passiva em português: quem "dá as penas" é quem as sofre.'),
            ('Tenho a intenção de visitar Roma.', '<i>In animō habeō Rōmam vīsere.</i> <i>Rōmam</i> sem preposição, por ser nome de cidade.'),
            ('Informou o cônsul da chegada dos inimigos.', '<i>Cōnsulem dē adventū hostium certiōrem fēcit.</i> <i>Certiōrem</i> concorda com <i>cōnsulem</i>.'),
            ('Os romanos travaram batalha com os gauleses.', '<i>Rōmānī cum Gallīs proelium commīsērunt.</i>'),
            ('Dedique-se aos estudos!', '<i>Studiīs operam dā!</i> (a uma pessoa) ou <i>operam date</i> (a várias). Dativo daquilo a que se dedica.'),
        ]),
        exercicio('Exercício 5 · Retroversão graduada', 'Verta cada frase. As respostas dão um modelo e comentam as alternativas. Vocabulário: <i>discipulus, -ī</i>, aluno; <i>dīligēns, -entis</i>, diligente; <i>brevis, -e</i>, breve; <i>hortor, -ārī, hortātus sum</i>, exortar; <i>pūniō, -īre</i>, punir; <i>oppidānus, -ī</i>, habitante da cidade; <i>relinquō, -ere, relīquī</i>, abandonar; <i>obses, -idis</i>, refém; <i>concēdō, -ere, concessī</i>, conceder.', [
            ('O mestre louva os alunos diligentes.', '<i>Magister discipulōs dīligentēs laudat.</i> Ordem neutra: sujeito, objeto, verbo. <i>Dīligentēs discipulōs</i> também é possível, com ênfase no adjetivo ("os <b>diligentes</b>").'),
            ('Sabemos que a vida é breve.', '<i>Scīmus vītam brevem esse.</i> Sujeito "nós" na terminação; oração infinitiva com predicativo no acusativo.'),
            ('Os cidadãos, depois de ouvirem o cônsul, voltaram para casa.', '<i>Cīvēs, cōnsule audītō, domum rediērunt.</i> Alternativa: <i>Cīvēs, cum cōnsulem audīvissent, domum rediērunt.</i> <i>Domum</i> sem preposição. O sujeito comum (<i>cīvēs</i>) abre o período.'),
            ('O general exortou os soldados a não temerem o inimigo.', '<i>Dux mīlitēs hortātus est nē hostem timērent.</i> Pedido negativo: <i>nē</i>; imperfeito do subjuntivo depois do perfeito <i>hortātus est</i>.'),
            ('Os escravos fugiram para não serem punidos.', '<i>Servī fūgērunt nē pūnīrentur.</i> Ou, com idiomatismo: <i>nē poenās darent</i>. Finalidade negativa: <i>nē</i>, nunca <i>ut nōn</i>.'),
            ('Como a cidade não podia ser defendida, os habitantes abandonaram-na.', '<i>Oppidum, cum dēfendī nōn posset, oppidānī relīquērunt.</i> <i>Oppidum</i> é sujeito da subordinada e objeto da principal, por isso abre o período (Bennett § 351.2), e o pronome "a" desaparece. Alternativas: <i>Oppidānī oppidum, quod dēfendī nōn poterat, relīquērunt</i> (causal com <i>quod</i> e indicativo, capítulo 37).'),
            ('Os embaixadores disseram que os gauleses dariam reféns se César lhes concedesse a paz.', '<i>Lēgātī dīxērunt Gallōs obsidēs datūrōs esse, sī Caesar sibi pācem concessisset.</i> Discurso indireto (capítulo 38): a principal vai para o infinitivo futuro; a condicional, que no discurso direto teria futuro perfeito (<i>sī … concesserit</i>), passa ao mais-que-perfeito do subjuntivo (se a fala direta tivesse o futuro simples, <i>sī … concēdet</i>, o indireto teria <i>sī … concēderet</i>, também correto); "lhes" é <i>sibi</i>, reflexivo indireto, porque se refere aos que falam.'),
        ]),
        exercicio('Exercício 6 · Um parágrafo', 'Verta o parágrafo inteiro, ligando as frases. Vocabulário: <i>viātor, -ōris</i>, viajante; <i>ignōtus, -a, -um</i>, desconhecido; <i>perveniō, -īre, pervēnī</i>, chegar; <i>nox, noctis</i> (f.), noite; <i>caupōna, -ae</i>, estalagem; <i>caupō, -ōnis</i> (m.), estalajadeiro; <i>quaerō, -ere, quaesīvī</i>, procurar; <i>arbor, -oris</i> (f.), árvore; <i>dormiō, -īre</i>, dormir.', [
            ('"Um viajante chegou a uma cidade desconhecida. Como já era noite, procurou uma estalagem. O estalajadeiro, porém, disse que não havia lugar. Por isso o viajante dormiu sob uma árvore."', 'Modelo: <i>Viātor quīdam ad urbem ignōtam pervēnit. Cum iam nox esset, caupōnam quaesīvit. Caupō autem dīxit nūllum locum esse. Itaque viātor sub arbore dormīvit.</i> Comentário: <i>quīdam</i> traduz o "um" de alguém que entra na história (sem ele, <i>Viātor</i> também é correto); "como" causal-temporal com <i>cum</i> + imperfeito do subjuntivo; <i>autem</i> em segundo lugar marca a troca de sujeito para o estalajadeiro; "não havia lugar" vai em oração infinitiva (<i>nūllum locum esse</i> ou <i>locum nōn esse</i>); <i>itaque</i> abre a consequência, e o sujeito <i>viātor</i> precisa ser repetido porque o último sujeito era <i>caupō</i>. Nenhum artigo, nenhum possessivo.'),
        ]),
    ],
    leituras=['orberg-exercitia-latina-ii', 'caesar-commentarii-de-bello-gallico-selecoes', 'nepos-de-viris-illustribus-vitae', 'cicero-laelius-de-amicitia', 'bennett-new-latin-grammar', 'short-a-latin-dictionary-lewis-short'],
    leituras_nota='Os <i>Exercitia Latina II</i> de Ørberg trazem exercícios de produção em latim graduados pelos capítulos de <i>Roma Aeterna</i>. Para imitar, leia César (seleções da <i>Guerra da Gália</i>) e as vidas de Cornélio Nepos, prosa clara e de períodos bem construídos, e copie para o seu caderno as soluções que quiser reutilizar; o <i>Laelius</i> de Cícero mostra a mesma língua num registro mais cuidado. O capítulo VIII de Bennett, "Hints on Latin Style" (§§ 352–359), é uma lista curta e prática dos pontos deste capítulo. Use o Lewis &amp; Short para conferir cada palavra que tirar de um dicionário português-latim.',
)
