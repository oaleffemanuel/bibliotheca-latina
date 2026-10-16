"""Une as pesquisas verificadas (research/*.json) à camada editorial (ed_*.py) e grava data/catalogo.json e data/candidatos.json."""
import glob, importlib, json, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
RES = HERE
OUT = os.path.join(HERE, '..', '..', 'data')
sys.path.insert(0, HERE)
TODAY = '2026-10-13'

research = {}
cands = []
for f in sorted(glob.glob(os.path.join(RES, '*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    for w in d.get('verified', []): research[w['source_url']] = w
    for c in d.get('candidates_not_verified', []): cands.append(dict(title=c.get('title'), author=c.get('author'), reason=c.get('reason'), url=c.get('url_tried')))

ED, HOST, OBP, EXTRA, AUDIO, AUDIO_NOTE = {}, {}, {}, {}, {}, {}
for m in sorted(glob.glob(os.path.join(HERE, 'ed_*.py'))):
    mod = importlib.import_module(os.path.basename(m)[:-3])
    ED.update(mod.ED); HOST.update(getattr(mod, 'HOST_OVERRIDE', {})); OBP.update(getattr(mod, 'OBP_FOR_DCC', {})); EXTRA.update(getattr(mod, 'EXTRA', {})); AUDIO.update(getattr(mod, 'AUDIO', {})); AUDIO_NOTE.update(getattr(mod, 'AUDIO_NOTE', {}))

def slug(s):
    s = unicodedata.normalize('NFD', s.lower().replace('ø', 'o').replace('æ', 'ae').replace('œ', 'oe')); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s)).strip('-')

def rights(r):
    rs = r.get('rights_status')
    lic = (r.get('license') or '')
    if rs == 'creative_commons' and re.search(r'NC|ND', lic): return rs, False
    return rs, bool(r.get('hosting_allowed'))

SRC = {'Hackett Publishing Company (Focus imprint)': 'Hackett Publishing', 'Corpus Thomisticum (Enrique Alarcón, Universidad de Navarra)': 'Corpus Thomisticum',
       'Repositório Institucional da UFES / EDUFES': 'Repositório UFES (EDUFES)', 'Corpus Corporum (University of Zurich)': 'Corpus Corporum', 'Latin Wikisource (la.wikisource.org)': 'Wikisource (latim)'}
for r in research.values(): r['source_name'] = SRC.get(r['source_name'], r['source_name'])
out, missing = [], []
for url, ed in ED.items():
    r = research.get(url)
    if not r: missing.append(url); continue
    rs, host = rights(r)
    if url in HOST: host = HOST[url]
    pdf = r.get('pdf_url'); official = r.get('official_url'); fmts = list(r.get('formats_available') or [])
    if url in OBP:
        o = research.get('https://books.openbookpublishers.com/10.11647/' + OBP[url] + '/')
        if o:
            pdf = o.get('pdf_url'); official = o['source_url']
            if 'pdf' not in fmts: fmts.append('pdf')
            if 'print' not in fmts: fmts.append('print')
    audio = bool(r.get('audio_available')) and bool(r.get('audio_url'))
    if audio and 'audio' not in fmts: fmts.append('audio')
    w = dict(
        id=ed.get('id') or slug(f"{(ed.get('author') or r.get('author') or '').split(' ')[-1]}-{ed.get('title') or r['title']}")[:70],
        title=ed.get('title') or r['title'], author=ed.get('author') or r.get('author'), author_death_year=r.get('author_death_year'),
        original_language=r.get('original_language') or 'la', historical_period=ed.get('period') or r.get('historical_period'),
        genre=ed.get('genre') or r.get('genre'), category=ed.get('category') or r.get('category') or 'Leitura',
        reading_stage=ed['stage'], difficulty=ed.get('dif'), vocabulary_difficulty=ed.get('voc'), morphology_difficulty=ed.get('morf'), syntax_difficulty=ed.get('sint'),
        recommended_prerequisites=ed.get('pre'), original_or_adapted=ed.get('kind') or {'didático': 'didatico'}.get(r.get('original_or_adapted'), r.get('original_or_adapted')),
        source_name=r['source_name'], source_url=url, source_home=ed.get('home'), official_url=official,
        license=r.get('license'), license_url=r.get('license_url'), rights_status=rs, hosting_allowed=host,
        rights_note=ed.get('rights_note') or r.get('editor_remarks'), edition=' · '.join(str(x) for x in [r.get('editor_or_annotator'), r.get('edition_year')] if x) or None,
        formats_available=fmts, pdf_url=pdf, epub_url=r.get('epub_url'), online_reading_url=r.get('online_reading_url'),
        audio_available=audio, audio_url=r.get('audio_url') if audio else None, audio_pronunciation=(ed.get('pron') or r.get('audio_pronunciation')) if audio else None,
        audio_license=r.get('audio_license') if audio else None,
        notes_available=bool(r.get('notes_available')), length_hint=r.get('length_hint'), estimated_reading_time=ed.get('tempo'),
        description_pt_br=ed['desc'], recommended_order=ed.get('ordem', 50), free=bool(r.get('free', True)),
        verification_status='verificado', last_verified=r.get('verification', {}).get('fetched_on') or TODAY)
    for k, v in ed.items():
        if k in ('rights_status', 'license', 'license_url', 'hosting_allowed', 'free', 'source_name', 'online_reading_url', 'pdf_url', 'epub_url', 'audio_url', 'audio_available', 'notes_available', 'original_language'): w[k] = v
    if url in EXTRA:
        x = EXTRA[url]; w['epub_url'] = x['epub_url']; w['description_pt_br'] += x['sufixo']
        if 'epub' not in w['formats_available']: w['formats_available'].append('epub')
    if url in AUDIO and AUDIO[url] in research:
        a = research[AUDIO[url]]
        w.update(audio_available=True, audio_url=AUDIO[url], audio_pronunciation=a.get('audio_pronunciation') or 'desconhecida', audio_license=a.get('audio_license'))
        if 'audio' not in w['formats_available']: w['formats_available'].append('audio')
        w['description_pt_br'] += AUDIO_NOTE.get(url, ' Gravação completa no LibriVox.')
    out.append(w)
out.sort(key=lambda w: (w['reading_stage'], w['recommended_order'], w['title']))
ids = [w['id'] for w in out]; assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
json.dump(out, open(os.path.join(OUT, 'catalogo.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# candidatos: só os que não entraram no catálogo
used_urls = {w['source_url'] for w in out}
cands = [c for c in cands if c.get('url') not in used_urls]
# data/candidatos.json é curado à mão; os candidatos brutos da pesquisa ficam só neste relatório
print('candidatos brutos da pesquisa (não gravados):', len(cands))
print(f'{len(out)} entradas; {len(cands)} candidatos; faltando na pesquisa: {missing}')
