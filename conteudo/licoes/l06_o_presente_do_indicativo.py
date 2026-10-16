from conteudo.util import (tabela, tabela_conjugacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='06-o-presente-do-indicativo', titulo='O presente do indicativo: esse e as quatro conjugações', titulo_latim='Dē verbō: tempus praesēns', tempo='60 min',
    resumo='O verbo como núcleo da frase: as terminações de pessoa e número, o presente de esse (ser, estar, haver), as quatro conjugações reconhecidas pelo infinitivo, a entrada de dicionário de um verbo, a negação com nōn e a diferença de quantidade e de acento entre monēre e regere.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['verbo', 'pessoa e número', 'terminações pessoais', 'presente do indicativo', 'esse (sum, es, est)', 'predicativo do sujeito', 'est / sunt existencial ("há")',
             'quatro conjugações', 'verbos em -iō (capiō)', 'infinitivo presente', 'entrada de dicionário do verbo', 'negação com nōn', 'monēre × regere: quantidade e acento',
             'cognatos portugueses', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 2: sujeito, objeto e a concordância do verbo com o sujeito (terminações -t e -nt). Os capítulos 3 a 5 (casos, primeira e segunda declinações, adjetivos de primeira classe) ajudam nos exemplos, mas não são indispensáveis.',
                       licoes=['02-como-funciona-uma-frase-latina']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 5.A.2.a (vogal breve antes de nt), § 6 (acento), §§ 93–96 (o verbo; terminações pessoais), § 98 (as quatro conjugações pelo infinitivo), § 99 (partes principais), § 100 (sum), §§ 101, 103, 105, 107 (presente de amō, moneō, regō, audiō), §§ 109–110 (verbos em -iō; capiō), § 166 (sujeito; pronome implícito no verbo), §§ 167–168 (predicativo), § 254 (concordância do verbo), §§ 257 e 259 (valores do presente)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 12 (acento), §§ 153–154 (conjugação), § 163 (terminações pessoais), § 170 (sum), §§ 171–173 (as quatro conjugações e as partes principais), § 188 (verbos em -iō), §§ 283–284 (cópula e predicativo; § 284.b, sum como verbo substantivo, "há"), § 465 (presente), § 596 (o sujeito tende a vir primeiro), § 599.a (posição da negação)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§§ 111–112 (as quatro conjugações pelo caráter do tema; amo, moneo, rego, audio)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 81 (as conjugações pela 2ª pessoa do presente e pelo infinitivo), n. 82 (esse), n. 84 (tempos primitivos), n. 85 (desinências do presente nas quatro conjugações)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina): Salmo 22,1; 1 João 4,16 e 4,18', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', nota='frases autênticas analisadas na seção 6 (texto conferido na Wikisource latina, "Vulgata Clementina/Liber Psalmorum" e "Vulgata Clementina/Joannis Epistola I")', tipo='dominio_publico'),
    ],
    objetivos=[
        'Reconhecer a pessoa e o número de qualquer verbo no presente pelas terminações <i>-ō/-m, -s, -t, -mus, -tis, -nt</i>, sem precisar de pronome sujeito.',
        'Conjugar <i>esse</i> no presente e usá-lo como cópula (com predicativo no nominativo) e no sentido de "haver, existir".',
        'Identificar a conjugação de um verbo pelo infinitivo da entrada de dicionário e conjugar no presente <i>amō, moneō, regō, audiō</i>, reconhecendo <i>capiō</i>.',
        'Distinguir <i>monēre</i> (2ª) de <i>regere</i> (3ª) pela quantidade da vogal e pronunciar cada um com o acento correto.',
        'Negar uma frase com <i>nōn</i> e analisar palavra a palavra frases autênticas da Vulgata no presente.',
    ],
    secoes=[
        ('O verbo, núcleo da frase', f'''
<p>No capítulo 2 você viu que o verbo latino "carrega" o sujeito: <i>-t</i> diz "uma pessoa faz isso", <i>-nt</i> diz "várias pessoas fazem isso". Agora vamos completar o quadro. O verbo latino traz, numa só palavra, o <b>significado</b> (amar, ver, ouvir) e a <b>pessoa gramatical</b> que o pratica: eu, tu, ele ou ela, nós, vós, eles ou elas. Por isso um verbo sozinho já é uma frase completa: <i>Cantō</i> é "eu canto"; <i>Labōrant</i> é "eles trabalham". O pronome sujeito, que o português do Brasil quase sempre diz ("eu canto", "você canta"), em latim normalmente fica de fora, porque a terminação já o expressa; ele só aparece quando há ênfase ou contraste (Bennett § 166.2).</p>
<p>Essas marcas de pessoa chamam-se <b>terminações pessoais</b> (ou desinências). São seis, três no singular e três no plural, e valem para quase todos os tempos da voz ativa; o que muda de um tempo para outro é o que vem antes delas. Aprenda-as agora e você terá metade do trabalho feito para os tempos dos capítulos 12 e 13.</p>
{tabela(['Pessoa', 'Terminação', 'Quem faz', 'Exemplo', 'Português'], [
    ['1ª sing.', '<b>-ō</b> ou <b>-m</b>', 'eu', 'cant<b>ō</b> · su<b>m</b>', 'eu canto · eu sou'],
    ['2ª sing.', '<b>-s</b>', 'tu (você)', 'cantā<b>s</b>', 'tu cantas, você canta'],
    ['3ª sing.', '<b>-t</b>', 'ele, ela', 'canta<b>t</b>', 'ele/ela canta'],
    ['1ª pl.', '<b>-mus</b>', 'nós', 'cantā<b>mus</b>', 'nós cantamos'],
    ['2ª pl.', '<b>-tis</b>', 'vós (vocês)', 'cantā<b>tis</b>', 'vós cantais, vocês cantam'],
    ['3ª pl.', '<b>-nt</b>', 'eles, elas', 'canta<b>nt</b>', 'eles/elas cantam'],
], 'As terminações pessoais da voz ativa', latim_cols=(1, 3))}
<p>A primeira pessoa tem duas formas: <i>-ō</i> na grande maioria dos verbos (<i>cantō</i>, <i>amō</i>) e <i>-m</i> em poucos, entre eles <i>sum</i> ("eu sou") e, como você verá, em outros tempos (<i>eram</i>, "eu era"). A segunda pessoa do latim é sempre "tu" e "vós"; em português do Brasil traduza naturalmente por "você" e "vocês" quando o contexto for de conversa, lembrando que o verbo português, nesse caso, vai para a terceira pessoa ("você canta").</p>
<h3>Ler a frase a partir do verbo</h3>
<p>A terminação do verbo é a pista mais segura de uma frase latina. Ela diz quantos sujeitos procurar e, muitas vezes, resolve uma palavra ambígua. Observe:</p>
{diagrama_frase([('Puellae', 'nominativo pl. · sujeito'), ('fābulās', 'acusativo pl. · objeto'), ('nōn', 'advérbio · nega o verbo'), ('nārrant', 'verbo · -nt: 3ª pl.')], '<i>Puellae fābulās nōn nārrant</i> = As meninas não contam histórias. Sozinha, <i>puellae</i> poderia ser genitivo ou dativo singular; o <i>-nt</i> de <i>nārrant</i> pede um sujeito plural e decide: é nominativo plural.')}
<p>O presente latim cobre, numa só forma, o presente simples e o presente contínuo do português: <i>Agricola in agrō labōrat</i> é "o agricultor trabalha no campo" ou "está trabalhando no campo", conforme o contexto (Bennett § 257). Também serve para verdades gerais, que valem sempre (§ 259.1): <i>Stellae in caelō lūcent</i>, "as estrelas brilham no céu".</p>
{exemplos([('Cant<b>ō</b>.', 'Eu canto. (o "eu" está na terminação)'), ('Puella cant<b>at</b>; puellae cant<b>ant</b>.', 'A menina canta; as meninas cantam.'), ('In vīllā habit<b>āmus</b>.', 'Moramos na casa. (sujeito "nós", implícito)'), ('Nautae nāvig<b>ant</b>, agricola labōr<b>at</b>.', 'Os marinheiros navegam (estão navegando), o agricultor trabalha.')])}
'''),
        ('O verbo esse: ser, estar, haver', f'''
<p>O verbo mais frequente do latim é <i>esse</i>, "ser". Ele é <b>irregular</b>: não segue nenhuma das quatro conjugações e por isso se aprende à parte, e primeiro, como fazem Bennett (§ 100), Allen &amp; Greenough (§ 170) e Ravizza (n. 82). Repare que as terminações pessoais estão todas lá, inclusive o <i>-m</i> da primeira pessoa; o que é irregular é o radical, que ora aparece como <i>es-</i>, ora como <i>s-</i>.</p>
{tabela_conjugacao('Presente do indicativo de esse, "ser"', [
    ('su<b>m</b>', 'eu sou, estou'), ('e<b>s</b>', 'tu és, você é'), ('es<b>t</b>', 'ele/ela é, está; há'),
    ('su<b>mus</b>', 'nós somos, estamos'), ('es<b>tis</b>', 'vós sois, vocês são'), ('su<b>nt</b>', 'eles/elas são, estão; há')])}
<p>O infinitivo é <i>esse</i>, "ser". A forma de dicionário reúne as partes principais, <i>sum, esse, fuī, futūrus</i>; por enquanto bastam as duas primeiras, <i>sum, esse</i>.</p>
<h3>Esse como cópula: o predicativo no nominativo</h3>
<p>Na maioria das frases, <i>esse</i> liga o sujeito a algo que se diz dele: "Marco é agricultor", "as meninas estão alegres". Nesse papel ele se chama <b>cópula</b> (do latim <i>cōpula</i>, "laço"), e aquilo que se diz do sujeito é o <b>predicativo</b>. A regra é a mais importante desta seção: o predicativo fica <b>no mesmo caso do sujeito, o nominativo</b> (Bennett § 168; A&amp;G § 284). O motivo é lógico: o predicativo não sofre a ação do verbo, como um objeto; ele é outro nome para o próprio sujeito, e por isso usa o mesmo "crachá". Quando o predicativo é um adjetivo, ele concorda com o sujeito também em gênero e número.</p>
{exemplos([('Mārcus agricol<b>a</b> est.', 'Marco é agricultor. (<i>agricola</i>: nominativo, predicativo)'), ('Puell<b>ae</b> laet<b>ae</b> sunt.', 'As meninas estão alegres. (<i>laetae</i>: nominativo plural feminino, como <i>puellae</i>)'), ('Nautae sumus.', 'Somos marinheiros. (sujeito "nós" na terminação; <i>nautae</i>, nominativo plural)'), ('Amīca bona es.', 'Você é uma boa amiga.'), ('Rosa in mēnsā est.', 'A rosa está na mesa.')])}
{observacao('Ser, estar ou haver?', 'O português distingue "ser" (qualidade permanente) de "estar" (estado ou lugar); o latim não. <i>Puella laeta est</i> pode ser "a menina é alegre" ou "está alegre", e é o contexto que decide. Com uma expressão de lugar, como <i>in mēnsā</i>, a tradução natural é "estar".')}
<h3>Est e sunt: "há"</h3>
<p>Sem predicativo, <i>esse</i> significa "existir", e o português o traduz por <b>"há" ou "existe"</b>. Allen &amp; Greenough chamam esse uso de verbo substantivo e dão o exemplo <i>Sunt virī fortēs</i>, "há homens corajosos" (§ 284.b). Repare que o latim conjuga o verbo com o que existe, que é o sujeito: muitas rosas pedem <i>sunt</i>, uma casa pede <i>est</i>. O português, ao contrário, diz "há" nos dois casos. Nesse sentido, o verbo aparece muitas vezes no começo da frase ou logo depois da expressão de lugar, como nos exemplos abaixo.</p>
{exemplos([('Est vīlla in īnsulā.', 'Há uma casa na ilha.'), ('In silvā sunt lupī.', 'Na floresta há lobos. (<i>lupī</i>, nominativo plural, é o sujeito de <i>sunt</i>)'), ('In hortō multae rosae sunt.', 'No jardim há muitas rosas.')])}
<h3>A negação: nōn antes do verbo</h3>
<p>Para negar, o latim usa o advérbio <i>nōn</i>, "não". Quando a negação recai sobre a frase toda, <i>nōn</i> fica normalmente <b>logo antes do verbo</b>; quando nega uma palavra em especial, vem antes dela, e quando é enfática pode abrir a frase (A&amp;G § 599.a). É a mesma posição do "não" português, o que facilita a vida: <i>Puer nōn labōrat</i> é "o menino não trabalha"; <i>Nōn sunt nautae</i>, "não são marinheiros".</p>
{exemplos([('Servī <b>nōn</b> sunt malī.', 'Os escravos não são maus.'), ('<b>Nōn</b> sumus nautae; agricolae sumus.', 'Não somos marinheiros; somos agricultores.'), ('In īnsulā <b>nōn</b> est aqua.', 'Na ilha não há água.')])}
'''),
        ('As quatro conjugações e a entrada de dicionário', f'''
<p>Fora <i>esse</i> e alguns poucos irregulares, os verbos latinos se distribuem em <b>quatro conjugações</b>, quatro famílias com o mesmo jogo de terminações pessoais, mas com uma vogal diferente antes delas. Assim como as declinações dos nomes se reconhecem pelo genitivo singular, as conjugações se reconhecem pelo <b>infinitivo presente</b>, a forma terminada em <i>-re</i> que corresponde ao nosso "amar, ver, ler, ouvir" (Bennett § 98; A&amp;G § 171):</p>
{tabela(['Conjugação', 'Infinitivo', 'Vogal', 'Verbo-modelo', 'Significado'], [
    ['1ª', '-<b>āre</b>', 'ā longo', 'amō, am<b>āre</b>', 'amar'],
    ['2ª', '-<b>ēre</b>', 'ē longo', 'moneō, mon<b>ēre</b>', 'advertir, aconselhar'],
    ['3ª', '-<b>ere</b>', 'e breve', 'regō, reg<b>ere</b>', 'reger, governar, dirigir'],
    ['4ª', '-<b>īre</b>', 'ī longo', 'audiō, aud<b>īre</b>', 'ouvir'],
    ['3ª (em -iō)', '-<b>ere</b>', 'e breve', 'capiō, cap<b>ere</b>', 'pegar, tomar'],
], 'As quatro conjugações pelo infinitivo', latim_cols=(1, 3))}
<p>A diferença entre a 2ª e a 3ª conjugação está toda na <b>quantidade</b> da vogal: <i>-ēre</i> longo em <i>monēre</i>, <i>-ere</i> breve em <i>regere</i>. Nos textos sem macron as duas se escrevem igual, e é por isso que este capítulo dedica uma seção inteira ao par (seção 5).</p>
<h3>Como o dicionário apresenta um verbo</h3>
<p>O dicionário não registra o infinitivo como verbete, como faz o português ("amar"). Ele registra primeiro a <b>1ª pessoa do singular do presente</b> e logo depois o <b>infinitivo</b>: <i>amō, amāre</i>; muitas vezes de forma abreviada, <i>amō, -āre</i>. Em seguida vêm mais duas formas, o perfeito e o particípio (<i>amō, amāre, amāvī, amātum</i>), que formam o conjunto das <b>partes principais</b> do verbo (Bennett § 99; A&amp;G § 172); você as estudará no capítulo 13. Ravizza chama essas formas de "tempos primitivos" e lembra que são elas que o dicionário fornece (n. 84). Por ora, trabalhe só com as duas primeiras.</p>
<p>Por que a primeira pessoa não basta? Porque ela engana. <i>Amō</i> e <i>regō</i> terminam igual, mas são de conjugações diferentes; <i>audiō</i> e <i>capiō</i> também. E <i>creō</i> ("criar", o verbo de <i>creāvit</i> em Gn 1,1) termina em <i>-eō</i> como <i>moneō</i>, mas é da primeira conjugação: <i>creō, creāre</i>. Só o infinitivo resolve. Ravizza ensina ainda uma segunda pista, a 2ª pessoa do singular: <i>amās, monēs, regis, audīs</i> (n. 81).</p>
{comparacao('Entradas de dicionário: o que cada parte informa', ['Entrada', 'Conjugação', 'Por quê'], [
    ['amō, -āre', '1ª', 'infinitivo em <i>-āre</i>'],
    ['creō, -āre', '1ª', 'o <i>-eō</i> engana; o infinitivo <i>creāre</i> decide'],
    ['videō, -ēre', '2ª', 'infinitivo em <i>-ēre</i> (longo); 1ª pessoa em <i>-eō</i>'],
    ['dūcō, -ere', '3ª', 'infinitivo em <i>-ere</i> (breve); 1ª pessoa sem <i>e</i> antes do <i>-ō</i>'],
    ['veniō, -īre', '4ª', 'infinitivo em <i>-īre</i>'],
    ['faciō, -ere', '3ª em -iō', 'primeira pessoa como <i>audiō</i>, infinitivo como <i>regere</i>'],
])}
<h3>O infinitivo presente</h3>
<p>O infinitivo presente ativo termina em <i>-re</i> (<i>amāre, monēre, regere, audīre, capere</i>), com a exceção de <i>esse</i>. Ele equivale ao infinitivo português e funciona como um <b>substantivo</b> que exprime a ação (A&amp;G § 157.d): pode, por exemplo, ser sujeito de <i>est</i> (Bennett § 166.1.b). Nesse caso o predicativo vai para o neutro singular, como no exemplo de Bennett <i>decōrum est prō patriā morī</i>, "morrer pela pátria é belo":</p>
{exemplos([('<b>Cantāre</b> bonum est.', 'Cantar é bom. (<i>cantāre</i>, sujeito; <i>bonum</i>, neutro, predicativo)'), ('<b>Nāvigāre</b> nōn est facile.', 'Navegar não é fácil. (<i>facile</i>, "fácil", é um adjetivo da 3ª declinação)')])}
'''),
        ('O presente nas quatro conjugações', f'''
<p>Cada conjugação forma o presente juntando ao radical a sua vogal e, depois dela, as terminações pessoais que você já conhece. Comece pela primeira conjugação, a mais regular e a mais numerosa:</p>
{tabela_conjugacao('Presente do indicativo da 1ª conjugação: amō, amāre, "amar"', [
    ('am<b>ō</b>', 'eu amo'), ('amā<b>s</b>', 'tu amas, você ama'), ('ama<b>t</b>', 'ele/ela ama'),
    ('amā<b>mus</b>', 'nós amamos'), ('amā<b>tis</b>', 'vós amais, vocês amam'), ('ama<b>nt</b>', 'eles/elas amam')])}
<p>Dois detalhes de quantidade aparecem já aqui e se repetem em todas as conjugações. Primeiro, na 1ª pessoa o <i>ā</i> do tema desaparece diante do <i>-ō</i>: <i>amō</i>, e não "amaō". Segundo, a vogal do tema, longa em <i>amās, amāmus, amātis</i>, é <b>breve antes de <i>-t</i> e de <i>-nt</i></b>: <i>amat, amant</i>. Antes de <i>nt</i> a vogal latina é, em regra, breve (Bennett § 5.A.2.a, que dá justamente o exemplo <i>amant</i>); e nos paradigmas de Bennett (§§ 101 e 103) <i>amat</i> e <i>monet</i> também aparecem sem macron.</p>
<p>Agora as cinco conjugações lado a lado. Leia cada coluna em voz alta, de cima para baixo:</p>
{tabela(['Pessoa', '1ª · amō', '2ª · moneō', '3ª · regō', '4ª · audiō', '3ª em -iō · capiō'], [
    ['1ª sing.', 'am<b>ō</b>', 'mone<b>ō</b>', 'reg<b>ō</b>', 'audi<b>ō</b>', 'capi<b>ō</b>'],
    ['2ª sing.', 'amā<b>s</b>', 'monē<b>s</b>', 'regi<b>s</b>', 'audī<b>s</b>', 'capi<b>s</b>'],
    ['3ª sing.', 'ama<b>t</b>', 'mone<b>t</b>', 'regi<b>t</b>', 'audi<b>t</b>', 'capi<b>t</b>'],
    ['1ª pl.', 'amā<b>mus</b>', 'monē<b>mus</b>', 'regi<b>mus</b>', 'audī<b>mus</b>', 'capi<b>mus</b>'],
    ['2ª pl.', 'amā<b>tis</b>', 'monē<b>tis</b>', 'regi<b>tis</b>', 'audī<b>tis</b>', 'capi<b>tis</b>'],
    ['3ª pl.', 'ama<b>nt</b>', 'mone<b>nt</b>', 'regu<b>nt</b>', 'audiu<b>nt</b>', 'capiu<b>nt</b>'],
    ['Infinitivo', 'amā<b>re</b>', 'monē<b>re</b>', 'rege<b>re</b>', 'audī<b>re</b>', 'cape<b>re</b>'],
], 'O presente do indicativo ativo nas quatro conjugações', latim_cols=(1, 2, 3, 4, 5))}
<p><b>2ª conjugação.</b> O <i>ē</i> longo fica visível em quase todas as formas e se conserva até na primeira pessoa (<i>moneō</i>), onde fica breve por estar antes de outra vogal. Esse <i>e</i> antes do <i>-ō</i> é a marca da 2ª no dicionário, mas, como você viu com <i>creō</i>, não é infalível.</p>
<p><b>3ª conjugação.</b> É a que pede mais atenção. A vogal de ligação é breve e muda de timbre: some diante do <i>-ō</i> (<i>regō</i>), vira <i>i</i> diante de <i>-s, -t, -mus, -tis</i> (<i>regis, regit, regimus, regitis</i>) e <i>u</i> diante de <i>-nt</i> (<i>regunt</i>). A terceira pessoa do plural em <i>-unt</i> é a forma que mais a distingue.</p>
<p><b>4ª conjugação.</b> O <i>ī</i> longo aparece em <i>audīs, audīmus, audītis</i>; fica breve antes de <i>-t</i> (<i>audit</i>) e antes de outra vogal (<i>audiō</i>), e a terceira do plural acrescenta um <i>u</i>: <i>audiunt</i>.</p>
<p><b>3ª conjugação em -iō.</b> Alguns verbos muito usados, como <i>capiō</i> (pegar), <i>faciō</i> (fazer) e <i>fugiō</i> (fugir), são da 3ª conjugação, mas conservam um <i>i</i> em parte do presente. A regra prática de Bennett (§ 109.1) é simples: eles tomam as terminações da 4ª onde estas têm duas vogais seguidas (<i>capiō</i>, <i>capiunt</i>, como <i>audiō</i>, <i>audiunt</i>) e, no resto, seguem <i>regō</i> (<i>capis, capit, capimus, capitis</i>, com <i>i</i> breve, e o infinitivo <i>capere</i>). Neste capítulo basta <b>reconhecê-los</b>: a entrada <i>capiō, -ere</i> já avisa que se trata deles.</p>
{tabela(['Conjugação', 'Verbos deste capítulo (presente, infinitivo)', 'Significado'], [
    ['1ª', 'labōrō, -āre · nārrō, -āre · spectō, -āre · laudō, -āre · creō, -āre', 'trabalhar · contar · olhar, contemplar · louvar · criar'],
    ['2ª', 'videō, -ēre · habeō, -ēre · timeō, -ēre · doceō, -ēre · maneō, -ēre', 'ver · ter · temer · ensinar · ficar, permanecer'],
    ['3ª', 'dūcō, -ere · legō, -ere · scrībō, -ere · mittō, -ere · vīvō, -ere', 'conduzir · ler · escrever · enviar · viver'],
    ['4ª', 'veniō, -īre · dormiō, -īre · sciō, -īre', 'vir · dormir · saber'],
    ['3ª em -iō', 'capiō, -ere · faciō, -ere · fugiō, -ere', 'pegar, tomar · fazer · fugir'],
], 'Vocabulário de verbos usado nos exemplos e exercícios', latim_cols=(1,))}
{exemplos([('Magistra puerōs mon<b>et</b>.', 'A professora adverte os meninos.'), ('Agricola equōs dūc<b>it</b>; servī in agrō labōr<b>ant</b>.', 'O agricultor conduz os cavalos; os escravos trabalham no campo.'), ('Puerī librōs leg<b>unt</b>.', 'Os meninos leem livros.'), ('Fābulās poētae aud<b>īmus</b>.', 'Ouvimos as histórias do poeta.'), ('Puella rosam cap<b>it</b>.', 'A menina pega a rosa.')])}
'''),
        ('Monēre ou regere? Quantidade, acento e o português', f'''
<p>A distinção entre <i>monēre</i> e <i>regere</i> é pequena no papel e grande na boca. Ela depende de uma regra que você já conhece do capítulo 1, a do acento latino: palavras de duas sílabas acentuam a primeira; palavras de três ou mais acentuam a <b>penúltima se ela for longa</b> e, se ela for breve, a <b>antepenúltima</b> (Bennett § 6.1–2; A&amp;G § 12). Em <i>mo-nē-re</i> a penúltima tem vogal longa e recebe o acento; em <i>re-ge-re</i> a penúltima é breve, e o acento recua para a antepenúltima. O mesmo vale para as formas do plural.</p>
{tabela(['Forma', 'Sílabas', 'Penúltima', 'Pronúncia (sílaba tônica sublinhada)'], [
    ['monēre', 'mo · nē · re', 'longa', 'mo<u>nē</u>re'],
    ['regere', 're · ge · re', 'breve', '<u>re</u>gere'],
    ['monēmus · monētis', 'mo · nē · mus', 'longa', 'mo<u>nē</u>mus · mo<u>nē</u>tis'],
    ['regimus · regitis', 're · gi · mus', 'breve', '<u>re</u>gimus · <u>re</u>gitis'],
    ['amāre · audīre', 'a · mā · re / au · dī · re', 'longa', 'a<u>mā</u>re · au<u>dī</u>re'],
    ['capere · capimus', 'ca · pe · re', 'breve', '<u>ca</u>pere · <u>ca</u>pimus'],
], 'O acento do infinitivo e das formas do plural', latim_cols=(0, 3))}
<p>Por que isso pede uma seção à parte? Porque o português embaralha justamente esse par. A 1ª conjugação latina deu verbos em <b>-ar</b> (<i>amāre</i> → amar, <i>labōrāre</i> → lavrar, <i>laudāre</i> → louvar) e a 4ª deu, em geral, verbos em <b>-ir</b> (<i>audīre</i> → ouvir, <i>dormīre</i> → dormir, <i>venīre</i> → vir). Mas a 2ª e a 3ª confluíram na mesma terminação <b>-er</b>, sempre oxítona: <i>vidēre</i> → ver, <i>habēre</i> → haver, <i>timēre</i> → temer, mas também <i>legere</i> → ler, <i>vīvere</i> → viver, <i>scrībere</i> → escrever e <i>regere</i> → reger. O falante de português pronuncia "re<u>ger</u>" e tende a dizer "re<u>ge</u>re" em latim; o certo é <u>re</u>gere.</p>
{comparacao('Cognatos portugueses: o que ajuda e o que engana', ['Latim', 'Conjugação', 'Português', 'Comentário'], [
    ['amāre, a<u>mā</u>re', '1ª', 'amar', '-āre → -ar: correspondência quase sempre segura'],
    ['vidēre, vi<u>dē</u>re', '2ª', 'ver', '-ēre → -er'],
    ['timēre, ti<u>mē</u>re', '2ª', 'temer', '-ēre → -er'],
    ['legere, <u>le</u>gere', '3ª', 'ler', '-ere → -er: o português apagou a diferença'],
    ['vīvere, <u>vī</u>vere', '3ª', 'viver', 'o português acentua no fim; o latim, na antepenúltima'],
    ['audīre, au<u>dī</u>re', '4ª', 'ouvir', '-īre → -ir'],
    ['fugere, <u>fu</u>gere', '3ª em -iō', 'fugir', 'cuidado: -ir em português nem sempre é 4ª conjugação'],
])}
{dica('<b>O italiano como contraprova.</b> Se você conhece italiano, ele conservou boa parte da distinção: <i>vedére</i>, <i>tenére</i> (da 2ª, tônicos na penúltima) ao lado de <i>lèggere</i>, <i>scrìvere</i>, <i>vìvere</i> (da 3ª, tônicos na antepenúltima). O português, não: aí a única pista é o macron do dicionário.')}
<p>Na prática: ao aprender um verbo em <i>-ere</i>, aprenda junto a quantidade da vogal e pronuncie o infinitivo em voz alta com o acento certo. Diante de um texto sem macrons, a primeira pessoa ajuda (<i>moneō</i> tem <i>e</i>, <i>regō</i> não), e as formas do plural decidem: <i>monent</i> é presente da 2ª; <i>regunt</i>, presente da 3ª.</p>
'''),
        ('Análise gramatical: três frases da Vulgata', f'''
<p>Com o presente de <i>esse</i> e as quatro conjugações você já reconhece o verbo de muitas frases autênticas. A Vulgata, a tradução latina da Bíblia, é um bom lugar para começar, porque usa frases curtas e ordem simples. As três a seguir foram conferidas no texto da Vulgata Clementina publicado na Wikisource latina, que não traz macrons; aqui eles foram acrescentados. Algumas palavras são da 3ª declinação (capítulo 9) ou pronomes (capítulo 14); o quadro dá a forma de cada uma.</p>
{exemplos([('Dominus regit mē.', 'O Senhor me governa (me conduz). (Sl 22,1 (23,1), Vulgata; a numeração entre parênteses é a das Bíblias que seguem o hebraico)'), ('Deus cāritās est.', 'Deus é amor. (1Jo 4,16; também em 4,8)'), ('Timor nōn est in cāritāte.', 'No amor não há temor. (1Jo 4,18)')])}
{analise('Sl 22,1; 1Jo 4,16 e 4,18, palavra a palavra', [
    ('Dominus', 'dominus, -ī (m.), senhor', 'nominativo singular, 2ª declinação', 'sujeito de <i>regit</i>'),
    ('regit', 'regō, regere (3ª), reger, governar', 'presente, 3ª pessoa do singular (<i>regi-t</i>)', 'verbo; o <i>-t</i> confirma o sujeito singular'),
    ('mē', 'pronome pessoal da 1ª pessoa', 'acusativo singular (capítulo 14)', 'objeto direto: "me"'),
    ('Deus', 'deus, -ī (m.), Deus', 'nominativo singular, 2ª declinação', 'sujeito'),
    ('cāritās', 'cāritās, -ātis (f.), amor, caridade', 'nominativo singular, 3ª declinação (capítulo 9)', 'predicativo do sujeito, no nominativo como <i>Deus</i>'),
    ('est', 'sum, esse, ser', 'presente, 3ª pessoa do singular', 'cópula: liga <i>Deus</i> a <i>cāritās</i>'),
    ('Timor', 'timor, -ōris (m.), temor, medo', 'nominativo singular, 3ª declinação', 'sujeito de <i>est</i>'),
    ('nōn', 'nōn, advérbio', 'invariável', 'nega o verbo; fica logo antes dele'),
    ('est', 'sum, esse', 'presente, 3ª pessoa do singular', 'sem predicativo: "há, existe"'),
    ('in cāritāte', 'in + cāritās, -ātis', 'ablativo singular, com <i>in</i>', 'lugar onde: "no amor"'),
])}
<p>Repare em três coisas. Em <i>Dominus regit mē</i>, <i>regit</i> é o nosso verbo-modelo da 3ª conjugação: o <i>i</i> breve diante do <i>-t</i> é exatamente o de <i>regis, regit, regimus</i>, e a pronúncia é <u>re</u>git. Em <i>Deus cāritās est</i>, dois nominativos cercam a cópula: qual é o sujeito? O contexto decide: a carta está falando de Deus e diz o que ele é; e o sujeito em primeiro lugar é a ordem mais comum (A&amp;G § 596). Os dois ficam no nominativo porque o predicativo não é objeto. Em <i>Timor nōn est in cāritāte</i>, <i>est</i> não tem predicativo, só uma expressão de lugar: é o <i>est</i> que se traduz por "há" (ou "o temor não está no amor"), e <i>nōn</i>, logo antes do verbo, nega a frase inteira.</p>
<h3>Resumo</h3>
<ul>
<li><b>Terminações pessoais</b>: <i>-ō/-m, -s, -t, -mus, -tis, -nt</i>; o pronome sujeito fica implícito.</li>
<li><b><i>Esse</i></b>: <i>sum, es, est, sumus, estis, sunt</i>; cópula com predicativo no nominativo, ou "há, existe".</li>
<li><b>Conjugações pelo infinitivo</b>: <i>-āre</i> (1ª), <i>-ēre</i> (2ª), <i>-ere</i> breve (3ª), <i>-īre</i> (4ª); <i>capiō, -ere</i> é 3ª em <i>-iō</i>.</li>
<li><b>Entrada de dicionário</b>: 1ª pessoa + infinitivo (<i>regō, -ere</i>); as outras partes vêm no capítulo 13.</li>
<li><b><i>Nōn</i></b> vai antes do verbo; <b>mo<u>nē</u>re</b> × <b><u>re</u>gere</b>: a quantidade da vogal decide o acento.</li>
</ul>
<p>O capítulo 7 mostra como achar no dicionário um verbo que aparece conjugado no texto: é a habilidade que transforma estas tabelas numa ferramenta de leitura.</p>
'''),
    ],
    erros_comuns=[
        ('Pronunciar <i>regere</i>, <i>legere</i> ou <i>scrībere</i> com o acento do português ("re<u>ge</u>re", "le<u>ge</u>re").', 'Na 3ª conjugação a penúltima sílaba do infinitivo é breve, e o acento recua: <u>re</u>gere, <u>le</u>gere, <u>scrī</u>bere. Só a 2ª conjugação acentua o <i>-ē-</i>: mo<u>nē</u>re, vi<u>dē</u>re. O português juntou as duas em "-er" e não serve de guia; o macron do dicionário, sim.'),
        ('Conjugar a 3ª conjugação como a 2ª: "regēmus", "regētis", "regent".', 'O presente da 3ª tem <i>i</i> breve e <i>u</i> na 3ª do plural: <i>regimus, regitis, regunt</i>. A forma <i>regent</i> existe, mas é <b>futuro</b> ("regerão", capítulo 12). Em <i>monent</i> (2ª) o <i>e</i> é do tema; em <i>regunt</i> não há <i>e</i>.'),
        ('Procurar um pronome sujeito que não está na frase, ou acrescentar <i>ego</i>, <i>tū</i> a cada verbo na retroversão.', 'A terminação já diz a pessoa: <i>labōrāmus</i> é "trabalhamos". O pronome latino só aparece por ênfase ou contraste (Bennett § 166.2). Ao traduzir para o latim, deixe-o de fora, a não ser que o português o destaque ("<i>eu</i> trabalho, <i>você</i> não").'),
        ('Pôr o predicativo no acusativo, como se fosse objeto: "Mārcus agricolam est", "Puellae laetās sunt".', '<i>Esse</i> não tem objeto: o predicativo é outro nome do sujeito e fica no nominativo, concordando com ele: <i>Mārcus agricola est</i>; <i>Puellae laetae sunt</i>.'),
        ('Traduzir <i>est</i> e <i>sunt</i> sempre por "é" e "são".', '<i>Esse</i> cobre "ser", "estar" e "haver". Sem predicativo, sobretudo no início da frase ou depois de uma expressão de lugar, é "há": <i>In silvā sunt lupī</i>, "na floresta há lobos" (e não "na floresta são lobos"). Repare também que o latim põe o verbo no plural quando o que existe é plural.'),
        ('Decidir a conjugação pela primeira pessoa.', '<i>Creō</i> termina em <i>-eō</i> e é da 1ª (<i>creāre</i>); <i>capiō</i> e <i>audiō</i> terminam em <i>-iō</i> e são de conjugações diferentes (<i>capere</i>, <i>audīre</i>). Consulte sempre o infinitivo da entrada de dicionário.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Decifrar uma forma verbal: monētis × regitis',
            'Num texto você encontra <i lang="la">monētis</i> e, adiante, <i lang="la">regitis</i>. Identifique pessoa, número, conjugação e entrada de dicionário de cada uma, e traduza.', [
            ('Qual é a terminação pessoal de cada forma?', 'As duas terminam em <i>-tis</i>: 2ª pessoa do plural, "vós" (ou "vocês"). A terminação é a mesma; o que distingue os verbos é o que vem antes.'),
            ('Que vogal precede a terminação?', 'Em <i>monē-tis</i>, um <i>ē</i> longo: é a vogal da 2ª conjugação, a mesma de <i>monēre</i>. Em <i>regi-tis</i>, um <i>i</i> breve: é a vogal de ligação da 3ª conjugação diante de <i>-tis</i>.'),
            ('Qual é a entrada de dicionário?', '<i>moneō, -ēre</i> (2ª), "advertir"; <i>regō, -ere</i> (3ª), "reger, governar".'),
            ('Como se pronunciam?', 'mo<u>nē</u>tis, com acento na penúltima longa; <u>re</u>gitis, com acento na antepenúltima, porque a penúltima é breve.'),
            ('Traduza.', '<i>Monētis</i>: "advertis", "vocês advertem". <i>Regitis</i>: "regeis, governais", "vocês governam".'),
        ]),
        pratica_guiada('Prática guiada 2 · Esse em dois sentidos',
            'Analise e traduza: <i lang="la">In silvā sunt lupī magnī; agricolae nōn sunt laetī.</i> Vocabulário: <i>lupus, -ī</i>, lobo; <i>magnus, -a, -um</i>, grande; <i>laetus, -a, -um</i>, alegre, contente.', [
            ('Quais são os verbos, e o que as terminações pedem?', 'Há dois <i>sunt</i>, 3ª pessoa do plural de <i>esse</i>. Cada um pede um sujeito no nominativo plural.'),
            ('Qual é o sujeito do primeiro <i>sunt</i>? Ele tem predicativo?', 'O sujeito é <i>lupī</i> (nominativo plural, 2ª declinação), com o adjetivo <i>magnī</i> concordando. <i>In silvā</i> é lugar onde (<i>in</i> + ablativo). Não há predicativo: <i>sunt</i> está no sentido de "existir", "há".'),
            ('E na segunda oração?', 'Sujeito <i>agricolae</i> (nominativo plural, masculino, da 1ª declinação); <i>laetī</i> é predicativo: nominativo plural <b>masculino</b>, porque <i>agricola</i> é masculino, embora termine em <i>-a</i>. <i>Nōn</i> vem antes do verbo e nega a oração.'),
            ('Monte a tradução.', '"Na floresta há lobos grandes; os agricultores não estão contentes."'),
        ], 'Conclusão: o mesmo <i>sunt</i> é "há" quando não tem predicativo e é "são, estão" quando liga o sujeito a um predicativo no nominativo.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Reconheça a forma', 'Dê a pessoa, o número, a entrada de dicionário (com a conjugação) e a tradução. Os verbos estão no vocabulário da seção 4.', [
            ('<i>amātis</i>', '2ª pessoa do plural; <i>amō, -āre</i> (1ª): "amais, vocês amam". Terminação <i>-tis</i> depois do <i>ā</i> da 1ª.'),
            ('<i>monent</i>', '3ª pessoa do plural; <i>moneō, -ēre</i> (2ª): "advertem". O <i>e</i> antes de <i>-nt</i> é do tema da 2ª.'),
            ('<i>regimus</i>', '1ª pessoa do plural; <i>regō, -ere</i> (3ª): "regemos, governamos". O <i>i</i> breve antes de <i>-mus</i> é o da 3ª.'),
            ('<i>audiunt</i>', '3ª pessoa do plural; <i>audiō, -īre</i> (4ª): "ouvem". Sozinha, a forma em <i>-iunt</i> poderia ser também da 3ª em <i>-iō</i> (<i>capiunt</i>); é o dicionário que diz que <i>audiō</i> é da 4ª.'),
            ('<i>capit</i>', '3ª pessoa do singular; <i>capiō, -ere</i> (3ª em <i>-iō</i>): "pega, toma". Diante de <i>-t</i>, segue <i>regit</i>.'),
            ('<i>sumus</i>', '1ª pessoa do plural de <i>sum, esse</i> (irregular): "somos, estamos".'),
            ('<i>vidēs</i>', '2ª pessoa do singular; <i>videō, -ēre</i> (2ª): "vês, você vê". O <i>ē</i> longo é a marca da 2ª.'),
            ('<i>dūcis</i>', '2ª pessoa do singular; <i>dūcō, -ere</i> (3ª): "conduzes, você conduz". O <i>i</i> breve antes de <i>-s</i> é o da 3ª (compare <i>vidēs</i>).'),
            ('<i>venīmus</i>', '1ª pessoa do plural; <i>veniō, -īre</i> (4ª): "vimos" (presente de "vir": nós vimos agora). O <i>ī</i> longo é o da 4ª.'),
            ('<i>estis</i>', '2ª pessoa do plural de <i>esse</i>: "sois, vocês são (estão)".'),
        ]),
        exercicio('Exercício 2 · Conjugação e acento', 'Diga a conjugação de cada verbo pela entrada de dicionário e indique a sílaba tônica do infinitivo, explicando por quê.', [
            ('<i>habeō, habēre</i> (ter)', '2ª conjugação (<i>-ēre</i> longo). Acento: ha<u>bē</u>re, porque a penúltima tem vogal longa.'),
            ('<i>legō, legere</i> (ler)', '3ª conjugação (<i>-ere</i> breve). Acento: <u>le</u>gere, porque a penúltima é breve e o acento recua para a antepenúltima.'),
            ('<i>veniō, venīre</i> (vir)', '4ª conjugação (<i>-īre</i>). Acento: ve<u>nī</u>re, penúltima longa.'),
            ('<i>laudō, laudāre</i> (louvar)', '1ª conjugação (<i>-āre</i>). Acento: lau<u>dā</u>re, penúltima longa.'),
            ('<i>faciō, facere</i> (fazer)', '3ª conjugação em <i>-iō</i>: primeira pessoa como <i>audiō</i>, infinitivo breve como <i>regere</i>. Acento: <u>fa</u>cere.'),
            ('<i>creō, creāre</i> (criar)', '1ª conjugação, apesar do <i>-eō</i>: o infinitivo é <i>-āre</i>. Acento: cre<u>ā</u>re, porque a penúltima, <i>ā</i>, é longa.'),
            ('<i>scrībō, scrībere</i> (escrever)', '3ª conjugação. Acento: <u>scrī</u>bere; a penúltima, <i>be</i>, é breve, e o acento cai na antepenúltima (que, no caso, também tem vogal longa).'),
            ('<i>timeō, timēre</i> (temer)', '2ª conjugação. Acento: ti<u>mē</u>re.'),
        ]),
        exercicio('Exercício 3 · Conjugue e transforme', 'Conjugue no presente os três primeiros verbos. Depois passe as frases para o número indicado, e a última para a forma negativa. Vocabulário: <i>puer, puerī</i> (m.), menino; <i>liber, librī</i> (m.), livro; <i>equus, -ī</i> (m.), cavalo.', [
            ('<i>labōrō, -āre</i>', '<i>labōrō, labōrās, labōrat, labōrāmus, labōrātis, labōrant</i>: como <i>amō</i>, com <i>a</i> breve antes de <i>-t</i> e <i>-nt</i>.'),
            ('<i>dūcō, -ere</i>', '<i>dūcō, dūcis, dūcit, dūcimus, dūcitis, dūcunt</i>: como <i>regō</i> (<i>i</i> breve; <i>u</i> antes de <i>-nt</i>).'),
            ('<i>veniō, -īre</i>', '<i>veniō, venīs, venit, venīmus, venītis, veniunt</i>: como <i>audiō</i>.'),
            ('Para o plural: <i>Puer librum legit.</i>', '<i>Puerī librōs legunt.</i> O sujeito e o objeto vão para o plural, e o verbo da 3ª passa de <i>-it</i> a <i>-unt</i>. "Os meninos leem os livros."'),
            ('Para o plural: <i>Nauta in īnsulā est.</i>', '<i>Nautae in īnsulā sunt.</i> "Os marinheiros estão na ilha." <i>In īnsulā</i> não muda: é o lugar, não o sujeito.'),
            ('Para o singular: <i>Servī in agrō labōrant.</i>', '<i>Servus in agrō labōrat.</i> "O escravo trabalha no campo."'),
            ('Para o plural: <i>Puella rosam capit.</i>', '<i>Puellae rosās capiunt.</i> Como <i>capiō</i> é da 3ª em <i>-iō</i>, a 3ª do plural é <i>capiunt</i>, com <i>i</i>, e não "capunt".'),
            ('Para a forma negativa: <i>Agricola equōs dūcit.</i>', '<i>Agricola equōs nōn dūcit.</i> <i>Nōn</i> entra logo antes do verbo, que nega a frase inteira. "O agricultor não conduz os cavalos."'),
        ]),
        exercicio('Exercício 4 · O verbo esse', 'Complete com a forma de <i>esse</i> pedida pela tradução e explique a escolha. No último item, escolha também a forma do adjetivo. Vocabulário: <i>et</i>, e; <i>bonus, -a, -um</i>, bom.', [
            ('<i>Rēgīna et fīlia in vīllā ___.</i> (A rainha e a filha estão na casa.)', '<i>sunt</i>: dois sujeitos ligados por <i>et</i> pedem verbo no plural.'),
            ('<i>Nautae ___.</i> (Somos marinheiros.)', '<i>sumus</i>: o sujeito "nós" está só na terminação; <i>nautae</i> é predicativo no nominativo plural.'),
            ('<i>Amīcus bonus ___.</i> (Você é um bom amigo.)', '<i>es</i>: 2ª pessoa do singular; <i>amīcus bonus</i> no nominativo, como predicativo.'),
            ('<i>In hortō multae rosae ___.</i> (No jardim há muitas rosas.)', '<i>sunt</i>: sentido de "há"; o que existe, <i>rosae</i>, é o sujeito plural.'),
            ('<i>Laeta ___.</i> (Estou contente, diz uma menina.)', '<i>sum</i>: 1ª pessoa do singular; <i>laeta</i> é feminino porque quem fala é uma menina.'),
            ('<i>Magistrae ___.</i> (Vocês são professoras.)', '<i>estis</i>: 2ª pessoa do plural, com o predicativo <i>magistrae</i> no nominativo plural.'),
            ('<i>Puerī ___ (bonus).</i> (Os meninos são bons.)', '<i>Puerī sunt bonī</i> (ou <i>bonī sunt</i>): verbo no plural, e o predicativo no nominativo plural masculino, concordando com <i>puerī</i>. "Bonōs" seria acusativo, e com <i>esse</i> não há objeto.'),
        ]),
        exercicio('Exercício 5 · Leia o texto', 'Leia em voz alta, depois traduza frase a frase, dizendo de cada verbo a pessoa, o número e a conjugação. Vocabulário: <i>ager, agrī</i> (m.), campo; <i>sed</i>, mas; <i>itaque</i>, por isso; <i>in</i> + acusativo, para dentro de.', [
            ('<i>Agricola in vīllā habitat; fīlia agricolae in hortō ambulat et rosās spectat.</i>', '<i>habitat, ambulat, spectat</i>: 3ª do singular, 1ª conjugação. "O agricultor mora na casa; a filha do agricultor passeia no jardim e olha as rosas." <i>Agricolae</i> é genitivo: os verbos estão no singular.'),
            ('<i>Servī in agrō sunt et equōs dūcunt.</i>', '<i>sunt</i>: 3ª do plural de <i>esse</i>, com lugar ("estão"); <i>dūcunt</i>: 3ª do plural, 3ª conjugação. "Os escravos estão no campo e conduzem os cavalos."'),
            ('<i>Puer epistulam scrībit, sed fābulās nōn legit.</i>', '<i>scrībit, legit</i>: 3ª do singular, 3ª conjugação; <i>nōn</i> nega <i>legit</i>. "O menino escreve uma carta, mas não lê histórias."'),
            ('<i>In silvā sunt lupī; itaque puerī in silvam nōn veniunt.</i>', '<i>sunt</i>: "há"; <i>veniunt</i>: 3ª do plural, 4ª conjugação. <i>In silvam</i>, com acusativo, indica movimento. "Na floresta há lobos; por isso os meninos não vão (não vêm) para dentro da floresta."'),
            ('<i>Agricola puerōs monet; puerī magistrum audiunt et timent.</i>', '<i>monet</i>: 3ª do singular, 2ª conjugação; <i>audiunt</i>: 3ª do plural, 4ª; <i>timent</i>: 3ª do plural, 2ª. "O agricultor adverte os meninos; os meninos ouvem o mestre e (o) temem."'),
        ]),
        exercicio('Exercício 6 · Retroversão', 'Passe para o latim, sem pronomes sujeito, usando o vocabulário do capítulo. Vocabulário extra: <i>caelum, -ī</i> (n.), céu; <i>magister, magistrī</i> (m.), mestre; <i>ad</i> + acusativo, para.', [
            ('Os meninos não ouvem a professora.', '<i>Puerī magistram nōn audiunt.</i> Sujeito no nominativo plural, objeto no acusativo, <i>nōn</i> antes do verbo da 4ª, que faz a 3ª do plural em <i>-iunt</i>.'),
            ('Somos agricultores e trabalhamos no campo.', '<i>Agricolae sumus et in agrō labōrāmus.</i> O predicativo <i>agricolae</i> fica no nominativo; os dois verbos na 1ª do plural.'),
            ('Há muitas estrelas no céu.', '<i>In caelō sunt multae stellae</i> (ou <i>Sunt multae stellae in caelō</i>). "Há" = <i>sunt</i>, no plural, porque o que existe é plural.'),
            ('Você lê a carta, mas não escreve.', '<i>Epistulam legis, sed nōn scrībis.</i> 2ª do singular da 3ª conjugação: <i>-is</i>, com <i>i</i> breve.'),
            ('O senhor conduz os escravos para a casa.', '<i>Dominus servōs ad vīllam dūcit</i> (ou <i>in vīllam</i>, "para dentro da casa"). Lugar para onde: acusativo com preposição.'),
            ('As meninas pegam as rosas.', '<i>Puellae rosās capiunt.</i> <i>Capiō</i> é da 3ª em <i>-iō</i>: a 3ª do plural é <i>capiunt</i>, como <i>audiunt</i>.'),
        ]),
    ],
    leituras=['ravizza-gramatica-latina', 'bennett-new-latin-grammar', 'greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', 'orberg-lingua-latina-per-se-illustrata-pars-i-familia-romana', 'sonnenschein-ora-maritima-a-latin-story-for-beginners', 'vulgata-biblia-sacra-vulgata-editio-clementina'],
    leituras_nota='Para consulta, Ravizza traz as desinências do presente das quatro conjugações em português (n. 85) e <i>esse</i> completo (n. 82); em Bennett, <i>sum</i> está no § 100 e os quatro modelos nos §§ 101, 103, 105 e 107, e em Allen &amp; Greenough as conjugações começam no § 171. Para leitura, os primeiros capítulos de <i>Familia Romana</i> e de <i>Ora Maritima</i> usam o presente o tempo todo: leia-os procurando a terminação de cada verbo antes do sujeito. Na Vulgata, o Salmo 22 (23) e o capítulo 4 da Primeira Carta de João têm muitas frases curtas no presente.',
)
