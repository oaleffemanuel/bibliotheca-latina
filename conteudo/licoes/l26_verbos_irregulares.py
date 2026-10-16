from conteudo.util import (tabela, tabela_conjugacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

PESSOAS = ('1ª sing.', '2ª sing.', '3ª sing.', '1ª pl.', '2ª pl.', '3ª pl.')


def seis_tempos(legenda, colunas):
    """Quadro dos seis tempos do indicativo: colunas = seis listas de seis formas (presente … futuro perfeito)."""
    cab = ['Pessoa', 'Presente', 'Imperfeito', 'Futuro', 'Perfeito', 'Mais-que-perfeito', 'Futuro perfeito']
    linhas = [[PESSOAS[i]] + [col[i] for col in colunas] for i in range(6)]
    return tabela(cab, linhas, legenda, latim_cols=(1, 2, 3, 4, 5, 6))


LICAO = dict(
    slug='26-verbos-irregulares', titulo='Verbos irregulares: sum, possum, volō, nōlō, mālō, eō, ferō, fīō',
    titulo_latim='Dē verbīs anōmalīs', tempo='75 min',
    resumo='Os oito verbos irregulares mais frequentes, com o indicativo completo de cada um: sum e seus compostos (prōsum, prōdesse), possum (pot- + sum), volō, nōlō e mālō, eō e seus compostos, ferō e seus compostos (com assimilação do prefixo e a passiva fertur) e fīō, que serve de passiva a faciō; por fim, um quadro comparativo dos presentes, dos infinitivos e dos imperativos (ī, īte; fer, ferte; nōlī, nōlīte).',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['verbos irregulares', 'verbos atemáticos', 'sum: os seis tempos', 'compostos de sum', 'prōsum, prōdesse', 'possum = pot- + sum', 'possum + infinitivo',
             'volō, nōlō, mālō', 'nōlī + infinitivo', 'eō, īre, iī, itum', 'compostos de eō', 'passiva impessoal ītur (menção)', 'ferō, ferre, tulī, lātum', 'passiva fertur',
             'compostos de ferō e assimilação', 'fīō, passiva de faciō', 'infinitivos e imperativos irregulares', 'quadro comparativo', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 13: os seis tempos do indicativo e as partes principais (e, antes dele, o capítulo 12 para o imperfeito e o futuro e o capítulo 6 para o presente de <i>esse</i>). Para a passiva <i>fertur</i> e para <i>fīō</i>, ajudam os capítulos 23 a 25.',
                       licoes=['06-o-presente-do-indicativo', '12-o-imperfeito-e-o-futuro', '13-o-perfeito-e-as-partes-principais', '25-verbos-depoentes']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 100 (sum, os seis tempos), § 124 (verbos irregulares: terminações juntas diretamente ao tema, fer-s), § 125 (compostos de sum; nota: prōsum < prōd + sum, prōdestis), § 126 (possum = pot- + sum; potuī de um antigo potēre), § 129 (ferō ativo e passivo; compostos afferō, auferō, cōnferō, differō, efferō, īnferō, offerō, referō), § 130 (volō, nōlō, mālō; imperativo nōlī, nōlīte), § 131 (fīō), § 132 (eō; § 132.1, compostos transitivos com passiva)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', url='https://dcc.dickinson.edu/grammar/latin/irregular-verbs-compounds-sum', nota='§ 170 (sum), § 197 (definição de verbo irregular), § 198 (compostos de sum; 198.a, prōsum conserva o d diante de e; 198.b, possum), § 199 (volō, nōlō, mālō), § 200 (compostos de ferō e as mudanças fonéticas do prefixo), § 203 (eō; 203.a, passiva impessoal itum est; 203.c, ii- contrai-se em ī- diante de s; 203.e, prōdeō), § 204 (fīō como passiva de faciō)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 134 (verbos irregulares: definição), § 135 (possum = potis + sum), § 136 (fero), § 137 (eo, com a nota sobre o perfeito em ii, mais usual que ivi, e a passiva impessoal itur, itum est), § 139 (volo, nolo, malo; "nolo de ne + volo, malo de magis + volo"), § 141 (fio), § 128 (fio entre os verbos de forma ativa e sentido passivo)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 82 e observações (esse; compostos de sum, com o d eufônico de prodest), n. 83 (possum: pot(e) + sum, assimilação do t diante de s), n. 127 (verbos irregulares propriamente ditos), n. 128 (fero), n. 130 (fio), n. 131 (volo, nolo, malo), n. 132 (eo e compostos, com as notas sobre o perfeito ii e a contração isti, isse)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Mt 6,24; 8,2–3; 20,4–5; 26,39; Jo 1,14; Gn 1,3.7; Sl 121,1 (122,1)', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Matthaeum', nota='frases autênticas das seções 2 a 6, conferidas na Wikisource latina (páginas "Evangelium Secundum Matthaeum", "Evangelium Secundum Joannem", "Liber Genesis" e "Liber Psalmorum"); ortografia adaptada (ae por æ, i por j) e macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Explicar o que torna um verbo irregular e conjugar <i>sum</i> e <i>possum</i> nos seis tempos do indicativo, aplicando a regra <i>pot-</i> / <i>pos-</i>.',
        'Conjugar <i>volō, nōlō, mālō</i>, distinguir <i>vīs, vult, volunt</i> e dar ordens negativas com <i>nōlī</i> / <i>nōlīte</i> + infinitivo.',
        'Conjugar <i>eō</i> e <i>ferō</i> nos seis tempos, reconhecer seus compostos (<i>abeō, redeō, exeō, ineō, pereō, trānseō</i>; <i>afferō, auferō, cōnferō, offerō, referō</i>) e explicar a assimilação do prefixo (<i>ad-ferō → afferō, attulī, allātum</i>).',
        'Usar <i>fīō</i> como passiva de <i>faciō</i> (<i>fit</i>, "é feito, torna-se, acontece"; <i>factum est</i>) e a passiva <i>fertur</i>.',
        'Comparar num só quadro os presentes, os infinitivos e os imperativos dos oito verbos, e analisar uma frase autêntica com <i>possum</i> + infinitivo.',
    ],
    secoes=[
        ('O que é um verbo irregular; sum e seus compostos', f'''
<p>Os verbos dos capítulos 6, 12 e 13 seguem quatro conjugações regulares: conhecida a entrada de dicionário, todas as formas se deduzem. Uns poucos verbos, porém, fogem a esse molde, e são justamente os mais usados da língua: "ser", "poder", "querer", "ir", "levar", "tornar-se". As gramáticas os chamam de <b>irregulares</b> (<i>anōmala</i>, "anômalos", na tradição antiga, daí o título latino do capítulo). A irregularidade tem duas causas principais (Bennett § 124; Allen e Greenough § 197; Ravizza n. 127):</p>
<ul>
<li><b>As terminações se juntam diretamente ao tema</b>, sem a vogal de ligação dos verbos regulares. Compare <i>reg-i-s, reg-i-t</i> com <i>fer-s, fer-t</i>: em <i>ferō</i> não há <i>i</i> entre o tema e a terminação. Esses verbos são restos de uma classe antiga, que no latim histórico ficou reduzida a poucos membros.</li>
<li><b>Partes principais vindas de raízes diferentes.</b> O perfeito de <i>sum</i> é <i>fuī</i>, de outra raiz; o de <i>ferō</i> é <i>tulī</i> e o particípio é <i>lātum</i>. O português conhece bem o fenômeno: "ir", "vou", "fui" também vêm de três verbos latinos diferentes (<i>īre</i>, <i>vādō</i>, <i>fuī</i>).</li>
</ul>
<p>A consequência prática é tranquilizadora: a irregularidade está quase toda no <b>presente</b> (e, em <i>ferō</i>, nas partes principais). O imperfeito, o futuro e os três tempos do perfectum são, na maioria, previsíveis, e o perfectum de <b>todos</b> os verbos deste capítulo é regular a partir do tema do perfeito: <i>fu-</i>, <i>potu-</i>, <i>volu-</i>, <i>i-</i>, <i>tul-</i>, com as terminações do capítulo 13.</p>
<h3>Sum: os seis tempos</h3>
<p>Você conhece o presente de <i>sum</i> desde o capítulo 6 e o imperfeito e o futuro desde o capítulo 12. Eis o verbo completo no indicativo, para servir de modelo aos compostos e a <i>possum</i> (Bennett § 100; Allen e Greenough § 170):</p>
{seis_tempos('Sum, esse, fuī, futūrus, "ser, estar, existir": indicativo', [
    ['su<b>m</b>', 'e<b>s</b>', 'es<b>t</b>', 'su<b>mus</b>', 'es<b>tis</b>', 'su<b>nt</b>'],
    ['era<b>m</b>', 'erā<b>s</b>', 'era<b>t</b>', 'erā<b>mus</b>', 'erā<b>tis</b>', 'era<b>nt</b>'],
    ['er<b>ō</b>', 'eri<b>s</b>', 'eri<b>t</b>', 'eri<b>mus</b>', 'eri<b>tis</b>', 'eru<b>nt</b>'],
    ['fu<b>ī</b>', 'fu<b>istī</b>', 'fu<b>it</b>', 'fu<b>imus</b>', 'fu<b>istis</b>', 'fu<b>ērunt</b>'],
    ['fu<b>eram</b>', 'fu<b>erās</b>', 'fu<b>erat</b>', 'fu<b>erāmus</b>', 'fu<b>erātis</b>', 'fu<b>erant</b>'],
    ['fu<b>erō</b>', 'fu<b>eris</b>', 'fu<b>erit</b>', 'fu<b>erimus</b>', 'fu<b>eritis</b>', 'fu<b>erint</b>']])}
<p>Repare que os tempos do perfectum de qualquer verbo (<i>amāv-eram</i>, <i>amāv-erō</i>) usam terminações que são, elas mesmas, o imperfeito e o futuro de <i>sum</i>: <i>-eram, -erās</i>; <i>-erō, -eris</i>. Só a 3ª do plural do futuro perfeito difere: <i>fuerint</i>, não *<i>fuerunt</i>.</p>
<h3>Os compostos de sum</h3>
<p><i>Sum</i> se compõe com várias preposições e se conjuga, nos compostos, exatamente como o simples (Bennett § 125; Allen e Greenough § 198). Os mais frequentes:</p>
{tabela(['Entrada de dicionário', 'Significado', 'Exemplo', 'Tradução'], [
    ['absum, abesse, āfuī', 'estar ausente, estar longe', 'Pater <b>abest</b>.', 'O pai está ausente.'],
    ['adsum, adesse, adfuī', 'estar presente', 'Omnēs <b>adsumus</b>.', 'Estamos todos presentes.'],
    ['dēsum, deesse, dēfuī', 'faltar', 'Aqua <b>deerat</b>.', 'Faltava água.'],
    ['praesum, praeesse, praefuī', 'estar à frente de, comandar (+ dativo)', 'Caesar exercituī <b>praeerat</b>.', 'César comandava o exército.'],
    ['intersum, interesse, interfuī', 'estar entre, tomar parte em (+ dativo)', 'Proeliō <b>interfuit</b>.', 'Tomou parte na batalha.'],
    ['prōsum, prōdesse, prōfuī', 'ser útil, fazer bem (+ dativo)', 'Labor <b>prōdest</b> corporī.', 'O trabalho faz bem ao corpo.'],
], 'Compostos de sum', latim_cols=(0, 2))}
<p>O único composto com uma particularidade é <i>prōsum</i>. A preposição tinha uma forma antiga, <i>prōd</i>, cujo <i>d</i> reaparece sempre que a forma de <i>sum</i> começa por vogal: <i>prōd-es</i>, <i>prōd-est</i>, <i>prōd-estis</i>, <i>prōd-eram</i>, <i>prōd-erō</i>, <i>prōd-esse</i>; diante de consoante, o <i>d</i> cai: <i>prō-sum</i>, <i>prō-sumus</i>, <i>prō-sunt</i>, <i>prō-fuī</i> (Bennett § 125, nota; Allen e Greenough § 198.a; Ravizza chama-o de "<i>d</i> eufônico"). Os compostos que significam "estar à frente de", "tomar parte em", "ser útil a" pedem <b>dativo</b>, como outros verbos compostos com preposição (capítulo 20).</p>
{exemplos([('Prōsum, prōd<b>es</b>, prōd<b>est</b>, prōsumus, prōd<b>estis</b>, prōsunt.', 'Sou útil, és útil, é útil, somos úteis, sois úteis, são úteis. (o <i>d</i> só diante de vogal)'),
           ('Litterae nōbīs semper <b>prōfuērunt</b>.', 'As letras sempre nos foram úteis. (perfeito: <i>prō-fuī</i>, sem <i>d</i>)'),
           ('Medicus aegrō <b>aderit</b>.', 'O médico estará junto do doente. (futuro de <i>adsum</i>; <i>aegrō</i>, dativo)')])}
'''),
        ('Possum: pot- + sum', f'''
<p><i>Possum</i>, "poder, ser capaz", é um composto do adjetivo antigo <i>potis</i> ou <i>pote</i>, "capaz", com <i>sum</i>: literalmente, "sou capaz" (Bennett § 126; Allen e Greenough § 198.b; Ravizza n. 83; Kennedy § 135). Todo o presente, o imperfeito e o futuro saem de <i>pot-</i> + as formas de <i>sum</i>, com uma única regra de som: <b>diante de <i>s</i>, o <i>t</i> de <i>pot-</i> assimila-se e vira <i>s</i></b> (*<i>pot-sum</i> → <i>possum</i>); diante de vogal, fica <i>t</i> (<i>pot-es</i>, <i>pot-est</i>, <i>pot-eram</i>). O perfeito, <i>potuī</i>, vem de um antigo verbo <i>potēre</i> e é regular.</p>
{seis_tempos('Possum, posse, potuī, "poder": indicativo', [
    ['pos<b>sum</b>', 'pot<b>es</b>', 'pot<b>est</b>', 'pos<b>sumus</b>', 'pot<b>estis</b>', 'pos<b>sunt</b>'],
    ['pot<b>eram</b>', 'pot<b>erās</b>', 'pot<b>erat</b>', 'pot<b>erāmus</b>', 'pot<b>erātis</b>', 'pot<b>erant</b>'],
    ['pot<b>erō</b>', 'pot<b>eris</b>', 'pot<b>erit</b>', 'pot<b>erimus</b>', 'pot<b>eritis</b>', 'pot<b>erunt</b>'],
    ['potu<b>ī</b>', 'potu<b>istī</b>', 'potu<b>it</b>', 'potu<b>imus</b>', 'potu<b>istis</b>', 'potu<b>ērunt</b>'],
    ['potu<b>eram</b>', 'potu<b>erās</b>', 'potu<b>erat</b>', 'potu<b>erāmus</b>', 'potu<b>erātis</b>', 'potu<b>erant</b>'],
    ['potu<b>erō</b>', 'potu<b>eris</b>', 'potu<b>erit</b>', 'potu<b>erimus</b>', 'potu<b>eritis</b>', 'potu<b>erint</b>']])}
{comparacao('Sum e possum lado a lado: a regra pot- / pos-', ['sum', 'possum', 'O que acontece'], [
    ['<b>s</b>um', 'po<b>s</b>-sum', '<i>pot-</i> + <i>s</i> → <i>poss-</i>'],
    ['<b>e</b>s', 'pot-<b>e</b>s', 'diante de vogal, <i>pot-</i> fica intacto'],
    ['<b>e</b>st', 'pot-<b>e</b>st', 'idem'],
    ['<b>s</b>umus, <b>e</b>stis, <b>s</b>unt', 'pos-sumus, pot-estis, pos-sunt', 'a regra vale pessoa por pessoa'],
    ['<b>e</b>ram, <b>e</b>rō', 'pot-eram, pot-erō', 'imperfeito e futuro: sempre <i>pot-</i>'],
    ['<b>e</b>sse', 'po<b>sse</b>', 'o infinitivo é irregular: <i>posse</i>, e não *<i>potesse</i>'],
    ['fuī', 'potuī', 'o perfeito não vem de <i>fuī</i>: tema <i>potu-</i>'],
])}
<p><i>Possum</i> quase sempre vem acompanhado de um <b>infinitivo</b>, que completa o seu sentido, como "poder" em português: <i>Nāvigāre possumus</i>, "podemos navegar"; <i>Puer legere nōn poterat</i>, "o menino não conseguia ler". O infinitivo pode ser de qualquer verbo, inclusive de um depoente (<i>loquī nōn possum</i>, "não consigo falar") ou de outro irregular (<i>īre possunt</i>, "podem ir"). Um leproso, no Evangelho de Mateus, dirige a Jesus uma frase que junta <i>possum</i> e <i>volō</i>:</p>
{exemplos([('Domine, sī <b>vīs</b>, <b>potes</b> mē mundāre.', 'Senhor, se queres, podes purificar-me. (Mt 8,2, Vulgata Clementina; <i>mundāre</i>, infinitivo de <i>mundō</i>, "purificar")'),
           ('<b>Volō</b>: mundāre.', 'Quero: sê purificado. (Mt 8,3; aqui <i>mundāre</i> é o imperativo passivo, com a terminação <i>-re</i> que você viu no imperativo dos depoentes, capítulo 25)')])}
<p>A resposta joga com as duas formas iguais: no versículo 2, <i>mundāre</i> é o infinitivo ativo que completa <i>potes</i>; no versículo 3, a mesma sequência de letras é um imperativo passivo dirigido ao doente. É o contexto que decide, como sempre que duas formas coincidem.</p>
'''),
        ('Volō, nōlō, mālō', f'''
<p><i>Volō</i>, "querer", é irregular no presente e no infinitivo; os outros tempos são regulares. Dele saem dois compostos: <i>nōlō</i>, "não querer", de <i>ne</i> + <i>volō</i>, e <i>mālō</i>, "preferir, querer mais", de <i>magis</i> + <i>volō</i> (Kennedy § 139 registra as duas etimologias; Bennett § 130; Allen e Greenough § 199; Ravizza n. 131). Aprenda os três presentes lado a lado:</p>
{tabela(['Pessoa', 'volō · querer', 'nōlō · não querer', 'mālō · preferir'], [
    ['1ª sing.', 'vol<b>ō</b>', 'nōl<b>ō</b>', 'māl<b>ō</b>'],
    ['2ª sing.', '<b>vīs</b>', 'nōn <b>vīs</b>', 'mā<b>vīs</b>'],
    ['3ª sing.', '<b>vult</b>', 'nōn <b>vult</b>', 'mā<b>vult</b>'],
    ['1ª pl.', 'vol<b>umus</b>', 'nōl<b>umus</b>', 'māl<b>umus</b>'],
    ['2ª pl.', '<b>vultis</b>', 'nōn <b>vultis</b>', 'mā<b>vultis</b>'],
    ['3ª pl.', 'vol<b>unt</b>', 'nōl<b>unt</b>', 'māl<b>unt</b>'],
    ['Infinitivo', '<b>velle</b>', '<b>nōlle</b>', '<b>mālle</b>'],
], 'Presente do indicativo e infinitivo de volō, nōlō, mālō', latim_cols=(1, 2, 3))}
<p>Há três radicais misturados: <i>vol-</i> (<i>volō, volumus, volunt</i>), <i>vul-</i> (<i>vult, vultis</i>; nos textos antigos, <i>volt, voltis</i>) e <i>vel-</i> (<i>velle</i>, com o <i>-se</i> do infinitivo assimilado ao <i>l</i>: *<i>vel-se</i> → <i>velle</i>). A 2ª do singular, <i>vīs</i>, vem de outra raiz. <i>Nōlō</i> mostra claramente a sua origem nas pessoas em que o <i>v</i> não aparece: <i>nōn vīs, nōn vult, nōn vultis</i> são simplesmente "não queres, não quer, não quereis". <i>Mālō</i> conserva o <i>v</i> de <i>volō</i> justamente nessas pessoas: <i>mā-vīs, mā-vult, mā-vultis</i>.</p>
{seis_tempos('Volō, velle, voluī: indicativo (nōlō e mālō seguem o mesmo modelo nos outros tempos: nōlēbam, nōlam, nōluī; mālēbam, mālam, māluī)', [
    ['volō', 'vīs', 'vult', 'volumus', 'vultis', 'volunt'],
    ['volē<b>bam</b>', 'volē<b>bās</b>', 'volē<b>bat</b>', 'volē<b>bāmus</b>', 'volē<b>bātis</b>', 'volē<b>bant</b>'],
    ['vol<b>am</b>', 'vol<b>ēs</b>', 'vol<b>et</b>', 'vol<b>ēmus</b>', 'vol<b>ētis</b>', 'vol<b>ent</b>'],
    ['volu<b>ī</b>', 'volu<b>istī</b>', 'volu<b>it</b>', 'volu<b>imus</b>', 'volu<b>istis</b>', 'volu<b>ērunt</b>'],
    ['volu<b>eram</b>', 'volu<b>erās</b>', 'volu<b>erat</b>', 'volu<b>erāmus</b>', 'volu<b>erātis</b>', 'volu<b>erant</b>'],
    ['volu<b>erō</b>', 'volu<b>eris</b>', 'volu<b>erit</b>', 'volu<b>erimus</b>', 'volu<b>eritis</b>', 'volu<b>erint</b>']])}
<p>O imperfeito é o da 3ª conjugação (<i>volēbam</i>, como <i>regēbam</i>), e o futuro também (<i>volam, volēs, volet</i>, como <i>regam, regēs, reget</i>). Note que <i>volam</i>, 1ª do singular, é futuro, "quererei". Os três verbos levam, como <i>possum</i>, um <b>infinitivo</b> complementar: <i>Discere volō</i>, "quero aprender"; <i>Puerī dormīre nōlunt</i>, "os meninos não querem dormir". <i>Mālō</i> compara duas coisas com <i>quam</i>, "do que", como os comparativos do capítulo 18: <i>Legere mālō quam scrībere</i>, "prefiro ler a escrever".</p>
<h3>Nōlī, nōlīte: a ordem negativa</h3>
<p>Dos três, só <i>nōlō</i> tem imperativo de uso corrente: <i>nōlī</i> (singular), <i>nōlīte</i> (plural), literalmente "não queiras, não queirais" (Bennett § 130). Com um infinitivo, essa é a maneira usual de dar uma ordem negativa em latim clássico: em vez de pôr <i>nōn</i> diante de um imperativo, diz-se "não queiras fazer".</p>
{exemplos([('<b>Nōlī</b> timēre!', 'Não temas! (literalmente, "não queiras temer")'),
           ('<b>Nōlīte</b> clāmāre, puerī!', 'Não griteis, meninos! / Não gritem, meninos!'),
           ('Vērumtamen nōn sīcut ego <b>volō</b>, sed sīcut tū.', 'Contudo, não como eu quero, mas como tu (queres). (Mt 26,39, Vulgata Clementina; <i>vērumtamen</i>, "contudo"; <i>sīcut</i>, "como"; o verbo da segunda parte, <i>vīs</i>, fica subentendido)')])}
{dica('<b>Vīs: verbo ou nome?</b> <i>Vīs</i>, "tu queres", tem a mesma forma do substantivo <i>vīs</i>, "força" (acusativo <i>vim</i>, ablativo <i>vī</i>, plural <i>vīrēs</i>). Se houver um sujeito "tu" possível e nenhum outro verbo, é o verbo; se a palavra estiver ligada a um adjetivo feminino (<i>magna vīs</i>) ou for sujeito de outro verbo, é o nome.')}
'''),
        ('Eō e seus compostos', f'''
<p><i>Eō</i>, "ir", tem um tema curtíssimo, <i>i-</i>, que vira <i>e-</i> diante de vogal: <i>e-ō</i>, <i>e-unt</i>; nas outras formas aparece como <i>ī</i> longo (<i>īs, īmus, īre</i>) ou <i>i</i> breve (<i>it</i>, <i>itum</i>). O imperfeito e o futuro se formam como nos verbos da 1ª e da 2ª conjugações, com <i>-bam</i> e <i>-bō</i>, e o perfeito é <i>iī</i> (mais raramente <i>īvī</i>), com a contração de <i>ii-</i> em <i>ī-</i> diante de <i>s</i>: <i>īstī</i>, <i>īstis</i>, <i>īsse</i> (Allen e Greenough § 203.b–c; Kennedy § 137; Ravizza n. 132; Bennett § 132 põe <i>īvī</i> em primeiro lugar, mas Allen e Greenough observam que as formas com <i>v</i> são muito raras no verbo simples).</p>
{seis_tempos('Eō, īre, iī (īvī), itum, "ir": indicativo', [
    ['e<b>ō</b>', 'ī<b>s</b>', 'i<b>t</b>', 'ī<b>mus</b>', 'ī<b>tis</b>', 'e<b>unt</b>'],
    ['ī<b>bam</b>', 'ī<b>bās</b>', 'ī<b>bat</b>', 'ī<b>bāmus</b>', 'ī<b>bātis</b>', 'ī<b>bant</b>'],
    ['ī<b>bō</b>', 'ī<b>bis</b>', 'ī<b>bit</b>', 'ī<b>bimus</b>', 'ī<b>bitis</b>', 'ī<b>bunt</b>'],
    ['i<b>ī</b> (īvī)', '<b>īstī</b> (iistī)', 'i<b>it</b>', 'i<b>imus</b>', '<b>īstis</b>', 'i<b>ērunt</b>'],
    ['i<b>eram</b>', 'i<b>erās</b>', 'i<b>erat</b>', 'i<b>erāmus</b>', 'i<b>erātis</b>', 'i<b>erant</b>'],
    ['i<b>erō</b>', 'i<b>eris</b>', 'i<b>erit</b>', 'i<b>erimus</b>', 'i<b>eritis</b>', 'i<b>erint</b>']])}
<p>O infinitivo é <i>īre</i>, e o imperativo é o mais curto do latim: <i>ī</i>, "vai!", e <i>īte</i>, "ide!". Para onde se vai exprime-se com o acusativo de direção (capítulo 19): <i>in urbem īre</i>, "ir para a cidade"; <i>Rōmam īre</i>, "ir a Roma"; <i>domum īre</i>, "ir para casa". Um salmo da Vulgata usa o futuro, e uma parábola do Evangelho de Mateus usa o imperativo e o perfeito de um composto:</p>
{exemplos([('Laetātus sum in hīs quae dicta sunt mihi: In domum Dominī <b>ībimus</b>.', 'Alegrei-me com o que me disseram: Iremos à casa do Senhor. (Sl 121,1 (122,1), Vulgata Clementina; <i>ībimus</i>, futuro, 1ª do plural)'),
           ('<b>Īte</b> et vōs in vīneam meam … Illī autem <b>abiērunt</b>.', 'Ide também vós para a minha vinha … E eles foram. (Mt 20,4–5; <i>īte</i>, imperativo plural; <i>abiērunt</i>, perfeito de <i>abeō</i>)')])}
<h3>Os compostos de eō</h3>
<p><i>Eō</i> forma muitos compostos com preposições, e todos se conjugam como o simples: <i>redit, redībat, redībit, rediit</i>. Esses compostos são muito mais frequentes nos textos do que o próprio <i>eō</i>.</p>
{tabela(['Entrada de dicionário', 'Prefixo', 'Significado', 'Exemplo'], [
    ['abeō, abīre, abiī, abitum', '<i>ab-</i>, de, para longe', 'ir embora, afastar-se', '<i>Hostēs <b>abeunt</b>.</i> Os inimigos vão embora.'],
    ['adeō, adīre, adiī, aditum', '<i>ad-</i>, para', 'aproximar-se, ir ter com', '<i>Rēgem <b>adiit</b>.</i> Foi ter com o rei.'],
    ['redeō, redīre, rediī, reditum', '<i>red-</i>, de volta', 'voltar', '<i>Crās <b>redībō</b>.</i> Voltarei amanhã.'],
    ['exeō, exīre, exiī, exitum', '<i>ex-</i>, para fora', 'sair', '<i>Ē templō <b>exiērunt</b>.</i> Saíram do templo.'],
    ['ineō, inīre, iniī, initum', '<i>in-</i>, para dentro', 'entrar em; começar', '<i>Cōnsilium <b>ineunt</b>.</i> Tomam uma decisão.'],
    ['pereō, perīre, periī, peritum', '<i>per-</i>, de todo', 'perecer, morrer, perder-se', '<i>Multī in marī <b>periērunt</b>.</i> Muitos pereceram no mar.'],
    ['trānseō, trānsīre, trānsiī, trānsitum', '<i>trāns-</i>, através', 'atravessar, passar', '<i>Flūmen <b>trānsībant</b>.</i> Atravessavam o rio.'],
], 'Compostos de eō', latim_cols=(0,))}
<p>Dois detalhes. <i>Redeō</i> tem a forma antiga <i>red-</i> do prefixo <i>re-</i>, usada diante de vogal (como o <i>prōd-</i> de <i>prōdesse</i>; Allen e Greenough § 203.e registra o mesmo em <i>prōdeō</i>, "avançar"). E alguns compostos são <b>transitivos</b> (<i>adeō</i>, <i>ineō</i>, <i>trānseō</i>: <i>flūmen trānsīre</i>, "atravessar o rio") e por isso podem ter passiva (Bennett § 132.1): <i>Flūmen trānsītur</i>, "o rio é atravessado". O próprio <i>eō</i>, intransitivo, só tem a passiva impessoal do capítulo 24: <i>ītur</i>, "vai-se, as pessoas vão"; <i>itum est</i>, "foi-se" (Allen e Greenough § 203.a; Kennedy § 137).</p>
{observacao('Eō, verbo, e eō, pronome', 'Não confunda as formas de <i>eō</i>, "ir", com as do pronome <i>is, ea, id</i> do capítulo 15. <i>Eō</i> também é o ablativo masculino e neutro de <i>is</i> ("por isso", "com ele") e um advérbio ("para lá"); <i>it</i>, "vai", não é <i>id</i>, "isso"; <i>īs</i>, "vais", não é <i>iīs</i> / <i>eīs</i>, dativo e ablativo plural do pronome. O resto da frase decide: se faltar um verbo, é provável que a forma seja de <i>eō</i>.')}
'''),
        ('Ferō e seus compostos; fīō', f'''
<p><i>Ferō</i>, "levar, trazer, carregar, suportar", tem as partes principais mais estranhas do latim: <i>ferō, ferre, tulī, lātum</i>, três raízes diferentes. No infectum ele é um verbo da 3ª conjugação (<i>ferēbam</i>, <i>feram, ferēs</i>, como <i>regēbam</i>, <i>regam</i>) com algumas formas atemáticas, sem vogal de ligação: <i>fer-s</i>, <i>fer-t</i>, <i>fer-tis</i>, o infinitivo <i>fer-re</i> (em vez de *<i>fer-e-re</i>) e o imperativo <i>fer</i> (Bennett § 129; Allen e Greenough § 197; Ravizza n. 128). No perfectum, tudo sai de <i>tul-</i>.</p>
{seis_tempos('Ferō, ferre, tulī, lātum, "levar": indicativo ativo', [
    ['fer<b>ō</b>', 'fer<b>s</b>', 'fer<b>t</b>', 'fer<b>imus</b>', 'fer<b>tis</b>', 'fer<b>unt</b>'],
    ['ferē<b>bam</b>', 'ferē<b>bās</b>', 'ferē<b>bat</b>', 'ferē<b>bāmus</b>', 'ferē<b>bātis</b>', 'ferē<b>bant</b>'],
    ['fer<b>am</b>', 'fer<b>ēs</b>', 'fer<b>et</b>', 'fer<b>ēmus</b>', 'fer<b>ētis</b>', 'fer<b>ent</b>'],
    ['tul<b>ī</b>', 'tul<b>istī</b>', 'tul<b>it</b>', 'tul<b>imus</b>', 'tul<b>istis</b>', 'tul<b>ērunt</b>'],
    ['tul<b>eram</b>', 'tul<b>erās</b>', 'tul<b>erat</b>', 'tul<b>erāmus</b>', 'tul<b>erātis</b>', 'tul<b>erant</b>'],
    ['tul<b>erō</b>', 'tul<b>eris</b>', 'tul<b>erit</b>', 'tul<b>erimus</b>', 'tul<b>eritis</b>', 'tul<b>erint</b>']])}
<p>Compare <i>ferō</i> com <i>regō</i>: <i>regis, regit, regitis, regere</i>, mas <i>fers, fert, fertis, ferre</i>. Nas outras pessoas (<i>ferimus, ferunt</i>) os dois coincidem. Como é transitivo, <i>ferō</i> tem a passiva completa (Bennett § 129), com as mesmas formas curtas: <i>feror, <b>ferris</b>, <b>fertur</b>, ferimur, feriminī, feruntur</i>; infinitivo <i><b>ferrī</b></i>; imperfeito <i>ferēbar</i>; futuro <i>ferar, ferēris</i>; perfeito <i>lātus sum</i>. Duas expressões frequentes vêm dessas formas: <i>ferunt</i>, "dizem, contam" (literalmente, "levam [a notícia]"), e <i>fertur</i>, "diz-se, conta-se"; a construção completa, com infinitivo, fica para o capítulo 28.</p>
{exemplos([('Servī aquam in vīllam <b>ferunt</b>.', 'Os escravos levam água para a casa de campo.'),
           ('Agricola onus magnum <b>tulit</b>.', 'O agricultor carregou um grande fardo. (<i>onus, oneris</i>, n., fardo)'),
           ('Nāvis ventō <b>fertur</b>.', 'O navio é levado pelo vento. (passiva; <i>ventō</i>, ablativo de causa ou meio)'),
           ('Haec dōna ad templum <b>lāta sunt</b>.', 'Estes presentes foram levados ao templo. (passiva do perfectum)')])}
<h3>Os compostos de ferō: a assimilação do prefixo</h3>
<p>Os compostos de <i>ferō</i> se conjugam como o simples, mas a preposição muda de forma conforme o som que vem depois, e como <i>ferō</i> tem três raízes (<i>fer-</i>, <i>tul-</i>, <i>lāt-</i>), um mesmo composto pode mostrar o prefixo de três maneiras (Bennett § 129; Allen e Greenough § 200 e nota). A mudança chama-se <b>assimilação</b>: a consoante final do prefixo se iguala à primeira consoante do verbo, para facilitar a pronúncia. O português herdou muitas dessas formas já assimiladas: <i>aferir</i>, <i>conferir</i>, <i>oferecer</i>, <i>referir</i>, <i>diferir</i>; <i>colação</i>, <i>oblação</i>, <i>relação</i>, <i>dilação</i>.</p>
{tabela(['Prefixo', 'Presente', 'Infinitivo', 'Perfeito', 'Supino', 'Significado'], [
    ['<i>ad-</i>', '<b>af</b>ferō', '<b>af</b>ferre', '<b>at</b>tulī', '<b>al</b>lātum', 'trazer, levar a'],
    ['<i>ab-</i> / <i>au-</i>', '<b>au</b>ferō', '<b>au</b>ferre', '<b>abs</b>tulī', '<b>ab</b>lātum', 'levar embora, tirar'],
    ['<i>con-</i>', '<b>cōn</b>ferō', '<b>cōn</b>ferre', '<b>con</b>tulī', '<b>col</b>lātum', 'reunir; comparar'],
    ['<i>ob-</i>', '<b>of</b>ferō', '<b>of</b>ferre', '<b>ob</b>tulī', '<b>ob</b>lātum', 'oferecer'],
    ['<i>re-</i>', 'referō', 'referre', '<b>ret</b>tulī', 'relātum', 'trazer de volta; relatar'],
    ['<i>in-</i>', 'īnferō', 'īnferre', 'intulī', '<b>il</b>lātum', 'levar para dentro, causar'],
    ['<i>dis-</i>', '<b>dif</b>ferō', '<b>dif</b>ferre', '<b>dis</b>tulī', '<b>dī</b>lātum', 'adiar; diferir'],
], 'Compostos de ferō (Bennett § 129; Allen e Greenough § 200)', latim_cols=(1, 2, 3, 4))}
<p>Leia a tabela como um conjunto de regras de som, não como uma lista a decorar: <i>ad-</i> vira <i>af-</i> diante de <i>f</i>, <i>at-</i> diante de <i>t</i>, <i>al-</i> diante de <i>l</i>; <i>ob-</i> vira <i>of-</i> diante de <i>f</i>; <i>con-</i> vira <i>col-</i> diante de <i>l</i>. O caso de <i>auferō</i> é especial: o latim usa ali uma preposição antiga, <i>au-</i>, de mesmo sentido que <i>ab-</i> (Allen e Greenough § 200, nota), e no perfeito e no supino volta <i>abs-</i> / <i>ab-</i>: <i>auferō, auferre, abstulī, ablātum</i>. O <i>tt</i> de <i>rettulī</i> não é assimilação do prefixo (<i>re-</i> não termina em consoante): explica-se pelo antigo perfeito com reduplicação <i>tetulī</i>, ainda usado por Plauto (Lewis & Short, s.v. <i>ferō</i>), de modo que <i>re-tetulī</i> se reduziu a <i>rettulī</i> (também grafado <i>retulī</i>). Quem encontra <i>abstulit</i> num texto e não conhece essa entrada não a acha no dicionário; por isso a regra prática é: <b>diante de uma forma em <i>-tul-</i> ou <i>-lāt-</i>, pense em <i>ferō</i></b>, separe o prefixo e procure o composto pelo presente.</p>
<h3>Fīō, a passiva de faciō</h3>
<p><i>Faciō</i>, "fazer", não tem passiva própria no infectum. Em seu lugar, o latim usa <i>fīō</i>, um verbo de <b>forma ativa e sentido passivo</b>: "sou feito", e daí "torno-me" e, na 3ª pessoa, "acontece". No perfectum, o próprio particípio de <i>faciō</i> fornece as formas: <i>factus sum</i>, "fui feito, tornei-me" (Bennett § 131; Allen e Greenough § 204; Kennedy §§ 128 e 141; Ravizza n. 130). É o verbo que o capítulo 25 deixou de lado ao falar dos semidepoentes: um semidepoente "ao contrário", ativo na forma do infectum e passivo na do perfectum.</p>
{seis_tempos('Fīō, fierī, factus sum, "ser feito, tornar-se, acontecer": indicativo', [
    ['fī<b>ō</b>', 'fī<b>s</b>', 'fi<b>t</b>', 'fī<b>mus</b>', 'fī<b>tis</b>', 'fī<b>unt</b>'],
    ['fīē<b>bam</b>', 'fīē<b>bās</b>', 'fīē<b>bat</b>', 'fīē<b>bāmus</b>', 'fīē<b>bātis</b>', 'fīē<b>bant</b>'],
    ['fī<b>am</b>', 'fī<b>ēs</b>', 'fī<b>et</b>', 'fī<b>ēmus</b>', 'fī<b>ētis</b>', 'fī<b>ent</b>'],
    ['factus <b>sum</b>', 'factus <b>es</b>', 'factus <b>est</b>', 'factī <b>sumus</b>', 'factī <b>estis</b>', 'factī <b>sunt</b>'],
    ['factus <b>eram</b>', 'factus <b>erās</b>', 'factus <b>erat</b>', 'factī <b>erāmus</b>', 'factī <b>erātis</b>', 'factī <b>erant</b>'],
    ['factus <b>erō</b>', 'factus <b>eris</b>', 'factus <b>erit</b>', 'factī <b>erimus</b>', 'factī <b>eritis</b>', 'factī <b>erunt</b>']])}
<p>O infectum é o de um verbo da 4ª conjugação (<i>fīunt</i>, como <i>audiunt</i>; <i>fīēbam</i>, como <i>audiēbam</i>; <i>fīam, fīēs</i>, como <i>audiam, audiēs</i>), com o <i>ī</i> longo mesmo diante de vogal, salvo em <i>fit</i> e no infinitivo <i>fierī</i>, que tem forma passiva. O sujeito de <i>fīō</i> leva um predicativo no <b>nominativo</b>, como com <i>sum</i> (capítulo 6): <i>Puer vir fit</i>, "o menino torna-se homem"; <i>Cicerō cōnsul factus est</i>, "Cícero foi feito cônsul". Duas frases muito conhecidas mostram o perfeito:</p>
{exemplos([('Dīxitque Deus: Fīat lūx. Et <b>facta est</b> lūx.', 'E Deus disse: Faça-se a luz. E a luz se fez. (Gn 1,3, Vulgata Clementina; <i>fīat</i> é subjuntivo, "faça-se", assunto do capítulo 32; <i>facta est</i>, perfeito, feminino como <i>lūx</i>)'),
           ('Et Verbum carō <b>factum est</b>.', 'E o Verbo se fez carne. (Jo 1,14; <i>factum</i>, neutro como <i>Verbum</i>; <i>carō, carnis</i>, f., predicativo no nominativo)')])}
<p>Em <i>Verbum carō factum est</i>, o particípio concorda com o sujeito (<i>Verbum</i>, neutro), não com o predicativo (<i>carō</i>, feminino): "o Verbo tornou-se carne". E <i>factum est</i>, sozinho, é a fórmula narrativa da Vulgata para "aconteceu": <i>Et factum est ita</i>, "e assim aconteceu" (Gn 1,7).</p>
'''),
        ('Quadro comparativo e análise de uma frase autêntica', f'''
<p>Reunidos num só quadro, os presentes dos oito verbos mostram o que eles têm em comum (as terminações pessoais são sempre as do capítulo 6, com <i>-m</i> só em <i>sum</i> e <i>possum</i>) e onde está a irregularidade de cada um:</p>
{tabela(['Pessoa', 'sum', 'possum', 'volō', 'nōlō', 'mālō', 'eō', 'ferō', 'fīō'], [
    ['1ª sing.', 'sum', 'possum', 'volō', 'nōlō', 'mālō', 'eō', 'ferō', 'fīō'],
    ['2ª sing.', 'es', 'potes', 'vīs', 'nōn vīs', 'māvīs', 'īs', 'fers', 'fīs'],
    ['3ª sing.', 'est', 'potest', 'vult', 'nōn vult', 'māvult', 'it', 'fert', 'fit'],
    ['1ª pl.', 'sumus', 'possumus', 'volumus', 'nōlumus', 'mālumus', 'īmus', 'ferimus', 'fīmus'],
    ['2ª pl.', 'estis', 'potestis', 'vultis', 'nōn vultis', 'māvultis', 'ītis', 'fertis', 'fītis'],
    ['3ª pl.', 'sunt', 'possunt', 'volunt', 'nōlunt', 'mālunt', 'eunt', 'ferunt', 'fīunt'],
], 'Presente do indicativo dos oito verbos irregulares', latim_cols=(1, 2, 3, 4, 5, 6, 7, 8))}
{tabela(['Verbo', 'Partes principais', 'Infinitivo presente', 'Imperativo', 'Tema do perfeito'], [
    ['sum', 'sum, esse, fuī, futūrus', 'esse', 'es, este', 'fu-'],
    ['possum', 'possum, posse, potuī', 'posse', '(não tem)', 'potu-'],
    ['volō', 'volō, velle, voluī', 'velle', '(não tem)', 'volu-'],
    ['nōlō', 'nōlō, nōlle, nōluī', 'nōlle', '<b>nōlī, nōlīte</b> (+ infinitivo)', 'nōlu-'],
    ['mālō', 'mālō, mālle, māluī', 'mālle', '(não tem)', 'mālu-'],
    ['eō', 'eō, īre, iī (īvī), itum', 'īre', '<b>ī, īte</b>', 'i- (īv-)'],
    ['ferō', 'ferō, ferre, tulī, lātum', 'ferre (passivo <i>ferrī</i>)', '<b>fer, ferte</b>', 'tul-'],
    ['fīō', 'fīō, fierī, factus sum', 'fierī', '(<i>fī, fīte</i>, raros)', '— (<i>factus sum</i>)'],
], 'Partes principais, infinitivos e imperativos', latim_cols=(1, 2, 3, 4))}
<p>O imperativo <i>fer</i> pertence ao pequeno grupo dos imperativos sem vogal final, ao lado de <i>dīc</i>, <i>dūc</i> e <i>fac</i>, de <i>dīcō</i>, <i>dūcō</i> e <i>faciō</i>. O subjuntivo destes verbos (<i>sim, possim, velim, eam, feram, fīam</i>) tem várias formas próprias e será estudado no capítulo 32; os outros infinitivos (perfeito e futuro), no capítulo 27.</p>
<h3>Análise gramatical: Mateus 6,24</h3>
<p>No Sermão da Montanha, uma frase curta e muito citada constrói <i>possum</i> com infinitivo:</p>
{exemplos([('Nēmō potest duōbus dominīs servīre … Nōn potestis Deō servīre et mammōnae.', 'Ninguém pode servir a dois senhores … Não podeis servir a Deus e ao dinheiro. (Mt 6,24, Vulgata Clementina)')])}
{diagrama_frase([('Nēmō', 'nominativo sing. · sujeito'), ('potest', 'possum, 3ª sing. · "pode"'), ('duōbus dominīs', 'dativo pl. · complemento de servīre'), ('servīre', 'infinitivo · completa potest')],
    '<i>Nēmō potest duōbus dominīs servīre</i> = Ninguém pode servir a dois senhores. <i>Potest</i> pede um infinitivo; <i>servīre</i> pede um dativo.')}
{analise('Mateus 6,24, palavra a palavra', [
    ('Nēmō', 'nēmō, nēminis (pronome indefinido), ninguém', 'nominativo singular', 'sujeito de <i>potest</i>'),
    ('potest', 'possum, posse, potuī, poder', 'presente do indicativo, 3ª sing.; <i>pot-</i> + <i>est</i>', 'verbo principal'),
    ('duōbus', 'duo, duae, duo, dois (numeral)', 'dativo plural masculino', 'concorda com <i>dominīs</i>'),
    ('dominīs', 'dominus, -ī (m.), senhor', 'dativo plural, 2ª declinação', 'complemento de <i>servīre</i>: "a dois senhores"'),
    ('servīre', 'serviō, servīre, servīvī, servītum, servir (+ dativo)', 'infinitivo presente, 4ª conjugação', 'complemento de <i>potest</i>'),
    ('Nōn', 'nōn (advérbio), não', 'invariável', 'nega <i>potestis</i>'),
    ('potestis', 'possum', 'presente do indicativo, 2ª pl.; <i>pot-</i> + <i>estis</i>', 'verbo principal: "podeis"'),
    ('Deō', 'deus, -ī (m.), Deus', 'dativo singular', 'complemento de <i>servīre</i>'),
    ('servīre', 'serviō', 'infinitivo presente', 'complemento de <i>potestis</i>'),
    ('et', 'et (conjunção), e', 'invariável', 'liga os dois dativos'),
    ('mammōnae', 'mammōna, -ae (m.), riqueza, dinheiro (palavra de origem aramaica, pelo grego; Lewis & Short registra também <i>mammōnās</i>)', 'dativo singular, 1ª declinação (masculino, como <i>nauta</i>)', 'complemento de <i>servīre</i>, paralelo a <i>Deō</i>'),
])}
<p>A frase mostra três coisas do capítulo. Primeiro, a regra <i>pot-</i> / <i>pos-</i>: <i>potest</i> e <i>potestis</i> têm <i>t</i> porque a forma de <i>sum</i> começa por vogal (<i>est</i>, <i>estis</i>); "não podem" seria <i>nōn possunt</i>. Segundo, <i>possum</i> não se basta: o que se pode (ou não) fazer vem num infinitivo, <i>servīre</i>. Terceiro, o infinitivo conserva a sua própria regência: <i>serviō</i> pede dativo (capítulo 20), e por isso <i>duōbus dominīs</i>, <i>Deō</i> e <i>mammōnae</i> estão todos no dativo. <i>Nēmō</i> (capítulo 17) e <i>duo</i> (capítulo 19) podem ser conferidos nos capítulos indicados.</p>
<h3>Resumo</h3>
<ul>
<li>Irregulares: terminações juntas diretamente ao tema (<i>fer-s</i>, <i>fer-t</i>) e partes principais de raízes diferentes (<i>sum/fuī</i>; <i>ferō/tulī/lātum</i>). O perfectum de todos é regular a partir do tema do perfeito.</li>
<li><i>Sum</i> e compostos (<i>absum, adsum, dēsum, praesum, prōsum</i>); <i>prōsum</i> tem <i>prōd-</i> diante de vogal: <i>prōdest, prōdesse</i>.</li>
<li><i>Possum</i> = <i>pot-</i> + <i>sum</i>; <i>pos-</i> diante de <i>s</i>; infinitivo <i>posse</i>; perfeito <i>potuī</i>; quase sempre com infinitivo.</li>
<li><i>Volō, vīs, vult, volumus, vultis, volunt</i>; <i>velle</i>. <i>Nōlō</i> (= <i>nōn volō</i>), <i>mālō</i> (= <i>magis volō</i>). <i>Nōlī / nōlīte</i> + infinitivo = ordem negativa.</li>
<li><i>Eō, īs, it, īmus, ītis, eunt</i>; <i>ībam</i>; <i>ībō</i>; <i>iī</i>; <i>īre</i>; <i>ī, īte</i>. Compostos: <i>abeō, adeō, redeō, exeō, ineō, pereō, trānseō</i>.</li>
<li><i>Ferō, ferre, tulī, lātum</i>; <i>fers, fert, fertis</i>; <i>fer, ferte</i>; passiva <i>fertur, ferrī</i>. Compostos com assimilação: <i>afferō/attulī/allātum</i>, <i>auferō/abstulī/ablātum</i>.</li>
<li><i>Fīō, fierī, factus sum</i>: passiva de <i>faciō</i>, "ser feito, tornar-se, acontecer"; predicativo no nominativo.</li>
</ul>
<p>Com este capítulo, você conhece todo o indicativo do verbo latino, ativo, passivo, depoente e irregular. O capítulo 27 passa às formas nominais, começando pelos infinitivos.</p>
'''),
    ],
    erros_comuns=[
        ('Construir <i>possum</i> com <i>t</i> diante de <i>s</i>, ou com <i>s</i> diante de vogal: *<i>potsum</i>, *<i>potsunt</i>, *<i>possest</i>; e o infinitivo *<i>potesse</i>.', 'A regra é de som: <i>pot-</i> diante de vogal (<i>potes, potest, potestis, poteram, poterō</i>), <i>pos-</i> diante de <i>s</i> (<i>possum, possumus, possunt</i>). O infinitivo é <i>posse</i>, e o perfeito, <i>potuī</i>, é regular.'),
        ('Confundir <i>vult</i> (3ª sing.) com <i>volunt</i> (3ª pl.), ou ler <i>volam</i> como presente.', '<i>Vult</i>, "quer"; <i>vultis</i>, "quereis"; <i>volunt</i>, "querem". <i>Volam, volēs, volet</i> é o futuro, formado como o da 3ª conjugação ("quererei, quererás, quererá").'),
        ('Dar ordens negativas com <i>nōn</i> + imperativo (*<i>Nōn timē!</i>), ou pôr o imperativo depois de <i>nōlī</i> (*<i>Nōlī timē!</i>).', 'A ordem negativa usual é <i>nōlī</i> (<i>nōlīte</i>) + <b>infinitivo</b>: <i>Nōlī timēre!</i>, <i>Nōlīte clāmāre!</i> Literalmente, "não queiras temer".'),
        ('Não reconhecer as formas de <i>ferō</i> e seus compostos: procurar *<i>tulō</i> ou *<i>abstulō</i> no dicionário.', 'O perfeito de <i>ferō</i> é <i>tulī</i> e o supino é <i>lātum</i>. Diante de <i>-tul-</i> ou <i>-lāt-</i>, pense em <i>ferō</i>, separe o prefixo (que pode estar assimilado: <i>at-tulit</i>, <i>col-lātum</i>, <i>abs-tulit</i>) e procure o composto pelo presente: <i>afferō</i>, <i>cōnferō</i>, <i>auferō</i>.'),
        ('Confundir as formas de <i>eō</i> com as do pronome <i>is, ea, id</i>: ler <i>it</i> como "isso", <i>eunt</i> como pronome, <i>eō</i> sempre como "eu vou".', '<i>It</i>, "vai", e <i>id</i>, "isso", diferem na consoante final; <i>īs</i>, "vais", não é <i>iīs</i>/<i>eīs</i>; <i>eō</i> pode ser "eu vou" ou o ablativo de <i>is</i> ("com ele", "por isso"). Procure o verbo da frase: se não houver outro, a forma provavelmente é de <i>eō</i>.'),
        ('Traduzir <i>fit</i> e <i>factum est</i> como ativos ("faz", "fez") ou pôr o predicativo de <i>fīō</i> no acusativo.', '<i>Fīō</i> é a passiva de <i>faciō</i>: <i>fit</i>, "é feito, torna-se, acontece"; <i>factum est</i>, "foi feito, aconteceu". O predicativo vai no nominativo, como com <i>sum</i>: <i>Cicerō cōnsul factus est</i>, não *<i>cōnsulem</i>.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Querer, não querer, preferir',
            'Analise e traduza: <i lang="la">Puerī domum redīre nōlunt; in hortō manēre mālunt.</i> Vocabulário: <i>puer, -ī</i>, menino; <i>domum</i>, para casa; <i>hortus, -ī</i>, jardim; <i>maneō, manēre</i>, ficar, permanecer.', [
            ('Quais são os verbos conjugados?', '<i>Nōlunt</i>, 3ª pl. do presente de <i>nōlō</i>, "não querem"; <i>mālunt</i>, 3ª pl. do presente de <i>mālō</i>, "preferem". Os dois estão no plural e concordam com <i>puerī</i>.'),
            ('Que formas são <i>redīre</i> e <i>manēre</i>?', '<i>Redīre</i> é o infinitivo de <i>redeō</i> (<i>red-</i> + <i>īre</i>), "voltar"; <i>manēre</i>, de <i>maneō</i>, 2ª conjugação. Cada um completa um dos verbos de vontade: "não querem voltar", "preferem ficar".'),
            ('E <i>domum</i>?', 'Acusativo de direção sem preposição, "para casa" (capítulo 19), dependente de <i>redīre</i>.'),
            ('Monte a tradução.', '"Os meninos não querem voltar para casa; preferem ficar no jardim."'),
            ('Agora passe para o singular.', '<i>Puer domum redīre nōn vult; in hortō manēre māvult.</i> Note que, no singular, <i>nōlō</i> se desfaz em <i>nōn vult</i> e <i>mālō</i> mostra o <i>v</i>: <i>māvult</i>.'),
        ]),
        pratica_guiada('Prática guiada 2 · Ferō, eō, fīō numa narrativa',
            'Analise e traduza: <i lang="la">Mīlitēs arma in castra tulērunt; deinde dux ad urbem iit, et rēx factus est.</i> Vocabulário: <i>mīles, mīlitis</i>, soldado; <i>arma, -ōrum</i> (n. pl.), armas; <i>castra, -ōrum</i> (n. pl.), acampamento; <i>deinde</i>, depois; <i>dux, ducis</i>, general; <i>urbs, urbis</i> (f.), cidade; <i>rēx, rēgis</i>, rei.', [
            ('De que verbo é <i>tulērunt</i>?', 'O tema <i>tul-</i> é o perfeito de <i>ferō</i>: <i>tulērunt</i>, 3ª pl. do perfeito, "levaram". O sujeito é <i>mīlitēs</i>; o objeto, <i>arma</i> (acusativo plural neutro).'),
            ('E <i>iit</i>?', '3ª sing. do perfeito de <i>eō</i> (<i>iī, īstī, iit</i>), "foi". Não é o pronome <i>id</i>. O sujeito é <i>dux</i>.'),
            ('Como ler <i>rēx factus est</i>?', 'Perfeito de <i>fīō</i>, "tornou-se, foi feito". <i>Rēx</i> está no nominativo porque é predicativo do sujeito (o general), como com <i>sum</i>.'),
            ('Monte a tradução.', '"Os soldados levaram as armas para o acampamento; depois o general foi para a cidade e foi feito rei (tornou-se rei)."'),
        ], 'Conclusão: os três verbos irregulares da frase só se reconhecem pelas partes principais (<i>tul-</i>, <i>i-</i>, <i>factus</i>); por isso elas devem ser decoradas junto com o presente.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Identifique', 'Para cada forma, dê o verbo (forma de dicionário), o tempo, a pessoa e o número, e traduza.', [
            ('<i>poterant</i>', '<i>possum</i>; imperfeito, 3ª pl.: "podiam".'),
            ('<i>vult</i>', '<i>volō</i>; presente, 3ª sing.: "quer".'),
            ('<i>māvīs</i>', '<i>mālō</i>; presente, 2ª sing.: "preferes".'),
            ('<i>ībunt</i>', '<i>eō</i>; futuro, 3ª pl.: "irão".'),
            ('<i>rediit</i>', '<i>redeō</i>; perfeito, 3ª sing.: "voltou".'),
            ('<i>fert</i>', '<i>ferō</i>; presente, 3ª sing.: "leva".'),
            ('<i>abstulērunt</i>', '<i>auferō</i> (<i>au-ferō, auferre, abs-tulī, ab-lātum</i>); perfeito, 3ª pl.: "levaram embora, tiraram".'),
            ('<i>fīunt</i>', '<i>fīō</i>; presente, 3ª pl.: "tornam-se, são feitos, acontecem".'),
            ('<i>prōderit</i>', '<i>prōsum</i>; futuro, 3ª sing.: "será útil" (com <i>d</i> diante da vogal de <i>erit</i>).'),
            ('<i>nōluērunt</i>', '<i>nōlō</i>; perfeito, 3ª pl.: "não quiseram".'),
        ]),
        exercicio('Exercício 2 · Transforme', 'Passe cada forma para o tempo ou o número indicado.', [
            ('<i>possumus</i> → imperfeito', '<i>poterāmus</i>, "podíamos" (imperfeito: sempre <i>pot-</i> + <i>eram</i>).'),
            ('<i>eō</i> → futuro', '<i>ībō</i>, "irei" (futuro em <i>-bō</i>, como na 1ª e 2ª conjugações).'),
            ('<i>ferimus</i> → perfeito', '<i>tulimus</i>, "levamos" (tema <i>tul-</i>).'),
            ('<i>vīs</i> → plural', '<i>vultis</i>, "quereis".'),
            ('<i>fit</i> → plural; e → perfeito (sujeito masculino plural)', '<i>fīunt</i>; <i>factī sunt</i>.'),
            ('<i>abest</i> → perfeito', '<i>āfuit</i> (também grafado <i>abfuit</i>), "esteve ausente".'),
            ('<i>it</i> → plural, nos três tempos do infectum', 'Presente <i>eunt</i>, imperfeito <i>ībant</i>, futuro <i>ībunt</i>.'),
            ('<i>fertur</i> → perfeito, sujeito feminino singular', '<i>lāta est</i>, "foi levada".'),
        ]),
        exercicio('Exercício 3 · Os compostos de ferō', 'Dê as partes principais do composto, explique a forma do prefixo e traduza a forma dada.', [
            ('<i>attulit</i>', '<i>afferō, afferre, attulī, allātum</i>: <i>ad-</i> assimilado a <i>af-</i> diante de <i>f</i>, a <i>at-</i> diante de <i>t</i>, a <i>al-</i> diante de <i>l</i>. "Trouxe."'),
            ('<i>contulērunt</i>', '<i>cōnferō, cōnferre, contulī, collātum</i>: <i>con-</i> permanece diante de <i>t</i> e <i>f</i>, vira <i>col-</i> diante de <i>l</i>. "Reuniram" ou "compararam".'),
            ('<i>obtulī</i>', '<i>offerō, offerre, obtulī, oblātum</i>: <i>ob-</i> vira <i>of-</i> diante de <i>f</i>, mas fica <i>ob-</i> diante de <i>t</i> e <i>l</i>. "Ofereci."'),
            ('<i>rettulit</i>', '<i>referō, referre, rettulī, relātum</i>: o perfeito tem <i>tt</i> (de uma antiga reduplicação). "Trouxe de volta, relatou."'),
            ('<i>ablātum</i>', '<i>auferō, auferre, abstulī, ablātum</i>: no presente <i>au-</i>, no perfeito <i>abs-</i>, no supino <i>ab-</i>. "Levado embora, tirado."'),
        ]),
        exercicio('Exercício 4 · Possum, volō, nōlō, mālō e o imperativo', 'Traduza para o latim.', [
            ('Podemos ver o mar.', '<i>Mare vidēre possumus.</i> <i>Pos-</i> diante de <i>s</i>; <i>vidēre</i>, infinitivo complementar.'),
            ('Não queres trabalhar?', '<i>Nōn vīs labōrāre?</i> A pergunta fica marcada só pela entonação, como em português (as partículas interrogativas são do capítulo 17). <i>Nōn vīs</i> é a 2ª sing. de <i>nōlō</i>, e <i>labōrāre</i>, o infinitivo complementar.'),
            ('O menino prefere brincar a estudar.', '<i>Puer lūdere māvult quam studēre.</i> <i>Māvult</i> + infinitivo, com <i>quam</i> introduzindo o segundo termo.'),
            ('Não temais, amigos!', '<i>Nōlīte timēre, amīcī!</i> <i>Nōlīte</i> + infinitivo; <i>amīcī</i>, vocativo plural.'),
            ('Vai para casa, menino!', '<i>Ī domum, puer!</i> Imperativo singular de <i>eō</i>; <i>domum</i>, acusativo de direção.'),
            ('Traze água!', '<i>Affer aquam!</i> (ou simplesmente <i>Fer aquam!</i>) Imperativo curto, como <i>fer</i>.'),
        ]),
        exercicio('Exercício 5 · Traduza lendo em ordem', 'Vocabulário: <i>nūntius, -ī</i>, mensageiro; <i>epistula, -ae</i>, carta; <i>flūmen, flūminis</i> (n.), rio; <i>pōns, pontis</i> (m.), ponte; <i>pater, patris</i>, pai; <i>medicus, -ī</i>, médico; <i>clārus, -a, -um</i>, famoso.', [
            ('<i>Nūntius epistulam ad rēgem tulit.</i>', '"O mensageiro levou a carta ao rei." <i>Tulit</i>: perfeito de <i>ferō</i>.'),
            ('<i>Mīlitēs flūmen trānsīre nōn poterant.</i>', '"Os soldados não podiam atravessar o rio." <i>Poterant</i> (imperfeito de <i>possum</i>) + infinitivo de <i>trānseō</i>, transitivo, com objeto <i>flūmen</i>.'),
            ('<i>Pater abest; crās redībit.</i>', '"O pai está ausente; voltará amanhã." <i>Abest</i>, de <i>absum</i>; <i>redībit</i>, futuro de <i>redeō</i>.'),
            ('<i>Medicus clārus factus est.</i>', '"O médico tornou-se famoso." Perfeito de <i>fīō</i>; <i>clārus</i>, predicativo no nominativo.'),
            ('<i>Pōns ā mīlitibus trānsītur.</i>', '"A ponte é atravessada pelos soldados." Passiva de <i>trānseō</i>, possível porque o composto é transitivo; <i>ā mīlitibus</i>, agente.'),
            ('<i>Quid vīs? Nihil volō.</i>', '"Que queres? Nada quero." <i>Vīs</i>, 2ª sing. de <i>volō</i>; <i>quid</i>, "que", e <i>nihil</i>, "nada", são objetos.'),
        ]),
        exercicio('Exercício 6 · Do português para o latim', 'Traduza usando os verbos do capítulo.', [
            ('Os amigos estarão presentes.', '<i>Amīcī aderunt.</i> Futuro de <i>adsum</i>, como <i>erunt</i>.'),
            ('O trabalho é útil aos meninos.', '<i>Labor puerīs prōdest.</i> <i>Prōd-</i> diante de vogal; <i>prōsum</i> + dativo.'),
            ('Íamos à cidade todos os dias.', '<i>Ad urbem cotīdiē ībāmus.</i> (<i>cotīdiē</i>, todos os dias) Imperfeito de <i>eō</i>: <i>ībāmus</i>.'),
            ('Eles não quiseram sair.', '<i>Exīre nōluērunt.</i> Perfeito de <i>nōlō</i> + infinitivo de <i>exeō</i>.'),
            ('A menina tornou-se rainha.', '<i>Puella rēgīna facta est.</i> Perfeito de <i>fīō</i>, no feminino; <i>rēgīna</i>, predicativo no nominativo.'),
        ]),
    ],
    leituras=['d-ooge-latin-for-beginners', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'lhomond-epitome-historiae-sacrae', 'kirtland-ritchie-s-fabulae-faciles', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'bennett-new-latin-grammar'],
    leituras_nota='Latin for Beginners, de D\'Ooge, e a Familia Romana, de Ørberg, apresentam os irregulares com muita leitura em volta, e convém revisá-los ali depois deste capítulo. O Epitome Historiae Sacrae, de Lhomond, e as Fabulae Faciles, de Ritchie, são narrativas simples em que <i>possum, volō, eō, ferō</i> e seus compostos aparecem a cada página. Na Vulgata, leia Mateus 6,19–34 e 8,1–4 procurando <i>possum</i> e <i>volō</i>, e Mateus 20,1–16 procurando <i>eō</i> e seus compostos. Para consulta, Bennett traz os paradigmas completos nos §§ 125–132.',
)
