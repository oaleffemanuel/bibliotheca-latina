"""Estrutura do livro digital Elementa Linguae Latinae (seção "Aprenda Latim"). Sumário editorial definitivo (2026-10-14).

Cada parte lista seus capítulos na ordem pedagógica. Campos de cada capítulo:
  titulo        título em português
  titulo_latim  título em latim (com macrons)
  nivel         'essencial' | 'intermediário' | 'avançado'
  pre           números dos capítulos pré-requisitos (numeração global, sempre menores que o próprio número)
  modulo        (opcional) módulo em conteudo/licoes/ quando o capítulo já foi escrito
Capítulos sem módulo aparecem no site como "em preparação". A justificativa do sumário está em conteudo/SUMARIO-EDITORIAL.md.
"""
TITULO = 'Elementa Linguae Latinae'
SUBTITULO = 'Um caminho progressivo para aprender a língua latina.'
NIVEIS = ('essencial', 'intermediário', 'avançado')

def c(lat, pt, nivel, pre=(), modulo=None):
    d = dict(titulo=pt, titulo_latim=lat, nivel=nivel, pre=list(pre))
    if modulo: d['modulo'] = modulo
    return d

PARTES = [
    dict(num=1, nome='Fundamenta', pt='Fundamentos',
         desc='O que é o latim, como se pronuncia e como uma frase latina funciona: os casos, as duas primeiras declinações, o presente do indicativo, o dicionário e o primeiro texto corrido.',
         licoes=[
             c('Dē linguā Latīnā', 'O que é o latim?', 'essencial', (), 'l01_o_que_e_o_latim'),
             c('Dē sententiā Latīnā', 'Como funciona uma frase latina?', 'essencial', (1,), 'l02_como_funciona_uma_frase_latina'),
             c('Dē cāsibus', 'Introdução aos casos gramaticais', 'essencial', (2,), 'l03_introducao_aos_casos'),
             c('Dē prīmā dēclīnātiōne', 'A primeira declinação', 'essencial', (3,), 'l04_a_primeira_declinacao'),
             c('Dē secundā dēclīnātiōne', 'A segunda declinação e os adjetivos de primeira classe', 'essencial', (4,), 'l05_a_segunda_declinacao'),
             c('Dē verbō: tempus praesēns', 'O presente do indicativo: esse e as quatro conjugações', 'essencial', (2,), 'l06_o_presente_do_indicativo'),
             c('Dē lexicō', 'Como usar o dicionário; o vocabulário básico', 'essencial', (5, 6), 'l07_como_usar_o_dicionario'),
             c('Prīma lēctiō', 'Da frase ao parágrafo: técnica de leitura e primeiro texto corrido', 'essencial', (7,), 'l08_da_frase_ao_paragrafo'),
         ]),
    dict(num=2, nome='Grammatica', pt='Gramática',
         desc='A morfologia completa e os usos dos casos: terceira, quarta e quinta declinações, os tempos do indicativo, os pronomes (inclusive o relativo), graus do adjetivo, numerais e a oração simples.',
         licoes=[
             c('Dē tertiā dēclīnātiōne (I)', 'A terceira declinação: temas consonantais', 'essencial', (5,), 'l09_a_terceira_declinacao_consonantal'),
             c('Dē tertiā dēclīnātiōne (II)', 'Temas em -i e adjetivos de segunda classe', 'essencial', (9,), 'l10_a_terceira_declinacao_temas_em_i'),
             c('Dē quārtā et quīntā dēclīnātiōne', 'Quarta e quinta declinações; quadro das cinco declinações', 'essencial', (10,), 'l11_a_quarta_e_a_quinta_declinacoes'),
             c('Dē imperfectō et futūrō', 'Imperfeito e futuro do indicativo', 'essencial', (6,), 'l12_o_imperfeito_e_o_futuro'),
             c('Dē perfectō', 'O perfeito e os tempos do perfectum; as partes principais do verbo', 'essencial', (12,), 'l13_o_perfeito_e_as_partes_principais'),
             c('Dē prōnōminibus persōnālibus', 'Pronomes pessoais, possessivos e reflexivos', 'essencial', (5,), 'l14_os_pronomes_pessoais'),
             c('Dē prōnōminibus dēmōnstrātīvīs', 'Demonstrativos; ipse e īdem', 'essencial', (14,), 'l15_os_demonstrativos'),
             c('Dē prōnōmine relātīvō', 'O pronome relativo e as orações relativas', 'essencial', (10, 15), 'l16_o_pronome_relativo'),
             c('Dē interrogātīvīs et indēfīnītīs', 'Interrogativos, indefinidos e a pergunta direta', 'intermediário', (16,), 'l17_interrogativos_e_indefinidos'),
             c('Dē gradibus comparātiōnis', 'Comparativos, superlativos e advérbios', 'intermediário', (10,), 'l18_comparativos_e_superlativos'),
             c('Dē numerīs, tempore et locō', 'Numerais; expressões de tempo e de lugar', 'intermediário', (11,), 'l19_numerais_tempo_e_lugar'),
             c('Dē genetīvō et datīvō', 'Usos do genitivo e do dativo', 'intermediário', (11,), 'l20_usos_do_genitivo_e_do_dativo'),
             c('Dē accūsātīvō et ablātīvō', 'Usos do acusativo e do ablativo', 'intermediário', (4, 11), 'l21_usos_do_acusativo_e_do_ablativo'),
             c('Dē imperātīvō et sententiā simplicī', 'Imperativo, vocativo e a sintaxe da oração simples', 'essencial', (13, 16), 'l22_imperativo_e_oracao_simples'),
         ]),
    dict(num=3, nome='Lectio', pt='Leitura',
         desc='As construções que abrem os textos autênticos: passiva, depoentes e irregulares, infinitivos e oração infinitiva, particípios e ablativo absoluto, gerúndio e gerundivo, subjuntivo e subordinadas, interrogativa indireta, condicionais, discurso indireto, o período, a métrica e a escrita em latim.',
         licoes=[
             c('Dē vōce passīvā', 'A voz passiva nos tempos do infectum', 'intermediário', (13, 21), 'l23_a_voz_passiva_infectum'),
             c('Dē passīvō perfectī', 'A passiva do perfectum e a passiva impessoal', 'intermediário', (23,), 'l24_a_passiva_do_perfectum'),
             c('Dē verbīs dēpōnentibus', 'Verbos depoentes e semidepoentes', 'intermediário', (24,), 'l25_verbos_depoentes'),
             c('Dē verbīs anōmalīs', 'Verbos irregulares: sum, possum, volō, nōlō, mālō, eō, ferō, fīō', 'intermediário', (13,), 'l26_verbos_irregulares'),
             c('Dē īnfīnītīvīs', 'Os infinitivos', 'intermediário', (24,), 'l27_os_infinitivos'),
             c('Accūsātīvus cum īnfīnītīvō', 'A oração infinitiva', 'intermediário', (14, 27), 'l28_a_oracao_infinitiva'),
             c('Dē participiīs', 'Os particípios', 'intermediário', (24,), 'l29_os_participios'),
             c('Ablātīvus absolūtus', 'O ablativo absoluto', 'intermediário', (21, 29), 'l30_o_ablativo_absoluto'),
             c('Dē gerundiō et gerundīvō', 'Gerúndio, gerundivo, perifrásticas e supino', 'intermediário', (29,), 'l31_gerundio_e_gerundivo'),
             c('Dē coniūnctīvō', 'O subjuntivo: formas e usos independentes', 'intermediário', (13,), 'l32_o_subjuntivo'),
             c('Ut et nē', 'Orações finais, consecutivas e completivas', 'intermediário', (32,), 'l33_oracoes_finais_e_consecutivas'),
             c('Cum et cōnsecūtiō temporum', 'Cum com subjuntivo e a sequência dos tempos', 'intermediário', (33,), 'l34_cum_e_sequencia_dos_tempos'),
             c('Dē interrogātiōne oblīquā', 'A interrogativa indireta', 'intermediário', (17, 34), 'l35_a_interrogativa_indireta'),
             c('Dē condiciōnibus', 'Orações condicionais', 'avançado', (34,), 'l36_oracoes_condicionais'),
             c('Dē causīs, concessiōnibus, comparātiōnibus', 'Orações causais, concessivas e comparativas', 'avançado', (34,), 'l37_causais_concessivas_comparativas'),
             c('Ōrātiō oblīqua', 'O discurso indireto', 'avançado', (28, 35), 'l38_o_discurso_indireto'),
             c('Dē periodō', 'O período complexo: como ler uma frase longa', 'avançado', (30, 38), 'l39_o_periodo_complexo'),
             c('Dē metrīs et figūrīs', 'Noções de métrica e figuras de linguagem', 'avançado', (8,), 'l40_metrica_e_figuras'),
             c('Dē compositiōne', 'Do latim lido ao latim escrito: composição e retroversão', 'avançado', (38,), 'l41_composicao_e_retroversao'),
         ]),
    dict(num=4, nome='Auctores', pt='Autores',
         desc='Leitura guiada de passagens autênticas, com contexto, análise gramatical e vocabulário: da fábula e da história à poesia clássica, e do latim cristão e medieval à escolástica.',
         licoes=[
             c('Phaedrus', 'Fedro: uma fábula', 'intermediário', (24,), 'l42_fedro'),
             c('Eutropius', 'Eutrópio: a fundação de Roma', 'intermediário', (22, 24), 'l43_eutropio'),
             c('Caesar', 'César: o início da Guerra da Gália', 'intermediário', (28, 30), 'l44_cesar'),
             c('Catullus et Horātius', 'Catulo e Horácio: dois poemas líricos', 'avançado', (32, 40), 'l45_catulo_e_horacio'),
             c('Ovidius', 'Ovídio: a criação do mundo (Metamorfoses I)', 'avançado', (30, 40), 'l46_ovidio'),
             c('Vergilius', 'Virgílio: a queda de Troia (Eneida II)', 'avançado', (46,), 'l47_virgilio'),
             c('Cicerō', 'Cícero: a Primeira Catilinária', 'avançado', (39,), 'l48_cicero'),
             c('Līvius', 'Tito Lívio: Rômulo e Remo (Ab urbe condita I)', 'avançado', (38,), 'l49_tito_livio'),
             c('Latīnitās Christiāna et mediaevālis', 'O latim cristão e medieval: o que muda', 'intermediário', (1, 22), 'l50_latim_cristao_e_medieval'),
             c('Biblia Vulgāta', 'A Vulgata: o Evangelho de Marcos', 'intermediário', (13, 50), 'l51_a_vulgata_marcos'),
             c('Hymnī', 'Dois hinos: Pange lingua e Dies irae', 'intermediário', (32, 50), 'l52_dois_hinos'),
             c('Augustīnus', 'Agostinho: as Confissões', 'avançado', (34, 51), 'l53_agostinho'),
             c('Thomās Aquīnās', 'Tomás de Aquino: um artigo da Summa', 'avançado', (35, 53), 'l54_tomas_de_aquino'),
         ]),
]
