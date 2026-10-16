from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='17-interrogativos-e-indefinidos', titulo='Interrogativos, indefinidos e a pergunta direta',
    titulo_latim='Dē interrogātīvīs et indēfīnītīs', tempo='75 min',
    resumo='Como se pergunta em latim: o pronome quis, quid e o adjetivo quī, quae, quod; as partículas -ne, nōnne e num, que anunciam a resposta esperada; a pergunta dupla com utrum … an; os advérbios ubi, quō, unde, cūr, quandō, quōmodo; como se responde "sim" e "não" sem ter palavras para isso. Depois, os indefinidos: aliquis, quis depois de sī, nisi, num e nē, quīdam, quisque, quisquam e ūllus, nēmō e nihil. Um diálogo do Gênesis analisado palavra a palavra.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['pergunta direta', 'perguntas de palavra e de frase', 'quis, quid', 'quī, quae, quod interrogativo', 'uter', '-ne', 'nōnne', 'num', 'utrum … an', 'pergunta retórica', 'como responder sim e não', 'advérbios interrogativos', 'ubi, quō, unde', 'cūr, quandō, quōmodo', 'pronomes indefinidos', 'aliquis, aliquid', 'sī quis, nē quis, num quis', 'quīdam', 'quisque', 'quisquam e ūllus', 'nēmō e nihil', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 16: o pronome relativo <i>quī, quae, quod</i>, cujas formas o interrogativo e os indefinidos repetem, e o relativo de ligação, que aparece no texto analisado. Também o capítulo 15 (declinação pronominal; <i>nūllus</i>, <i>uter</i>).',
                       licoes=['16-o-pronome-relativo', '15-os-demonstrativos']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 57.3 (nēmō: nēminī, nēminem; genitivo e ablativo supridos por nūllīus, nūllō), § 90 (quis substantivo e quī adjetivo; 90.2 c quis homō × quī homō; 90.2 d -nam), § 91 (indefinidos; 91.1 só a parte pronominal se declina; 91.2 aliqua; 91.3 quendam, quōrundam; 91.5 sī quis; 91.7 quisquam sem plural), § 135 (aiō, ait), § 140 (quadro dos correlativos: ubi, quō, unde, quā, quandō e os demonstrativos correspondentes), § 162 (perguntas de palavra e de frase; nōnne, num, -ne; pergunta sem partícula; pergunta retórica; perguntas duplas; respostas), § 252 (quis, aliquis, quīdam, quisquam e ūllus, quisque, nēmō), § 347.2 (duas negações valem uma afirmação: nōn nūllī)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 148 (quis, quid; quī, quae, quod adjetivo: quis vocat × quī homō vocat; quid vidēs × quod templum vidēs), § 149 (indefinido quis, quī, qua; raro fora de sī, nisi, nē, num), § 151 c–g (quīdam, quisquam e ūllus, aliquis, quisque), §§ 309–314 (usos dos indefinidos; aliquis × quisquam; nēmō e nūllus), §§ 330–337 (perguntas diretas; ordem das palavras igual à da afirmação; -ne, nōnne, num; perguntas duplas; respostas: ita, etiam, vērō, sānē, minimē)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§§ 98–100 (interrogativo e indefinido; Quis venit? × Quī homō venit?; pronomes compostos; números pelo índice do OCR), §§ 322–327 (quis, aliquis, quīdam; quisquam e ūllus; quisque; uter), §§ 405–406 (perguntas simples com nōnne, num, -ne, an; perguntas alternativas com utrum … an; o número do segundo parágrafo aparece corrompido no OCR)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 72 (interrogativos com tradução portuguesa; quis e quid substantivos, quī e quod adjetivos), o número seguinte (uter, "qual dos dois?"), n. 76 (indefinidos; quis depois de sī, nisi, nē, num), n. 77 (nihil; nēmō), e a seção sobre as proposições interrogativas da sintaxe (pronomes, adjetivos e advérbios interrogativos; partículas -ne, num, nōnne, utrum, an; quandō e não cum nas perguntas), cujos números estão corrompidos no OCR', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Gn 4,9; Jo 1,19–21, 14,6 e 18,38', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Liber_Genesis', nota='frases autênticas das seções 1, 5 e 6 e do exercício 6, conferidas na Wikisource latina; ortografia adaptada (ae por æ) e macrons acrescentados, exceto nos nomes próprios hebraicos', tipo='dominio_publico'),
    ],
    objetivos=[
        'Distinguir perguntas de palavra (com <i>quis, ubi, cūr</i>…) de perguntas de frase (com <i>-ne, nōnne, num</i> ou sem partícula) e prever a resposta esperada.',
        'Declinar <i>quis, quid</i> e usar corretamente <i>quis</i> (substantivo) e <i>quī, quae, quod</i> (adjetivo) interrogativos.',
        'Traduzir os advérbios interrogativos, distinguindo <i>ubi</i>, <i>quō</i> e <i>unde</i>, que o português reúne em "onde".',
        'Reconhecer os indefinidos <i>aliquis</i>, <i>quis</i> (depois de <i>sī, nisi, num, nē</i>), <i>quīdam</i>, <i>quisque</i>, <i>quisquam</i>/<i>ūllus</i>, <i>nēmō</i> e <i>nihil</i>, e escolher entre eles pelo grau de definição e pela presença de negação.',
        'Analisar um diálogo autêntico com pergunta de palavra, relativo de ligação e <i>num</i>.',
    ],
    secoes=[
        ('Dois tipos de pergunta', f'''
<p>Toda pergunta pede uma de duas coisas. Ou pede uma <b>informação</b> que falta ("<b>quem</b> chegou?", "<b>onde</b> está o livro?", "<b>por que</b> você não trabalha?"), e então começa por uma palavra interrogativa que marca o lugar do que falta; ou pede a <b>confirmação</b> de uma frase inteira ("você vê o menino?"), e então espera um sim ou um não. As gramáticas chamam as primeiras de perguntas de palavra e as segundas de perguntas de frase (Bennett § 162).</p>
<p>O português marca a pergunta de frase só pela entoação: "você vê o menino." e "você vê o menino?" têm as mesmas palavras na mesma ordem. O latim também não muda a ordem das palavras numa pergunta (Allen e Greenough § 331), mas costuma marcá-la com uma <b>partícula</b>, que, além de anunciar a pergunta, muitas vezes diz que resposta se espera. O ponto de interrogação que você vê nos textos é obra dos editores (a escrita antiga não tinha pontuação regular); ler uma pergunta latina é, portanto, aprender a reconhecer os sinais que estão nas próprias palavras.</p>
{tabela(['Tipo', 'Sinal', 'Exemplo', 'Resposta esperada'], [
    ['Pergunta de palavra', 'pronome ou advérbio interrogativo', '<i>Quis venit?</i> Quem vem?', 'uma informação: <i>Mārcus.</i>'],
    ['Pergunta de frase neutra', '<i>-ne</i> colado à primeira palavra', '<i>Vidēs<b>ne</b> puerum?</i> Você vê o menino?', 'sim ou não'],
    ['Pergunta que espera "sim"', '<i>nōnne</i>', '<i><b>Nōnne</b> puerum vidēs?</i> Você não vê o menino?', 'sim'],
    ['Pergunta que espera "não"', '<i>num</i>', '<i><b>Num</b> puerum vidēs?</i> Por acaso você vê o menino?', 'não'],
    ['Pergunta dupla', '<i>utrum … an</i>', '<i><b>Utrum</b> puer <b>an</b> puella cantat?</i> Quem canta, o menino ou a menina?', 'uma das alternativas'],
    ['Pergunta sem partícula', 'só o tom (e o contexto)', '<i>Puerum vidēs?</i> Você vê o menino?', 'sim ou não; muitas vezes com surpresa'],
], 'Os tipos de pergunta direta', latim_cols=())}
<p>A pergunta sem partícula é mais comum do que as gramáticas escolares fazem crer, sobretudo em diálogos vivos e em expressões de surpresa ou indignação (Bennett § 162.2 d; Allen e Greenough § 332 a). No Evangelho de João, os enviados de Jerusalém interrogam João Batista assim: <i>Elias es tū? … Prophēta es tū?</i>, "Você é Elias? … Você é o profeta?" (Jo 1,21). Nada, além do contexto e da pontuação do editor, indica a pergunta.</p>
<p>Há também a <b>pergunta retórica</b>, que tem forma de pergunta mas é uma afirmação enfática: <i>Quis dubitat?</i>, "quem duvida?", isto é, "ninguém duvida" (Bennett § 162.3). O português usa o mesmo recurso, e a tradução pode conservá-lo.</p>
<h3>Sim e não</h3>
<p>O latim não tem uma palavra de uso corrente que signifique simplesmente "sim" ou "não" (Allen e Greenough § 336). Para responder que sim, repete-se o verbo ou a palavra principal da pergunta; para responder que não, repete-se com <i>nōn</i>. É exatamente o que o português faz quando responde "vejo" ou "não vejo" a "você vê?". Também se usam advérbios de reforço: para "sim", <i>ita</i> ("assim é"), <i>etiam</i>, <i>vērō</i>, <i>sānē</i> ("certamente"), <i>certē</i>; para "não", <i>nōn</i>, <i>minimē</i> ("de modo nenhum"), <i>minimē vērō</i>.</p>
{exemplos([('Estne frāter intus? — Nōn est.', 'Teu irmão está em casa? — Não está. (Bennett § 162.5 b; <i>intus</i>, dentro)'),
           ('Vidēsne puerum? — Videō.', 'Você vê o menino? — Vejo.'),
           ('Elias es tū? — Nōn sum.', 'Você é Elias? — Não sou. (Jo 1,21)')])}
'''),
        ('Quis? Quid? Quī? Quae? Quod?', f'''
<p>A pergunta de palavra precisa de um pronome que ocupe o lugar da informação que falta. O latim tem dois: um <b>substantivo</b>, <i>quis</i>, "quem?", com o neutro <i>quid</i>, "o quê?"; e um <b>adjetivo</b>, <i>quī, quae, quod</i>, "que …? qual …?", que acompanha um nome (Bennett § 90; Allen e Greenough § 148). O adjetivo declina-se exatamente como o relativo do capítulo 16. O substantivo difere do relativo só no nominativo singular e no acusativo neutro:</p>
{tabela_declinacao('quis, quid, "quem? o quê?" (singular)', [
    ('qu<b>is</b>', 'qui<b>d</b>'), ('cu<b>ius</b>', 'cu<b>ius</b>'), ('cu<b>i</b>', 'cu<b>i</b>'), ('qu<b>em</b>', 'qui<b>d</b>'), ('qu<b>ō</b>', 'qu<b>ō</b>')],
    casos=('Nominativo', 'Genitivo', 'Dativo', 'Acusativo', 'Ablativo'), colunas=('Masculino e feminino', 'Neutro'))}
<p>O plural, pouco usado, é igual ao do relativo: <i>quī, quae, quae; quōrum</i> etc. Note que <i>quis</i> não tem forma feminina própria: serve para "quem?" sem distinção de sexo. As formas oblíquas dão as perguntas que o português faz com preposição: <i>Cuius liber est?</i>, "de quem é o livro?"; <i>Cui librum dās?</i>, "a quem você dá o livro?"; <i>Quem vidēs?</i>, "quem você vê?"; <i>Quōcum ambulās?</i>, "com quem você passeia?", com o <i>cum</i> posposto, como no relativo.</p>
<p>A diferença entre os dois pronomes é a de qualquer substantivo e qualquer adjetivo. <i>Quis</i> e <i>quid</i> ficam sozinhos; <i>quī, quae, quod</i> concordam com um nome:</p>
{comparacao('Substantivo ou adjetivo interrogativo', ['Latim', 'Tradução', 'Por quê'], [
    ['<b>Quis</b> venit?', 'Quem vem?', 'sozinho: substantivo'],
    ['<b>Quī</b> homō venit?', 'Que homem vem?', 'com <i>homō</i>: adjetivo, nom. sing. m.'],
    ['<b>Quid</b> vidēs?', 'O que você vê?', 'sozinho, neutro: substantivo'],
    ['<b>Quod</b> templum vidēs?', 'Que templo você vê?', 'com <i>templum</i>: adjetivo, ac. sing. n.'],
    ['<b>Quae</b> puella cantat?', 'Que menina canta?', 'com <i>puella</i>: adjetivo, nom. sing. f.'],
    ['<b>Quem</b> librum legis?', 'Que livro você lê?', 'com <i>librum</i>: adjetivo, ac. sing. m. (igual a <i>quem</i>, "quem?")'],
])}
<p>Os exemplos das duas primeiras linhas são os mesmos de Kennedy (§ 99) e de Allen e Greenough (§ 148). Na prática, os autores misturam um pouco as duas séries: <i>quis</i> aparece como adjetivo junto de nomes de pessoa, e então há uma nuance que Bennett (§ 90.2 c) registra: <i>quis homō?</i> é "que homem? quem é esse homem?", e <i>quī homō?</i> é "que tipo de homem?". Para escrever, siga a regra: <i>quis, quid</i> sozinhos; <i>quī, quae, quod</i> com um nome.</p>
<p>O neutro <i>quid</i>, por ser substantivo, não acompanha um nome; quando quer dizer "que coisa de …", leva o nome no genitivo: <i>quid novī?</i>, "que (há de) novo?", literalmente "o que de novidade?" (Ravizza n. 72; o genitivo partitivo é estudado no capítulo 20). E, quando a pergunta escolhe entre <b>duas</b> pessoas ou coisas, usa-se <i>uter, utra, utrum</i>, "qual dos dois?", que se declina como os adjetivos pronominais do capítulo 15 (genitivo <i>utrīus</i>, dativo <i>utrī</i>): <i>Uter melior est, pater an fīlius?</i>, "qual dos dois é melhor, o pai ou o filho?" (Ravizza; <i>melior</i>, melhor, capítulo 18).</p>
{dica('<b>Interrogativo ou relativo?</b> As formas <i>quī, quae, quod, cuius, cui, quem, quam, quō</i> são idênticas nos dois. O relativo tem antecedente e está dentro de uma frase maior: <i>puer quem vidēs</i>. O interrogativo abre uma pergunta e não retoma nada: <i>Quem vidēs?</i> Se a forma está no começo de uma frase com ponto de interrogação e não há antecedente, é interrogativo; se está no começo de uma frase afirmativa e retoma algo da frase anterior, é o relativo de ligação do capítulo 16.')}
'''),
        ('-ne, nōnne, num; a pergunta dupla', f'''
<p>A pergunta de frase neutra, a que apenas pede informação, forma-se com a partícula enclítica <b><i>-ne</i></b>, colada à palavra sobre a qual recai a pergunta, que normalmente vai para o início da frase (Bennett § 162.2 c; Allen e Greenough § 332). Na maioria das vezes é o verbo: <i>Vidēsne?</i>, "você vê?"; <i>Estne frāter intus?</i>, "o irmão está dentro?". Mas pode ser qualquer palavra que se queira pôr em questão: <i>Tūne hōc dīcis?</i>, "é <b>você</b> que diz isso?".</p>
<p>Duas partículas fazem mais do que perguntar: <b>antecipam a resposta</b>. <b><i>Nōnne</i></b> (que é <i>nōn</i> + <i>-ne</i>) espera "sim", como o "não é?" português: <i>Nōnne vidēs?</i>, "você não está vendo?", isto é, "claro que está". <b><i>Num</i></b> espera "não": <i>Num dubium est?</i>, "por acaso há dúvida?", isto é, "não há, não é?" (Allen e Greenough § 332 b). Para <i>num</i>, o português tem várias soluções: "por acaso…?", "será que…?", ou uma frase afirmativa com "…, não é?" invertido: "você não está esperando isso, está?".</p>
{exemplos([('Magister<b>ne</b> puerōs docet?', 'O mestre ensina os meninos? (neutra)'),
           ('<b>Nōnne</b> magister puerōs docet?', 'O mestre não ensina os meninos? (espera: ensina, sim)'),
           ('<b>Num</b> magister puerōs docet?', 'Por acaso o mestre ensina os meninos? (espera: não ensina)'),
           ('Tū<b>ne</b> librum habēs?', 'É você que tem o livro? (<i>-ne</i> põe em questão o <i>tū</i>)')])}
<p>Quando a pergunta oferece duas ou mais alternativas, ela é <b>dupla</b> (ou alternativa): o primeiro membro começa por <i>utrum</i> ou leva <i>-ne</i>, e o segundo começa por <i>an</i>, "ou"; se o segundo é negativo, "ou não", usa-se <i>annōn</i> (Bennett § 162.4; Allen e Greenough § 335). O primeiro membro também pode ficar sem partícula. <i>Utrum</i> não se traduz: só avisa que vem uma alternativa.</p>
{exemplos([('<b>Utrum</b> puer <b>an</b> puella cantat?', 'Quem canta, o menino ou a menina?'),
           ('Puer<b>ne</b> cantat <b>an</b> puella?', 'O menino canta, ou a menina? (mesmo sentido, com <i>-ne … an</i>)'),
           ('Venitne magister <b>annōn</b>?', 'O mestre vem ou não?'),
           ('Utrum honestum est an turpe?', 'É honesto ou vergonhoso? (exemplo de Bennett § 162.4)')])}
{observacao('Três coisas que se parecem com -ne', 'O <i>-ne</i> interrogativo é breve e vem colado ao fim de uma palavra. Não o confunda com <i>nē</i>, palavra independente, de vogal longa, que é negação ("para que não", "que não"; capítulos 32 e 33) e aparece em <i>nē … quidem</i>, "nem mesmo"; nem com o enclítico <i>-que</i>, "e" (capítulo 7); nem com o fim de palavras que simplesmente terminam em <i>-ne</i>, como <i>bene</i>, "bem", ou o ablativo <i>homine</i>. A prova é tirar o <i>-ne</i>: se sobra uma palavra completa (<i>vidēs-ne</i>, <i>tū-ne</i>), é a partícula.')}
'''),
        ('Onde, para onde, de onde, quando, por que, como', f'''
<p>As perguntas sobre as circunstâncias usam advérbios interrogativos. A maioria tem a mesma raiz <i>qu-</i> do pronome, e cada um tem um correspondente demonstrativo, que dá a resposta: à pergunta <i>ubi?</i>, "onde?", responde-se <i>hīc</i>, "aqui", ou <i>ibi</i>, "ali". Bennett (§ 140) apresenta essas famílias num quadro de correlativos que vale a pena ter à mão:</p>
{tabela(['Interrogativo', 'Pergunta', 'Respostas demonstrativas', 'Observação'], [
    ['<i>ubi?</i>', 'onde? (sem movimento)', '<i>hīc</i> aqui; <i>ibi</i>, <i>illīc</i> ali', 'lugar em que se está'],
    ['<i>quō?</i>', 'para onde? aonde?', '<i>hūc</i> para cá; <i>eō</i>, <i>illūc</i> para lá', 'movimento em direção a'],
    ['<i>unde?</i>', 'de onde?', '<i>hinc</i> daqui; <i>inde</i>, <i>illinc</i> dali', 'movimento a partir de'],
    ['<i>quā?</i>', 'por onde? por que caminho?', '<i>hāc</i> por aqui; <i>eā</i>, <i>illāc</i> por ali', 'passagem'],
    ['<i>quandō?</i>', 'quando?', '<i>nunc</i> agora; <i>tum</i>, <i>tunc</i> então', 'nas perguntas, nunca <i>cum</i>'],
    ['<i>cūr?</i>', 'por quê? para quê?', '(a resposta vem em geral com <i>quia</i> ou <i>quod</i>, "porque", capítulo 37)', 'também <i>quārē?</i>, "por que razão?"'],
    ['<i>quōmodo?</i>', 'como? de que modo?', '<i>sīc</i>, <i>ita</i> assim', 'literalmente "de que modo", ablativo de <i>quī modus</i>'],
    ['<i>quam diū?</i>', 'por quanto tempo?', '<i>tam diū</i> por tanto tempo', ''],
    ['<i>quotiēns?</i>', 'quantas vezes?', '<i>totiēns</i> tantas vezes', ''],
    ['<i>quot?</i>', 'quantos?', '<i>tot</i> tantos', 'indeclinável'],
    ['<i>quantus, -a, -um?</i>', 'quão grande? quanto?', '<i>tantus</i> tão grande', 'adjetivo de primeira classe'],
    ['<i>quālis, -e?</i>', 'de que tipo? qual?', '<i>tālis</i> tal', 'adjetivo de segunda classe (capítulo 10)'],
], 'Advérbios e adjetivos interrogativos e seus correlativos', latim_cols=(0,))}
<p>A linha que mais engana o falante de português é a primeira. Em português do Brasil, "onde" serve hoje a três perguntas: "onde você está?", "onde você vai?" (por "aonde") e "de onde você vem?". O latim tem três palavras diferentes, e escolher a errada muda o sentido: <i>Ubi est pater?</i>, "onde está o pai?"; <i>Quō ambulās?</i>, "para onde você está indo?"; <i>Unde venīs?</i>, "de onde você vem?". A pergunta é sempre a mesma que você aprendeu para os casos: há movimento? para onde ou a partir de onde?</p>
<p>Duas observações. <i>Quandō</i> é a palavra para perguntar "quando?"; a conjunção <i>cum</i>, que também se traduz por "quando", introduz orações subordinadas e nunca uma pergunta (Ravizza observa isso expressamente; <i>cum</i> é o assunto do capítulo 34). E vários desses advérbios são também <b>relativos</b>: <i>locus ubi habitō</i>, "o lugar onde moro"; <i>oppidum unde venit</i>, "a cidade de onde vem". Como com o pronome, o que decide é haver ou não um antecedente.</p>
{exemplos([('<b>Ubi</b> est liber meus? — <b>Hīc</b> est.', 'Onde está o meu livro? — Está aqui.'),
           ('<b>Quō</b> ambulātis? — Ad templum.', 'Para onde vocês estão indo? — Ao templo.'),
           ('<b>Unde</b> venit nauta? — Ex oppidō.', 'De onde vem o marinheiro? — Da cidade.'),
           ('<b>Cūr</b> nōn labōrās?', 'Por que você não trabalha?'),
           ('<b>Quōmodo</b> possumus viam scīre?', 'Como podemos saber o caminho? (Jo 14,5; <i>possumus</i>, podemos, capítulo 26; <i>scīre</i>, saber)')])}
'''),
        ('Os indefinidos: alguém, um certo, cada, ninguém', f'''
<p>Os <b>pronomes indefinidos</b> indicam que se fala de alguma pessoa ou coisa sem dizer qual (Allen e Greenough § 309). Quase todos são formados a partir de <i>quis</i> ou <i>quī</i>, com um prefixo ou um sufixo, e só a parte pronominal se declina: <i>aliquis</i> faz <i>alicuius, alicui, aliquem</i>; <i>quīdam</i> faz <i>cuiusdam, cuidam</i> (Bennett § 91.1). Quem domina o relativo e o interrogativo já sabe declinar quase todos.</p>
{tabela(['Indefinido', 'Substantivo / adjetivo', 'Sentido', 'Onde aparece'], [
    ['<i>aliquis, aliquid</i> / <i>aliquī, aliqua, aliquod</i>', 'subst. / adj.', 'alguém, algo; algum', 'em frases afirmativas; o mais comum'],
    ['<i>quis, quid</i> / <i>quī, qua, quod</i>', 'subst. / adj.', 'alguém, algo; algum (fraco)', 'quase só depois de <i>sī, nisi, num, nē</i>'],
    ['<i>quīdam, quaedam, quiddam</i> (adj. <i>quoddam</i>)', 'subst. e adj.', 'um certo, uma certa', 'alguém que o falante conhece, mas não nomeia'],
    ['<i>quisque, quidque</i> / <i>quīque, quaeque, quodque</i>', 'subst. / adj.', 'cada um, cada', 'raramente no início da oração'],
    ['<i>quisquam, quidquam</i> / <i>ūllus, -a, -um</i>', 'subst. / adj.', 'alguém, algum (qualquer que seja)', 'em frases negativas, condicionais e perguntas que esperam "não"'],
    ['<i>nēmō</i> / <i>nūllus, -a, -um</i>', 'subst. / adj.', 'ninguém; nenhum', '<i>nēmō</i> só para pessoas'],
    ['<i>nihil</i> (<i>nīl</i>)', 'subst. neutro', 'nada', 'indeclinável'],
], 'Os principais indefinidos', latim_cols=(0,))}
<p><b>Aliquis</b> é o indefinido comum: <i>Aliquis portam pulsat</i>, "alguém bate à porta". Declina-se como <i>quis</i> (substantivo) e <i>quī</i> (adjetivo), mas o feminino singular e o neutro plural do adjetivo são <i>aliqua</i>, e não *<i>aliquae</i> (Bennett § 91.2): <i>aliqua puella</i>, "alguma menina".</p>
<p><b>Quis</b>, sem prefixo, também pode ser indefinido, mas é a forma mais fraca e quase só aparece depois de <i>sī</i> ("se"), <i>nisi</i> ("se não"), <i>num</i> e <i>nē</i> (Bennett § 252.1; Allen e Greenough § 310 a). As gramáticas escolares resumem: depois de <i>sī, nisi, num, nē</i>, o <i>ali-</i> cai. <i>Sī quis venit</i> é "se alguém vem", e não "se quem vem"; <i>num quis</i> é "acaso alguém?". O Evangelho de João tem um exemplo célebre: <i>Sī quis sitit, veniat ad mē et bibat</i>, "se alguém tem sede, venha a mim e beba" (Jo 7,37; <i>sitit</i>, tem sede; <i>veniat</i> e <i>bibat</i> são subjuntivos de ordem, capítulo 32).</p>
<p><b>Quīdam</b> é o mais definido dos três: designa alguém que o falante tem em mente, mas não nomeia (Bennett § 252.3): <i>homō quīdam</i>, "um certo homem". Antes do <i>d</i>, o <i>m</i> vira <i>n</i>, como em <i>eundem</i>: acusativo <i>quendam, quandam</i>, genitivo plural <i>quōrundam, quārundam</i> (Bennett § 91.3). A escala é, portanto: <i>quis</i> (o mais vago) &lt; <i>aliquis</i> &lt; <i>quīdam</i> (o mais definido) (Allen e Greenough § 310).</p>
<p><b>Quisque</b>, "cada um", raramente abre a oração; costuma vir depois de outra palavra, muitas vezes do reflexivo: <i>suum cuique</i>, "a cada um o que é seu" (Allen e Greenough § 313). Com superlativos, forma expressões como "todos os melhores", que você verá no capítulo 18.</p>
<p><b>Quisquam</b> (substantivo, sem plural) e <b>ūllus</b> (adjetivo) significam "alguém, algum, qualquer que seja" e aparecem em frases <b>negativas</b>, condicionais e perguntas que esperam "não" (Bennett § 252.4; Allen e Greenough § 311). Onde o português diz "não … ninguém" ou "nunca … a ninguém", o latim diz "nunca … a alguém": <i>Iūstitia numquam nocet cuiquam</i>, "a justiça nunca faz mal a ninguém" (Cícero, citado por Bennett e por Allen e Greenough). <i>Sine ūllō metū</i> é "sem medo algum".</p>
<p><b>Nēmō</b>, "ninguém", usa só três formas próprias: <i>nēmō, nēminī, nēminem</i>; o genitivo e o ablativo vêm de <i>nūllus</i>: <i>nūllīus, nūllō</i> (Bennett § 57.3). <i>Nūllus</i>, "nenhum", é o adjetivo correspondente, com o genitivo em <i>-īus</i> do capítulo 15. <b>Nihil</b>, "nada", é indeclinável. Lembre que em latim, como em português culto, <b>duas negações valem uma afirmação</b> (Bennett § 347.2): <i>nōn nēmō</i>, "alguém" (não ninguém); <i>nēmō nōn</i>, "todos" (ninguém deixa de); <i>nōn nihil</i>, "alguma coisa".</p>
{exemplos([('<b>Nēmō</b> venit ad Patrem, nisi per mē.', 'Ninguém vem ao Pai senão por mim. (Jo 14,6)'),
           ('<b>Quīdam</b> mīles ad oppidum venit.', 'Um certo soldado chega à cidade.'),
           ('Sī <b>quis</b> librum meum habet, <b>nihil</b> dīcit.', 'Se alguém tem o meu livro, não diz nada.'),
           ('<b>Nēminī</b> librum dō; <b>nūllīus</b> librum legō.', 'Não dou o livro a ninguém; não leio o livro de ninguém.')])}
'''),
        ('Análise gramatical: um diálogo do Gênesis', f'''
<p>Depois da morte de Abel, Deus interroga Caim. O versículo traz uma pergunta de palavra, uma resposta que começa por um relativo de ligação e uma pergunta com <i>num</i>, que espera "não":</p>
{exemplos([('Et ait Dominus ad Cain: Ubi est Abel frāter tuus? Quī respondit: Nesciō: num custōs frātris meī sum ego?', 'E o Senhor disse a Caim: Onde está teu irmão Abel? E ele respondeu: Não sei. Por acaso sou eu o guarda do meu irmão? (Gn 4,9, Vulgata Clementina)')])}
{analise('Gn 4,9, palavra a palavra', [
    ('Et', 'et (conjunção), e', 'invariável', 'liga o versículo ao anterior'),
    ('ait', 'aiō, dizer (verbo defectivo)', '3ª pessoa do singular; na narração, "disse"', 'verbo da frase introdutória'),
    ('Dominus', 'dominus, -ī (m.), senhor; na Bíblia, o Senhor', 'nominativo singular, 2ª declinação', 'sujeito de <i>ait</i>'),
    ('ad Cain', 'ad (preposição) + Cain, nome hebraico indeclinável', '<i>ad</i> com acusativo', 'a quem se fala: "a Caim"'),
    ('Ubi', 'ubi (advérbio interrogativo), onde?', 'invariável', 'abre a pergunta de palavra: lugar onde, sem movimento'),
    ('est', 'sum, esse, ser, estar', '3ª pessoa do singular do presente', 'verbo da pergunta'),
    ('Abel', 'nome hebraico indeclinável', 'aqui nominativo, pela função', 'sujeito de <i>est</i>'),
    ('frāter tuus', 'frāter, frātris (m.), irmão; tuus, -a, -um, teu', 'nominativo singular', 'aposto de <i>Abel</i>: "teu irmão"'),
    ('Quī', 'quī, quae, quod, relativo', 'nominativo singular masculino', 'relativo de ligação (capítulo 16): <i>quī</i> = <i>et is</i>, "e ele" (Caim); sujeito de <i>respondit</i>'),
    ('respondit', 'respondeō, -ēre, respondī, respōnsum, responder', '3ª pessoa do singular do perfeito (capítulo 13)', 'verbo: "respondeu"'),
    ('Nesciō', 'nesciō, -īre, não saber (prefixo negativo <i>ne-</i> + <i>sciō</i>)', '1ª pessoa do singular do presente, 4ª conjugação', 'primeira resposta: "não sei"'),
    ('num', 'num (partícula interrogativa)', 'invariável', 'abre uma pergunta que espera resposta negativa'),
    ('custōs', 'custōs, custōdis (m.), guarda, guardião', 'nominativo singular, 3ª declinação (tema <i>custōd-</i>)', 'predicativo do sujeito <i>ego</i>'),
    ('frātris meī', 'frāter, frātris; meus, -a, -um', 'genitivo singular', 'complemento de <i>custōs</i>: "do meu irmão"'),
    ('sum ego', 'sum; ego', '1ª pessoa do singular do presente; nominativo', 'verbo e sujeito; <i>ego</i> expresso e no fim da frase, com ênfase: "eu"'),
])}
<p>Repare em três coisas. A primeira pergunta é de palavra: <i>ubi</i> marca o lugar da informação que falta, e a resposta esperada seria um lugar. Caim não a dá. A segunda observação é o <i>quī</i>: nenhuma oração principal o acolhe; ele retoma <i>Cain</i>, da frase anterior, e é o relativo de ligação do capítulo 16, que se traduz "e ele" ou simplesmente "Caim". A terceira é o <i>num</i>. Caim não pergunta para saber: a partícula já fornece a resposta que ele quer ouvir, "não, você não é o guarda do seu irmão". A pergunta é uma recusa disfarçada, e a tradução "por acaso sou eu…?" conserva esse tom; uma tradução com "sou eu…?" neutro perderia o que o latim diz. O pronome <i>ego</i>, expresso e posto no fim, reforça a recusa (sobre o pronome sujeito expresso, veja o capítulo 14).</p>
{diagrama_frase([('Num', 'partícula · espera "não"'), ('custōs', 'nominativo · predicativo'), ('frātris meī', 'genitivo · "do meu irmão"'), ('sum ego', 'verbo + sujeito enfático')],
    '<i>Num custōs frātris meī sum ego?</i> = Por acaso sou eu o guarda do meu irmão? (espera-se: não)')}
<p>No Evangelho de João, Pilatos responde a Jesus com uma pergunta de palavra que se tornou proverbial e que você já pode ler sozinho: <i>Dīcit eī Pīlātus: Quid est vēritās?</i>, "Pilatos lhe diz: Que é a verdade?" (Jo 18,38). <i>Quid</i>, neutro, sozinho, é o pronome substantivo; <i>eī</i> é o dativo de <i>is</i>.</p>
<h3>Resumo</h3>
<ul>
<li>Pergunta de palavra: pronome ou advérbio interrogativo no início. Pergunta de frase: <i>-ne</i> (neutra), <i>nōnne</i> (espera "sim"), <i>num</i> (espera "não"), ou nenhuma partícula. Pergunta dupla: <i>utrum … an</i>, <i>-ne … an</i>; "ou não" = <i>annōn</i>.</li>
<li>Responde-se repetindo o verbo (com <i>nōn</i>, para negar), ou com <i>ita, etiam, vērō, sānē</i> / <i>nōn, minimē</i>.</li>
<li><i>Quis, quid</i>: substantivo ("quem? o quê?"); <i>quī, quae, quod</i>: adjetivo ("que …?"), com as formas do relativo; <i>uter</i>: "qual dos dois?".</li>
<li><i>ubi</i> onde, <i>quō</i> para onde, <i>unde</i> de onde, <i>quā</i> por onde; <i>quandō</i> quando; <i>cūr</i> por quê; <i>quōmodo</i> como.</li>
<li>Indefinidos: <i>aliquis</i> (alguém); <i>quis</i> depois de <i>sī, nisi, num, nē</i>; <i>quīdam</i> (um certo); <i>quisque</i> (cada); <i>quisquam, ūllus</i> (em frases negativas); <i>nēmō</i>, <i>nūllus</i>, <i>nihil</i>.</li>
</ul>
<p>As perguntas deste capítulo são diretas. Quando uma pergunta passa a depender de um verbo como "sei", "pergunto", "não sei" (<i>nesciō quid dīcās</i>, "não sei o que você diz"), ela se torna uma interrogativa indireta e pede o subjuntivo: é o assunto do capítulo 35.</p>
'''),
    ],
    erros_comuns=[
        ('Usar <i>quid</i> ou <i>quis</i> junto de um nome: *<i>Quid librum legis?</i> para "que livro você lê?".', 'Junto de um nome, use o adjetivo <i>quī, quae, quod</i>, concordando com ele: <i>Quem librum legis?</i> (m., ac.); <i>Quod templum vidēs?</i> (n., ac.). <i>Quid</i> fica sozinho: <i>Quid legis?</i>, "o que você lê?".'),
        ('Ler <i>num</i> como uma pergunta neutra, ou como se esperasse "sim".', '<i>Num</i> antecipa a resposta "não"; quem espera "sim" usa <i>nōnne</i>. Traduza <i>num</i> por "por acaso…?", "será que…?", e <i>nōnne</i> por "não é verdade que…?", "…, não é?". No Gênesis, <i>num custōs frātris meī sum ego?</i> é uma recusa, não uma dúvida.'),
        ('Traduzir todo "onde" por <i>ubi</i>: *<i>Ubi ambulās?</i> para "aonde você vai?".', '<i>Ubi</i> é só o lugar em que se está. Movimento para: <i>quō?</i>; movimento a partir de: <i>unde?</i>. Antes de escolher, pergunte se há movimento e em que direção, como faria com os casos (<i>in</i> + ablativo, <i>in</i> + acusativo, <i>ex</i> + ablativo).'),
        ('Ler <i>sī quis</i> como "se quem" ou <i>nē quis</i> como "que quem não".', 'Depois de <i>sī, nisi, num, nē</i>, <i>quis</i> é o indefinido, "alguém": <i>sī quis venit</i>, "se alguém vem"; <i>sī quid habēs</i>, "se você tem alguma coisa". É o <i>aliquis</i> sem o <i>ali-</i>.'),
        ('Usar <i>aliquis</i> numa frase negativa, ou somar negações à maneira do português popular: *<i>Nēmō nōn venit</i> para "ninguém não veio".', 'Em frase negativa, "alguém, qualquer" é <i>quisquam</i> ou <i>ūllus</i>: <i>numquam cuiquam nocet</i>, "nunca faz mal a ninguém". E duas negações se anulam: <i>nēmō nōn venit</i> quer dizer "todos vieram". Para "ninguém veio", basta <i>nēmō venit</i>.'),
        ('Confundir <i>-ne</i> interrogativo com <i>nē</i> ou <i>-que</i>.', '<i>-ne</i> é breve e colado ao fim da palavra (<i>vidēsne</i>); tirando-o, sobra uma palavra inteira. <i>Nē</i> é palavra separada e negativa; <i>-que</i> significa "e". Em <i>bene</i> ou <i>homine</i>, o <i>-ne</i> é parte da própria palavra.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Interrogativo e relativo lado a lado',
            'Analise e traduza: <i lang="la">Quem librum legis? Num eum quem magister tibi dat?</i>', [
            ('O primeiro <i>quem</i> é substantivo ou adjetivo?', 'Adjetivo: está junto de <i>librum</i> e concorda com ele (masculino, singular, acusativo). É o interrogativo <i>quī</i> no acusativo: "que livro?".'),
            ('Que tipo de pergunta é a primeira, e qual a resposta esperada?', 'Pergunta de palavra: espera a identificação de um livro.'),
            ('Na segunda frase, o que anuncia <i>num</i>?', 'Uma pergunta de frase que espera "não": "por acaso é aquele…?". Quem pergunta desconfia de que não seja.'),
            ('E o segundo <i>quem</i>?', 'Tem antecedente: <i>eum</i> (m. sing., ac., subentendido <i>librum</i>). É, portanto, relativo: masculino singular por causa de <i>eum</i>, acusativo por ser o objeto de <i>dat</i>. A relativa é <i>[quem magister tibi dat]</i>.'),
            ('Monte a tradução.', '"Que livro você está lendo? Por acaso aquele que o mestre lhe dá?" O verbo da segunda pergunta (<i>legis</i>) fica subentendido.'),
        ]),
        pratica_guiada('Prática guiada 2 · Três indefinidos',
            'Traduza, explicando cada indefinido: <i lang="la">Sī quis puerum vocat, puer nihil respondet; quīdam enim puerī nēminī respondent.</i> Vocabulário: <i>respondeō, -ēre</i>, responder; <i>enim</i>, pois (vem sempre depois da primeira palavra).', [
            ('Que valor tem <i>quis</i> depois de <i>sī</i>?', 'Indefinido: "alguém". <i>Sī quis puerum vocat</i>, "se alguém chama o menino". Nominativo singular, sujeito de <i>vocat</i>.'),
            ('<i>Nihil</i> e <i>nēminī</i>: que formas são?', '<i>Nihil</i>, indeclinável, é aqui o objeto de <i>respondet</i>: "não responde nada". <i>Nēminī</i> é o dativo de <i>nēmō</i>: "a ninguém".'),
            ('E <i>quīdam puerī</i>?', 'Nominativo plural masculino de <i>quīdam</i>, adjetivo concordando com <i>puerī</i>: "certos meninos", isto é, meninos de um tipo que o falante conhece.'),
            ('Monte a tradução.', '"Se alguém chama o menino, o menino não responde nada; pois certos meninos não respondem a ninguém." Note que o latim usa uma só negação em cada oração (<i>nihil</i>, <i>nēminī</i>), e o português precisa de duas ("não … nada", "não … a ninguém").'),
        ], 'Conclusão: o português nega duas vezes ("não … nada"); o latim, uma só. Ao verter, não acrescente um <i>nōn</i> a <i>nēmō</i> ou <i>nihil</i>.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Que pergunta, que resposta?', 'Diga o tipo de pergunta e a resposta esperada, e traduza.', [
            ('<i>Vidēsne puerum?</i>', 'Pergunta de frase neutra (<i>-ne</i>): "Você vê o menino?" Resposta: <i>videō</i> ou <i>nōn videō</i>.'),
            ('<i>Nōnne puerum vidēs?</i>', 'Pergunta que espera "sim": "Você não está vendo o menino?" Resposta esperada: <i>videō</i>.'),
            ('<i>Num puerum vidēs?</i>', 'Pergunta que espera "não": "Por acaso você vê o menino?" Resposta esperada: <i>nōn videō</i>.'),
            ('<i>Utrum puer an puella cantat?</i>', 'Pergunta dupla: "Quem canta, o menino ou a menina?" Resposta: uma das duas (<i>puella</i>).'),
            ('<i>Quis cantat?</i>', 'Pergunta de palavra: "Quem canta?" Resposta: um nome.'),
            ('<i>Quis dubitat?</i>', 'Pergunta retórica: "Quem duvida?" = ninguém duvida. Não espera resposta.'),
        ]),
        exercicio('Exercício 2 · Quis ou quī?', 'Complete com a forma certa de <i>quis, quid</i> ou <i>quī, quae, quod</i> e explique.', [
            ('<i>___ venit?</i> (Quem vem?)', '<i>Quis</i>: sozinho, nominativo, substantivo.'),
            ('<i>___ puella cantat?</i> (Que menina canta?)', '<i>Quae</i>: adjetivo, nom. sing. f., concordando com <i>puella</i>.'),
            ('<i>___ legis?</i> (O que você lê?)', '<i>Quid</i>: neutro, sozinho, acusativo.'),
            ('<i>___ librum legis?</i> (Que livro você lê?)', '<i>Quem</i>: adjetivo, ac. sing. m., com <i>librum</i>.'),
            ('<i>___ templum vidēs?</i> (Que templo você vê?)', '<i>Quod</i>: adjetivo, ac. sing. n., com <i>templum</i>.'),
            ('<i>___ librum dās?</i> (A quem você dá o livro?)', '<i>Cui</i>: dativo de <i>quis</i>.'),
            ('<i>___ liber est?</i> (De quem é o livro?)', '<i>Cuius</i>: genitivo de <i>quis</i>.'),
            ('<i>___ ambulās?</i> (Com quem você passeia?)', '<i>Quōcum</i>: ablativo de companhia, com <i>cum</i> posposto.'),
        ]),
        exercicio('Exercício 3 · Advérbios interrogativos', 'Traduza. Vocabulário: <i>habitō, -āre</i>, morar; <i>valeō, -ēre</i>, estar bem de saúde.', [
            ('<i>Ubi habitat poēta?</i>', '"Onde mora o poeta?" Lugar onde, sem movimento: <i>ubi</i>.'),
            ('<i>Quō ambulās?</i>', '"Para onde você está indo?" Movimento para: <i>quō</i>.'),
            ('<i>Unde venīs?</i>', '"De onde você vem?" Movimento a partir de: <i>unde</i>.'),
            ('<i>Cūr nōn labōrās?</i>', '"Por que você não trabalha?"'),
            ('<i>Quandō venit magister?</i>', '"Quando vem o mestre?" Nas perguntas, <i>quandō</i>, nunca <i>cum</i>.'),
            ('<i>Quōmodo valēs?</i>', '"Como você está (de saúde)?" <i>Quōmodo</i>, "de que modo".'),
        ]),
        exercicio('Exercício 4 · Indefinidos', 'Traduza e diga por que se usou cada indefinido. Vocabulário: <i>pulsō, -āre</i>, bater; <i>porta, -ae</i>, porta; <i>iūstitia, -ae</i>, justiça; <i>numquam</i>, nunca; <i>noceō, -ēre</i> (+ dat.), prejudicar, fazer mal a.', [
            ('<i>Aliquis portam pulsat.</i>', '"Alguém bate à porta." Frase afirmativa, pessoa indeterminada: <i>aliquis</i>.'),
            ('<i>Sī quis venit, eum videō.</i>', '"Se alguém vem, eu o vejo." Depois de <i>sī</i>, o indefinido é <i>quis</i>, sem <i>ali-</i>.'),
            ('<i>Quīdam mīles ad oppidum venit.</i>', '"Um certo soldado chega à cidade." <i>Quīdam</i>: alguém determinado, que o narrador não nomeia.'),
            ('<i>Suum cuique.</i>', '"A cada um o seu." <i>Cuique</i> é o dativo de <i>quisque</i>; o verbo ("dê-se") fica subentendido.'),
            ('<i>Iūstitia numquam nocet cuiquam.</i>', '"A justiça nunca faz mal a ninguém." Frase negativa (<i>numquam</i>): "alguém" é <i>quisquam</i>, aqui no dativo, pedido por <i>nocet</i>. O português diz "ninguém"; o latim, com uma só negação, "alguém".'),
            ('<i>Nēmō hōc scit; nihil videō.</i>', '"Ninguém sabe isto; não vejo nada." Uma negação em cada frase latina; duas em cada frase portuguesa.'),
        ]),
        exercicio('Exercício 5 · Do português para o latim', 'Verta. Vocabulário: <i>casa, -ae</i>, casa; <i>habitō, -āre</i>, morar.', [
            ('Quem você vê?', '<i>Quem vidēs?</i> Acusativo de <i>quis</i>.'),
            ('Que menino canta?', '<i>Quī puer cantat?</i> Adjetivo, nom. sing. m.'),
            ('Você não é o mestre? (espera-se "sim")', '<i>Nōnne tū magister es?</i>'),
            ('Por acaso a menina está dormindo? (espera-se "não")', '<i>Num puella dormit?</i>'),
            ('De quem é esta casa?', '<i>Cuius haec casa est?</i> Genitivo de <i>quis</i>; <i>haec</i> concorda com <i>casa</i>.'),
            ('Para onde vão os soldados?', '<i>Quō ambulant mīlitēs?</i> Movimento em direção a um lugar: <i>quō</i>, e não <i>ubi</i>.'),
            ('Ninguém mora aqui.', '<i>Nēmō hīc habitat.</i> Uma só negação; <i>hīc</i> advérbio, "aqui".'),
        ]),
        exercicio('Exercício 6 · Leitura: o interrogatório de João Batista', 'Jo 1,19 e 21, Vulgata Clementina (macrons acrescentados, exceto nos nomes próprios): <i lang="la">… ut interrogārent eum: Tū quis es? … Et interrogāvērunt eum: Quid ergō? Elias es tū? Et dīxit: Nōn sum. Prophēta es tū? Et respondit: Nōn.</i> Vocabulário: <i>ut interrogārent eum</i>, para o interrogarem (subjuntivo, capítulo 33); <i>interrogāvērunt</i>, interrogaram; <i>ergō</i>, então; <i>dīxit</i>, disse; <i>respondit</i>, respondeu; <i>prophēta, -ae</i> (m.), profeta.', [
            ('Que tipo de pergunta é <i>Tū quis es?</i>, e qual é o sujeito de <i>es</i>?', 'Pergunta de palavra, com <i>quis</i> (nominativo, predicativo). O sujeito é <i>tū</i>, expresso e posto antes do interrogativo, com ênfase: "Tu, quem és?"'),
            ('O que marca a pergunta em <i>Elias es tū?</i>', 'Nada além do contexto e da pontuação do editor: é uma pergunta de frase sem partícula, comum em diálogos vivos.'),
            ('Como João responde "não" às duas perguntas?', 'Na primeira, repetindo o verbo com negação: <i>Nōn sum</i>, "não sou"; na segunda, só com <i>nōn</i>. É o modo latino de responder, já que não há uma palavra corrente para "não".'),
            ('Que valor tem <i>quid</i> em <i>Quid ergō?</i>', 'É o interrogativo neutro, sozinho, numa pergunta elíptica: "Que (és) então?", "E então?".'),
            ('Traduza o diálogo.', '"… para o interrogarem: Tu, quem és? … E interrogaram-no: E então? Tu és Elias? E ele disse: Não sou. Tu és o profeta? E respondeu: Não."'),
        ]),
    ],
    leituras=['orberg-colloquia-personarum', 'hessus-colloquia-sive-confabulationes-tyronum-literatorum', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'roterodamus-colloquia-familiaria', 'greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc'],
    leituras_nota='Perguntas e respostas se aprendem em diálogos. Os Colloquia Personarum de Ørberg e os colóquios escolares de Hessus são conversas curtas, cheias de quis, cūr, ubi, -ne e num, boas para ler em voz alta; Familia Romana também os usa desde cedo. Na Vulgata, leia Gn 4,1–16 e Jo 1,19–28 (o interrogatório de João Batista) contando as perguntas e classificando-as. Os Colloquia Familiaria de Erasmo são o passo seguinte, já em nível intermediário. Allen e Greenough (§§ 309–315 e 330–337) explicam os indefinidos e as perguntas com muitos exemplos de Cícero.',
)
