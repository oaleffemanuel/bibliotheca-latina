from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Eneida II, 1–20, edição de J. B. Greenough (Boston, Ginn & Co., 1900), conferida no Perseus (1999.02.0055)
# e na The Latin Library (vergil/aen2.shtml). Pontuação de Greenough; macrons acrescentados por este livro.
VERSOS = [
    (1, 'Conticuēre omnēs, intentīque ōra tenēbant.'),
    (2, 'Inde torō pater Aenēās sīc ōrsus ab altō:'),
    (3, 'Īnfandum, rēgīna, iubēs renovāre dolōrem,'),
    (4, 'Trōiānās ut opēs et lāmentābile rēgnum'),
    (5, 'ēruerint Danaī; quaeque ipse miserrima vīdī,'),
    (6, 'et quōrum pars magna fuī. Quis tālia fandō'),
    (7, 'Myrmidonum Dolopumve aut dūrī mīles Ulixī'),
    (8, 'temperet ā lacrimīs? Et iam nox ūmida caelō'),
    (9, 'praecipitat, suādentque cadentia sīdera somnōs.'),
    (10, 'Sed sī tantus amor cāsūs cognōscere nostrōs'),
    (11, 'et breviter Trōiae suprēmum audīre labōrem,'),
    (12, 'quamquam animus meminisse horret, lūctūque refūgit,'),
    (13, 'incipiam. Frāctī bellō fātīsque repulsī'),
    (14, 'ductōrēs Danaum, tot iam lābentibus annīs,'),
    (15, 'īnstar montis equum dīvīnā Palladis arte'),
    (16, 'aedificant, sectāque intexunt abiete costās:'),
    (17, 'vōtum prō reditū simulant; ea fāma vagātur.'),
    (18, 'Hūc dēlēcta virum sortītī corpora fūrtim'),
    (19, 'inclūdunt caecō laterī, penitusque cavernās'),
    (20, 'ingentīs uterumque armātō mīlite complent.'),
]
TEXTO = tabela(['v.', 'Vergílio, <i>Eneida</i> II, 1–20'], [[str(n), f'<span lang="la">{v}</span>'] for n, v in VERSOS],
               'Texto latino: ed. J. B. Greenough (1900), domínio público; macrons deste livro', latim_cols=(1,))

LICAO = dict(
    slug='47-virgilio', titulo='Virgílio: a queda de Troia (Eneida II)', titulo_latim='Vergilius', tempo='90 min',
    resumo='Leitura comentada dos vinte primeiros versos do livro II da Eneida: Eneias começa a contar a Dido a queda de Troia e os gregos constroem o cavalo de madeira. Texto da edição Greenough, vocabulário e notas, escansão do hexâmetro com elisão, os traços do estilo épico, análise de um período e tradução própria.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['Virgílio', 'Eneida II', 'leitura comentada', 'hexâmetro datílico', 'escansão', 'elisão', 'ectlipse e sinalefa', 'cesura', 'sinizese e i consonantal (abiete)', 'perfeito em -ēre', 'genitivo plural em -um (Danaum, virum)', 'acusativo plural em -īs', 'interrogativa indireta com ut', 'subjuntivo potencial', 'gerúndio no ablativo', 'ablativo absoluto na poesia', 'presente histórico', 'hipérbato', 'enjambement', 'hendíadis', 'estilo épico', 'tradução de poesia'],
    prerequisitos=dict(texto='Capítulo 46 (Ovídio), em que você leu pela primeira vez um trecho longo em hexâmetros; por trás dele, o capítulo 40 (métrica e figuras). Usamos também o ablativo absoluto (capítulo 30), a interrogativa indireta (capítulo 35), o subjuntivo independente (capítulo 32), o gerúndio (capítulo 31) e os depoentes (capítulo 25).',
                       licoes=['46-ovidio', '40-metrica-e-figuras', '30-o-ablativo-absoluto', '35-a-interrogativa-indireta']),
    referencias=[
        referencia('Vergílio, Aeneis II, 1–20, ed. J. B. Greenough (Boston, Ginn & Co., 1900)', 'Públio Vergílio Marão', catalogo='maro-aeneis-texto-integral', url='https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0055:book=2:card=1', nota='texto da leitura, conferido verso a verso no Perseus e no TEI do PerseusDL (phi0690.phi003, que indica a impressão de 1881); v. 2 (ab altō, sem est) conferido também em Ribbeck 1861, Conington 1895 e Fairclough 1916 (archive.org); pontuação de Greenough; macrons acrescentados por este livro', tipo='dominio_publico'),
        referencia('Vergílio, Aeneis II (The Latin Library)', None, catalogo='the-latin-library', url='https://www.thelatinlibrary.com/vergil/aen2.shtml', nota='segunda conferência do texto: mesmas palavras nos vv. 1–20; só a pontuação difere', tipo='dominio_publico'),
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar', nota='§ 25.6.c (genitivo plural em -um), § 67.3.a (acusativo plural em -īs dos adjetivos da 3ª declinação), § 101 (perfeito em -ērunt ou -ēre), § 227 (ablativo absoluto), § 259.3 (presente histórico), § 280.2 (subjuntivo potencial), § 300 (interrogativa indireta), § 338.4.a e 338.5 (gerúndio no ablativo, com objeto), §§ 366.7 e 366.10 (elisão; sílaba final anceps), § 367.4 (i consonantal: abjete por abiete), § 368 (hexâmetro; 368.3 cesuras, com o v. 2 deste trecho como exemplo), § 350.11.a (hipérbato), § 374.4 (hendíadis)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc', nota='§ 163, nota 3 (as terminações -ērunt e -ēre do perfeito), § 419 (ablativo absoluto), §§ 445–447 (subjuntivo potencial), §§ 573–574 (interrogativa indireta), § 598 (ordem das palavras)', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer', nota='§ 474 (elisão ou sinalefa da vogal final; ectlipse da vogal + m; hiato), § 477 (hexâmetro datílico: os quatro primeiros pés dáctilos ou espondeus, o quinto dáctilo, o sexto espondeu ou troqueu)', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina', nota='n. 535 (figuras de escansão: "elisão" para a sílaba final em -m, com o exemplo suprēmum audīre labōrem, Eneida II, 11; "sinalefa" para a vogal final, com o exemplo Conticuēre omnēs, Eneida II, 1), n. 536 (o hexâmetro)', tipo='dominio_publico'),
        referencia('A Latin Dictionary (Lewis & Short)', 'Charlton T. Lewis e Charles Short', catalogo='short-a-latin-dictionary-lewis-short', nota='s.v. Ulixes: genitivo Ulixī, com remissão a Aen. 2, 7', tipo='dominio_publico'),
    ],
    objetivos=[
        'Situar o livro II da Eneida na obra e reconhecer quem fala, a quem e em que momento.',
        'Ler e traduzir Eneida II, 1–20 com apoio das notas, identificando as construções já estudadas (ablativo absoluto, interrogativa indireta, subjuntivo potencial, gerúndio).',
        'Escandir um hexâmetro datílico, aplicando a elisão e a regra da posição, e localizar a cesura principal.',
        'Reconhecer marcas do estilo épico: perfeito em <i>-ēre</i>, genitivo em <i>-um</i>, hipérbato, enjambement, presente histórico e hendíadis.',
        'Comparar a sua tradução com o latim e justificar as escolhas de ordem e de tempo verbal.',
    ],
    secoes=[
        ('Virgílio, a Eneida e o livro II', f'''
<p>Públio Vergílio Marão (<i>Pūblius Vergilius Marō</i>, 70–19 a.C.) nasceu perto de Mântua e escreveu três obras: as <i>Bucólicas</i>, dez poemas pastoris; as <i>Geórgicas</i>, quatro livros sobre o trabalho do campo; e a <i>Eneida</i>, a epopeia em doze livros a que dedicou os últimos dez anos de vida. O poema conta como Eneias, príncipe troiano, sobrevive à destruição de Troia e, depois de anos de viagem, chega ao Lácio, onde seus descendentes fundarão Roma. Virgílio morreu antes de dar a última demão à obra (restam versos incompletos, como você notará se ler o poema inteiro), e ela foi publicada por ordem de Augusto.</p>
<p>No fim do livro I, Eneias, náufrago, é recebido em Cartago pela rainha Dido, que oferece um banquete aos troianos e lhe pede que conte desde o início a ruína da cidade e as suas viagens. Os livros II e III são essa narrativa, na primeira pessoa: o herói passa a ser narrador, como Ulisses na corte dos feácios na <i>Odisseia</i>, modelo que Virgílio tem em mente. O livro II, o da queda de Troia, é o mais lido nas escolas desde a Antiguidade: o cavalo de madeira, a serpente que mata Laocoonte, o fantasma de Heitor, o incêndio, a morte de Príamo e a fuga de Eneias com o pai às costas.</p>
<p>Os vinte versos deste capítulo são a abertura. Os dois primeiros ainda são do narrador do poema; a partir do v. 3 fala Eneias. Ele recusa e aceita ao mesmo tempo (a dor é "indizível", mas ele contará), e no v. 13 passa, sem transição, à história: os gregos, cansados de dez anos de guerra, constroem o cavalo e escondem nele os melhores guerreiros.</p>
{observacao('Sobre o texto', 'Seguimos a edição escolar de J. B. Greenough (Boston, Ginn, 1900, segundo a página da Perseus; o arquivo TEI da Perseus indica como fonte a impressão de 1881; Greenough morreu em 1901, e o texto está em domínio público), conferida no Perseus e, para as palavras, na The Latin Library; a pontuação é a de Greenough e os macrons foram acrescentados por este livro. No v. 12 escrevemos <i>refūgit</i>, perfeito, porque o metro exige ali uma sílaba longa (exercício 4). O texto da <i>Eneida</i> chega até nós por alguns códices antigos e por muitos medievais, que as edições críticas indicam por siglas; este capítulo não trata dessa tradição manuscrita.')}
'''),
        ('O texto e a tradução', f'''
<p>Leia o texto em voz alta duas vezes antes de olhar as notas: primeiro devagar, palavra por palavra; depois tentando respeitar as elisões (seção 4). Os números à esquerda são os dos versos, pelos quais o trecho é citado.</p>
{TEXTO}
<p>Tradução deste livro, linha a linha quanto ao sentido, sem pretensão poética:</p>
<p>[1–2] Calaram-se todos e, atentos, mantinham os rostos voltados para ele. Então o pai Eneias, do alto do seu leito, começou assim:</p>
<p>[3–8] "Mandas-me, rainha, renovar uma dor indizível: contar como os gregos derrubaram o poderio troiano e o reino digno de lágrimas, as coisas tristíssimas que eu mesmo vi e das quais fui parte importante. Quem, ao narrar tais coisas, seja dos mirmidões ou dos dólopes, seja soldado do duro Ulisses, se conteria das lágrimas?</p>
<p>[8–13] E já a noite úmida se precipita do céu, e as estrelas que se põem convidam ao sono. Mas, se é tão grande o teu desejo de conhecer as nossas desgraças e de ouvir em poucas palavras a provação final de Troia, embora a alma estremeça de lembrar e tenha recuado de dor, começarei.</p>
<p>[13–20] Alquebrados pela guerra e repelidos pelos fados, os chefes dos gregos, passados já tantos anos, constroem, com a arte divina de Palas, um cavalo do tamanho de um monte, e entretecem as suas costelas com tábuas de abeto; fingem que é uma oferenda votiva pelo regresso: essa é a notícia que corre. Ali, às escondidas, encerram no flanco escuro guerreiros escolhidos por sorteio, e enchem por dentro de soldados armados as cavernas enormes do ventre."</p>
{dica('<b>Por que o presente em "constroem", "fingem", "encerram"?</b> Virgílio narra o passado no presente (<i>aedificant, simulant, inclūdunt, complent</i>): é o presente histórico (Bennett § 259.3), que torna a cena visível. Em português o presente também funciona bem numa narrativa oral; a tradução o mantém.')}
'''),
        ('Vocabulário e notas', f'''
<p>A tabela segue a ordem dos versos. As palavras do vocabulário básico dos capítulos anteriores não estão glosadas; as formas difíceis estão explicadas onde aparecem.</p>
{tabela(['v.', 'Palavra ou expressão', 'Nota'], [
    ['1', 'conticuēre', 'perfeito de <i>conticēscō, -ere, conticuī</i>, "calar-se": 3ª pl. em <i>-ēre</i>, forma alternativa de <i>conticuērunt</i> (seção 5). Não é infinitivo.'],
    ['1', 'intentī … ōra tenēbant', '<i>intentus</i>, "atento"; <i>ōs, ōris</i> (n.), "boca, rosto". Literalmente "atentos, mantinham os rostos": isto é, olhavam fixamente para Eneias.'],
    ['2', 'torō … ab altō', '<i>torus, -ī</i> (m.), "leito" (o divã do banquete). As duas palavras emolduram o verso, com o sujeito no meio (hipérbato).'],
    ['2', 'ōrsus', 'particípio de <i>ordior, ordīrī, ōrsus sum</i> (depoente), "começar"; subentenda <i>est</i>: "começou".'],
    ['3', 'īnfandum … dolōrem', '<i>īnfandus</i>, "indizível, que não se deve dizer" (<i>in-</i> + gerundivo de <i>for, fārī</i>, "falar"). Adjetivo no início do verso e nome no fim: a dor ocupa a linha toda.'],
    ['3', 'iubēs renovāre', '<i>iubeō</i> + infinitivo, "mandas renovar". <i>Rēgīna</i> é vocativo: Dido.'],
    ['4–5', 'Trōiānās ut opēs … ēruerint Danaī', '<i>ut</i> aqui é "como", e introduz uma interrogativa indireta (subjuntivo perfeito <i>ēruerint</i>, de <i>ēruō</i>, "arrancar, derrubar") que explica <i>dolōrem</i>. Note o <i>ut</i> deslocado para depois de <i>Trōiānās</i>. <i>Opēs</i>: "poder, riqueza". <i>Danaī</i>: os gregos.'],
    ['5–6', 'quaeque … miserrima vīdī / et quōrum pars magna fuī', 'relativas com antecedente subentendido ("e as coisas tristíssimas que…"); <i>quōrum</i>, genitivo partitivo com <i>pars</i>: "das quais fui grande parte".'],
    ['6', 'tālia fandō', '<i>fandō</i>, gerúndio de <i>for, fārī</i>, no ablativo, com objeto direto <i>tālia</i>: "ao contar tais coisas" (Bennett § 338.4.a e 338.5).'],
    ['7', 'Myrmidonum Dolopumve', 'genitivos plurais (3ª declinação) partitivos de <i>quis</i>: "quem dos mirmidões ou dos dólopes" (tropas de Aquiles). <i>-ve</i>, "ou".'],
    ['7', 'dūrī … Ulixī', 'genitivo de <i>Ulixēs</i> (Ulisses), na forma <i>Ulixī</i> (Lewis &amp; Short registra esta passagem); <i>dūrus</i>, "duro, implacável".'],
    ['6–8', 'quis … temperet ā lacrimīs?', '<i>temperō ā</i> + ablativo, "abster-se de". Subjuntivo potencial (Bennett § 280.2): "quem se conteria?", isto é, se contasse estas coisas. A resposta implícita é "ninguém": pergunta retórica.'],
    ['8–9', 'nox ūmida caelō praecipitat', '<i>praecipitō</i> aqui é intransitivo, "lançar-se, descer depressa"; <i>caelō</i>, ablativo: "do céu". Já é tarde da noite.'],
    ['9', 'suādent … cadentia sīdera somnōs', '<i>suādeō</i>, "aconselhar, convidar a"; <i>cadentia</i>, particípio presente de <i>cadō</i>: as estrelas "que caem", isto é, que se põem. <i>Somnōs</i>, plural poético.'],
    ['10', 'sī tantus amor (est) cāsūs cognōscere nostrōs', 'subentenda <i>est</i>. <i>Amor</i> + infinitivo, "desejo de conhecer", construção poética. <i>Cāsūs</i>: acusativo plural de <i>cāsus, -ūs</i>, "queda, desgraça".'],
    ['11', 'suprēmum … labōrem', '"a provação final", objeto de <i>audīre</i>.'],
    ['12', 'meminisse horret', '<i>horreō</i>, "arrepiar-se, ter horror", + infinitivo; <i>meminī</i>, "lembrar-se", verbo defectivo: só tem formas de perfeito, com sentido de presente.'],
    ['12', 'lūctūque refūgit', '<i>lūctus, -ūs</i>, "luto, dor"; ablativo de causa. <i>Refūgit</i> é perfeito de <i>refugiō</i> (o presente seria <i>refugit</i>, com <i>u</i> breve): o metro garante a vogal longa, porque a sílaba ocupa o início do sexto pé. "Recuou", e o efeito dura: a alma recuou e ainda recua.'],
    ['13', 'incipiam', 'futuro de <i>incipiō</i>: "começarei". O verbo fica isolado no início do verso, depois de três versos de condição e concessão (enjambement).'],
    ['13', 'frāctī … repulsī', 'particípios perfeitos de <i>frangō</i> ("quebrar") e <i>repellō</i> ("repelir"), concordando com <i>ductōrēs</i>: particípio conjunto. <i>Bellō</i> e <i>fātīs</i>, ablativos de causa ou de meio.'],
    ['14', 'ductōrēs Danaum', '<i>ductor, -ōris</i>, "chefe"; <i>Danaum</i> = <i>Danaōrum</i>, genitivo plural em <i>-um</i> (seção 5).'],
    ['14', 'tot iam lābentibus annīs', 'ablativo absoluto com particípio presente do depoente <i>lābor</i>, "escorregar, passar": "passando já tantos anos".'],
    ['15', 'īnstar montis', '<i>īnstar</i>, substantivo neutro indeclinável, "tamanho, equivalente", + genitivo: "do tamanho de um monte".'],
    ['15', 'dīvīnā Palladis arte', 'ablativo de meio com genitivo encaixado: "pela arte divina de Palas" (Atena, a Minerva dos romanos).'],
    ['16', 'sectāque intexunt abiete costās', '<i>intexō</i>, "entretecer"; <i>costa, -ae</i>, "costela"; <i>abiēs, abietis</i> (f.), "abeto", ablativo de meio; <i>secta</i>, "cortada". No metro, o <i>i</i> de <i>abiete</i> vale consoante (seção 4).'],
    ['17', 'vōtum prō reditū simulant', '<i>vōtum</i>, "oferenda prometida aos deuses"; <i>reditus, -ūs</i>, "regresso"; <i>simulō</i>, "fingir": fingem que o cavalo é um ex-voto pela volta. <i>Vagātur</i>: depoente <i>vagor</i>, "espalhar-se".'],
    ['18', 'dēlēcta virum … corpora', '<i>virum</i> = <i>virōrum</i>. "Corpos escolhidos de homens" é perífrase épica para "homens escolhidos".'],
    ['18', 'sortītī', 'particípio perfeito do depoente <i>sortior</i>, "tirar à sorte", com sentido ativo: "tendo-os sorteado".'],
    ['19', 'caecō laterī', '<i>caecus</i>, "cego, escuro"; <i>latus, -eris</i> (n.), "lado, flanco". Dativo com o composto <i>inclūdō</i>, onde a prosa diria <i>in latere</i>.'],
    ['19–20', 'cavernās ingentīs uterumque', '<i>ingentīs</i> = <i>ingentēs</i>, acusativo plural em <i>-īs</i> (seção 5); <i>uterus, -ī</i>, "ventre". "As cavernas enormes e o ventre" = as cavernas enormes do ventre: hendíadis (Bennett § 374.4).'],
    ['20', 'armātō mīlite complent', '<i>mīles</i> no singular coletivo, "soldados"; ablativo com o verbo de encher <i>compleō</i>.'],
], 'Notas a Eneida II, 1–20', latim_cols=(1,))}
'''),
        ('O hexâmetro: escandir com elisão', f'''
<p>O capítulo 40 apresentou o hexâmetro datílico e o capítulo 46 o pôs em prática com Ovídio. Recapitulando o essencial: o verso tem seis pés; os quatro primeiros podem ser dáctilos (– ˘ ˘) ou espondeus (– –), o quinto é quase sempre dáctilo e o sexto tem duas sílabas, a última das quais pode ser breve ou longa (Bennett § 368.1; Kennedy § 477). Uma sílaba é longa se tem vogal longa ou ditongo, ou se a vogal é seguida de duas consoantes, mesmo que a segunda esteja na palavra seguinte.</p>
<p>A novidade aqui é a <b>elisão</b>. Quando uma palavra termina em vogal, ditongo ou vogal + <i>m</i> e a seguinte começa por vogal ou <i>h</i>, a sílaba final da primeira some na leitura métrica (Bennett § 366.7). As gramáticas dão nomes diferentes ao fenômeno, e vale a pena conhecê-los para não se confundir ao consultá-las:</p>
{comparacao('Os nomes da elisão nas gramáticas', ['Exemplo', 'Bennett', 'Kennedy', 'Ravizza'], [
    ['Conticuēr<b>e</b> omnēs (v. 1)', 'elisão', 'elisão ou sinalefa', 'sinalefa'],
    ['quamqu<b>am</b> animus (v. 12)', 'elisão', 'ectlipse (vogal + <i>m</i>)', 'elisão'],
    ['meminiss<b>e</b> horret (v. 12)', 'elisão (antes de <i>h</i>)', 'elisão', 'sinalefa'],
])}
<p>A gramática do Pe. Ravizza (n. 535) usa justamente dois versos deste trecho como exemplos: <i>Conticuēre omnēs</i> para a sinalefa e <i>suprēmum audīre labōrem</i> (v. 11) para a elisão em <i>-m</i>. Na leitura em voz alta, a sílaba elidida pode ser pronunciada de leve ou cair; na escansão, ela simplesmente não conta.</p>
<h3>Verso 1, com duas elisões</h3>
{tabela(['Pé', '1', '2', '3', '4', '5', '6'], [
    ['Sílabas', 'Con-ti-cu', 'ē-r(e) om', 'nēs in', 'ten-tī', 'qu(e) ō-ra te', 'nē-bant'],
    ['Quantidade', '– ˘ ˘', '– –', '– –', '– –', '– ˘ ˘', '– –'],
    ['Pé', 'dáctilo', 'espondeu', 'espondeu', 'espondeu', 'dáctilo', 'espondeu'],
], 'Conticuēre omnēs, intentīque ōra tenēbant (v. 1)')}
<p>Repare por que <i>Con-</i>, <i>-nēs</i>, <i>in-</i> e <i>-ten-</i> são longas: <i>Con-</i> e <i>in-</i> por posição (vogal breve + <i>n</i> + consoante), <i>-nēs</i> por natureza. Os três espondeus seguidos tornam o verso lento e grave: é o silêncio da sala antes da narrativa.</p>
<h3>Verso 3, sem elisão</h3>
{tabela(['Pé', '1', '2', '3', '4', '5', '6'], [
    ['Sílabas', 'Īn-fan', 'dum rē', 'gī-na iu', 'bēs re-no', 'vā-re do', 'lō-rem'],
    ['Quantidade', '– –', '– –', '– ˘ ˘', '– ˘ ˘', '– ˘ ˘', '– –'],
], 'Īnfandum, rēgīna, iubēs renovāre dolōrem (v. 3)')}
<p>O <i>i</i> de <i>iubēs</i> é consoante (soa como o <i>i</i> de "iate"), por isso <i>-na</i> continua breve: está diante de uma só consoante.</p>
<h3>Verso 5, com uma elisão</h3>
{tabela(['Pé', '1', '2', '3', '4', '5', '6'], [
    ['Sílabas', 'ē-ru-e', 'rint Da-na', 'ī quae', 'qu(e) ip-se mi', 'ser-ri-ma', 'vī-dī'],
    ['Quantidade', '– ˘ ˘', '– ˘ ˘', '– –', '– ˘ ˘', '– ˘ ˘', '– –'],
], 'ēruerint Danaī; quaeque ipse miserrima vīdī (v. 5)')}
<h3>A cesura</h3>
<p>Na maioria dos hexâmetros há um corte de palavra logo depois da primeira sílaba do terceiro pé, a cesura principal: <i>Īnfandum, rēgīna, || iubēs</i>; <i>ēruerint Danaī; || quaeque</i>. O v. 2 é o exemplo que Bennett (§ 368.3.b) dá do tipo menos comum, com cortes no segundo e no quarto pés: <i>Inde torō || pater Aenēās || sīc ōrsus ab altō</i>. Observe que Bennett cita o verso com <i>est</i> no fim (<i>ab altō est</i>), palavra que nenhuma das edições conferidas para este capítulo traz (Greenough; O. Ribbeck, Leipzig, Teubner, 1861; J. Conington, reimpressão de Nova York, 1895; H. R. Fairclough, Loeb, 1916; The Latin Library): seguimos o texto delas, e a forma de Bennett fica registrada como variante; a diferença não muda a escansão, porque <i>altō est</i> se pronuncia <i>altōst</i>, com a mesma última sílaba longa.</p>
{observacao('Abiete: quando o i vira consoante', 'No v. 16, <i>abiete</i> tem, no dicionário, quatro sílabas breves (<i>a-bi-e-te</i>), sequência impossível no hexâmetro. Virgílio pronuncia o <i>i</i> como consoante, <i>ab-je-te</i>: a primeira sílaba fica longa por posição e a palavra forma um dáctilo. Bennett (§ 367.4) dá exatamente este exemplo, <i>abjete</i> por <i>abiete</i>.')}
'''),
        ('O estilo épico: o que muda em relação à prosa', f'''
<p>Quase tudo no trecho é gramática que você já conhece. O que dá estranheza é um conjunto de hábitos da poesia épica, que convém reconhecer de uma vez.</p>
<h3>Formas próprias da poesia</h3>
{tabela(['Forma', 'Equivale a', 'Explicação'], [
    ['<i>conticu<b>ēre</b></i> (v. 1)', '<i>conticuērunt</i>', 'como você viu em Ovídio (capítulo 46), a 3ª pessoa do plural do perfeito tem duas terminações, <i>-ērunt</i> e <i>-ēre</i> (Bennett § 101; A&amp;G § 163, nota 3). A forma em <i>-ēre</i> é frequente nos poetas e nos historiadores. Não confunda com o infinitivo presente da 2ª conjugação (<i>monēre</i>): aqui o tema é o do perfeito, <i>conticu-</i>.'],
    ['<i>Dana<b>um</b></i> (v. 14), <i>vir<b>um</b></i> (v. 18)', '<i>Danaōrum</i>, <i>virōrum</i>', 'genitivo plural da 2ª declinação em <i>-um</i>, forma antiga conservada em certas palavras e muito usada na poesia (Bennett § 25.6.c; o mesmo com <i>deum</i> por <i>deōrum</i>, § 25.4). Não é acusativo singular: o contexto pede "dos gregos", "de homens".'],
    ['<i>ingent<b>īs</b></i> (v. 20)', '<i>ingentēs</i>', 'acusativo plural em <i>-īs</i> dos temas em <i>-i</i> e dos adjetivos da 3ª declinação (Bennett § 67.3.a; capítulo 10).'],
    ['<i>Ulix<b>ī</b></i> (v. 7)', '<i>Ulixis</i>', 'genitivo de um nome de origem grega, em forma contraída; Lewis &amp; Short a registra nesta passagem, em outros versos de Virgílio e também em Cícero.'],
], 'Formas que a prosa usaria de outro modo')}
<h3>A ordem das palavras</h3>
<p>A poesia latina separa o que concorda, e o faz de propósito. O <b>hipérbato</b> (separação de palavras que formam um grupo; Bennett § 350.11.a; capítulo 40) cria molduras: <i>torō … ab altō</i> (v. 2), <i>īnfandum … dolōrem</i> (v. 3), <i>dīvīnā Palladis arte</i> (v. 15, adjetivo e nome em volta do genitivo), <i>caecō laterī</i> diante de <i>cavernās ingentīs</i>. Até a conjunção se desloca: <i>Trōiānās ut opēs</i> (v. 4) põe <i>ut</i> em segunda posição. Para ler, aplique o que você aprendeu no capítulo 39: anote o caso e o gênero de cada adjetivo e espere o nome com que ele concorda.</p>
<p>O <b>enjambement</b> (a frase continua no verso seguinte) também conta. A condição e a concessão dos vv. 10–12 terminam com <i>incipiam</i>, isolado no início do v. 13 e seguido de pausa forte: a palavra "começarei" cai sozinha, depois de toda a hesitação.</p>
<h3>O registro épico</h3>
<p>Três traços dão o tom elevado. As <b>perífrases</b>: <i>dēlēcta virum corpora</i>, "corpos escolhidos de homens", em vez de "homens escolhidos". A <b>hendíadis</b>, que exprime uma ideia por dois nomes coordenados: <i>cavernās … uterumque</i>, "as cavernas e o ventre" = "as cavernas do ventre" (Bennett § 374.4). E o <b>singular coletivo</b>: <i>armātō mīlite</i>, "com soldado armado", isto é, com soldados. A isso se somam o presente histórico (vv. 16–20) e o ablativo absoluto, que você conhece da prosa e que a poesia usa com a mesma função: <i>tot iam lābentibus annīs</i>, "passando já tantos anos" (capítulo 30; Bennett § 227).</p>
<h3>A sintaxe que já é sua</h3>
<p>O trecho exercita construções da parte III: a interrogativa indireta com <i>ut</i>, "como" (<i>Trōiānās ut opēs … ēruerint</i>, capítulo 35; Bennett § 300), o subjuntivo potencial numa pergunta retórica (<i>quis … temperet</i>, capítulo 32; Bennett § 280.2; A&amp;G §§ 445–447), o gerúndio no ablativo com objeto (<i>tālia fandō</i>, capítulo 31), a condicional real (<i>sī tantus amor …, incipiam</i>, capítulo 36) e a concessiva com <i>quamquam</i> e indicativo (<i>quamquam animus … horret</i>, capítulo 37).</p>
'''),
        ('Análise de um período: os vv. 13–16', f'''
<p>A primeira frase da narrativa propriamente dita é um bom exemplo do período poético: sujeito com dois particípios, um ablativo absoluto intercalado, o objeto envolvido pelos seus determinantes e o verbo guardado para o início do verso seguinte.</p>
{exemplos([('Frāctī bellō fātīsque repulsī / ductōrēs Danaum, tot iam lābentibus annīs, / īnstar montis equum dīvīnā Palladis arte / aedificant.', 'Alquebrados pela guerra e repelidos pelos fados, os chefes dos gregos, passados já tantos anos, constroem com a arte divina de Palas um cavalo do tamanho de um monte. (Eneida II, 13–16)')])}
{analise('Eneida II, 13–16, palavra a palavra', [
    ('Frāctī', 'frangō, -ere, frēgī, frāctum, quebrar', 'particípio perfeito passivo, nom. pl. masc.', 'particípio conjunto, concorda com <i>ductōrēs</i>'),
    ('bellō', 'bellum, -ī (n.), guerra', 'ablativo singular', 'causa/meio de <i>frāctī</i>'),
    ('fātīsque', 'fātum, -ī (n.), destino + -que', 'ablativo plural', 'causa/meio de <i>repulsī</i>'),
    ('repulsī', 'repellō, -ere, reppulī, repulsum, repelir', 'particípio perfeito passivo, nom. pl. masc.', 'particípio conjunto, concorda com <i>ductōrēs</i>'),
    ('ductōrēs', 'ductor, -ōris (m.), chefe', 'nominativo plural', 'sujeito de <i>aedificant</i>'),
    ('Danaum', 'Danaī, -ōrum (m. pl.), gregos', 'genitivo plural em <i>-um</i>', 'complemento de <i>ductōrēs</i>'),
    ('tot … annīs', 'tot (indeclinável), tantos; annus, -ī (m.), ano', 'ablativo plural', 'ablativo absoluto com <i>lābentibus</i>'),
    ('iam', 'advérbio', 'invariável', '"já"'),
    ('lābentibus', 'lābor, lābī, lāpsus sum, deslizar, passar', 'particípio presente (depoente), abl. pl.', 'predicado do ablativo absoluto'),
    ('īnstar', 'īnstar (n., indeclinável), tamanho', 'acusativo (aposto a <i>equum</i>)', '"do tamanho de"'),
    ('montis', 'mōns, montis (m.), monte', 'genitivo singular', 'complemento de <i>īnstar</i>'),
    ('equum', 'equus, -ī (m.), cavalo', 'acusativo singular', 'objeto direto de <i>aedificant</i>'),
    ('dīvīnā … arte', 'dīvīnus, -a, -um; ars, artis (f.), arte', 'ablativo singular', 'ablativo de meio'),
    ('Palladis', 'Pallas, -adis (f.), Palas', 'genitivo singular', 'complemento de <i>arte</i>'),
    ('aedificant', 'aedificō, -āre, construir', 'presente do indicativo, 3ª pl. (presente histórico)', 'verbo principal'),
])}
{diagrama_frase([('ductōrēs Danaum', 'sujeito · os chefes gregos'), ('frāctī … repulsī', 'particípios · alquebrados, repelidos'), ('tot … annīs', 'abl. absoluto · passados tantos anos'), ('equum', 'objeto · o cavalo'), ('aedificant', 'verbo · constroem')], 'O esqueleto do período: <i>ductōrēs Danaum … equum aedificant</i>; o resto pendura-se nessas três palavras.')}
<p>A estratégia de leitura é a do capítulo 39. Os particípios no nominativo plural (<i>frāctī, repulsī</i>) anunciam um sujeito masculino plural, que chega no verso seguinte (<i>ductōrēs</i>). O ablativo absoluto se fecha sozinho (<i>tot … lābentibus annīs</i>). No v. 15, <i>equum</i> é o único acusativo que pode ser objeto, e <i>īnstar montis</i> se prende a ele; o verbo só chega no v. 16. Repare também na diferença entre os dois tipos de particípio: <i>frāctī</i> e <i>repulsī</i> concordam com o sujeito (particípio conjunto), enquanto <i>lābentibus</i> concorda com <i>annīs</i>, que não tem papel nenhum na oração principal (ablativo absoluto).</p>
'''),
    ],
    erros_comuns=[
        ('Ler <i>conticuēre</i> como infinitivo.', 'O tema <i>conticu-</i> é o do perfeito (<i>conticuī</i>), e o verso precisa de um verbo finito para <i>omnēs</i>. Toda forma em <i>-ēre</i> sobre tema de perfeito é 3ª pessoa do plural: <i>conticuēre</i> = <i>conticuērunt</i>, "calaram-se".'),
        ('Tomar <i>Danaum</i> ou <i>virum</i> como acusativo singular.', 'Na poesia, <i>-um</i> pode ser genitivo plural (= <i>-ōrum</i>). Teste as duas leituras: "os chefes os gregos" não faz sentido; "os chefes <b>dos gregos</b>" faz. O mesmo com <i>dēlēcta virum corpora</i>, "corpos escolhidos <b>de homens</b>".'),
        ('Traduzir o <i>ut</i> do v. 4 por "para que" ou "de modo que".', 'Depois de <i>renovāre dolōrem</i>, a oração com <i>ut</i> e subjuntivo explica qual é a dor: "como os gregos derrubaram…". É <i>ut</i> interrogativo, "como", numa interrogativa indireta (capítulo 35), não final nem consecutivo.'),
        ('Contar as sílabas elididas na escansão.', 'Em <i>Conticuēre omnēs</i>, o <i>-re</i> não forma sílaba: o verso só tem seis pés se você o eliminar. Antes de marcar longas e breves, risque todas as vogais finais (e as terminações em <i>-m</i>) que vêm antes de vogal ou <i>h</i>.'),
        ('Ler <i>a-bi-e-te</i> com quatro sílabas.', 'Quatro breves seguidas não cabem no hexâmetro. Quando a escansão "não fecha", procure um <i>i</i> ou <i>u</i> que possa valer como consoante (Bennett § 367.4) ou duas vogais que se fundem numa sílaba (sinizese).'),
        ('Tratar <i>nox</i> como objeto e <i>sīdera</i> como sujeito de <i>praecipitat</i>.', '<i>Praecipitat</i> está no singular e é intransitivo: o sujeito é <i>nox ūmida</i>, e <i>caelō</i> diz de onde ela desce. <i>Cadentia sīdera</i> é sujeito do outro verbo, <i>suādent</i>, que está no plural.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · O primeiro período de Eneias (vv. 3–6)',
            'Leia <i lang="la">Īnfandum, rēgīna, iubēs renovāre dolōrem, Trōiānās ut opēs et lāmentābile rēgnum ēruerint Danaī; quaeque ipse miserrima vīdī, et quōrum pars magna fuī.</i> Use as notas da seção 3.', [
            ('Qual é o verbo principal e quem é o sujeito?', '<i>Iubēs</i>, 2ª pessoa do singular: o sujeito é "tu", a rainha, chamada no vocativo <i>rēgīna</i>. O complemento é o infinitivo <i>renovāre</i>, que tem por objeto <i>dolōrem</i>.'),
            ('Com que palavra concorda <i>īnfandum</i>?', 'Com <i>dolōrem</i>, no fim do verso: acusativo singular masculino. O adjetivo abre o verso e o nome o fecha, e a palavra "indizível" ganha destaque por vir antes de tudo.'),
            ('O que é a oração com <i>ut</i>?', 'Uma interrogativa indireta com subjuntivo perfeito (<i>ēruerint</i>, sequência primária depois do presente <i>iubēs</i>): "como os gregos derrubaram". Ela explica em que consiste a dor. <i>Danaī</i> é o sujeito; <i>opēs</i> e <i>rēgnum</i> são os objetos.'),
            ('E as relativas <i>quaeque … vīdī et quōrum … fuī</i>?', 'O antecedente está subentendido ("e [as coisas] tristíssimas que eu mesmo vi"). <i>Quae</i> é neutro plural, objeto de <i>vīdī</i>; <i>miserrima</i> concorda com ele. <i>Quōrum</i> é genitivo partitivo de <i>pars</i>: "das quais fui parte importante".'),
            ('Monte a tradução.', '"Mandas-me, rainha, renovar uma dor indizível: [contar] como os gregos derrubaram o poderio troiano e o reino digno de lágrimas, e as coisas tristíssimas que eu mesmo vi e das quais fui parte importante."'),
        ]),
        pratica_guiada('Prática guiada 2 · Escandir o v. 16',
            'Escanda <i lang="la">aedificant, sectāque intexunt abiete costās</i>.', [
            ('Há elisão?', 'Sim: <i>sectāqu(e) intexunt</i>, porque <i>-que</i> termina em vogal e <i>intexunt</i> começa por vogal.'),
            ('Marque as sílabas certamente longas.', '<i>ae-</i> (ditongo), <i>-cant</i> e <i>sec-</i> (vogal + duas consoantes), <i>-tā-</i> (vogal longa), <i>-quin-</i> (depois da elisão, <i>qu(e) in-</i> forma uma sílaba fechada por <i>n</i> + <i>t</i>), <i>-tex-</i> (o <i>x</i> vale duas consoantes), <i>-unt</i>, <i>cos-</i>, <i>-tās</i>.'),
            ('Os seis pés fecham?', '<i>ae-di-fi | cant sec | tā quin | tex-unt | a-bi-e-te? | cos-tās</i>: com <i>abiete</i> em quatro breves sobram sílabas e o quinto pé não é dáctilo. Lendo <i>ab-je-te</i>, fica <i>ab-je-te</i> = – ˘ ˘.'),
            ('Escreva o esquema final.', '<i>ae-di-fi | cant sec | tā-qu(e) in | tex-unt | ab-je-te | cos-tās</i>: – ˘ ˘ | – – | – – | – – | – ˘ ˘ | – –.'),
        ], 'Os três espondeus do meio desaceleram o verso enquanto os gregos trabalham na madeira; o dáctilo de <i>abiete</i> volta ao ritmo normal antes do fim.'),
    ],
    exercicios=[
        exercicio('Exercício 1 · Compreensão', 'Responda em português, com base no texto latino.', [
            ('Quem fala nos vv. 1–2, e quem fala a partir do v. 3?', 'Nos vv. 1–2 fala o narrador do poema, que descreve o silêncio e apresenta Eneias (<i>pater Aenēās sīc ōrsus</i>). A partir do v. 3 fala Eneias, que se dirige a Dido (<i>rēgīna</i>, vocativo).'),
            ('Que dois argumentos Eneias dá para hesitar antes de contar?', 'A dor da lembrança (<i>īnfandum dolōrem</i>; <i>animus meminisse horret</i>) e a hora avançada (<i>nox ūmida caelō praecipitat, suādentque cadentia sīdera somnōs</i>). Mesmo assim, ele começa (<i>incipiam</i>).'),
            ('Por que Eneias menciona mirmidões, dólopes e Ulisses?', 'São os inimigos mais duros de Troia (as tropas de Aquiles e o astuto Ulisses). Se até eles chorariam ao ouvir a história, o sofrimento é imenso: é um argumento <i>a fortiori</i>, em forma de pergunta retórica.'),
            ('Que pretexto os gregos espalham sobre o cavalo?', 'Que é uma oferenda votiva pelo seu regresso (<i>vōtum prō reditū simulant</i>); <i>simulant</i>, "fingem", mostra que é mentira.'),
        ]),
        exercicio('Exercício 2 · Morfologia', 'Identifique a forma e dê o verbete de dicionário.', [
            ('<i>conticuēre</i>', 'Perfeito do indicativo ativo, 3ª pl., forma em <i>-ēre</i> = <i>conticuērunt</i>; <i>conticēscō, -ere, conticuī</i>, "calar-se".'),
            ('<i>ēruerint</i>', 'Perfeito do subjuntivo ativo, 3ª pl.; <i>ēruō, -ere, ēruī, ērutum</i>, "arrancar, derrubar". O subjuntivo vem da interrogativa indireta.'),
            ('<i>fandō</i>', 'Gerúndio, ablativo; <i>for, fārī, fātus sum</i> (depoente), "falar, dizer".'),
            ('<i>cāsūs</i> (v. 10)', 'Acusativo plural da 4ª declinação; <i>cāsus, -ūs</i> (m.), "queda, desgraça". Concorda com <i>nostrōs</i>.'),
            ('<i>sortītī</i>', 'Particípio perfeito, nom. pl. masc.; <i>sortior, -īrī, sortītus sum</i> (depoente), "tirar à sorte". Sentido ativo: "tendo sorteado".'),
            ('<i>vagātur</i>', 'Presente do indicativo, 3ª sing., de um depoente: <i>vagor, -ārī, vagātus sum</i>, "vaguear, espalhar-se". Forma passiva, sentido ativo (capítulo 25).'),
        ]),
        exercicio('Exercício 3 · Sintaxe', 'Explique a construção destacada.', [
            ('<i>Quis … <b>temperet</b> ā lacrimīs?</i>', 'Subjuntivo potencial numa pergunta retórica: "quem se conteria?", com a condição implícita "se contasse estas coisas" (Bennett § 280.2). A resposta esperada é "ninguém".'),
            ('<i><b>tot iam lābentibus annīs</b></i>', 'Ablativo absoluto com particípio presente (de depoente): a circunstância de tempo, simultânea, "passando já tantos anos". <i>Annīs</i> não tem função na oração principal.'),
            ('<i>et iam nox ūmida <b>caelō</b> praecipitat</i>', 'Ablativo de lugar de onde (separação), sem preposição, como é comum na poesia: "desce do céu".'),
            ('<i><b>īnstar</b> montis equum</i>', '<i>Īnstar</i> é um substantivo indeclinável, "equivalente, tamanho", aposto a <i>equum</i>, com o genitivo <i>montis</i>: "um cavalo do tamanho de um monte".'),
            ('<i>uterumque <b>armātō mīlite</b> complent</i>', 'Ablativo com verbo de encher (<i>compleō</i>), da família do ablativo de meio: "enchem de soldados armados". <i>Mīlite</i> é singular coletivo.'),
        ]),
        exercicio('Exercício 4 · Escansão', 'Escanda os versos, marcando elisões, longas (–) e breves (˘).', [
            ('v. 13: <i>incipiam. Frāctī bellō fātīsque repulsī</i>', '<i>in-ci-pi | am frāc | tī bel | lō fā | tīs-que re | pul-sī</i>: – ˘ ˘ | – – | – – | – – | – ˘ ˘ | – –. Não há elisão: <i>incipiam</i> termina em <i>-m</i>, mas a palavra seguinte começa por consoante, e <i>-am</i> fica longa por posição.'),
            ('v. 17: <i>vōtum prō reditū simulant; ea fāma vagātur</i>', '<i>vō-tum | prō re-di | tū si-mu | lant e-a | fā-ma va | gā-tur</i>: – – | – ˘ ˘ | – ˘ ˘ | – ˘ ˘ | – ˘ ˘ | – ˘. Quatro dáctilos seguidos: o boato corre depressa.'),
            ('v. 12: <i>quamquam animus meminisse horret, lūctūque refūgit</i>', 'Duas elisões: <i>quamqu(am) animus</i> (vogal + <i>m</i>) e <i>meminiss(e) horret</i> (antes de <i>h</i>). <i>quam-qua-ni | mus me-mi | nis-s(e) hor | ret lūc | tū-que re | fū-git</i>: – ˘ ˘ | – ˘ ˘ | – – | – – | – ˘ ˘ | – ˘. A última sílaba é indiferente (Bennett § 366.10), mas a primeira do sexto pé tem de ser longa (§ 368.1): por isso a forma é o perfeito <i>refūgit</i>, e não o presente <i>refugit</i>, de <i>u</i> breve. A escansão serve também para decidir uma forma.'),
            ('v. 20: <i>ingentīs uterumque armātō mīlite complent</i>', '<i>in-gen | tīs u-te | rum-qu(e) ar | mā-tō | mī-li-te | com-plent</i>: – – | – ˘ ˘ | – – | – – | – ˘ ˘ | – –. Uma elisão: <i>uterumqu(e) armātō</i>.'),
        ]),
        exercicio('Exercício 5 · Tradução e prosa', 'Reescreva em ordem de prosa e traduza.', [
            ('<i>Inde torō pater Aenēās sīc ōrsus ab altō</i>', 'Prosa: <i>Inde pater Aenēās ab altō torō sīc ōrsus est.</i> "Então o pai Eneias, do alto leito, começou assim."'),
            ('<i>Hūc dēlēcta virum sortītī corpora fūrtim inclūdunt caecō laterī</i>', 'Prosa: <i>Hūc virōrum corpora dēlēcta sortītī fūrtim in caecō latere inclūdunt.</i> "Ali, depois de os sortear, encerram às escondidas no flanco escuro homens escolhidos."'),
            ('<i>sed sī tantus amor cāsūs cognōscere nostrōs …, incipiam</i>', 'Prosa: <i>Sed sī tantus tibi amor est cāsūs nostrōs cognōscere, incipiam.</i> "Mas, se tens tanto desejo de conhecer as nossas desgraças, começarei." Condicional real (capítulo 36): indicativo nas duas orações.'),
        ]),
    ],
    leituras=['maro-aeneis-selecoes', 'maro-aeneis-texto-integral', 'maro-aeneis-iv-1-299-dido', 'naso-metamorphoses-texto-integral', 'short-a-latin-dictionary-lewis-short'],
    leituras_nota='Continue o livro II nas <i>Seleções</i> do DCC, que trazem macrons, vocabulário e notas verso a verso: depois deste trecho vêm Laocoonte (vv. 40–56) e o fantasma de Heitor (vv. 268–297). Quando quiser ler sem apoio, use o texto integral de Greenough no Perseus, com análise morfológica ao clique e o Lewis &amp; Short ao lado. O livro IV (Dido), na edição comentada de Gildenhard, é a continuação natural; e Ovídio (capítulo 46) serve de contraste: o mesmo metro, um ritmo muito mais leve.',
)
