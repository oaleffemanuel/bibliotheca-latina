from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio, referencia,
                           pratica_guiada, analise)

LICAO = dict(
    slug='04-a-primeira-declinacao', titulo='A primeira declinação', titulo_latim='Dē prīmā dēclīnātiōne', tempo='60 min',
    resumo='A primeira família de nomes do latim, completa: gênero, as exceções masculinas, as formas especiais, as preposições que acompanham cada caso e um primeiro texto corrido para ler.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['1ª declinação', 'gênero dos nomes', 'masculinos em -a', 'dativo e ablativo plural', 'preposições com acusativo', 'preposições com ablativo', 'vocabulário básico', 'nomes só no plural (tenebrae)', 'análise de frase autêntica', 'leitura de texto corrido'],
    prerequisitos=dict(texto='Capítulo 3: os seis casos, o paradigma de rosa e as formas que coincidem (-ae, -a/-ā, -īs).', licoes=['03-introducao-aos-casos']),
    referencias=[referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§§ 40–42 (1ª declinação: tema, paradigma, gênero), § 43 (formas especiais; -ābus em § 43.e), § 44 (nomes gregos), §§ 219–221 (preposições)', tipo='dominio_publico'),
                 referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 20 (paradigma), § 21 (masculinos; -ābus em § 21.2.e), § 22 (nomes gregos), § 56.3 (tenebrae, só no plural), §§ 141–143 (preposições; ā/ab e ē/ex em § 142.1–2)', tipo='dominio_publico'),
                 referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 34 (1ª declinação, mensa; nota 4: dea e fīlia com -ābus)', tipo='dominio_publico'),
                 referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 18 (1ª declinação, poeta e rosa), n. 19 (formas em -ābus), nn. 146–147 (preposições com acusativo e com ablativo)', tipo='dominio_publico'),
                 referencia('DCC Latin Core Vocabulary', 'Dickinson College', catalogo='college-dcc-latin-core-vocabulary', nota='conferência do vocabulário do capítulo contra a lista básica', tipo='site'),
                 referencia('Biblia Sacra Vulgata (editio Clementina), João 1,5', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', nota='frase autêntica analisada na seção 4', tipo='dominio_publico')],
    objetivos=[
        'Declinar qualquer nome da primeira declinação, no singular e no plural, inclusive os masculinos.',
        'Reconhecer as formas especiais (<i>fīliābus</i>, <i>deābus</i>) e os nomes gregos mais comuns.',
        'Usar as preposições que pedem acusativo e as que pedem ablativo, e entender o par <i>in</i> + acusativo / <i>in</i> + ablativo.',
        'Analisar palavra a palavra uma frase autêntica com preposição e formas da primeira declinação.',
        'Ler um texto corrido de dez frases só com nomes da primeira declinação e verbos no presente.',
    ],
    secoes=[
        ('A família das palavras em -a', f'''
<p>No capítulo anterior você viu o paradigma de <i>rosa</i>. Agora vamos olhar a família inteira. A <b>primeira declinação</b> reúne todos os nomes cujo <b>genitivo singular termina em <i>-ae</i></b>: é esse o critério, e é assim que o dicionário os apresenta: <i>rosa, -ae</i>; <i>puella, -ae</i>; <i>nauta, -ae</i>. Sempre que você encontrar um nome em <i>-a</i> com genitivo em <i>-ae</i>, ele se declina exatamente como <i>rosa</i>.</p>
{tabela_declinacao('Primeira declinação: puella, -ae (f.), "menina" · nauta, -ae (m.), "marinheiro"', [
    ('puell<b>a</b>', 'puell<b>ae</b>', 'naut<b>a</b>', 'naut<b>ae</b>'), ('puell<b>ae</b>', 'puell<b>ārum</b>', 'naut<b>ae</b>', 'naut<b>ārum</b>'),
    ('puell<b>ae</b>', 'puell<b>īs</b>', 'naut<b>ae</b>', 'naut<b>īs</b>'), ('puell<b>am</b>', 'puell<b>ās</b>', 'naut<b>am</b>', 'naut<b>ās</b>'),
    ('puell<b>a</b>', 'puell<b>ae</b>', 'naut<b>a</b>', 'naut<b>ae</b>'), ('puell<b>ā</b>', 'puell<b>īs</b>', 'naut<b>ā</b>', 'naut<b>īs</b>')],
    colunas=('puella · sing.', 'puella · pl.', 'nauta · sing.', 'nauta · pl.'))}
<p>As terminações são as mesmas para os dois nomes. A única diferença entre <i>puella</i> e <i>nauta</i> é o <b>gênero</b>, que não se vê na palavra, mas se vê no adjetivo que a acompanha: <i>puella bona</i>, mas <i>nauta bonus</i> (o capítulo 5 apresenta os adjetivos; por enquanto, basta saber que eles "obedecem" ao gênero do nome).</p>
<p>Para fixar o ritmo, declame em voz alta, sempre na mesma ordem: <i>puella, puellae, puellae, puellam, puella, puellā; puellae, puellārum, puellīs, puellās, puellae, puellīs</i>. É uma ladainha, e é para ser: o ouvido guarda o que a boca repete.</p>
'''),
        ('O gênero: femininos, e os homens em -a', f'''
<p>Os nomes da primeira declinação são <b>femininos</b>, com uma exceção previsível: os que designam <b>homens</b> ou ofícios tradicionalmente masculinos. Esses são masculinos, embora terminem em <i>-a</i> e se declinem como <i>rosa</i>. O português conserva vários deles: <i>o poeta, o pirata, o nauta</i>.</p>
{tabela(['Latim', 'Português', 'Gênero'], [
    ['nauta, -ae', 'marinheiro', 'm.'], ['agricola, -ae', 'agricultor', 'm.'], ['poēta, -ae', 'poeta', 'm.'], ['pīrāta, -ae', 'pirata', 'm.'],
    ['scrība, -ae', 'escriba, escrivão', 'm.'], ['incola, -ae', 'habitante', 'm. (ou f., conforme a pessoa)'], ['convīva, -ae', 'conviva, convidado', 'm. (ou f.)'],
], 'Os masculinos mais comuns da primeira declinação', latim_cols=(0,))}
{observacao('Por que isso importa agora?', 'Porque a concordância depende do gênero, não da terminação. Quando você chegar aos adjetivos, verá <i>poēta clārus</i> ("poeta famoso"), com o adjetivo masculino em <i>-us</i> ao lado de um nome em <i>-a</i>. Quem aprendeu que "<i>-a</i> é feminino" estranha; quem aprendeu que "<i>-a</i> é a primeira declinação, e o gênero vem do dicionário" não.')}
<h3>Duas formas especiais</h3>
<p>Dois nomes fazem normalmente o dativo e o ablativo plural em <b><i>-ābus</i></b> em vez de <i>-īs</i>: <i>fīlia</i> (filha) e <i>dea</i> (deusa). O motivo é prático: distingui-los de <i>fīliīs</i> ("aos filhos", de <i>fīlius</i>) e <i>deīs</i> ("aos deuses", de <i>deus</i>). Raramente outros nomes com par masculino fazem o mesmo, como <i>līberta</i> (liberta) e <i>equa</i> (égua), mas quase só quando os dois sexos aparecem juntos. A forma em <i>-ābus</i> é sobretudo esperada justamente nesse contexto (<i>fīliīs et fīliābus</i>, "aos filhos e às filhas"); fora dele, a forma regular <i>fīliīs</i> também se encontra. Este livro segue Allen e Greenough, Bennett e Kennedy, que dão <i>deābus</i> e <i>fīliābus</i> como as formas usuais de <i>dea</i> e <i>fīlia</i>, mesmo sem masculino ao lado; por isso os exemplos e exercícios do capítulo usam <i>fīliābus</i> também sozinho. O Pe. Ravizza é mais restritivo: só admite <i>-ābus</i> quando há um masculino unido ou contraposto.</p>
{exemplos([('Agricola fīli<b>ābus</b> fābulās nārrat.', 'O agricultor conta histórias às filhas.'), ('Nautae de<b>ābus</b> et de<b>īs</b> rosās dant.', 'Os marinheiros dão rosas às deusas e aos deuses.')])}
<p>Alguns nomes de origem grega entraram na primeira declinação com terminações gregas no singular: <i>Aenēās</i> (Eneias, acusativo <i>Aenēān</i>) e <i>epitomē</i> ("resumo", acusativo <i>epitomēn</i>). Muitos outros se latinizaram por completo e se declinam como <i>rosa</i> (<i>grammatica</i>, <i>mūsica</i>). Você os encontrará nos poetas; no plural, seguem <i>rosa</i>. Por ora, só reconheça.</p>
'''),
        ('Preposições: o acusativo e o ablativo ganham companhia', f'''
<p>Boa parte dos acusativos e ablativos que você vai ler vem depois de uma <b>preposição</b>. Em latim, cada preposição "pede" um caso fixo, e isso é uma pista de leitura: ao ver <i>cum</i>, você já espera um ablativo; ao ver <i>ad</i>, um acusativo.</p>
{comparacao('Preposições mais frequentes e o caso que pedem', ['Preposição', 'Caso', 'Sentido', 'Exemplo'], [
    ['ad', 'acusativo', 'para, até, junto a', '<i>ad vīllam</i>: para a casa'], ['in (+ ac.)', 'acusativo', 'para dentro de, contra', '<i>in silvam</i>: para dentro da floresta'],
    ['per', 'acusativo', 'através de, por', '<i>per viās</i>: pelas ruas'], ['trāns', 'acusativo', 'além de, do outro lado de', '<i>trāns aquam</i>: do outro lado da água'],
    ['inter', 'acusativo', 'entre', '<i>inter puellās</i>: entre as meninas'], ['ante · post', 'acusativo', 'antes de · depois de', '<i>post cēnam</i>: depois do jantar'],
    ['in (+ abl.)', 'ablativo', 'em, dentro de (sem movimento)', '<i>in silvā</i>: na floresta'], ['cum', 'ablativo', 'com (companhia)', '<i>cum amīcā</i>: com a amiga'],
    ['ā / ab', 'ablativo', 'de, desde, a partir de; por (agente)', '<i>ā vīllā</i>: desde a casa'], ['ē / ex', 'ablativo', 'de dentro de, de', '<i>ex Ītaliā</i>: da Itália'],
    ['dē', 'ablativo', 'de cima de; sobre, a respeito de', '<i>dē fāmā</i>: sobre a fama'], ['sine', 'ablativo', 'sem', '<i>sine pecūniā</i>: sem dinheiro'], ['prō', 'ablativo', 'diante de; em favor de', '<i>prō patriā</i>: pela pátria'],
])}
<p>Repare no par <b><i>in</i></b>: com acusativo, há <b>movimento para dentro</b>; com ablativo, <b>permanência</b>. A diferença de sentido está inteira na terminação:</p>
{exemplos([('Puella in vīll<b>am</b> ambulat.', 'A menina caminha para dentro da casa. (movimento)'), ('Puella in vīll<b>ā</b> habitat.', 'A menina mora na casa. (sem movimento)'), ('Nautae in aqu<b>am</b> saliunt.', 'Os marinheiros pulam na água. (para dentro dela)'), ('Nautae in aqu<b>ā</b> sunt.', 'Os marinheiros estão na água.')])}
{dica('<b>Duas formas para a mesma preposição.</b> <i>ā</i> e <i>ab</i>, <i>ē</i> e <i>ex</i> são a mesma palavra. Antes de vogal ou <i>h</i>, use sempre a forma longa: <i>ab Ītaliā</i>, <i>ex aquā</i>. Antes de consoante, <i>ex</i> e <i>ē</i> alternam livremente (<i>ex silvā</i> ou <i>ē silvā</i>); já <i>ab</i> aparece só às vezes antes de consoante, e normalmente não antes de <i>b, p, f, v, m, c, g, q, t</i> (Bennett § 142.1): aí o normal é <i>ā</i>: <i>ā vīllā</i>, não <i>ab vīllā</i>. Regra prática: <i>ex</i> serve sempre; <i>ab</i>, só antes de vogal ou <i>h</i>.')}
'''),
        ('Frases caso a caso: uma construída, uma autêntica', f'''
<p>Com as preposições, as frases ganham circunstâncias: de onde, para onde, com quem. Leia esta na ordem latina, registrando o crachá de cada grupo:</p>
{diagrama_frase([('Nautae', 'nominativo pl. · sujeito'), ('cum fīliābus', 'cum + ablativo · companhia'), ('ex Ītaliā', 'ex + ablativo · origem'), ('ad īnsulam', 'ad + acusativo · destino'), ('nāvigant', 'verbo · "navegam"')],
    'Lendo em ordem: <i>Nautae cum fīliābus ex Ītaliā ad īnsulam nāvigant</i> = Os marinheiros navegam da Itália até a ilha com as filhas.')}
<ol>
<li><i>Nautae</i>: <i>-ae</i>; nominativo plural ou genitivo/dativo singular? Está no começo da frase e não há outro candidato a sujeito: aposto em sujeito plural. Espero um verbo em <i>-nt</i>.</li>
<li><i>cum fīliābus</i>: a preposição resolve tudo; <i>cum</i> pede ablativo, e <i>fīliābus</i> é a forma especial. Companhia: com as filhas.</li>
<li><i>ex Ītaliā</i>: <i>ex</i> + ablativo, origem: da Itália.</li>
<li><i>ad īnsulam</i>: <i>ad</i> + acusativo, destino: até a ilha.</li>
<li><i>nāvigant</i>: verbo em <i>-nt</i>, plural, "navegam". Confirma o sujeito <i>nautae</i>. Frase fechada.</li>
</ol>
<p>Note que, lendo assim, os grupos preposicionados se fecham sozinhos: preposição + nome é uma unidade, e você nunca precisa "esperar" por eles. O que fica em aberto, até o verbo, é só a dupla sujeito e objeto.</p>
<h3>Análise gramatical: uma frase autêntica</h3>
<p>O prólogo do Evangelho de João, na Vulgata, tem uma frase que parece escrita para treinar este capítulo: um nome da primeira declinação aparece duas vezes, uma no ablativo plural com <i>in</i> e outra no nominativo plural.</p>
{exemplos([('Et lūx in tenebrīs lūcet, et tenebrae eam nōn comprehendērunt.', 'E a luz brilha nas trevas, e as trevas não a compreenderam. (Jo 1,5, Vulgata)')])}
<p><i>Tenebrae</i> ("trevas") é um nome da primeira declinação que só se usa no plural, como o português "trevas" ou "férias" (Bennett § 56.3); declina-se como o plural de <i>rosa</i>. Três palavras ainda não foram estudadas: <i>lūx</i> ("luz", terceira declinação, capítulo 9), o pronome <i>eam</i> ("a ela", capítulo 15) e o perfeito <i>comprehendērunt</i> ("compreenderam", capítulo 13). Para a análise, basta saber o que elas são.</p>
{analise('Jo 1,5, palavra a palavra', [
    ('Et', 'et (conjunção), "e"', 'invariável', 'liga esta frase à anterior'),
    ('lūx', 'lūx, lūcis (f.), "luz"', 'nominativo singular, 3ª declinação', 'sujeito de <i>lūcet</i>'),
    ('in', 'in (preposição)', 'aqui com ablativo', 'lugar onde, sem movimento'),
    ('tenebrīs', 'tenebrae, -ārum (f., só plural), "trevas"', 'ablativo plural, 1ª declinação', '<i>in</i> + ablativo: "nas trevas"'),
    ('lūcet', 'lūceō, lūcēre, "brilhar"', 'presente, 3ª pessoa do singular', 'verbo da primeira oração'),
    ('et', 'et (conjunção), "e"', 'invariável', 'liga as duas orações'),
    ('tenebrae', 'tenebrae, -ārum', 'nominativo plural, 1ª declinação', 'sujeito de <i>comprehendērunt</i>'),
    ('eam', 'is, ea, id (pronome), "ele, ela"', 'acusativo singular feminino', 'objeto direto; retoma <i>lūx</i> (feminino): "a ela", "a"'),
    ('nōn', 'nōn (advérbio), "não"', 'invariável', 'nega o verbo, que vem logo depois'),
    ('comprehendērunt', 'comprehendō, comprehendere, "apreender, compreender; dominar"', 'perfeito, 3ª pessoa do plural (<i>-nt</i>)', 'verbo da segunda oração'),
])}
<p>Dois raciocínios deste capítulo resolvem a frase. <i>Tenebrīs</i> poderia ser dativo ou ablativo plural, mas vem depois de <i>in</i>, e <i>in</i> nunca pede dativo: é ablativo, e sem movimento, "nas trevas". <i>Tenebrae</i>, na segunda oração, poderia ser genitivo ou dativo singular, se a palavra tivesse singular; como é um nome só de plural e o verbo termina em <i>-nt</i>, é o nominativo plural, o sujeito. Repare ainda que <i>eam</i> tem a mesma terminação <i>-am</i> dos acusativos da primeira declinação: o crachá do objeto é reconhecível mesmo num pronome que você ainda não estudou. (O verbo <i>comprehendere</i> tem dois sentidos possíveis aqui, "compreender" e "dominar, vencer", e as traduções se dividem; a gramática da frase é a mesma.)</p>
'''),
        ('Vocabulário do capítulo', f'''
<p>Vinte e quatro nomes da primeira declinação e dez verbos no presente. A maioria está na lista das mil palavras mais frequentes do latim (DCC Latin Core Vocabulary): 17 dos 24 nomes e 8 dos 10 verbos; os outros foram escolhidos porque aparecem muito nos leitores para iniciantes. Aprenda-os pelas frases dos exercícios e do texto, não pela lista; a lista é para consulta.</p>
{tabela(['Nome', 'Significado', 'Nome', 'Significado'], [
    ['aqua, -ae (f.)', 'água', 'lūna, -ae (f.)', 'lua'], ['terra, -ae (f.)', 'terra', 'stella, -ae (f.)', 'estrela'],
    ['vīta, -ae (f.)', 'vida', 'rosa, -ae (f.)', 'rosa'], ['puella, -ae (f.)', 'menina', 'mēnsa, -ae (f.)', 'mesa'],
    ['fēmina, -ae (f.)', 'mulher', 'epistula, -ae (f.)', 'carta'], ['fīlia, -ae (f.)', 'filha', 'fābula, -ae (f.)', 'história, fábula'],
    ['domina, -ae (f.)', 'senhora', 'pecūnia, -ae (f.)', 'dinheiro'], ['rēgīna, -ae (f.)', 'rainha', 'patria, -ae (f.)', 'pátria'],
    ['vīlla, -ae (f.)', 'casa de campo', 'amīca, -ae (f.)', 'amiga'], ['īnsula, -ae (f.)', 'ilha', 'nauta, -ae (m.)', 'marinheiro'],
    ['silva, -ae (f.)', 'floresta', 'agricola, -ae (m.)', 'agricultor'], ['via, -ae (f.)', 'caminho, rua', 'poēta, -ae (m.)', 'poeta'],
], 'Nomes', latim_cols=(0, 2))}
{tabela(['Verbo (3ª pessoa)', 'Significado', 'Verbo (3ª pessoa)', 'Significado'], [
    ['amat · amant', 'ama · amam', 'portat · portant', 'carrega · carregam'], ['dat · dant', 'dá · dão', 'spectat · spectant', 'olha, contempla · olham'],
    ['habitat · habitant', 'mora · moram', 'vocat · vocant', 'chama · chamam'], ['nāvigat · nāvigant', 'navega · navegam', 'laudat · laudant', 'elogia · elogiam'],
    ['nārrat · nārrant', 'conta · contam', 'est · sunt', 'é, está · são, estão'],
], 'Verbos (só a 3ª pessoa, por enquanto)', latim_cols=(0, 2))}
{observacao('O que o português herdou', 'Quase toda a lista continua viva em português, às vezes disfarçada: <i>fēmina</i> deu "fêmea", <i>vīta</i> deu "vida", <i>stella</i> deu "estrela", <i>epistula</i> deu "epístola", <i>īnsula</i> deu "ilha" (e "insular"), <i>via</i> deu "via" e "viagem". Os nomes em <i>-a</i> são a declinação que o português mais conservou: por isso ela parece tão familiar.')}
'''),
        ('Resumo', '''
<ul>
<li>Primeira declinação = genitivo singular em <i>-ae</i>. Terminações: <i>-a, -ae, -ae, -am, -a, -ā</i> / <i>-ae, -ārum, -īs, -ās, -ae, -īs</i>.</li>
<li>Gênero feminino, exceto os nomes de homens e ofícios (<i>nauta, agricola, poēta</i>), que são masculinos.</li>
<li><i>fīliābus, deābus</i>: dativo e ablativo plural especiais, para não confundir com <i>fīliīs, deīs</i> (sobretudo quando os dois sexos aparecem juntos; <i>fīliīs</i> também ocorre).</li>
<li><i>ab</i> e <i>ex</i> antes de vogal; antes de consoante, <i>ā</i> (às vezes <i>ab</i>, quase nunca antes de labial ou de <i>c, g, q, t</i>) e <i>ē</i> ou <i>ex</i>.</li>
<li>Preposições com acusativo (<i>ad, in</i> movimento, <i>per, trāns, inter, ante, post</i>) e com ablativo (<i>in</i> sem movimento, <i>cum, ā/ab, ē/ex, dē, sine, prō</i>).</li>
<li>Ler em ordem: preposição + nome fecha um grupo; o que fica aberto até o verbo é a dupla sujeito e objeto.</li>
</ul>
<p>No próximo capítulo, a segunda declinação (<i>dominus, puer, bellum</i>) completa os crachás masculinos e neutros e traz os adjetivos.</p>
'''),
    ],
    erros_comuns=[
        ('Fazer o adjetivo concordar com a terminação, e não com o gênero: <i>nauta bona</i>.', '<i>Nauta</i>, <i>agricola</i>, <i>poēta</i> são masculinos, e o adjetivo vai para o masculino: <i>nauta bonus</i>, <i>poēta clārus</i>. O gênero vem do dicionário (<i>nauta, -ae</i>, m.), não da letra final.'),
        ('Usar <i>in</i> + acusativo para dizer onde algo está: <i>Puella in vīllam habitat</i>.', 'Morar não é movimento: <i>in vīllā habitat</i>, com ablativo. O acusativo depois de <i>in</i> só aparece quando há deslocamento para dentro (<i>in vīllam ambulat</i>, "entra caminhando na casa").'),
        ('Usar <i>cum</i> para o instrumento: <i>Agricola cum aquā terram rigat</i>.', '<i>Cum</i> indica companhia ("junto com alguém"). O instrumento vai no ablativo <b>sem</b> preposição, como você viu no capítulo 3: <i>Agricola aquā terram rigat</i>, "rega a terra com água".'),
        ('Estender o <i>-ābus</i> a qualquer nome: <i>puellābus</i>, <i>rosābus</i>.', 'Essas formas não existem no latim clássico. <i>-ābus</i> é próprio de <i>dea</i> e <i>fīlia</i> (e, raramente, de mais um ou outro nome com par masculino), justamente para distingui-los de <i>deīs</i> e <i>fīliīs</i>. Os demais nomes fazem sempre <i>-īs</i>.'),
        ('Ler <i>-īs</i> sempre como dativo ("a, para").', '<i>-īs</i> é também o ablativo plural. Se há preposição de ablativo (<i>in, cum, ex, ā, dē, sine, prō</i>), o caso está decidido: <i>in silvīs</i> é "nas florestas", não "às florestas".'),
        ('Escrever <i>ab</i> antes de qualquer consoante: <i>ab vīllā</i>.', 'Antes de consoante, o normal é <i>ā</i> (<i>ā vīllā</i>); <i>ab</i> vai antes de vogal ou <i>h</i> (<i>ab īnsulā</i>). Com <i>ex</i> não há esse problema: <i>ex vīllā</i> e <i>ē vīllā</i> são ambos corretos.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Três grupos preposicionados',
            'Leia na ordem latina e traduza: <i lang="la">Rēgīna cum fīliābus ā vīllā in silvam ambulat.</i> Vocabulário: <i>ambulat</i>, caminha; o resto está na lista do capítulo.', [
            ('<i>Rēgīna</i>: que caso, e o que você espera?', 'Nominativo singular: o sujeito. Espera-se um verbo em <i>-t</i>.'),
            ('<i>cum fīliābus</i>: como se resolve?', '<i>Cum</i> pede ablativo; <i>fīliābus</i> é o ablativo plural especial de <i>fīlia</i>. Companhia: "com as filhas". O grupo se fecha sozinho.'),
            ('<i>ā vīllā</i>: e este?', '<i>Ā</i> pede ablativo (forma curta, porque <i>vīllā</i> começa com consoante): ponto de partida, "da casa".'),
            ('<i>in silvam</i>: lugar onde ou direção?', 'Acusativo (<i>-am</i>) com <i>in</i>: movimento para dentro, "para a floresta".'),
            ('<i>ambulat</i> e a tradução final.', 'Verbo em <i>-t</i>, singular, confirma <i>rēgīna</i>. "A rainha, com as filhas, caminha da casa para a floresta."'),
        ]),
        pratica_guiada('Prática guiada 2 · Quatro formas em -ae e -īs',
            'Analise e traduza: <i lang="la">Poētae fābulās nautīs in īnsulā nārrant.</i>', [
            ('<i>Poētae</i>: nominativo plural, genitivo ou dativo singular?', 'Por enquanto, em aberto. É a primeira palavra e não há outro candidato a sujeito à vista: a hipótese mais provável é nominativo plural, "os poetas". O verbo vai decidir.'),
            ('<i>fābulās</i> e <i>nautīs</i>?', '<i>Fābulās</i>: acusativo plural, o objeto, "histórias". <i>Nautīs</i>: dativo ou ablativo plural; não há preposição antes dele, e quem conta histórias conta "a alguém": dativo, "aos marinheiros".'),
            ('<i>in īnsulā</i>?', '<i>In</i> + ablativo: lugar onde, "na ilha".'),
            ('<i>nārrant</i>: o que ele confirma?', 'Verbo em <i>-nt</i>: o sujeito é plural. <i>Poētae</i> é mesmo nominativo plural.'),
            ('Tradução.', '"Os poetas contam histórias aos marinheiros na ilha."'),
        ], 'Os grupos com preposição fecham-se sozinhos; as formas sem preposição esperam o verbo.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Caso e número', 'Diga o caso e o número da palavra destacada e sua função. Use o vocabulário do capítulo.', [
            ('<i>Rēgīna <b>epistulās</b> fīliābus dat.</i>', 'Acusativo plural: objeto direto de <i>dat</i>. A rainha dá cartas às filhas.'),
            ('<i>Rēgīna epistulās <b>fīliābus</b> dat.</i>', 'Dativo plural (forma especial de <i>fīlia</i>): destinatário. Não é ablativo, porque não há preposição e <i>dat</i> pede "a quem".'),
            ('<i>Poēta in <b>īnsulā</b> habitat.</i>', 'Ablativo singular, com <i>in</i>: lugar onde, sem movimento. O poeta mora na ilha.'),
            ('<i>Poēta ad <b>īnsulam</b> nāvigat.</i>', 'Acusativo singular, com <i>ad</i>: destino. O poeta navega até a ilha.'),
            ('<i>Fēminae <b>viās</b> spectant.</i>', 'Acusativo plural: objeto direto. As mulheres olham as ruas.'),
            ('<i><b>Agricolae</b> fīlia aquam portat.</i>', 'Genitivo singular: "do agricultor", ligado a <i>fīlia</i>. Não é nominativo plural: o verbo está no singular e <i>fīlia</i> já é o sujeito.'),
            ('<i>Puellae sine <b>pecūniā</b> sunt.</i>', 'Ablativo singular, com <i>sine</i>: as meninas estão sem dinheiro.'),
            ('<i>Nautae <b>patriam</b> amant.</i>', 'Acusativo singular: objeto direto. Os marinheiros amam a pátria.'),
        ]),
        exercicio('Exercício 2 · Preposição e caso', 'Complete com a forma correta do nome entre parênteses, conforme a preposição.', [
            ('<i>Puella cum ___ ambulat.</i> (amīca)', '<i>amīcā</i>: <i>cum</i> pede ablativo.'),
            ('<i>Nautae ad ___ nāvigant.</i> (patria)', '<i>patriam</i>: <i>ad</i> pede acusativo.'),
            ('<i>Agricola ex ___ aquam portat.</i> (silva)', '<i>silvā</i>: <i>ex</i> pede ablativo (origem).'),
            ('<i>Poēta in ___ ambulat.</i> (via) — "caminha pela rua, dentro dela"', '<i>viā</i>: sem movimento de entrada, <i>in</i> + ablativo. Se fosse "entra na rua", <i>in viam</i>.'),
            ('<i>Fēminae inter ___ sunt.</i> (puella, plural)', '<i>puellās</i>: <i>inter</i> pede acusativo.'),
            ('<i>Rēgīna prō ___ pecūniam dat.</i> (patria)', '<i>patriā</i>: <i>prō</i> pede ablativo ("pela pátria").'),
        ]),
        exercicio('Exercício 3 · Decline', 'Decline no singular e no plural, em voz alta e por escrito.', [
            ('<i>fīlia, -ae</i> (f.)', 'fīlia, fīliae, fīliae, fīliam, fīlia, fīliā; fīliae, fīliārum, fīli<b>ābus</b>, fīliās, fīliae, fīli<b>ābus</b>. A forma regular <i>fīliīs</i> também existe, mas <i>fīliābus</i> é a que evita a confusão com <i>fīliīs</i>, "aos filhos".'),
            ('<i>poēta, -ae</i> (m.)', 'poēta, poētae, poētae, poētam, poēta, poētā; poētae, poētārum, poētīs, poētās, poētae, poētīs. Masculino, mas as terminações são as de sempre.'),
        ]),
        exercicio('Exercício 4 · Do português para o latim', 'Traduza, usando só o vocabulário do capítulo. Verbos no presente, 3ª pessoa.', [
            ('A menina ama a lua.', '<i>Puella lūnam amat.</i>'),
            ('As filhas do agricultor moram na floresta.', '<i>Fīliae agricolae in silvā habitant.</i>'),
            ('O poeta dá rosas à rainha.', '<i>Poēta rēgīnae rosās dat.</i>'),
            ('Os marinheiros navegam da ilha até a pátria.', '<i>Nautae ex īnsulā ad patriam nāvigant.</i> (também <i>ab īnsulā</i>)'),
            ('A senhora conta uma história às amigas.', '<i>Domina amīcīs fābulam nārrat.</i>'),
        ]),
        exercicio('Exercício 5 · Singular e plural', 'Passe o grupo destacado para o número indicado e ajuste o que for necessário na frase.', [
            ('<i><b>Puella</b> in vīllā habitat.</i> → plural', '<i>Puellae in vīllā habitant.</i> O sujeito no plural leva o verbo ao plural (<i>-nt</i>).'),
            ('<i>Agricola <b>fīliae</b> rosam dat.</i> → plural ("às filhas")', '<i>Agricola fīliābus rosam dat.</i> O dativo plural de <i>fīlia</i> é <i>fīliābus</i>; o verbo não muda, porque o sujeito continua singular.'),
            ('<i>Nautae ex <b>īnsulā</b> nāvigant.</i> → plural', '<i>Nautae ex īnsulīs nāvigant.</i> Ablativo plural em <i>-īs</i>, ainda regido por <i>ex</i>.'),
            ('<i><b>Poētae</b> rēgīnam laudant.</i> → singular', '<i>Poēta rēgīnam laudat.</i> Sujeito singular, verbo em <i>-t</i>.'),
            ('<i>Fēmina <b>epistulās</b> portat.</i> → singular', '<i>Fēmina epistulam portat.</i> Só o objeto muda; o verbo concorda com o sujeito, não com o objeto.'),
        ]),
        exercicio('Exercício 6 · Leitura', 'Leia o texto em voz alta, duas vezes, e responda em português. Texto escrito para este capítulo, só com o vocabulário acima (e <i>et</i> = "e"; <i>nōn</i> = "não"; <i>magna</i> = grande; <i>pulchra</i> = bela; <i>Rōmāna</i> = romana; <i>Iūlia</i> = Júlia; <i>Ītalia</i> = Itália).<br><br><i lang="la">Iūlia est puella Rōmāna. Iūlia in vīllā cum fēminīs et puellīs habitat. Vīlla est magna et pulchra. Agricola, nauta et poēta in viā sunt. Poēta fābulās nārrat; puellae poētam laudant. Nautae ex Ītaliā ad īnsulās nāvigant et stellās spectant. Fīlia nautae epistulās ad vīllam portat. Iūlia epistulās amīcīs dat. Agricola terram amat et fīliābus aquam portat. Rēgīna patriae in vīllā nōn habitat.</i>', [
            ('Onde Júlia mora, e com quem?', 'Numa casa de campo (<i>in vīllā</i>), com as mulheres e as meninas (<i>cum fēminīs et puellīs</i>).'),
            ('Quem está na rua?', 'O agricultor, o marinheiro e o poeta (<i>agricola, nauta et poēta</i>): três masculinos da primeira declinação.'),
            ('O que as meninas fazem, e por quê?', 'Elogiam o poeta (<i>poētam laudant</i>), porque ele conta histórias.'),
            ('De onde partem os marinheiros, e para onde vão?', 'Da Itália (<i>ex Ītaliā</i>) para as ilhas (<i>ad īnsulās</i>).'),
            ('Que caso é <i>nautae</i> em "<i>Fīlia nautae epistulās ad vīllam portat</i>"?', 'Genitivo singular: a filha <b>do marinheiro</b>. O sujeito é <i>fīlia</i>, e o verbo está no singular.'),
            ('A quem o agricultor leva água, e qual é a forma especial?', 'Às filhas: <i>fīliābus</i>, dativo plural especial.'),
            ('A última frase é verdadeira sobre a rainha?', 'Diz que a rainha da pátria <b>não</b> mora na casa (<i>nōn habitat</i>). <i>Nōn</i> nega o verbo e fica antes dele.'),
        ]),
    ],
    leituras=['sonnenschein-ora-maritima-a-latin-story-for-beginners', 'jones-puer-romanus', 'appleton-fabulae-virginibus-puerisque-aut-narrandae-aut-recitandae', 'nutting-a-first-latin-reader', 'ravizza-gramatica-latina', 'greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc'],
    leituras_nota='Os primeiros capítulos de Ora Maritima usam quase só a primeira declinação e o presente: é a leitura ideal para esta semana. Puer Romanus e as Fabulae de Appleton vêm em seguida. As gramáticas são para consultar a tabela.',
)
