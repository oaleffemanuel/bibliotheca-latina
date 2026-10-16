from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Ab urbe condita I, 4, edição de R. S. Conway e C. F. Walters (Oxford, 1914), conferida no Perseus (1999.02.0160)
# e na The Latin Library (livy/liv.1.shtml). Grafia u/v normalizada para v; macrons acrescentados por este livro.
SECOES_TEXTO = [
    ('1', 'Sed dēbēbātur, ut opīnor, fātīs tantae orīgō urbis maximīque secundum deōrum opēs imperiī prīncipium.'),
    ('2', 'Vī compressa Vestālis cum geminum partum ēdidisset, seu ita rata seu quia deus auctor culpae honestior erat, Mārtem incertae stirpis patrem nuncupat.'),
    ('3', 'Sed nec dī nec hominēs aut ipsam aut stirpem ā crūdēlitāte rēgiā vindicant: sacerdōs vincta in custōdiam datur, puerōs in prōfluentem aquam mittī iubet.'),
    ('4', 'Forte quādam dīvīnitus super rīpās Tiberis effūsus lēnibus stagnīs nec adīrī usquam ad iūstī cursum poterat amnis et posse quamvīs languidā mergī aquā īnfantēs spem ferentibus dabat.'),
    ('5', 'Ita velut dēfūnctī rēgis imperiō in proximā alluviē ubi nunc fīcus Rūmīnālis est (Rōmulārem vocātam ferunt) puerōs expōnunt.'),
    ('6', 'Vastae tum in hīs locīs sōlitūdinēs erant. Tenet fāma cum fluitantem alveum, quō expositī erant puerī, tenuis in siccō aqua dēstituisset, lupam sitientem ex montibus quī circā sunt ad puerīlem vāgītum cursum flexisse; eam submissās īnfantibus adeō mītem praebuisse mammās ut linguā lambentem puerōs magister rēgiī pecoris invēnerit (Faustulō fuisse nōmen ferunt);'),
    ('7', 'ab eō ad stabula Larentiae uxōrī ēducandōs datōs. Sunt quī Larentiam volgātō corpore lupam inter pāstōrēs vocātam putent; inde locum fābulae ac mīrāculō datum.'),
    ('8', 'Ita genitī itaque ēducātī, cum prīmum adolēvit aetās, nec in stabulīs nec ad pecora segnēs vēnandō peragrāre saltūs.'),
    ('9', 'Hinc rōbore corporibus animīsque sūmptō iam nōn ferās tantum subsistere sed in latrōnēs praedā onustōs impetūs facere pāstōribusque rapta dīvidere et cum hīs crēscente in diēs grege iuvenum sēria ac iocōs celebrāre.'),
]
TEXTO = tabela(['§', 'Tito Lívio, <i>Ab urbe condita</i> I, 4'], [[n, f'<span lang="la">{t}</span>'] for n, t in SECOES_TEXTO],
               'Texto latino: ed. R. S. Conway e C. F. Walters (Oxford, 1914), domínio público; macrons deste livro', latim_cols=(1,))

LICAO = dict(
    slug='49-tito-livio', titulo='Tito Lívio: Rômulo e Remo (Ab urbe condita I)', titulo_latim='Līvius', tempo='90 min',
    resumo='Leitura comentada de Ab urbe condita I, 4: a vestal, os gêmeos lançados ao Tibre, a loba, Fáustulo e a juventude de Rômulo e Remo. Texto da edição Conway e Walters, vocabulário e notas, o discurso indireto como instrumento do historiador ("conta-se que…"), o infinitivo histórico, os ablativos absolutos, a análise de um período e a comparação com Eutrópio (capítulo 43).',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['Tito Lívio', 'Ab urbe condita', 'Rômulo e Remo', 'leitura comentada', 'narrativa histórica', 'discurso indireto', 'fāma est, ferunt', 'subordinadas no subjuntivo no discurso indireto', 'indicativo para observações do autor', 'oração consecutiva com perfeito do subjuntivo', 'oração relativa de caráter (sunt quī)', 'infinitivo histórico', 'presente histórico', 'ablativo absoluto', 'particípio conjunto', 'dēfungor + ablativo', 'gerundivo de finalidade (ēducandōs dare)', 'gerúndio no ablativo', 'comparação Lívio × Eutrópio'],
    prerequisitos=dict(texto='Capítulo 38 (o discurso indireto), com o que ele pressupõe: a oração infinitiva (capítulo 28), a interrogativa indireta e a sequência dos tempos (capítulos 34–35). Usamos ainda o ablativo absoluto (capítulo 30), o infinitivo histórico (capítulo 27), o gerúndio e o gerundivo (capítulo 31), os depoentes (capítulo 25) e, para a comparação, o capítulo 43 (Eutrópio).',
                       licoes=['38-o-discurso-indireto', '30-o-ablativo-absoluto', '27-os-infinitivos', '43-eutropio']),
    referencias=[
        referencia('Tito Lívio, Ab urbe condita I, 4, ed. R. S. Conway e C. F. Walters (Oxford, 1914)', 'Tito Lívio', catalogo='livius-ab-urbe-condita-liber-i', url='https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0160:book=1:chapter=4', nota='texto da leitura (§§ 1–9), conferido no Perseus; a edição imprime u por v (uincta, uocatam), aqui normalizado; macrons acrescentados por este livro', tipo='dominio_publico'),
        referencia('Tito Lívio, Ab urbe condita I (The Latin Library)', None, catalogo='the-latin-library', url='https://www.thelatinlibrary.com/livy/liv.1.shtml', nota='segunda conferência do capítulo 4: mesmo texto, salvo a grafia u/v e a pontuação', tipo='dominio_publico'),
        referencia('Eutrópio, Breviarium ab urbe condita I, 1', 'Eutrópio', catalogo='eutropius-breviarium-ab-urbe-condita', url='https://www.thelatinlibrary.com/eutropius/eutropius1.shtml', nota='frases da seção 6, no mesmo texto do capítulo 43 (The Latin Library, idêntico nas palavras à edição de F. Rühl, Teubner, 1887; macrons deste livro); a edição moderna da DCC não é usada como texto', tipo='dominio_publico'),
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 218.1 (fungor e compostos com ablativo), § 227 (ablativo absoluto), § 259.3 (presente histórico), § 268.2, 268.3 e 268.6 (infinitivo perfeito como tempo histórico; presente histórico como tempo principal ou histórico; perfeito do subjuntivo nas consecutivas depois de tempo histórico, frequente nos historiadores), § 283 (relativa de caráter), §§ 313–314 (discurso indireto; 314.3 indicativo nas observações do autor), § 317.a (infinitivo perfeito por qualquer tempo passado do indicativo), § 331 (acusativo com infinitivo), § 335 (infinitivo histórico), § 337.8.b.2 (gerundivo com dō e trādō para finalidade), § 338.4.a (gerúndio no ablativo)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 419 (ablativo absoluto), § 463 (infinitivo histórico), § 485.c (perfeito do subjuntivo nas consecutivas depois de tempo secundário), § 535 (relativa de caráter), § 580 (discurso indireto: principal no infinitivo, subordinadas no subjuntivo), § 583 (subordinada explicativa no indicativo), § 601 (estrutura do período, com exemplo de Lívio)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 372 (infinitivo histórico "usado pelos historiadores em descrições vívidas"), §§ 458–459 (ōrātiō oblīqua; o exemplo Narrant Rōmulum urbem condidisse)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 410, observação (infinitivo histórico, sujeito no nominativo), nn. 484–490 (discurso indireto; observação sobre as observações do autor no indicativo)', tipo='dominio_publico'),
    ],
    objetivos=[
        'Situar Tito Lívio e o livro I de <i>Ab urbe condita</i> e reconhecer a atitude do historiador diante da lenda.',
        'Ler e traduzir <i>Ab urbe condita</i> I, 4 com apoio das notas.',
        'Reconhecer no texto o discurso indireto narrativo (<i>tenet fāma, ferunt, sunt quī putent</i>), explicar os modos das subordinadas e distinguir as observações do próprio autor, no indicativo.',
        'Identificar infinitivos históricos, ablativos absolutos e particípios conjuntos, e traduzi-los com naturalidade.',
        'Comparar a mesma história em Lívio e em Eutrópio e descrever a diferença de estilo.',
    ],
    secoes=[
        ('Tito Lívio e Ab urbe condita', f'''
<p>Tito Lívio (<i>Titus Līvius</i>, c. 59 a.C. – c. 17 d.C., datas transmitidas pela tradição antiga), natural de Pádua, dedicou a vida a uma só obra: a história de Roma "desde a fundação da cidade" (<i>ab urbe conditā</i>) até a sua própria época, em 142 livros, dos quais restam 35 (os livros I–X e XXI–XLV). Escreveu sob Augusto, num momento em que Roma, depois das guerras civis, procurava no passado modelos de conduta; o prefácio diz isso abertamente: a história serve para mostrar exemplos a imitar e a evitar.</p>
<p>O livro I vai da chegada de Eneias à Itália até a expulsão do último rei, Tarquínio, o Soberbo. O capítulo 3 explicou o cenário do nosso trecho: em Alba Longa, Amúlio tomou o trono do irmão mais velho, Numitor, e, para que este não tivesse descendentes, fez da sobrinha, Reia Sílvia, uma vestal, isto é, uma sacerdotisa obrigada à virgindade. O capítulo 4, que lemos inteiro, conta o nascimento dos gêmeos, a sua exposição no Tibre, a loba e a juventude dos dois entre os pastores.</p>
<p>Lívio sabe que está contando lendas e diz isso no prefácio: os fatos anteriores à fundação chegam "mais adornados de fábulas poéticas do que de documentos". Por isso o capítulo está cheio de fórmulas de distância: <i>ut opīnor</i>, "segundo penso"; <i>ferunt</i>, "dizem"; <i>tenet fāma</i>, "conta a tradição"; <i>sunt quī putent</i>, "há quem pense". Gramaticalmente, essa distância tem um nome que você conhece do capítulo 38: o discurso indireto.</p>
{observacao('Sobre o texto', 'Seguimos a edição de R. S. Conway e C. F. Walters (Oxford, 1914), conferida no Perseus e, para as palavras, na The Latin Library. A edição imprime <i>u</i> também para o som consonantal (<i>uincta, uocatam</i>); aqui usamos <i>v</i>, como no resto deste livro, e acrescentamos os macrons. Grafias antigas como <i>volgātō</i> (por <i>vulgātō</i>) foram mantidas. Não marcamos a quantidade de algumas vogais incertas ou "ocultas" (por exemplo em <i>Larentia</i>, <i>nuncupat</i>). A edição está em domínio público (Conway morreu em 1933). Outras edições antigas conferidas, a de W. Weissenborn e H. J. Müller (Leipzig, Teubner) e a de B. O. Foster (Loeb, 1919), ambas no repositório da Perseus, trazem as mesmas palavras com estas diferenças: <i>diī</i> por <i>dī</i> (§ 3), <i>summissās</i> por <i>submissās</i> (§ 6) e <i>vulgātō</i> por <i>volgātō</i> (§ 7), questões de grafia; e, só em Weissenborn e Müller, <i>ēluviē</i> por <i>alluviē</i> (§ 5), duas palavras para "terreno inundado".')}
'''),
        ('O texto e a tradução', f'''
<p>O capítulo tem nove parágrafos curtos, numerados como nas edições. Leia primeiro os §§ 1–5 (a ação dos homens), depois os §§ 6–7 (a lenda, contada em discurso indireto) e por fim os §§ 8–9 (a juventude dos gêmeos, em infinitivos históricos).</p>
{TEXTO}
<p>Tradução deste livro:</p>
<p>[1] Mas, segundo penso, estava reservada aos fados a origem de tão grande cidade e o começo do maior império depois do poder dos deuses. [2] A vestal, violentada, depois de dar à luz gêmeos, declara Marte pai da sua descendência duvidosa, ou porque assim acreditava, ou porque um deus como autor da falta era mais honroso. [3] Mas nem deuses nem homens a livram, a ela e aos filhos, da crueldade do rei: a sacerdotisa é presa e posta sob guarda; os meninos, o rei manda lançá-los na corrente do rio. [4] Por um acaso providencial, o Tibre, que transbordara das margens em águas paradas e mansas, não deixava chegar em parte alguma até o leito normal do rio, e dava a quem levava os meninos a esperança de que, mesmo numa água sem correnteza, as crianças pudessem afogar-se. [5] Assim, como quem cumpre a ordem do rei, deixam os meninos no alagado mais próximo, onde hoje está a figueira Ruminal (dizem que se chamava Romular).</p>
<p>[6] Naqueles lugares havia então vastas solidões. Conta a tradição que, quando a água rasa deixou em seco a cesta flutuante em que os meninos tinham sido expostos, uma loba sedenta, vinda dos montes que há em volta, desviou o seu caminho na direção do choro das crianças; que se abaixou e ofereceu as tetas aos meninos, tão mansa que o chefe dos rebanhos do rei a encontrou lambendo-os com a língua (dizem que o seu nome era Fáustulo); [7] e que os meninos foram levados por ele aos estábulos e entregues à sua mulher, Larência, para serem criados. Há quem pense que Larência, por se prostituir, era chamada "loba" entre os pastores, e que daí veio a ocasião para a lenda e o prodígio.</p>
<p>[8] Nascidos assim e assim criados, logo que chegaram à idade adulta, sem ficarem ociosos nos estábulos nem junto ao gado, percorriam os bosques caçando. [9] Ganhando assim vigor no corpo e no ânimo, já não só enfrentavam as feras, mas também atacavam os salteadores carregados de presa e repartiam o que tomavam com os pastores; e com eles, enquanto o bando de jovens crescia dia a dia, passavam o tempo entre coisas sérias e brincadeiras.</p>
{dica('<b>Os tempos da tradução.</b> Lívio narra os §§ 2–5 no presente histórico (<i>nuncupat, vindicant, datur, iubet, expōnunt</i>; Bennett § 259.3) e os §§ 8–9 com infinitivos históricos, que equivalem a imperfeitos. A tradução conserva o presente nos §§ 2–5 e usa o imperfeito nos §§ 8–9 ("percorriam", "enfrentavam"), que é o valor do infinitivo histórico.')}
'''),
        ('Vocabulário e notas', f'''
{tabela(['§', 'Palavra ou expressão', 'Nota'], [
    ['1', 'dēbēbātur … fātīs', '"era devida aos fados": o sujeito é <i>orīgō</i> (e <i>prīncipium</i>). <i>Ut opīnor</i>, "como penso", é a voz do autor.'],
    ['1', 'secundum deōrum opēs', '<i>secundum</i>, preposição com acusativo, "depois de, logo abaixo de": o império romano só perde para o poder dos deuses.'],
    ['2', 'vī compressa Vestālis', '<i>vī</i>, ablativo de <i>vīs</i>, "força"; <i>comprimō</i>, "violentar". Particípio conjunto com o sujeito <i>Vestālis</i>.'],
    ['2', 'cum geminum partum ēdidisset', '<i>cum</i> com mais-que-perfeito do subjuntivo (capítulo 34); <i>ēdō, ēdere, ēdidī</i>, "dar à luz"; <i>geminus partus</i>, "parto duplo".'],
    ['2', 'seu ita rata seu quia …', '<i>rata</i>, particípio de <i>reor</i> (depoente), "pensar": "ou por pensar assim, ou porque…". Lívio oferece duas explicações e não escolhe.'],
    ['2', 'Mārtem … patrem nuncupat', '<i>nuncupō</i>, "declarar, nomear", com duplo acusativo: "declara Marte (como) pai". <i>Incertae stirpis</i>, genitivo: "da descendência duvidosa".'],
    ['3', 'ā crūdēlitāte rēgiā vindicant', '<i>vindicō ā</i>, "livrar de, proteger contra".'],
    ['3', 'sacerdōs vincta', '<i>vinciō, vīnxī, vinctum</i>, "amarrar, prender".'],
    ['3', 'puerōs … mittī iubet', '<i>iubeō</i> + acusativo com infinitivo passivo (capítulo 28): "manda que os meninos sejam lançados". O sujeito de <i>iubet</i> é o rei, subentendido.'],
    ['4', 'forte quādam dīvīnitus', '"por um acaso, providencial": <i>dīvīnitus</i>, "por vontade divina", corrige <i>forte</i>.'],
    ['4', 'Tiberis effūsus lēnibus stagnīs', '<i>Tiberis</i>, nominativo; <i>effūsus</i>, "transbordado"; <i>lēnibus stagnīs</i>, ablativo de modo, "em águas paradas e mansas".'],
    ['4', 'nec adīrī usquam ad iūstī cursum poterat amnis', '"não podia ser alcançado em parte alguma até o leito do rio normal": <i>iūstus amnis</i>, o rio no seu curso regular.'],
    ['4', 'posse … mergī … īnfantēs spem … dabat', 'a oração infinitiva <i>īnfantēs posse mergī</i> explica <i>spem</i>; <i>quamvīs languidā … aquā</i>, "numa água, por mais parada que fosse"; <i>ferentibus</i>, particípio substantivado no dativo: "aos que (os) levavam".'],
    ['5', 'velut dēfūnctī rēgis imperiō', '<i>dēfūnctī</i> é nominativo plural (sujeito: os servos) de <i>dēfungor</i>, "cumprir, desincumbir-se de", com ablativo (<i>imperiō</i>), como <i>fungor</i> (Bennett § 218.1). Não é "do rei falecido".'],
    ['5', 'in proximā alluviē', '<i>alluviēs, -ēī</i> (f.), "terreno alagado"; 5ª declinação.'],
    ['5', 'fīcus Rūmīnālis … Rōmulārem vocātam ferunt', '<i>fīcus</i>, "figueira", feminino; <i>ferunt</i> + infinitivo: "dizem que foi chamada Romular". <i>Ubi nunc … est</i>: a figueira ainda existia, ou era mostrada, no tempo de Lívio.'],
    ['6', 'tenet fāma', '"a tradição sustenta": introduz todo o discurso indireto dos §§ 6–7 (seção 4).'],
    ['6', 'fluitantem alveum', '<i>alveus, -ī</i>, "cesto, gamela"; <i>fluitō</i>, "flutuar".'],
    ['6', 'tenuis in siccō aqua dēstituisset', '<i>tenuis aqua</i>, "a água rasa", sujeito; <i>dēstituō</i>, "abandonar, deixar"; <i>in siccō</i>, "em seco".'],
    ['6', 'ad puerīlem vāgītum cursum flexisse', '<i>vāgītus, -ūs</i>, "vagido, choro de criança"; <i>flectō, flexī</i>, "dobrar, desviar".'],
    ['6', 'submissās … mammās', '<i>submittō</i>, "abaixar"; literalmente "ofereceu as tetas abaixadas", isto é, abaixou-se para oferecê-las.'],
    ['6', 'magister rēgiī pecoris', '"o chefe dos rebanhos do rei" (<i>pecus, -oris</i>, n.). <i>Lambentem</i>, particípio presente de <i>lambō</i>, predicativo do objeto <i>eam</i> (subentendido) de <i>invēnerit</i>.'],
    ['7', 'ēducandōs datōs', 'gerundivo de finalidade com <i>dō</i> (Bennett § 337.8.b.2): "entregues para serem criados".'],
    ['7', 'volgātō corpore', 'ablativo absoluto: "tendo prostituído o corpo" (<i>vulgō</i>, "tornar público").'],
    ['7', 'lupam', 'em latim, <i>lupa</i> é "loba" e também gíria para "prostituta": a explicação racional de Lívio joga com esse duplo sentido.'],
    ['8', 'cum prīmum adolēvit aetās', '<i>cum prīmum</i> + perfeito do indicativo, "logo que"; <i>adolēscō, adolēvī</i>, "crescer".'],
    ['8', 'segnēs … peragrāre saltūs', '<i>segnis</i>, "indolente"; <i>peragrō</i>, "percorrer"; <i>saltus, -ūs</i>, "bosque, desfiladeiro". <i>Peragrāre</i> é infinitivo histórico (seção 5); <i>vēnandō</i>, gerúndio de <i>vēnor</i>, "caçar".'],
    ['9', 'rōbore … sūmptō', 'ablativo absoluto: "tomado vigor".'],
    ['9', 'subsistere … facere … dīvidere … celebrāre', 'quatro infinitivos históricos. <i>Subsistō</i> + acusativo, "enfrentar"; <i>impetum facere in</i> + acusativo, "atacar".'],
    ['9', 'praedā onustōs', '<i>onustus</i>, "carregado", com ablativo.'],
    ['9', 'crēscente in diēs grege', 'ablativo absoluto com particípio presente: "crescendo dia a dia o bando".'],
    ['9', 'sēria ac iocōs celebrāre', '"celebrar coisas sérias e brincadeiras": passar o tempo juntos, no trabalho e na festa.'],
], 'Notas a Ab urbe condita I, 4', latim_cols=(1,))}
'''),
        ('O discurso indireto na narrativa histórica', f'''
<p>Nos §§ 6–7, Lívio não afirma que uma loba amamentou os gêmeos: afirma que a tradição o afirma. A frase principal é <i>Tenet fāma</i>, e tudo o que ela sustenta vem em discurso indireto, segundo as regras do capítulo 38 (Bennett §§ 313–314; A&amp;G § 580; Kennedy §§ 458–459): as orações principais passam ao <b>acusativo com infinitivo</b>, e as subordinadas ao <b>subjuntivo</b>.</p>
{tabela(['Discurso indireto (Lívio)', 'Discurso direto equivalente', 'Regra'], [
    ['<i>lupam … cursum <b>flexisse</b></i>', '<i>lupa … cursum <b>flexit</b></i>', 'principal: indicativo → acusativo com infinitivo (perfeito → infinitivo perfeito)'],
    ['<i>eam … mītem <b>praebuisse</b> mammās</i>', '<i>ea … mītis <b>praebuit</b> mammās</i>', 'idem; o predicativo <i>mītem</i> passa também ao acusativo'],
    ['<i>(puerōs) ab eō … ēducandōs <b>datōs</b></i> (subentenda <i>esse</i>)', '<i>(puerī) ab eō … ēducandī <b>datī sunt</b></i>', 'perfeito passivo → infinitivo perfeito passivo'],
    ['<i>cum … aqua <b>dēstituisset</b></i>', '<i>cum … aqua <b>dēstituisset</b></i>', 'subordinada: subjuntivo, na sequência secundária (com o <i>cum</i> narrativo do capítulo 34, já seria subjuntivo no direto)'],
    ['<i>ut … magister <b>invēnerit</b></i>', '<i>ut … magister <b>invēnerit</b></i>', 'consecutiva: já é subjuntiva no direto; perfeito do subjuntivo depois de tempo histórico (seção 5)'],
    ['<i>quō expositī <b>erant</b> puerī</i>; <i>quī circā <b>sunt</b></i>', '(idem)', '<b>exceção</b>: observações do próprio autor ficam no indicativo (Bennett § 314.3; A&amp;G § 583)'],
], 'Os §§ 6–7 em discurso indireto e direto')}
<p>A última linha da tabela é a mais instrutiva. Uma oração subordinada que, pela regra, deveria estar no subjuntivo aparece no indicativo quando contém uma informação do <b>narrador</b>, não da fonte citada. <i>Quī circā sunt</i>, "que há em volta", é Lívio falando dos montes de Roma que o seu leitor conhecia; por isso o presente do indicativo, num trecho todo no passado. <i>Quō expositī erant puerī</i> é uma retomada do que o próprio Lívio contou no § 5. O modo verbal mostra de quem é cada afirmação: subjuntivo, a tradição; indicativo, o historiador.</p>
<p>O mesmo procedimento aparece em escala menor: <i>Rōmulārem vocātam ferunt</i> e <i>Faustulō fuisse nōmen ferunt</i>, parênteses com <i>ferunt</i> + infinitivo; e <i>Sunt quī … putent</i>, oração relativa de caráter no subjuntivo (Bennett § 283; A&amp;G § 535), que introduz uma versão concorrente e racionalista, também em discurso indireto (<i>Larentiam … lupam … vocātam</i>, <i>inde locum … datum</i>, com <i>esse</i> subentendido nos dois). Lívio dá as duas versões, a maravilhosa e a racional, e deixa o leitor decidir.</p>
{observacao('Fāma, ferunt, trāditur', 'Os historiadores latinos têm um repertório de fórmulas para atribuir uma informação a outros: <i>fāma est</i> ou <i>tenet fāma</i>, <i>ferunt</i> ou <i>dīcunt</i>, <i>trāditur</i> ou <i>trāditum est</i> (com oração infinitiva), <i>sunt quī</i> + subjuntivo. Ao traduzir, mantenha a distância: "conta-se que", "dizem que", "há quem pense". Apagar essas fórmulas transforma a dúvida de Lívio em afirmação.')}
'''),
        ('Narrativa histórica: presente histórico, infinitivo histórico e ablativo absoluto', f'''
<p>Três recursos dão ritmo à narração de Lívio, e os três estão concentrados neste capítulo.</p>
<h3>O presente histórico</h3>
<p>Nos §§ 2–5, os fatos decisivos estão no presente: <i>nuncupat</i>, <i>vindicant</i>, <i>datur</i>, <i>iubet</i>, <i>expōnunt</i> (Bennett § 259.3). O efeito é o de uma cena que se passa diante do leitor. Note que <i>ēdidisset</i>, dentro da oração com <i>cum</i>, está no mais-que-perfeito do subjuntivo: o presente histórico pode ser tratado como tempo secundário e pedir a sequência dos tempos do passado (Bennett § 268.3).</p>
<h3>O infinitivo histórico</h3>
<p>Nos §§ 8–9, os verbos principais são infinitivos: <i>peragrāre</i>, <i>subsistere</i>, <i>facere</i>, <i>dīvidere</i>, <i>celebrāre</i>. Não dependem de nada. É o <b>infinitivo histórico</b>, que você viu no capítulo 27: o infinitivo presente usado na narração no lugar do imperfeito do indicativo, com o sujeito no <b>nominativo</b> (Bennett § 335; A&amp;G § 463; Kennedy § 372; Ravizza n. 410, obs.). O sujeito, aqui, são os gêmeos, subentendidos, e por isso os adjetivos e particípios que se referem a eles estão no nominativo: <i>genitī</i>, <i>ēducātī</i>, <i>segnēs</i>.</p>
{comparacao('Infinitivo histórico × infinitivo do discurso indireto', ['Latim', 'Construção', 'Como saber'], [
    ['(geminī) … <b>peragrāre</b> saltūs', 'infinitivo histórico', 'nenhum verbo de dizer ou pensar; sujeito no nominativo (<i>segnēs</i>); vale "percorriam"'],
    ['Tenet fāma … lupam … cursum <b>flexisse</b>', 'oração infinitiva (discurso indireto)', 'depende de <i>tenet fāma</i>; sujeito no acusativo (<i>lupam</i>)'],
])}
<p>Kennedy define o infinitivo histórico como próprio "dos historiadores, em descrições vívidas". É isso que ele faz aqui: uma série de ações habituais, sem pormenor, que resume os anos de juventude em duas frases.</p>
<h3>Ablativo absoluto e particípio conjunto</h3>
<p>Lívio usa a gama completa das construções participiais do capítulo 30. Há <b>ablativos absolutos</b> com particípio perfeito (<i>rōbore … sūmptō</i>, <i>volgātō corpore</i>) e presente (<i>crēscente in diēs grege</i>); e há <b>particípios conjuntos</b> que concordam com o sujeito ou o objeto (<i>vī compressa Vestālis</i>, <i>sacerdōs vincta</i>, <i>lupam sitientem</i>, <i>lambentem</i>, <i>genitī … ēducātī</i>). A diferença é a de sempre (Bennett § 227; A&amp;G § 419): no ablativo absoluto, o nome não tem função na oração principal; em <i>rōbore … sūmptō</i>, o vigor não é sujeito nem objeto de <i>subsistere</i>.</p>
<h3>A consecutiva com perfeito do subjuntivo</h3>
<p>Em <i>adeō mītem praebuisse mammās ut … magister … invēnerit</i>, a oração consecutiva depende de um infinitivo perfeito que equivale a um tempo histórico (Bennett § 268.2); pela sequência dos tempos esperaríamos o imperfeito <i>invenīret</i>. O perfeito do subjuntivo apresenta o resultado como um fato pontual, "chegou a encontrá-la"; Bennett (§ 268.6) observa que o uso é raro em Cícero e frequente nos historiadores, e A&amp;G (§ 485.c) o dá como regular nas consecutivas depois de tempos secundários.</p>
'''),
        ('Lívio e Eutrópio: a mesma história', f'''
<p>No capítulo 43 você leu o começo do <i>Breviarium</i> de Eutrópio, escrito no século IV d.C., quase quatro séculos depois de Lívio. Eutrópio resume em poucas linhas o que Lívio conta em dois capítulos:</p>
{exemplos([
    ('Rōmānum imperium … ā Rōmulō exōrdium habet, quī Rēae Silviae, Vestālis virginis, fīlius et, quantum putātus est, Mārtis cum Remō frātre ūnō partū ēditus est. Is cum inter pāstōrēs latrōcinārētur, decem et octō annōs nātus urbem exiguam in Palātīnō monte cōnstituit …', 'O Império Romano … começa com Rômulo, que, filho de Reia Sílvia, virgem vestal, e, segundo se julgou, de Marte, nasceu de um só parto com o irmão Remo. Este, quando vivia de saques entre os pastores, aos dezoito anos fundou uma pequena cidade no monte Palatino… (Eutrópio, I, 1)'),
])}
{tabela(['', 'Lívio, I, 4', 'Eutrópio, I, 1'], [
    ['O pai divino', '<i>seu ita rata seu quia deus auctor culpae honestior erat, Mārtem … patrem nuncupat</i>: a mãe declara; o historiador sugere dois motivos.', '<i>quantum putātus est, Mārtis</i>: a dúvida reduzida a um parêntese.'],
    ['O nascimento', '<i>cum geminum partum ēdidisset</i>', '<i>cum Remō frātre ūnō partū ēditus est</i>: o mesmo verbo <i>ēdō</i>, agora no passivo.'],
    ['A loba', 'contada em discurso indireto (<i>tenet fāma</i>), com uma versão racional (<i>sunt quī … putent</i>).', 'omitida.'],
    ['A juventude', 'caçam e atacam os salteadores (<i>in latrōnēs … impetūs facere</i>).', 'Rômulo é ele mesmo um salteador (<i>inter pāstōrēs latrōcinārētur</i>).'],
    ['A frase', 'períodos longos, discurso indireto, infinitivos históricos, ablativos absolutos.', 'orações curtas: relativa, <i>cum</i>, verbo principal; vocabulário mais simples.'],
], 'Duas versões de Rômulo e Remo')}
<p>A comparação mostra o que é o estilo de Lívio: não só mais palavras, mas uma atitude. Eutrópio informa; Lívio conta, pondera as fontes, mostra a sua distância e constrói cenas. Note, porém, uma divergência de conteúdo que nenhum dos dois discute: para Lívio, os jovens atacam os ladrões; para Eutrópio, Rômulo "praticava o banditismo" entre os pastores. Os historiadores antigos não tinham uma versão única da lenda, e o próprio Lívio, no capítulo seguinte (I, 5), conta que os salteadores acusaram Remo de roubar as terras de Numitor.</p>
{analise('Ab urbe condita I, 4, 2, palavra a palavra', [
    ('Vī', 'vīs, vim, vī (f.), força', 'ablativo singular', 'meio de <i>compressa</i>'),
    ('compressa', 'comprimō, -ere, -pressī, -pressum, violentar', 'particípio perfeito passivo, nom. sing. fem.', 'particípio conjunto com <i>Vestālis</i>'),
    ('Vestālis', 'Vestālis, -is (f.), vestal', 'nominativo singular', 'sujeito de <i>nuncupat</i> (e de <i>ēdidisset</i>)'),
    ('cum', 'conjunção', '+ subjuntivo', 'temporal-causal: "depois de, como"'),
    ('geminum partum', 'geminus, -a, -um; partus, -ūs (m.), parto', 'acusativo singular', 'objeto de <i>ēdidisset</i>'),
    ('ēdidisset', 'ēdō, -ere, ēdidī, ēditum, dar à luz', 'mais-que-perfeito do subjuntivo, 3ª sing.', 'verbo da oração com <i>cum</i>'),
    ('seu … seu', 'conjunções', 'invariáveis', '"ou … ou": duas explicações alternativas'),
    ('ita rata', 'reor, rērī, ratus sum, pensar', 'particípio perfeito (depoente), nom. sing. fem.', '"tendo pensado assim": refere-se a <i>Vestālis</i>'),
    ('quia … erat', 'quia (conj.); sum', 'imperfeito do indicativo', 'causal: razão apresentada pelo autor'),
    ('deus auctor', 'deus, -ī; auctor, -ōris (m.), autor', 'nominativo singular', 'sujeito de <i>erat</i> ("um deus como autor")'),
    ('culpae', 'culpa, -ae (f.), falta', 'genitivo singular', 'complemento de <i>auctor</i>'),
    ('honestior', 'honestus, comparativo', 'nominativo singular', 'predicativo: "mais honroso"'),
    ('Mārtem', 'Mārs, Mārtis (m.), Marte', 'acusativo singular', 'objeto de <i>nuncupat</i>'),
    ('incertae stirpis', 'incertus; stirps, stirpis (f.), descendência', 'genitivo singular', 'complemento de <i>patrem</i>'),
    ('patrem', 'pater, patris (m.), pai', 'acusativo singular', 'predicativo do objeto (<i>Mārtem … patrem</i>)'),
    ('nuncupat', 'nuncupō, -āre, declarar, nomear', 'presente do indicativo, 3ª sing. (presente histórico)', 'verbo principal'),
])}
{diagrama_frase([('Tenet fāma', 'principal · conta a tradição'), ('cum … dēstituisset', 'subjuntivo · quando deixou em seco'), ('lupam sitientem', 'sujeito ac. · uma loba sedenta'), ('cursum', 'objeto · o caminho'), ('flexisse', 'infinitivo · ter desviado')], 'O esqueleto do § 6: <i>Tenet fāma … lupam … cursum flexisse</i>. A oração com <i>cum</i>, encaixada antes do sujeito do infinitivo, fica no subjuntivo porque está dentro do discurso indireto.')}
'''),
    ],
    erros_comuns=[
        ('Ler <i>velut dēfūnctī rēgis imperiō</i> como "por ordem do rei morto".', 'O rei, Amúlio, está bem vivo. <i>Dēfūnctī</i> é nominativo plural, sujeito de <i>expōnunt</i>, e vem de <i>dēfungor</i>, "cumprir", que rege ablativo (<i>imperiō</i>), como <i>fungor</i>. <i>Rēgis</i> depende de <i>imperiō</i>: "como quem cumpriu a ordem do rei".'),
        ('Procurar um verbo de que dependam <i>peragrāre</i>, <i>subsistere</i>, <i>facere</i>.', 'São infinitivos históricos, que funcionam como verbos principais no imperfeito. O sujeito no nominativo (<i>genitī, ēducātī, segnēs</i>) distingue-os dos infinitivos do discurso indireto, cujo sujeito está no acusativo.'),
        ('Corrigir mentalmente <i>quō expositī erant</i> e <i>quī circā sunt</i> para o subjuntivo.', 'O indicativo é intencional: são observações do narrador, não parte do que "a tradição sustenta" (Bennett § 314.3; A&amp;G § 583). O modo mostra quem garante a informação.'),
        ('Traduzir <i>Tenet fāma</i> por "a fama tem" ou "a fama mantém".', '<i>Fāma</i> é "o que se diz, a tradição", e <i>tenet</i> + oração infinitiva vale "sustenta que, conta que". Em português: "conta a tradição que…".'),
        ('Ler <i>ut … invēnerit</i> como oração final.', 'Depois de <i>adeō</i>, "a tal ponto", a oração com <i>ut</i> é consecutiva: "tão mansa que o pastor a encontrou". Uma final diria a intenção da loba, o que não faz sentido.'),
        ('Ignorar o duplo sentido de <i>lupa</i>.', 'A explicação racional do § 7 só se entende sabendo que <i>lupa</i> também designava a prostituta. Traduza com aspas ("loba") e, se necessário, com uma nota.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Do discurso indireto ao direto',
            'Transforme em discurso direto, como se a própria tradição falasse: <i lang="la">Tenet fāma … lupam sitientem ex montibus quī circā sunt ad puerīlem vāgītum cursum flexisse; eam submissās īnfantibus adeō mītem praebuisse mammās ut linguā lambentem puerōs magister rēgiī pecoris invēnerit.</i>', [
            ('Qual é o verbo introdutor, e o que muda ao retirá-lo?', '<i>Tenet fāma</i>. Sem ele, as orações infinitivas voltam a ser orações principais no indicativo, e os seus sujeitos voltam ao nominativo.'),
            ('Reescreva a primeira oração.', '<i>Lupa sitiēns ex montibus quī circā sunt ad puerīlem vāgītum cursum flexit.</i> O infinitivo perfeito <i>flexisse</i> corresponde ao perfeito do indicativo <i>flexit</i> (Bennett § 317.a); <i>lupam sitientem</i> passa a <i>lupa sitiēns</i>.'),
            ('E a segunda?', '<i>Ea submissās īnfantibus adeō mītis praebuit mammās ut …</i> O predicativo <i>mītem</i> acompanha o sujeito e volta ao nominativo, <i>mītis</i>.'),
            ('A oração consecutiva muda?', 'Não no modo: consecutivas estão sempre no subjuntivo. <i>Ut linguā lambentem puerōs magister rēgiī pecoris invēnerit</i> pode ficar igual (ou <i>invenīret</i>, na sequência regular).'),
            ('E <i>quī circā sunt</i>?', 'Fica igual: já estava no indicativo, porque é observação do autor.'),
        ], 'A transformação mostra que o discurso indireto não muda o conteúdo, só a responsabilidade por ele: no direto, o narrador afirma; no indireto, ele relata.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Compreensão', 'Responda em português.', [
            ('Que duas explicações Lívio oferece para a vestal declarar Marte como pai?', 'Ou ela acreditava nisso (<i>ita rata</i>), ou um deus como autor da falta era mais honroso (<i>quia deus auctor culpae honestior erat</i>).'),
            ('Por que os meninos não se afogaram, segundo o § 4?', 'Porque o Tibre transbordara em águas paradas e não se podia chegar à corrente; os servos os deixaram na beira alagada, e a água baixou, deixando o cesto em seco (§ 6).'),
            ('Qual é a explicação "racional" da lenda da loba?', 'A mulher de Fáustulo, Larência, por se prostituir, seria chamada <i>lupa</i> pelos pastores; daí teria nascido a fábula (§ 7).'),
            ('O que os gêmeos faziam na juventude?', 'Caçavam nos bosques, enfrentavam feras, atacavam salteadores carregados de presa e repartiam o butim com os pastores (§§ 8–9).'),
        ]),
        exercicio('Exercício 2 · Discurso indireto', 'Diga se cada forma está em discurso indireto e explique o modo ou a forma.', [
            ('<i>Rōmulārem <b>vocātam</b> ferunt</i> (§ 5)', 'Discurso indireto: infinitivo perfeito passivo (<i>vocātam esse</i>, com <i>esse</i> omitido) depois de <i>ferunt</i>; o sujeito subentendido é <i>fīcum</i>, por isso o feminino.'),
            ('<i>Faustulō <b>fuisse</b> nōmen ferunt</i> (§ 6)', 'Discurso indireto: infinitivo perfeito; no direto, <i>Faustulō nōmen erat</i>. <i>Faustulō</i> é dativo de posse.'),
            ('<i>cum fluitantem alveum … aqua <b>dēstituisset</b></i>', 'Subordinada dentro do discurso indireto, no subjuntivo mais-que-perfeito (sequência secundária).'),
            ('<i>quō expositī <b>erant</b> puerī</i>', 'Indicativo dentro do discurso indireto: retomada do narrador, que não faz parte da tradição citada (Bennett § 314.3).'),
            ('<i>Sunt quī Larentiam … vocātam <b>putent</b></i>', 'Não é discurso indireto: <i>putent</i> é subjuntivo de uma relativa de caráter (Bennett § 283). Mas o que segue (<i>vocātam</i>, <i>datum</i>) é oração infinitiva que depende de <i>putent</i>.'),
        ]),
        exercicio('Exercício 3 · Particípios e ablativos absolutos', 'Classifique como ablativo absoluto ou particípio conjunto e traduza.', [
            ('<i>Vī compressa Vestālis</i>', 'Particípio conjunto: <i>compressa</i> concorda com o sujeito <i>Vestālis</i>; <i>vī</i> é ablativo de meio. "A vestal, violentada…"'),
            ('<i>volgātō corpore</i>', 'Ablativo absoluto: <i>corpore</i> não tem função na oração. "Por ter prostituído o corpo."'),
            ('<i>rōbore corporibus animīsque sūmptō</i>', 'Ablativo absoluto: "tendo ganho vigor no corpo e no ânimo". <i>Corporibus animīsque</i> entende-se como dativo ("para o corpo e o ânimo") ou, segundo outros, como ablativo de referência ("no corpo e no ânimo"); o sentido é o mesmo.'),
            ('<i>crēscente in diēs grege iuvenum</i>', 'Ablativo absoluto com particípio presente: ação simultânea, "enquanto o bando crescia dia a dia".'),
            ('<i>lupam sitientem</i>', 'Particípio conjunto com <i>lupam</i>, sujeito do infinitivo: "uma loba sedenta".'),
        ]),
        exercicio('Exercício 4 · Infinitivo histórico', 'Reescreva com o imperfeito do indicativo e traduza.', [
            ('<i>(geminī) vēnandō peragrāre saltūs</i>', '<i>Vēnandō peragrābant saltūs.</i> "Percorriam os bosques caçando."'),
            ('<i>in latrōnēs praedā onustōs impetūs facere</i>', '<i>In latrōnēs praedā onustōs impetūs faciēbant.</i> "Atacavam os salteadores carregados de presa."'),
            ('<i>pāstōribusque rapta dīvidere</i>', '<i>Pāstōribusque rapta dīvidēbant.</i> "E repartiam o que tomavam com os pastores." <i>Pāstōribus</i>, dativo; <i>rapta</i>, neutro plural substantivado.'),
        ]),
        exercicio('Exercício 5 · Lívio × Eutrópio', 'Responda com base na seção 6.', [
            ('Que verbo latino Lívio e Eutrópio usam para o nascimento, e em que voz?', '<i>Ēdō</i>: Lívio, na voz ativa, com a mãe por sujeito (<i>geminum partum ēdidisset</i>); Eutrópio, na passiva, com Rômulo por sujeito (<i>ūnō partū ēditus est</i>).'),
            ('Como cada um exprime a dúvida sobre Marte?', 'Lívio, com duas explicações coordenadas por <i>seu … seu</i>; Eutrópio, com o parêntese <i>quantum putātus est</i>, "segundo se julgou".'),
            ('Reescreva em latim simples, à maneira de Eutrópio, a frase "A loba alimentou os meninos e Fáustulo os encontrou."', '<i>Lupa puerōs aluit, et Faustulus eōs invēnit.</i> (<i>alō, alere, aluī</i>, "alimentar".) Frase direta, sem discurso indireto: o tom de Eutrópio, que não discute as fontes.'),
        ]),
    ],
    leituras=['livius-ab-urbe-condita-liber-i', 'eutropius-breviarium-ab-urbe-condita', 'lhomond-urbis-romae-viri-illustres-selecoes', 'lodge-gildersleeve-s-latin-grammar', 'bennett-new-latin-grammar'],
    leituras_nota='Continue no livro I de Lívio pelo Perseus (capítulos 5–7: o reconhecimento dos gêmeos, a morte de Amúlio, os auspícios e a morte de Remo), consultando a análise morfológica ao clique. O <i>Breviarium</i> de Eutrópio (DCC) dá o resumo dos mesmos fatos para comparar, e o <i>Dē virīs illūstribus</i> de Lhomond reconta Rômulo em latim simples, a partir de Lívio: bom para uma leitura rápida antes do original. Para o discurso indireto, a gramática de Gildersleeve é a mais detalhada; Bennett (§§ 313–318) a mais concisa.',
)
