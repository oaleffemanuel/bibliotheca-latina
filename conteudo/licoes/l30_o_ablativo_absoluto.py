from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='30-o-ablativo-absoluto', titulo='O ablativo absoluto', titulo_latim='Ablātīvus absolūtus', tempo='60 min',
    resumo='A construção mais típica da prosa narrativa latina: um nome e um particípio no ablativo, soltos do resto da frase, que resumem uma circunstância (tempo, causa, concessão, condição). Como reconhecê-la, quando ela é possível, os tipos segundo o tempo do particípio, o ablativo absoluto sem particípio (Cicerōne cōnsule) e como traduzi-la para um português natural.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['ablativo absoluto', 'particípio conjunto × ablativo absoluto', 'ablativo absoluto com particípio presente', 'ablativo absoluto com particípio perfeito', 'depoentes no ablativo absoluto', 'ablativo absoluto nominal', 'datação pelos cônsules', 'tradução do ablativo absoluto', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulos 21 e 29: os usos do ablativo (o ablativo absoluto é mais um deles) e os particípios, com a ideia de tempo relativo e o particípio conjunto, com o qual esta construção será comparada o tempo todo.',
                       licoes=['21-usos-do-acusativo-e-do-ablativo', '29-os-participios']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 227 (definição; 227.1 adjetivo ou nome em lugar do particípio: vīvō Caesare, Tarquiniō rēge; 227.2 equivalência a orações de tempo, condição, oposição, causa e circunstância; 227.4 o nome do ablativo absoluto não designa ninguém da oração principal), § 70.3 (ablativo em -e do particípio presente: Tarquiniō rēgnante), § 336 (tempo relativo do particípio), § 356.2.b (o ablativo absoluto supre a falta de particípio perfeito ativo)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 419 (definição e nota: por que "absoluto"; 419.a adjetivo ou segundo nome no lugar do particípio, inclusive a datação por cônsules), § 420 (equivalência a orações temporais, causais, concessivas, condicionais e de circunstância; conselhos de tradução), § 121.a (ablativo em -e do particípio presente no ablativo absoluto), § 493 (o perfeito passivo no ablativo absoluto substitui o perfeito ativo que falta)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 237.5 (o ablativo absoluto; equivalência a uma oração adverbial reduzida), § 72, nota 2 (no ablativo absoluto o particípio presente termina sempre em -e), § 392 (armīs abiectīs como substituto do particípio perfeito ativo)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='nn. 296–299 (definição; quando não se pode usar; tipos: nome + particípio, nome + adjetivo, dois nomes; traduções em português; depoentes intransitivos sim, transitivos não), n. 399, obs. 1 (o gerúndio português vertido por ablativo absoluto)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Mt 2,11.19; 14,15; 26,30', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Matthaeum', nota='frases autênticas da seção 6 e do exercício 6, conferidas na Wikisource latina; ortografia adaptada (i por j, ae por æ) e macrons acrescentados', tipo='dominio_publico'),
        referencia('César, Commentarii de bello Gallico 1.6 e 1.33.1', 'Caio Júlio César', catalogo='caesar-commentarii-de-bello-gallico-texto-integral', url='https://www.thelatinlibrary.com/caesar/gall1.shtml', nota='frases conferidas no texto da Latin Library e na edição de T. Rice Holmes (1914, domínio público; texto Perseus): His rebus cognitis... em 1.33.1; Omnibus rebus ad profectionem comparatis... em 1.6, subseção 3 na divisão do texto Perseus e 4 em outras edições; macrons acrescentados', tipo='dominio_publico'),
        referencia('Suetônio, De vita Caesarum, Augusto 5; Horácio, Odes 1.7.27', None, url='https://www.thelatinlibrary.com/suetonius/suet.aug.html', nota='ablativos absolutos nominais da seção 4, conferidos na Latin Library (Suetônio abrevia cōnsulibus como "conss."; aqui por extenso); Horácio em https://www.thelatinlibrary.com/horace/carm1.shtml', tipo='dominio_publico'),
    ],
    objetivos=[
        'Reconhecer um ablativo absoluto (nome ou pronome + particípio no ablativo, sem ligação gramatical com a oração principal) e distingui-lo de um ablativo regido e de um particípio conjunto.',
        'Explicar por que o ablativo absoluto só se usa quando o seu nome não é sujeito nem complemento da oração principal.',
        'Classificar o ablativo absoluto pelo tempo do particípio (simultâneo, anterior) e reconhecer o tipo nominal (<i>Cicerōne cōnsule</i>, <i>mē invītō</i>).',
        'Traduzir um ablativo absoluto de várias maneiras (particípio português, gerúndio, oração temporal, causal, concessiva, condicional, "sem que") e escolher a mais natural.',
    ],
    secoes=[
        ('O que é o ablativo absoluto', f'''
<p>No capítulo 29 você viu o particípio conjunto: um particípio que concorda com um termo da oração (<i>Puer lupum timēns fūgit</i>). Às vezes, porém, a circunstância envolve alguém ou algo que <b>não</b> aparece na oração principal. Nesse caso o latim põe o nome e o particípio no <b>ablativo</b> e os deixa soltos, sem depender de nenhuma palavra da frase:</p>
{exemplos([
    ('<b>Urbe captā</b>, hostēs discessērunt.', 'Tomada a cidade, os inimigos partiram. (lit. "a cidade tendo sido tomada")'),
    ('<b>Sōle oriente</b>, agricolae labōrāre incipiunt.', 'Ao nascer o sol, os agricultores começam a trabalhar. (<i>orior</i>, nascer; <i>incipiō</i>, começar)'),
])}
<p>É o <b>ablativo absoluto</b>. "Absoluto" vem de <i>absolūtus</i>, particípio de <i>absolvō</i>, "soltar, desligar": a expressão é gramaticalmente livre do resto da oração. Não é sujeito, não é objeto, não é regida por preposição nem por verbo. Mas não é solta quanto ao sentido: funciona como um adjunto adverbial da oração inteira, dizendo <b>em que circunstância</b> a ação principal acontece.</p>
<p>A estrutura tem sempre duas peças, que concordam entre si em gênero, número e caso, como um nome e o seu adjetivo:</p>
{tabela(['Peça', 'O que é', 'Em <i>urbe captā</i>'], [
    ['o "sujeito" da construção', 'um nome ou pronome no ablativo', '<i>urbe</i>, ablativo singular de <i>urbs</i> (f.)'],
    ['o "predicado" da construção', 'um particípio no ablativo (ou um nome ou adjetivo, seção 4)', '<i>captā</i>, ablativo singular feminino de <i>captus</i>'],
], 'As duas peças do ablativo absoluto')}
<p>Por que justamente o ablativo? As gramáticas o explicam como um desenvolvimento dos valores que você estudou no capítulo 21: o ablativo de circunstância, de tempo e de meio. "Com a cidade tomada", "no nascer do sol": o caso que já dizia "quando" e "em que condições" passou a carregar uma pequena oração inteira. Para o português, a ideia é familiar, porque nós também temos uma construção "absoluta": <b>"Terminada a aula, os alunos saíram"</b>. Esse "terminada a aula" é exatamente um ablativo absoluto, só que sem caso.</p>
'''),
        ('Quando é possível: o nome não pode estar na oração principal', f'''
<p>A regra que define a construção é simples e quase sem exceções: o nome do ablativo absoluto designa alguém ou algo <b>diferente</b> de qualquer termo da oração principal. Se a pessoa ou coisa já é sujeito ou complemento da principal, o latim usa o particípio conjunto, concordando com esse termo.</p>
{comparacao('Particípio conjunto ou ablativo absoluto?', ['Latim', 'Construção', 'Por quê'], [
    ['Hostēs <b>urbem captam</b> incendērunt.', 'particípio conjunto', 'a cidade é o objeto de <i>incendērunt</i>: o particípio concorda com ela, no acusativo'],
    ['<b>Urbe captā</b>, hostēs discessērunt.', 'ablativo absoluto', 'a cidade não é sujeito nem objeto de <i>discessērunt</i>'],
    ['<b>Caesar reversus</b> triumphum ēgit.', 'particípio conjunto', 'César é o sujeito; "tendo voltado" refere-se a ele (<i>revertor</i>, depoente)'],
    ['<b>Caesare reversō</b>, senātus gaudēbat.', 'ablativo absoluto', 'César não é termo da oração principal, cujo sujeito é o senado'],
])}
<p>Por isso uma frase como *<i>Caesare reversō, Caesar triumphum ēgit</i> está errada: César seria ao mesmo tempo solto e sujeito. Na leitura, a regra também ajuda: se você encontrou um nome e um particípio no ablativo, e o nome não tem papel nenhum na oração principal, é quase certo que seja um ablativo absoluto.</p>
<p>Há, nos autores, algumas exceções raras em que o nome do ablativo absoluto é retomado por um pronome na oração principal; as gramáticas as registram como desvios, e você não deve imitá-las ao escrever.</p>
{observacao('Como distinguir de outros ablativos', 'Nem todo nome com adjetivo no ablativo é absoluto. Em <i>Magnā vōce clāmāvit</i>, "gritou em alta voz", <i>magnā vōce</i> é um ablativo de modo (capítulo 21): o adjetivo apenas qualifica o nome. No ablativo absoluto, a segunda peça funciona como <b>predicado</b> da primeira: em <i>urbe captā</i> se afirma que a cidade foi tomada, e a tradução precisa de um verbo ou de um particípio português ("tomada a cidade"). Pergunte-se: dá para transformar o par numa oração ("a cidade foi tomada")? Se dá, é absoluto.')}
'''),
        ('Os tipos segundo o tempo do particípio', f'''
<p>O tempo do particípio continua relativo ao verbo principal, exatamente como no capítulo 29. Na prática, quase todos os ablativos absolutos usam o particípio presente ou o perfeito.</p>
<h3>Com particípio presente: ação simultânea</h3>
<p>O particípio presente indica que a circunstância se desenrola enquanto a ação principal acontece. No ablativo absoluto ele termina sempre em <b>-e</b> (<i>rēgnante</i>, <i>oriente</i>), nunca em <i>-ī</i>, porque tem valor verbal (capítulo 29, seção 2). O português traduz bem com "enquanto", "durante", "ao" + infinitivo ou com o gerúndio.</p>
{exemplos([
    ('<b>Rēge rēgnante</b>, cīvēs beātī erant.', 'Enquanto o rei reinava (durante o reinado do rei), os cidadãos eram felizes. (<i>rēgnō</i>, reinar; <i>beātus</i>, feliz)'),
    ('<b>Nūllō resistente</b>, hostēs urbem intrāvērunt.', 'Sem que ninguém resistisse, os inimigos entraram na cidade. (<i>nūllus</i>, nenhum; <i>resistō</i>, resistir)'),
])}
<h3>Com particípio perfeito: ação anterior</h3>
<p>É o tipo mais comum. O particípio perfeito, passivo, indica uma ação concluída antes da principal: <i>urbe captā</i>, "tendo sido tomada a cidade". Aqui está a grande utilidade da construção. O latim não tem particípio perfeito ativo ("tendo tomado"), e o ablativo absoluto passivo supre essa falta: em vez de "César, tendo recebido a carta", o latim diz "César, recebida a carta".</p>
{exemplos([
    ('Caesar, <b>litterīs acceptīs</b>, nūntium mīsit.', 'César, recebida a carta, enviou um mensageiro. = Depois de receber a carta, César... (<i>litterae</i>, carta; <i>nūntius</i>, mensageiro)'),
    ('<b>Hīs verbīs dictīs</b>, rēgīna discessit.', 'Ditas estas palavras, a rainha retirou-se. = Depois de dizer isso, a rainha...'),
])}
<p>Note que, no primeiro exemplo, quem recebeu a carta foi César, embora a gramática não o diga: <i>litterīs acceptīs</i> só afirma que a carta foi recebida. O contexto quase sempre deixa claro que o agente é o sujeito da principal, e então a tradução portuguesa pode passar para a voz ativa: "tendo recebido a carta". Essa é a tradução mais natural na maioria dos casos, desde que o contexto a autorize.</p>
<h3>Com depoentes</h3>
<p>Como o particípio perfeito dos depoentes é ativo, ele só pode entrar no ablativo absoluto quando o verbo é <b>intransitivo</b>: <i>rēge mortuō</i>, "morto o rei"; <i>sōle ortō</i>, "nascido o sol"; <i>Valeriō profectō</i>, "tendo partido Valério". Um depoente transitivo, como <i>hortor</i>, não serve: "tendo exortado os soldados" não é *<i>mīlitibus hortātīs</i>, que significaria "os soldados tendo exortado"; diz-se com particípio conjunto, <i>Dux mīlitēs hortātus signum dedit</i>.</p>
<h3>Com particípio futuro</h3>
<p>Raro e tardio: aparece sobretudo a partir de Tito Lívio, para indicar intenção ou iminência. Basta reconhecê-lo quando surgir.</p>
{tabela(['Particípio', 'Relação com o verbo principal', 'Exemplo', 'Tradução típica'], [
    ['presente (abl. em <i>-e</i>)', 'simultânea', '<i>rēge rēgnante</i>', 'enquanto o rei reinava; no reinado do rei'],
    ['perfeito (passivo)', 'anterior', '<i>urbe captā</i>', 'tomada a cidade; depois que a cidade foi tomada'],
    ['perfeito de depoente intransitivo', 'anterior', '<i>rēge mortuō</i>', 'morto o rei; depois que o rei morreu'],
    ['futuro (raro, Lívio em diante)', 'posterior', '—', 'estando para...; com a intenção de...'],
], 'Tipos de ablativo absoluto', latim_cols=(2,))}
'''),
        ('O ablativo absoluto sem particípio', f'''
<p>O verbo <i>esse</i> não tem particípio presente. Por isso, quando a circunstância é "sendo X cônsul", "sendo eu menino", "estando César vivo", o latim simplesmente omite o particípio e põe no ablativo os dois nomes, ou o nome e um adjetivo. É o <b>ablativo absoluto nominal</b>, e o português quase nunca o traduz palavra por palavra.</p>
{tabela(['Latim', 'Literal', 'Tradução natural'], [
    ['<i>Cicerōne cōnsule</i>', 'sendo Cícero cônsul', 'no consulado de Cícero'],
    ['<i>Hannibale duce</i>', 'sendo Aníbal o comandante', 'sob o comando de Aníbal'],
    ['<i>mē puerō</i>', 'sendo eu menino', 'quando eu era menino'],
    ['<i>mē invītō</i>', 'sendo eu contrário', 'contra a minha vontade (<i>invītus</i>, que não quer)'],
    ['<i>vīvō patre</i>', 'estando o pai vivo', 'em vida do pai, enquanto o pai vivia'],
    ['<i>caelō serēnō</i>', 'estando o céu limpo', 'com céu limpo (<i>serēnus</i>, sereno)'],
], 'Ablativos absolutos nominais', latim_cols=(0,))}
<p>O uso mais importante deste tipo é a <b>datação</b>. Os romanos contavam os anos pelos dois cônsules em exercício, e a fórmula é um ablativo absoluto com <i>cōnsulibus</i>. Suetônio data assim o nascimento de Augusto (63 a.C.):</p>
{exemplos([('Nātus est Augustus M. Tulliō Cicerōne C. Antōniō cōnsulibus.', 'Augusto nasceu no consulado de Marco Túlio Cícero e Caio Antônio. (Suetônio, <i>Aug.</i> 5; lit. "sendo cônsules Marco Túlio Cícero e Caio Antônio")')])}
<p>E Horácio põe na boca do herói Teucro, que parte para o exílio, um verso que se tornou proverbial; ele contém dois ablativos absolutos nominais coordenados:</p>
{exemplos([('Nīl dēspērandum Teucrō duce et auspice Teucrō.', 'Não há por que desesperar, sendo Teucro o guia e Teucro o áugure. (Horácio, <i>Odes</i> 1.7.27; <i>auspex</i>, quem toma os auspícios, protetor)')])}
<p>A forma <i>dēspērandum</i>, "deve-se desesperar", é um gerundivo, assunto do capítulo 31; aqui importa o par <i>Teucrō duce</i>, "sendo Teucro o guia", com a sua repetição em ordem inversa, <i>auspice Teucrō</i>.</p>
'''),
        ('Como traduzir', f'''
<p>O ablativo absoluto, como o particípio conjunto, deixa a relação lógica implícita. As gramáticas o comparam a uma oração subordinada reduzida, que pode ser temporal, causal, concessiva, condicional ou de simples circunstância. A tradução depende do contexto, mas há um procedimento seguro.</p>
<ol>
<li><b>Isole o ablativo absoluto</b> e leia a oração principal sem ele: ela deve ficar completa.</li>
<li><b>Transforme o par numa oração</b>, com o tempo certo: presente → simultâneo ("enquanto o rei reinava"); perfeito → anterior e passivo ("a cidade tinha sido tomada").</li>
<li><b>Pergunte a relação</b> com a principal: tempo? causa? oposição? condição? acompanhamento?</li>
<li><b>Escolha a forma portuguesa</b> mais natural e, se o agente é obviamente o sujeito da principal, passe para a ativa.</li>
</ol>
{tabela(['Relação', 'Português', 'Exemplo'], [
    ['nenhuma marcada', 'particípio absoluto português', '<i>Urbe captā, hostēs discessērunt.</i> Tomada a cidade, os inimigos partiram.'],
    ['tempo', 'quando, depois que, enquanto, ao + infinitivo', 'Depois que a cidade foi tomada, os inimigos partiram.'],
    ['causa', 'como, porque, visto que', '<i>Duce occīsō, mīlitēs fūgērunt.</i> Como o comandante tinha sido morto, os soldados fugiram.'],
    ['concessão', 'embora, apesar de', '<i>Omnibus rēbus āmissīs, virtūs tamen manet.</i> Embora tudo se tenha perdido, a virtude permanece.'],
    ['condição', 'se', '<i>Deō iuvante, omnia bene ēvenient.</i> Se Deus ajudar, tudo correrá bem.'],
    ['negação com <i>nūllō</i>, <i>nōn</i>', 'sem que, sem', '<i>Nūllō resistente...</i> Sem que ninguém resistisse...'],
    ['agente = sujeito', 'tendo + particípio (ativa)', '<i>Caesar, litterīs acceptīs...</i> César, tendo recebido a carta...'],
], 'Repertório de traduções do ablativo absoluto')}
<p>Vocabulário dos exemplos da tabela: <i>occīdō, occīsum</i>, matar; <i>āmittō, āmissum</i>, perder; <i>iuvō</i>, ajudar; <i>ēveniō</i>, acontecer, sair (bem ou mal). Evite o decalque "a cidade tendo sido tomada": é compreensível, mas não é português corrente. O particípio absoluto português ("tomada a cidade") ou uma oração com conjunção soam muito melhor.</p>
{dica('<b>Leia o ablativo absoluto como um parêntese.</b> Na prosa de César e de Tito Lívio é comum uma frase abrir com dois ou três ablativos absolutos seguidos, que resumem o que aconteceu antes, e só depois vir o sujeito e o verbo. Marque cada par (nome + particípio no ablativo) entre colchetes antes de traduzir; a oração principal aparece sozinha.')}
'''),
        ('Análise gramatical: frases autênticas', f'''
<p>O Evangelho de Mateus usa o ablativo absoluto para marcar a passagem de um episódio a outro. Depois da fuga para o Egito, a narrativa recomeça assim:</p>
{exemplos([('Dēfūnctō autem Hērōde, ecce angelus Dominī appāruit in somnīs Ioseph in Aegyptō.', 'Morto, porém, Herodes, eis que o anjo do Senhor apareceu em sonho a José, no Egito. (Mt 2,19, Vulgata Clementina)')])}
{analise('Mt 2,19, palavra a palavra', [
    ('Dēfūnctō', 'dēfungor, dēfungī, dēfūnctus sum, cumprir até o fim; morrer', 'particípio perfeito de depoente intransitivo, ablativo singular masculino', 'predicado do ablativo absoluto: "tendo morrido"'),
    ('autem', 'autem (conjunção)', 'invariável, sempre em segunda posição', '"porém, ora": liga ao episódio anterior'),
    ('Hērōde', 'Hērōdēs, -is (m.), Herodes', 'ablativo singular, 3ª declinação', '"sujeito" do ablativo absoluto; Herodes não é termo da oração principal'),
    ('ecce', 'ecce (interjeição)', 'invariável', '"eis que": chama a atenção para o que vem'),
    ('angelus', 'angelus, -ī (m.), anjo', 'nominativo singular', 'sujeito de <i>appāruit</i>'),
    ('Dominī', 'dominus, -ī (m.), senhor', 'genitivo singular', 'adjunto de <i>angelus</i>: "do Senhor"'),
    ('appāruit', 'appāreō, appārēre, appāruī, aparecer', 'perfeito do indicativo, 3ª pessoa do singular', 'verbo principal'),
    ('in somnīs', 'somnus, -ī (m.), sono', '<i>in</i> + ablativo plural', 'circunstância: "em sonho, durante o sono"'),
    ('Ioseph', 'Ioseph (m.), José', 'indeclinável; aqui dativo pelo sentido', 'a quem aparece: "a José"'),
    ('in Aegyptō', 'Aegyptus, -ī (f.), Egito', '<i>in</i> + ablativo singular', 'lugar onde'),
])}
<p>Três pontos. <i>Dēfūnctō Hērōde</i> está no ablativo e nada na frase o rege: nem preposição, nem verbo. Herodes não volta na oração principal, cujo sujeito é o anjo: é a condição para o ablativo absoluto. E o particípio é de um depoente intransitivo, o único tipo de depoente que cabe nesta construção (seção 3). A relação com a principal é de tempo: "depois que Herodes morreu".</p>
{exemplos([('Et hymnō dictō, exiērunt in montem Olīvētī.', 'E, dito o hino, saíram para o monte das Oliveiras. (Mt 26,30; <i>hymnus</i>, hino; <i>exeō, exiī</i>, sair; <i>Olīvētum</i>, olival)')])}
<p>Aqui o particípio é passivo, <i>dictō</i>, "tendo sido dito", e o agente (Jesus e os discípulos) é o próprio sujeito de <i>exiērunt</i>: em bom português, "depois de cantarem o hino, saíram". César usa o mesmo recurso a cada página:</p>
{exemplos([('Hīs rēbus cognitīs Caesar Gallōrum animōs verbīs cōnfirmāvit.', 'Conhecidos esses fatos, César animou os gauleses com palavras. = Tendo tomado conhecimento disso, César... (César, <i>BG</i> 1.33.1; a frase continua)')])}
{diagrama_frase([('Hīs rēbus cognitīs', 'ablativo absoluto · circunstância anterior'), ('Caesar', 'nominativo · sujeito'), ('Gallōrum animōs', 'genitivo + acusativo · objeto'), ('verbīs', 'ablativo de meio · "com palavras"'), ('cōnfirmāvit', 'verbo principal · "fortaleceu"')],
    'O ablativo absoluto fica fora do esqueleto da oração: <i>Caesar animōs cōnfirmāvit</i> é a oração completa.')}
<p>O par <i>hīs rēbus cognitīs</i> está no ablativo plural feminino (<i>rēs</i>, 5ª declinação; <i>hīs</i>, de <i>hīc</i>; <i>cognitīs</i>, de <i>cognōscō, cognōvī, cognitum</i>). Ao lado dele há outro ablativo, <i>verbīs</i>, que não é absoluto: é o meio de <i>cōnfirmāvit</i> e não tem predicado. Comparar os dois na mesma frase é o melhor treino para a distinção da seção 2.</p>
<h3>Resumo</h3>
<ul>
<li><b>Forma</b>: nome ou pronome + particípio (ou nome, ou adjetivo) no ablativo, concordando entre si.</li>
<li><b>Condição</b>: o nome não é sujeito nem complemento da oração principal; se for, usa-se o particípio conjunto.</li>
<li><b>Tempo</b>: presente (em <i>-e</i>) = simultâneo; perfeito = anterior e passivo (supre o perfeito ativo que falta); depoentes só se intransitivos.</li>
<li><b>Nominal</b>: <i>Cicerōne cōnsule</i>, <i>mē invītō</i>, <i>mē puerō</i>; datação pelos cônsules.</li>
<li><b>Tradução</b>: particípio absoluto português, temporal, causal, concessiva, condicional, "sem que", ou ativa com "tendo".</li>
</ul>
<p>O capítulo 31 apresenta o gerúndio, o gerundivo e o supino; o capítulo 34 mostra a outra grande maneira de exprimir circunstâncias, as orações com <i>cum</i>, que muitas vezes alternam com o ablativo absoluto no mesmo autor.</p>
'''),
    ],
    erros_comuns=[
        ('Procurar um verbo ou preposição que "reja" o ablativo absoluto, e traduzi-lo como complemento: <i>urbe captā hostēs discessērunt</i> → *"os inimigos partiram da cidade tomada".', 'O ablativo absoluto não depende de nada. Se não há preposição nem verbo que peça ablativo, e o par tem um particípio que funciona como predicado, leia-o como uma oração à parte: "tomada a cidade, os inimigos partiram".'),
        ('Traduzir o particípio perfeito do ablativo absoluto como ativo do seu próprio nome: <i>Caesar, litterīs acceptīs</i> → *"César, tendo as cartas recebido".', 'O particípio concorda com o nome do ablativo absoluto (<i>litterīs acceptīs</i>, "as cartas recebidas"), não com o sujeito. Quem recebeu não está dito; o contexto mostra que foi César, e só então a tradução pode virar ativa: "tendo recebido a carta".'),
        ('Ao escrever em latim, usar o ablativo absoluto para um nome que já é sujeito ou objeto: *<i>Caesare reversō, Caesar triumphum ēgit</i>.', 'Se a pessoa ou coisa é termo da oração principal, use o particípio conjunto: <i>Caesar reversus triumphum ēgit</i>; <i>Hostēs urbem captam incendērunt</i>. O ablativo absoluto é para quem está de fora.'),
        ('Pôr um depoente transitivo no ablativo absoluto: *<i>mīlitibus hortātīs</i> para "tendo exortado os soldados".', 'O perfeito do depoente é ativo; <i>mīlitibus hortātīs</i> diria "os soldados tendo exortado". Com depoentes transitivos use o particípio conjunto ao sujeito: <i>Dux mīlitēs hortātus...</i>. Só os depoentes intransitivos cabem no ablativo absoluto (<i>rēge mortuō</i>, <i>sōle ortō</i>).'),
        ('Confundir o ablativo absoluto com um ablativo de modo ou de meio acompanhado de adjetivo: <i>magnā vōce clāmāvit</i> → *"sendo grande a voz, gritou".', 'Um adjetivo atributivo não faz ablativo absoluto. Teste: dá para dizer "a voz foi grande" como uma afirmação separada? Não; "em voz alta" é o modo de gritar. Já <i>urbe captā</i> afirma algo (a cidade foi tomada).'),
        ('Traduzir o ablativo absoluto nominal palavra por palavra: <i>Cicerōne cōnsule</i> → *"Cícero cônsul", <i>mē invītō</i> → *"eu contrariado".', 'Falta um verbo em português: o latim omite o particípio de <i>esse</i>, que não existe. Diga "no consulado de Cícero", "sendo Cícero cônsul", "contra a minha vontade".'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Do latim para um português natural',
            'Analise e traduza: <i lang="la">Rēge mortuō, cīvēs novum rēgem creāvērunt.</i> Vocabulário: <i>rēx, rēgis</i> (m.), rei; <i>morior, morī, mortuus sum</i>, morrer; <i>cīvis, cīvis</i> (m.), cidadão; <i>novus</i>, novo; <i>creō</i>, eleger, nomear.', [
            ('Qual é a oração principal, e ela está completa?', '<i>Cīvēs novum rēgem creāvērunt</i>: sujeito <i>cīvēs</i> (nom. pl.), objeto <i>novum rēgem</i> (ac. sing.), verbo <i>creāvērunt</i>. "Os cidadãos elegeram um novo rei." Está completa.'),
            ('Que caso é <i>rēge mortuō</i>, e o que o rege?', 'Ablativo singular masculino: <i>rēge</i> (3ª declinação) e <i>mortuō</i> (como <i>bonus</i>). Nada o rege: não há preposição, e <i>creāvērunt</i> não pede ablativo.'),
            ('O rei morto é termo da oração principal?', 'Não: o rei da principal é outro (<i>novum rēgem</i>); o morto não é sujeito nem objeto. Logo é um ablativo absoluto, e não um particípio conjunto.'),
            ('Que tempo e que voz exprime <i>mortuō</i>?', 'Particípio perfeito do depoente intransitivo <i>morior</i>: sentido ativo e anterior, "tendo morrido". Por ser intransitivo, pode entrar no ablativo absoluto.'),
            ('Que relação lógica liga as duas partes?', 'Tempo (e, pelo sentido, causa): a eleição veio depois da morte, e por causa dela.'),
            ('Dê duas traduções.', '"Morto o rei, os cidadãos elegeram um novo rei." / "Depois que o rei morreu, os cidadãos elegeram um novo." A segunda evita repetir "rei".'),
        ]),
        pratica_guiada('Prática guiada 2 · Juntar duas orações numa só',
            'Junte cada par numa única frase, usando particípio conjunto ou ablativo absoluto, e explique a escolha. Vocabulário: <i>mūrus</i>, muro; <i>dēleō, dēlēvī, dēlētum</i>, destruir; <i>mīles, mīlitis</i>, soldado; <i>intrō</i>, entrar; <i>capiō, cēpī, captum</i>, capturar; <i>dux, ducis</i>, comandante; <i>interficiō, interfēcī, interfectum</i>, matar.', [
            ('<i>Mūrī dēlētī sunt. Mīlitēs urbem intrāvērunt.</i>', 'Os muros não aparecem na segunda oração: ablativo absoluto. <i>Mūrīs dēlētīs, mīlitēs urbem intrāvērunt.</i> "Destruídos os muros, os soldados entraram na cidade."'),
            ('<i>Dux captus est. Mīlitēs ducem interfēcērunt.</i>', 'O comandante é o objeto da segunda oração (<i>ducem</i>): particípio conjunto no acusativo. <i>Mīlitēs ducem captum interfēcērunt.</i> "Os soldados mataram o comandante capturado" (ou "capturaram o comandante e o mataram"). *<i>Duce captō, mīlitēs ducem interfēcērunt</i> seria errado.'),
            ('<i>Sōl oriēbātur. Nautae nāvigāre incipiunt.</i> (<i>orior</i>, nascer; <i>nāvigō</i>, navegar; <i>incipiō</i>, começar)', 'O sol não é termo da principal, e as ações são simultâneas: ablativo absoluto com particípio presente, em <i>-e</i>. <i>Sōle oriente, nautae nāvigāre incipiunt.</i> "Ao nascer do sol, os marinheiros começam a navegar."'),
        ], 'Conclusão: a escolha não depende do sentido, mas da gramática: o nome está ou não está na oração principal?'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Absoluto ou não?', 'Diga se o trecho em destaque é um ablativo absoluto, um particípio conjunto ou outro tipo de ablativo, e justifique. Vocabulário: <i>gladius</i>, espada; <i>pugnō</i>, lutar; <i>vincō, vīcī, victum</i>, vencer; <i>gaudeō</i>, alegrar-se; <i>clāmor, -ōris</i>, grito.', [
            ('<i>Mīlitēs <b>gladiīs</b> pugnābant.</i>', 'Ablativo de meio (capítulo 21): não há particípio nem predicado; "lutavam com espadas".'),
            ('<i><b>Hostibus victīs</b>, Rōmānī gaudēbant.</i>', 'Ablativo absoluto: nome + particípio perfeito no ablativo; os inimigos não são termo da principal. "Vencidos os inimigos, os romanos se alegravam."'),
            ('<i>Rōmānī <b>hostēs victōs</b> in urbem dūxērunt.</i>', 'Particípio conjunto no acusativo: os inimigos são o objeto de <i>dūxērunt</i>. "Os romanos levaram para a cidade os inimigos vencidos."'),
            ('<i><b>Magnō clāmōre</b> mīlitēs urbem intrāvērunt.</i>', 'Ablativo de modo, com adjetivo atributivo: "com grande gritaria". Não afirma nada sobre o grito; não é absoluto.'),
            ('<i><b>Patre absente</b>, fīlius vīllam cūrābat.</i> (<i>absum</i>, estar ausente; <i>cūrō</i>, cuidar)', 'Ablativo absoluto com particípio presente de <i>absum</i> (<i>absēns, absentis</i>), em <i>-e</i>: "Na ausência do pai, o filho cuidava da casa."'),
        ]),
        exercicio('Exercício 2 · Traduza escolhendo a relação', 'Traduza para um português natural e diga que relação lógica você escolheu. Vocabulário: <i>bellum</i>, guerra; <i>cōnficiō, cōnfēcī, cōnfectum</i>, terminar; <i>domum</i>, para casa; <i>redeō, rediī</i>, voltar; <i>auxilium</i>, ajuda; <i>mittō, mīsī, missum</i>, enviar; <i>perīculum</i>, perigo; <i>maneō</i>, permanecer; <i>vīlla</i>, casa de campo; <i>dormiō</i>, dormir; <i>fūr, fūris</i>, ladrão.', [
            ('<i>Bellō cōnfectō, mīlitēs domum rediērunt.</i>', 'Tempo: "Terminada a guerra (depois que a guerra terminou), os soldados voltaram para casa."'),
            ('<i>Auxiliō nōn missō, oppidum captum est.</i> (<i>oppidum</i>, cidade fortificada)', 'Causa: "Como não foi enviada ajuda, a cidade foi tomada." Também possível: "Sem que se enviasse ajuda".'),
            ('<i>Perīculō cognitō, fēmina tamen in vīllā mānsit.</i> (<i>cognōscō, cognitum</i>, conhecer)', 'Concessão, marcada por <i>tamen</i>: "Embora conhecesse o perigo, a mulher permaneceu na casa de campo." O agente de <i>cognitō</i> é a própria mulher: tradução ativa.'),
            ('<i>Dominō dormiente, fūr vīllam intrāvit.</i>', 'Tempo (simultaneidade): "Enquanto o senhor dormia, o ladrão entrou na casa." Particípio presente em <i>-e</i>.'),
            ('<i>Deō iuvante, nihil timēbimus.</i> (<i>iuvō</i>, ajudar; <i>nihil</i>, nada)', 'Condição: "Se Deus nos ajudar, nada temeremos." Com futuro na principal, o particípio presente toma valor condicional.'),
        ]),
        exercicio('Exercício 3 · O ablativo absoluto nominal', 'Traduza. Vocabulário: <i>cōnsul, -is</i>, cônsul; <i>imperātor, -ōris</i>, general; <i>invītus</i>, que não quer; <i>senex, senis</i>, velho; <i>puer</i>, menino.', [
            ('<i>Pompeiō et Crassō cōnsulibus</i>', '"No consulado de Pompeu e Crasso" (lit. "sendo cônsules Pompeu e Crasso"). Fórmula de datação.'),
            ('<i>Hannibale imperātōre, Poenī multa proelia vīcērunt.</i> (<i>Poenī</i>, cartagineses; <i>proelium</i>, batalha; <i>vincō, vīcī</i>, vencer)', '"Sob o comando de Aníbal, os cartagineses venceram muitas batalhas." <i>Hannibale imperātōre</i> = "sendo Aníbal general".'),
            ('<i>Mē invītō discessistī.</i>', '"Partiste contra a minha vontade." <i>Invītō</i> é adjetivo concordando com <i>mē</i> (ablativo).'),
            ('<i>Patre sene, fīliī agrōs colēbant.</i> (<i>colō</i>, cultivar)', '"Como o pai era velho (estando o pai velho), os filhos cultivavam os campos." Causa ou tempo, conforme o contexto; o substantivo <i>senex</i> faz o papel de predicado.'),
        ]),
        exercicio('Exercício 4 · Transforme', 'Reescreva a oração entre colchetes como ablativo absoluto ou como particípio conjunto, conforme a regra da seção 2, e traduza o resultado.', [
            ('[<i>Epistula scrīpta est.</i>] <i>Puella epistulam mīsit.</i>', 'A carta é objeto de <i>mīsit</i>: particípio conjunto. <i>Puella epistulam scrīptam mīsit.</i> "A menina enviou a carta escrita" = "escreveu a carta e a enviou".'),
            ('[<i>Epistula scrīpta est.</i>] <i>Puella dormīvit.</i>', 'A carta não está na principal: ablativo absoluto. <i>Epistulā scrīptā, puella dormīvit.</i> "Escrita a carta, a menina dormiu."'),
            ('[<i>Imperātor clāmābat.</i>] <i>Mīlitēs fūgērunt.</i>', 'O general não está na principal; ação simultânea: <i>Imperātōre clāmante, mīlitēs fūgērunt.</i> "Enquanto o general gritava, os soldados fugiram."'),
            ('[<i>Imperātor clāmābat.</i>] <i>Mīlitēs imperātōrem audīvērunt.</i>', 'O general é objeto de <i>audīvērunt</i>: particípio conjunto no acusativo, com verbo de percepção. <i>Mīlitēs imperātōrem clāmantem audīvērunt.</i> "Os soldados ouviram o general gritando."'),
        ]),
        exercicio('Exercício 5 · Do português para o latim', 'Traduza usando um ablativo absoluto. Vocabulário: <i>porta, -ae</i>, porta; <i>aperiō, aperuī, apertum</i>, abrir; <i>hostis, -is</i>, inimigo; <i>irrumpō, irrūpī</i>, irromper; <i>nāvis, -is</i>, navio; <i>parō</i>, preparar; <i>nauta</i>, marinheiro; <i>discēdō, discessī</i>, partir; <i>Caesar, -aris</i>; <i>cōnsul, -is</i>.', [
            ('Abertas as portas, os inimigos irromperam.', '<i>Portīs apertīs, hostēs irrūpērunt.</i> Ablativo plural feminino; as portas não são termo da principal.'),
            ('Depois que os navios foram preparados, os marinheiros partiram.', '<i>Nāvibus parātīs, nautae discessērunt.</i> A oração temporal vira ablativo absoluto com particípio perfeito: anterioridade.'),
            ('No consulado de César, Roma estava em perigo.', '<i>Caesare cōnsule, Rōma in perīculō erat.</i> Ablativo absoluto nominal: falta o particípio de <i>esse</i>.'),
            ('Enquanto os cidadãos dormiam, o fogo destruiu a casa.', '<i>Cīvibus dormientibus, ignis domum dēlēvit.</i> (<i>ignis</i>, fogo.) Particípio presente, simultâneo; no plural o ablativo é <i>-ibus</i>, sem a questão <i>-e/-ī</i>.'),
        ]),
        exercicio('Exercício 6 · Leitura autêntica', 'Identifique os ablativos absolutos e traduza. Vocabulário: <i>aperiō, apertum</i>, abrir; <i>thēsaurus</i>, cofre, tesouro; <i>offerō, obtulī</i>, oferecer; <i>mūnus, -eris</i>, presente; <i>vesper, -erī</i> ou <i>-eris</i> (m.), tarde; <i>accēdō, accessī</i>, aproximar-se; <i>discipulus</i>, discípulo; <i>profectiō, -ōnis</i>, partida; <i>comparō</i>, preparar; <i>diem dīcere</i>, marcar o dia.', [
            ('<i>Et apertīs thēsaurīs suīs obtulērunt eī mūnera.</i> (Mt 2,11)', '<i>Apertīs thēsaurīs suīs</i>: ablativo absoluto com particípio perfeito passivo; quem abriu foram os magos, sujeito de <i>obtulērunt</i> (<i>suīs</i> remete a eles). "E, abrindo os seus cofres, ofereceram-lhe presentes."'),
            ('<i>Vespere autem factō, accessērunt ad eum discipulī eius.</i> (Mt 14,15)', '<i>Vespere factō</i>: ablativo absoluto, "feita a tarde", isto é, "ao cair da tarde". <i>Factō</i> é o particípio perfeito de <i>faciō</i>, que também serve de perfeito a <i>fīō</i> (capítulo 26): "feito, acontecido". "Ao cair da tarde, os seus discípulos aproximaram-se dele."'),
            ('<i>Omnibus rēbus ad profectiōnem comparātīs diem dīcunt.</i> (César, <i>BG</i> 1.6; a frase continua)', '<i>Omnibus rēbus ... comparātīs</i>: ablativo absoluto; <i>ad profectiōnem</i> está encaixado no meio dele. O sujeito de <i>dīcunt</i> são os helvécios. "Preparado tudo para a partida, marcam o dia." Note o presente histórico, comum em César.'),
        ]),
    ],
    leituras=['collar-the-gate-to-caesar-de-bello-gallico-ii-simplificado-e-original', 'lhomond-urbis-romae-viri-illustres-selecoes', 'eutropius-breviarium-ab-urbe-condita', 'caesar-commentarii-de-bello-gallico-selecoes', 'vulgata-biblia-sacra-vulgata-editio-clementina'],
    leituras_nota='O ablativo absoluto é a marca da prosa histórica. Comece pelo <i>De viris illustribus</i> de Lhomond, em que quase toda biografia tem um <i>rēge mortuō</i> ou <i>urbe captā</i>, e pelo <i>Breviarium</i> de Eutrópio. <i>The Gate to Caesar</i> põe lado a lado o texto simplificado e o original do livro II da <i>Guerra da Gália</i>, ótimo para ver ablativos absolutos em série; depois passe às seleções de César. Na Vulgata, procure-os em Mateus 2, 14 e 26, sempre nas transições de cena.',
)
