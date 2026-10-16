# Bibliotheca Latina — research brief (shared by all research agents)

You are researching candidate resources for a free, static, curated digital library for
Portuguese-speaking (Brazilian) students of Latin. Interface language: pt-BR. Latin titles stay in Latin.

## Non-negotiable rules
1. NEVER invent titles, authors, URLs, licenses, download links, audio availability, or metadata.
   Every URL you report must have been fetched by you in this session (WebFetch or `curl -sIL`) and
   must return HTTP 200 (or a redirect ending at 200). Record the final URL.
2. For every entry, record the exact URL of the rights / license statement you relied on
   (e.g. the site's terms page, the CC badge page, the Gutenberg license section, the TEI header, the "About" page).
   If you could not find a license statement, write license_url = null and rights_status = "unverified".
3. A public-domain ancient author does NOT make a modern edition, translation, commentary, vocabulary,
   or recording public domain. Judge the SPECIFIC version at the URL.
4. Default to "link only" (hosting_allowed = false) whenever rights are uncertain.
   hosting_allowed = true ONLY when the specific file is clearly public domain worldwide OR under a CC license
   that permits redistribution (CC BY, CC BY-SA, CC0). CC BY-NC / NC-ND and "free to read" open access = false.
   Brazil: public domain = 70 years after the author's death (counted from Jan 1 of the following year).
   Editors/annotators/translators of a modern edition also have rights. Record author death year when known.
5. Do NOT download or copy any text into your report. Report metadata only.
6. Do NOT apply CEFR levels (A1/B2/C1). Do not rate difficulty with CEFR.
7. Do not pad the list to reach a number. Fewer, fully verified entries beat many shaky ones.
   If something could not be verified, put it in a separate `candidates_not_verified` list with the reason.

## Output
Write ONE JSON file at the path given in your task, with this structure:
{
  "agent": "<your area>",
  "verified": [ <entry>, ... ],
  "candidates_not_verified": [ {"title": "...", "author": "...", "url_tried": "...", "reason": "..."} ],
  "notes": "free text: anything the editor should know (site-wide license terms, caveats, URL patterns)"
}

<entry> fields (use null when unknown; do not guess):
{
  "title": "exact title as shown at the source (Latin titles in Latin)",
  "author": "Author name (e.g. 'Gaius Iulius Caesar', 'Augustinus Hipponensis', 'Hans H. Ørberg'); for modern readers/grammars the modern author",
  "author_death_year": 1932 or null,
  "editor_or_annotator": "name(s) of modern editor/commentator or null",
  "edition_year": 1913 or null,
  "original_language": "la" (or "la+pt-BR", "la+en" for bilingual/annotated),
  "historical_period": one of ["Clássico", "Pós-clássico", "Tardio e patrístico", "Medieval", "Renascentista e neolatino", "Moderno (material didático)"],
  "genre": short label, pt-BR, e.g. "Leitor graduado", "Gramática", "Método", "Comentário anotado", "Historiografia", "Oratória", "Poesia épica", "Poesia elegíaca", "Poesia lírica", "Filosofia", "Teologia", "Autobiografia", "Epistolografia", "Hagiografia", "Fábula", "Narrativa", "Escritura (Vulgata)", "Dicionário", "Ferramenta",
  "category": one of ["Leitura", "Gramática e referência", "Método e curso", "Ferramenta", "Referência comercial"],
  "original_or_adapted": one of ["original", "adaptado", "simplificado", "didático"]  (didático = written for learners from scratch; adaptado = abridged/simplified from an ancient original),
  "what_it_is": "2–4 sentences in English describing precisely what is at the URL: full text or selection? Latin only or with English/Portuguese notes/vocabulary/translation? Length (pages/chapters/lines if shown). Macrons? This is the ONLY place for description; be factual.",
  "source_name": "e.g. 'Dickinson College Commentaries'",
  "source_url": "final URL you fetched (HTTP 200)",
  "official_url": "publisher/official page if different from source_url, else null",
  "license": "exact license label as stated (e.g. 'CC BY-SA 4.0', 'Public domain (Project Gutenberg License)', 'Copyright — all rights reserved', 'Open access, no license stated')",
  "license_url": "URL of the rights statement you read, or null",
  "rights_status": one of ["public_domain", "creative_commons", "open_access_limited", "commercial", "unverified"],
  "hosting_allowed": true/false,
  "formats_available": subset of ["html", "pdf", "epub", "txt", "xml", "audio", "print"],
  "pdf_url": direct PDF URL you fetched (HEAD 200, content-type application/pdf) or null,
  "epub_url": direct EPUB URL or null,
  "online_reading_url": URL where the text can be read in the browser, or null,
  "audio_available": true/false,
  "audio_url": URL of the audio page (e.g. LibriVox project page) or null,
  "audio_pronunciation": "restaurada" | "eclesiástica" | "desconhecida" | null,
  "audio_license": "e.g. 'Public domain (LibriVox)'" or null,
  "notes_available": true/false  (true = running vocabulary, grammatical notes, commentary at the source),
  "length_hint": "e.g. '~120 pages', '8 books', '1,200 lines', 'c. 40 short chapters' — only if visible at the source, else null",
  "free": true/false  (false for commercial textbooks),
  "verification": {"http_status": 200, "fetched_on": "2026-10-13", "how": "WebFetch|curl"},
  "editor_remarks": "optional: anything about difficulty, suitability, caveats (English)"
}

Use `curl -sIL -A 'Mozilla/5.0' <url> | grep -i -E 'HTTP/|content-type|location'` to verify downloads without saving them.
Prefer WebFetch to read page content. Be efficient: ~25–40 fetches is plenty. Time-box yourself.
