from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Diagrama do encaixe: a oração infinitiva como objeto do verbo principal, e o "que" do português
_SVG_ENCAIXE = (
    '<svg viewBox="0 0 720 236" width="720" role="img" aria-label="Dīcō Mārcum venīre: a oração infinitiva Mārcum venīre é o objeto de dīcō; em português, Digo que Marco vem">'
    '<rect x="20" y="30" width="150" height="66" rx="6" fill="#fbf8f1" stroke="#8a2b1d" stroke-width="1.5"/>'
    '<text x="95" y="60" text-anchor="middle" font-size="22" font-style="italic" fill="#211c17">Dīcō</text>'
    '<text x="95" y="82" text-anchor="middle" font-size="12" font-family="system-ui, sans-serif" fill="#6e665b">verbo principal</text>'
    '<path d="M173 63 h24" stroke="#8a2b1d" stroke-width="2"/><path d="M191 57 l6 6 -6 6" fill="none" stroke="#8a2b1d" stroke-width="2"/>'
    '<rect x="208" y="12" width="492" height="102" rx="10" fill="none" stroke="#8a2b1d" stroke-width="1.5" stroke-dasharray="6 4"/>'
    '<rect x="228" y="30" width="200" height="66" rx="6" fill="#fbf8f1" stroke="#8a2b1d" stroke-width="1.5"/>'
    '<text x="328" y="60" text-anchor="middle" font-size="22" font-style="italic" fill="#211c17">Mārcum</text>'
    '<text x="328" y="82" text-anchor="middle" font-size="12" font-family="system-ui, sans-serif" fill="#6e665b">acusativo · sujeito do infinitivo</text>'
    '<rect x="480" y="30" width="200" height="66" rx="6" fill="#fbf8f1" stroke="#8a2b1d" stroke-width="1.5"/>'
    '<text x="580" y="60" text-anchor="middle" font-size="22" font-style="italic" fill="#211c17">venīre</text>'
    '<text x="580" y="82" text-anchor="middle" font-size="12" font-family="system-ui, sans-serif" fill="#6e665b">infinitivo · verbo da oração</text>'
    '<text x="454" y="134" text-anchor="middle" font-size="13" font-family="system-ui, sans-serif" fill="#8a2b1d">oração infinitiva = objeto direto de dīcō</text>'
    '<path d="M20 152 H700" stroke="#6e665b" stroke-width="1" stroke-dasharray="2 4"/>'
    '<text x="95" y="188" text-anchor="middle" font-size="20" fill="#211c17">Digo</text>'
    '<text x="214" y="188" text-anchor="middle" font-size="20" font-weight="bold" fill="#8a2b1d">que</text>'
    '<text x="328" y="188" text-anchor="middle" font-size="20" fill="#211c17">Marco</text>'
    '<text x="580" y="188" text-anchor="middle" font-size="20" fill="#211c17">vem</text>'
    '<text x="360" y="222" text-anchor="middle" font-size="12" font-family="system-ui, sans-serif" fill="#6e665b">o português acrescenta a conjunção "que", põe o sujeito no caso reto e o verbo num tempo pessoal</text>'
    '</svg>'
)

LICAO = dict(
    slug='28-a-oracao-infinitiva', titulo='A oração infinitiva', titulo_latim='Accūsātīvus cum īnfīnītīvō', tempo='70 min',
    resumo='A construção mais característica da prosa latina: depois de verbos de dizer, pensar, saber, perceber e sentir, o latim não usa "que"; põe o sujeito da oração dependente no acusativo e o verbo no infinitivo. Como reconhecê-la, como o tempo do infinitivo se traduz, o reflexivo sē/suus, a construção pessoal com dīcitur e vidētur, iubeō, vetō e volō, e as estratégias para passar tudo isso ao português.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['oração infinitiva', 'acusativo com infinitivo', 'verba dicendi et sentiendi', 'negō', 'tempo do infinitivo no discurso indireto', 'concordância no acusativo', 'fore e posse com sentido futuro', 'spērō e prōmittō com infinitivo futuro', 'reflexivo indireto sē, suus', 'construção pessoal: dīcitur, vidētur', 'construção impessoal: trāditum est', 'iubeō e vetō', 'volō com e sem acusativo', 'verbos de emoção: gaudeō', 'tradução para o português', 'quia e quod no latim cristão', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 27 (os seis infinitivos e o tempo relativo) e capítulo 14 (pronomes pessoais e reflexivos: <i>sē</i>, <i>suus</i>, <i>is</i>). A passiva dos capítulos 23 e 24 é usada o tempo todo.',
                       licoes=['14-os-pronomes-pessoais', '23-a-voz-passiva-infectum', '24-a-passiva-do-perfectum', '27-os-infinitivos']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 116.5 (esse omitido), § 184 (sujeito do infinitivo no acusativo), § 244 (reflexivo direto e indireto), § 270 (tempo relativo do infinitivo), § 330 (acusativo com infinitivo como sujeito de impessoais), § 331 I–V (como objeto: verbos de dizer, pensar, saber, perceber, inclusive negō; iubeō e vetō, 331 II e II.a; volō, nōlō, mālō, cupiō, 331 IV; verbos de emoção, 331 V), § 332 (construção pessoal da passiva: iubeor, vetor; videor; dīcor, putor; fertur, trāditur; nota sobre a construção impessoal nos tempos compostos)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 451 (origem do sujeito acusativo), §§ 299–300 (reflexivo; reflexivo indireto), § 459, §§ 577–579 (discurso indireto; verbos de saber, pensar, dizer, perceber), § 580 (580.b negō; 580.c verbos de esperar, prometer, ameaçar com infinitivo futuro), § 581 (sujeito acusativo sempre expresso), § 582 (construção pessoal e impessoal com verbos passivos), § 584 (tempos do infinitivo no discurso indireto; 584.a perfeito para todo passado; 584.b posse com sentido futuro)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 207 nota (acusativo sujeito do infinitivo), § 370 e nota (nominativo com infinitivo: narrātur, trāditur; uso impessoal no perfeito), § 371 (esse omitido), § 412 (tempos do infinitivo na oratio obliqua), § 414 (acusativo com infinitivo como sujeito e como objeto; nota: verbos de esperar e prometer com infinitivo futuro)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='nn. 238–240 (construção pessoal de videor, jubeor, vetor, dicor, putor, traditur), n. 377 (acusativo com infinito nas proposições subjetivas), n. 378 e observação 1 (proposições objetivas; ambiguidade entre sujeito e objeto do infinitivo), n. 379 (verba sentiendi, declarandi, voluntatis, affectuum), n. 380 (o sujeito vem sempre expresso; se), n. 381 c (esperar, prometer: infinitivo futuro), n. 382 (volo, nolo, malo; jubeo e veto, com infinitivo passivo quando falta a pessoa), n. 384 (tempos do infinito), n. 383 a (gaudeo te valere e gaudeo quod)', tipo='dominio_publico'),
        referencia('Cícero, Primeira Catilinária 1.1', None, catalogo='cicero-in-catilinam-i-iv', url='https://www.thelatinlibrary.com/cicero/cat1.shtml', nota='Patere tua consilia non sentis..., frase analisada na seção 6, conferida na Latin Library; no texto, as duas perguntas (patere... non sentis, constrictam... non vides?) formam uma só frase, separadas por vírgula; o capítulo cita cada metade em separado, com ponto de interrogação', tipo='dominio_publico'),
        referencia('Cícero, Tusculanas 1.4 e Sobre a adivinhação 2.115–116', None, url='https://www.thelatinlibrary.com/cicero/divinatione2.shtml', nota='Epaminondas... cecinisse dicitur (Tusc. 1.4); hostium vim se perversurum putavit (Div. 2.115); aio te, Aeacida, Romanos vincere posse (Div. 2.116, verso de Ênio citado por Cícero); conferidos na Latin Library', tipo='dominio_publico'),
        referencia('Cornélio Nepos, Aníbal 2.4', None, catalogo='nepos-vita-hannibalis', url='https://www.thelatinlibrary.com/nepos/nepos.han.shtml', nota='iurare iussit numquam me in amicitia cum Romanis fore, conferido na Latin Library (prática guiada 2)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Jo 4,19–20', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Joannem', nota='video quia propheta es tu; vos dicitis, quia Jerosolymis est locus..., conferidos na Wikisource latina', tipo='dominio_publico'),
    ],
    objetivos=[
        'Reconhecer uma oração infinitiva (verbo de dizer, pensar, saber, perceber ou sentir + acusativo + infinitivo) e delimitar seu sujeito e seu verbo.',
        'Traduzir o infinitivo da oração infinitiva pelo tempo português correto, depois de um verbo principal no presente ou no passado.',
        'Distinguir <i>sē/suus</i> (o sujeito do verbo principal) de <i>eum/eius</i> (outra pessoa) e aplicar a concordância no acusativo.',
        'Traduzir a construção pessoal (<i>dīcitur</i>, <i>vidētur</i> + nominativo e infinitivo) e as construções com <i>iubeō</i>, <i>vetō</i>, <i>volō</i> e <i>gaudeō</i>.',
        'Escolher, em cada caso, a melhor estratégia de tradução: "que" + indicativo, "que" + subjuntivo ou infinitivo.',
    ],
    secoes=[
        ('Uma oração dentro da outra', f'''
<p>Em português, quando contamos o que alguém diz ou pensa, usamos uma oração introduzida por "que": "Digo <i>que Marco vem</i>", "Penso <i>que a cidade é bela</i>". O latim clássico, nessa situação, não usa conjunção nenhuma. Ele põe o <b>sujeito</b> da oração dependente no <b>acusativo</b> e o <b>verbo</b> no <b>infinitivo</b> (Bennett § 184 e § 331; A&G §§ 577–579; Kennedy § 414; Ravizza n. 378):</p>
{exemplos([
    ('Dīcō <b>Mārcum venīre</b>.', 'Digo que Marco vem.'),
    ('Putō <b>urbem pulchram esse</b>.', 'Penso que a cidade é bela.'),
    ('Sciō <b>tē Latīnē legere</b>.', 'Sei que você lê latim.'),
])}
{diagrama(_SVG_ENCAIXE, 'A oração infinitiva <i>Mārcum venīre</i> ocupa, inteira, o lugar de objeto direto de <i>dīcō</i>. O "que" é uma exigência do português, não do latim.')}
<p>Por que acusativo? A explicação histórica é que, num estágio antigo, o nome era objeto do próprio verbo principal ("digo Marco, [quanto a] vir"), e o infinitivo o completava; com o tempo, esse objeto passou a ser sentido como o sujeito do infinitivo (A&G § 451 e § 577). Para o leitor, o que importa é o resultado: depois de certos verbos, um <b>acusativo seguido de um infinitivo</b> forma uma oração completa, com sujeito e verbo próprios. O nome tradicional da construção é <i>accūsātīvus cum īnfīnītīvō</i>, "acusativo com infinitivo".</p>
<p>Os verbos que a introduzem são, sobretudo, os de <b>dizer</b>, <b>pensar</b>, <b>saber</b> e <b>perceber</b> (os <i>verba dīcendī et sentiendī</i> das gramáticas), e também os de <b>sentimento</b>:</p>
{tabela(['Grupo', 'Verbos', 'Exemplo'], [
    ['dizer, anunciar', '<i>dīcō, nūntiō, respondeō, scrībō, nārrō, negō</i>', '<i>Nūntius dīcit hostēs adesse.</i> O mensageiro diz que os inimigos estão aí.'],
    ['pensar, crer, esperar', '<i>putō, crēdō, exīstimō, spērō</i>', '<i>Crēdō deōs bonōs esse.</i> Creio que os deuses são bons.'],
    ['saber, compreender', '<i>sciō, intellegō, cognōscō</i>', '<i>Intellegō tē fessum esse.</i> Percebo (compreendo) que você está cansado.'],
    ['perceber', '<i>videō, audiō, sentiō</i>', '<i>Videō sōlem lūcēre.</i> Vejo que o sol brilha (vejo o sol brilhar).'],
    ['sentir (emoção)', '<i>gaudeō, doleō, mīror</i>', '<i>Gaudeō tē valēre.</i> Alegro-me de que você esteja bem.'],
], 'Verbos que pedem oração infinitiva (Bennett § 331; A&G § 579; Ravizza n. 379)')}
<p>Um caso especial é <b><i>negō</i></b>. Para dizer "diz que não", o latim prefere <i>negō</i> a <i>dīcō ... nōn</i>: <i>Negat Mārcum venīre</i>, "Diz que Marco <b>não</b> vem" (A&G § 580.b). A negação vai para o verbo principal, mas em português ela volta para a oração dependente; traduzir <i>negat</i> por "nega" funciona às vezes, mas "diz que não" é quase sempre mais natural.</p>
<p>A oração infinitiva também pode ser <b>sujeito</b> de expressões impessoais, como o infinitivo simples do capítulo 27: <i>Necesse est mē abīre</i>, "É necessário que eu parta"; <i>Cōnstat Rōmam magnam esse</i>, "É sabido que Roma é grande" (Bennett § 330; Ravizza n. 377).</p>
{dica('<b>Como reconhecer.</b> Quando você ler um verbo de dizer, pensar, saber ou perceber, e logo depois (ou antes) encontrar um acusativo e um infinitivo que não dependem de mais nada, ponha mentalmente um "que" entre o verbo e o acusativo. O acusativo vira o sujeito, e o infinitivo vira um verbo conjugado.')}
'''),
        ('O tempo do infinitivo e como traduzi-lo', f'''
<p>Aqui entra o que você aprendeu no capítulo 27: o tempo do infinitivo é <b>relativo</b> ao verbo principal. O presente indica simultaneidade, o perfeito anterioridade, o futuro posterioridade (Bennett § 270; A&G § 584; Kennedy § 412; Ravizza n. 384). O português, por sua vez, exprime essas relações com tempos diferentes conforme o verbo principal esteja no presente ou no passado. Por isso a mesma forma latina se traduz de dois modos:</p>
{tabela(['Infinitivo', 'Depois de dīcit (presente)', 'Depois de dīxit (passado)'], [
    ['<i>Mārcum ven<b>īre</b></i> (simultâneo)', 'diz que Marco <b>vem</b>', 'disse que Marco <b>vinha</b>'],
    ['<i>Mārcum vēn<b>isse</b></i> (anterior)', 'diz que Marco <b>veio</b>', 'disse que Marco <b>tinha vindo</b> (viera)'],
    ['<i>Mārcum vent<b>ūrum esse</b></i> (posterior)', 'diz que Marco <b>virá</b>', 'disse que Marco <b>viria</b>'],
    ['<i>urbem cap<b>ī</b></i> (simultâneo, passivo)', 'diz que a cidade <b>é tomada</b> (está sendo tomada)', 'disse que a cidade <b>era tomada</b>'],
    ['<i>urbem capt<b>am esse</b></i> (anterior, passivo)', 'diz que a cidade <b>foi tomada</b>', 'disse que a cidade <b>tinha sido tomada</b>'],
    ['<i>urbem capt<b>um īrī</b></i> (posterior, passivo)', 'diz que a cidade <b>será tomada</b>', 'disse que a cidade <b>seria tomada</b>'],
], 'Um só infinitivo latino, dois tempos portugueses')}
<p>Na prática, traduza em dois passos: primeiro decida a relação (simultâneo, anterior, posterior); depois escolha o tempo português que exprime essa relação a partir do tempo do verbo principal. O infinitivo perfeito cobre <b>qualquer</b> passado: conforme o contexto, <i>dīxit Mārcum vēnisse</i> pode ser "tinha vindo", "veio" ou "vinha" (A&G § 584.a).</p>
{observacao('Fore e posse', 'Com <i>sum</i>, o infinitivo futuro é muitas vezes <i>fore</i>: <i>Spērō tē fēlīcem fore</i>, "Espero que você seja (venha a ser) feliz". <i>Possum</i> não tem infinitivo futuro, e o seu presente <i>posse</i> assume muitas vezes o sentido futuro: <i>Spērant sē vincere posse</i>, "Esperam poder vencer" (A&G § 584.b). Lembre também que o <i>esse</i> dos infinitivos compostos costuma faltar: <i>dīxit urbem captam</i> = <i>captam esse</i> (Bennett § 116.5).')}
<p>Um grupo de verbos merece atenção especial: os de <b>esperar, prometer, ameaçar, jurar</b> (<i>spērō, prōmittō, polliceor, minor, iūrō</i>). Em português dizemos "espero vencer", "prometo vir", com infinitivo simples. Em latim, esses verbos pedem uma oração infinitiva completa, com sujeito expresso e infinitivo <b>futuro</b>: <i>Spērō <b>mē</b> ventūrum esse</i>, "Espero vir"; <i>Prōmīsit <b>sē</b> pecūniam redditūrum esse</i>, "Prometeu devolver o dinheiro" (A&G § 580.c; Kennedy § 414, nota; Ravizza n. 381 c).</p>
'''),
        ('Tudo no acusativo; sē e suus', f'''
<p>Como o sujeito da oração infinitiva está no acusativo, tudo o que concorda com ele vai para o acusativo também: o predicativo, o particípio dos infinitivos compostos, os adjetivos (Ravizza n. 378 c):</p>
{exemplos([
    ('Putō Iūli<b>am</b> laet<b>am</b> esse.', 'Penso que Júlia está alegre.'),
    ('Sciō epistul<b>am</b> scrīpt<b>am</b> esse.', 'Sei que a carta foi escrita.'),
    ('Nūntiant host<b>ēs</b> vict<b>ōs</b> esse.', 'Anunciam que os inimigos foram vencidos.'),
    ('Crēdō v<b>ōs</b> ventūr<b>ōs</b> esse.', 'Creio que vocês virão.'),
])}
<p>Repare que, nos exemplos com <i>vōs</i> e <i>tē</i>, o sujeito do infinitivo é um pronome pessoal no acusativo. Em latim o sujeito da oração infinitiva vem <b>sempre expresso</b>, mesmo quando é o mesmo do verbo principal, o que nunca acontece com o sujeito de um verbo conjugado, normalmente omitido (A&G § 581; Ravizza n. 380 a): <i>Dīcō <b>mē</b> fessum esse</i>, "Digo que estou cansado"; <i>Putās <b>tē</b> errāre?</i>, "Achas que estás errado?".</p>
<h3>O reflexivo indireto</h3>
<p>Na terceira pessoa surge uma pergunta que o português resolve mal: em "Marco diz que <i>ele</i> vem", quem vem, o próprio Marco ou outra pessoa? O latim não deixa dúvida. Como você viu no capítulo 14, <i>sē</i> e <i>suus</i> apontam para o sujeito; na oração infinitiva, eles apontam para o <b>sujeito do verbo principal</b>, aquele que diz ou pensa (o "reflexivo indireto": Bennett § 244.1 II; A&G § 300; Ravizza n. 380 a):</p>
{comparacao('Sē e suus × eum e eius na oração infinitiva', ['Latim', 'Quem é', 'Português'], [
    ['Mārcus dīcit <b>sē</b> venīre.', '<i>sē</i> = Marco', 'Marco diz que (ele mesmo) vem.'],
    ['Mārcus dīcit <b>eum</b> venīre.', '<i>eum</i> = outra pessoa', 'Marco diz que ele (Paulo, por exemplo) vem.'],
    ['Mārcus dīcit amīcōs <b>suōs</b> venīre.', '<i>suōs</i> = de Marco', 'Marco diz que os amigos dele (seus próprios amigos) vêm.'],
    ['Mārcus dīcit amīcōs <b>eius</b> venīre.', '<i>eius</i> = de outra pessoa', 'Marco diz que os amigos dele (de Paulo) vêm.'],
    ['Puellae putant <b>sē</b> laudātās esse.', '<i>sē</i> = as meninas', 'As meninas pensam que foram elogiadas.'],
])}
<p>Note a última linha: <i>sē</i> serve para o singular e para o plural, e quem mostra o gênero e o número é o particípio (<i>laudātās</i>, feminino plural). Num texto autêntico, Cícero conta como Creso entendeu o oráculo segundo o qual, atravessando o rio Hális, ele derrubaria "uma grande potência": <i>hostium vim sē perversūrum putāvit</i>, "pensou que destruiria o poder dos inimigos" (<i>Div.</i> 2.115). O império destruído acabou sendo o dele.</p>
{diagrama_frase([('(Croesus)', 'sujeito de putāvit · subentendido'), ('hostium vim', 'acusativo · objeto do infinitivo'), ('sē', 'acusativo · sujeito do infinitivo = Creso'), ('perversūrum', 'infinitivo futuro · esse omitido'), ('putāvit', 'verbo principal · "pensou"')], '<i>Hostium vim sē perversūrum putāvit</i> (Cícero, <i>Div.</i> 2.115): o reflexivo <i>sē</i> retoma o sujeito de <i>putāvit</i>; <i>perversūrum</i> (de <i>pervertō</i>, "derrubar") concorda com <i>sē</i> no acusativo masculino singular, e a ação é posterior ao "pensar".')}
{observacao('Dois acusativos: quem faz o quê?', 'Quando o infinitivo é transitivo, a oração tem dois acusativos, e a frase pode ficar ambígua. O exemplo clássico é o oráculo que, segundo Ênio, Apolo teria dado ao rei Pirro, citado por Cícero (<i>Div.</i> 2.116): <i>aiō tē, Aeacida, Rōmānōs vincere posse</i>. Quer dizer "digo que tu, descendente de Éaco, podes vencer os romanos" ou "digo que os romanos podem vencer-te"? As duas leituras são gramaticais, e por isso o oráculo não podia errar. Em prosa, a ordem das palavras costuma resolver (o sujeito vem em geral primeiro), e quem escreve pode evitar a dúvida passando o infinitivo para a passiva (Ravizza n. 378, obs. 1).')}
'''),
        ('A passiva: dīcitur e vidētur', f'''
<p>Para dizer "diz-se que Marco vem", o latim tem duas construções. A mais comum nos tempos simples é a <b>pessoal</b>: o sujeito da oração dependente passa a ser o sujeito do verbo passivo, no <b>nominativo</b>, e o infinitivo fica (Bennett § 332; A&G § 582; Kennedy § 370; Ravizza nn. 238–240):</p>
{exemplos([
    ('<b>Mārcus</b> venīre <b>dīcitur</b>.', 'Diz-se que Marco vem. (literalmente "Marco é dito vir")'),
    ('<b>Rōmulus</b> prīmus rēx fuisse <b>dīcitur</b>.', 'Diz-se que Rômulo foi o primeiro rei.'),
    ('<b>Hostēs</b> appropinquāre <b>nūntiantur</b>.', 'Anuncia-se que os inimigos se aproximam.'),
    ('<b>Tū</b> mihi errāre <b>vidēris</b>.', 'Parece-me que você está errado. (literalmente "tu me pareces errar")'),
])}
<p>Repare que o predicativo também vai para o nominativo (<i>prīmus rēx</i>), porque concorda com o sujeito de <i>dīcitur</i>. Assim se constroem <i>dīcor, putor, exīstimor, videor</i> em todas as pessoas, e <i>fertur, feruntur, trāditur, trāduntur</i> (diz-se, conta-se) na terceira (Bennett § 332 c, d). Um exemplo autêntico, de Cícero: <i>Epamīnōndās ... fidibus praeclārē cecinisse dīcitur</i>, "diz-se que Epaminondas tocava lira admiravelmente" (<i>Tusc.</i> 1.4).</p>
<p>Nos tempos compostos (<i>dictum est, trāditum est, nūntiātum est</i>) é mais comum a construção <b>impessoal</b>, com a oração infinitiva no acusativo como sujeito: <i>Trāditum est Homērum caecum fuisse</i>, "A tradição diz que Homero era cego" (Bennett § 332, nota; A&G § 582.a; Kennedy § 370, nota).</p>
{comparacao('Pessoal × impessoal', ['Latim', 'Construção', 'Português'], [
    ['Homērus caecus fuisse dīcitur.', 'pessoal: nominativo + infinitivo', 'Diz-se que Homero era cego.'],
    ['Trāditum est Homērum caecum fuisse.', 'impessoal: acusativo + infinitivo', 'Conta a tradição que Homero era cego.'],
])}
{dica('<b>Não traduza ao pé da letra.</b> "Marco é dito vir" e "tu pareces a mim errar" não são português. Use "diz-se que", "dizem que", "conta-se que", "parece que" + indicativo. Com <i>vidētur</i>, às vezes a construção pessoal soa bem também em português: <i>Mārcus fessus esse vidētur</i>, "Marco parece estar cansado".')}
'''),
        ('Vontade e sentimento: iubeō, vetō, volō, gaudeō', f'''
<p>Os verbos de <b>ordenar</b> e <b>proibir</b>, <i>iubeō</i> e <i>vetō</i>, também se constroem com acusativo e infinitivo, mas aqui o acusativo é a pessoa que recebe a ordem e o infinitivo é o que ela deve (ou não deve) fazer (Bennett § 331 II; Ravizza n. 382 d):</p>
{exemplos([
    ('Rēx mīlitēs pontem facere iubet.', 'O rei manda os soldados fazerem uma ponte.'),
    ('Pater puerōs in silvā errāre vetat.', 'O pai proíbe os meninos de vagar na floresta.'),
    ('Rēx pontem fierī iussit.', 'O rei mandou fazer uma ponte. (sem a pessoa: infinitivo passivo)'),
    ('Mīlitēs pontem facere iussī sunt.', 'Os soldados receberam ordem de fazer uma ponte. (passiva pessoal)'),
])}
<p>Quando a pessoa que recebe a ordem não é mencionada, o infinitivo vai para a passiva: <i>pontem fierī iussit</i>, literalmente "mandou a ponte ser feita" (Bennett § 331 II.a). E na passiva, <i>iubeor</i> e <i>vetor</i> seguem a construção pessoal da seção anterior: <i>mīlitēs ... iussī sunt</i> (Bennett § 332 a).</p>
<p>Com <i>volō, nōlō, mālō, cupiō</i> tudo depende do sujeito. Se é o mesmo, basta o infinitivo complementar do capítulo 27; se é outro, usa-se a oração infinitiva (Bennett § 331 IV; Ravizza n. 382 a):</p>
{exemplos([
    ('Volō venīre.', 'Quero vir. (mesmo sujeito: infinitivo simples)'),
    ('Volō <b>tē</b> venīre.', 'Quero que você venha. (outro sujeito: acusativo + infinitivo)'),
])}
<p>Por fim, os verbos de <b>sentimento</b>, como <i>gaudeō</i> (alegro-me), <i>doleō</i> (lamento) e <i>mīror</i> (admiro-me), aceitam a oração infinitiva para dizer aquilo de que alguém se alegra ou se queixa: <i>Gaudeō tē salvum advenīre</i>, "Alegro-me de que você chegue são e salvo" (Bennett § 331 V; Ravizza n. 379 c). Eles também admitem <i>quod</i> + indicativo, que põe em relevo a causa: <i>gaudeō quod valēs</i>, "estou contente porque você está bem" (Ravizza n. 383 a).</p>
<p>Um exemplo autêntico reúne quase tudo. Aníbal, já velho, conta ao rei Antíoco o juramento que o pai lhe impôs quando ele tinha nove anos, diante de um altar: <i>iūrāre iussit numquam mē in amīcitiā cum Rōmānīs fore</i>, "fez-me jurar que eu nunca seria amigo dos romanos" (Cornélio Nepos, <i>Han.</i> 2.4). <i>Iussit</i> pede o infinitivo <i>iūrāre</i>; <i>iūrāre</i>, verbo de jurar, pede uma oração infinitiva com infinitivo futuro, <i>mē ... fore</i>. A prática guiada 2 analisa a frase passo a passo.</p>
'''),
        ('Traduzir para o português e uma frase autêntica', f'''
<p>Não existe uma tradução única para a oração infinitiva. O português tem três recursos, e o bom tradutor escolhe o que soa natural em cada caso:</p>
{tabela(['Estratégia', 'Quando usar', 'Exemplo'], [
    ['"que" + indicativo', 'verbos de dizer, pensar, saber, perceber', '<i>Dīcit Mārcum venīre</i>: diz que Marco vem.'],
    ['"que" + subjuntivo', 'vontade, ordem, proibição, sentimento, esperança', '<i>Volō tē venīre</i>: quero que você venha. <i>Gaudeō tē valēre</i>: alegro-me de que você esteja bem. <i>Iussit mīlitēs abīre</i>: mandou que os soldados partissem.'],
    ['infinitivo (pessoal ou não)', 'perceber, mandar, deixar; estilo mais conciso', '<i>Videō sōlem lūcēre</i>: vejo o sol brilhar. <i>Iussit mīlitēs abīre</i>: mandou os soldados partirem. <i>Dīcit sē fessum esse</i>: diz estar cansado.'],
], 'Três maneiras de traduzir a oração infinitiva')}
<p>O terceiro recurso mostra que a construção latina não é tão estranha ao português quanto parece. Em "vejo-o nascer", "mandei-os sair", "deixa-me falar", o pronome oblíquo <i>o, os, me</i> é, historicamente, um acusativo, e é ao mesmo tempo o sujeito do infinitivo: é o acusativo com infinitivo latino, sobrevivendo com os verbos de perceber, mandar e deixar.</p>
{observacao('Quia e quod no latim cristão', 'No latim tardio e cristão, a oração infinitiva convive com uma construção nova, com <i>quod</i>, <i>quia</i> ou <i>quoniam</i> e o verbo em geral no indicativo (às vezes no subjuntivo, sem diferença de sentido; capítulo 50), muito parecida com o "que" das línguas românicas. Na Vulgata, a samaritana diz a Jesus: <i>Domine, videō quia prophēta es tū</i>, "Senhor, vejo que tu és profeta"; e logo depois: <i>vōs dīcitis quia Ierosolymis est locus ubi adōrāre oportet</i>, "vós dizeis que em Jerusalém está o lugar onde é preciso adorar" (Jo 4,19–20). Em latim clássico seria <i>videō tē prophētam esse</i>. Reconheça a construção nos textos cristãos (capítulo 50 em diante), mas, ao escrever em latim clássico, use a oração infinitiva.')}
<p>Para terminar, uma das frases mais famosas de Cícero, no começo da primeira Catilinária (63 a.C.), quando ele denuncia no Senado a conjuração de Catilina, que estava presente:</p>
{exemplos([('Patēre tua cōnsilia nōn sentīs?', 'Não percebes que os teus planos estão descobertos? (Cícero, <i>Cat.</i> 1.1)')])}
{analise('Cícero, Cat. 1.1, palavra a palavra', [
    ('Patēre', 'pateō, patēre, patuī, estar aberto, exposto', 'infinitivo presente ativo, 2ª conjugação', 'verbo da oração infinitiva; simultâneo a <i>sentīs</i>'),
    ('tua', 'tuus, -a, -um, teu', 'acusativo plural neutro', 'concorda com <i>cōnsilia</i>'),
    ('cōnsilia', 'cōnsilium, -ī (n.), plano, projeto', 'acusativo plural neutro, 2ª declinação', 'sujeito do infinitivo <i>patēre</i>'),
    ('nōn', 'nōn (advérbio)', 'invariável', 'nega <i>sentīs</i>'),
    ('sentīs', 'sentiō, sentīre, sēnsī, sēnsum, perceber, sentir', 'presente do indicativo, 2ª pessoa do singular', 'verbo principal (de percepção), que introduz a oração infinitiva'),
])}
<p>O ponto delicado é <i>cōnsilia</i>: como todo neutro, tem nominativo e acusativo iguais. Mas não pode ser sujeito de <i>sentīs</i>, que está na 2ª pessoa (o sujeito é "tu", Catilina); e o infinitivo <i>patēre</i> precisa de um sujeito. Logo, <i>tua cōnsilia</i> é o acusativo sujeito de <i>patēre</i>, e toda a oração <i>patēre tua cōnsilia</i> é o objeto de <i>sentīs</i>. Cícero ainda a coloca <b>antes</b> do verbo principal, com <i>patēre</i> na primeira posição, para dar ênfase: o que importa é que os planos estão expostos. Na tradução, porém, o verbo principal vem primeiro: "não percebes que...".</p>
<ul>
<li><b>Construção</b>: verbo de dizer, pensar, saber, perceber, sentir + sujeito no <b>acusativo</b> + verbo no <b>infinitivo</b>, sem conjunção. <i>Negō</i> = "dizer que não".</li>
<li><b>Tempo</b>: presente = simultâneo, perfeito = anterior, futuro = posterior; depois de um passado, "vinha / tinha vindo / viria". <i>Spērō, prōmittō, iūrō</i> pedem infinitivo futuro com sujeito expresso.</li>
<li><b>Concordância</b>: predicativo e particípio no acusativo; o sujeito vem sempre expresso; <i>sē/suus</i> = sujeito do verbo principal.</li>
<li><b>Passiva</b>: <i>Mārcus venīre dīcitur</i> (pessoal, nominativo); <i>trāditum est Homērum caecum fuisse</i> (impessoal, nos tempos compostos).</li>
<li><b>Vontade</b>: <i>iubeō, vetō</i> + acusativo + infinitivo; <i>volō</i> + infinitivo (mesmo sujeito) ou + oração infinitiva (outro sujeito).</li>
<li><b>Tradução</b>: "que" + indicativo, "que" + subjuntivo, ou infinitivo.</li>
</ul>
<p>O capítulo 38 amplia esta construção ao discurso indireto inteiro, em que discursos longos são relatados com orações infinitivas e subordinadas no subjuntivo.</p>
'''),
    ],
    erros_comuns=[
        ('Procurar em latim uma conjunção para o "que" ("<i>Dīcō quod Mārcus venit</i>").', 'No latim clássico, depois de verbos de dizer e pensar, não há conjunção: <i>Dīcō Mārcum venīre</i>. A construção com <i>quod</i> ou <i>quia</i> (em geral com indicativo) é do latim tardio e cristão; reconheça-a nos textos cristãos, mas não a use ao escrever latim clássico.'),
        ('Traduzir o infinitivo pelo tempo "dele" sem olhar o verbo principal (<i>Dīxit Mārcum venīre</i> → "disse que Marco vem").', 'O infinitivo presente é simultâneo ao verbo principal; se este está no passado, a ação também está: "disse que Marco <b>vinha</b>". Do mesmo modo, <i>dīxit Mārcum ventūrum esse</i> é "disse que viria", e não "disse que virá".'),
        ('Usar <i>eum</i> ou <i>eius</i> para o próprio sujeito do verbo principal (<i>Mārcus dīcit eum aegrum esse</i> querendo dizer "Marco diz que está doente").', 'Para o sujeito do verbo principal, o latim usa <i>sē</i> e <i>suus</i>: <i>Mārcus dīcit sē aegrum esse</i>. <i>Eum</i> e <i>eius</i> apontam para outra pessoa. É o reflexivo indireto anunciado no capítulo 14.'),
        ('Omitir o sujeito quando ele é o mesmo do verbo principal (<i>Spērō venīre</i>, para "espero vir").', 'Na oração infinitiva o sujeito vem sempre expresso, e os verbos de esperar e prometer pedem infinitivo futuro: <i>Spērō mē ventūrum esse</i>. O português "espero vir" esconde essas duas exigências.'),
        ('Deixar o predicativo no nominativo (<i>Putō Iūliam laeta esse</i>).', 'Tudo o que concorda com o sujeito acusativo vai para o acusativo: <i>Putō Iūliam laetam esse</i>; <i>Sciō epistulam scrīptam esse</i>. Só na construção pessoal (<i>Iūlia laeta esse dīcitur</i>) o predicativo fica no nominativo, porque o sujeito também está.'),
        ('Traduzir a construção pessoal ao pé da letra ("Homero é dito ter sido cego").', '<i>Homērus caecus fuisse dīcitur</i> é "diz-se que Homero era cego" ou "dizem que Homero foi cego". Transforme o nominativo em sujeito da oração com "que" e o infinitivo em verbo conjugado, segundo o tempo relativo.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Do discurso direto à oração infinitiva',
            'Marco diz: <i lang="la">"Iūlia in hortō ambulat."</i> Relate a frase em latim depois de <i>Mārcus dīcit</i> e depois de <i>Mārcus dīxit</i>, e traduza. Depois faça o mesmo com <i lang="la">"Iūlia in hortō ambulāvit"</i> e com <i lang="la">"Ego crās veniam"</i> (<i>crās</i>, amanhã).', [
            ('O que acontece com o sujeito <i>Iūlia</i> e com o verbo <i>ambulat</i>?', 'O sujeito vai para o acusativo, <i>Iūliam</i>; o verbo vai para o infinitivo. Como a ação é simultânea à fala, infinitivo presente: <i>ambulāre</i>. <i>In hortō</i> não muda.'),
            ('Escreva e traduza com <i>dīcit</i> e com <i>dīxit</i>.', '<i>Mārcus dīcit Iūliam in hortō ambulāre</i>: "Marco diz que Júlia passeia no jardim". <i>Mārcus dīxit Iūliam in hortō ambulāre</i>: "Marco disse que Júlia passeava no jardim". A forma latina é a mesma; o tempo português muda.'),
            ('E se a frase direta for <i>Iūlia in hortō ambulāvit</i>?', 'A ação é anterior à fala: infinitivo perfeito, <i>ambulāvisse</i>. <i>Mārcus dīcit Iūliam in hortō ambulāvisse</i>, "diz que Júlia passeou"; com <i>dīxit</i>, "disse que Júlia tinha passeado".'),
            ('Agora <i>Ego crās veniam</i>: quem é o sujeito do infinitivo?', 'O próprio Marco, que é o sujeito de <i>dīcit</i>. O sujeito deve vir expresso, e como é o mesmo do verbo principal, é o reflexivo <i>sē</i>. A ação é posterior: infinitivo futuro, concordando com <i>sē</i> (masculino singular): <i>ventūrum esse</i>.'),
            ('Escreva e traduza.', '<i>Mārcus dīcit sē crās ventūrum esse</i>: "Marco diz que virá amanhã". <i>Mārcus dīxit sē crās ventūrum esse</i>: "Marco disse que viria amanhã". O <i>ego</i> do discurso direto virou <i>sē</i>.'),
        ]),
        pratica_guiada('Prática guiada 2 · O juramento de Aníbal',
            'Aníbal conta o que o pai, Amílcar, fez diante do altar: <i lang="la">[pater mē] iūrāre iussit numquam mē in amīcitiā cum Rōmānīs fore.</i> (Cornélio Nepos, <i>Han.</i> 2.4; no texto, o objeto de <i>iussit</i> está numa frase anterior, e por isso vai entre colchetes.) Vocabulário: <i>iūrō, -āre</i>, jurar; <i>numquam</i>, nunca; <i>amīcitia, -ae</i>, amizade.', [
            ('Qual é o verbo principal e o que ele pede?', '<i>Iussit</i>, perfeito de <i>iubeō</i>, "mandou". Pede a pessoa que recebe a ordem no acusativo (<i>mē</i>, subentendido aqui) e um infinitivo: <i>iūrāre</i>. "Mandou-me jurar", "fez-me jurar".'),
            ('<i>Iūrāre</i> também introduz alguma coisa?', 'Sim: jurar é um verbo de dizer (como prometer), e pede uma oração infinitiva com o conteúdo do juramento: <i>numquam mē in amīcitiā cum Rōmānīs fore</i>.'),
            ('Qual é o sujeito e qual o verbo dessa oração?', 'Sujeito: <i>mē</i>, no acusativo (o próprio Aníbal, que fala). Verbo: <i>fore</i>, infinitivo futuro de <i>sum</i> (= <i>futūrum esse</i>, capítulo 27). Como verbo de jurar, <i>iūrō</i> pede infinitivo futuro: a ação é posterior ao juramento.'),
            ('Como traduzir o tempo?', 'O verbo principal está no passado (<i>iussit</i>), e a ação é posterior: em português, futuro do pretérito, "seria".'),
            ('Monte a tradução.', '"Fez-me jurar que eu nunca seria amigo dos romanos" (literalmente "que nunca eu estaria em amizade com os romanos").'),
        ], 'Repare que aqui o sujeito do infinitivo é <i>mē</i>, e não <i>sē</i>: quem fala é Aníbal, em primeira pessoa. O reflexivo <i>sē</i> só se usa na terceira pessoa.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Encontre a oração infinitiva', 'Em cada frase, indique o verbo principal, o sujeito acusativo e o infinitivo, diga a relação de tempo e traduza. Vocabulário: <i>nūntius, -ī</i>, mensageiro; <i>Rōmae</i>, em Roma; <i>nauta, -ae</i>, marinheiro; <i>fugiō, -ere, fūgī</i>, fugir.', [
            ('<i>Sciō tē Latīnē legere.</i>', 'Verbo principal <i>sciō</i>; sujeito <i>tē</i>; infinitivo <i>legere</i> (presente: simultâneo). "Sei que você lê latim."'),
            ('<i>Nūntius dīcit hostēs vēnisse.</i>', '<i>Dīcit</i>; <i>hostēs</i> (acusativo plural); <i>vēnisse</i> (perfeito: anterior). "O mensageiro diz que os inimigos vieram (chegaram)."'),
            ('<i>Putābam Mārcum Rōmae esse.</i>', '<i>Putābam</i> (imperfeito); <i>Mārcum</i>; <i>esse</i> (simultâneo a um passado). "Eu pensava que Marco estava em Roma."'),
            ('<i>Crēdimus urbem captum īrī.</i>', '<i>Crēdimus</i>; <i>urbem</i>; <i>captum īrī</i> (futuro passivo, invariável: posterior). "Cremos que a cidade será tomada."'),
            ('<i>Negant nautās fūgisse.</i>', '<i>Negant</i> = "dizem que não"; <i>nautās</i>; <i>fūgisse</i> (anterior). "Dizem que os marinheiros não fugiram."'),
            ('<i>Audīvī puellās in hortō cantāre.</i>', '<i>Audīvī</i>; <i>puellās</i>; <i>cantāre</i> (simultâneo a um passado). "Ouvi as meninas cantarem no jardim" ou "ouvi que as meninas cantavam no jardim".'),
        ]),
        exercicio('Exercício 2 · Relate a frase', 'Passe cada frase para uma oração infinitiva depois de <i>Nūntius dīcit</i> e depois de <i>Nūntius dīxit</i>, e traduza as duas versões.', [
            ('<i>Mīlitēs pugnant.</i>', '<i>... mīlitēs pugnāre.</i> "Diz que os soldados lutam" / "disse que os soldados lutavam". Presente: simultâneo.'),
            ('<i>Mīlitēs pugnāvērunt.</i>', '<i>... mīlitēs pugnāvisse.</i> "Diz que os soldados lutaram" / "disse que os soldados tinham lutado". Perfeito: anterior.'),
            ('<i>Mīlitēs pugnābunt.</i>', '<i>... mīlitēs pugnātūrōs esse.</i> "Diz que os soldados lutarão" / "disse que os soldados lutariam". Futuro, com <i>pugnātūrōs</i> no acusativo masculino plural.'),
            ('<i>Urbs dēlēta est.</i>', '<i>... urbem dēlētam esse.</i> "Diz que a cidade foi destruída" / "disse que a cidade tinha sido destruída". <i>Dēlētam</i> concorda com <i>urbem</i>.'),
            ('<i>Rēx laetus erit.</i>', '<i>... rēgem laetum fore</i> (ou <i>futūrum esse</i>). "Diz que o rei estará alegre" / "disse que o rei estaria alegre". Predicativo <i>laetum</i> no acusativo.'),
        ]),
        exercicio('Exercício 3 · Sē ou eum? Suus ou eius?', 'Escolha a forma correta para o sentido pedido e justifique. Vocabulário: <i>aeger, -gra, -grum</i>, doente; <i>vincō, -ere, vīcī</i>, vencer.', [
            ('Marco diz que ele mesmo está doente: <i>Mārcus dīcit (sē / eum) aegrum esse.</i>', '<i>Sē</i>: refere-se ao sujeito de <i>dīcit</i>. Com <i>eum</i>, o doente seria outra pessoa.'),
            ('As meninas pensam que (elas) serão elogiadas: <i>Puellae putant (sē / eās) laudātum īrī.</i>', '<i>Sē</i>, pelo mesmo motivo. Note que <i>laudātum īrī</i> não concorda com <i>sē</i>: o futuro passivo é invariável.'),
            ('O rei anuncia que os soldados dele (do próprio rei) venceram: <i>Rēx nūntiat mīlitēs (suōs / eius) vīcisse.</i>', '<i>Suōs</i>, concordando com <i>mīlitēs</i>: os soldados pertencem ao sujeito de <i>nūntiat</i>.'),
            ('Júlia sabe que (ela mesma) é amada pela mãe: <i>Iūlia scit (sē / eam) ā mātre amārī.</i>', '<i>Sē</i>; o infinitivo presente passivo <i>amārī</i> indica simultaneidade; <i>ā mātre</i> é o agente da passiva.'),
            ('Paulo diz que Marco viu o irmão de uma terceira pessoa (Tito, por exemplo): <i>Paulus dīcit Mārcum frātrem (suum / eius) vīdisse.</i>', '<i>Eius</i>: o irmão não pertence a nenhum dos dois sujeitos. Repare que, nesta frase, <i>suum</i> seria ambíguo, porque o reflexivo pode remeter tanto ao sujeito do infinitivo (Marco: reflexivo direto) quanto ao sujeito do verbo principal (Paulo: reflexivo indireto); só o contexto decide (Bennett § 244.1; A&G § 300).'),
        ]),
        exercicio('Exercício 4 · Passiva, ordem e vontade', 'Traduza. Vocabulário: <i>appropinquō, -āre</i>, aproximar-se; <i>imperātor, -ōris</i>, general; <i>castra, -ōrum</i> (n. pl.), acampamento; <i>mūniō, -īre</i>, fortificar; <i>valeō, -ēre</i>, estar bem de saúde.', [
            ('<i>Rōmulus prīmus rēx Rōmānōrum fuisse dīcitur.</i>', '"Diz-se que Rômulo foi o primeiro rei dos romanos." Construção pessoal: <i>Rōmulus</i> e <i>prīmus rēx</i> no nominativo.'),
            ('<i>Hostēs appropinquāre nūntiantur.</i>', '"Anuncia-se que os inimigos se aproximam" (chegam notícias de que se aproximam).'),
            ('<i>Imperātor mīlitēs castra mūnīre iussit.</i>', '"O general mandou os soldados fortificarem o acampamento." <i>Mīlitēs</i> é a pessoa que recebe a ordem; <i>castra</i>, objeto de <i>mūnīre</i>.'),
            ('<i>Imperātor castra mūnīrī iussit.</i>', '"O general mandou fortificar o acampamento." Sem a pessoa, o infinitivo vai para a passiva (<i>mūnīrī</i>).'),
            ('<i>Mīlitēs castra mūnīre iussī sunt.</i>', '"Os soldados receberam ordem de fortificar o acampamento." Passiva pessoal de <i>iubeō</i>.'),
            ('<i>Volō tēcum venīre. — Volō tē mēcum venīre.</i>', '"Quero ir com você" (mesmo sujeito: infinitivo simples). "Quero que você venha comigo" (outro sujeito: acusativo <i>tē</i> + infinitivo).'),
            ('<i>Gaudeō tē valēre.</i>', '"Alegro-me de que você esteja bem." Verbo de sentimento: em português, "que" + subjuntivo.'),
        ]),
        exercicio('Exercício 5 · Retroversão', 'Passe para o latim. Vocabulário: <i>crās</i>, amanhã; <i>fessus, -a, -um</i>, cansado; <i>caecus, -a, -um</i>, cego.', [
            ('Sei que você é bom.', '<i>Sciō tē bonum esse</i> (a uma mulher, <i>bonam</i>). Sujeito e predicativo no acusativo.'),
            ('Os mensageiros anunciaram que a cidade tinha sido tomada.', '<i>Nūntiī nūntiāvērunt urbem captam esse.</i> Perfeito passivo: anterior a um passado; <i>captam</i> concorda com <i>urbem</i>.'),
            ('Marco espera vir amanhã.', '<i>Mārcus spērat sē crās ventūrum esse.</i> <i>Spērō</i> pede sujeito expresso (<i>sē</i>) e infinitivo futuro.'),
            ('Júlia diz que não está cansada.', '<i>Iūlia negat sē fessam esse.</i> <i>Negō</i> em vez de <i>dīcō ... nōn</i>; <i>sē</i> porque é a própria Júlia; <i>fessam</i>, feminino, no acusativo.'),
            ('Diz-se que o poeta era cego.', '<i>Poēta caecus fuisse dīcitur</i> (construção pessoal, preferida), ou, menos comum nos tempos simples, <i>dīcitur poētam caecum fuisse</i>. Infinitivo perfeito: anterior ao "dizer".'),
            ('O pai mandou o filho ler o livro.', '<i>Pater fīlium librum legere iussit.</i> <i>Fīlium</i>, quem recebe a ordem; <i>librum</i>, objeto de <i>legere</i>.'),
        ]),
        exercicio('Exercício 6 · Textos autênticos', 'Analise a oração infinitiva (ou a construção que a substitui) e traduza. Os macrons foram acrescentados.', [
            ('<i>cōnstrictam iam hōrum omnium scientiā tenērī coniūrātiōnem tuam nōn vidēs?</i> (Cícero, <i>Cat.</i> 1.1, continuação da frase da seção 6; <i>cōnstrictus, -a, -um</i>, amarrado, contido; <i>hōrum omnium</i>, "de todos estes"; <i>scientia, -ae</i>, conhecimento; <i>coniūrātiō, -ōnis</i>, conjuração)', 'Verbo principal <i>vidēs</i>; sujeito acusativo <i>coniūrātiōnem tuam</i>; infinitivo presente passivo <i>tenērī</i> (simultâneo); <i>cōnstrictam</i> concorda com <i>coniūrātiōnem</i>. "Não vês que a tua conjuração já está presa, amarrada pelo conhecimento de todos estes?" De novo, a oração infinitiva vem antes do verbo principal.'),
            ('<i>Epamīnōndās, prīnceps meō iūdiciō Graeciae, fidibus praeclārē cecinisse dīcitur.</i> (Cícero, <i>Tusc.</i> 1.4; <i>meō iūdiciō</i>, a meu juízo; <i>fidēs, -ium</i> (f. pl.), lira; <i>canō, -ere, cecinī</i>, cantar, tocar; <i>praeclārē</i>, admiravelmente)', 'Construção pessoal: sujeito <i>Epamīnōndās</i> no nominativo, com <i>dīcitur</i>; infinitivo perfeito <i>cecinisse</i>, anterior. "Epaminondas, a meu juízo o primeiro homem da Grécia, tocava lira admiravelmente, segundo se diz."'),
            ('<i>aiō tē, Aeacida, Rōmānōs vincere posse.</i> (Ênio, citado por Cícero, <i>Div.</i> 2.116; <i>aiō</i>, digo, afirmo; <i>Aeacida</i>, vocativo, "descendente de Éaco", isto é, Pirro)', 'Verbo principal <i>aiō</i>; infinitivo <i>posse</i> com o complemento <i>vincere</i>; dois acusativos, <i>tē</i> e <i>Rōmānōs</i>, e qualquer um pode ser o sujeito: "digo que tu podes vencer os romanos" ou "digo que os romanos podem vencer-te". Cícero cita o verso justamente como exemplo de oráculo ambíguo.'),
            ('<i>Domine, videō quia prophēta es tū.</i> (Jo 4,19, Vulgata)', 'Não há oração infinitiva: <i>quia</i> + indicativo (<i>es</i>) faz o papel do "que", como no latim cristão. "Senhor, vejo que tu és profeta." Em latim clássico: <i>videō tē prophētam esse</i>.'),
        ]),
    ],
    leituras=['ravizza-gramatica-latina', 'collar-the-gate-to-caesar-de-bello-gallico-ii-simplificado-e-original', 'nepos-vita-hannibalis', 'eutropius-breviarium-ab-urbe-condita', 'henderson-in-catilinam-i-com-notas-e-vocabulario', 'vulgata-biblia-sacra-vulgata-editio-clementina'],
    leituras_nota='O Pe. Ravizza trata a oração infinitiva em português, com muitos exemplos (nn. 377–385). Para treinar a leitura, comece por Eutrópio, que relata o que se diz e se pensa com orações infinitivas curtas, e passe à <i>Gate to Caesar</i>, que apresenta o livro II da <i>Guerra da Gália</i> em versão simplificada e original: em César, quase todo relato de mensagens e discursos usa esta construção (preparação para o capítulo 44). A <i>Vida de Aníbal</i> de Nepos contém o juramento da prática guiada 2, e a primeira Catilinária comentada por Henderson começa com a frase analisada na seção 6. Nos Evangelhos da Vulgata, compare as orações infinitivas com as construções com <i>quia</i>.',
)
