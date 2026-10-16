from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Linha do tempo do tempo relativo (SVG inline, mesmas cores dos outros diagramas)
_SVG_TEMPO = (
    '<svg viewBox="0 0 700 170" width="700" role="img" aria-label="Tempo relativo do infinitivo: anterior, simultâneo, posterior ao verbo principal">'
    '<path d="M30 80 H670" stroke="#6e665b" stroke-width="2"/>'
    '<path d="M662 74 l8 6 -8 6" fill="none" stroke="#6e665b" stroke-width="2"/>'
    '<circle cx="350" cy="80" r="9" fill="#8a2b1d"/>'
    '<text x="350" y="40" text-anchor="middle" font-size="13" font-family="system-ui, sans-serif" fill="#211c17">momento do verbo principal</text>'
    '<text x="350" y="58" text-anchor="middle" font-size="12" font-family="system-ui, sans-serif" fill="#6e665b">(vidētur, vidēbātur, dīcit, dīxit...)</text>'
    '<circle cx="140" cy="80" r="6" fill="#fbf8f1" stroke="#8a2b1d" stroke-width="2"/>'
    '<circle cx="560" cy="80" r="6" fill="#fbf8f1" stroke="#8a2b1d" stroke-width="2"/>'
    '<text x="140" y="110" text-anchor="middle" font-size="13" font-family="system-ui, sans-serif" fill="#211c17">ANTES · infinitivo perfeito</text>'
    '<text x="140" y="132" text-anchor="middle" font-size="17" font-style="italic" fill="#8a2b1d">amāvisse · amātus esse</text>'
    '<text x="350" y="110" text-anchor="middle" font-size="13" font-family="system-ui, sans-serif" fill="#211c17">AO MESMO TEMPO · presente</text>'
    '<text x="350" y="132" text-anchor="middle" font-size="17" font-style="italic" fill="#8a2b1d">amāre · amārī</text>'
    '<text x="560" y="110" text-anchor="middle" font-size="13" font-family="system-ui, sans-serif" fill="#211c17">DEPOIS · infinitivo futuro</text>'
    '<text x="560" y="132" text-anchor="middle" font-size="17" font-style="italic" fill="#8a2b1d">amātūrus esse · amātum īrī</text>'
    '</svg>'
)

LICAO = dict(
    slug='27-os-infinitivos', titulo='Os infinitivos', titulo_latim='Dē īnfīnītīvīs', tempo='60 min',
    resumo='As seis formas do infinitivo latino (presente, perfeito e futuro, na ativa e na passiva), como formá-las em todas as conjugações, em esse e nos irregulares, o tempo relativo que elas exprimem e os usos que não pedem sujeito no acusativo: o infinitivo complementar, o infinitivo sujeito de expressões impessoais e o infinitivo histórico.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['infinitivo', 'forma nominal do verbo', 'infinitivo presente ativo e passivo', 'infinitivo perfeito ativo e passivo', 'infinitivo futuro ativo e passivo', 'fore', 'infinitivos dos irregulares', 'infinitivos dos depoentes', 'omissão de esse', 'tempo relativo', 'infinitivo complementar', 'infinitivo sujeito de impessoais', 'necesse est, licet, oportet, iuvat', 'infinitivo histórico', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulos 13 (partes principais), 23 e 24 (a passiva, com <i>amātus, -a, -um</i> no perfectum), 25 (depoentes) e 26 (sum, possum, volō, eō, ferō, fīō). Ajuda rever o capítulo 22, onde aparece <i>nōlī</i> + infinitivo.',
                       licoes=['13-o-perfeito-e-as-partes-principais', '23-a-voz-passiva-infectum', '24-a-passiva-do-perfectum', '25-verbos-depoentes', '26-verbos-irregulares']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 100 e nota 32 (infinitivos de sum; fore = futūrus esse), §§ 101–111 (paradigmas com os seis infinitivos de amō, moneō, regō, audiō, capiō), § 112.a e § 113 (infinitivos dos depoentes; futuro de forma ativa), § 116.1 (amāsse, audīsse) e § 116.5 (esse omitido), §§ 126, 129–132 (infinitivos de possum, ferō, volō/nōlō/mālō, fīō, eō), § 138 (impessoais), § 270 (tempo relativo; dēbuit dīcere; fore ut), § 325, §§ 326–328 (infinitivo sem sujeito acusativo: sujeito, objeto, predicativo no nominativo), § 335 (infinitivo histórico)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 170.a (fore), § 193 nota (amātum īrī), § 451 (natureza do infinitivo), § 452 e nota 2 (infinitivo sujeito; predicativo no acusativo), §§ 454–455 (sujeito de impessoais; pessoa no dativo ou acusativo), §§ 456–458 (infinitivo complementar; predicativo no caso do sujeito), § 463 (infinitivo histórico), § 486 (tempos do infinitivo fora do discurso indireto)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 365 (o infinitivo como verbo e como nome), § 366 (sujeito de impessoais), § 369 (infinitivo "prolativo" com possum, dēbeō, soleō, volō, coepī...), § 371 (esse omitido), § 372 (infinitivo histórico), § 387 (supino + īrī = futuro passivo), § 412 (tempos do infinitivo: simultâneo, anterior, posterior)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 82 (o verbo esse; fore), n. 92 (formação do infinitivo passivo), n. 165 c (infinito sujeito), n. 375 (o infinito como sujeito e como objeto dos "verbos servis"), n. 384 (os três tempos do infinito)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Mt 6,24 e Jo 4,20', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Matthaeum', nota='frase analisada na seção 6 e exercício 6, conferidas na Wikisource latina (grafia com æ e sem macrons; os macrons são deste livro)', tipo='dominio_publico'),
        referencia('Horácio, Odes 3.2.13', None, catalogo='flaccus-carmina-et-epodi-odes-e-epodos', url='https://www.thelatinlibrary.com/horace/carm3.shtml', nota='Dulce et decorum est pro patria mori, conferido na Latin Library', tipo='dominio_publico'),
        referencia('Salústio, Bellum Catilinae 21.2', None, catalogo='crispus-bellum-catilinae', url='https://www.thelatinlibrary.com/sall.1.html', nota='Tum Catilina polliceri tabulas novas..., exemplo de infinitivo histórico, conferido na Latin Library', tipo='dominio_publico'),
    ],
    objetivos=[
        'Formar os seis infinitivos (presente, perfeito e futuro; ativo e passivo) de um verbo de qualquer conjugação a partir das partes principais, além dos de <i>esse</i> (com <i>fore</i>) e dos irregulares.',
        'Reconhecer um infinitivo num texto e dizer seu tempo e sua voz, inclusive quando o <i>esse</i> vem subentendido.',
        'Explicar o tempo relativo do infinitivo (ação simultânea, anterior ou posterior à do verbo principal) e traduzi-lo corretamente depois de um verbo no presente ou no passado.',
        'Identificar e traduzir o infinitivo complementar, o infinitivo sujeito de expressões impessoais e o infinitivo histórico.',
    ],
    secoes=[
        ('O que é um infinitivo', f'''
<p>Você usa infinitivos o tempo todo em português: "quero <i>ler</i>", "é bom <i>descansar</i>", "posso <i>sair</i>?". O infinitivo é a forma do verbo que dá nome à ação sem dizer quem a faz: não tem pessoa nem número, e por isso os gramáticos o classificam entre as <b>formas nominais</b> do verbo, ao lado do particípio (capítulo 29) e do gerúndio (capítulo 31). Ele vive entre dois mundos. Como <b>verbo</b>, tem tempo e voz, pede os mesmos complementos que as formas pessoais do mesmo verbo (<i>patriam amāre</i>, com acusativo; <i>dominō servīre</i>, com dativo) e é modificado por advérbios (<i>bene vīvere</i>, "viver bem"). Como <b>substantivo</b>, pode ser sujeito ou objeto de outro verbo, e é tratado como um neutro singular: o adjetivo que se diz dele fica no neutro (Bennett § 325; A&G § 451; Kennedy § 365).</p>
<p>O infinitivo latino é mais rico que o português num ponto e mais pobre noutro. Mais rico, porque tem <b>três tempos</b> em <b>duas vozes</b>, ao todo seis formas, entre elas um infinitivo futuro que o português não tem (precisamos de uma perífrase: "haver de amar", "estar para amar"). Mais pobre, porque não existe em latim o nosso <b>infinitivo pessoal</b> ("para <i>amarmos</i>", "é hora de <i>partirem</i>"): o infinitivo latino nunca se flexiona em pessoa. Quando é preciso dizer quem faz a ação do infinitivo, o latim usa outros meios, que são o assunto do capítulo 28.</p>
{comparacao('Os seis infinitivos de amō, com o equivalente português', ['Latim', 'Tempo e voz', 'Português'], [
    ['am<b>āre</b>', 'presente ativo', 'amar'],
    ['am<b>ārī</b>', 'presente passivo', 'ser amado'],
    ['amāv<b>isse</b>', 'perfeito ativo', 'ter amado'],
    ['amāt<b>us esse</b>', 'perfeito passivo', 'ter sido amado'],
    ['amāt<b>ūrus esse</b>', 'futuro ativo', 'haver de amar, estar para amar'],
    ['amāt<b>um īrī</b>', 'futuro passivo', 'haver de ser amado'],
])}
{dica('<b>Você já conhece um infinitivo de cada verbo.</b> A segunda parte principal de um verbo no dicionário (<i>amō, <b>amāre</b>, amāvī, amātum</i>) é justamente o infinitivo presente ativo (capítulos 7 e 13). As outras cinco formas saem das outras partes principais, como mostra a seção seguinte.')}
'''),
        ('Os seis infinitivos e como se formam', f'''
<p>Cada infinitivo é construído sobre uma das partes principais, e por isso basta saber as quatro partes para formar todos. Veja a regra de cada forma e, em seguida, o quadro das cinco conjugações (Bennett §§ 101–111; Ravizza n. 92).</p>
{tabela(['Infinitivo', 'Formação', 'Exemplo (amō, amāre, amāvī, amātum)'], [
    ['Presente ativo', '2ª parte principal', '<i>amā<b>re</b></i>'],
    ['Presente passivo', '<i>-re</i> → <i>-rī</i> na 1ª, 2ª e 4ª conjugações; na 3ª (também nos verbos em <i>-iō</i>) a terminação inteira <i>-ere</i> → <i>-ī</i>', '<i>amā<b>rī</b></i>; mas <i>reg-ere</i> → <i>reg<b>ī</b></i>, <i>cap-ere</i> → <i>cap<b>ī</b></i>'],
    ['Perfeito ativo', 'tema do perfeito (3ª parte sem o <i>-ī</i>) + <i>-isse</i>', '<i>amāv<b>isse</b></i>'],
    ['Perfeito passivo', '<i>-us, -a, -um</i> (o mesmo de <i>amātus sum</i>, capítulo 24) + <i>esse</i>', '<i>amāt<b>us</b> (-a, -um) <b>esse</b></i>'],
    ['Futuro ativo', 'tema da 4ª parte (sem o <i>-um</i>) + <i>-ūrus, -ūra, -ūrum</i> + <i>esse</i>', '<i>amāt<b>ūrus</b> (-a, -um) <b>esse</b></i>'],
    ['Futuro passivo', 'a 4ª parte, invariável, + <i>īrī</i>', '<i>amāt<b>um īrī</b></i>'],
], 'Regras de formação')}
{tabela(['', 'amō, -āre (1ª)', 'moneō, -ēre (2ª)', 'regō, -ere (3ª)', 'audiō, -īre (4ª)', 'capiō, -ere (3ª, -iō)'], [
    ['Pres. ativo', 'amā<b>re</b>', 'monē<b>re</b>', 'reg<b>ere</b>', 'audī<b>re</b>', 'cap<b>ere</b>'],
    ['Pres. passivo', 'amā<b>rī</b>', 'monē<b>rī</b>', 'reg<b>ī</b>', 'audī<b>rī</b>', 'cap<b>ī</b>'],
    ['Perf. ativo', 'amāv<b>isse</b>', 'monu<b>isse</b>', 'rēx<b>isse</b>', 'audīv<b>isse</b>', 'cēp<b>isse</b>'],
    ['Perf. passivo', 'amāt<b>us esse</b>', 'monit<b>us esse</b>', 'rēct<b>us esse</b>', 'audīt<b>us esse</b>', 'capt<b>us esse</b>'],
    ['Fut. ativo', 'amāt<b>ūrus esse</b>', 'monit<b>ūrus esse</b>', 'rēct<b>ūrus esse</b>', 'audīt<b>ūrus esse</b>', 'capt<b>ūrus esse</b>'],
    ['Fut. passivo', 'amāt<b>um īrī</b>', 'monit<b>um īrī</b>', 'rēct<b>um īrī</b>', 'audīt<b>um īrī</b>', 'capt<b>um īrī</b>'],
], 'Os seis infinitivos nas cinco conjugações (Bennett §§ 101–111)', latim_cols=(1, 2, 3, 4, 5))}
<p>Três pontos merecem atenção. Primeiro, o presente passivo da terceira conjugação, que você já encontrou no capítulo 23: <i>regī</i>, e não "<i>regerī</i>". A terceira conjugação perde a sílaba <i>-er-</i> inteira, porque o <i>-ī</i> se junta direto à raiz; é por isso que <i>regī</i> e <i>capī</i> são tão curtos e tão fáceis de confundir com outras formas (o dativo <i>rēgī</i>, de <i>rēx</i>, tem <i>ē</i> longo).</p>
<p>Segundo, as duas formas compostas com <i>esse</i> contêm um elemento <b>que concorda</b>. Em <i>amātus esse</i> está o mesmo <i>amātus, -a, -um</i> que você usou na passiva do perfectum; em <i>amātūrus esse</i> está uma forma em <i>-ūrus, -ūra, -ūrum</i>, que é o particípio futuro ativo. O capítulo 29 estuda os particípios por si mesmos; aqui basta tratá-los como peças do infinitivo, que, como adjetivos de primeira classe, concordam em gênero, número e caso com o sujeito do infinitivo: <i>Mārcus laudātus esse</i>, <i>Iūlia laudāta esse</i>, <i>puerī laudātī esse</i>. Neste capítulo esse sujeito estará sempre no nominativo; no capítulo 28 você o verá no acusativo (<i>laudātum, laudātam, laudātōs esse</i>).</p>
<p>Terceiro, o futuro passivo <i>amātum īrī</i> é a única forma composta que <b>não muda</b>: <i>amātum</i> é a quarta parte principal (o supino, que o capítulo 31 explica), e <i>īrī</i> é o infinitivo passivo impessoal de <i>eō</i>, "ir" (A&G § 193, nota; Kennedy § 387). Ao pé da letra, algo como "haver ida para amar". É uma forma rara; em seu lugar o latim usa também uma perífrase com <i>fore ut</i> e o subjuntivo, obrigatória nos verbos sem supino, que você poderá reconhecer depois dos capítulos sobre o subjuntivo (Bennett § 270.3).</p>
{observacao('Formas contraídas', 'Os perfeitos em <i>-āvī, -ēvī, -īvī</i> perdem com frequência o <i>-vi-</i> antes de <i>-ss-</i>: <i>amāsse</i> = <i>amāvisse</i>, <i>dēlēsse</i> = <i>dēlēvisse</i>, <i>audīsse</i> = <i>audīvisse</i> (Bennett § 116.1). Você encontrará essas formas curtas em todos os autores; o sentido é o mesmo.')}
'''),
        ('Esse, os irregulares e os depoentes', f'''
<p>O verbo <i>sum</i> não tem voz passiva e, portanto, tem só três infinitivos: <i>esse</i> ("ser"), <i>fuisse</i> ("ter sido") e <i>futūrus esse</i> ("haver de ser"). Para este último existe uma forma curta e invariável, muito usada: <b><i>fore</i></b> (Bennett § 100 e nota 32; A&G § 170.a; Ravizza n. 82). <i>Fore</i> não concorda com nada, e é por isso cômoda: <i>futūrus esse</i>, <i>futūra esse</i>, <i>futūrī esse</i> podem ser todos substituídos por <i>fore</i>.</p>
{tabela(['Verbo', 'Presente', 'Perfeito', 'Futuro', 'Observação'], [
    ['sum, esse, fuī', 'esse', 'fuisse', 'futūrus esse = fore', 'sem passiva'],
    ['possum, posse, potuī', 'posse', 'potuisse', '(não tem)', 'sem supino, sem futuro; <i>posse</i> pode ter sentido futuro'],
    ['volō, velle, voluī', 'velle', 'voluisse', '(não tem)', 'assim também <i>nōlle</i>, <i>mālle</i>'],
    ['eō, īre, iī (īvī), itum', 'īre', 'īsse (īvisse, iisse)', 'itūrus esse', 'passiva só impessoal: <i>īrī</i>'],
    ['ferō, ferre, tulī, lātum', 'ferre · ferrī', 'tulisse · lātus esse', 'lātūrus esse · lātum īrī', 'ativa · passiva'],
    ['fīō, fierī, factus sum', 'fierī', 'factus esse', 'factum īrī', 'serve de passiva a <i>faciō</i>'],
], 'Infinitivos de sum e dos irregulares do capítulo 26 (Bennett §§ 100, 126, 129–132)', latim_cols=(0, 1, 2, 3))}
<p>Os <b>depoentes</b> (capítulo 25) têm forma passiva e sentido ativo também no infinitivo: <i>hortārī</i> é "exortar", e <i>hortātus esse</i> é "ter exortado". A exceção é o futuro, que tem <b>forma ativa</b>, porque o latim não usa <i>-um īrī</i> com sentido ativo: <i>hortātūrus esse</i>, "haver de exortar" (Bennett § 112.a e § 113). Assim: <i>sequī, secūtus esse, secūtūrus esse</i>; <i>loquī, locūtus esse, locūtūrus esse</i>; <i>morī, mortuus esse, moritūrus esse</i>.</p>
{observacao('O esse que desaparece', 'Nos infinitivos compostos, o auxiliar <i>esse</i> é muitas vezes omitido: <i>dēlētum</i> por <i>dēlētum esse</i>, <i>ventūrōs</i> por <i>ventūrōs esse</i> (Bennett § 116.5; Kennedy § 371). Quando você encontrar uma forma em <i>-tus</i> ou em <i>-tūrus</i> sozinha onde a frase pede um infinitivo (depois de um verbo de dizer ou pensar, por exemplo), suponha um <i>esse</i> subentendido. Isso acontece sobretudo na oração infinitiva do capítulo 28.')}
'''),
        ('Tempo relativo: antes, ao mesmo tempo, depois', f'''
<p>Este é o ponto mais importante do capítulo, e o que mais confunde quem vem do português. O "presente", o "perfeito" e o "futuro" do infinitivo <b>não indicam o tempo em relação a quem fala</b>, mas em relação ao <b>verbo de que o infinitivo depende</b> (Bennett § 270; A&G § 486; Ravizza n. 384; Kennedy § 412):</p>
<ul>
<li>o <b>infinitivo presente</b> indica uma ação <b>simultânea</b> à do verbo principal;</li>
<li>o <b>infinitivo perfeito</b>, uma ação <b>anterior</b> à do verbo principal;</li>
<li>o <b>infinitivo futuro</b>, uma ação <b>posterior</b> à do verbo principal.</li>
</ul>
{diagrama(_SVG_TEMPO, 'O infinitivo não marca o tempo absoluto: ele se situa antes, no mesmo momento ou depois do verbo principal, seja esse verbo presente ou passado.')}
<p>Veja o efeito com <i>vidētur</i>, "parece" (literalmente "é visto", a passiva de <i>videō</i>), que se usa pessoalmente com um infinitivo: <i>Mārcus labōrāre vidētur</i>, "Marco parece trabalhar".</p>
{tabela(['Latim', 'Relação', 'Português'], [
    ['Mārcus labōr<b>āre</b> vidētur.', 'simultânea ao presente', 'Marco parece trabalhar (agora).'],
    ['Mārcus labōrāv<b>isse</b> vidētur.', 'anterior ao presente', 'Marco parece ter trabalhado.'],
    ['Mārcus labōrāt<b>ūrus esse</b> vidētur.', 'posterior ao presente', 'Marco parece estar para trabalhar (parece que vai trabalhar).'],
    ['Mārcus labōr<b>āre</b> vidēbātur.', 'simultânea ao passado', 'Marco parecia trabalhar (naquele momento).'],
    ['Mārcus labōrāv<b>isse</b> vidēbātur.', 'anterior ao passado', 'Marco parecia ter trabalhado (antes daquele momento).'],
    ['Mārcus labōrāt<b>ūrus esse</b> vidēbātur.', 'posterior ao passado', 'Marco parecia estar para trabalhar (parecia que ia trabalhar).'],
], 'O mesmo infinitivo, dois tempos do verbo principal', latim_cols=(0,))}
<p>Repare nas duas linhas com <i>labōrāre</i>: a forma latina é a mesma, mas a tradução muda conforme o verbo principal esteja no presente ou no passado. O infinitivo "presente" depois de <i>vidēbātur</i> descreve algo que acontecia <b>no passado</b>. Por isso, quando você classificar um infinitivo, pergunte sempre "em relação a quê?". Essa pergunta é a chave da oração infinitiva no capítulo 28, onde a mesma regra decide se se traduz "diz que vem", "disse que vinha" ou "disse que viria".</p>
{observacao('Dēbuit dīcere: "devia ter dito"', 'Com os passados de <i>dēbeō</i>, <i>possum</i> e <i>oportet</i>, o latim usa o infinitivo <b>presente</b> onde o português prefere o composto: <i>dēbuit dīcere</i>, "devia ter dito" (literalmente "devia dizer", naquele momento); <i>potuit vidēre</i>, "podia ter visto" (Bennett § 270.2; A&G § 486.a). Não "corrija" o latim: a obrigação é que está no passado, e o infinitivo é simultâneo a ela.')}
'''),
        ('Os usos do infinitivo sem sujeito próprio', f'''
<p>Neste capítulo o infinitivo aparece sem um sujeito próprio no acusativo: ou ele tem o mesmo sujeito do verbo principal, ou não tem sujeito pessoal nenhum. O caso em que o infinitivo tem um sujeito próprio no acusativo (<i>dīcō Mārcum venīre</i>) é a oração infinitiva, tema do capítulo 28.</p>
<h3>1. Infinitivo complementar</h3>
<p>Muitos verbos têm sentido incompleto e pedem outro verbo para completá-lo, com o <b>mesmo sujeito</b>: "posso ler", "quero sair", "comecei a escrever". Em latim esse segundo verbo vai para o infinitivo, exatamente como em português (Bennett § 328.1; A&G § 456; Kennedy § 369; Ravizza n. 375 b). Os principais: <i>possum</i> (posso), <i>volō, nōlō, mālō</i> (quero, não quero, prefiro), <i>cupiō</i> (desejo), <i>dēbeō</i> (devo), <i>soleō</i> (costumo), <i>audeō</i> (ouso), <i>incipiō</i> e <i>coepī</i> (começo, comecei), <i>dēsinō</i> (deixo de), <i>cōnstituō</i> e <i>statuō</i> (decido), <i>discō</i> (aprendo), <i>sciō</i> (sei, no sentido de "sei fazer").</p>
{exemplos([
    ('Puerī Latīnē leg<b>ere</b> possunt.', 'Os meninos sabem (podem) ler em latim.'),
    ('Mārcus Rōmam <b>īre</b> cōnstituit.', 'Marco decidiu ir a Roma.'),
    ('Nautae nāvig<b>āre</b> incipiunt.', 'Os marinheiros começam a navegar.'),
    ('Fīlius patrem aud<b>īre</b> dēbet.', 'O filho deve ouvir o pai. (<i>patrem</i> é objeto de <i>audīre</i>)'),
    ('Omnēs laud<b>ārī</b> cupimus.', 'Todos desejamos ser elogiados. (infinitivo passivo)'),
    ('Nōlī tim<b>ēre</b>!', 'Não tenhas medo! (<i>nōlī</i> + infinitivo, a proibição do capítulo 22)'),
])}
<p>Se o infinitivo complementar for <i>esse</i> (ou outro verbo de ligação), o predicativo concorda com o sujeito do verbo principal e fica, portanto, no <b>nominativo</b> (Bennett § 328.2; A&G § 458): <i>Discipulī bon<b>ī</b> esse volunt</i>, "Os alunos querem ser bons"; <i>Iūlia laet<b>a</b> esse nōn potest</i>, "Júlia não consegue estar alegre".</p>
<h3>2. Infinitivo sujeito</h3>
<p>Com <i>est</i> + adjetivo ou substantivo neutro (<i>dulce est</i>, <i>facile est</i>, <i>difficile est</i>, <i>tempus est</i>) e com os verbos impessoais (<i>necesse est</i>, "é necessário"; <i>oportet</i>, "convém, é preciso"; <i>licet</i>, "é permitido"; <i>iuvat</i>, "agrada"; <i>placet</i>, "parece bem"), o infinitivo funciona como <b>sujeito</b>: o que "é necessário" ou "é agradável" é a própria ação (Bennett § 327; A&G §§ 452, 454; Kennedy § 366; Ravizza n. 165 c e n. 375 a). Como sujeito, ele é neutro singular, e por isso o adjetivo predicativo vai para o neutro.</p>
{exemplos([
    ('Dulce et decōrum est prō patriā <b>morī</b>.', 'É doce e honroso morrer pela pátria. (Horácio, <i>Odes</i> 3.2.13; <i>morī</i> é o infinitivo do depoente <i>morior</i>, sujeito de <i>est</i>)'),
    ('Necesse est <b>labōrāre</b>.', 'É necessário trabalhar.'),
    ('Iuvat in hortō <b>ambulāre</b>.', 'É agradável passear no jardim.'),
    ('Nōbīs nōn licet hīc <b>dormīre</b>.', 'Não nos é permitido dormir aqui.'),
])}
<p>A pessoa a quem algo é necessário, permitido ou agradável vem em geral no <b>dativo</b> (<i>nōbīs licet</i>, <i>mihi placet</i>); com <i>oportet</i> e, às vezes, com <i>necesse est</i>, ela aparece no acusativo, como sujeito do infinitivo, construção que o capítulo 28 explica (A&G § 455 e nota).</p>
{observacao('Nominativo ou acusativo no predicativo?', 'Compare <i>Beātī esse omnēs cupiunt</i>, "Todos desejam ser felizes", e <i>Beātum esse dulce est</i>, "Ser feliz é doce". No primeiro, o infinitivo é complementar e o predicativo concorda com o sujeito de <i>cupiunt</i> (nominativo plural). No segundo, o infinitivo é sujeito e não há pessoa nenhuma expressa; nesse caso o predicativo vai para o acusativo masculino singular, porque se refere a um sujeito indeterminado, "alguém" (A&G § 452, nota 2; Bennett § 327.2).')}
<h3>3. Infinitivo histórico (nota)</h3>
<p>Nas narrativas vivas, sobretudo em Salústio, Lívio e Tácito, o infinitivo presente aparece no lugar do <b>imperfeito do indicativo</b>, com o sujeito no <b>nominativo</b> e sem verbo nenhum de que dependa (Bennett § 335; A&G § 463; Kennedy § 372). O efeito é o de uma sucessão rápida de ações, como numa cena filmada. Traduza-o pelo imperfeito:</p>
{exemplos([('Tum Catilīna <b>pollicērī</b> tabulās novās...', 'Então Catilina prometia a abolição das dívidas... (Salústio, <i>Cat.</i> 21.2, <i>A conjuração de Catilina</i>; <i>pollicērī</i>, depoente, "prometer"; <i>tabulae novae</i>, literalmente "registros novos", isto é, o cancelamento das dívidas)')])}
<p>Você não precisa produzir essa construção; basta reconhecê-la quando um infinitivo aparece com sujeito no nominativo e nenhum verbo pessoal por perto.</p>
'''),
        ('Uma frase autêntica e resumo', f'''
<p>No Sermão da Montanha, na tradução de São Jerônimo, há uma frase curta com um infinitivo complementar perfeito para análise (Mt 6,24, Vulgata Clementina):</p>
{exemplos([('Nēmō potest duōbus dominīs servīre.', 'Ninguém pode servir a dois senhores.'), ('Nōn potestis Deō servīre et mammōnae.', 'Não podeis servir a Deus e à riqueza.')])}
{diagrama_frase([('Nēmō', 'nominativo · sujeito'), ('potest', 'verbo · "pode"'), ('duōbus dominīs', 'dativo · a quem se serve'), ('servīre', 'infinitivo · completa potest')], 'O infinitivo <i>servīre</i> completa o sentido de <i>potest</i> e tem o mesmo sujeito (<i>nēmō</i>); o dativo <i>duōbus dominīs</i> depende de <i>servīre</i>, não de <i>potest</i>.')}
{analise('Mateus 6,24, palavra a palavra', [
    ('Nēmō', 'nēmō, nēminis (m./f.), ninguém', 'nominativo singular', 'sujeito de <i>potest</i>'),
    ('potest', 'possum, posse, potuī, poder', 'presente do indicativo, 3ª pessoa do singular', 'verbo principal, de sentido incompleto'),
    ('duōbus', 'duo, duae, duo, dois', 'dativo plural masculino (capítulo 19)', 'concorda com <i>dominīs</i>'),
    ('dominīs', 'dominus, -ī (m.), senhor', 'dativo plural, 2ª declinação', 'complemento de <i>servīre</i> (verbo que pede dativo, capítulo 20)'),
    ('servīre', 'serviō, servīre, servīvī, servītum, servir', 'infinitivo presente ativo, 4ª conjugação', 'infinitivo complementar de <i>potest</i>: ação simultânea, mesmo sujeito'),
])}
<p>Dois raciocínios estão em jogo. O primeiro é de valência: <i>potest</i> sozinho não diz nada ("ninguém pode... o quê?"), e o infinitivo que vem no fim da frase fecha a expectativa. O segundo é de regência: o dativo <i>duōbus dominīs</i> não depende de "poder", mas de "servir", que em latim pede dativo, como mostra também a segunda frase, onde <i>Deō</i> e <i>mammōnae</i> (de <i>mammōna</i>, masculino da 1ª declinação, palavra de origem aramaica, "riqueza") estão ambos no dativo. O infinitivo conserva a regência do seu verbo: é o lado "verbo" da forma nominal.</p>
<ul>
<li><b>Seis infinitivos</b>: <i>amāre, amārī; amāvisse, amātus esse; amātūrus esse, amātum īrī</i>. Na 3ª conjugação, presente passivo em <i>-ī</i> (<i>regī, capī</i>).</li>
<li><b>Concordância</b>: <i>-tus</i> e <i>-tūrus</i> concordam com o sujeito do infinitivo; <i>-tum īrī</i> e <i>fore</i> são invariáveis; <i>esse</i> pode faltar.</li>
<li><b>Tempo relativo</b>: presente = simultâneo, perfeito = anterior, futuro = posterior ao verbo principal.</li>
<li><b>Usos deste capítulo</b>: complementar (mesmo sujeito: <i>possum, volō, dēbeō, incipiō, cōnstituō</i>), sujeito de impessoais (<i>necesse est, licet, oportet, iuvat</i>, <i>dulce est</i>) e, para reconhecer, o histórico (sujeito no nominativo, traduzido pelo imperfeito).</li>
</ul>
<p>O próximo capítulo dá ao infinitivo um sujeito próprio, no acusativo: <i>Dīcō Mārcum venīre</i>, "Digo que Marco vem". É a construção mais característica da prosa latina, e tudo o que você aprendeu aqui sobre o tempo relativo será usado ali a cada frase.</p>
'''),
    ],
    erros_comuns=[
        ('Formar o presente passivo da 3ª conjugação com <i>-erī</i> ("<i>regerī</i>", "<i>caperī</i>").', 'Na 3ª conjugação, inclusive nos verbos em <i>-iō</i>, a terminação <i>-ere</i> inteira se troca por <i>-ī</i>: <i>regī</i>, <i>capī</i>, <i>dūcī</i>, <i>mittī</i>. Só a 1ª, a 2ª e a 4ª trocam <i>-re</i> por <i>-rī</i> (<i>amārī, monērī, audīrī</i>).'),
        ('Confundir <i>amātum esse</i>, <i>amātūrum esse</i> e <i>amātum īrī</i>.', 'São três tempos diferentes. <i>Amātum esse</i> (com <i>esse</i>) é perfeito passivo, "ter sido amado"; <i>amātūrum esse</i> (com <i>-ūr-</i>) é futuro ativo, "haver de amar"; <i>amātum īrī</i> (com <i>īrī</i>) é futuro passivo, "haver de ser amado". Olhe para o elemento que acompanha: <i>esse</i> ou <i>īrī</i>, e se há ou não <i>-ūr-</i>.'),
        ('Traduzir o infinitivo presente sempre pelo presente.', 'O tempo do infinitivo é relativo. <i>Labōrāre vidēbātur</i> é "parecia trabalhar", não "parece trabalhar"; o infinitivo apenas diz que o trabalho era simultâneo ao "parecer", que está no passado. Pergunte sempre "simultâneo, anterior ou posterior a quê?".'),
        ('Deixar invariável o particípio dos infinitivos compostos ("<i>Iūlia laudātus esse vidētur</i>").', '<i>Laudātus</i> e <i>laudātūrus</i> declinam-se como adjetivos de primeira classe e concordam com o sujeito do infinitivo: <i>Iūlia laudāta esse vidētur</i>, "Júlia parece ter sido elogiada"; <i>puerī laudātūrī esse videntur</i>, "os meninos parecem estar para elogiar". Só <i>-tum īrī</i> e <i>fore</i> não variam.'),
        ('Traduzir <i>dēbuit venīre</i> por "deve ter vindo".', 'O latim põe a obrigação no passado e o infinitivo no presente: <i>dēbuit venīre</i> = "devia ter vindo" (era obrigação dele vir, naquele momento). "Deve ter vindo", no sentido de suposição, é outra ideia. Veja Bennett § 270.2.'),
        ('Procurar o verbo de que depende um infinitivo histórico.', 'No infinitivo histórico não há verbo regente: o sujeito está no nominativo e o infinitivo faz as vezes de um imperfeito (<i>Tum Catilīna pollicērī...</i>, "Então Catilina prometia..."). Se uma série de infinitivos tem sujeitos no nominativo e nenhum verbo pessoal, você está diante dessa construção.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Os seis infinitivos de mittō',
            'Forme os seis infinitivos de <i lang="la">mittō, mittere, mīsī, missum</i> (3ª conjugação, "enviar") e traduza cada um.', [
            ('Qual é o presente ativo, e qual o passivo?', 'O presente ativo é a 2ª parte principal: <i>mittere</i>, "enviar". Como o verbo é da 3ª conjugação, o passivo troca <i>-ere</i> por <i>-ī</i>: <i>mittī</i>, "ser enviado" (não "<i>mitterī</i>").'),
            ('Qual é o perfeito ativo?', 'Tema do perfeito: <i>mīs-</i> (de <i>mīsī</i>) + <i>-isse</i>: <i>mīsisse</i>, "ter enviado".'),
            ('E o perfeito passivo?', 'Tema da 4ª parte, <i>miss-</i>, + <i>-us, -a, -um</i> + <i>esse</i>: <i>missus (missa, missum) esse</i>, "ter sido enviado". O <i>-us</i> concorda com o sujeito: <i>epistula missa esse vidētur</i>, "a carta parece ter sido enviada".'),
            ('Agora o futuro ativo.', '<i>miss-</i> + <i>-ūrus</i> + <i>esse</i>: <i>missūrus (-a, -um) esse</i>, "haver de enviar". Também concorda com o sujeito.'),
            ('E o futuro passivo?', 'A 4ª parte inteira, invariável, + <i>īrī</i>: <i>missum īrī</i>, "haver de ser enviado". Não muda, qualquer que seja o sujeito.'),
        ], 'Quadro final: <i>mittere, mittī; mīsisse, missus esse; missūrus esse, missum īrī</i>. Com as quatro partes principais, nenhum infinitivo precisa ser decorado à parte.'),
        pratica_guiada('Prática guiada 2 · Dois infinitivos, dois usos',
            'Analise e traduza: <i lang="la">Necesse est mīlitibus pugnāre; sed hostēs iam fūgisse videntur.</i> Vocabulário: <i>mīles, mīlitis</i>, soldado; <i>pugnō, -āre</i>, lutar; <i>hostis, -is</i>, inimigo; <i>fugiō, fugere, fūgī</i>, fugir; <i>iam</i>, já; <i>videntur</i>, "parecem".', [
            ('Qual é o sujeito de <i>necesse est</i>?', 'O infinitivo <i>pugnāre</i>: o que "é necessário" é lutar. É um infinitivo sujeito de expressão impessoal.'),
            ('E <i>mīlitibus</i>, que caso é e por que está ali?', 'Dativo plural: a pessoa para quem a ação é necessária (A&G § 455). "É necessário aos soldados lutar", isto é, "os soldados precisam lutar".'),
            ('Que infinitivo é <i>fūgisse</i>, e de que depende?', 'Perfeito ativo de <i>fugiō</i> (tema <i>fūg-</i> + <i>-isse</i>). Depende de <i>videntur</i>, cujo sujeito é <i>hostēs</i>; o mesmo sujeito vale para o infinitivo.'),
            ('Que relação de tempo o perfeito indica?', 'Anterioridade em relação a <i>videntur</i> (presente): a fuga aconteceu antes do momento em que "parece". Daí "parecem ter fugido", reforçado por <i>iam</i>.'),
            ('Monte a tradução.', '"É necessário que os soldados lutem (os soldados precisam lutar); mas os inimigos parecem já ter fugido."'),
        ]),
    ],
    exercicios=[
        exercicio('Exercício 1 · Tempo e voz', 'Diga o tempo e a voz de cada infinitivo, de que verbo vem e traduza.', [
            ('<i>monuisse</i>', 'Perfeito ativo de <i>moneō</i> (tema <i>monu-</i> + <i>-isse</i>): "ter advertido".'),
            ('<i>audīrī</i>', 'Presente passivo de <i>audiō</i> (4ª conjugação, <i>-re</i> → <i>-rī</i>): "ser ouvido".'),
            ('<i>rēctūrus esse</i>', 'Futuro ativo de <i>regō</i> (tema da 4ª parte <i>rēct-</i> + <i>-ūrus</i> + <i>esse</i>), masculino singular: "haver de reger".'),
            ('<i>captum īrī</i>', 'Futuro passivo de <i>capiō</i>, invariável: "haver de ser capturado".'),
            ('<i>regī</i>', 'Presente passivo de <i>regō</i>: "ser regido". Não confunda com <i>rēgī</i>, dativo de <i>rēx</i>, que tem <i>ē</i> longo; num texto sem macrons, decida pelo contexto (um verbo como <i>vult</i> ou <i>dēbet</i> pede infinitivo; um verbo de dar pede dativo).'),
            ('<i>laudātae esse</i>', 'Perfeito passivo de <i>laudō</i>, com o particípio no feminino plural (nominativo): "terem sido louvadas", referindo-se a um sujeito feminino plural.'),
            ('<i>fore</i>', 'Futuro de <i>sum</i>, forma curta e invariável de <i>futūrus esse</i>: "haver de ser".'),
            ('<i>ferrī</i>', 'Presente passivo do irregular <i>ferō</i>: "ser levado".'),
            ('<i>hortātūrus esse</i>', 'Futuro do depoente <i>hortor</i>. Embora o verbo seja depoente, o infinitivo futuro tem forma ativa (Bennett § 112.a): "haver de exortar".'),
            ('<i>amāsse</i>', 'Perfeito ativo de <i>amō</i>, forma contraída de <i>amāvisse</i> (Bennett § 116.1): "ter amado".'),
        ]),
        exercicio('Exercício 2 · Forme os seis infinitivos', 'Dê os infinitivos presente, perfeito e futuro, ativos e passivos, a partir das partes principais.', [
            ('<i>dūcō, dūcere, dūxī, ductum</i> (conduzir)', '<i>dūcere, dūcī; dūxisse, ductus esse; ductūrus esse, ductum īrī</i>. Presente passivo em <i>-ī</i>, porque o verbo é da 3ª conjugação.'),
            ('<i>dēleō, dēlēre, dēlēvī, dēlētum</i> (destruir)', '<i>dēlēre, dēlērī; dēlēvisse (dēlēsse), dēlētus esse; dēlētūrus esse, dēlētum īrī</i>.'),
            ('<i>scrībō, scrībere, scrīpsī, scrīptum</i> (escrever)', '<i>scrībere, scrībī; scrīpsisse, scrīptus esse; scrīptūrus esse, scrīptum īrī</i>.'),
            ('<i>faciō, facere, fēcī, factum</i> (fazer)', 'Ativa: <i>facere, fēcisse, factūrus esse</i>. Passiva: o presente é <i>fierī</i>, de <i>fīō</i> (capítulo 26), e não "<i>facī</i>"; depois <i>factus esse</i>, <i>factum īrī</i>.'),
            ('<i>veniō, venīre, vēnī, ventum</i> (vir)', 'Ativa: <i>venīre, vēnisse, ventūrus esse</i>. Por ser intransitivo, <i>veniō</i> não tem passiva pessoal ("ser vindo" não faz sentido); só tem a passiva impessoal do capítulo 24 (<i>ventum est</i>, "veio-se, chegou-se"), cujos infinitivos são raros e não precisam ser praticados.'),
        ]),
        exercicio('Exercício 3 · Tempo relativo', 'Traduza, prestando atenção à relação de tempo entre o infinitivo e o verbo principal. Vocabulário: <i>vidētur, videntur</i>, parece(m); <i>vidēbātur, vidēbantur</i>, parecia(m); <i>urbs, urbis</i>, cidade.', [
            ('<i>Rēx bonus esse vidētur.</i>', '"O rei parece ser bom." Infinitivo presente: simultâneo a <i>vidētur</i>; <i>bonus</i>, predicativo no nominativo, concorda com <i>rēx</i>.'),
            ('<i>Rēx bonus fuisse vidētur.</i>', '"O rei parece ter sido bom." Perfeito: anterior ao presente.'),
            ('<i>Urbs capta esse vidēbātur.</i>', '"A cidade parecia ter sido tomada." Perfeito passivo, anterior a um passado; <i>capta</i> concorda com <i>urbs</i> (feminino singular).'),
            ('<i>Hostēs ventūrī esse videntur.</i>', '"Os inimigos parecem estar para vir" (parece que virão). Futuro: posterior; <i>ventūrī</i> no masculino plural, com <i>hostēs</i>.'),
            ('<i>Puerī dormīre vidēbantur.</i>', '"Os meninos pareciam dormir." Presente: simultâneo a um passado, por isso traduzido como ação daquele momento passado.'),
        ]),
        exercicio('Exercício 4 · Que uso é este?', 'Classifique o infinitivo (complementar, sujeito ou histórico) e traduza. Vocabulário: <i>discō, -ere</i>, aprender; <i>omnis, -e</i>, todo; <i>templum, -ī</i>, templo; <i>sub arboribus</i>, sob as árvores; <i>nostrī</i>, os nossos (soldados); <i>sequor, sequī</i>, perseguir; <i>fortis, -e</i>, corajoso.', [
            ('<i>Discipulī Latīnē scrībere discunt.</i>', 'Complementar de <i>discunt</i>, com o mesmo sujeito: "Os alunos aprendem a escrever em latim."'),
            ('<i>Necesse est omnibus labōrāre.</i>', 'Sujeito de <i>necesse est</i>; <i>omnibus</i> é dativo da pessoa: "É necessário a todos trabalhar" ("todos precisam trabalhar").'),
            ('<i>Nōbīs nōn licet in templō dormīre.</i>', 'Sujeito de <i>licet</i>, com a pessoa no dativo: "Não nos é permitido dormir no templo."'),
            ('<i>Iuvat sub arboribus legere.</i>', 'Sujeito de <i>iuvat</i>: "É agradável ler sob as árvores."'),
            ('<i>Tum hostēs fugere, nostrī sequī.</i>', 'Infinitivos históricos: sujeitos no nominativo (<i>hostēs</i>, <i>nostrī</i>) e nenhum verbo regente. Traduza pelo imperfeito: "Então os inimigos fugiam, os nossos os perseguiam."'),
            ('<i>Mīlitēs fortēs esse dēbent.</i>', 'Complementar de <i>dēbent</i>; <i>fortēs</i> é predicativo no nominativo, concordando com <i>mīlitēs</i>: "Os soldados devem ser corajosos."'),
        ]),
        exercicio('Exercício 5 · Retroversão', 'Passe para o latim. Use o vocabulário dos exercícios anteriores.', [
            ('Os meninos querem ser elogiados.', '<i>Puerī laudārī volunt</i> (ou <i>cupiunt</i>). Infinitivo presente passivo, complementar.'),
            ('A menina não consegue dormir.', '<i>Puella dormīre nōn potest.</i>'),
            ('É preciso ler muitos livros.', '<i>Necesse est multōs librōs legere.</i> <i>Librōs</i> é objeto de <i>legere</i>, que conserva a regência do verbo.'),
            ('O rei decidiu enviar soldados.', '<i>Rēx mīlitēs mittere cōnstituit.</i> <i>Cōnstituō</i> + infinitivo complementar (mesmo sujeito).'),
            ('Os soldados parecem ter sido vencidos.', '<i>Mīlitēs victī esse videntur.</i> Perfeito passivo de <i>vincō</i> (<i>victum</i>), com <i>victī</i> no nominativo masculino plural, concordando com <i>mīlitēs</i>.'),
            ('Não tenhas medo!', '<i>Nōlī timēre!</i> Proibição com <i>nōlī</i> + infinitivo (capítulo 22); a vários: <i>Nōlīte timēre!</i>'),
        ]),
        exercicio('Exercício 6 · Textos autênticos', 'Identifique cada infinitivo, seu tempo, sua voz e seu uso. Os textos estão citados com macrons acrescentados.', [
            ('<i>Dulce et decōrum est prō patriā morī.</i> (Horácio, <i>Odes</i> 3.2.13)', '<i>Morī</i>: infinitivo presente do depoente <i>morior</i> (forma passiva, sentido ativo), sujeito de <i>est</i>. Os predicativos <i>dulce</i> e <i>decōrum</i> estão no neutro porque o sujeito é um infinitivo. "É doce e honroso morrer pela pátria."'),
            ('<i>Nōn potestis Deō servīre et mammōnae.</i> (Mt 6,24)', '<i>Servīre</i>: presente ativo, complementar de <i>potestis</i>; <i>Deō</i> e <i>mammōnae</i> são dativos regidos por <i>servīre</i>. "Não podeis servir a Deus e à riqueza."'),
            ('<i>Tum Catilīna pollicērī tabulās novās.</i> (Salústio, <i>Cat.</i> 21.2)', '<i>Pollicērī</i>: presente do depoente <i>polliceor</i>, infinitivo histórico (sujeito <i>Catilīna</i> no nominativo, nenhum verbo regente). "Então Catilina prometia a abolição das dívidas."'),
            ('<i>Ierosolymis est locus ubi adōrāre oportet.</i> (Jo 4,20; <i>Ierosolymis</i>, "em Jerusalém"; <i>ubi</i>, onde; <i>adōrō, -āre</i>, adorar)', '<i>Adōrāre</i>: presente ativo, sujeito do impessoal <i>oportet</i>. "Em Jerusalém está o lugar onde é preciso adorar."'),
        ]),
    ],
    leituras=['bennett-new-latin-grammar', 'ravizza-gramatica-latina', 'kirtland-ritchie-s-fabulae-faciles', 'eutropius-breviarium-ab-urbe-condita', 'crispus-bellum-catilinae', 'vulgata-biblia-sacra-vulgata-editio-clementina'],
    leituras_nota='Para consultar as formas, os paradigmas de Bennett (§§ 100–113) trazem os seis infinitivos de cada conjugação, e o Pe. Ravizza explica em português o infinito como sujeito e como objeto (n. 375). As <i>Fabulae Faciles</i> e o <i>Breviarium</i> de Eutrópio estão cheios de infinitivos complementares com <i>possum</i>, <i>volō</i> e <i>cōnstituō</i>, bons para treinar o reconhecimento. Em Salústio (<i>Bellum Catilinae</i>) procure séries de infinitivos históricos; nos Evangelhos da Vulgata, infinitivos complementares e sujeitos de <i>oportet</i>.',
)
