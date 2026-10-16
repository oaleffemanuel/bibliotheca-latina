from conteudo.util import (tabela, comparacao, exemplos, observacao, dica, diagrama_frase, exercicio,
                           referencia, pratica_guiada, analise)

# Notação de escansão usada no capítulo: – sílaba longa · ˘ sílaba breve · × sílaba final indiferente (anceps).
# As tabelas de escansão têm um pé (ou um segmento) por linha, para caber na largura de um celular.

def _escansao(legenda, pes):
    """pes: lista de (texto do pé, sílabas, esquema, tipo)."""
    return tabela(['Pé', 'Texto', 'Sílabas', 'Esquema', 'Tipo'],
                  [[str(i), t, s, f'<b>{q}</b>', tp] for i, (t, s, q, tp) in enumerate(pes, 1)],
                  legenda, latim_cols=(1, 2))

def _segmentos(legenda, segs):
    """Para versos líricos: lista de (texto, sílabas, esquema)."""
    return tabela(['Segmento', 'Sílabas', 'Esquema'], [[t, s, f'<b>{q}</b>'] for t, s, q in segs], legenda, latim_cols=(0, 1))

_AEN_1_1 = _escansao('Eneida 1.1 escandida (cesura depois de canō)', [
    ('Arma vi-', 'ar · ma · vi', '– ˘ ˘', 'dáctilo'),
    ('-rumque ca-', 'rum · que · ca', '– ˘ ˘', 'dáctilo'),
    ('-nō ‖ Trō-', 'nō · Trō', '– –', 'espondeu'),
    ('-iae quī', 'iae · quī', '– –', 'espondeu'),
    ('prīmus ab', 'prī · mus · ab', '– ˘ ˘', 'dáctilo'),
    ('ōrīs', 'ō · rīs', '– ×', 'espondeu/troqueu'),
])

_AEN_1_33 = _escansao('Eneida 1.33 escandida (cesura depois de erat)', [
    ('Tantae', 'tan · tae', '– –', 'espondeu'),
    ('mōlis e-', 'mō · lis · e', '– ˘ ˘', 'dáctilo'),
    ('-rat ‖ Rō-', 'rat · Rō', '– –', 'espondeu'),
    ('-mānam', 'mā · nam', '– –', 'espondeu'),
    ('condere', 'con · de · re', '– ˘ ˘', 'dáctilo'),
    ('gentem', 'gen · tem', '– ×', 'espondeu'),
])

_TRIST_HEX = _escansao('Tristia 1.9.5: o hexâmetro do dístico', [
    ('Dōnec e-', 'dō · nec · e', '– ˘ ˘', 'dáctilo'),
    ('-ris sos-', 'ris · sos', '– –', 'espondeu'),
    ('-pes ‖ mul-', 'pes · mul', '– –', 'espondeu'),
    ('-tōs nume-', 'tōs · nu · me', '– ˘ ˘', 'dáctilo'),
    ('-rābis a-', 'rā · bis · a', '– ˘ ˘', 'dáctilo'),
    ('-mīcōs', 'mī · cōs', '– ×', 'espondeu'),
])

_TRIST_PENT = tabela(['Parte', 'Texto', 'Sílabas', 'Esquema'], [
    ['1ª metade, pé 1', 'tempora', 'tem · po · ra', '<b>– ˘ ˘</b>'],
    ['1ª metade, pé 2', 'sī fue-', 'sī · fu · e', '<b>– ˘ ˘</b>'],
    ['1ª metade, sílaba final', '-rint ‖', 'rint', '<b>–</b>'],
    ['2ª metade, pé 1', 'nūbila', 'nū · bi · la', '<b>– ˘ ˘</b>'],
    ['2ª metade, pé 2', 'sōlus e-', 'sō · lus · e', '<b>– ˘ ˘</b>'],
    ['2ª metade, sílaba final', '-ris', 'ris', '<b>×</b>'],
], 'Tristia 1.9.6: o pentâmetro do dístico', latim_cols=(1, 2))

LICAO = dict(
    slug='40-metrica-e-figuras', titulo='Noções de métrica e figuras de linguagem', titulo_latim='Dē metrīs et figūrīs', tempo='75 min',
    resumo='Como soa a poesia latina: a sílaba longa e a breve (por natureza e por posição), a elisão e a sinizese, o hexâmetro datílico escandido verso a verso na Eneida, o dístico elegíaco de Ovídio, uma amostra da estrofe sáfica e do asclepiadeu de Horácio e o verso rítmico dos hinos medievais. Depois, as figuras de linguagem que você vai encontrar nos autores, cada uma com um exemplo autêntico.',
    status='rascunho',
    creditos=dict(autor='Bibliotheca Latina', colaboradores=[], revisao_gramatical=None),
    direitos=dict(tipo='dominio_publico', licenca='CC BY 4.0', adaptacoes=[]),
    aulas_complementares=[],
    topicos=['métrica quantitativa', 'quantidade por natureza e por posição', 'muda + líquida (sílaba comum)', 'elisão', 'hiato', 'sinizese', 'pés: dáctilo, espondeu, troqueu, iambo',
             'hexâmetro datílico', 'cesura', 'escansão de Eneida 1.1', 'pentâmetro e dístico elegíaco', 'estrofe sáfica', 'asclepiadeu menor', 'verso rítmico medieval',
             'figuras de linguagem', 'aliteração', 'anáfora', 'tricolon', 'assíndeto e polissíndeto', 'zeugma', 'quiasmo', 'hipérbato', 'lítotes', 'metonímia e sinédoque', 'hendíadis', 'análise de frase autêntica'],
    prerequisitos=dict(texto='Capítulo 1 (divisão silábica, vogais longas e breves, regra do acento) e capítulo 8 (técnica de leitura de um texto corrido). Nenhuma gramática nova é exigida: as formas verbais e as construções que você ainda não estudou vêm explicadas ao lado de cada exemplo.',
                       licoes=['01-o-que-e-o-latim', '08-da-frase-ao-paragrafo']),
    referencias=[
        referencia('New Latin Grammar', 'Charles E. Bennett', catalogo='bennett-new-latin-grammar',
                   nota='§ 5 (quantidade de vogais e sílabas); § 360–361 (prosódia; verso baseado na quantidade, não no acento); § 362.1 e 362.3 (vogal antes de vogal; duas consoantes, mesmo na palavra seguinte); § 362.5 (vogal antes de j); §§ 363–364 (quantidade das sílabas finais); § 366.1–2 (mora; pés de três e de quatro tempos), 366.5 (ictus), 366.7 (elisão; 7a, hiato), 366.8 (cesura e diérese), 366.10 (sílaba final anceps); § 367.1 (sinizese); § 368 (hexâmetro: esquema, verso espondaico, cesuras; 368.3a escande Arma virumque canō); § 369 (pentâmetro e dístico elegíaco); § 346 (assíndeto); § 350.11 (hipérbato, anáfora, quiasmo, sínquise); § 374.2a (zeugma) e 374.4 (hendíadis); § 375.1 (lítotes) e 375.3 (aliteração, com sēnsim sine sēnsū aetās senēscit)', tipo='dominio_publico'),
        referencia("Allen and Greenough's New Latin Grammar", 'J. H. Allen e J. B. Greenough', catalogo='greenough-allen-and-greenough-s-new-latin-grammar-edicao-dcc',
                   nota='§§ 9–11 (quantidade da vogal e da sílaba; 11.b posição; 11.c muda + l/r, sílaba "comum" no verso; notas 2–3: consoante final e h); § 603 (regras gerais de quantidade); § 598.f (anáfora e quiasmo), 598.h (ordem entrelaçada, sínquise); Glossário da edição DCC (figuras gramaticais e retóricas: aliteração, anáfora, assíndeto, polissíndeto, hendíadis, hipérbato, lítotes, metonímia, sinédoque, zeugma). A edição DCC não inclui a parte de versificação da obra impressa.', tipo='dominio_publico'),
        referencia("Kennedy's Revised Latin Primer", 'Benjamin Hall Kennedy', catalogo='kennedy-kennedy-s-revised-latin-primer',
                   nota='§ 471 (regras gerais de quantidade; muda + líquida "duvidosa"), § 474 ("On the laws of metre": pés; elisão e ecthlipsis; hiato), §§ 475–476 (metro, ritmo, escansão e cesura), § 477 (hexâmetro), § 478 (pentâmetro e dístico elegíaco), §§ 481–482 (metros estróficos; estrofe sáfica). Números lidos no OCR e conferidos no índice do próprio livro (§§ 474 e 482).', tipo='dominio_publico'),
        referencia('Gramática Latina', 'Pe. João Ravizza', catalogo='ravizza-gramatica-latina',
                   nota='n. 496 (sintaxe figurada: assíndeto, zeugma, polissíndeto, anáfora, hipérbato, quiasmo); n. 522–523 (quantidade; muda + l/r no verso); n. 532 (métrica: verso quantitativo); n. 535 (licenças poéticas: elisão, sinalefa, sinérese); n. 536 (hexâmetro, pentâmetro, dístico); nn. 538–540 (composições: asclepiadeus, sáficos e adônio); n. 541 (metros clássicos na hinologia e passagem para a poesia acentual e rimada). Números lidos no OCR.', tipo='dominio_publico'),
        referencia('Vergílio, Aeneis I (vv. 1–11, 33, 630)', None, catalogo='maro-aeneis-texto-integral', url='https://www.thelatinlibrary.com/vergil/aen1.shtml', nota='versos escandidos nas seções 3 e 4, na prática guiada e nos exercícios; texto conferido em The Latin Library (com macrons nos vv. 1–33)', tipo='dominio_publico'),
        referencia('Ovídio, Tristia 1.9.1–2 e 5–6', None, url='https://www.thelatinlibrary.com/ovid/ovid.tristia1.shtml', nota='dístico analisado na seção 4; The Latin Library grafa sospes no v. 5 (Kennedy cita o verso com felix)', tipo='dominio_publico'),
        referencia('Horácio, Carmina 1.1.1 e 1.22.1', None, catalogo='flaccus-carmina-et-epodi-odes-e-epodos', url='https://www.thelatinlibrary.com/horace/carm1.shtml', nota='asclepiadeu menor e verso sáfico da seção 5', tipo='dominio_publico'),
        referencia('Dies irae, estrofe 1 (atribuído a Tomás de Celano)', None, catalogo='celano-dies-irae', url='https://la.wikisource.org/wiki/The_seven_great_hymns_of_the_mediaeval_church/Dies_Ir%C3%A6/Tommaso', nota='verso rítmico da seção 5, conferido na edição de C. C. Nott (1902) na Wikisource latina', tipo='dominio_publico'),
        referencia('Cícero, Cato Maior de senectute 38; In Catilinam 1.1 e 2.1; De re publica 6.26; De officiis 1.77', None, catalogo='cicero-in-catilinam-i-iv', url='https://www.thelatinlibrary.com/cicero/cat1.shtml', nota='exemplos de aliteração, anáfora, assíndeto, quiasmo e metonímia da seção 6, conferidos nas páginas de The Latin Library (senectute, cat1, cat2, repub6, off1)', tipo='dominio_publico'),
        referencia('Cícero, Pro Archia 14', None, url='https://www.thelatinlibrary.com/cicero/arch.shtml', nota='tricolon com anáfora da seção 6 e da prática guiada 2 (também citado por Bennett § 350.11b)', tipo='dominio_publico'),
        referencia('Suetônio, Dīvus Iūlius 37', None, url='https://www.thelatinlibrary.com/suetonius/suet.caesar.html', nota='Vēnī, vīdī, vīcī, o letreiro do triunfo pôntico', tipo='dominio_publico'),
        referencia('Terêncio, Andria 68', None, url='https://www.thelatinlibrary.com/ter.andria.html', nota='exemplo de zeugma no sentido amplo (Ravizza n. 496)', tipo='dominio_publico'),
        referencia('Vergílio, Georgica 2.192 e 3.344–345', None, url='https://www.thelatinlibrary.com/vergil/geo3.shtml', nota='hendíadis (paterīs et aurō) e polissíndeto (tēctumque laremque…); páginas geo2 e geo3 de The Latin Library', tipo='dominio_publico'),
        referencia('Biblia Sacra Vulgata (editio Clementina), Lucas 11,3', None, catalogo='vulgata-biblia-sacra-vulgata-editio-clementina', url='https://la.wikisource.org/wiki/Vulgata_Clementina/Evangelium_Secundum_Lucam', nota='exemplo de sinédoque (pānem)', tipo='dominio_publico'),
    ],
    objetivos=[
        'Dizer se uma sílaba é longa por natureza, longa por posição, breve ou comum (muda + líquida), explicando a regra aplicada.',
        'Reconhecer a elisão, o hiato e a sinizese e aplicá-los ao contar as sílabas de um verso.',
        'Escandir um hexâmetro datílico, dividindo-o em seis pés e localizando a cesura principal.',
        'Reconhecer o dístico elegíaco e escandir um pentâmetro; identificar de ouvido uma estrofe sáfica, um asclepiadeu e um verso rítmico medieval.',
        'Identificar, num texto autêntico, as figuras mais comuns (aliteração, anáfora, tricolon, assíndeto, polissíndeto, zeugma, quiasmo, hipérbato, lítotes, metonímia, sinédoque, hendíadis) e dizer que efeito cada uma produz.',
    ],
    secoes=[
        ('Um verso feito de durações, não de acentos', f'''
<p>Um verso português é medido pelo número de sílabas e pela posição dos acentos tônicos: o decassílabo heroico de Camões tem dez sílabas poéticas, com acento na sexta e na décima. O verso latino clássico segue outro princípio. Ele não conta sílabas nem acentos, mas <b>durações</b>: o poeta organiza sílabas longas e breves numa sequência regular, como um músico organiza notas longas e curtas num compasso. Bennett resume a diferença assim: a poesia latina se baseava na quantidade, não no acento (§ 361), e o Pe. Ravizza diz o mesmo em português, chamando a poesia grega e latina de "quantitativa" e a dos povos modernos de acentual (n. 532).</p>
<p>A unidade dessa música é a <b>mora</b>, o tempo de uma sílaba breve. Uma sílaba longa vale duas moras (Bennett § 366.1). As sílabas se agrupam em <b>pés</b>, pequenos compassos que se repetem ao longo do verso. Quatro pés bastam para começar:</p>
{tabela(['Pé', 'Esquema', 'Tempos', 'Exemplo (uma palavra)'], [
    ['dáctilo', '<b>– ˘ ˘</b>', '4', '<i>lītora</i>'],
    ['espondeu', '<b>– –</b>', '4', '<i>fātō</i>'],
    ['troqueu', '<b>– ˘</b>', '3', '<i>arma</i>'],
    ['iambo', '<b>˘ –</b>', '3', '<i>virō</i>'],
], 'Os pés mais frequentes (– longa, ˘ breve)')}
<p>Repare que o dáctilo e o espondeu têm a mesma duração, quatro tempos: é por isso que um pode substituir o outro no hexâmetro, como você verá na seção 3. A sílaba longa de cada pé recebe uma proeminência natural, que os gramáticos chamam <b>ictus</b> (Bennett § 366.5). Como exatamente os romanos liam um verso em voz alta, respeitando ao mesmo tempo as durações e o acento das palavras, é questão discutida entre os especialistas. Para aprender, o caminho mais seguro é este: leia cada palavra com o acento que ela tem na prosa (capítulo 1) e mantenha as longas com o dobro da duração das breves. O ritmo aparece sozinho.</p>
{dica('<b>Notação deste capítulo.</b> <b>–</b> marca a sílaba longa, <b>˘</b> a breve e <b>×</b> a última sílaba do verso, que pode ser longa ou breve (Bennett § 366.10 a chama <i>syllaba anceps</i>). O traço duplo <b>‖</b> marca a cesura.')}
'''),
        ('Sílabas longas e breves; elisão e sinizese', f'''
<p>No capítulo 1 você aprendeu a quantidade da sílaba para acentuar palavras. A métrica usa as mesmas regras, com duas diferenças: agora todas as sílabas contam, não só a penúltima, e as palavras de um verso se emendam umas nas outras como se fossem uma só.</p>
<h3>Longa por natureza, longa por posição</h3>
<p>Uma sílaba é <b>longa por natureza</b> quando tem vogal longa ou ditongo: <i>Rō-mā-nus</i>, <i>cae-lum</i>. É <b>longa por posição</b> quando a sua vogal, mesmo breve, é seguida de duas consoantes ou de <i>x</i> ou <i>z</i>, que valem por duas: <i>ter-ra</i>, <i>sax-um</i> (A&amp;G § 11.a–b). Atenção a um ponto que confunde muitos alunos: na sílaba longa por posição, a <b>vogal continua breve</b> e se pronuncia breve; o que fica longo é a sílaba, porque a primeira consoante "pesa" sobre ela. Em <i>est</i>, o <i>e</i> é breve, mas a sílaba é longa.</p>
<p>No verso, as duas consoantes podem estar em palavras diferentes. Em <i>et terrīs</i>, a sílaba <i>et</i> é longa porque o <i>t</i> final é seguido do <i>t</i> de <i>terrīs</i> (Bennett § 362.3). Pelo mesmo motivo, uma consoante final seguida de vogal passa para a palavra seguinte, e a sílaba fica aberta: em <i>prīmus ab ōrīs</i>, pronuncia-se <i>prī-mu-sa-bō-rīs</i>, e as sílabas <i>mu</i> e <i>sa</i> são breves (A&amp;G § 11, nota 2). Para essas contas, o <i>h</i> não vale como consoante, e o <i>qu</i> conta como uma só (A&amp;G § 11, nota 3).</p>
<h3>Breve e comum</h3>
<p>Uma vogal seguida imediatamente de outra vogal é, em regra, breve: <i>de-us</i>, <i>vi-a</i> (Bennett § 362.1; A&amp;G § 10.a). Resta o caso que o capítulo 1 já anunciou: uma vogal breve seguida de <b>consoante muda</b> (<i>p, b, t, d, c, g</i>) <b>+ <i>l</i> ou <i>r</i></b> forma sílaba breve na prosa, mas o poeta pode tratá-la como longa. Os gramáticos chamam essa sílaba de <b>comum</b> (A&amp;G § 11.c; Kennedy § 471.3, "doubtful"; Ravizza n. 523). A primeira sílaba de <i>patrem</i> se lê <i>pa-trem</i> (breve) ou <i>pat-rem</i> (longa), conforme o verso pedir.</p>
{tabela(['Palavra', 'Sílaba', 'Quantidade', 'Por quê'], [
    ['<i>Rōma</i>', '<i>Rō</i>', 'longa por natureza', 'vogal longa (macron)'],
    ['<i>caelum</i>', '<i>cae</i>', 'longa por natureza', 'ditongo'],
    ['<i>puella</i>', '<i>el</i>', 'longa por posição', '<i>e</i> breve + <i>ll</i>'],
    ['<i>saxum</i>', '<i>sax</i>', 'longa por posição', '<i>x</i> vale por duas consoantes'],
    ['<i>deus</i>', '<i>de</i>', 'breve', 'vogal antes de vogal'],
    ['<i>tenebrae</i>', '<i>ne</i>', 'comum', '<i>e</i> breve + <i>br</i> (muda + líquida)'],
], 'Classificando sílabas')}
<p>E as vogais finais? Algumas regras ajudam (o <i>-ā</i> do ablativo da primeira declinação é longo; o <i>-ō</i> final é quase sempre longo; o <i>-īs</i> do dativo e ablativo plural é longo: Bennett §§ 363–364), mas o melhor recurso continua sendo o que você já usa: textos e dicionários com macrons. Escandir não é adivinhar quantidades, é aplicar as regras de posição às quantidades que o dicionário dá.</p>
<h3>Elisão, hiato e sinizese</h3>
<p>Quando uma palavra termina em vogal, ditongo ou <i>-m</i> e a seguinte começa por vogal ou <i>h</i>, a sílaba final da primeira se <b>elide</b>: some na leitura métrica (Bennett § 366.7; Ravizza n. 535 a–b; Kennedy chama de <i>ecthlipsis</i> a elisão com <i>-m</i>). O português faz algo parecido quando canta "de amor" como "d'amor". Em <i>multum ille et</i> (<i>Eneida</i> 1.3), as cinco sílabas escritas (<i>mul-tum-il-le-et</i>) reduzem-se a três na leitura métrica, <i>mul-til-let</i>, porque <i>-um</i> e <i>-e</i> desaparecem. A falta de elisão onde ela seria esperada chama-se <b>hiato</b>; é rara e costuma ocorrer junto a interjeições como <i>ō</i> (Bennett § 366.7a).</p>
<p>A <b>sinizese</b> (ou sinérese) faz o contrário dentro de uma palavra: duas vogais vizinhas se fundem numa sílaba longa. <i>Deinde</i> se lê em duas sílabas, <i>dein-de</i>; <i>deesse</i> também, <i>dēs-se</i> (Bennett § 367.1; Ravizza n. 535 c). Essas licenças não são arbitrárias: em geral refletem pronúncias correntes que a escrita não mostrava.</p>
'''),
        ('O hexâmetro datílico: escandindo a Eneida', f'''
<p>O <b>hexâmetro datílico</b> é o verso da epopeia: Ênio, Lucrécio, Vergílio e as <i>Metamorfoses</i> de Ovídio são escritos nele. Tem seis pés. Os quatro primeiros podem ser dáctilos ou espondeus; o quinto é quase sempre dáctilo; o sexto tem duas sílabas, a última indiferente (Bennett § 368.1; Kennedy § 477; Ravizza n. 536 a):</p>
{tabela(['Pé', 'Forma', 'Observação'], [
    ['1º a 4º', '<b>– ˘ ˘</b> ou <b>– –</b>', 'dáctilo ou espondeu, à escolha do poeta'],
    ['5º', '<b>– ˘ ˘</b>', 'quase sempre dáctilo'],
    ['6º', '<b>– ×</b>', 'duas sílabas; a última, indiferente'],
], 'Esquema do hexâmetro')}
<p>A regra do quinto pé dá ao hexâmetro uma cadência final inconfundível, <b>– ˘ ˘ | – ×</b>, que você ouve em <i>condere gentem</i> ou <i>prīmus ab ōrīs</i>. Quando o quinto pé é espondeu, o verso se chama espondaico, e é raro (Bennett § 368.2).</p>
<p>No capítulo 7 você procurou no dicionário as palavras do primeiro verso da <i>Eneida</i>. Agora é possível ouvi-lo. O método tem quatro passos: (1) marque as longas por natureza que o texto e o dicionário dão; (2) aplique as regras de posição, inclusive entre palavras; (3) faça as elisões; (4) comece pelo fim, onde a cadência é fixa, e distribua o resto em dáctilos e espondeus.</p>
{exemplos([('Arma virumque canō, Trōiae quī prīmus ab ōrīs', 'Canto as armas e o herói que, primeiro, das costas de Troia… (Vergílio, <i>Eneida</i> 1.1)')])}
{_AEN_1_1}
<p>Três detalhes merecem atenção. <i>Ar</i> é longa por posição (<i>r</i> + <i>m</i>), embora o <i>a</i> seja breve. <i>Trōiae</i> se pronuncia <i>Trōi-iae</i>: o <i>i</i> entre vogais é consoante e "dobra", de modo que a sílaba seguinte, <i>iae</i>, começa por consoante e tem ditongo, longa. E <i>prīmus ab</i> dá um dáctilo porque <i>-s</i> e <i>-b</i> passam para as vogais seguintes (<i>prī-mu-sa-bō-rīs</i>), deixando <i>mu</i> e <i>sa</i> abertas e breves.</p>
{diagrama_frase([('Arma vi-', 'dáctilo · – ˘ ˘'), ('-rumque ca-', 'dáctilo · – ˘ ˘'), ('-nō Trō-', 'espondeu · – –'), ('-iae quī', 'espondeu · – –'), ('prīmus ab', 'dáctilo · – ˘ ˘'), ('ōrīs', 'final · – ×')], 'Os seis pés de <i>Eneida</i> 1.1. A cesura cai depois de <i>canō</i>, no meio do terceiro pé.')}
<h3>A cesura</h3>
<p>Quando uma palavra termina no meio de um pé, há uma <b>cesura</b> (Bennett § 366.8). Todo hexâmetro tem uma cesura principal, que funciona como respiração e quase sempre coincide com uma pausa de sentido. A mais comum fica depois da primeira sílaba do terceiro pé, e Bennett ilustra justamente com este verso: <i>arma virumque canō ‖ Trōiae quī prīmus ab ōrīs</i> (§ 368.3a). A primeira metade anuncia o tema; a segunda começa a narrativa. Quando a cesura cai depois da primeira sílaba do quarto pé, geralmente vem acompanhada de outra no segundo (§ 368.3b; Kennedy § 477). Um segundo verso, sem elisões, mostra o mesmo desenho:</p>
{exemplos([('Tantae mōlis erat Rōmānam condere gentem!', 'Tão grande esforço era fundar a nação romana! (<i>Eneida</i> 1.33; <i>tantae mōlis</i>, "de tão grande esforço", é um genitivo; <i>condere</i>, "fundar", é infinitivo)')])}
{_AEN_1_33}
<p>Este verso fecha o proêmio da <i>Eneida</i>, e o ritmo trabalha a favor do sentido: três espondeus em quatro pés tornam o verso lento e pesado, como o esforço que ele descreve. Não exagere esse tipo de leitura, mas também não a despreze: os poetas latinos escolhiam dáctilos e espondeus com intenção (Ravizza n. 536 a observa que muitos dáctilos exprimem rapidez).</p>
'''),
        ('O dístico elegíaco: um pentâmetro depois de cada hexâmetro', f'''
<p>O <b>pentâmetro</b> nunca aparece sozinho: vem sempre depois de um hexâmetro, e o par forma o <b>dístico elegíaco</b>, o metro de Ovídio, Tibulo e Propércio, e também do epigrama (Bennett § 369.2; Kennedy § 478; Ravizza n. 536 b). O nome engana: o verso não tem cinco pés iguais. São duas metades de dois pés e meio, separadas por uma cesura fixa. Na primeira metade os pés podem ser dáctilos ou espondeus; na segunda, só dáctilos (Bennett § 369.1):</p>
{tabela(['Metade', 'Esquema'], [
    ['1ª', '<b>– ˘ ˘ | – ˘ ˘ | –</b> &nbsp;(os dois pés podem ser – –)'],
    ['2ª', '<b>– ˘ ˘ | – ˘ ˘ | ×</b> &nbsp;(sempre dáctilos)'],
], 'Esquema do pentâmetro')}
<p>O efeito é de pergunta e resposta: o hexâmetro corre, e o pentâmetro, com duas paradas bruscas, fecha o pensamento. Ovídio, exilado no mar Negro, escreve a um amigo fiel:</p>
{exemplos([('Dōnec eris sospes, multōs numerābis amīcōs:<br>&nbsp;&nbsp;&nbsp;tempora sī fuerint nūbila, sōlus eris.', 'Enquanto estiveres a salvo, contarás muitos amigos; se os tempos se fizerem nublados, estarás sozinho. (Ovídio, <i>Tristia</i> 1.9.5–6; texto da The Latin Library, que traz <i>sospes</i>; Kennedy § 478 cita o verso com <i>fēlīx</i>, a forma que se tornou proverbial)')])}
{_TRIST_HEX}
{_TRIST_PENT}
<p>No hexâmetro, <i>ris</i> e <i>pes</i> são longas por posição (<i>-s</i> + consoante), embora tenham vogal breve; a cesura cai depois de <i>sospes</i>. No pentâmetro, <i>rint</i> é longa por posição e fecha a primeira metade; a segunda metade corre em dois dáctilos até o <i>eris</i> final, que repete o <i>eris</i> do primeiro verso. A forma métrica sublinha o sentido: o dístico começa com "muitos amigos" e termina, depois da parada, com "sozinho".</p>
<h3>Análise palavra a palavra</h3>
<p>Duas formas verbais deste dístico pertencem a capítulos posteriores ao capítulo 8, o pré-requisito deste: <i>eris</i> é o futuro de <i>sum</i> (capítulo 12) e <i>fuerint</i>, o futuro perfeito (capítulo 13). Basta reconhecê-las pela tradução.</p>
{analise('Ovídio, Tristia 1.9.5–6', [
    ('Dōnec', 'dōnec (conjunção), enquanto', 'invariável', 'abre a oração de tempo'),
    ('eris', 'sum, esse, ser, estar', 'futuro, 2ª pessoa do singular', 'verbo da oração de tempo: "estiveres"'),
    ('sospes', 'sospes, -itis, são e salvo, próspero', 'nominativo singular (3ª declinação)', 'predicativo do sujeito "tu"'),
    ('multōs', 'multus, -a, -um, muito', 'acusativo plural masculino', 'concorda com <i>amīcōs</i>'),
    ('numerābis', 'numerō, -āre, contar', 'futuro, 2ª pessoa do singular', 'verbo principal: "contarás"'),
    ('amīcōs', 'amīcus, -ī (m.), amigo', 'acusativo plural', 'objeto direto de <i>numerābis</i>'),
    ('tempora', 'tempus, -oris (n.), tempo', 'nominativo plural neutro (capítulo 9)', 'sujeito de <i>fuerint</i>'),
    ('sī', 'sī (conjunção), se', 'invariável', 'abre a oração condicional (capítulo 36)'),
    ('fuerint', 'sum, esse', 'futuro perfeito, 3ª pessoa do plural', '"tiverem sido", em português melhor "se fizerem"'),
    ('nūbila', 'nūbilus, -a, -um, nublado, sombrio', 'nominativo plural neutro', 'predicativo de <i>tempora</i>'),
    ('sōlus', 'sōlus, -a, -um, só, sozinho', 'nominativo singular masculino', 'predicativo do sujeito "tu"'),
    ('eris', 'sum, esse', 'futuro, 2ª pessoa do singular', 'verbo principal: "estarás"'),
])}
<p>Repare que nenhuma das duas orações tem o sujeito "tu" expresso: ele está nas terminações <i>-s</i> de <i>eris</i> e <i>numerābis</i>, como você aprendeu no capítulo 8. E <i>tempora</i>, neutro plural, poderia ser acusativo; decide por exclusão a concordância com <i>fuerint</i>, plural, que precisa de um sujeito.</p>
'''),
        ('Lírica e hinos: o sáfico, o asclepiadeu e o verso rítmico', f'''
<p>Catulo e Horácio usaram dezenas de metros líricos, quase todos imitados dos poetas gregos. Você vai lê-los no capítulo 45; aqui basta aprender a reconhecer dois deles, que ao contrário do hexâmetro <b>não admitem substituições</b> livres: cada posição do verso tem quantidade fixa.</p>
<h3>A estrofe sáfica</h3>
<p>Leva o nome de Safo, a poeta grega de Lesbos. Tem quatro versos: três <b>sáficos</b> de onze sílabas e um verso curto final, o <b>adônio</b> (<b>– ˘ ˘ – ×</b>) (Kennedy § 482; Ravizza n. 540 a). Diferentemente de Safo, os poetas latinos fazem sempre longa a quarta sílaba do sáfico, como observa Kennedy, e Horácio segue a regra:</p>
{exemplos([('Integer vītae scelerisque pūrus', 'Íntegro de vida e puro de crime… (Horácio, <i>Odes</i> 1.22.1)')])}
{_segmentos('O verso sáfico (11 sílabas)', [
    ('Integer', 'in · te · ger', '– ˘ –'),
    ('vītae', 'vī · tae', '– –'),
    ('scelerisque', 'sce · le · ris · que', '˘ ˘ – ˘'),
    ('pūrus', 'pū · rus', '– ×'),
])}
<p>O esquema completo é <b>– ˘ – – – ˘ ˘ – ˘ – ×</b>. Note que <i>ger</i> é longa por posição (<i>r</i> + <i>v</i> da palavra seguinte) e <i>ris</i> também (<i>s</i> + <i>qu</i>).</p>
<h3>O asclepiadeu menor</h3>
<p>Tem doze sílabas, com uma cesura fixa no meio (Ravizza n. 538 e, que cita este mesmo verso). Horácio abre o primeiro livro das <i>Odes</i> com ele:</p>
{exemplos([('Maecēnās atavīs ēdite rēgibus', 'Mecenas, descendente de reis ancestrais… (Horácio, <i>Odes</i> 1.1.1)')])}
{_segmentos('O asclepiadeu menor (12 sílabas)', [
    ('Maecēnās', 'mae · cē · nās', '– – –'),
    ('atavīs ‖', 'a · ta · vīs', '˘ ˘ –'),
    ('ēdite', 'ē · di · te', '– ˘ ˘'),
    ('rēgibus', 'rē · gi · bus', '– ˘ ×'),
])}
<p>O esquema é <b>– – – ˘ ˘ – ‖ – ˘ ˘ – ˘ ×</b>: duas metades quase simétricas, cada uma com um "dáctilo" no centro.</p>
<h3>Do metro ao ritmo: os hinos medievais</h3>
<p>A Igreja antiga e medieval ainda compôs hinos em metros clássicos; Ravizza lista hexâmetros, dísticos, sáficos e asclepiadeus na hinologia (n. 541). Mas a pronúncia mudou: com o tempo, a diferença entre vogais longas e breves deixou de ser ouvida, e só o acento tônico continuou claro. Surgiu então um verso novo, o <b>verso rítmico</b>, que conta sílabas, alterna acentos e usa <b>rima</b>, como faria depois a poesia das línguas modernas, baseada no número de sílabas e na sucessão dos acentos (Ravizza, n. 541, último parágrafo). O exemplo mais famoso é o <i>Diēs īrae</i>:</p>
{exemplos([('Dies irae, dies illa<br>solvet saeclum in favilla,<br>teste David cum Sibylla.', 'Dia de ira, aquele dia dissolverá o mundo em cinzas, como atestam Davi e a Sibila. (<i>Dies irae</i>, estrofe 1; o texto vai sem macrons de propósito, porque aqui eles não contam)')])}
{comparacao('Dois princípios de verso', ['Verso', 'Mede', 'Rima', 'Exemplo'], [
    ['Quantitativo (clássico)', 'durações: longas e breves em pés', 'não usa', '<i>Arma virumque canō…</i>'],
    ['Rítmico (medieval)', 'número de sílabas e posição dos acentos', 'usa', '<i>Dies irae, dies illa…</i>'],
])}
<p>Cada verso do <i>Diēs īrae</i> tem oito sílabas, com acento nas ímpares: <i>DÍ-es Í-rae, DÍ-es ÍL-la</i>. Não há elisão (<i>saeclum in</i> conta três sílabas, <i>sae-clum-in</i>), e as três linhas rimam em <i>-illa</i>. Quem tentar escandi-lo em longas e breves vai se frustrar; quem ler pelo acento, como leria um poema em português, vai ouvi-lo na hora. O capítulo 52 lê este hino e o <i>Pange lingua</i> por inteiro.</p>
'''),
        ('Figuras de linguagem: as que você vai encontrar nos autores', f'''
<p>Os romanos aprendiam retórica na escola, e quase todo autor latino escreve com consciência do efeito de cada frase. As figuras não são enfeites a serem catalogados: são escolhas de som, de ordem e de sentido que fazem o texto convencer ou comover. Para o leitor, reconhecê-las tem uma utilidade bem prática: muitas "dificuldades" de uma frase latina são figuras, e entendê-las resolve a dificuldade. A lista abaixo traz as mais frequentes, cada uma com um exemplo autêntico conferido na fonte (os macrons foram acrescentados).</p>
<h3>Som e repetição</h3>
<p><b>Aliteração</b>: repetição do mesmo som, em geral no início de palavras vizinhas (Bennett § 375.3).</p>
{exemplos([('Ita <b>s</b>ēnsim <b>s</b>ine <b>s</b>ēnsū aetās <b>s</b>enēscit.', 'Assim, pouco a pouco, sem que se perceba, a idade envelhece. (Cícero, <i>Sobre a velhice</i> 38; o sibilar dos <i>s</i> imita o passar silencioso do tempo)')])}
<p><b>Anáfora</b>: repetição da mesma palavra no início de membros sucessivos (A&amp;G § 598.f; Ravizza n. 496.6).</p>
{exemplos([('<b>Nihil</b>ne tē nocturnum praesidium Palātī, <b>nihil</b> urbis vigiliae, <b>nihil</b> timor populī, <b>nihil</b> concursus bonōrum omnium… mōvērunt?', 'Nada te abalaram a guarda noturna do Palatino, nada as sentinelas da cidade, nada o medo do povo, nada a reunião de todos os homens de bem…? (Cícero, <i>Contra Catilina</i> 1.1)')])}
<p><b>Tricolon</b>: três membros paralelos, muitas vezes de tamanho crescente. É talvez a forma de frase mais típica da prosa de Cícero, e costuma vir junto com a anáfora (Bennett cita este exemplo, como anáfora, em § 350.11b).</p>
{exemplos([('plēnī omnēs sunt librī, plēnae sapientium vōcēs, plēna exemplōrum vetustās', 'cheios estão todos os livros, cheias as vozes dos sábios, cheia de exemplos a antiguidade (Cícero, <i>Em defesa de Árquias</i> 14)')])}
<h3>Ligação: com conjunções demais ou de menos</h3>
<p><b>Assíndeto</b>: omissão das conjunções entre membros coordenados, para dar rapidez ou emoção (Bennett § 346; Ravizza n. 496.2–3). <b>Polissíndeto</b>: o contrário, a repetição da conjunção, que alonga e acumula (Ravizza n. 496.5).</p>
{exemplos([
    ('Abiit, excessit, ēvāsit, ērūpit.', 'Foi-se, retirou-se, escapou, irrompeu para fora. (Cícero, <i>Contra Catilina</i> 2.1: quatro verbos sem "e", em gradação, para a fuga de Catilina)'),
    ('Vēnī, vīdī, vīcī.', 'Vim, vi, venci. (Suetônio, <i>César</i> 37: o letreiro do triunfo de César sobre o Ponto; assíndeto, tricolon e aliteração juntos)'),
    ('…tēctum<b>que</b> larem<b>que</b> / arma<b>que</b> Amyclaeum<b>que</b> canem Cressam<b>que</b> pharetram', '…e a casa, e o lar, e as armas, e o cão de Amiclas, e a aljava cretense (Vergílio, <i>Geórgicas</i> 3.344–345: o pastor africano leva tudo consigo; os cinco <i>-que</i> fazem sentir o peso da bagagem)'),
])}
<p><b>Zeugma</b>: um só verbo serve a dois membros e fica subentendido num deles. No sentido estrito de Bennett (§ 374.2a) e do glossário de A&amp;G, o verbo convém propriamente a um só dos membros; no sentido mais amplo de Ravizza (n. 496, observação), basta que a palavra seja subentendida no segundo membro, ainda que com outra forma.</p>
{exemplos([('obsequium amīcōs, vēritās odium parit', 'a complacência gera amigos, a franqueza [gera] ódio (Terêncio, <i>Ândria</i> 68: <i>parit</i>, "gera", serve aos dois membros; zeugma no sentido amplo de Ravizza)'),
           ('pācem an bellum gerēns', '"estando em paz ou em guerra", literalmente "conduzindo a paz ou a guerra" (Salústio, <i>Guerra de Jugurta</i> 46.8, citado por Lewis &amp; Short s.v. <i>gerō</i>: <i>gerere</i> convém propriamente a <i>bellum</i>, e só por extensão a <i>pācem</i>; zeugma no sentido estrito)')])}
<h3>Ordem das palavras</h3>
<p><b>Quiasmo</b>: dois pares de palavras em ordem inversa, A B | B A, desenhando um X (a letra grega <i>chi</i>) (Bennett § 350.11c; A&amp;G § 598.f; Ravizza n. 496.20, que cita este exemplo).</p>
{exemplos([('…sīc <b>fragile</b> <u>corpus</u> <u>animus</u> <b>sempiternus</b> movet.', '…assim o espírito eterno move o corpo frágil. (Cícero, <i>Sonho de Cipião</i> = <i>Da república</i> 6.26: adjetivo–nome | nome–adjetivo, e os opostos "frágil" e "eterno" nas pontas)')])}
<p><b>Hipérbato</b>: separação de palavras que normalmente andam juntas, como um adjetivo e o seu nome (Bennett § 350.11a). Na poesia ele é constante, muitas vezes na forma entrelaçada (<b>sínquise</b>), em que os pares se cruzam: a b A B (Bennett § 350.11d; A&amp;G § 598.h).</p>
{exemplos([('saevae memorem Iūnōnis ob īram', 'por causa da ira rancorosa da cruel Juno (Vergílio, <i>Eneida</i> 1.4: <i>saevae</i> concorda com <i>Iūnōnis</i>, <i>memorem</i> com <i>īram</i>; a ordem entrelaçada prende o verso inteiro até a última palavra)')])}
{dica('<b>Hipérbato não é qualquer ordem livre.</b> O latim já põe as palavras em muitas ordens possíveis (capítulo 2). Fale de hipérbato quando a separação é marcada: quando você precisa de um par de terminações para reunir duas palavras distantes, como <i>saevae … Iūnōnis</i>.')}
<h3>Sentido</h3>
<p><b>Lítotes</b>: afirmar algo negando o contrário, quase sempre para dizer mais, com discrição (Bennett § 375.1).</p>
{exemplos([('Nōn ignāra malī miserīs succurrere discō.', 'Não ignorante do sofrimento, aprendo a socorrer os infelizes. (Vergílio, <i>Eneida</i> 1.630: Dido quer dizer que conhece o sofrimento muito bem)')])}
<p><b>Metonímia</b>: usar o nome de uma coisa por outra ligada a ela (o instrumento pela atividade, o símbolo pela instituição). <b>Sinédoque</b>: usar a parte pelo todo, ou o todo pela parte (Glossário de A&amp;G).</p>
{exemplos([
    ('cēdant arma togae, concēdat laurea laudī', 'cedam as armas à toga, ceda o louro ao louvor (verso de Cícero citado por ele mesmo em <i>Dos deveres</i> 1.77: <i>arma</i> é a guerra, <i>toga</i> a vida civil, <i>laurea</i> o triunfo militar: metonímias)'),
    ('Pānem nostrum quotīdiānum dā nōbīs hodiē.', 'O pão nosso de cada dia dá-nos hoje. (Lc 11,3, Vulgata: o "pão" é todo o sustento, sinédoque)'),
])}
<p><b>Hendíadis</b> ("um por meio de dois"): dois nomes ligados por "e" exprimem uma só ideia, em que um deles qualifica o outro (Bennett § 374.4).</p>
{exemplos([('…quālem paterīs lībāmus et aurō', '…[um vinho] tal como o que libamos em páteras e ouro, isto é, em páteras de ouro (Vergílio, <i>Geórgicas</i> 2.192)')])}
{tabela(['Figura', 'Em uma frase'], [
    ['aliteração', 'mesmo som repetido em palavras vizinhas'],
    ['anáfora', 'mesma palavra no início de membros sucessivos'],
    ['tricolon', 'três membros paralelos, em geral crescentes'],
    ['assíndeto / polissíndeto', 'conjunções omitidas / repetidas'],
    ['zeugma', 'um verbo serve a dois membros'],
    ['quiasmo', 'pares em ordem inversa: A B | B A'],
    ['hipérbato', 'palavras que andam juntas aparecem separadas'],
    ['lítotes', 'afirmar negando o contrário'],
    ['metonímia / sinédoque', 'coisa por coisa ligada / parte pelo todo'],
    ['hendíadis', 'dois nomes coordenados por uma ideia só'],
], 'Resumo das figuras')}
<p>Quando encontrar uma figura, faça sempre duas perguntas: <b>qual é</b> e <b>o que ela faz</b> ali. "Há uma anáfora" é só metade da resposta; "a anáfora de <i>nihil</i> martela a ideia de que nada intimida Catilina" é a leitura inteira.</p>
'''),
    ],
    erros_comuns=[
        ('Achar que, na sílaba longa por posição, a vogal também fica longa, e pronunciar <i>ēst</i> ou <i>tērra</i>.', 'O que é longo é a <b>sílaba</b>, não a vogal: em <i>est</i> e <i>terra</i> o <i>e</i> continua breve e se pronuncia breve; a duração extra vem da consoante que fecha a sílaba (A&amp;G § 11.b). Por isso os textos com macrons não marcam o <i>e</i> de <i>est</i>.'),
        ('Contar as sílabas elididas ao escandir.', 'Vogal, ditongo ou <i>-m</i> final antes de vogal ou <i>h</i> desaparece na leitura métrica (Bennett § 366.7). Antes de dividir o verso em pés, risque as elisões: em <i>multum ille et</i>, o <i>-um</i> e o <i>-e</i> não contam. Se o seu verso tiver sílabas demais, procure primeiro uma elisão esquecida.'),
        ('Escandir pelo acento tônico, como num verso português.', 'O acento da palavra e a quantidade da sílaba são coisas diferentes: <i>canō</i> tem acento em <i>ca</i>, que é breve, e a sílaba longa é <i>nō</i>. Escanda pelas durações; o acento tônico só serve para ler as palavras naturalmente.'),
        ('Tratar a muda + líquida sempre do mesmo jeito.', 'Em <i>patrem</i>, <i>tenebrae</i>, <i>agrī</i>, a sílaba antes de <i>tr, br, gr</i> é <b>comum</b>: o poeta a usa como breve ou como longa, conforme o verso pede (A&amp;G § 11.c). Deixe essas sílabas por último e decida-as pelo esquema do verso.'),
        ('Procurar longas e breves num hino medieval rítmico (ou contar só sílabas num verso de Vergílio).', 'São dois sistemas. O <i>Diēs īrae</i> mede número de sílabas e acentos e usa rima; a <i>Eneida</i> mede durações e não rima. Antes de ler um poema, pergunte de que época e de que tipo ele é.'),
        ('Chamar de figura qualquer coisa estranha, sem dizer o efeito; ou ver hipérbato em toda ordem livre.', 'A ordem latina é naturalmente flexível (capítulo 2). Identifique a figura com o critério da definição (há mesmo três membros paralelos? há mesmo inversão A B | B A?) e diga o que ela faz no texto: rapidez, ênfase, contraste, solenidade.'),
    ],
    pratica_guiada=[
        pratica_guiada('Prática guiada 1 · Escandir um verso com elisões',
            'Escanda <i lang="la">lītora, multum ille et terrīs iactātus et altō</i> (Vergílio, <i>Eneida</i> 1.3: "[às] costas, muito ele, atirado por terras e por mar"). Use os quatro passos da seção 3.', [
            ('Passo 1: quais sílabas são longas por natureza?', 'As que têm vogal longa marcada: <i>lī</i>, <i>rīs</i> (de <i>terrīs</i>, ablativo plural), <i>tā</i> (de <i>iactātus</i>) e <i>tō</i> (de <i>altō</i>).'),
            ('Passo 2: quais são longas por posição?', '<i>mul</i> (<i>l</i> + <i>t</i>), <i>il</i> (<i>ll</i>), <i>et</i> antes de <i>terrīs</i> (<i>t</i> + <i>t</i>, entre palavras), <i>ter</i> (<i>rr</i>), <i>iac</i> (<i>c</i> + <i>t</i>) e <i>al</i> (<i>l</i> + <i>t</i>).'),
            ('Passo 3: onde há elisão?', 'Duas vezes: <i>multum</i> antes de <i>ille</i> perde o <i>-um</i>, e <i>ille</i> antes de <i>et</i> perde o <i>-e</i>. Lê-se <i>mul-til-let-ter-rīs</i>. Também <i>tātus et altō</i> se emenda: <i>tā-tu-se-tal-tō</i>, e <i>tu</i> e <i>se</i> ficam breves, porque as consoantes passam para as vogais seguintes.'),
            ('Passo 4: comece pelo fim. Quais são o 5º e o 6º pés?', '6º: <i>altō</i> (<i>al-tō</i>, – ×). 5º: <i>tātus et</i> (<i>tā-tu-se</i>, – ˘ ˘), o dáctilo obrigatório.'),
            ('Distribua o resto em quatro pés.', '1º <i>lītora</i> (– ˘ ˘, dáctilo); 2º <i>mult(um) il-</i> (<i>mul-til</i>, – –, espondeu); 3º <i>-l(e) et ter-</i> (<i>let-ter</i>, – –, espondeu); 4º <i>-rīs iac-</i> (– –, espondeu). Seis pés: D E E E D E (D = dáctilo, E = espondeu).'),
        ], 'Conferência: se você não tivesse feito as elisões, sobrariam duas sílabas e os pés não fechariam. É o sinal mais seguro de que uma elisão foi esquecida.'),
        pratica_guiada('Prática guiada 2 · Reconhecer figuras num período de Cícero',
            'Leia <i lang="la">Sed plēnī omnēs sunt librī, plēnae sapientium vōcēs, plēna exemplōrum vetustās.</i> (Cícero, <i>Em defesa de Árquias</i> 14). Vocabulário: <i>plēnus, -a, -um</i>, cheio; <i>sapiēns, -entis</i>, sábio; <i>vōx, vōcis</i> (f.), voz; <i>exemplum, -ī</i>, exemplo; <i>vetustās, -ātis</i> (f.), antiguidade.', [
            ('Quantos membros paralelos há, e como você sabe?', 'Três: cada um tem a forma "cheio + nome". <i>Plēnī … librī</i>, <i>plēnae … vōcēs</i>, <i>plēna … vetustās</i>. É um <b>tricolon</b>.'),
            ('Que palavra se repete, e onde?', 'O adjetivo <i>plēnus</i>, sempre no início de cada membro: <b>anáfora</b>. Ele muda de forma para concordar com cada nome (<i>plēnī</i> masc. pl., <i>plēnae</i> fem. pl., <i>plēna</i> fem. sing.), o que confirma a que nome cada um pertence.'),
            ('Há conjunções entre os membros? E o verbo?', 'Não há "e": <b>assíndeto</b>. E o verbo <i>sunt</i> aparece só no primeiro membro e fica subentendido nos outros dois (no terceiro, no singular: <i>est</i>): é o tipo de omissão que Ravizza chama de zeugma no sentido amplo.'),
            ('Que efeito o conjunto produz?', 'A acumulação sem conjunções e a repetição de <i>plēnus</i> dão a impressão de uma evidência esmagadora: tudo, livros, sábios e história, está cheio de exemplos de virtude. É o argumento de Cícero a favor das letras.'),
        ]),
    ],
    exercicios=[
        exercicio('Exercício 1 · Longa, breve ou comum?', 'Diga a quantidade da sílaba destacada e a regra aplicada.', [
            ('<i>Rō<b>mā</b>nus</i>', 'Longa por natureza: vogal longa <i>ā</i>.'),
            ('<i><b>poe</b>na</i>', 'Longa por natureza: ditongo <i>oe</i>.'),
            ('<i>ma<b>gis</b>ter</i>', 'Longa por posição: <i>i</i> breve seguido de <i>s</i> + <i>t</i>.'),
            ('<i><b>vi</b>a</i>', 'Breve: vogal seguida imediatamente de outra vogal.'),
            ('<i><b>a</b>grī</i>', 'Comum: <i>a</i> breve seguido de muda + líquida (<i>gr</i>); breve na prosa, longa ou breve no verso.'),
            ('<i><b>et</b> terrīs</i> (num verso)', 'Longa por posição: o <i>t</i> de <i>et</i> e o <i>t</i> de <i>terrīs</i> somam duas consoantes, mesmo em palavras diferentes (Bennett § 362.3).'),
            ('<i>prīm<b>us</b> ab</i> (num verso)', 'Breve: o <i>-s</i> passa para a vogal de <i>ab</i> (<i>prī-mu-sab</i>), e a sílaba <i>mu</i> fica aberta com vogal breve.'),
        ]),
        exercicio('Exercício 2 · Elisões', 'Marque as elisões e diga quantas sílabas cada trecho tem na leitura métrica. Todos os versos são da <i>Eneida</i>, livro 1.', [
            ('<i>multa quoque et bellō passus</i> (v. 5: "tendo sofrido muito também na guerra")', 'Uma elisão: <i>quoqu(e) et</i>. Sílabas: <i>mul-ta-quo-quet-bel-lō-pas-sus</i>, oito.'),
            ('<i>Albānīque patrēs, atque altae moenia Rōmae</i> (v. 7: "e os pais albanos, e as muralhas da alta Roma")', 'Uma elisão: <i>atqu(e) altae</i>. São 15 sílabas escritas (<i>Al-bā-nī-que-pa-trēs-at-que-al-tae-moe-ni-a-Rō-mae</i>) e 14 na leitura métrica, porque o <i>-que</i> de <i>atque</i> cai: <i>…at-qual-tae…</i>.'),
            ('<i>impulerit. Tantaene animīs caelestibus īrae?</i> (v. 11: "…[a] impeliu. Tão grandes iras há nos espíritos celestes?")', 'Uma elisão: <i>Tantaen(e) animīs</i>. A pausa de sentido depois de <i>impulerit</i> não impede a elisão seguinte, que se dá entre <i>Tantaene</i> e <i>animīs</i>.'),
            ('<i>Arma virumque canō, Trōiae quī prīmus ab ōrīs</i> (v. 1)', 'Nenhuma elisão: nenhuma palavra terminada em vogal ou <i>-m</i> vem antes de vogal. (<i>Canō, Trōiae</i>: <i>Trōiae</i> começa por consoante.)'),
        ]),
        exercicio('Exercício 3 · Escanda hexâmetros', 'Divida em seis pés, diga o tipo de cada um (D = dáctilo, E = espondeu) e localize a cesura principal.', [
            ('<i>Mūsa, mihī causās memorā, quō nūmine laesō</i> (<i>Eneida</i> 1.8: "Musa, recorda-me as causas, por qual divindade ofendida…")', '<i>Mūsa mi- | -hī cau- | -sās ‖ memo- | -rā quō | nūmine | laesō</i>: D E D E D E. Cesura depois de <i>causās</i>, primeira sílaba do 3º pé. <i>Sa</i> e <i>mi</i> são breves; <i>mihī</i> aqui tem o <i>ī</i> final longo (Bennett § 363.3 admite as duas quantidades).'),
            ('<i>multa quoque et bellō passus, dum conderet urbem</i> (<i>Eneida</i> 1.5)', '<i>multa quo- | -qu(e) et bel- | -lō ‖ pas- | -sus dum | conderet | urbem</i>: D E E E D E. <i>Ta</i> e <i>quo</i> são breves (<i>qu</i> vale uma consoante); <i>quet</i> é longa por posição (<i>t</i> + <i>b</i>). Cesura principal depois de <i>bellō</i> (3º pé); há outra depois de <i>passus</i> (4º pé). No fim, <i>conderet urbem</i> se lê <i>con-de-re-tur-bem</i>: o <i>-t</i> passa para <i>urbem</i>, <i>re</i> fica breve e o 5º pé é o dáctilo <i>con-de-re</i>.'),
            ('<i>Dētur inoffēnsō vītae tibi tangere mētam</i> (Ovídio, <i>Tristia</i> 1.9.1: "Que te seja dado tocar sem tropeço a meta da vida")', '<i>Dētur i- | -noffēn- | -sō ‖ vī- | -tae tibi | tangere | mētam</i>: D E E D D E. <i>Tu</i> e <i>ri</i> são breves (<i>dē-tu-ri-nof</i>); <i>nof</i> é longa por posição (<i>ff</i>). Cesura depois de <i>inoffēnsō</i>.'),
        ]),
        exercicio('Exercício 4 · O pentâmetro', 'Escanda o pentâmetro que completa o dístico do exercício anterior e responda.', [
            ('<i>quī legis hōc nōbīs nōn inimīcus opus</i> (<i>Tristia</i> 1.9.2: "tu que lês, sem hostilidade, esta obra minha")', '1ª metade: <i>quī legi- | -s hōc nō- | -bīs ‖</i> = – ˘ ˘ | – – | –. 2ª metade: <i>nōn ini- | -mīcus o- | -pus</i> = – ˘ ˘ | – ˘ ˘ | ×. O <i>h</i> de <i>hōc</i> não conta como consoante, por isso <i>gis</i> fica breve (<i>le-gi-shōc</i>).'),
            ('Por que a segunda metade do pentâmetro é mais previsível que a primeira?', 'Porque nela os dois pés são sempre dáctilos (Bennett § 369.1); na primeira, cada pé pode ser dáctilo ou espondeu.'),
            ('Em que lugar do pentâmetro há sempre fim de palavra?', 'No meio, depois da sílaba longa que fecha a primeira metade: em <i>nōbīs ‖</i> e em <i>fuerint ‖</i> (Bennett § 369.1).'),
        ]),
        exercicio('Exercício 5 · Que figura é esta?', 'Identifique a figura principal e diga o efeito. Todos os exemplos estão na seção 6.', [
            ('<i>Abiit, excessit, ēvāsit, ērūpit.</i>', '<b>Assíndeto</b> (e gradação): os verbos se seguem sem conjunção, cada vez mais fortes, e a frase imita a pressa da fuga.'),
            ('<i>Nōn ignāra malī</i>', '<b>Lítotes</b>: "não ignorante" quer dizer "bem conhecedora". A negação torna a afirmação discreta e, por isso mesmo, mais forte.'),
            ('<i>cēdant arma togae</i>', '<b>Metonímia</b>: as armas representam a guerra e a toga, a vida civil. O verso diz que a política deve prevalecer sobre a força militar.'),
            ('<i>paterīs lībāmus et aurō</i>', '<b>Hendíadis</b>: "páteras e ouro" = páteras de ouro. Os dois nomes coordenados exprimem uma ideia só.'),
            ('<i>fragile corpus animus sempiternus</i>', '<b>Quiasmo</b>: adjetivo + nome, nome + adjetivo. As pontas opõem "frágil" a "eterno", e o centro aproxima "corpo" e "espírito".'),
            ('<i>Vēnī, vīdī, vīcī.</i>', 'Três figuras juntas: <b>tricolon</b> (três membros), <b>assíndeto</b> (sem "e") e <b>aliteração</b> (<i>v-</i>). O efeito é de rapidez e de vitória sem esforço.'),
            ('<i>obsequium amīcōs, vēritās odium parit</i>', '<b>Zeugma</b> (no sentido amplo): <i>parit</i> serve aos dois membros. A frase fica curta como um provérbio, e o paralelismo destaca a oposição <i>amīcōs</i> / <i>odium</i>.'),
        ]),
        exercicio('Exercício 6 · Lírica e hino', 'Responda com base na seção 5.', [
            ('Quantas sílabas tem <i>Integer vītae scelerisque pūrus</i>, e qual é a quantidade da 4ª?', 'Onze: <i>in-te-ger-vī-tae-sce-le-ris-que-pū-rus</i>. A 4ª, <i>vī</i>, é longa, como Horácio sempre a faz no sáfico.'),
            ('Em <i>Maecēnās atavīs ēdite rēgibus</i>, onde fica a cesura e por que ela é fácil de achar?', 'Depois de <i>atavīs</i>, a 6ª sílaba. No asclepiadeu menor ela é fixa, e coincide com o fim de palavra e com o meio do verso.'),
            ('Por que <i>solvet saeclum in favilla</i> tem oito sílabas, e não sete?', 'Porque o verso rítmico medieval não faz elisão: <i>-clum in</i> conta duas sílabas (<i>sol-vet-sae-clum-in-fa-vil-la</i>). Num hexâmetro clássico, <i>saecl(um) in</i> se leria <i>sae-clin</i>, e <i>-clum in</i> se fundiria numa só sílaba.'),
            ('Que três traços do <i>Diēs īrae</i> mostram que ele não é um verso quantitativo?', 'O número fixo de sílabas (oito), a alternância regular de sílabas tônicas e átonas e a rima (<i>illa / favilla / Sibylla</i>).'),
        ]),
    ],
    leituras=['maro-aeneis-selecoes', 'naso-amores-liber-i', 'flaccus-carmina-et-epodi-odes-e-epodos', 'catullus-catulli-carmina', 'cicero-in-catilinam-i-iv', 'celano-dies-irae'],
    leituras_nota='Para treinar o hexâmetro, escanda em voz alta os primeiros versos das <i>Eneida</i> (seleções), sempre com um texto com macrons; dez versos por dia bastam para que o ouvido aprenda a cadência. Os <i>Amores</i> de Ovídio dão prática do dístico elegíaco; as <i>Odes</i> de Horácio e Catulo trazem o sáfico e o asclepiadeu, que você lerá no capítulo 45. Para as figuras, leia o primeiro parágrafo da <i>Primeira Catilinária</i>, que concentra anáfora, tricolon e perguntas retóricas. O <i>Dies irae</i> é o modelo do verso rítmico (capítulo 52).',
)
