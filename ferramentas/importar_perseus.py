#!/usr/bin/env python3
"""Importa textos latinos da Perseus Digital Library (repositório PerseusDL/canonical-latinLit, CC BY-SA 4.0)
para textos/<id>/texto.txt, numa versão fixa (commit) para que a importação seja reproduzível.

Uso: python3 ferramentas/importar_perseus.py [id ...]     (sem argumentos: todas as obras de OBRAS)

Formato de texto.txt (lido por ferramentas/construir.py):
  # Título           cabeçalho de 1º nível (livro, discurso)
  ## Título          cabeçalho de 2º nível (poema, fábula, episódio)
  > Nome             personagem que fala (diálogos em verso)
  ref<TAB>texto      parágrafo (prosa) ou verso (poesia); ref = capítulo ou número do verso
  {n}                dentro de um parágrafo: início da seção n
  linha em branco    separa estrofes / grupos
Regras de conversão (iguais para todas as obras, registradas em metadata.json → normalizacao):
  - notas (<note>) e variantes do aparato (<app>/<rdg>) são omitidas: são material editorial, não texto latino;
  - acréscimos do editor (<add>) entre ⟨ ⟩; supressões propostas pelo editor (<del>) entre [ ]; lacunas (<gap>) como * * *;
  - <choice>: usa a correção marcada pela Perseus (<corr>, erros de digitalização) e a abreviatura impressa (<abbr>);
  - <q> recebe aspas “ ” apenas quando o arquivo declara que as aspas foram retiradas (<quotation marks="none">);
    <q rend="merge"> continua a citação do verso anterior: abre-se uma vez e fecha-se no último verso da fala;
  - nada mais é alterado: grafia, maiúsculas, u/v, pontuação e ordem são as da edição.
"""
import html, json, os, re, subprocess, sys
from xml.etree import ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMIT = '128a05afa9cc7179ab18f8d05f78a9f1dd50e415'   # PerseusDL/canonical-latinLit, master em 2026-10-18
RAW = 'https://raw.githubusercontent.com/PerseusDL/canonical-latinLit/{c}/data/{p}'
BLOB = 'https://github.com/PerseusDL/canonical-latinLit/blob/{c}/data/{p}'
CACHE = os.path.join(os.environ.get('TMPDIR', '/tmp'), 'bibliotheca-latina-perseus')
T = '{http://www.tei-c.org/ns/1.0}'

# id do catálogo → arquivo TEI, forma, e como achar livros/capítulos
OBRAS = {
    'phaedrus-fabulae-aesopiae': dict(tei='phi0975/phi001/phi0975.phi001.perseus-lat2.xml', forma='verso'),
    'caesar-commentarii-de-bello-gallico-texto-integral': dict(tei='phi0448/phi001/phi0448.phi001.perseus-lat2.xml', forma='prosa', livro='Liber'),
    'cicero-in-catilinam-i-iv': dict(tei='phi0474/phi013/phi0474.phi013.perseus-lat2.xml', forma='prosa'),
    'cicero-laelius-de-amicitia': dict(tei='phi0474/phi052/phi0474.phi052.perseus-lat2.xml', forma='prosa'),
    'cicero-cato-maior-de-senectute': dict(tei='phi0474/phi051/phi0474.phi051.perseus-lat2.xml', forma='prosa'),
    'crispus-bellum-catilinae': dict(tei='phi0631/phi001/phi0631.phi001.perseus-lat3.xml', forma='prosa', cap_marcos=True),
    'livius-ab-urbe-condita-liber-i': dict(tei='phi0914/phi001/phi0914.phi001.perseus-lat2.xml', forma='prosa', so_livro='1'),
    'maro-bucolica-eclogae': dict(tei='phi0690/phi001/phi0690.phi001.perseus-lat2.xml', forma='verso'),
    'maro-aeneis-texto-integral': dict(tei='phi0690/phi003/phi0690.phi003.perseus-lat2.xml', forma='verso', livro='Liber'),
    'naso-metamorphoses-texto-integral': dict(tei='phi0959/phi006/phi0959.phi006.perseus-lat2.xml', forma='verso', livro='Liber', episodios=True),
}
# Edição-fonte de cada arquivo TEI (lida no <sourceDesc> do próprio arquivo) e data de morte do editor,
# conferida em 2026-10-18 (Wikidata / Wikipédia). Lei 9.610/98, art. 41: domínio público no Brasil a partir de
# 1º de janeiro do ano seguinte aos 70 anos da morte; nos EUA, obras publicadas até 1930 estão em domínio público.
EDICOES = {
    'phaedrus-fabulae-aesopiae': dict(titulo_latino='Fabulae Aesopiae', editor='Lucian Mueller', edicao='Phaedri Fabulae Aesopiae', local='Leipzig', editora='B. G. Teubner', ano='1876', morte=1898, fonte_morte='https://www.wikidata.org/wiki/Q71344'),
    'caesar-commentarii-de-bello-gallico-texto-integral': dict(titulo_latino='Commentarii de bello Gallico (com o livro VIII de A. Hírcio)', editor='T. Rice Holmes', edicao='C. Iuli Commentarii Rerum in Gallia Gestarum VII, A. Hirti Commentarius VIII', local='Oxford', editora='Clarendon Press (Scriptorum Classicorum Bibliotheca Oxoniensis)', ano='1914', morte=1933, fonte_morte='https://www.wikidata.org/wiki/Q7668644'),
    'cicero-in-catilinam-i-iv': dict(titulo_latino='In L. Catilinam orationes IV', editor='Albert Curtis Clark', edicao='M. Tulli Ciceronis Orationes, vol. 1', local='Oxford', editora='Clarendon Press (Oxford Classical Texts)', ano='1908', morte=1937, fonte_morte='https://www.wikidata.org/wiki/Q2637776'),
    'cicero-laelius-de-amicitia': dict(titulo_latino='Laelius de amicitia', editor='William Armistead Falconer', edicao='Cicero, De Senectute, De Amicitia, De Divinatione (Loeb Classical Library)', local='Londres / Nova York', editora='William Heinemann / G. P. Putnam’s Sons', ano='1923', morte=1927, fonte_morte='https://www.wikidata.org/wiki/Q93268573'),
    'cicero-cato-maior-de-senectute': dict(titulo_latino='Cato Maior de senectute', editor='William Armistead Falconer', edicao='Cicero, De Senectute, De Amicitia, De Divinatione (Loeb Classical Library)', local='Londres / Nova York', editora='William Heinemann / G. P. Putnam’s Sons', ano='1923', morte=1927, fonte_morte='https://www.wikidata.org/wiki/Q93268573'),
    'crispus-bellum-catilinae': dict(titulo_latino='Bellum Catilinae (De Catilinae coniuratione)', editor='Axel W. Ahlberg', edicao='C. Sallusti Crispi Catilina, Iugurtha, Orationes et epistulae excerptae de Historiis', local='Leipzig', editora='B. G. Teubner', ano='1919', morte=1951, fonte_morte='https://www.wikidata.org/wiki/Q5543810'),
    'livius-ab-urbe-condita-liber-i': dict(titulo_latino='Ab urbe condita, liber I', editor='Wilhelm Weissenborn e Hermann Johannes Müller', edicao='Titi Livi Ab urbe condita libri', local='Leipzig', editora='B. G. Teubner', ano='1884–1911', morte=1912, fonte_morte='https://www.wikidata.org/wiki/Q18932954 (H. J. Müller, †1912); https://www.wikidata.org/wiki/Q2575612 (W. Weissenborn, †1878)'),
    'maro-bucolica-eclogae': dict(titulo_latino='Bucolica (Eclogae)', editor='J. B. Greenough', edicao='The Bucolics, Aeneid, and Georgics of Virgil', local='Boston', editora='Ginn and Company', ano='1881', morte=1901, fonte_morte='https://www.wikidata.org/wiki/Q6129112'),
    'maro-aeneis-texto-integral': dict(titulo_latino='Aeneis', editor='J. B. Greenough', edicao='The Bucolics, Aeneid, and Georgics of Virgil', local='Boston', editora='Ginn and Company', ano='1881', morte=1901, fonte_morte='https://www.wikidata.org/wiki/Q6129112'),
    'naso-metamorphoses-texto-integral': dict(titulo_latino='Metamorphoses', editor='Hugo Magnus', edicao='P. Ovidi Nasonis Metamorphoseon libri XV', local='Gotha', editora='F. A. Perthes', ano='1892', morte=1924, fonte_morte='https://de.wikipedia.org/wiki/Hugo_Magnus_(Philologe)'),
}
# ───── segundo lote (2026-10-18) ─────
def _pl(n): return f'phi0119/phi{n:03d}/phi0119.phi{n:03d}.perseus-lat2.xml'
OBRAS.update({
    'catullus-catulli-carmina': dict(tei='phi0472/phi001/phi0472.phi001.perseus-lat2.xml', forma='verso'),
    'flaccus-carmina-et-epodi-odes-e-epodos': dict(tei=['phi0893/phi001/phi0893.phi001.perseus-lat2.xml', 'phi0893/phi002/phi0893.phi002.perseus-lat2.xml', 'phi0893/phi003/phi0893.phi003.perseus-lat2.xml'],
                                                   forma='verso', titulos=['Carmina', 'Carmen saeculare', 'Epodi'], unidade='obra'),
    'nepos-de-viris-illustribus-vitae': dict(tei=[f'phi0588/abo{n:03d}/phi0588.abo{n:03d}.perseus-lat2.xml' for n in range(1, 26)], forma='prosa', unidade='vida'),
    'tacitus-agricola': dict(tei='phi1351/phi001/phi1351.phi001.perseus-lat2.xml', forma='prosa'),
    'naso-amores-liber-i': dict(tei='phi0959/phi001/phi0959.phi001.perseus-lat2.xml', forma='verso', so_livro='1'),
    'cicero-de-officiis-latim-e-ingles': dict(tei='phi0474/phi055/phi0474.phi055.perseus-lat2.xml', forma='prosa'),
    'cicero-somnium-scipionis-de-re-publica-vi': dict(tei='phi0474/phi043/phi0474.phi043.perseus-lat2.xml', forma='prosa', so_livro='6'),
    'maro-georgica': dict(tei='phi0690/phi002/phi0690.phi002.perseus-lat2.xml', forma='verso', livro='Liber'),
    'caesar-commentarii-de-bello-civili': dict(tei='phi0448/phi002/phi0448.phi002.perseus-lat2.xml', forma='prosa', restaurar_capitulos=True),
    'crispus-bellum-iugurthinum': dict(tei='phi0631/phi002/phi0631.phi002.perseus-lat3.xml', forma='prosa', cap_marcos=True),
    'tacitus-germania': dict(tei='phi1351/phi002/phi1351.phi002.perseus-lat1.xml', forma='prosa'),
    'tacitus-annales': dict(tei='phi1351/phi005/phi1351.phi005.perseus-lat1.xml', forma='prosa', cap_marcos=True),
    'tranquillus-de-vita-caesarum': dict(tei=[f'phi1348/abo{n:03d}/phi1348.abo{n:03d}.perseus-lat2.xml' for n in range(11, 23)], forma='prosa', unidade='vida',
                                         titulos=['Divus Iulius', 'Divus Augustus', 'Tiberius', 'Gaius Caligula', 'Divus Claudius', 'Nero', 'Galba', 'Otho', 'Vitellius', 'Divus Vespasianus', 'Divus Titus', 'Domitianus']),
    'cicero-pro-archia-poeta': dict(tei='phi0474/phi016/phi0474.phi016.perseus-lat2.xml', forma='prosa'),
    'cicero-pro-milone': dict(tei='phi0474/phi031/phi0474.phi031.perseus-lat2.xml', forma='prosa'),
    'cicero-pro-caelio': dict(tei='phi0474/phi024/phi0474.phi024.perseus-lat2.xml', forma='prosa'),
    'cicero-philippicae': dict(tei='phi0474/phi035/phi0474.phi035.perseus-lat2.xml', forma='prosa'),
    'cicero-de-natura-deorum': dict(tei='phi0474/phi050/phi0474.phi050.perseus-lat2.xml', forma='prosa'),
    'cicero-de-oratore': dict(tei='phi0474/phi037/phi0474.phi037.perseus-lat2.xml', forma='prosa'),
    'cicero-de-finibus-bonorum-et-malorum': dict(tei='phi0474/phi048/phi0474.phi048.perseus-lat2.xml', forma='prosa'),
    'cicero-epistulae-ad-familiares': dict(tei='phi0474/phi056/phi0474.phi056.perseus-lat2.xml', forma='prosa'),
    'cicero-epistulae-ad-atticum': dict(tei='phi0474/phi057/phi0474.phi057.perseus-lat2.xml', forma='prosa'),
    'terentius-comoediae': dict(tei=[f'phi0134/phi{n:03d}/phi0134.phi{n:03d}.perseus-lat2.xml' for n in range(1, 7)], forma='verso', unidade='comédia',
                                titulos=['Andria', 'Heauton timorumenos', 'Eunuchus', 'Phormio', 'Hecyra', 'Adelphoe']),
    'plautus-amphitruo': dict(tei=_pl(1), forma='verso'), 'plautus-aulularia': dict(tei=_pl(3), forma='verso'),
    'plautus-captivi': dict(tei=_pl(5), forma='verso'), 'plautus-menaechmi': dict(tei=_pl(10), forma='verso'),
    'plautus-miles-gloriosus': dict(tei=_pl(12), forma='verso'), 'plautus-mostellaria': dict(tei=_pl(13), forma='verso'),
    'naso-heroides': dict(tei='phi0959/phi002/phi0959.phi002.perseus-lat2.xml', forma='verso'),
    'tibullus-elegiae': dict(tei='phi0660/phi001/phi0660.phi001.perseus-lat2.xml', forma='verso'),
    'iuvenalis-saturae': dict(tei='phi1276/phi001/phi1276.phi001.perseus-lat2.xml', forma='verso'),
    'persius-saturae': dict(tei='phi0969/phi001/phi0969.phi001.perseus-lat2.xml', forma='verso'),
    'lucanus-pharsalia': dict(tei='phi0917/phi001/phi0917.phi001.perseus-lat2.xml', forma='verso'),
    'petronius-satyricon': dict(tei='phi0972/phi001/phi0972.phi001.perseus-lat2.xml', forma='prosa'),
    'apuleius-metamorphoses': dict(tei='phi1212/phi002/phi1212.phi002.perseus-lat1.xml', forma='prosa'),
    'seneca-tragoediae': dict(tei=[f'phi1017/phi{n:03d}/phi1017.phi{n:03d}.perseus-lat2.xml' for n in range(1, 11)], forma='verso', unidade='tragédia',
                              titulos=['Hercules furens', 'Troades', 'Phoenissae', 'Medea', 'Phaedra', 'Oedipus', 'Agamemnon', 'Thyestes', 'Hercules Oetaeus', 'Octavia']),
    'seneca-apocolocyntosis': dict(tei='phi1017/phi011/phi1017.phi011.perseus-lat2.xml', forma='prosa'),
    'gellius-noctes-atticae': dict(tei='phi1254/phi001/phi1254.phi001.perseus-lat2.xml', forma='prosa', ictus_dup=True),
    'curtius-historiae-alexandri-magni': dict(tei='phi0860/phi001/phi0860.phi001.perseus-lat2.xml', forma='prosa'),
    'maximus-facta-et-dicta-memorabilia': dict(tei='phi1038/phi001/phi1038.phi001.perseus-lat1.xml', forma='prosa'),
    'florus-epitome-rerum-romanorum': dict(tei='phi1242/phi001/phi1242.phi001.perseus-lat1.xml', forma='prosa'),
    'vitruvius-de-architectura': dict(tei='phi1056/phi001/phi1056.phi001.perseus-lat2.xml', forma='prosa'),
    'flaccus-sermones-epistulae-ars-poetica': dict(tei=['phi0893/phi004/phi0893.phi004.perseus-lat2.xml', 'phi0893/phi005/phi0893.phi005.perseus-lat2.xml', 'phi0893/phi006/phi0893.phi006.perseus-lat2.xml'],
                                                   forma='verso', titulos=['Sermones', 'Epistulae', 'Ars poetica (Epistula ad Pisones)'], unidade='obra'),
    'ausonius-mosella': dict(tei='stoa0045/stoa019/stoa0045.stoa019.perseus-lat2.xml', forma='verso'),
    'cicero-commentariolum-petitionis': dict(tei='phi0478/phi003/phi0478.phi003.perseus-lat2.xml', forma='prosa'),
})
WD = 'https://www.wikidata.org/wiki/'
def _ed(editor, edicao, local, editora, ano, morte, fonte, partes=None):
    d = dict(editor=editor, edicao=edicao, local=local, editora=editora, ano=ano, morte=morte, fonte_morte=fonte)
    if partes: d['partes'] = partes
    return d
CLARK = lambda ano, vol: _ed('Albert Curtis Clark', f'M. Tulli Ciceronis Orationes, vol. {vol} (Oxford Classical Texts)', 'Oxford', 'Clarendon Press', ano, 1937, WD + 'Q2637776')
LEO = lambda ano, vol: _ed('Friedrich Leo', f'Plauti Comoediae, vol. {vol}', 'Berlim', 'Weidmann', ano, 1914, WD + 'Q71353')
EDICOES.update({
    'catullus-catulli-carmina': dict(titulo_latino='Carmina', edicoes=[_ed('Elmer Truesdell Merrill', 'Catullus', 'Boston', 'Ginn and Company', '1893', 1936, WD + 'Q5366688')]),
    'flaccus-carmina-et-epodi-odes-e-epodos': dict(titulo_latino='Carmina, Carmen saeculare, Epodi', edicoes=[
        _ed('Paul Shorey e Gordon J. Laing', 'Horace, Odes and Epodes', 'Chicago', 'Benj. H. Sanborn and Co.', '1919', 1945, WD + 'Q1760571 (Shorey, †1934); ' + WD + 'Q1538040 (Laing, †1945)', 'Carmina e Carmen saeculare'),
        _ed('Friedrich Vollmer', 'Q. Horati Flacci Carmina', 'Leipzig', 'Teubner', '1912', 1923, WD + 'Q1460274', 'Epodi')]),
    'nepos-de-viris-illustribus-vitae': dict(titulo_latino='Vitae (De viris illustribus)', edicoes=[_ed('Alfred Fleckeisen e Karl Halm', 'Cornelii Nepotis Vitae', 'Leipzig', 'Teubner', '1886', 1899, WD + 'Q84805 (Fleckeisen, †1899); ' + WD + 'Q96389 (Halm, †1882)')]),
    'tacitus-agricola': dict(titulo_latino='De vita Iulii Agricolae', edicoes=[_ed('Henry Furneaux', 'Cornelii Taciti Opera minora (Oxford Classical Texts)', 'Oxford', 'Clarendon Press', '1900', 1900, WD + 'Q14945582')]),
    'naso-amores-liber-i': dict(titulo_latino='Amores, liber I', edicoes=[_ed('Rudolf Ehwald', 'P. Ovidius Naso, vol. 1: Amores, Epistulae, Medicamina faciei femineae, Ars amatoria, Remedia amoris', 'Leipzig', 'B. G. Teubner', '1907', 1927, WD + 'Q2172569')]),
    'cicero-de-officiis-latim-e-ingles': dict(titulo_latino='De officiis', edicoes=[_ed('Walter Miller', 'Cicero, De Officiis (Loeb Classical Library)', 'Londres / Nova York', 'William Heinemann / G. P. Putnam’s Sons', '1913', 1949, WD + 'Q7965639')],
                                              omitido_extra=['tradução inglesa da edição bilíngue']),
    'cicero-somnium-scipionis-de-re-publica-vi': dict(titulo_latino='De re publica, liber VI (Somnium Scipionis)', edicoes=[_ed('Carl Friedrich Wilhelm Müller', 'M. Tulli Ciceronis librorum de re publica sex', 'Leipzig', 'Teubner', '1889', 1903, WD + 'Q1038116')]),
    'maro-georgica': dict(titulo_latino='Georgica', edicoes=[_ed('J. B. Greenough', 'The Bucolics, Aeneid, and Georgics of Virgil', 'Boston', 'Ginn and Company', '1881', 1901, WD + 'Q6129112')]),
    'caesar-commentarii-de-bello-civili': dict(titulo_latino='Commentarii de bello civili', edicoes=[_ed('René du Pontet', 'C. Iuli Caesaris Commentariorum pars posterior (Oxford Classical Texts)', 'Oxford', 'Clarendon Press', '1901', 1948, WD + 'Q99857272')]),
    'crispus-bellum-iugurthinum': dict(titulo_latino='Bellum Iugurthinum', edicoes=[_ed('Axel W. Ahlberg', 'C. Sallusti Crispi Catilina, Iugurtha, Orationes et epistulae excerptae de Historiis', 'Leipzig', 'Teubner', '1919', 1951, WD + 'Q5543810')]),
    'tacitus-germania': dict(titulo_latino='De origine et situ Germanorum (Germania)', edicoes=[_ed('Henry Furneaux', 'Cornelii Taciti Opera minora (Oxford Classical Texts)', 'Oxford', 'Clarendon Press', '1900', 1900, WD + 'Q14945582')]),
    'tacitus-annales': dict(titulo_latino='Annales (Ab excessu divi Augusti)', edicoes=[_ed('Charles Dennis Fisher', 'Cornelii Taciti Annalium ab excessu divi Augusti libri (Oxford Classical Texts)', 'Oxford', 'Clarendon Press', '1906', 1916, WD + 'Q5076828')]),
    'tranquillus-de-vita-caesarum': dict(titulo_latino='De vita Caesarum', edicoes=[_ed('Maximilian Ihm', 'C. Suetoni Tranquilli De vita Caesarum libri VIII', 'Leipzig', 'Teubner', '1908', 1909, WD + 'Q1454372')]),
    'cicero-pro-archia-poeta': dict(titulo_latino='Pro A. Licinio Archia poeta', edicoes=[CLARK('1911', 6)]),
    'cicero-pro-milone': dict(titulo_latino='Pro T. Annio Milone', edicoes=[CLARK('1918', 2)]),
    'cicero-pro-caelio': dict(titulo_latino='Pro M. Caelio', edicoes=[CLARK('1908', 1)]),
    'cicero-philippicae': dict(titulo_latino='Philippicae (In M. Antonium orationes)', edicoes=[CLARK('1918', 2)]),
    'cicero-de-natura-deorum': dict(titulo_latino='De natura deorum', edicoes=[_ed('Otto Plasberg', 'M. Tulli Ciceronis scripta quae manserunt omnia, fasc. 45: De natura deorum', 'Leipzig', 'Teubner', '1917', 1924, WD + 'Q1519749')]),
    'cicero-de-oratore': dict(titulo_latino='De oratore', edicoes=[_ed('Augustus Samuel Wilkins', 'M. Tulli Ciceronis Rhetorica, vol. 1 (Oxford Classical Texts)', 'Oxford', 'Clarendon Press', '1902', 1905, WD + 'Q16943919')]),
    'cicero-de-finibus-bonorum-et-malorum': dict(titulo_latino='De finibus bonorum et malorum', edicoes=[_ed('Theodor Schiche', 'M. Tulli Ciceronis scripta quae manserunt omnia, fasc. 43: De finibus bonorum et malorum', 'Leipzig', 'Teubner', '1915', 1950, WD + 'Q93233907')]),
    'cicero-epistulae-ad-familiares': dict(titulo_latino='Epistulae ad familiares', edicoes=[_ed('Louis Claude Purser', 'M. Tulli Ciceronis Epistulae, vol. 1: Epistulae ad familiares (Oxford Classical Texts)', 'Oxford', 'Clarendon Press', '1901', 1932, WD + 'Q6686912')], omitido_extra=['datas de redação propostas pelo editor (Scr. ...)']),
    'cicero-epistulae-ad-atticum': dict(titulo_latino='Epistulae ad Atticum', edicoes=[_ed('Louis Claude Purser', 'M. Tulli Ciceronis Epistulae, vol. 2: Epistulae ad Atticum (Oxford Classical Texts)', 'Oxford', 'Clarendon Press', '1903', 1932, WD + 'Q6686912')], omitido_extra=['datas de redação propostas pelo editor (Scr. ...)']),
    'terentius-comoediae': dict(titulo_latino='Comoediae (Andria, Heauton timorumenos, Eunuchus, Phormio, Hecyra, Adelphoe)', omitido_extra=['listas de personagens (dramatis personae) da edição'], edicoes=[_ed('Edward St. John Parry', 'Publii Terentii Comoediae sex', 'Londres', 'Whitaker and Co. / George Bell', '1857', None,
        'sem registro no Wikidata; editor de livro publicado em 1857, portanto necessariamente falecido muito antes de 1956')]),
    'plautus-amphitruo': dict(titulo_latino='Amphitruo', edicoes=[LEO('1895', 1)]), 'plautus-aulularia': dict(titulo_latino='Aulularia', edicoes=[LEO('1895', 1)]),
    'plautus-captivi': dict(titulo_latino='Captivi', edicoes=[LEO('1895', 1)]), 'plautus-menaechmi': dict(titulo_latino='Menaechmi', edicoes=[LEO('1895', 1)]),
    'plautus-miles-gloriosus': dict(titulo_latino='Miles gloriosus', edicoes=[LEO('1896', 2)]), 'plautus-mostellaria': dict(titulo_latino='Mostellaria', edicoes=[LEO('1896', 2)]),
    'naso-heroides': dict(titulo_latino='Heroides (Epistulae heroidum)', edicoes=[_ed('Rudolf Ehwald', 'P. Ovidius Naso, vol. 1: Amores, Epistulae, Medicamina faciei femineae, Ars amatoria, Remedia amoris', 'Leipzig', 'B. G. Teubner', '1907', 1927, WD + 'Q2172569')]),
    'tibullus-elegiae': dict(titulo_latino='Elegiae (com o livro III do Corpus Tibullianum)', edicoes=[_ed('J. P. Postgate', 'Tibulli aliorumque carminum libri tres (Oxford Classical Texts)', 'Oxford', 'Clarendon Press', '1915', 1926, WD + 'Q3805133')]),
    'iuvenalis-saturae': dict(titulo_latino='Saturae', edicoes=[_ed('G. G. Ramsay', 'Juvenal and Persius (Loeb Classical Library)', 'Londres / Nova York', 'William Heinemann / G. P. Putnam’s Sons', '1918', 1921, WD + 'Q15980942')], omitido_extra=['tradução inglesa da edição bilíngue']),
    'persius-saturae': dict(titulo_latino='Saturae', edicoes=[_ed('G. G. Ramsay', 'Juvenal and Persius (Loeb Classical Library)', 'Londres / Nova York', 'William Heinemann / G. P. Putnam’s Sons', '1918', 1921, WD + 'Q15980942')], omitido_extra=['tradução inglesa da edição bilíngue']),
    'lucanus-pharsalia': dict(titulo_latino='Pharsalia (Bellum civile)', edicoes=[_ed('Karl Hermann Weise', 'M. Annaei Lucani Pharsaliae libri X', 'Leipzig', 'G. Basse', '1835', None, WD + 'Q21544592 (nascido em 1787; data de morte não registrada; necessariamente falecido muito antes de 1956)')]),
    'petronius-satyricon': dict(titulo_latino='Satyricon', edicoes=[_ed('Michael Heseltine', 'Petronius (Loeb Classical Library)', 'Londres / Nova York', 'William Heinemann / G. P. Putnam’s Sons', '1913', 1952, WD + 'Q90025266; https://en.wikipedia.org/wiki/Michael_Heseltine_(civil_servant)')], omitido_extra=['tradução inglesa da edição bilíngue']),
    'apuleius-metamorphoses': dict(titulo_latino='Metamorphoses (Asinus aureus)', edicoes=[_ed('Stephen Gaselee', 'The Golden Ass, being the Metamorphoses of Lucius Apuleius (Loeb Classical Library)', 'Londres / Nova York', 'William Heinemann / G. P. Putnam’s Sons', '1915', 1943, WD + 'Q7609298')], omitido_extra=['tradução inglesa (de W. Adlington, revista) da edição bilíngue']),
    'seneca-tragoediae': dict(titulo_latino='Tragoediae', edicoes=[_ed('Rudolf Peiper e Gustav Richter', 'L. Annaei Senecae Tragoediae', 'Leipzig', 'Teubner', '1921 (reimpressão; 1ª ed. 1867)', None,
        WD + 'Q15843261 (Peiper, †1898); G. Richter: coeditor desde a 1ª edição (1867), necessariamente falecido muito antes de 1956')]),
    'seneca-apocolocyntosis': dict(titulo_latino='Apocolocyntosis (Ludus de morte Claudii)', edicoes=[_ed('W. H. D. Rouse (com M. Heseltine)', 'Petronius; Seneca, Apocolocyntosis (Loeb Classical Library)', 'Londres / Nova York', 'William Heinemann / G. P. Putnam’s Sons', '1913', 1952, WD + 'Q7945630 (Rouse, †1950); ' + WD + 'Q90025266 (Heseltine, †1952)')], omitido_extra=['tradução inglesa da edição bilíngue']),
    'gellius-noctes-atticae': dict(titulo_latino='Noctes Atticae', edicoes=[_ed('John C. Rolfe', 'The Attic Nights of Aulus Gellius (Loeb Classical Library)', 'Cambridge, Mass. / Londres', 'Harvard University Press / William Heinemann', '1927', 1943, WD + 'Q6225114')], omitido_extra=['tradução inglesa da edição bilíngue']),
    'curtius-historiae-alexandri-magni': dict(titulo_latino='Historiae Alexandri Magni Macedonis', edicoes=[_ed('Edmund Hedicke', 'Q. Curti Rufi Historiarum Alexandri Magni Macedonis libri qui supersunt', 'Leipzig', 'Teubner', '1908', None, WD + 'Q1286408 (nascido em 1840; a data de morte registrada no Wikidata não é confiável; necessariamente falecido muito antes de 1956)')]),
    'maximus-facta-et-dicta-memorabilia': dict(titulo_latino='Facta et dicta memorabilia', edicoes=[_ed('Karl Friedrich Kempf', 'Valerii Maximi Factorum et dictorum memorabilium libri novem', 'Leipzig', 'Teubner', '1888', 1894, WD + 'Q21544470')]),
    'florus-epitome-rerum-romanorum': dict(titulo_latino='Epitome rerum Romanarum', edicoes=[_ed('Edward Seymour Forster', 'Lucius Annaeus Florus, Epitome of Roman History (Loeb Classical Library)', 'Londres / Nova York', 'William Heinemann / G. P. Putnam’s Sons', '1929', 1950, WD + 'Q18910558')], omitido_extra=['tradução inglesa da edição bilíngue']),
    'vitruvius-de-architectura': dict(titulo_latino='De architectura', edicoes=[_ed('Fritz Krohn', 'Vitruvii De architectura libri decem', 'Leipzig', 'B. G. Teubner', '1912', 1941, WD + 'Q15436493')]),
    'flaccus-sermones-epistulae-ars-poetica': dict(titulo_latino='Sermones, Epistulae, Ars poetica', edicoes=[
        _ed('Christopher Smart (texto latino da edição)', 'The Works of Horace, vol. 2', 'Filadélfia', 'Joseph Whetham', '1836', 1771, 'https://en.wikipedia.org/wiki/Christopher_Smart', 'Sermones e Ars poetica'),
        _ed('H. Rushton Fairclough', 'Horace, Satires, Epistles and Ars Poetica (Loeb Classical Library)', 'Londres / Cambridge, Mass.', 'William Heinemann / Harvard University Press', '1929', 1938, WD + 'Q18745992', 'Epistulae')], omitido_extra=['traduções inglesas das edições']),
    'ausonius-mosella': dict(titulo_latino='Mosella', edicoes=[_ed('Hugh G. Evelyn-White', 'Ausonius, vol. 1 (Loeb Classical Library)', 'Londres / Cambridge, Mass.', 'William Heinemann / Harvard University Press', '1919', 1924, WD + 'Q18912247')], omitido_extra=['tradução inglesa da edição bilíngue']),
    'cicero-commentariolum-petitionis': dict(titulo_latino='Commentariolum petitionis', obra_nota='Obra antiga atribuída a Quinto Túlio Cícero; em domínio público.',
        edicoes=[_ed('Louis Claude Purser', 'M. Tulli Ciceronis Epistulae, vol. 3 (Oxford Classical Texts)', 'Oxford', 'Clarendon Press', '1902', 1932, WD + 'Q6686912')]),
})

VERIFICADO = '2026-10-18'

def edicoes_de(id_):
    e = EDICOES[id_]
    if 'edicoes' in e: return e['edicoes']
    return [{k: e.get(k) for k in ('editor', 'edicao', 'local', 'editora', 'ano', 'morte', 'fonte_morte')}]

def metadados(id_, cfg, raws, aspas, correcoes):
    e = EDICOES[id_]; eds = edicoes_de(id_)
    teis = cfg['tei'] if isinstance(cfg['tei'], list) else [cfg['tei']]
    decls = set()
    for raw in raws:
        av = re.search(r'<availability[^>]*>(.*?)</availability>', raw, re.S)
        decls.add(ws(re.sub('<[^>]+>', ' ', av.group(1))) if av else '')
    geral = 'vale a licença geral do repositório: “Unless otherwise indicated, all contents of this repository are licensed under a Creative Commons Attribution-ShareAlike 4.0 International License” (README e LICENSE do repositório).'
    if decls == {''}: decl = 'Sem declaração no arquivo; ' + geral
    elif '' in decls: decl = 'Parte dos arquivos declara “' + next(d for d in decls if d) + '”; nos demais, ' + geral
    else: decl = ' / '.join(sorted(decls))
    norm = ['Notas do editor e variantes do aparato crítico omitidas (material editorial, não texto latino).',
            'Acréscimos do editor entre ⟨ ⟩, supressões propostas pelo editor entre [ ], lacunas como * * *, como na edição impressa.',
            'Correções de digitalização marcadas pela Perseus (<choice>/<corr>) aplicadas; abreviaturas mantidas como impressas.',
            'Grafia, maiúsculas, u/v, pontuação e ordem do texto mantidas como na edição; nenhuma modernização.',
            'Espaços e quebras de linha do arquivo XML normalizados; numeração de livros, capítulos, seções e versos preservada.']
    if cfg['forma'] == 'prosa' and any('<l>' in r or '<l ' in r for r in raws):
        norm.append('Versos citados dentro da prosa aparecem na mesma linha, separados por “ / ”.')
    if aspas: norm.append('Aspas “ ” recolocadas onde a Perseus codificou citações como <q> e declarou ter retirado as aspas (<quotation marks="none">); falas de vários versos (<q rend="merge">) recebem uma só abertura e um só fechamento.')
    if cfg.get('episodios'): norm.append('Títulos de episódio: os da edição de Magnus (marcos ed="Magnus"); títulos em inglês de outra fonte omitidos.')
    if cfg.get('so_livro'): norm.append(f'Só o livro {cfg["so_livro"]} (o catálogo trata deste livro).' + (' As periochae (resumos tardios) omitidas.' if 'phi0914' in teis[0] else ''))
    if len(teis) > 1: norm.append(f'Reúne {len(teis)} arquivos TEI da Perseus (um por {cfg.get("unidade", "parte")}), na ordem da edição.')
    norm += [c[0].upper() + c[1:] + '.' for c in correcoes]
    def ed_txt(x): return f'{x["edicao"]}, ed. {x["editor"]} ({x["local"]}: {x["editora"]}, {x["ano"]})' + (f' [{x["partes"]}]' if x.get('partes') else '')
    conhecidas = [x['morte'] for x in eds if x.get('morte')]
    morte = max(conhecidas) if conhecidas else None
    def m_txt(x): return f'†{x["morte"]}' if x.get('morte') else 'data de morte não localizada'
    if morte is None: dir_br = 'Domínio público no Brasil: ' + '; '.join(x['fonte_morte'] for x in eds)
    elif any(not x.get('morte') for x in eds): dir_br = f'Domínio público no Brasil (morte conhecida mais recente: {morte}; para os demais: ' + '; '.join(x['fonte_morte'] for x in eds if not x.get('morte')) + ')'
    elif len(eds) > 1 or ' e ' in eds[0]['editor']: dir_br = f'Domínio público no Brasil (editores falecidos até {morte})'
    else: dir_br = f'Domínio público no Brasil (editor falecido em {morte})'
    return {
        'id': id_, 'titulo_latino': e['titulo_latino'], 'forma': cfg['forma'],
        'edicoes': [{k: x[k] for k in ('editor', 'edicao', 'local', 'editora', 'ano', 'partes') if x.get(k)} for x in eds],
        'transcricao': {'nome': 'Perseus Digital Library (Tufts University), repositório PerseusDL/canonical-latinLit',
                        'arquivos': [BLOB.format(c=COMMIT, p=t) for t in teis], 'commit': COMMIT, 'acessado_em': VERIFICADO},
        'licenca': {'nome': 'CC BY-SA 4.0', 'url': 'https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br', 'declaracao': decl},
        'atribuicao': 'Texto latino: ' + '; '.join(ed_txt(x) for x in eds) + '. Transcrição digital: Perseus Digital Library, Tufts University (PerseusDL/canonical-latinLit), CC BY-SA 4.0. Adaptação de formato (texto, PDF, EPUB) pela Bibliotheca Latina, distribuída sob a mesma licença CC BY-SA 4.0.',
        'auditoria': {
            '1_autor_e_obra': e.get('obra_nota', 'Autor antigo; obra em domínio público.'),
            '2_edicao_fonte': '; '.join(ed_txt(x) for x in eds) + ' (lida no <sourceDesc> do arquivo TEI).',
            '3_data_e_editor': '; '.join(f'{x["ano"]}; {x["editor"]} ({m_txt(x)}; fonte: {x["fonte_morte"]})' for x in eds) + '.',
            '4_direitos_da_edicao': dir_br + '; Lei 9.610/98, art. 41. Nos EUA, domínio público (publicada antes de 1931).',
            '5_licenca_da_transcricao': 'CC BY-SA 4.0 (Perseus Digital Library).',
            '6_permissao_de_reproduzir': 'Sim: CC BY-SA 4.0 permite copiar e redistribuir.',
            '7_permissao_de_derivados': 'Sim: CC BY-SA 4.0 permite adaptar (PDF, EPUB), com atribuição e mesma licença.',
            '8_atribuicao_exigida': 'Créditos à Perseus Digital Library e à edição-fonte, link da licença, indicação das mudanças; derivados sob CC BY-SA 4.0.',
        },
        'decisao': 'hospedar', 'downloads': True,
        'omitido': ['notas e aparato crítico do editor', 'introduções, comentários e traduções da edição impressa'] + e.get('omitido_extra', []),
        'normalizacao': norm, 'verificado_em': VERIFICADO,
    }

ROMAN = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV']

def baixar(p):
    os.makedirs(CACHE, exist_ok=True)
    dest = os.path.join(CACHE, COMMIT[:12] + '-' + os.path.basename(p))
    if not os.path.exists(dest):
        subprocess.run(['curl', '-sfL', '-A', 'BibliothecaLatina/1.0', '-o', dest, RAW.format(c=COMMIT, p=p)], check=True)
    return dest

def ler_tei(path):
    """Lê o TEI; entidades HTML não declaradas (ex.: &dagger; das cruces do editor) viram o caractere correspondente."""
    raw = open(path, encoding='utf-8').read()
    fix = re.sub(r'&([A-Za-z][A-Za-z0-9]*);', lambda m: m.group(0) if m.group(1) in ('amp', 'lt', 'gt', 'quot', 'apos') else html.unescape(m.group(0)), raw)
    root = ET.fromstring(fix)
    if not root.tag.startswith('{'):   # arquivos antigos sem o namespace TEI
        for el in root.iter():
            if isinstance(el.tag, str) and not el.tag.startswith('{'): el.tag = T + el.tag
    return root, raw

# Beta Code (transliteração ASCII do grego usada em arquivos antigos da Perseus) → grego Unicode
_BETA = dict(zip('abgdezhqiklmncoprstufxywv', 'αβγδεζηθικλμνξοπρστυφχψωϝ'))
_DIAC = {')': '\u0313', '(': '\u0314', '/': '\u0301', '\\': '\u0300', '=': '\u0342', '+': '\u0308', '|': '\u0345'}
def beta_para_grego(b):
    import unicodedata
    out, i, b = [], 0, b.replace('\n', ' ')
    while i < len(b):
        c = b[i]
        if c == '*':   # maiúscula: *, diacríticos, letra
            j = i + 1; marcas = ''
            while j < len(b) and b[j] in _DIAC: marcas += _DIAC[b[j]]; j += 1
            if j < len(b) and b[j].lower() in _BETA:
                out.append(_BETA[b[j].lower()].upper() + marcas); i = j + 1; continue
            out.append(c); i += 1; continue
        if c.lower() in _BETA:
            l = _BETA[c.lower()]; j = i + 1; marcas = ''
            while j < len(b) and b[j] in _DIAC: marcas += _DIAC[b[j]]; j += 1
            if l == 'σ' and (j >= len(b) or not (b[j].lower() in _BETA)): l = 'ς'
            out.append((l.upper() if c.isupper() else l) + marcas); i = j; continue
        out.append(c); i += 1
    return unicodedata.normalize('NFC', ''.join(out))

def ws(s): return re.sub(r'\s+', ' ', s or '').strip()

class Conv:
    def __init__(self, aspas, marcos_secao, prosa, marcos_capitulo=False):
        self.aspas = aspas; self.marcos = marcos_secao; self.prosa = prosa; self.cap = marcos_capitulo; self.beta = 0
    def inline(self, el):
        """Texto de el e descendentes (sem a cauda de el), aplicando as regras do cabeçalho do módulo."""
        tag = el.tag.replace(T, '')
        if tag in ('note', 'lb'): return ' '   # a nota sai e a quebra de linha vira espaço; as palavras dos dois lados continuam separadas
        if tag == 'seg' and el.get('rend') == 'dateline': return ''   # data de redação proposta pelo editor
        if tag in ('rdg', 'pb', 'sic', 'expan', 'speaker', 'head', 'bibl', 'figure', 'listPerson', 'castList'):
            return ''
        if tag == 'gap': return ' * * * '
        if tag == 'milestone':
            if self.cap and el.get('unit') == 'chapter': return f' \x04{el.get("n")}\x04 '   # início de capítulo marcado só por marco
            return f' {{{el.get("n")}}} ' if (self.marcos and el.get('unit') == 'section') else ''
        if tag == 'app':
            lem = el.find(T + 'lem'); return self.inline(lem) if lem is not None else ''
        if tag == 'choice':
            for k in ('corr', 'abbr', 'orig', 'reg'):
                c = el.find(T + k)
                if c is not None: return self.inline(c)
            return ''
        s = el.text or ''
        for ch in el:
            s += self.inline(ch) + (ch.tail or '')
        if tag == 'foreign' and el.get('{http://www.w3.org/XML/1998/namespace}lang') == 'grc' and not re.search('[\u0370-\u03ff\u1f00-\u1fff]', s) and re.search('[a-z]', s):
            self.beta += 1; return ' ' + beta_para_grego(s.strip())
        if tag == 'foreign': return ' ' + s   # grego ou outra língua colada à palavra anterior; o enclítico seguinte (-que) continua unido
        if tag == 'add': return '⟨' + s.strip() + '⟩'
        if tag == 'del': return '[' + s.strip() + ']'
        if tag == 'q' and self.aspas:   # rend="merge": continuação da citação do verso anterior
            return ' ' + ('\x03' if el.get('rend') == 'merge' else '\x01') + s.strip() + '\x02 '
        if tag == 'q': return ' ' + s + ' '   # a citação era separada só pelas aspas, que o arquivo omite
        if tag == 'l' and self.prosa: return ' ' + s.strip() + ' / '   # verso citado dentro de prosa
        return s

def head_of(div):
    h = div.find(T + 'head'); return ws(''.join(h.itertext())) if h is not None else ''

def titulo_tei(root):
    for t in root.iter(T + 'title'):
        x = ws(''.join(t.itertext()))
        if x: return x
    return ''

H1 = {'book', 'speech', 'act'}
H2 = {'poem', 'satire', 'prologue', 'letter', 'scene', 'epistle', 'elegy', 'ode', 'topic'}
def rot(n): return ROMAN[int(n)] if n.isdigit() and int(n) < len(ROMAN) else n

def converter(id_, cfg):
    teis = cfg['tei'] if isinstance(cfg['tei'], list) else [cfg['tei']]
    multi = len(teis) > 1
    prosa = cfg['forma'] == 'prosa'
    out, correcoes, aspas_any, raws = [], [], False, []

    def subdivs(d): return [c for c in d if c.tag == T + 'div' and c.get('type') == 'textpart']

    n_beta = 0
    for k_tei, tei in enumerate(teis):
        path = baixar(tei)
        root, raw = ler_tei(path); raws.append(raw)
        aspas = '<quotation marks="none"' in raw; aspas_any = aspas_any or aspas
        corpo = root.find(f'.//{T}body')
        ed = corpo.find(f'{T}div[@type="edition"]')
        if ed is None: ed = corpo.find(f'{T}div[@type!="commentary"]') if corpo.find(f'{T}div[@type="commentary"]') is not None else corpo.find(f'{T}div')
        marcos = prosa and not corpo.findall(f'.//{T}div[@subtype="section"]')
        cv = Conv(aspas, marcos, prosa, cfg.get('cap_marcos', False))

        def bloco(d):
            tags = (T + 'p', T + 'ab', T + 'l', T + 'lg', T + 'quote', T + 'sp', T + 'said', T + 'q', T + 'milestone')
            filhos = [c for c in d if c.tag in tags]
            t = ' '.join(cv.inline(c) for c in filhos) if filhos else cv.inline(d)
            t = re.sub(r'\s*/\s*(?=$|[“”"])', '', ws(t))
            t = re.sub(r'\s+/\s+', ' / ', t)
            return re.sub(r'\s+([,.;:?!])', r'\1', t)

        def prosa_paragrafo(d, ref):
            # um capítulo (ou seção sem subdivisões) vira um parágrafo; seções internas viram marcas {n}
            secs = [s for s in subdivs(d) if s.get('subtype') == 'section']
            if secs:
                texto = ' '.join((f'{{{s.get("n")}}} ' if k else '') + bloco(s) for k, s in enumerate(secs))
            else:
                texto = bloco(d)
            pedacos = re.split(r'\s*\x04(\w+)\x04\s*', ws(texto))
            pre = ref.rsplit('.', 1)[0] + '.' if '.' in ref else ''
            for r, t in [(ref, pedacos[0])] + [(pre + pedacos[i], pedacos[i + 1]) for i in range(1, len(pedacos), 2)]:
                t = re.sub(r'^\{1\}\s*', '', ws(t))
                if t: out.append(f'{r}\t{t}')

        def verso(d):
            for el in d:
                tag = el.tag.replace(T, '')
                if tag == 'l':
                    t = re.sub(r'\s+([,.;:?!])', r'\1', ws(cv.inline(el)))
                    if t: out.append(f'{el.get("n") or ""}\t{t}')
                elif tag == 'stage':
                    t = ws(cv.inline(el))
                    if t: out.append(f'\t{t}')
                elif tag == 'label' and el.get('rend') == 'opener':
                    t = ws(cv.inline(el))
                    if t: out.append(f'\t{t}')
                elif tag == 'milestone' and cfg.get('episodios') and el.get('unit') == 'tale' and el.get('n') and el.get('ed') == 'Magnus':
                    out.append(''); out.append('## ' + ws(el.get('n')))
                elif tag in ('lg', 'sp', 'q', 'quote', 'said', 'p'):
                    if tag == 'sp':
                        sp = el.find(T + 'speaker')
                        if sp is not None: out.append(''); out.append('> ' + ws(''.join(sp.itertext())))
                    elif tag == 'lg': out.append('')
                    if tag == 'q' and aspas:
                        n0 = len(out); verso(el)
                        linhas = [i for i in range(n0, len(out)) if '\t' in out[i]]
                        if linhas:
                            a, b = linhas[0], linhas[-1]
                            r, t = out[a].split('\t', 1); out[a] = f'{r}\t“{t}'
                            r, t = out[b].split('\t', 1); out[b] = f'{r}\t{t}”'
                    elif tag == 'p' and el.find(T + 'l') is None and el.find(T + 'lg') is None:
                        t = ws(cv.inline(el))     # rubrica ou didascália em prosa dentro de texto em verso
                        if t: out.append(f'\t{t}')
                    else:
                        verso(el)

        def abertura(d):
            for lab in d.findall(f'{T}label'):
                if lab.get('rend') == 'opener':
                    t = ws(cv.inline(lab))
                    # saudação em maiúsculas com letras marcadas <reg> em minúsculas (ex.: AT<reg>ti</reg>CO): como na edição, ATTICO
                    t1 = re.sub(r'(?<=[A-Z])l(?=[A-Z])', 'I', t)   # erro de digitalização: l minúsculo no lugar de I maiúsculo
                    if t1 != t: correcoes.append(f'erro de digitalização corrigido na saudação “{t}” → “{t1}” (l no lugar de I)')
                    t2 = re.sub(r'\b[A-Z]{2,}[a-z]+[A-Z]{2,}\b', lambda m: m.group(0).upper(), t1)
                    if t2 != t1: correcoes.append(f'maiúsculas uniformizadas na saudação “{t1}” → “{t2}” (letras marcadas <reg> em minúsculas no arquivo)')
                    if t2: out.append(f'\t{t2}')

        def cabecalho(lvl, h):
            if out and out[-1] != '': out.append('')
            out.append('#' * lvl + ' ' + h)

        def walk(d, refpref, ctx):
            for c in subdivs(d):
                st, n = c.get('subtype'), c.get('n') or ''
                if st == 'index' or (cfg.get('so_livro') and st == 'book' and n != cfg['so_livro']): continue
                if st == 'part': walk(c, refpref, ctx); continue
                h = head_of(c)
                if 'periocha' in h.lower(): continue
                if st in H1 or st in H2 or (st == 'chapter' and not prosa):
                    if st == 'act' and multi and any(x.get('subtype') == 'scene' for x in subdivs(c)):
                        walk(c, refpref, dict(ctx, ato=n)); continue   # obra com várias peças: o ato entra no título da cena
                    if not h:
                        h = {'book': f'{cfg.get("livro", "Liber")} {rot(n)}', 'speech': f'Oratio {rot(n)}', 'act': f'Actus {rot(n)}',
                             'scene': (f'Actus {rot(ctx["ato"])}, scaena {n}' if ctx.get('ato') else f'Scaena {n}'),
                             'satire': f'Satura {rot(n)}', 'prologue': 'Prologus', 'letter': f'Epistula {refpref}{n}', 'topic': f'Pars {rot(n)}'}.get(st, n)
                    lvl = 2 if (multi or st not in H1) else 1
                    cabecalho(lvl, h)
                    abertura(c)
                    if not prosa: verso(c)
                    novo = (refpref + n + '.') if st in ('book', 'speech', 'letter', 'topic') else refpref
                    if prosa and not subdivs(c): prosa_paragrafo(c, novo.rstrip('.') or n)
                    else: walk(c, novo, ctx)
                elif prosa and st in ('chapter', 'section'):
                    prosa_paragrafo(c, refpref + n)
                elif prosa:
                    if subdivs(c): walk(c, refpref, ctx)
                    else:
                        for k, p in enumerate([x for x in c if x.tag in (T + 'p', T + 'ab')], 1):
                            t = bloco(p)
                            if t: out.append(f'{refpref}{k}\t{t}')
                else:
                    verso(c); walk(c, refpref, ctx)

        if multi:
            cabecalho(1, cfg.get('titulos', [None] * len(teis))[k_tei] or titulo_tei(root))
        if ed is None:   # codificação antiga (div1 = livro; capítulos e seções só como marcos), ex.: Tácito, Annales
            for liv in corpo.findall(f'{T}div1'):
                n = liv.get('n') or ''
                if cfg.get('so_livro') and n != cfg['so_livro']: continue
                cabecalho(1, head_of(liv) or f'{cfg.get("livro", "Liber")} {rot(n)}')
                prosa_paragrafo(liv, f'{n}.0')
            continue
        if not subdivs(ed):
            if prosa:
                for k, p in enumerate([x for x in ed if x.tag in (T + 'p', T + 'ab')], 1):
                    t = bloco(p)
                    if t: out.append(f'{k}\t{t}')
            else: verso(ed)
        walk(ed, '', {})
        n_beta += cv.beta

    # Divisão de capítulo ausente no TEI (ex.: Salústio, Cat. 54 dentro do 53): se a numeração das seções recomeça
    # em {1} no meio de um parágrafo e o capítulo seguinte não existe, separa ali. Só muda a divisão, não o texto.
    refs = {l.split('\t')[0] for l in out if '\t' in l}
    for l in (list(out) if cfg.get('restaurar_capitulos') else []):
        if '\t' not in l or not prosa: continue
        ref, t = l.split('\t', 1)
        m = re.search(r' \{1\} ', t)
        if not m: continue
        pre, num = ref.rsplit('.', 1) if '.' in ref else ('', ref)
        if not num.isdigit(): continue
        prox = (pre + '.' if pre else '') + str(int(num) + 1)
        if prox in refs: continue
        k = out.index(l)
        out[k:k + 1] = [f'{ref}\t{t[:m.start()]}', f'{prox}\t{t[m.end():]}']
        refs.add(prox); correcoes.append(f'capítulo {prox} separado do {ref} (divisão ausente no arquivo TEI)')
    txt = '\n'.join(out).strip() + '\n'
    # aspas: fecha só onde a citação não continua no verso seguinte (<q rend="merge">)
    txt = re.sub(r'\x02(\n[^\t\n]*\t)\x03', r'\1', txt)
    txt = txt.replace('\x01', '“').replace('\x03', '“').replace('\x02', '”')
    if n_beta: correcoes.append(f'grego em Beta Code (transliteração ASCII do arquivo) convertido para letras gregas Unicode ({n_beta} trechos)')
    if cfg.get('ictus_dup'):
        base = {'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u'}
        n0 = len(re.findall(r'([ÁÉÍÓÚ])(?=[aeiouAEIOU])', txt))
        txt = re.sub(r'([ÁÉÍÓÚ])([aeiouAEIOU])', lambda m: m.group(1) if m.group(2).lower() == base[m.group(1)] else m.group(0), txt)
        correcoes.append(f'letra duplicada após maiúscula com acento de ictus corrigida ({n0} casos; a correção <corr> da Perseus repetia a inicial, ex.: “Íincerte” → “Íncerte”)')
    txt = re.sub(r'\n{3,}', '\n\n', txt)
    return txt, aspas_any, correcoes, raws

def conferir(cfg, txt):
    """Conferência de integridade: as palavras do corpo TEI (menos o que as regras omitem) devem ser as mesmas do texto.txt."""
    from collections import Counter
    teis = cfg['tei'] if isinstance(cfg['tei'], list) else [cfg['tei']]
    OMIT = {'note', 'rdg', 'sic', 'expan', 'head', 'bibl', 'figure', 'teiHeader', 'listPerson', 'castList'}
    esperado = Counter()
    for tei in teis:
        root = ler_tei(baixar(tei))[0]
        def visita(el):
            tag = el.tag.replace(T, '')
            if tag in OMIT or (tag == 'seg' and el.get('rend') == 'dateline'): return
            if tag == 'div' and el.get('type') == 'commentary': return
            if tag == 'div' and el.get('type') == 'textpart':
                st, n = el.get('subtype'), el.get('n') or ''
                if st == 'index' or (cfg.get('so_livro') and st == 'book' and n != cfg['so_livro']): return
                h = el.find(T + 'head')
                if h is not None and 'periocha' in ''.join(h.itertext()).lower(): return
            if tag == 'app':
                lem = el.find(T + 'lem')
                if lem is not None: visita(lem)
                return
            if tag == 'choice':
                for k in ('corr', 'abbr', 'orig', 'reg'):
                    c = el.find(T + k)
                    if c is not None: visita(c); return
                return
            esperado.update(re.findall(r"[^\W\d_]+", el.text or ''))
            for ch in el:
                visita(ch); esperado.update(re.findall(r"[^\W\d_]+", ch.tail or ''))
        corpo = root.find(f'.//{T}body')
        ed = corpo.find(f'{T}div[@type="edition"]')
        visita(ed if ed is not None else corpo)
    corpo = '\n'.join(l.split('\t', 1)[1] if '\t' in l else l[2:] for l in txt.splitlines() if '\t' in l or l.startswith('> '))
    corpo = re.sub(r'\{[^}]*\}', ' ', corpo)
    obtido = Counter(re.findall(r"[^\W\d_]+", corpo))
    faltam, sobram = esperado - obtido, obtido - esperado
    return sum(esperado.values()), sum(faltam.values()), sum(sobram.values()), faltam.most_common(6), sobram.most_common(6)

def main():
    ids = sys.argv[1:] or list(OBRAS)
    for id_ in ids:
        cfg = OBRAS[id_]
        txt, aspas, correcoes, raws = converter(id_, cfg)
        d = os.path.join(ROOT, 'textos', id_); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'texto.txt'), 'w', encoding='utf-8').write(txt)
        json.dump(metadados(id_, cfg, raws, aspas, correcoes), open(os.path.join(d, 'metadata.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        n_l = sum(1 for l in txt.splitlines() if '\t' in l)
        for c in correcoes:
            if 'separado' not in c: print('   ' + c)
        rest = [c.split(' separado')[0].replace('capítulo ', '') for c in correcoes if 'separado' in c]
        if rest: print(f'   {len(rest)} divisões de capítulo restauradas: ' + ', '.join(rest))
        tot, falta, sobra, fx, sx = conferir(cfg, txt)
        print(f'{id_}: {n_l} {"versos" if cfg["forma"] == "verso" else "parágrafos"}, {len(txt.split())} palavras, aspas={aspas}; conferência: {tot} palavras no TEI, {falta} ausentes, {sobra} a mais' + (f' {fx} {sx}' if falta or sobra else ''))

if __name__ == '__main__': main()
