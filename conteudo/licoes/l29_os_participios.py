from conteudo.util import (tabela, tabela_declinacao, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

LICAO = dict(
    slug='29-os-participios', titulo='Os particípios', titulo_latim='Dē participiīs', tempo='70 min',
    resumo='Os três particípios do latim (presente ativo, perfeito passivo e futuro ativo): como se formam, como se declinam, que tempo exprimem em relação ao verbo principal, como funcionam na frase (atributo, substantivo, particípio conjunto) e como se traduzem para o português sem perder a relação lógica que o latim deixa implícita.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['particípio presente', 'particípio perfeito passivo', 'particípio futuro ativo', 'declinação de amāns', 'ablativo em -e e em -ī', 'particípios dos depoentes', 'tempo relativo', 'particípio atributivo', 'particípio substantivado', 'particípio conjunto', 'particípio predicativo com videō e audiō', 'tradução do particípio', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulos 10, 13, 24 e 25: os adjetivos de segunda classe (o particípio presente declina-se como eles), as partes principais do verbo, a passiva do perfectum (onde o particípio perfeito já apareceu dentro de <i>amātus est</i>) e os verbos depoentes. Ajuda ter feito o capítulo 27, sobre os infinitivos, porque o tempo do particípio funciona como o tempo do infinitivo: relativo ao verbo principal.',
                       licoes=['10-a-terceira-declinacao-temas-em-i', '13-o-perfeito-e-as-partes-principais', '24-a-passiva-do-perfectum', '25-verbos-depoentes', '27-os-infinitivos']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 70 (paradigma de prūdēns), § 70.3 (particípios em -āns, -ēns: ablativo em -e quando particípio ou substantivo, em -ī quando adjetivo), §§ 101, 103, 105, 107, 110 (particípios de amō, moneō, regō, audiō, capiō), § 112 (formas e sentidos dos depoentes), § 119.1–4 (formação do particípio perfeito e do futuro ativo), § 132 (iēns, euntis), § 336 (tempo relativo; 336.5 particípios de depoentes com valor de presente), § 337.1–5 (usos atributivo e predicativo; videō e audiō + particípio; particípio perfeito equivalente a oração coordenada), § 356.2 (como se supre a falta de particípio perfeito ativo)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 117.b (particípios em -ns declinados como egēns), § 121.a (ablativo em -e ou -ī), § 158 (os particípios e seus sentidos), § 190.a–b (particípios dos depoentes), §§ 488–493 (natureza e tempo do particípio; não há particípio presente passivo nem perfeito ativo), §§ 494–497 (usos atributivo, predicativo e circunstancial), §§ 498–499 (particípio futuro)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 72, nota 2 (ablativo em -ī ou -e nos particípios presentes), § 107 (o verbo infinito: os três particípios e os três que faltam), §§ 389–393 (usos do particípio; falta do perfeito ativo)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 53, d (adjetivos e particípios em -ns; paradigma de amans e observação sobre o ablativo em -e/-i), nn. 388–397 (o particípio: espécies, usos, falta do perfeito ativo), nn. 399–400 (como verter em latim o gerúndio e o particípio português)', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Mt 2,10–11; 9,9; Lc 2,16.20', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Matthaeum', nota='frases autênticas das seções 6 e do exercício 6, conferidas na Wikisource latina; ortografia adaptada (i por j, ae por æ) e macrons acrescentados', tipo='dominio_publico'),
        referencia('Suetônio, De vita Caesarum, Cláudio 21.6', 'Suetônio', url='https://www.thelatinlibrary.com/suetonius/suet.claudius.html', nota='"Have imperator, morituri te salutant!", conferido no texto da Latin Library e na edição de Ihm (Teubner, 1907, domínio público; texto Perseus), que traz a frase em 21.6 e grafa "haue imperator" sem vírgula; macrons acrescentados', tipo='dominio_publico'),
    ],
    objetivos=[
        'Formar e reconhecer os três particípios de qualquer verbo a partir das partes principais (<i>amāns</i>, <i>amātus</i>, <i>amātūrus</i>), inclusive nos depoentes.',
        'Declinar o particípio presente e escolher entre o ablativo em <i>-e</i> e em <i>-ī</i>.',
        'Explicar que o tempo do particípio é relativo ao verbo principal (simultâneo, anterior, posterior) e traduzi-lo de acordo.',
        'Distinguir os usos atributivo, substantivado e predicativo (particípio conjunto) e achar o nome com que o particípio concorda.',
        'Traduzir um particípio conjunto para o português de várias maneiras (gerúndio, oração relativa, temporal, causal, concessiva, coordenada) e justificar a escolha pelo contexto.',
    ],
    secoes=[
        ('O que é um particípio', f'''
<p>O particípio é um <b>adjetivo verbal</b>. O nome vem do latim <i>participium</i>, "o que tem parte": os gramáticos antigos o chamavam assim porque ele participa ao mesmo tempo da natureza do nome e da do verbo. Como adjetivo, ele concorda em gênero, número e caso com um substantivo e se declina como os adjetivos que você já conhece. Como verbo, ele tem voz (ativa ou passiva), exprime um tempo e pode ter os mesmos complementos que o verbo teria: um objeto direto, um dativo, um adjunto adverbial. Em <i>puer lupum timēns</i>, "o menino que teme o lobo", <i>timēns</i> concorda com <i>puer</i> (nominativo singular masculino), como um adjetivo, e tem o seu objeto <i>lupum</i>, como um verbo.</p>
<p>O latim tem <b>três particípios</b> propriamente ditos, e cada um combina uma voz com um tempo. Há ainda uma quarta forma participial, o <b>gerundivo</b> em <i>-ndus</i> (<i>amandus</i>, "que deve ser amado"), que tem usos próprios e fica para o capítulo 31.</p>
{tabela(['Particípio', 'Voz', 'Tempo (relativo)', 'Exemplo', 'Sentido básico'], [
    ['<b>presente</b>', 'ativa', 'simultâneo ao verbo principal', '<i>amāns, amantis</i>', '"que ama", "amando"'],
    ['<b>perfeito</b>', 'passiva', 'anterior ao verbo principal', '<i>amātus, -a, -um</i>', '"amado", "tendo sido amado"'],
    ['<b>futuro</b>', 'ativa', 'posterior ao verbo principal', '<i>amātūrus, -a, -um</i>', '"que vai amar", "prestes a amar"'],
], 'Os três particípios do latim')}
<p>Repare no que <b>falta</b>. Não há particípio presente passivo ("sendo amado") nem particípio perfeito ativo ("tendo amado"). Isso tem consequências práticas: <i>amātus</i> nunca quer dizer "tendo amado", e quando o latim precisa dizer "tendo tomado a cidade" recorre a outras construções, sobretudo ao ablativo absoluto (capítulo 30) e às orações com <i>cum</i> (capítulo 34). A grande exceção são os verbos depoentes, que você estudou no capítulo 25: como a sua forma passiva tem sentido ativo, o particípio perfeito deles significa "tendo feito" (<i>hortātus</i>, "tendo exortado"). É o único particípio perfeito ativo da língua.</p>
{dica('<b>O português herdou os três.</b> O particípio presente latino sobrevive em adjetivos e nomes como <i>amante</i>, <i>estudante</i>, <i>ouvinte</i>, <i>presidente</i> (de <i>amāns, studēns, audiēns, praesidēns</i>); o perfeito, no nosso particípio passado (<i>amado</i>, de <i>amātus</i>); e o futuro em <i>-ūrus</i>, em palavras como <i>futuro</i> (de <i>futūrus</i>) e <i>nascituro</i> (de <i>nāscitūrus</i>, "que vai nascer"). Quando você encontrar um particípio latino, vale procurar o parente português: ele costuma dar a pista do sentido.')}
'''),
        ('Formação e declinação', f'''
<h3>O particípio presente: tema do presente + -ns</h3>
<p>Forma-se do tema do presente, o mesmo do imperfeito do indicativo: <i>amā-ns</i>, <i>monē-ns</i>, <i>reg-ēns</i>, <i>audi-ēns</i>, <i>capi-ēns</i>. Na 3ª e na 4ª conjugações aparece <i>-ēns</i> (com <i>-iēns</i> nos verbos em <i>-iō</i> e na 4ª), exatamente como no imperfeito <i>regēbam</i>, <i>audiēbam</i>, <i>capiēbam</i>. O genitivo, que mostra o tema, termina em <i>-ntis</i>: <i>amantis</i>, <i>monentis</i>, <i>regentis</i>, <i>audientis</i>, <i>capientis</i>. A vogal é longa antes de <i>-ns</i> e breve antes de <i>-nt-</i> (<i>amāns</i>, mas <i>amantis</i>); é uma regra geral da pronúncia latina, não uma irregularidade. O verbo <i>eō</i> (capítulo 26) faz <i>iēns, euntis</i>, e <i>sum</i> não tem particípio presente no latim clássico.</p>
<p>Declina-se como um adjetivo de segunda classe de uma só terminação (capítulo 10), igual a <i>prūdēns, prūdentis</i>: uma forma para o masculino e o feminino, outra para o neutro só no nominativo, vocativo e acusativo.</p>
{tabela_declinacao('Particípio presente: amāns, amantis, "que ama, amando"', [
    ('amā<b>ns</b>', 'amā<b>ns</b>', 'ama<b>ntēs</b>', 'ama<b>ntia</b>'),
    ('ama<b>ntis</b>', 'ama<b>ntis</b>', 'ama<b>ntium</b>', 'ama<b>ntium</b>'),
    ('ama<b>ntī</b>', 'ama<b>ntī</b>', 'ama<b>ntibus</b>', 'ama<b>ntibus</b>'),
    ('ama<b>ntem</b>', 'amā<b>ns</b>', 'ama<b>ntēs</b> (-<b>īs</b>)', 'ama<b>ntia</b>'),
    ('amā<b>ns</b>', 'amā<b>ns</b>', 'ama<b>ntēs</b>', 'ama<b>ntia</b>'),
    ('ama<b>nte</b> / ama<b>ntī</b>', 'ama<b>nte</b> / ama<b>ntī</b>', 'ama<b>ntibus</b>', 'ama<b>ntibus</b>'),
], colunas=('Masc. e fem. sing.', 'Neutro sing.', 'Masc. e fem. pl.', 'Neutro pl.'))}
{observacao('Ablativo em -e ou em -ī?', 'Os adjetivos de segunda classe fazem o ablativo singular em <i>-ī</i> (<i>prūdentī</i>). O particípio presente hesita, e a regra das gramáticas é funcional: quando ele funciona como <b>particípio</b> (com valor verbal, e sempre no ablativo absoluto do capítulo 30) ou como <b>substantivo</b>, o ablativo é em <i>-e</i>; quando é usado como simples <b>adjetivo</b>, em <i>-ī</i>. Assim, <i>ab amante</i>, "por um amante" (substantivo), mas <i>ab amantī fēminā</i>, "por uma mulher amorosa" (adjetivo); <i>Tarquiniō rēgnante</i>, "reinando Tarquínio" (particípio). Para o leitor, basta saber que as duas formas são o mesmo caso. No genitivo plural, a forma regular é <i>-ium</i> (<i>amantium</i>); <i>-um</i> (<i>venientum</i>, <i>silentum</i>) aparece sobretudo na poesia (Bennett § 70.7; Allen e Greenough § 121.b). O Pe. Ravizza (n. 53, obs. 2) ensina outra regra: <i>-um</i> quando o particípio é substantivo (<i>sapientum</i>), <i>-ium</i> quando é particípio ou adjetivo (<i>audientium</i>). Este livro segue Bennett e Allen e Greenough e usa <i>-ium</i>; nos textos você encontrará as duas formas.')}
<h3>O particípio perfeito: a quarta parte principal</h3>
<p>Você já o conhece: é a quarta parte principal do verbo (capítulo 13) e a peça variável da passiva do perfectum (<i>amātus est</i>, capítulo 24). Termina em <i>-tus</i> ou <i>-sus</i> e declina-se como <i>bonus, -a, -um</i>: <i>amātus</i>, <i>monitus</i>, <i>rēctus</i>, <i>audītus</i>, <i>captus</i>, <i>missus</i>, <i>vīsus</i>. Por ser passivo, só os verbos transitivos o têm com sentido pessoal: há <i>urbs capta</i>, "a cidade tomada", mas não há "o homem vindo" a partir de <i>veniō</i>, que é intransitivo (a forma <i>ventum</i> existe só na passiva impessoal, <i>ventum est</i>, "chegou-se").</p>
<h3>O particípio futuro: tema do particípio perfeito + -ūrus</h3>
<p>Tire <i>-us</i> do particípio perfeito e acrescente <i>-ūrus, -ūra, -ūrum</i>: <i>amāt-ūrus</i>, <i>monit-ūrus</i>, <i>rēct-ūrus</i>, <i>audīt-ūrus</i>, <i>capt-ūrus</i>. Também se declina como <i>bonus</i>. Alguns verbos o formam de outro modo, e o dicionário os registra: <i>sum</i> faz <i>futūrus</i>; <i>morior</i>, <i>moritūrus</i>; <i>eō</i>, <i>itūrus</i>; e os intransitivos, que não têm particípio perfeito pessoal, têm futuro normalmente (<i>veniō</i> → <i>ventūrus</i>). Se você já estudou o infinitivo futuro ativo no capítulo 27 (<i>amātūrus esse</i>), reconhecerá a forma.</p>
{tabela(['Verbo (partes principais)', 'Particípio presente', 'Particípio perfeito', 'Particípio futuro'], [
    ['<i>amō, amāre, amāvī, amātum</i>', '<i>amāns, amantis</i>', '<i>amātus, -a, -um</i>', '<i>amātūrus, -a, -um</i>'],
    ['<i>moneō, monēre, monuī, monitum</i>', '<i>monēns, monentis</i>', '<i>monitus</i>', '<i>monitūrus</i>'],
    ['<i>regō, regere, rēxī, rēctum</i>', '<i>regēns, regentis</i>', '<i>rēctus</i>', '<i>rēctūrus</i>'],
    ['<i>audiō, audīre, audīvī, audītum</i>', '<i>audiēns, audientis</i>', '<i>audītus</i>', '<i>audītūrus</i>'],
    ['<i>capiō, capere, cēpī, captum</i>', '<i>capiēns, capientis</i>', '<i>captus</i>', '<i>captūrus</i>'],
    ['<i>sum, esse, fuī</i>', '(não há)', '(não há)', '<i>futūrus</i>'],
    ['<i>eō, īre, iī, itum</i>', '<i>iēns, euntis</i>', '(só impessoal)', '<i>itūrus</i>'],
], 'Os particípios dos verbos-modelo', latim_cols=(1, 2, 3))}
<h3>Os particípios dos depoentes</h3>
<p>Os depoentes têm os três particípios, e todos com sentido <b>ativo</b>: o presente e o futuro têm forma ativa (<i>sequēns</i>, "seguindo"; <i>secūtūrus</i>, "que vai seguir"), e o perfeito, de forma passiva, tem o sentido ativo do verbo (<i>secūtus</i>, "tendo seguido"). É por isso que <i>hortātus</i>, <i>locūtus</i>, <i>profectus</i>, <i>cōnspicātus</i> se traduzem por "tendo exortado", "tendo falado", "tendo partido", "tendo avistado". Alguns perfeitos de depoentes e semidepoentes, como <i>ratus</i> ("pensando"), <i>veritus</i> ("temendo"), <i>ūsus</i> ("usando") e <i>gāvīsus</i> ("alegrando-se"), costumam equivaler a um presente.</p>
{tabela(['Depoente', 'Presente', 'Perfeito (ativo!)', 'Futuro'], [
    ['<i>hortor, hortārī, hortātus sum</i>, exortar', '<i>hortāns</i>, exortando', '<i>hortātus</i>, tendo exortado', '<i>hortātūrus</i>, que vai exortar'],
    ['<i>sequor, sequī, secūtus sum</i>, seguir', '<i>sequēns</i>, seguindo', '<i>secūtus</i>, tendo seguido', '<i>secūtūrus</i>, que vai seguir'],
    ['<i>loquor, loquī, locūtus sum</i>, falar', '<i>loquēns</i>, falando', '<i>locūtus</i>, tendo falado', '<i>locūtūrus</i>, que vai falar'],
    ['<i>morior, morī, mortuus sum</i>, morrer', '<i>moriēns</i>, morrendo', '<i>mortuus</i>, tendo morrido, morto', '<i>moritūrus</i>, que vai morrer'],
], 'Os particípios dos depoentes', latim_cols=())}
'''),
        ('O tempo do particípio é relativo', f'''
<p>O particípio não diz se uma ação é passada, presente ou futura em relação ao momento em que se fala. Diz só se ela é <b>simultânea</b>, <b>anterior</b> ou <b>posterior</b> à ação do verbo principal da oração. O tempo absoluto vem do verbo principal. É o mesmo princípio que governa o tempo dos infinitivos (capítulo 27), e entender isso evita boa parte dos erros de tradução.</p>
{comparacao('O particípio presente acompanha o tempo do verbo principal', ['Latim', 'Relação', 'Tradução'], [
    ['Puerum <b>currentem</b> videō.', 'simultâneo a um presente', 'Vejo o menino correndo (que corre).'],
    ['Puerum <b>currentem</b> vīdī.', 'simultâneo a um passado', 'Vi o menino correndo (que corria).'],
    ['Puerum <b>currentem</b> vidēbō.', 'simultâneo a um futuro', 'Verei o menino correndo (que estará correndo).'],
])}
<p>Nas três frases <i>currentem</i> é o mesmo particípio presente, e a tradução muda conforme o verbo principal: "que corre", "que corria", "que estará correndo". Com o particípio perfeito, a ação está sempre concluída antes; com o futuro, ainda está por vir:</p>
{exemplos([
    ('Epistulam <b>scrīptam</b> legō.', 'Leio a carta escrita (que foi escrita antes de eu ler).'),
    ('Epistulam <b>scrīptam</b> lēgī.', 'Li a carta que tinha sido escrita.'),
    ('Mīles <b>pugnātūrus</b> arma capit.', 'O soldado, prestes a combater, pega as armas. (<i>pugnō</i>, combater; <i>arma</i>, armas)'),
    ('Mīlitēs <b>pugnātūrī</b> arma cēpērunt.', 'Os soldados, que iam combater, pegaram as armas.'),
])}
{observacao('Por que "particípio presente" engana', 'O nome "presente" é tradicional, mas a ideia é de <b>ação em curso</b> ao mesmo tempo que outra. Por isso o português o traduz tão bem pelo gerúndio, que também não tem tempo próprio: "Vi o menino <i>correndo</i>", "Vejo o menino <i>correndo</i>". Quando o gerúndio português ficar ambíguo, troque-o por uma oração com o tempo certo: "que corria", "enquanto corria".')}
'''),
        ('Como o particípio funciona na frase', f'''
<p>Por ser adjetivo, o particípio pode ocupar na frase os lugares de um adjetivo. As gramáticas distinguem três usos, e reconhecer qual deles está em jogo é metade da tradução.</p>
<h3>1. Atributivo: uma qualidade estável</h3>
<p>O particípio qualifica o nome como um adjetivo comum e costuma se traduzir por um adjetivo ou por uma oração relativa curta. Muitos particípios se tornaram adjetivos plenos, com comparativo e superlativo (<i>doctus</i>, "instruído"; <i>doctior</i>, <i>doctissimus</i>).</p>
{exemplos([('aqua <b>fluēns</b>', 'água corrente'), ('urbs <b>capta</b>', 'a cidade tomada (conquistada)'), ('vir <b>doctus</b>', 'um homem instruído'), ('fīlius <b>amātus</b>', 'o filho amado')])}
<h3>2. Substantivado: o particípio vira nome</h3>
<p>Sem substantivo explícito, o particípio passa a designar quem pratica a ação (masculino e feminino) ou a coisa feita (neutro). O português faz o mesmo com "os amantes", "os estudantes", "o dito", "o feito".</p>
{exemplos([('<b>amantēs</b>', 'os amantes, os que amam'), ('<b>discentēs</b>', 'os que aprendem, os alunos (<i>discō</i>, aprender)'), ('<b>moritūrī</b>', 'os que vão morrer'), ('<b>dictum</b>, <b>facta</b>', 'o dito (a frase), os feitos (os atos)')])}
<h3>3. Predicativo ou circunstancial: o particípio conjunto</h3>
<p>É o uso mais frequente nos textos e o mais importante deste capítulo. O particípio concorda com um termo da oração (o sujeito, o objeto, um dativo) mas não diz uma qualidade permanente dele: diz em que <b>circunstância</b> ele está enquanto a ação principal acontece. Chama-se <b>particípio conjunto</b> (<i>participium coniūnctum</i>) justamente porque está "conjunto", ligado gramaticalmente, a um termo da oração; o capítulo 30 vai contrastá-lo com o ablativo absoluto, que não está ligado a nenhum.</p>
{exemplos([
    ('Puer lupum <b>timēns</b> fūgit.', 'O menino, temendo o lobo, fugiu. = porque temia o lobo (<i>fugiō, fūgī</i>, fugir)'),
    ('Mīles <b>vulnerātus</b> pugnam nōn relīquit.', 'O soldado, ferido, não abandonou o combate. = embora estivesse ferido (<i>vulnerō</i>, ferir; <i>relinquō, relīquī</i>, abandonar)'),
    ('Hostēs urbem <b>captam</b> incendērunt.', 'Os inimigos tomaram a cidade e a incendiaram. (lit. "incendiaram a cidade tomada"; <i>incendō, incendī</i>, incendiar)'),
    ('Dux mīlitēs <b>hortātus</b> castra mōvit.', 'O comandante, tendo exortado os soldados, moveu o acampamento. (<i>hortor</i>, depoente; <i>castra</i>, acampamento)'),
])}
<p>O particípio conjunto sempre concorda com o seu termo, e é essa concordância que diz a quem ele se refere. Em <i>Mīlitēs ducem fugientem vīdērunt</i>, <i>fugientem</i> é acusativo singular e só pode ir com <i>ducem</i>: "os soldados viram o comandante <b>que fugia</b>"; se fosse <i>fugientēs</i>, iria com <i>mīlitēs</i> (nominativo plural): "os soldados, <b>fugindo</b>, viram o comandante". Uma terminação muda quem foge.</p>
<p>Um caso particular: com verbos de percepção, sobretudo <i>videō</i> e <i>audiō</i>, o particípio presente concordando com o objeto mostra a ação no momento em que é percebida, de modo mais vivo que a oração infinitiva do capítulo 28: <i>Videō tē currentem</i>, "vejo você correndo"; <i>Audīvī puellam cantantem</i>, "ouvi a menina cantando".</p>
{observacao('O particípio perfeito como oração coordenada', 'Em <i>Hostēs urbem captam incendērunt</i>, o latim junta duas ações sucessivas numa só oração: primeiro tomaram, depois incendiaram. O português prefere dois verbos coordenados: "tomaram a cidade e a incendiaram". Traduzir ao pé da letra ("incendiaram a cidade tomada") não é errado, mas apaga a sucessão das ações, que é o que o autor quis dizer.')}
'''),
        ('Traduzir o particípio para o português', f'''
<p>O latim usa o particípio para dizer, com uma só palavra, o que o português costuma dizer com uma oração inteira. O particípio conjunto deixa a relação lógica <b>implícita</b>: o leitor deve decidir, pelo contexto, se ela é de tempo, de causa, de concessão, de condição ou de simples acompanhamento. Por isso não existe uma tradução única; existe um repertório, e a escolha é sua.</p>
{tabela(['Recurso em português', 'Quando funciona', 'Exemplo com <i>Puer lupum timēns fūgit</i> ou similar'], [
    ['<b>gerúndio</b> ("temendo")', 'quase sempre, para o particípio presente; mantém a ambiguidade do latim', 'O menino, temendo o lobo, fugiu.'],
    ['<b>oração relativa</b> ("que...")', 'uso atributivo e particípio ligado ao objeto', 'Os soldados viram o comandante que fugia.'],
    ['<b>temporal</b> ("quando", "enquanto", "depois que")', 'simultaneidade (presente) ou anterioridade (perfeito)', 'Depois que exortou os soldados, o comandante moveu o acampamento.'],
    ['<b>causal</b> ("porque", "como")', 'o particípio explica o motivo da ação principal', 'Como temia o lobo, o menino fugiu.'],
    ['<b>concessiva</b> ("embora", "apesar de")', 'o particípio contrasta com a ação principal; muitas vezes há <i>tamen</i>', 'Embora ferido, o soldado não abandonou o combate.'],
    ['<b>condicional</b> ("se")', 'com verbo principal no presente ou futuro, em verdades gerais', '<i>Mīles fugiēns nōn vincit.</i> Se foge, o soldado não vence.'],
    ['<b>coordenada</b> ("e")', 'particípio perfeito de ação anterior e sucessiva', 'Tomaram a cidade e a incendiaram.'],
    ['<b>"tendo" + particípio</b>', 'anterioridade; com depoentes ("tendo exortado") ou passiva ("tendo sido ferido")', 'O soldado, tendo sido ferido, voltou.'],
], 'O repertório de traduções do particípio conjunto')}
<p>Três conselhos práticos. Primeiro, traduza o tempo pela relação com o verbo principal (seção 3): com verbo principal no passado, o particípio presente vira imperfeito ("que corria") e o perfeito vira mais-que-perfeito ("que tinha sido escrita"). Segundo, ao usar o particípio perfeito dos verbos <b>não</b> depoentes, mantenha a voz passiva: <i>captus</i> é "tomado, tendo sido tomado", nunca "tendo tomado". Terceiro, procure palavras que indiquem a relação: <i>tamen</i> ("contudo") na oração principal sugere concessão; <i>iam</i> ("já") sugere tempo; o próprio sentido dos verbos costuma bastar.</p>
{dica('<b>Um teste rápido.</b> Ponha o particípio conjunto entre vírgulas e leia a frase sem ele. O que sobra é a oração principal, completa. Depois pergunte: que relação esta circunstância tem com o que sobrou? A resposta decide a conjunção portuguesa.')}
'''),
        ('Análise gramatical: frases autênticas', f'''
<p>A narrativa da visita dos magos, no Evangelho de Mateus, encadeia vários particípios, todos conjuntos ao sujeito (os magos):</p>
{exemplos([('Videntēs autem stellam gāvīsī sunt gaudiō magnō valdē. Et intrantēs domum, invēnērunt puerum cum Maria mātre eius, et prōcidentēs adōrāvērunt eum.', 'Vendo a estrela, alegraram-se com imensa alegria. E, entrando na casa, encontraram o menino com Maria, sua mãe, e, prostrando-se, adoraram-no. (Mt 2,10–11, Vulgata Clementina)')])}
<p>Antes da análise, duas observações. <i>Gāvīsī sunt</i> é o perfeito do semidepoente <i>gaudeō, gaudēre, gāvīsus sum</i>, "alegrar-se" (capítulo 25): forma passiva, sentido ativo. E <i>Maria</i> é deixado sem macron, como os demais nomes hebraicos neste capítulo, porque a quantidade das suas vogais varia nas fontes.</p>
{analise('Mt 2,11 (primeira oração), palavra a palavra', [
    ('Et', 'et (conjunção)', 'invariável', 'liga esta oração à anterior'),
    ('intrantēs', 'intrō, intrāre, intrāvī, intrātum, entrar', 'particípio presente, nominativo plural masculino', 'particípio conjunto ao sujeito (os magos, contido em <i>invēnērunt</i>); simultâneo: "entrando, ao entrar"'),
    ('domum', 'domus, -ūs (f.), casa', 'acusativo singular, 4ª declinação', 'objeto do particípio <i>intrantēs</i> (o particípio conserva a regência do verbo)'),
    ('invēnērunt', 'inveniō, invenīre, invēnī, inventum, encontrar', 'perfeito do indicativo, 3ª pessoa do plural', 'verbo principal: "encontraram"'),
    ('puerum', 'puer, puerī (m.), menino', 'acusativo singular, 2ª declinação', 'objeto direto de <i>invēnērunt</i>'),
    ('cum Maria', 'Maria, -ae (f.), Maria', '<i>cum</i> + ablativo singular, 1ª declinação', 'companhia: "com Maria"'),
    ('mātre', 'māter, mātris (f.), mãe', 'ablativo singular, 3ª declinação', 'aposto de <i>Maria</i>, no mesmo caso'),
    ('eius', 'is, ea, id', 'genitivo singular', 'posse: "dele", isto é, "sua mãe"'),
])}
<p>O ponto central é <i>intrantēs</i>. Ele concorda com o sujeito de <i>invēnērunt</i>, que não está escrito, mas está na desinência <i>-ērunt</i> (eles, os magos): é nominativo plural masculino. Como particípio presente, indica ação simultânea à do verbo principal; como o verbo principal está no perfeito, a entrada e o encontro são do mesmo momento passado: "ao entrar na casa, encontraram". E, sendo verbo, <i>intrantēs</i> tem o seu próprio objeto, <i>domum</i>. A tradução portuguesa pode manter o gerúndio ("entrando na casa") justamente porque a relação aqui é só de tempo.</p>
{diagrama_frase([('Et intrantēs', 'part. presente · nom. pl. m. (os magos)'), ('domum', 'acusativo · objeto do particípio'), ('invēnērunt', 'verbo principal · "encontraram"'), ('puerum', 'acusativo · objeto do verbo')],
    'O particípio conjunto e o seu próprio objeto: <i>Et intrantēs domum, invēnērunt puerum</i> = E, entrando na casa, encontraram o menino.')}
<p>Um particípio futuro substantivado ficou famoso graças a Suetônio, que conta como os combatentes de uma batalha naval encenada saudaram o imperador Cláudio:</p>
{exemplos([('Havē, imperātor, moritūrī tē salūtant!', 'Salve, imperador, os que vão morrer te saúdam! (Suetônio, <i>Cláudio</i> 21.6; a grafia <i>have</i> é a do texto, por <i>avē</i>)')])}
<p><i>Moritūrī</i> é o particípio futuro do depoente <i>morior</i>, no nominativo plural masculino, sem substantivo: é ele o sujeito de <i>salūtant</i>. Literalmente, "os que vão morrer". Fora da conjugação perifrástica e do infinitivo futuro, o particípio futuro é raro na prosa clássica, salvo <i>futūrus</i> e <i>ventūrus</i> (Allen e Greenough § 498); os poetas e os autores posteriores, como o próprio Suetônio, usam-no com mais liberdade (§ 499).</p>
<h3>Resumo</h3>
<ul>
<li><b>Três particípios</b>: presente ativo (<i>amāns, amantis</i>; declina-se como <i>prūdēns</i>), perfeito passivo (<i>amātus, -a, -um</i>), futuro ativo (<i>amātūrus, -a, -um</i>). Não há presente passivo nem perfeito ativo, salvo o perfeito dos depoentes (<i>hortātus</i>, "tendo exortado").</li>
<li><b>Tempo relativo</b>: presente = simultâneo; perfeito = anterior; futuro = posterior, sempre em relação ao verbo principal.</li>
<li><b>Usos</b>: atributivo (<i>urbs capta</i>), substantivado (<i>amantēs</i>), predicativo ou conjunto (<i>puer lupum timēns fūgit</i>).</li>
<li><b>Tradução</b>: gerúndio, relativa, temporal, causal, concessiva, condicional ou coordenada, conforme o contexto.</li>
</ul>
<p>No capítulo 30 você verá o particípio numa construção independente, o ablativo absoluto (<i>urbe captā</i>, "tomada a cidade"); no 31, a quarta forma participial, o gerundivo, e o gerúndio.</p>
'''),
    ],
    erros_comuns=[
        ('Traduzir o particípio perfeito como ativo: <i>urbem captam</i> → *"tendo tomado a cidade".', 'Fora dos depoentes, o particípio perfeito é <b>passivo</b>: <i>captus</i> é "tomado, tendo sido tomado". <i>Hostēs urbem captam incendērunt</i> é "incendiaram a cidade tomada", ou seja, "tomaram a cidade e a incendiaram"; quem toma é o sujeito do verbo principal, não o particípio.'),
        ('Traduzir o particípio perfeito de um depoente como passivo: <i>Caesar hortātus</i> → *"César, exortado".', 'Os depoentes têm sentido ativo também no particípio perfeito: <i>hortātus</i> é "tendo exortado". Antes de traduzir uma forma em <i>-tus</i>, verifique no dicionário se o verbo é depoente (<i>hortor</i>, <i>sequor</i>, <i>loquor</i>, <i>proficīscor</i>).'),
        ('Dar ao particípio presente um tempo presente absoluto: <i>puerum currentem vīdī</i> → *"vi o menino que corre".', 'O tempo do particípio é relativo: o presente indica simultaneidade com o verbo principal. Com <i>vīdī</i> (passado), o menino corria naquele momento: "vi o menino que corria" ou "correndo".'),
        ('Ligar o particípio ao nome mais próximo em vez do nome com que ele concorda.', 'Em <i>Mīlitēs ducem fugientēs vīdērunt</i>, <i>fugientēs</i> está ao lado de <i>ducem</i>, mas é nominativo plural e concorda com <i>mīlitēs</i>: "os soldados, fugindo, viram o comandante". O que decide é a concordância de gênero, número e caso, não a vizinhança.'),
        ('Achar que <i>amante</i> e <i>amantī</i> são casos diferentes, ou "corrigir" um pelo outro.', 'Os dois são ablativos singulares. O particípio com valor verbal ou substantivo prefere <i>-e</i> (<i>ab amante</i>, "por um amante"); usado como adjetivo, <i>-ī</i> (<i>ab amantī mātre</i>, "por uma mãe amorosa"). Ao ler, identifique o caso; ao escrever, use <i>-e</i> quando o particípio tem valor verbal.'),
        ('Procurar um particípio perfeito pessoal de verbos intransitivos: *<i>puer ventus</i>, "o menino vindo".', 'O particípio perfeito é passivo, e verbos intransitivos como <i>veniō</i>, <i>currō</i>, <i>eō</i> não têm passiva pessoal. Para "o menino, tendo chegado", o latim usa uma oração (capítulo 34) ou um depoente de sentido parecido; já o particípio futuro existe normalmente (<i>ventūrus</i>, "que vai vir").'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Um particípio de depoente e um particípio presente',
            'Analise e traduza: <i lang="la">Agricola lupum ovēs rapientem cōnspicātus canem vocāvit.</i> Vocabulário: <i>agricola, -ae</i> (m.), agricultor; <i>lupus, -ī</i>, lobo; <i>ovis, ovis</i> (f.), ovelha; <i>rapiō, rapere, rapuī, raptum</i>, arrebatar; <i>cōnspicor, cōnspicārī, cōnspicātus sum</i>, avistar; <i>canis, canis</i> (m.), cão; <i>vocō</i>, chamar.', [
            ('Qual é o verbo principal e quem é o sujeito?', '<i>Vocāvit</i>, perfeito, 3ª pessoa do singular: "chamou". O sujeito é <i>agricola</i>, nominativo singular (masculino, apesar da 1ª declinação).'),
            ('Que forma é <i>cōnspicātus</i>, e com que termo concorda?', 'Particípio perfeito do depoente <i>cōnspicor</i>, nominativo singular masculino: concorda com <i>agricola</i>. Como o verbo é depoente, o sentido é ativo e anterior: "tendo avistado".'),
            ('E <i>rapientem</i>?', 'Particípio presente de <i>rapiō</i> (verbo em <i>-iō</i>, por isso <i>-ient-</i>), acusativo singular. Não pode concordar com <i>ovēs</i> (plural) nem com <i>agricola</i> (nominativo): concorda com <i>lupum</i>. É um particípio predicativo do objeto de <i>cōnspicātus</i>: o lobo foi visto <b>arrebatando</b> as ovelhas.'),
            ('Qual é a função de <i>ovēs</i>?', 'Acusativo plural, objeto do particípio <i>rapientem</i>: o particípio conserva a regência do verbo <i>rapiō</i>.'),
            ('Que relação lógica liga <i>cōnspicātus</i> a <i>vocāvit</i>?', 'Tempo (anterioridade) e, pelo sentido, causa: ele chamou o cão <b>porque</b> viu o lobo. Ambas as traduções são aceitáveis.'),
            ('Monte a tradução.', '"O agricultor, tendo avistado o lobo arrebatando as ovelhas, chamou o cão." Ou, mais natural: "Quando avistou o lobo que arrebatava as ovelhas, o agricultor chamou o cão."'),
        ]),
        pratica_guiada('Prática guiada 2 · Uma frase, três relações lógicas',
            'Traduza cada frase escolhendo a conjunção portuguesa adequada. Vocabulário: <i>dormiō</i>, dormir; <i>fūr, fūris</i> (m.), ladrão; <i>intrō</i>, entrar; <i>moneō</i>, advertir; <i>pāreō</i> (+ dativo), obedecer; <i>tamen</i>, contudo.', [
            ('<i lang="la">Dominus dormiēns fūrem nōn audīvit.</i>', '<i>Dormiēns</i> concorda com <i>dominus</i> e explica por que ele não ouviu: relação <b>causal</b>. "Como estava dormindo, o senhor não ouviu o ladrão." O gerúndio ("dormindo, não ouviu") também serve, porque conserva a mesma ambiguidade do latim.'),
            ('<i lang="la">Fūr intrāns canem excitāvit.</i> (<i>excitō</i>, acordar)', '<i>Intrāns</i>, nominativo singular, concorda com <i>fūr</i>; a ação é simultânea: relação <b>temporal</b>. "Ao entrar, o ladrão acordou o cão" ou "o ladrão, quando entrava, acordou o cão".'),
            ('<i lang="la">Puer saepe monitus magistrō tamen nōn pāret.</i>', '<i>Monitus</i>, particípio perfeito passivo de <i>moneō</i>, concorda com <i>puer</i>; <i>tamen</i> na oração principal marca contraste: relação <b>concessiva</b>. "Embora tenha sido advertido muitas vezes, o menino contudo não obedece ao professor." Note a voz passiva: o menino foi advertido, não advertiu.'),
        ], 'Conclusão: a forma do particípio diz o tempo relativo e a voz; a relação lógica (causa, tempo, concessão) vem do sentido das orações e de palavras como <i>tamen</i>.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Identifique', 'Diga que particípio é (presente, perfeito ou futuro), o caso, o número e o gênero possíveis, e o verbo de origem.', [
            ('<i>amantem</i>', 'Particípio presente de <i>amō</i>, acusativo singular masculino ou feminino.'),
            ('<i>audītīs</i>', 'Particípio perfeito de <i>audiō</i>, dativo ou ablativo plural dos três gêneros: "aos (pelos) ouvidos".'),
            ('<i>ventūrī</i>', 'Particípio futuro de <i>veniō</i>: genitivo singular masculino ou neutro, ou nominativo (vocativo) plural masculino. "Que vai vir".'),
            ('<i>capientibus</i>', 'Particípio presente de <i>capiō</i>, dativo ou ablativo plural dos três gêneros.'),
            ('<i>secūtae</i>', 'Particípio perfeito do depoente <i>sequor</i>: genitivo ou dativo singular feminino, ou nominativo (vocativo) plural feminino. Sentido ativo: "tendo seguido".'),
            ('<i>euntēs</i>', 'Particípio presente de <i>eō</i> (<i>iēns, euntis</i>), nominativo, acusativo ou vocativo plural masculino ou feminino: "indo, os que vão".'),
            ('<i>regente</i>', 'Particípio presente de <i>regō</i>, ablativo singular dos três gêneros, com a terminação <i>-e</i> própria do uso verbal ou substantivo.'),
            ('<i>monitūrum</i>', 'Particípio futuro de <i>moneō</i>: acusativo singular masculino ou nominativo/acusativo/vocativo singular neutro.'),
        ]),
        exercicio('Exercício 2 · Forme os particípios', 'Dê os três particípios (no nominativo singular masculino) de cada verbo, ou diga por que algum falta.', [
            ('<i>laudō, laudāre, laudāvī, laudātum</i>, louvar', '<i>laudāns, laudantis</i>; <i>laudātus</i>; <i>laudātūrus</i>.'),
            ('<i>videō, vidēre, vīdī, vīsum</i>, ver', '<i>vidēns, videntis</i>; <i>vīsus</i>; <i>vīsūrus</i>.'),
            ('<i>dūcō, dūcere, dūxī, ductum</i>, conduzir', '<i>dūcēns, dūcentis</i>; <i>ductus</i>; <i>ductūrus</i>.'),
            ('<i>veniō, venīre, vēnī, ventum</i>, vir', '<i>veniēns, venientis</i>; não tem particípio perfeito pessoal, porque é intransitivo (a forma neutra <i>ventum</i> só aparece na passiva impessoal, <i>ventum est</i>); <i>ventūrus</i>.'),
            ('<i>loquor, loquī, locūtus sum</i>, falar (depoente)', '<i>loquēns, loquentis</i>; <i>locūtus</i>, com sentido ativo ("tendo falado"); <i>locūtūrus</i>.'),
            ('<i>sum, esse, fuī</i>, ser', 'Não tem particípio presente nem perfeito no latim clássico; o futuro é <i>futūrus</i>, "que vai ser", de onde vem o português "futuro".'),
        ]),
        exercicio('Exercício 3 · O tempo relativo', 'Traduza, prestando atenção ao tempo do verbo principal. Vocabulário: <i>cantō</i>, cantar; <i>legō, lēgī, lēctum</i>, ler; <i>liber, librī</i>, livro; <i>dormiō</i>, dormir; <i>discēdō, discessī</i>, partir; <i>nāvigō</i>, navegar.', [
            ('<i>Puellam cantantem audiō.</i>', 'Ouço a menina cantando (que canta). Presente com presente: simultaneidade no presente.'),
            ('<i>Puellam cantantem audīvī.</i>', 'Ouvi a menina cantando (que cantava). O mesmo particípio, agora simultâneo a um passado.'),
            ('<i>Librum ā magistrō lēctum lēgī.</i>', 'Li o livro (que tinha sido) lido pelo professor. Particípio perfeito com verbo no passado: anterioridade, expressa pelo mais-que-perfeito em português.'),
            ('<i>Nautae nāvigātūrī ad portum vēnērunt.</i> (<i>portus, -ūs</i>, porto)', 'Os marinheiros, que iam navegar (prestes a navegar), vieram ao porto. Particípio futuro: posterioridade.'),
            ('<i>Patrem dormientem nōn excitābō.</i> (<i>excitō</i>, acordar)', 'Não acordarei o pai que estará dormindo (enquanto dorme). Simultaneidade a um futuro.'),
        ]),
        exercicio('Exercício 4 · O particípio conjunto', 'Ache o termo com que o particípio concorda e traduza de duas maneiras: com gerúndio ou particípio português, e com uma oração (relativa, temporal, causal, concessiva ou coordenada). Vocabulário: <i>timeō</i>, temer; <i>clāmō</i>, gritar; <i>servus, -ī</i>, escravo; <i>līberō</i>, libertar; <i>dux, ducis</i>, comandante; <i>urbs, urbis</i>, cidade; <i>dēleō, dēlēvī, dēlētum</i>, destruir.', [
            ('<i>Puerī perīculum timentēs clāmābant.</i> (<i>perīculum</i>, perigo)', '<i>Timentēs</i> (nom. pl. m.) concorda com <i>puerī</i>. "Os meninos, temendo o perigo, gritavam" / "Como temiam o perigo, os meninos gritavam" (causal).'),
            ('<i>Dominus servum diū labōrantem līberāvit.</i> (<i>diū</i>, muito tempo; <i>labōrō</i>, trabalhar)', '<i>Labōrantem</i> (ac. sing.) concorda com <i>servum</i>. "O senhor libertou o escravo, que trabalhava havia muito tempo" (relativa). O particípio presente com <i>diū</i> indica ação que vinha de antes e continuava.'),
            ('<i>Dux urbem dēlētam relīquit.</i>', '<i>Dēlētam</i> (ac. sing. f.) concorda com <i>urbem</i>. "O comandante deixou a cidade destruída" / "O comandante destruiu a cidade e a deixou" (coordenada, se o contexto disser que foi ele quem a destruiu).'),
            ('<i>Mīles vulnerātus tamen pugnābat.</i>', '<i>Vulnerātus</i> (nom. sing. m.) concorda com <i>mīles</i>; <i>tamen</i> pede concessiva. "O soldado, ferido, continuava lutando" / "Embora estivesse ferido, o soldado contudo lutava".'),
            ('<i>Rēgīna fīliam ad templum euntem salūtāvit.</i> (<i>templum</i>, templo; <i>salūtō</i>, saudar)', '<i>Euntem</i> (ac. sing., de <i>eō</i>) concorda com <i>fīliam</i>. "A rainha saudou a filha indo ao templo" é ambíguo em português; melhor: "A rainha saudou a filha, que ia ao templo" (relativa).'),
        ]),
        exercicio('Exercício 5 · Do português para o latim', 'Traduza usando um particípio conjunto. Vocabulário: <i>fēmina, -ae</i>, mulher; <i>flōs, flōris</i> (m.), flor; <i>legō, legere</i>, colher; <i>cantō</i>, cantar; <i>vocō</i>, chamar; <i>lupus</i>, lobo; <i>fugiō</i>, fugir; <i>proficīscor, profectus sum</i>, partir; <i>Rōma, -ae</i>, Roma.', [
            ('A mulher, colhendo flores, cantava.', '<i>Fēmina flōrēs legēns cantābat.</i> <i>Legēns</i>, particípio presente, concorda com <i>fēmina</i> (nom. sing. f.) e tem o seu objeto <i>flōrēs</i>.'),
            ('O pai chamou o filho que fugia.', '<i>Pater fīlium fugientem vocāvit.</i> O particípio vai para o acusativo, concordando com <i>fīlium</i>; uma oração relativa também seria possível (capítulo 16), mas o particípio é mais latino.'),
            ('Tendo partido de Roma, o cônsul chegou à Grécia.', '<i>Cōnsul Rōmā profectus in Graeciam pervēnit.</i> (<i>perveniō</i>, chegar.) Só um depoente permite "tendo partido" com particípio: <i>profectus</i> tem sentido ativo. <i>Rōmā</i>, ablativo de origem sem preposição (nome de cidade).'),
            ('Os soldados mataram o lobo capturado.', '<i>Mīlitēs lupum captum necāvērunt.</i> (<i>necō</i>, matar.) <i>Captum</i>, perfeito passivo, concorda com <i>lupum</i>: o lobo foi capturado antes de ser morto.'),
        ]),
        exercicio('Exercício 6 · Leitura autêntica', 'Frases do Evangelho de Lucas e de Mateus (Vulgata Clementina). Identifique cada particípio, diga com que termo concorda e traduza. Vocabulário: <i>festīnō</i>, apressar-se; <i>īnfāns, īnfantis</i>, criança; <i>pōnō, positum</i>, pôr; <i>praesēpium</i>, manjedoura; <i>revertor, reversus sum</i>, voltar; <i>glōrificō</i>, glorificar; <i>telōnium</i>, banca de cobrador de impostos; <i>surgō</i>, levantar-se.', [
            ('<i>Et vēnērunt festīnantēs, et invēnērunt Mariam et Ioseph et īnfantem positum in praesēpiō.</i> (Lc 2,16)', '<i>Festīnantēs</i>: particípio presente, nom. pl. m., conjunto ao sujeito (os pastores): "vieram apressando-se, às pressas". <i>Positum</i>: particípio perfeito passivo de <i>pōnō</i>, ac. sing. m., concorda com <i>īnfantem</i>: "a criança posta (deitada) na manjedoura". Tradução: "E vieram às pressas e encontraram Maria, José e o menino deitado na manjedoura."'),
            ('<i>Et reversī sunt pāstōrēs glōrificantēs et laudantēs Deum.</i> (Lc 2,20, início)', '<i>Reversī sunt</i> é o perfeito do depoente <i>revertor</i> (verbo principal). <i>Glōrificantēs</i> e <i>laudantēs</i>: particípios presentes, nom. pl. m., conjuntos a <i>pāstōrēs</i>, com o objeto comum <i>Deum</i>. "E os pastores voltaram glorificando e louvando a Deus." A relação é de acompanhamento: o gerúndio é a melhor tradução.'),
            ('<i>Vīdit hominem sedentem in telōniō. [...] Et surgēns, secūtus est eum.</i> (Mt 9,9, trechos)', '<i>Sedentem</i>: particípio presente de <i>sedeō</i>, ac. sing., concorda com <i>hominem</i>; depois de <i>vīdit</i>, mostra a ação percebida: "viu um homem sentado na banca de impostos". <i>Surgēns</i>: particípio presente, nom. sing., conjunto ao sujeito de <i>secūtus est</i> (perfeito do depoente <i>sequor</i>): "e, levantando-se, seguiu-o". Simultaneidade imediata: "levantou-se e o seguiu".'),
        ]),
    ],
    leituras=['d-ooge-latin-for-beginners', 'kirtland-ritchie-s-fabulae-faciles', 'lhomond-epitome-historiae-sacrae', 'vulgata-biblia-sacra-vulgata-editio-clementina', 'eutropius-breviarium-ab-urbe-condita', 'bennett-new-latin-grammar'],
    leituras_nota='Para fixar as formas, faça os exercícios de particípios de <i>Latin for Beginners</i>, de D\'Ooge. Depois leia narrativas em que os particípios conjuntos aparecem a cada frase: as <i>Fabulae Faciles</i> (os trabalhos de Hércules e os Argonautas) e o <i>Epitome Historiae Sacrae</i>, de Lhomond. Na Vulgata, leia Mateus 2 e Lucas 2 inteiros, sublinhando cada particípio e o nome com que concorda. O <i>Breviarium</i> de Eutrópio é a primeira prosa histórica autêntica em que vale treinar a escolha da tradução (temporal, causal, coordenada). Bennett (§§ 336–337) resume os usos em duas páginas.',
)
