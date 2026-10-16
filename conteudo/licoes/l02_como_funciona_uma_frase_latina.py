from conteudo.util import (tabela, exemplos, dica, diagrama_frase, exercicio, referencia, observacao,
                           pratica_guiada, analise)

LICAO = dict(
    slug='02-como-funciona-uma-frase-latina', titulo='Como funciona uma frase latina?', titulo_latim='Dē sententiā Latīnā', tempo='45 min',
    resumo='Em português, a ordem das palavras diz quem faz o quê. Em latim, quem diz isso são as terminações. Entender essa diferença é a chave de tudo o que vem depois.',
    status='publicada',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['flexão e casos', 'nominativo e acusativo', 'ordem das palavras', 'ênfase', 'ausência de artigo', 'sujeito oculto', 'concordância', 'presente do indicativo (prévia)', 'leitura na ordem latina', 'raciocínio por exclusão', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 1 (pronúncia e acento), para ler os exemplos em voz alta.', licoes=['01-o-que-e-o-latim']),
    referencias=[referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 21 (o latim como língua flexional), § 286 (concordância do adjetivo), § 316 (concordância do verbo), § 339 (sujeito no nominativo), § 387 (objeto direto no acusativo), §§ 595–599 (ordem das palavras; o § 597 comenta a ênfase na primeira frase de César), § 600 (relações expressas pela flexão)', tipo='dominio_publico'),
                 referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 20.1 (o latim não tem artigo), § 166 (sujeito no nominativo), § 172 (objeto direto no acusativo), § 234 (concordância do adjetivo), § 254 (concordância do verbo), §§ 348–350 (ordem das palavras e ênfase), §§ 67.a e 69 (acusativo plural em -īs de fortis)', tipo='dominio_publico'),
                 referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 14 (a proposição: sujeito, predicado e complementos), em português', tipo='dominio_publico'),
                 referencia('Commentarii de Bello Gallico, 1.1', 'Gaius Iulius Caesar', catalogo='caesar-commentarii-de-bello-gallico-selecoes', nota='frase citada como exemplo autêntico (texto conferido na ed. T. Rice Holmes, Oxford, 1914, via Perseus: partes tres; A&G § 597 cita a frase numa edição que escreve partīs trīs)', tipo='dominio_publico'),
                 referencia('Vulgata, Evangelho segundo João 1,1', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', nota='frase citada como exemplo autêntico (texto conferido na Vulgata Clementina, Wikisource latina)', tipo='dominio_publico'),
                 referencia('Phormio, verso 203', 'Publius Terentius Afer (Terêncio)', url='https://www.thelatinlibrary.com/ter.phormio.html', nota='frase autêntica analisada na seção 6 (não está no catálogo). Texto da The Latin Library (fortis fortuna adiuvat); a ed. de E. St. J. Parry (Londres, 1857), no Perseus, traz fortes, variante de grafia do acusativo plural', tipo='dominio_publico')],
    objetivos=[
        'Entender que o latim marca a função das palavras pela terminação, não pela posição.',
        'Reconhecer sujeito e objeto direto numa frase simples pelas terminações.',
        'Saber o que o latim não tem (artigos, pronome sujeito obrigatório) e como compensa isso.',
        'Começar a ler na ordem latina, da primeira à última palavra, sem reordenar.',
        'Usar o número do verbo e o raciocínio por exclusão para decidir quem é o sujeito numa frase autêntica.',
    ],
    secoes=[
        ('Uma língua de terminações', f'''
<p>Compare estas duas frases em português: <i>Marco ama Júlia</i> e <i>Júlia ama Marco</i>. As palavras são as mesmas; o que mudou foi a ordem, e com ela o sentido. Em português, a <b>posição</b> da palavra diz se ela é sujeito ou objeto.</p>
<p>Em latim, não. Veja:</p>
{exemplos([('Mārc<b>us</b> Iūli<b>am</b> amat.', 'Marco ama Júlia.'), ('Iūli<b>am</b> Mārc<b>us</b> amat.', 'Marco ama Júlia. (a mesma coisa!)'), ('Amat Mārc<b>us</b> Iūli<b>am</b>.', 'Marco ama Júlia. (ainda a mesma coisa)'), ('Mārc<b>um</b> Iūli<b>a</b> amat.', 'Júlia ama Marco.')])}
<p>As três primeiras frases significam exatamente o mesmo, porque em todas <i>Mārcus</i> termina em <i>-us</i> (a terminação de quem faz a ação) e <i>Iūliam</i> termina em <i>-am</i> (a terminação de quem recebe a ação). Na quarta frase, as terminações trocaram de lugar: <i>Mārcum</i> agora é o objeto e <i>Iūlia</i> é o sujeito. A ordem ficou igual à da primeira; o sentido inverteu.</p>
<p>É isso que se chama de <b>língua flexional</b>: a palavra "se flexiona", muda de forma, para indicar sua função. Cada forma diferente de um nome é um <b>caso</b>. No próximo capítulo você verá os seis casos; por enquanto, bastam dois:</p>
{tabela(['Função', 'Nome do caso', 'Terminação (palavras como <i>Iūlia</i>)', 'Terminação (palavras como <i>Mārcus</i>)'], [
    ['quem faz a ação (sujeito)', 'nominativo', '-a (<i>Iūlia</i>, <i>puella</i>, <i>rosa</i>)', '-us (<i>Mārcus</i>, <i>servus</i>, <i>amīcus</i>)'],
    ['quem recebe a ação (objeto direto)', 'acusativo', '-am (<i>Iūliam</i>, <i>puellam</i>, <i>rosam</i>)', '-um (<i>Mārcum</i>, <i>servum</i>, <i>amīcum</i>)'],
], 'Os dois casos de que você precisa hoje')}
{dica('<b>Pense na terminação como um crachá.</b> Cada palavra chega à frase dizendo o que veio fazer: "-us: sou o sujeito", "-am: sou o objeto". Por isso o romano podia espalhar as palavras na ordem que quisesse, e você precisa ler os crachás antes de ler a ordem.')}
'''),
        ('O que o latim não tem', f'''
<p>Duas ausências costumam surpreender quem começa.</p>
<h3>Não há artigos</h3>
<p>O latim não tem "o, a, um, uma". <i>Puella</i> pode ser <i>a menina</i>, <i>uma menina</i> ou simplesmente <i>menina</i>; o contexto decide. Ao traduzir, escolha o artigo que o português pede.</p>
{exemplos([('Puella cantat.', 'A menina canta. / Uma menina canta.'), ('Rosa pulchra est.', 'A rosa é bela.')])}
<h3>O sujeito pode ficar dentro do verbo</h3>
<p>Como em português, o latim não precisa de pronome sujeito: a terminação do verbo já diz a pessoa. <i>Amat</i> significa "ele ama" ou "ela ama"; <i>amō</i>, "eu amo". Veja as seis formas do presente de <i>amāre</i> (amar), só para reconhecê-las por enquanto (o capítulo 6 apresenta o presente de todos os verbos):</p>
{tabela(['Pessoa', 'Latim', 'Português', 'Terminação'], [
    ['1ª do singular', 'am<b>ō</b>', 'eu amo', '-ō'], ['2ª do singular', 'amā<b>s</b>', 'tu amas / você ama', '-s'], ['3ª do singular', 'ama<b>t</b>', 'ele, ela ama', '-t'],
    ['1ª do plural', 'amā<b>mus</b>', 'nós amamos', '-mus'], ['2ª do plural', 'amā<b>tis</b>', 'vós amais / vocês amam', '-tis'], ['3ª do plural', 'ama<b>nt</b>', 'eles, elas amam', '-nt'],
], 'Presente do indicativo de amāre (prévia)', latim_cols=(1,))}
<p>Repare que as terminações do verbo também são "crachás": <i>-t</i> diz "uma pessoa faz isso", <i>-nt</i> diz "várias pessoas fazem isso". Isso permite um primeiro teste de leitura: o sujeito de um verbo em <i>-nt</i> tem de estar no plural.</p>
{exemplos([('Puellae cantant.', 'As meninas cantam. (verbo em -nt, sujeito no plural: <i>puellae</i>)'), ('Puella cantat.', 'A menina canta. (verbo em -t, sujeito no singular)')])}
'''),
        ('A ordem das palavras: tendências, não regras', f'''
<p>Se a ordem não muda o sentido, ela é livre? Quase. A ordem latina é flexível, mas tem preferências, e conhecê-las ajuda a antecipar o que vem.</p>
<ul>
<li>Na prosa, o <b>verbo tende a ficar no fim</b> da frase: <i>Mārcus Iūliam amat</i>. Isso significa que você muitas vezes só descobre "o que aconteceu" na última palavra. Aguente a expectativa.</li>
<li>O <b>sujeito costuma vir primeiro</b>, e o objeto antes do verbo. A ordem "neutra" é sujeito, objeto, verbo.</li>
<li>Palavras que dependem uma da outra ficam normalmente <b>próximas</b>: o genitivo ("de alguém") perto do nome a que se refere, o adjetivo perto do substantivo.</li>
<li>Mudar a ordem serve para dar <b>ênfase</b>. O lugar de maior destaque é o começo da frase: a palavra deslocada para lá chama atenção. O fim também pode receber ênfase, mas com bem menos frequência. Os poetas exploram essas possibilidades ao máximo.</li>
</ul>
<p>Dois exemplos autênticos, para ver as tendências em textos reais:</p>
{exemplos([('Gallia est omnis dīvīsa in partēs trēs.', 'A Gália está, toda ela, dividida em três partes. (César, <i>BG</i> 1.1.1)'), ('In prīncipiō erat Verbum, et Verbum erat apud Deum…', 'No princípio era o Verbo, e o Verbo estava junto de Deus… (Jo 1,1, Vulgata)')])}
<p>Na frase de César, <i>Gallia</i> (sujeito, <i>-a</i>) abre a frase como o assunto de que se vai falar, <i>omnis</i> ("toda") concorda com ela e <i>in partēs trēs</i> ("em três partes") fecha com a informação nova. A gramática de Allen e Greenough (§ 597) lê aí uma ênfase em <i>dīvīsa</i>: a Gália que os romanos chamavam por um só nome, na verdade, está <b>dividida</b>. Na frase de João, o verbo <i>erat</i> ("era, estava") vem antes do sujeito <i>Verbum</i>: a ordem muda, o sentido não.</p>
'''),
        ('Concordância: palavras que combinam', f'''
<p>Se a terminação é um crachá, as palavras que andam juntas usam crachás combinando. O verbo concorda com o sujeito em número; o adjetivo concorda com o substantivo em gênero, número e caso. Observe os pares:</p>
{exemplos([('puell<b>a</b> bon<b>a</b>', 'a boa menina'), ('puell<b>ae</b> bon<b>ae</b>', 'as boas meninas'), ('serv<b>us</b> bon<b>us</b>', 'o bom escravo'), ('serv<b>um</b> bon<b>um</b>', 'o bom escravo (como objeto)'), ('Puell<b>a</b> bon<b>a</b> serv<b>um</b> bon<b>um</b> laudat.', 'A boa menina elogia o bom escravo.')])}
<p>Na última frase, mesmo se as palavras estivessem embaralhadas (<i>bonum puella laudat bona servum</i>), as terminações diriam quem combina com quem: <i>-a</i> com <i>-a</i>, <i>-um</i> com <i>-um</i>. É assim que a poesia latina consegue afastar o adjetivo do seu substantivo, às vezes com várias palavras no meio, sem perder a clareza.</p>
{observacao('Combinar não é rimar', 'O crachá do adjetivo combina com o <b>gênero</b>, o número e o caso do nome, e não necessariamente com as suas letras finais. Nos exemplos acima as terminações coincidem, mas há nomes em <i>-a</i> que são masculinos, como <i>nauta</i> (marinheiro), e pedem o adjetivo masculino: <i>nauta bonus</i>. Você os verá no capítulo 4.')}
'''),
        ('Como ler na ordem latina', f'''
<p>A tentação de quem começa é "caçar o verbo", depois procurar o sujeito, depois reordenar tudo para o português. Funciona com frases curtas e desaba nas longas. A técnica que vale a pena aprender desde já é outra: <b>leia da primeira à última palavra</b>, registrando o crachá de cada uma e criando expectativas.</p>
{diagrama_frase([('Agricola', 'nominativo: eis o sujeito'), ('fīliam', 'acusativo: eis o objeto'), ('magistrī', 'genitivo: "do mestre", liga-se a fīliam'), ('laudat', 'verbo, 3ª sing.: "elogia"')], 'Lendo em ordem: <i>Agricola fīliam magistrī laudat</i> = O agricultor elogia a filha do mestre.')}
<ol>
<li><i>Agricola</i>: termina em <i>-a</i>, nominativo. Já sei quem faz a ação: o agricultor. Espero um verbo no singular.</li>
<li><i>fīliam</i>: termina em <i>-am</i>, acusativo. Alguém recebe a ação: a filha. Filha de quem?</li>
<li><i>magistrī</i>: terminação <i>-ī</i>, o genitivo ("de"), caso que você conhecerá no próximo capítulo (a terminação <i>-ī</i> das palavras como <i>magister</i> e <i>Mārcus</i> é estudada no capítulo 5). Responde à pergunta: do mestre.</li>
<li><i>laudat</i>: verbo em <i>-t</i>, singular, "elogia". Combina com o sujeito singular. Frase fechada.</li>
</ol>
<p>Note que em nenhum momento foi preciso reordenar. A frase foi se montando palavra a palavra, como um romano a ouviria. Com a prática, as expectativas ficam automáticas: um nominativo pede um verbo; um acusativo pede um verbo que o receba; um genitivo procura um substantivo vizinho.</p>
{dica('<b>Regra de ouro do iniciante:</b> antes de perguntar "o que esta palavra significa?", pergunte "qual é a terminação desta palavra?". O sentido vem do dicionário; a função, só da terminação.')}
'''),
        ('Análise gramatical: uma frase autêntica', f'''
<p>Você já tem tudo o que precisa para analisar um provérbio que os romanos repetiam e que chegou até o português. Na comédia <i>Phormio</i> (Formião), de Terêncio, um escravo esperto anima o jovem patrão desesperado com estas três palavras:</p>
{exemplos([('… fortīs fortūna adiuvat.', 'A sorte ajuda os corajosos. (Terêncio, <i>Phormio</i> 203)')])}
<p>Leia na ordem latina. <i>Fortīs</i> é uma forma que você ainda não conhece: é o adjetivo <i>fortis</i> ("forte, corajoso"), de outro grupo de palavras, que você estudará no capítulo 10. <i>Fortūna</i> termina em <i>-a</i>, como <i>Iūlia</i> e <i>puella</i>: nominativo, um candidato a sujeito. <i>Adiuvat</i> ("ajuda") termina em <i>-t</i>: o sujeito é uma só pessoa ou coisa. A frase está resolvida, mesmo com uma palavra desconhecida.</p>
{analise('Terêncio, Phormio 203, palavra a palavra', [
    ('fortīs', 'fortis, forte (adjetivo), "forte, corajoso"; aqui usado como substantivo: "os corajosos"', 'acusativo plural masculino; <i>-īs</i> é uma variante de <i>-ēs</i> (Bennett § 67.a); a edição de César citada por Allen e Greenough (§ 597) também escreve <i>partīs trīs</i>; já a edição de Terêncio de E. St. J. Parry (1857) traz aqui a forma em <i>-ēs</i>, <i>fortes</i>', 'objeto direto: quem recebe a ajuda'),
    ('fortūna', 'fortūna, -ae (f.), "sorte, fortuna"', 'nominativo singular (terminação <i>-a</i>, como <i>Iūlia</i>)', 'sujeito: quem ajuda'),
    ('adiuvat', 'adiuvō, adiuvāre, "ajudar"', 'presente do indicativo, 3ª pessoa do singular (<i>-t</i>)', 'verbo; concorda com o sujeito singular <i>fortūna</i>'),
])}
<p>O raciocínio que decide a frase é de <b>exclusão</b>, e vale a pena guardá-lo. O verbo em <i>-t</i> pede um sujeito singular. <i>Fortūna</i> é um nominativo singular e preenche esse lugar. Então <i>fortīs</i>, seja qual for a sua forma, não pode ser o sujeito: um lugar já ocupado não se ocupa duas vezes. Como <i>adiuvāre</i> pede alguém que seja ajudado, <i>fortīs</i> é o objeto. Quem lê só pela ordem traduziria "os fortes, a fortuna ajuda" ou, pior, "a fortuna forte ajuda", o que não faz sentido em latim nem em português.</p>
<p>Repare também na ordem: objeto, sujeito, verbo. O objeto foi para o começo, o lugar de destaque: não é qualquer pessoa que a sorte ajuda, são os <b>corajosos</b>. E o verbo ficou no fim, como de costume. O som também ajuda a memorizar: <i>fortīs fortūna</i> começa duas vezes por <i>fort-</i>.</p>
'''),
    ],
    erros_comuns=[
        ('Tomar a primeira palavra da frase como sujeito.', 'Em <i>Iūliam Mārcus amat</i>, a primeira palavra é o objeto: o <i>-am</i> diz isso. Antes de decidir quem faz a ação, leia a terminação de cada palavra; a posição, em latim, indica ênfase, não função.'),
        ('Traduzir conservando a ordem latina.', '<i>Mārcum Iūlia amat</i> não é "Marco Júlia ama", frase que em português ou é estranha ou diz o contrário. Identifique as funções na ordem latina e, ao escrever em português, use a ordem que o português exige para essas funções: "Júlia ama Marco".'),
        ('Ignorar a terminação do verbo.', 'O <i>-t</i> e o <i>-nt</i> são a melhor prova do sujeito. Em <i>Rosae puellam dēlectant</i>, o verbo plural confirma que o sujeito é <i>rosae</i>, e não <i>puellam</i>, que além disso tem crachá de objeto.'),
        ('Procurar um sujeito escrito em toda frase.', 'Como em português, o sujeito pode estar só no verbo: <i>Rosam amat</i> é "(ele, ela) ama a rosa". Não transforme <i>rosam</i> em sujeito só porque falta um nominativo; o <i>-am</i> continua dizendo "objeto".'),
        ('Pensar que concordar é ter as mesmas letras.', 'O adjetivo concorda em gênero, número e caso, e as letras às vezes não coincidem: <i>nauta</i> (marinheiro) é masculino e se diz <i>nauta bonus</i>, não <i>nauta bona</i>. O capítulo 4 explica esses nomes.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · O objeto na frente',
            'Leia na ordem latina e traduza: <i lang="la">Fīliam agricola laudat.</i> Vocabulário: <i>fīlia</i>, filha; <i>agricola</i>, agricultor; <i>laudat</i>, elogia.', [
            ('<i>Fīliam</i>: que crachá é esse, e o que ele faz esperar?', 'Terminação <i>-am</i>: acusativo, o objeto. Alguém vai fazer algo com "a filha"; falta saber quem e o quê.'),
            ('<i>agricola</i>: e agora?', 'Terminação <i>-a</i>: nominativo, o sujeito. Já sabemos quem age: o agricultor.'),
            ('<i>laudat</i>: o verbo confirma?', 'Sim. Termina em <i>-t</i>, singular, e combina com o sujeito singular <i>agricola</i>. "Elogia".'),
            ('Monte a tradução portuguesa.', '"O agricultor elogia a filha." Em português o sujeito vem antes; em latim, a filha estava em destaque no começo. Se quiser preservar a ênfase: "É a filha que o agricultor elogia."'),
        ]),
        pratica_guiada('Prática guiada 2 · Decidir por exclusão',
            'Traduza <i lang="la">Magistrum puerī audiunt.</i> Vocabulário: <i>magister</i>, mestre; <i>puer</i>, menino; <i>audiunt</i>, ouvem. A forma <i>puerī</i> ainda não foi ensinada: descubra a função dela pelo resto da frase.', [
            ('Qual é a função de <i>magistrum</i>?', 'Terminação <i>-um</i>: acusativo, o objeto. O mestre é quem recebe a ação.'),
            ('O que <i>audiunt</i> exige?', 'Termina em <i>-nt</i>: o sujeito tem de ser plural, "eles ouvem".'),
            ('Então, o que é <i>puerī</i>?', 'O objeto já está ocupado por <i>magistrum</i>, e o verbo plural precisa de um sujeito plural. A única palavra que sobra é <i>puerī</i>: só pode ser o sujeito, no plural, "os meninos". (O capítulo 5 confirma: <i>-ī</i> é o nominativo plural desse grupo.)'),
            ('Monte a tradução.', '"Os meninos ouvem o mestre."'),
        ], 'É o mesmo raciocínio da frase de Terêncio: quando uma função já está ocupada, a palavra desconhecida fica com a função que sobra.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Quem faz, quem recebe', 'Em cada frase, diga qual palavra é o sujeito e qual é o objeto direto, olhando só as terminações. Depois traduza. Vocabulário: <i>videt</i> = vê; <i>audiunt</i> = ouvem; <i>timet</i> = teme; <i>amant</i> = amam.', [
            ('<i>Mārcus Iūliam videt.</i>', 'Sujeito <i>Mārcus</i> (-us), objeto <i>Iūliam</i> (-am): Marco vê Júlia.'),
            ('<i>Iūliam Mārcus videt.</i>', 'As mesmas terminações, a mesma frase: Marco vê Júlia. Só a ênfase muda (Júlia em primeiro plano).'),
            ('<i>Puerī magistrum audiunt.</i>', 'Sujeito <i>puerī</i> (plural, combinando com <i>audiunt</i> em -nt), objeto <i>magistrum</i> (-um): Os meninos ouvem o mestre.'),
            ('<i>Dominum servus timet.</i>', 'Sujeito <i>servus</i> (-us), objeto <i>dominum</i> (-um): O escravo teme o senhor. A ordem "objeto primeiro" dá ênfase ao senhor.'),
            ('<i>Puellae rosās amant.</i>', 'Sujeito <i>puellae</i> (plural; o verbo está em -nt), objeto <i>rosās</i> (acusativo plural, -ās): As meninas amam as rosas.'),
        ]),
        exercicio('Exercício 2 · Troque os crachás', 'Mude só as terminações necessárias para inverter quem faz e quem recebe a ação.', [
            ('<i>Servus dominum videt.</i> → "O senhor vê o escravo."', '<i>Dominus servum videt.</i>'),
            ('<i>Puella amīcam exspectat.</i> (exspectat = espera) → "A amiga espera a menina."', '<i>Amīca puellam exspectat.</i>'),
            ('<i>Magister puerum laudat.</i> → "O menino elogia o mestre."', '<i>Puer magistrum laudat.</i> Repare que o nominativo de <i>puerum</i> é <i>puer</i>, sem <i>-us</i>: algumas palavras do grupo de <i>Mārcus</i> têm o nominativo em <i>-er</i>, e você as verá no capítulo 5, sobre a segunda declinação.'),
        ]),
        exercicio('Exercício 3 · Traduza lendo em ordem', 'Leia palavra a palavra, anotando a função de cada uma, e só então traduza. Vocabulário: <i>terra</i> = terra; <i>dēlectant</i> = encantam, agradam; <i>vīlla</i> = casa de campo; <i>ōrnant</i> = enfeitam; <i>dominae</i> = da senhora; <i>cantant</i> = cantam; <i>nautae</i> = os marinheiros; <i>lūnam</i> = a lua; <i>spectant</i> = contemplam.', [
            ('<i>Agricola terram amat.</i>', '<i>Agricola</i> (sujeito), <i>terram</i> (objeto), <i>amat</i> (verbo): O agricultor ama a terra.'),
            ('<i>Rosae puellam dēlectant.</i>', '<i>Rosae</i> (sujeito plural, confirmado por -nt), <i>puellam</i> (objeto), <i>dēlectant</i>: As rosas encantam a menina. Cuidado: a primeira palavra não é "a menina".'),
            ('<i>Servī vīllam dominae ōrnant.</i>', '<i>Servī</i> (sujeito plural), <i>vīllam</i> (objeto), <i>dominae</i> (genitivo, "da senhora", ligado a <i>vīllam</i>), <i>ōrnant</i>: Os escravos enfeitam a casa da senhora.'),
            ('<i>Nautae lūnam spectant et cantant.</i>', '<i>Nautae</i> (sujeito plural), <i>lūnam</i> (objeto), <i>spectant</i>, <i>et</i> ("e"), <i>cantant</i>: Os marinheiros contemplam a lua e cantam. <i>Nauta</i> termina em -a, mas é masculino: há algumas palavras assim.'),
        ]),
        exercicio('Exercício 4 · Mude a ordem ou o número', 'Faça a transformação pedida, mudando só o que for necessário.', [
            ('Escreva <i>Mārcus Iūliam videt</i> em duas outras ordens, sem mudar o sentido.', 'Por exemplo, <i>Iūliam Mārcus videt</i> e <i>Videt Mārcus Iūliam</i> (também <i>Iūliam videt Mārcus</i>, <i>Mārcus videt Iūliam</i>...). Qualquer ordem serve, porque as terminações <i>-us</i> e <i>-am</i> não mudam; o que muda é a ênfase.'),
            ('Ponha o sujeito no plural: <i>Puella rosam amat.</i>', '<i>Puellae rosam amant.</i> O sujeito passa a <i>puellae</i> e o verbo, que concorda com ele, passa de <i>-t</i> a <i>-nt</i>. O objeto não muda.'),
            ('Ponha o sujeito no plural: <i>Nauta lūnam spectat.</i>', '<i>Nautae lūnam spectant.</i> Mesma operação: <i>nauta</i> → <i>nautae</i>, <i>spectat</i> → <i>spectant</i>.'),
            ('Ponha o sujeito no singular: <i>Agricolae terram amant.</i>', '<i>Agricola terram amat.</i> O verbo volta a <i>-t</i>.'),
            ('Ponha o objeto no singular: <i>Rosās puella amat.</i>', '<i>Rosam puella amat.</i> Só o objeto muda (<i>-ās</i> → <i>-am</i>); o verbo continua em <i>-t</i>, porque concorda com o sujeito, não com o objeto.'),
        ]),
        exercicio('Exercício 5 · Do português para o latim', 'Traduza para o latim, usando o vocabulário deste capítulo (<i>amat, laudat, spectant, timet, cantat; agricola, lūna, servus, dominus, puella</i>). Não há artigos em latim.', [
            ('Júlia ama Marco.', '<i>Iūlia Mārcum amat.</i> Sujeito em <i>-a</i>, objeto em <i>-um</i>. Outras ordens (<i>Mārcum Iūlia amat</i>) dizem o mesmo, com outra ênfase.'),
            ('Marco elogia o agricultor.', '<i>Mārcus agricolam laudat.</i> <i>Agricola</i> recebe a ação, por isso vai para o acusativo <i>agricolam</i>.'),
            ('As meninas contemplam a lua.', '<i>Puellae lūnam spectant.</i> Sujeito plural, verbo em <i>-nt</i>.'),
            ('O escravo teme o senhor.', '<i>Servus dominum timet.</i>'),
            ('Uma menina canta.', '<i>Puella cantat.</i> O latim não distingue "a menina" de "uma menina": a mesma frase serve para as duas traduções.'),
        ]),
    ],
    leituras=['sonnenschein-ora-maritima-a-latin-story-for-beginners', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'mainwaring-lingua-latina-primus-annus', 'jones-puer-romanus', 'college-dcc-latin-core-vocabulary'],
    leituras_nota='Os leitores graduados abaixo começam exatamente com frases como as deste capítulo: sujeito, objeto e verbo, repetidos até virarem naturais. Leia em voz alta. A lista do DCC serve para consultar as palavras mais frequentes.',
)
