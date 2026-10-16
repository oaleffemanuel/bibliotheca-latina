from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# In Catilinam I, 1–2, edição de A. C. Clark (Oxford, 1908), conferida no Perseus (1999.02.0010)
# e na The Latin Library (cicero/cat1.shtml). Ortografia de Clark (voltūs, cōnsilī); macrons acrescentados.
P1 = ('Quō usque tandem abūtēre, Catilīna, patientiā nostrā? Quam diū etiam furor iste tuus nōs ēlūdet? '
      'Quem ad fīnem sēsē effrēnāta iactābit audācia? Nihilne tē nocturnum praesidium Palātī, nihil urbis vigiliae, '
      'nihil timor populī, nihil concursus bonōrum omnium, nihil hīc mūnītissimus habendī senātūs locus, '
      'nihil hōrum ōra voltūsque mōvērunt? Patēre tua cōnsilia nōn sentīs, cōnstrictam iam hōrum omnium scientiā '
      'tenērī coniūrātiōnem tuam nōn vidēs? Quid proximā, quid superiōre nocte ēgeris, ubi fueris, quōs convocāveris, '
      'quid cōnsilī cēperis, quem nostrum ignōrāre arbitrāris?')
P2 = ('Ō tempora, ō mōrēs! Senātus haec intellegit, cōnsul videt; hīc tamen vīvit. Vīvit? Immō vērō etiam in senātum '
      'venit, fit pūblicī cōnsilī particeps, notat et dēsignat oculīs ad caedem ūnum quemque nostrum. Nōs autem, '
      'fortēs virī, satis facere reī pūblicae vidēmur, sī istīus furōrem ac tēla vītāmus. Ad mortem tē, Catilīna, '
      'dūcī iussū cōnsulis iam prīdem oportēbat, in tē cōnferrī pestem quam tū in nōs omnīs iam diū māchināris.')
TEXTO = tabela(['§', 'Cícero, <i>In Catilīnam</i> I, 1–2'], [['1', f'<span lang="la">{P1}</span>'], ['2', f'<span lang="la">{P2}</span>']],
               'Texto latino: ed. A. C. Clark (Oxford, 1908), domínio público; macrons deste livro', latim_cols=(1,))

LICAO = dict(
    slug='48-cicero', titulo='Cícero: a Primeira Catilinária', titulo_latim='Cicerō', tempo='90 min',
    resumo='Leitura comentada do exórdio da Primeira Catilinária (In Catilinam I, 1–2): "Quō usque tandem abūtēre, Catilīna, patientiā nostrā?". O contexto de 8 de novembro de 63 a.C., texto da edição Clark, vocabulário e notas, o depoente abūtor com ablativo e o futuro em -ēre, as figuras da oratória (perguntas retóricas, anáfora, trícolon, assíndeto, Ō tempora, ō mōrēs) e a análise de dois períodos.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['Cícero', 'Catilinárias', 'leitura comentada', 'oratória', 'exórdio', 'abūtor + ablativo', 'futuro em -ēre (2ª sing. passiva)', 'depoentes', 'pergunta retórica', 'anáfora', 'trícolon', 'assíndeto', 'acusativo de exclamação', 'correção (immō vērō)', 'iste depreciativo', 'genitivo partitivo (quid cōnsilī, quem nostrum)', 'gerundivo (habendī senātūs)', 'interrogativas indiretas antecipadas', 'videor pessoal', 'oportēbat + infinitivo presente', 'período ciceroniano'],
    prerequisitos=dict(texto='Capítulo 39 (o período complexo, que já analisou um período de Cícero), que traz consigo o discurso indireto, a interrogativa indireta e a oração infinitiva (capítulos 28, 35 e 38). Usamos também as figuras de linguagem (capítulo 40), os depoentes (capítulo 25), a 2ª pessoa passiva em -re (capítulo 23), o gerundivo (capítulo 31) e os demonstrativos, inclusive iste (capítulo 15).',
                       licoes=['39-o-periodo-complexo', '25-verbos-depoentes', '35-a-interrogativa-indireta', '28-a-oracao-infinitiva']),
    referencias=[
        referencia('Cícero, In Catilinam I, 1–2, ed. A. C. Clark (Oxford, Clarendon Press, 1908)', 'Marco Túlio Cícero', catalogo='cicero-in-catilinam-i-iv', url='https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0010:text=Catil.:speech=1:chapter=1', nota='texto da leitura, conferido no Perseus, com o aparato crítico de Clark; ortografia de Clark (voltūs, cōnsilī); macrons acrescentados por este livro', tipo='dominio_publico'),
        referencia('Cícero, In Catilinam I (The Latin Library)', None, catalogo='the-latin-library', url='https://www.thelatinlibrary.com/cicero/cat1.shtml', nota='segunda conferência: lê vītēmus por vītāmus e cōnsiliī por cōnsilī, e põe entre colchetes [omnēs iam diū]', tipo='dominio_publico'),
        referencia('In Catilinam I, com notas e vocabulário', 'John Henderson', catalogo='henderson-in-catilinam-i-com-notas-e-vocabulario', nota='edição escolar recomendada para continuar a leitura', tipo='dominio_publico'),
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 96 (terminação -re da 2ª sing. passiva), § 106 (futuro regēris ou -re), § 113 (depoentes), § 176.2.b (nihil como acusativo interno), § 183 (acusativo de exclamação: Ō fallācem spem), § 201.2 (genitivo partitivo com neutros: quid cōnsilī), § 218.1 (ūtor e compostos com ablativo), § 242.2 (nostrum como genitivo partitivo), § 246.4 (iste com desprezo), § 270.2 (oportēbat + infinitivo presente: "devia ter"), § 300 (interrogativa indireta), § 331 (acusativo com infinitivo depois de sentiō, videō, arbitror), § 332 (videor pessoal), § 339.1 (gerundivo em lugar do gerúndio com objeto), § 346 (assíndeto), § 349 (ordem enfática), § 350.11 (anáfora e hipérbato como recursos de ênfase)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 190 (depoentes), § 397.d (acusativo em exclamações), § 410 e notas (ūtor, fruor, fungor, potior, vescor e compostos com ablativo; origem instrumental; acusativo no latim arcaico), §§ 573–574 (interrogativa indireta), § 598 (ordem das palavras e ênfase; 598.f anáfora e quiasmo), §§ 600–601 (estrutura do período)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='nn. 484–490 (discurso direto e indireto; as subordinadas no subjuntivo), úteis para as interrogativas indiretas do § 1', tipo='dominio_publico'),
    ],
    objetivos=[
        'Situar a Primeira Catilinária no seu momento histórico (8 de novembro de 63 a.C.) e reconhecer a função do exórdio.',
        'Ler e traduzir In Catilinam I, 1–2 com apoio das notas.',
        'Explicar <i>abūtēre … patientiā nostrā</i>: depoente composto de <i>ūtor</i>, regência do ablativo e futuro em <i>-ēre</i>.',
        'Identificar e nomear as figuras do trecho (pergunta retórica, anáfora, trícolon, assíndeto, exclamação, correção) e dizer o que cada uma faz no discurso.',
        'Analisar um período ciceroniano com interrogativas indiretas antecipadas e encaixadas numa oração infinitiva.',
    ],
    secoes=[
        ('Cícero, Catilina e o 8 de novembro de 63 a.C.', f'''
<p>Marco Túlio Cícero (<i>Mārcus Tullius Cicerō</i>, 106–43 a.C.) foi o maior orador de Roma e, para a posteridade, o modelo da prosa latina. Nascido em Arpino, sem antepassados no senado (um <i>homō novus</i>), chegou ao consulado em 63 a.C. graças à advocacia e à palavra. Foi nesse ano que enfrentou Lúcio Sérgio Catilina, nobre arruinado e derrotado nas eleições, que reuniu endividados, veteranos e jovens aristocratas numa conspiração para tomar o poder.</p>
<p>No fim de outubro o senado já havia dado aos cônsules poderes de emergência. Na noite de 6 para 7 de novembro os conjurados se reuniram e combinaram, entre outras coisas, matar Cícero na manhã seguinte; o atentado falhou porque o cônsul fora avisado. No dia 8, Cícero convocou o senado no templo de Júpiter Estator, ao pé do Palatino, sob forte guarda, e Catilina teve a audácia de comparecer. O discurso que lemos começa sem nenhuma das fórmulas de cortesia habituais: Cícero se volta diretamente para o acusado. Na mesma noite, Catilina deixou Roma para juntar-se às suas tropas na Etrúria.</p>
<p>O que temos é a versão escrita, revista e publicada por Cícero alguns anos depois, em 60 a.C., junto com os outros discursos do seu consulado. O começo, conhecido de cor por gerações de estudantes, é um exórdio <i>ex abruptō</i>: em vez de preparar os ouvintes, ataca.</p>
{observacao('Sobre o texto', 'Seguimos a edição de A. C. Clark (Oxford, 1908), conferida no Perseus, com a ortografia dela (<i>voltūs</i> por <i>vultūs</i>, <i>cōnsilī</i> por <i>cōnsiliī</i>); os macrons foram acrescentados por este livro. A The Latin Library traz algumas variantes: <i>vītēmus</i> (subjuntivo) por <i>vītāmus</i>, <i>cōnsiliī</i>, e <i>omnēs iam diū</i> entre colchetes. O aparato de Clark mostra que os próprios manuscritos se dividem em <i>vītāmus/vītēmus</i> e em <i>omnēs iam diū</i>; <i>cōnsilī/cōnsiliī</i> é questão de ortografia. Nenhuma dessas diferenças altera o sentido do trecho. A edição de Clark (que morreu em 1937) está em domínio público.')}
'''),
        ('O texto e a tradução', f'''
<p>Leia o texto em voz alta, como um discurso: as perguntas pedem entonação de pergunta, e as repetições só funcionam ouvidas.</p>
{TEXTO}
<p>Tradução deste livro:</p>
<p>[1] Até quando, afinal, Catilina, abusarás da nossa paciência? Por quanto tempo ainda esse teu furor zombará de nós? Até que limite vai se exibir essa audácia sem freio? Nada te abalaram a guarda noturna do Palatino, nada as sentinelas da cidade, nada o medo do povo, nada a afluência de todos os homens de bem, nada este lugar fortificadíssimo escolhido para a reunião do senado, nada o rosto e o semblante destes que aqui estão? Não percebes que os teus planos estão descobertos, não vês que a tua conjuração já está presa e dominada pelo conhecimento de todos estes? O que fizeste na noite passada, o que na anterior, onde estiveste, quem convocaste, que decisão tomaste: qual de nós julgas que ignora isso?</p>
<p>[2] Ó tempos, ó costumes! O senado sabe destas coisas, o cônsul as vê; e este homem, no entanto, vive. Vive? Mais ainda: vem até ao senado, toma parte no conselho público, marca e aponta com os olhos para a morte cada um de nós. E nós, homens valentes, achamos que cumprimos o nosso dever para com a república se nos esquivamos do furor e das armas desse homem. À morte, Catilina, há muito tempo devias ter sido levado por ordem do cônsul; contra ti devia ter sido lançada a ruína que tu, há tanto tempo, tramas contra todos nós.</p>
{dica('<b>Traduzir oratória.</b> A tradução mantém as repetições (<i>nada … nada …</i>) e a ordem das perguntas, mesmo quando o português ficaria mais "limpo" sem elas: neste texto, a forma é o argumento. Onde o latim usa o pronome de desprezo <i>iste</i>, o português pede "esse", com o tom de quem aponta.')}
'''),
        ('Vocabulário e notas', f'''
{tabela(['§', 'Palavra ou expressão', 'Nota'], [
    ['1', 'quō usque tandem', '"até onde, até quando"; <i>tandem</i> nas perguntas exprime impaciência: "afinal", "de uma vez".'],
    ['1', 'abūtēre … patientiā nostrā', '<i>abūtor, abūtī, abūsus sum</i>, "usar até o fim, abusar de", com ablativo; <i>abūtēre</i> é futuro, 2ª sing. (seção 4).'],
    ['1', 'furor iste tuus', '<i>iste</i>, "esse (teu)", com nuance de desprezo (Bennett § 246.4); <i>tuus</i> reforça: o furor é de Catilina.'],
    ['1', 'nōs ēlūdet', '<i>ēlūdō</i>, "zombar de, iludir"; futuro.'],
    ['1', 'sēsē effrēnāta iactābit audācia', '<i>sē iactāre</i>, "agitar-se, exibir-se"; <i>effrēnātus</i>, "sem freio" (<i>frēnum</i>, freio). Sujeito no fim: <i>audācia</i>.'],
    ['1', 'nihilne … mōvērunt', '<i>nihil</i> como advérbio, "em nada", repetido seis vezes; <i>-ne</i> marca a pergunta. O verbo, no plural, só chega depois dos seis sujeitos.'],
    ['1', 'praesidium Palātī', '<i>praesidium</i>, "guarda, posto armado"; <i>Palātī</i>, genitivo de <i>Palātium</i> (forma em <i>-ī</i>).'],
    ['1', 'concursus bonōrum omnium', '<i>concursus, -ūs</i>, "afluência"; <i>bonī</i>, "os homens de bem", termo político: os cidadãos leais à ordem.'],
    ['1', 'habendī senātūs locus', '"lugar de reunir o senado": gerundivo no genitivo, concordando com <i>senātūs</i> (Bennett § 339.1; capítulo 31). O templo de Júpiter Estator, guardado por tropas: daí <i>mūnītissimus</i>.'],
    ['1', 'hōrum ōra voltūsque', '<i>hōrum</i>, "destes" (os senadores presentes); <i>voltus</i> = <i>vultus</i>, "expressão do rosto". Cícero aponta para a plateia.'],
    ['1', 'patēre tua cōnsilia nōn sentīs', 'oração infinitiva depois de <i>sentīs</i> (capítulo 28; Bennett § 331): "não percebes que os teus planos estão à vista". <i>Pateō</i>, "estar aberto, descoberto".'],
    ['1', 'cōnstrictam … tenērī coniūrātiōnem tuam', 'outra oração infinitiva, depois de <i>vidēs</i>: "que a tua conjuração está presa, amarrada"; <i>scientiā</i>, ablativo de meio.'],
    ['1', 'quid proximā, quid superiōre nocte ēgeris …', 'quatro interrogativas indiretas no subjuntivo perfeito (<i>ēgeris, fueris, convocāveris, cēperis</i>) que dependem de <i>ignōrāre</i>, no fim (seção 6). <i>Superiōre nocte</i>, "na noite anterior".'],
    ['1', 'quid cōnsilī', '"que decisão": genitivo partitivo com o neutro <i>quid</i> (Bennett § 201.2, que cita justamente <i>quid cōnsilī</i>).'],
    ['1', 'quem nostrum', '"qual de nós": <i>nostrum</i> é o genitivo partitivo do pronome (Bennett § 242.2), não o possessivo.'],
    ['2', 'Ō tempora, ō mōrēs!', 'acusativos de exclamação (Bennett § 183; A&amp;G § 397.d): "que tempos, que costumes!"'],
    ['2', 'hīc tamen vīvit', '<i>hīc</i>, pronome: "este homem". O advérbio <i>hīc</i>, "aqui", tem a mesma grafia; aqui é o pronome, porque é o sujeito de <i>vīvit</i>.'],
    ['2', 'immō vērō', '"mais ainda, ou melhor": corrige o que veio antes, para mais.'],
    ['2', 'fit … particeps', '<i>fīō</i>, "tornar-se"; <i>particeps, -cipis</i>, "participante", + genitivo.'],
    ['2', 'ūnum quemque nostrum', '"cada um de nós"; <i>nostrum</i> partitivo, como acima.'],
    ['2', 'satis facere reī pūblicae vidēmur', '<i>satis faciō</i> + dativo, "cumprir o dever para com"; <i>vidēmur</i> + infinitivo, construção pessoal: "parecemos cumprir", isto é, "achamos que cumprimos" (Bennett § 332; capítulo 28).'],
    ['2', 'istīus furōrem ac tēla', '<i>istīus</i>, genitivo de <i>iste</i>, de novo com desprezo; <i>tēlum</i>, "arma de arremesso, arma".'],
    ['2', 'dūcī … oportēbat', '<i>oportet</i>, "é necessário", com oração infinitiva passiva (<i>tē dūcī</i>). O imperfeito <i>oportēbat</i> com infinitivo presente vale "devia ter (sido)" (Bennett § 270.2).'],
    ['2', 'iussū cōnsulis', '<i>iussū</i>, ablativo de <i>iussus</i> (4ª declinação, só neste caso): "por ordem do cônsul".'],
    ['2', 'pestem quam … māchināris', '<i>pestis</i>, "peste, ruína"; <i>māchinor</i> (depoente), "tramar"; <i>māchināris</i>, presente, 2ª sing.'],
], 'Notas a In Catilinam I, 1–2', latim_cols=(1,))}
'''),
        ('Abūtor e o futuro em -ēre', f'''
<p>A primeira frase do discurso concentra uma lição de morfologia. <i>Abūtor</i> é um verbo depoente (capítulo 25): forma passiva, sentido ativo. É composto de <i>ūtor</i>, "usar", que pede ablativo, e herda essa regência, como os demais compostos dos cinco depoentes com ablativo (<i>ūtor, fruor, fungor, potior, vescor</i>; Bennett § 218.1; A&amp;G § 410). Por isso o "objeto" do abuso está no ablativo: <i>patientiā nostrā</i>, e não <i>patientiam nostram</i>. O prefixo <i>ab-</i> dá a ideia de "usar até gastar", e daí "abusar".</p>
<p>A forma <i>abūtēre</i> é a 2ª pessoa do singular. Como você viu no capítulo 23, a 2ª pessoa singular passiva tem duas terminações, <i>-ris</i> e <i>-re</i> (Bennett § 96), e os depoentes, que se conjugam como passivos, também as têm. Num verbo da 3ª conjugação, o que distingue presente e futuro nessa pessoa é apenas a quantidade da vogal:</p>
{comparacao('Abūtor, 2ª pessoa do singular', ['Forma', 'Tempo', 'Tradução'], [
    ['abūt<b>eris</b> / abūt<b>ere</b>', 'presente (vogal breve)', 'abusas'],
    ['abūt<b>ēris</b> / abūt<b>ēre</b>', 'futuro (vogal longa)', 'abusarás'],
    ['abūt<b>ēbāris</b> / abūt<b>ēbāre</b>', 'imperfeito', 'abusavas'],
    ['abūt<b>ere</b>!', 'imperativo (igual ao presente em -re)', 'abusa!'],
])}
<p>Nos manuscritos e nas edições sem macrons, <i>abutere</i> é ambíguo. Por que futuro? Pelo sentido e pelo paralelo: a pergunta seguinte tem <i>ēlūdet</i> e a terceira <i>iactābit</i>, ambos futuros. Cícero não pergunta "até quando abusas", mas "até quando continuarás a abusar": o futuro projeta a paciência do senado, já gasta, para a frente. Bennett registra o padrão nos paradigmas: <i>regēris, or -re</i> no futuro (§ 106).</p>
<p>O trecho tem outros depoentes, todos no presente e na 2ª pessoa com <i>-ris</i>: <i>arbitrāris</i> ("julgas", de <i>arbitror</i>) e <i>māchināris</i> ("tramas", de <i>māchinor</i>). Compare as três formas lado a lado e note que a terminação <i>-ris</i> ou <i>-re</i>, num verbo depoente, nunca é passiva no sentido.</p>
{observacao('Por que ablativo?', 'A&amp;G (§ 410, nota) explica que o ablativo destes verbos é, na origem, um ablativo de meio: <i>ūtor</i> + ablativo significava "sirvo-me por meio de". No latim arcaico (Terêncio, por exemplo) esses verbos às vezes aparecem com acusativo (§ 410, nota 1 à alínea a); na prosa clássica a regra é o ablativo, e é ela que você deve aplicar ao ler e ao escrever.')}
'''),
        ('A retórica do exórdio', f'''
<p>A Primeira Catilinária é o texto escolar clássico para estudar as figuras da oratória porque as usa todas de uma vez e com função clara: isolar Catilina, mostrar que ele foi descoberto e envergonhar o próprio senado pela inércia. O capítulo 40 apresentou as principais figuras; aqui elas aparecem em ação. Nas gramáticas de referência, Bennett trata da anáfora e do hipérbato entre os recursos de ênfase (§ 350.11), do assíndeto no § 346 e de outras figuras nos §§ 374–375; A&amp;G registra a anáfora no § 598.f. O trícolon e a correção não têm parágrafo próprio nessas gramáticas: os nomes são os da tradição retórica escolar, e as definições, as mais simples possíveis.</p>
{tabela(['Figura', 'Onde', 'O que faz'], [
    ['<b>Pergunta retórica</b>: pergunta que não espera resposta, porque a resposta é óbvia', '<i>Quō usque tandem…? Quam diū…? Quem ad fīnem…?</i>', 'acusa sem afirmar: obriga o ouvinte (e o acusado) a responder mentalmente "basta".'],
    ['<b>Trícolon</b>: três membros paralelos', 'as três perguntas iniciais', 'diz a mesma coisa três vezes com palavras diferentes (<i>quō usque, quam diū, quem ad fīnem</i>; <i>patientia, furor, audācia</i>), martelando a ideia.'],
    ['<b>Anáfora</b>: a mesma palavra no início de membros sucessivos', '<i>nihil … nihil … nihil …</i> (seis vezes); <i>quid … quid …</i>', 'enumera todas as defesas da cidade, do mais distante (o Palatino) ao mais próximo (o rosto dos senadores), em gradação.'],
    ['<b>Assíndeto</b>: coordenação sem conjunção', '<i>Senātus haec intellegit, cōnsul videt; hīc tamen vīvit.</i>', 'frases curtas, secas, em sequência rápida (Bennett § 346).'],
    ['<b>Exclamação</b>', '<i>Ō tempora, ō mōrēs!</i>', 'interrompe a argumentação com indignação; gramaticalmente, acusativo de exclamação.'],
    ['<b>Correção</b> (lat. <i>correctiō</i>): retomar uma palavra para corrigi-la, em geral para mais', '<i>Vīvit? Immō vērō etiam in senātum venit…</i>', 'faz a indignação crescer: não só vive, como vem ao senado, e não só vem, como marca as vítimas.'],
    ['<b>Antítese</b>', '<i>Nōs autem fortēs virī …</i> × <i>tū</i>; <i>in tē</i> × <i>in nōs</i>', 'opõe a passividade dos senadores (com ironia em <i>fortēs virī</i>) à ação de Catilina; a pena que deveria cair <i>in tē</i> é a que ele trama <i>in nōs</i>.'],
], 'Figuras de In Catilinam I, 1–2')}
<p>A ordem das palavras também é retórica. O latim põe no início o que quer destacar (Bennett § 349; A&amp;G § 598): <i>Ad mortem tē, Catilīna, dūcī … oportēbat</i> abre com "à morte"; e na terceira pergunta o sujeito <i>audācia</i> é guardado para o fim, depois de <i>sēsē effrēnāta iactābit</i>, como um golpe final. Observe ainda o uso dos demonstrativos: <i>hīc</i> e <i>hōrum</i> apontam para o que está diante de todos (o lugar, os senadores); <i>iste</i> e <i>istīus</i> apontam para Catilina, com desprezo.</p>
{exemplos([
    ('Nihil<b>ne</b> tē nocturnum praesidium Palātī, <b>nihil</b> urbis vigiliae, <b>nihil</b> timor populī …', 'Nada te abalaram a guarda noturna do Palatino, nada as sentinelas da cidade, nada o medo do povo… (anáfora em gradação)'),
    ('<b>Vīvit?</b> Immō vērō etiam in senātum venit.', 'Vive? Mais ainda: vem até ao senado. (correção)'),
])}
'''),
        ('O período ciceroniano: suspender o sentido', f'''
<p>A&amp;G (§ 600) define o período como a frase em que "o sentido é expresso pelo todo e fica em suspenso até a última palavra". O capítulo 39 ensinou a ler esses períodos: identificar o verbo principal (muitas vezes no fim), separar as subordinadas, ver de que cada uma depende. A última pergunta do § 1 é um exemplo perfeito, porque o que vem primeiro depende do que vem por último.</p>
{exemplos([('Quid proximā, quid superiōre nocte ēgeris, ubi fueris, quōs convocāveris, quid cōnsilī cēperis, quem nostrum ignōrāre arbitrāris?', 'O que fizeste na noite passada, o que na anterior, onde estiveste, quem convocaste, que decisão tomaste: qual de nós julgas que ignora isso?')])}
{diagrama_frase([('quid … ēgeris …', 'interrog. indiretas · objeto de ignōrāre'), ('quem nostrum', 'sujeito do infinitivo · qual de nós'), ('ignōrāre', 'infinitivo · ignora'), ('arbitrāris', 'verbo principal · julgas')], 'Três níveis: as interrogativas indiretas dependem de <i>ignōrāre</i>, que é o infinitivo de uma oração infinitiva dependente de <i>arbitrāris</i>.')}
<p>Leia de trás para a frente para entender, e de frente para trás para sentir. O verbo principal é <i>arbitrāris</i>, "julgas", que pede uma oração infinitiva (capítulo 28): o seu sujeito no acusativo é <i>quem</i> (interrogativo: "quem … julgas que ignora?"), especificado pelo partitivo <i>nostrum</i>, e o seu verbo é <i>ignōrāre</i>. O objeto de <i>ignōrāre</i> são as quatro interrogativas indiretas (capítulo 35), no subjuntivo perfeito porque o verbo de que dependem está no presente (sequência primária) e os fatos são anteriores. Cícero as põe todas na frente, em anáfora, como uma lista de acusações; só a última linha revela que a pergunta é outra: "quem de nós não sabe?". O efeito é dizer a Catilina, sem afirmá-lo, que tudo foi descoberto.</p>
<p>O outro grande período do trecho fecha o § 2. Aqui a dificuldade é diferente: um verbo impessoal (<i>oportēbat</i>) com duas orações infinitivas passivas coordenadas sem conjunção.</p>
{analise('In Catilinam I, 2 (final), palavra a palavra', [
    ('Ad mortem', 'ad (prep. + ac.); mors, mortis (f.), morte', 'acusativo singular', 'direção: "à morte"; posto em destaque no início'),
    ('tē', 'tū, tuī', 'acusativo singular', 'sujeito do infinitivo <i>dūcī</i>'),
    ('Catilīna', 'Catilīna, -ae (m.)', 'vocativo', 'chamamento'),
    ('dūcī', 'dūcō, -ere, dūxī, ductum, levar', 'infinitivo presente passivo', 'verbo da 1ª oração infinitiva'),
    ('iussū', 'iussus, -ūs (m.), ordem (só no ablativo)', 'ablativo singular', 'causa: "por ordem"'),
    ('cōnsulis', 'cōnsul, -is (m.)', 'genitivo singular', 'complemento de <i>iussū</i>'),
    ('iam prīdem', 'advérbios', 'invariáveis', '"já há muito tempo"'),
    ('oportēbat', 'oportet, -ēre, oportuit (impessoal), é preciso', 'imperfeito do indicativo, 3ª sing.', 'verbo principal; com infinitivo presente = "devia ter (sido)"'),
    ('in tē', 'in (prep. + ac.); tū', 'acusativo', 'direção hostil: "contra ti"'),
    ('cōnferrī', 'cōnferō, -ferre, -tulī, collātum, lançar, dirigir', 'infinitivo presente passivo', 'verbo da 2ª oração infinitiva (assíndeto)'),
    ('pestem', 'pestis, -is (f.), ruína, peste', 'acusativo singular', 'sujeito de <i>cōnferrī</i>; antecedente de <i>quam</i>'),
    ('quam', 'quī, quae, quod', 'acusativo singular feminino', 'objeto de <i>māchināris</i>'),
    ('tū', 'tū', 'nominativo', 'sujeito de <i>māchināris</i>, expresso por contraste (<i>tē</i> × <i>tū</i>)'),
    ('in nōs omnīs', 'in; nōs; omnis, -e', 'acusativo plural (<i>omnīs</i> = <i>omnēs</i>)', '"contra todos nós"'),
    ('iam diū', 'advérbios', 'invariáveis', '"há tanto tempo"'),
    ('māchināris', 'māchinor, -ārī, māchinātus sum (depoente), tramar', 'presente do indicativo, 2ª sing.', 'verbo da relativa'),
])}
<p>Repare na simetria: <i>ad mortem tē … dūcī</i> / <i>in tē cōnferrī pestem</i>; e na volta final, em que a ruína que Catilina prepara <i>in nōs omnīs</i> deveria cair <i>in tē</i>. Para o tempo verbal, siga Bennett § 270.2: o latim usa o passado de <i>oportet</i> (ou de <i>dēbeō</i>, <i>possum</i>) com o infinitivo presente onde o português diz "devia ter sido".</p>
'''),
    ],
    erros_comuns=[
        ('Ler <i>abūtēre</i> como infinitivo ativo.', '<i>Abūtor</i> é depoente: o infinitivo é <i>abūtī</i>. A forma em <i>-ēre</i> é a 2ª pessoa do singular (futuro), alternativa a <i>abūtēris</i>. O vocativo <i>Catilīna</i> logo depois confirma que Cícero fala com alguém: "tu abusarás".'),
        ('Tomar <i>patientiā nostrā</i> como sujeito.', 'É ablativo (<i>-ā</i> longo), regido por <i>abūtor</i>. Em português o complemento vem com "de" ("abusar da paciência"), mas em latim não há preposição: a regência está no verbo.'),
        ('Traduzir <i>Quid … ēgeris, ubi fueris …</i> como perguntas diretas.', 'O subjuntivo perfeito mostra que são interrogativas indiretas, que dependem de <i>ignōrāre</i> no fim do período. Pontuar como perguntas soltas ("O que fizeste? Onde estiveste?") é aceitável numa tradução livre, mas a análise precisa reconhecer a dependência.'),
        ('Ler <i>quem nostrum</i> como "quem nosso" ou <i>nostrum</i> como possessivo.', '<i>Nostrum</i> aqui é genitivo partitivo do pronome <i>nōs</i> (Bennett § 242.2): "qual de nós". O possessivo neutro <i>nostrum</i> concordaria com um nome neutro, que não existe na frase.'),
        ('Traduzir <i>oportēbat</i> por "devia" no presente ou por "era preciso" sem consequência.', '<i>Iam prīdem oportēbat</i> + infinitivo presente refere-se a algo que deveria ter acontecido e não aconteceu: "há muito tempo devias ter sido levado" (Bennett § 270.2).'),
        ('Ler <i>hīc</i> como o advérbio "aqui" em <i>hīc tamen vīvit</i>.', 'O pronome <i>hīc</i> e o advérbio <i>hīc</i> têm a mesma grafia, e só a construção os distingue. Em <i>hīc tamen vīvit</i>, a palavra é sujeito de <i>vīvit</i>: "este homem vive"; o advérbio "aqui" não pode ser sujeito. No § 1, <i>hīc … locus</i> também é o pronome, concordando com <i>locus</i>.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Nihilne … mōvērunt',
            'Analise o período <i lang="la">Nihilne tē nocturnum praesidium Palātī, nihil urbis vigiliae, nihil timor populī, nihil concursus bonōrum omnium, nihil hīc mūnītissimus habendī senātūs locus, nihil hōrum ōra voltūsque mōvērunt?</i>', [
            ('Onde está o verbo e em que número?', 'No fim: <i>mōvērunt</i>, perfeito de <i>moveō</i>, 3ª pessoa do plural. É plural porque tem vários sujeitos coordenados.'),
            ('Quais são os sujeitos?', 'Seis grupos no nominativo: <i>praesidium</i>, <i>vigiliae</i>, <i>timor</i>, <i>concursus</i>, <i>locus</i>, <i>ōra voltūsque</i>. Cada um vem precedido de <i>nihil</i>.'),
            ('Qual é o objeto?', '<i>Tē</i>, acusativo, logo no início: "a ti". Catilina é o alvo de tudo o que segue.'),
            ('E <i>nihil</i>? É sujeito?', 'Não: os sujeitos já estão preenchidos e o verbo tem objeto (<i>tē</i>). <i>Nihil</i> funciona como advérbio, "em nada" (Bennett § 176.2.b). O <i>-ne</i> do primeiro <i>nihil</i> faz da frase uma pergunta retórica.'),
            ('Monte a tradução.', '"Nada te abalaram a guarda noturna do Palatino, as sentinelas da cidade, o medo do povo, a afluência de todos os homens de bem, este lugar fortificadíssimo de reunião do senado, o rosto e o semblante destes que aqui estão?" Para manter a anáfora: "Nada te abalou a guarda…, nada as sentinelas…, nada…".'),
        ], 'A gradação vai de fora para dentro: das guardas da cidade até os rostos dos senadores que Catilina tem diante de si naquele momento.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Compreensão', 'Responda em português.', [
            ('Que elementos do § 1 mostram que o senado estava reunido num lugar protegido?', '<i>Nocturnum praesidium Palātī</i>, <i>urbis vigiliae</i> e <i>hīc mūnītissimus habendī senātūs locus</i>: a sessão ocorria sob guarda armada, num templo escolhido por ser defensável.'),
            ('O que Cícero diz saber a respeito de Catilina?', 'O que ele fez nas duas últimas noites, onde esteve, quem reuniu e o que decidiu (<i>quid proximā, quid superiōre nocte ēgeris…</i>): a reunião dos conjurados foi descoberta.'),
            ('Qual é a crítica que Cícero faz ao próprio senado no § 2?', 'Que os senadores, "homens valentes" (com ironia), se contentam em esquivar-se do furor de Catilina em vez de puni-lo (<i>satis facere reī pūblicae vidēmur, sī istīus furōrem ac tēla vītāmus</i>).'),
            ('Que pena Cícero diz que Catilina já merecia?', 'A morte, por ordem do cônsul (<i>ad mortem tē … dūcī iussū cōnsulis … oportēbat</i>).'),
        ]),
        exercicio('Exercício 2 · Morfologia', 'Identifique a forma e dê o verbete.', [
            ('<i>abūtēre</i>', 'Futuro do indicativo, 2ª sing., do depoente <i>abūtor, abūtī, abūsus sum</i>; variante de <i>abūtēris</i>.'),
            ('<i>iactābit</i>', 'Futuro do indicativo ativo, 3ª sing.; <i>iactō, -āre</i>, "agitar, lançar".'),
            ('<i>mōvērunt</i>', 'Perfeito do indicativo ativo, 3ª pl.; <i>moveō, -ēre, mōvī, mōtum</i>.'),
            ('<i>cēperis</i>', 'Perfeito do subjuntivo ativo, 2ª sing.; <i>capiō, -ere, cēpī, captum</i>. Subjuntivo de interrogativa indireta.'),
            ('<i>arbitrāris</i>', 'Presente do indicativo, 2ª sing., do depoente <i>arbitror, -ārī, arbitrātus sum</i>, "julgar".'),
            ('<i>vidēmur</i>', 'Presente do indicativo passivo, 1ª pl., de <i>videō</i>; na construção pessoal, "parecemos".'),
        ]),
        exercicio('Exercício 3 · Sintaxe', 'Explique a construção destacada.', [
            ('<i>abūtēre … <b>patientiā nostrā</b></i>', 'Ablativo regido por <i>abūtor</i>, composto de <i>ūtor</i> (Bennett § 218.1; A&amp;G § 410).'),
            ('<i><b>Ō tempora, ō mōrēs!</b></i>', 'Acusativos de exclamação (Bennett § 183): nomes no acusativo, com <i>ō</i>, exprimindo indignação.'),
            ('<i>nihil hīc mūnītissimus <b>habendī senātūs</b> locus</i>', 'Gerundivo no genitivo concordando com <i>senātūs</i>, em lugar do gerúndio com objeto (<i>habendī senātum</i>): "lugar de reunir o senado" (Bennett § 339.1).'),
            ('<i><b>Patēre tua cōnsilia</b> nōn sentīs</i>', 'Oração infinitiva objeto de <i>sentīs</i>: sujeito <i>cōnsilia</i> (acusativo neutro plural), verbo <i>patēre</i> (Bennett § 331).'),
            ('<i>Nōs … satis facere reī pūblicae <b>vidēmur</b></i>', 'Construção pessoal de <i>videor</i> com infinitivo (Bennett § 332): o sujeito de <i>vidēmur</i> é o mesmo do infinitivo. Em português: "achamos que cumprimos" ou "parece que cumprimos".'),
        ]),
        exercicio('Exercício 4 · Retórica', 'Nomeie a figura e diga o efeito.', [
            ('<i>Quō usque tandem…? Quam diū etiam…? Quem ad fīnem…?</i>', 'Trícolon de perguntas retóricas: três perguntas paralelas que dizem quase a mesma coisa e não esperam resposta; insistem na impaciência.'),
            ('<i>Senātus haec intellegit, cōnsul videt; hīc tamen vīvit.</i>', 'Assíndeto: três orações curtas sem conjunção, com <i>tamen</i> marcando o contraste final. Efeito de secura e escândalo.'),
            ('<i>Vīvit? Immō vērō etiam in senātum venit.</i>', 'Correção: Cícero retoma <i>vīvit</i> em forma de pergunta e o corrige para mais, aumentando a indignação.'),
            ('<i>in tē cōnferrī pestem quam tū in nōs omnīs … māchināris</i>', 'Antítese (<i>in tē</i> × <i>in nōs</i>; <i>tē</i> × <i>tū</i>): a ruína tramada por Catilina deveria voltar-se contra ele.'),
        ]),
        exercicio('Exercício 5 · Retroversão', 'Passe para o latim, imitando Cícero. Vocabulário: <i>tempus, -oris</i> (n.), tempo; <i>Mārcus</i>; <i>audācia</i>; <i>nōscō, -ere</i>, conhecer (perf. <i>nōvī</i>, "sei").', [
            ('Até quando, Marco, abusarás do nosso tempo?', '<i>Quō usque tandem, Mārce, tempore nostrō abūtēre?</i> (ou <i>abūtēris</i>). Ablativo com <i>abūtor</i>; vocativo <i>Mārce</i>.'),
            ('Ó audácia!', '<i>Ō audāciam!</i> Acusativo de exclamação.'),
            ('Qual de nós não sabe onde estiveste?', '<i>Quis nostrum nōn nōvit ubi fueris?</i> <i>Nostrum</i> partitivo; interrogativa indireta com subjuntivo perfeito, em sequência primária (<i>nōvit</i> tem valor de presente).'),
        ]),
    ],
    leituras=['henderson-in-catilinam-i-com-notas-e-vocabulario', 'cicero-in-catilinam-i-iv', 'crispus-bellum-catilinae', 'cicero-in-verrem-ii-1-53-86', 'cicero-de-imperio-cn-pompei-27-49'],
    leituras_nota='Para continuar o discurso, a edição escolar de Henderson traz notas e vocabulário completo; depois, as quatro Catilinárias no Perseus (texto de Clark, o deste capítulo). A <i>Conjuração de Catilina</i> de Salústio conta os mesmos fatos do ponto de vista de um historiador, em estilo oposto ao de Cícero: breve, arcaizante, sem períodos longos. Para outras amostras de oratória com apoio completo, o DCC tem as Verrinas (episódio de Lâmpsaco) e o discurso sobre o comando de Pompeu.',
)
