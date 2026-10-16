# Fluxo editorial do *Elementa Linguae Latinae*

Como uma lição nasce, é revisada e publicada, e como se registra a origem de cada conteúdo. Vale para `conteudo/livro.py`, `conteudo/licoes/*.py` e `conteudo/permissoes.json`.

## 1. Estados de uma lição (`status`)

| Status | Significado | Como aparece no site |
|---|---|---|
| `planejada` | só o título, em `livro.py`, sem módulo (ou módulo com `status='planejada'`) | listada como "em preparação", sem link |
| `rascunho` | módulo escrito, ainda sem revisão gramatical | gerada com selo "Rascunho" (só em builds locais; `--so-publicadas` a exclui) |
| `revisada` | gramática conferida por um revisor (nome e data em `creditos.revisao_gramatical`) | gerada com selo "Em revisão final"; `--so-publicadas` a exclui |
| `publicada` | pronta para o site público | gerada sem selo |

Para publicar no GitHub Pages, rode `python3 ferramentas/construir.py --so-publicadas`: só lições `publicada` vão para `docs/aprenda/`. O build local sem a opção mostra tudo, para revisar.

## 2. Tipos de conteúdo (`direitos.tipo`)

| Tipo | O que é | Exige |
|---|---|---|
| `original` | explicações, exemplos e exercícios escritos para o livro | nada além da licença do projeto (CC BY 4.0) |
| `dominio_publico` | lição que incorpora trechos de obras em domínio público (textos antigos, gramáticas antigas) | citar a fonte em `referencias` com `tipo='dominio_publico'` |
| `adaptacao_autorizada` | lição que adapta material de terceiros com permissão expressa | entrada em `permissoes.json` com `status_adaptacao = concedida`, documento arquivado, e `direitos.adaptacoes` preenchido |
| referência externa | **não é um tipo de lição**: é a seção "Aulas complementares", que só aponta (link) para aulas públicas de outros educadores | URL oficial verificada (`verificado` = data), atribuição; nunca reproduz o conteúdo |

Regras fixas:
- Não se copia, transcreve, parafraseia nem reorganiza o conteúdo de cursos de terceiros sem autorização. Estudar um curso para aprender a matéria é legítimo; o que vai para o livro é redigido de novo, a partir da gramática de domínio comum e de fontes em domínio público.
- Uma referência a aula externa não implica endosso, colaboração nem autoria do educador citado. O componente de atribuição diz isso explicitamente.
- O build recusa: `aulas_complementares` sem `url`, `titulo`, `educador` e `verificado`; `direitos.tipo = adaptacao_autorizada` sem `adaptacoes`; ids de catálogo inexistentes; status fora da lista.

## 3. Como escrever uma lição nova

1. Em `livro.py`, localize o título planejado e acrescente `modulo='lNN_slug'`.
2. Crie `conteudo/licoes/lNN_slug.py` copiando a estrutura de uma lição existente (`LICAO = dict(...)`). Campos:
   - identidade: `slug`, `titulo`, `tempo`, `resumo`, `status`
   - pedagogia: `objetivos` (lista), `topicos` (lista de tópicos gramaticais, ex. "1ª declinação", "presente do indicativo"), `prerequisitos` (`dict(texto=..., licoes=[slugs])`)
   - conteúdo: `secoes` (lista de pares título/HTML, com os construtores de `util.py`: `tabela`, `tabela_declinacao`, `tabela_conjugacao`, `comparacao`, `exemplos`, `observacao`, `dica`, `diagrama_frase`), `exercicios` (lista de `util.exercicio`, sempre com resposta explicada)
   - ligações: `leituras` (ids do catálogo; o build falha se não existirem) e `leituras_nota`; `aulas_complementares` (opcional; só com URL verificada); `referencias` (fontes consultadas, com `util.referencia`)
   - créditos e direitos: `creditos = dict(autor=..., colaboradores=[...], revisao_gramatical=dict(nome=..., data=...) ou None)`; `direitos = dict(tipo=..., licenca='CC BY 4.0', adaptacoes=[...])`
3. Status `rascunho`. Rode o build, abra `docs/aprenda/<slug>.html`, confira tabelas, macrons e exercícios.
4. Revisão gramatical por outra pessoa (ou por você, em outro dia, com uma gramática de referência ao lado: Allen & Greenough, Bennett, Ravizza). Registre em `creditos.revisao_gramatical` e mude para `revisada`.
5. Mude para `publicada`; rode `construir.py --so-publicadas`; commit da pasta `docs/`.

## 4. Como ligar a lição ao catálogo

Use `leituras` para apontar leituras que exercitam exatamente o tópico da lição (ex.: depois da 1ª declinação, *Ora Maritima* e *Puer Romanus*). Prefira recursos das etapas I–III para lições da parte I e II; para a parte IV (*Auctores*), aponte o texto autêntico comentado (DCC) que a lição lê. Os ids estão em `data/catalogo.json`.

## 5. Permissões de terceiros (`permissoes.json`)

Uma entrada por fonte, com `status_referencia` (link só: em geral `nao_necessaria`) e `status_adaptacao` (`nao_solicitada` → `solicitada` → `concedida`/`negada`). Guarde o documento da permissão (e-mail, carta) fora do repositório público e registre o caminho em `documento`. Só com `concedida` uma lição pode ter `direitos.tipo = adaptacao_autorizada` citando esse `id` em `direitos.adaptacoes[].fonte`.

## 6. Padrão de capítulo (definitivo, 2026-10-14)

Modelo implementado: capítulo 3, *Dē cāsibus* (`conteudo/licoes/l03_introducao_aos_casos.py`). Todo capítulo novo segue esta ordem; os campos entre parênteses são os do dicionário `LICAO`.

| # | Elemento | Campo / componente | Regra |
|---|---|---|---|
| 1 | Título latino | `titulo_latim` (ou herdado de `livro.py`) | latim correto, com macrons; *Dē* + ablativo ou nome do autor |
| 2 | Título em português | `titulo` | claro, sem jargão desnecessário |
| 3 | Objetivos | `objetivos` | 3–5 itens verificáveis ("reconhecer", "declinar", "traduzir") |
| 4 | Pré-requisitos | `prerequisitos` | texto + slugs; coerentes com `pre` em `livro.py` |
| 5 | Explicação | `secoes` | 4–6 seções de prosa contínua (evitar parágrafos de uma linha); cada regra com o porquê |
| 6–7 | Exemplos e traduções | `exemplos()` | latim original do livro ou autor em domínio público com a fonte; tradução que mostre a função, não só o sentido |
| 8 | Análise gramatical | `analise()` | ao menos uma frase analisada palavra a palavra; de preferência autêntica |
| 9 | Tabelas | `tabela_declinacao`, `tabela_conjugacao`, `comparacao` | terminações em `<b>`; macrons em todos os paradigmas |
| 10 | Diagrama | `diagrama_frase()` | um por capítulo nas partes I–III |
| 11 | Erros comuns | `erros_comuns` | 4–6 pares (erro, por quê e como evitar) baseados em dificuldades reais de falantes de português |
| 12 | Prática guiada | `pratica_guiada()` | 1–2 frases resolvidas em passos, cada passo escondido |
| 13 | Exercícios independentes | `exercicio()` | 4–6 conjuntos: reconhecimento, produção, transformação, leitura/análise, retroversão |
| 14 | Gabarito explicado | resposta em cada item | toda resposta diz *por quê*; ambiguidades reconhecidas e resolvidas |
| 15 | Leituras do catálogo | `leituras`, `leituras_nota` | 3–6 ids reais; dizer o que ler e quando |
| 16 | Referências | `referencias` | gramáticas citadas por parágrafo **conferido** (Bennett, A&G na edição DCC, Ravizza, Kennedy); nunca citar de memória |

Estilo: português do Brasil, segunda pessoa ("você"), frases claras; termos técnicos explicados na primeira ocorrência; latim sempre em itálico com `lang="la"` nos blocos; números de lições citados sempre pelo sumário (`SUMARIO-EDITORIAL.md`). Nada de conteúdo raso para aumentar o número de capítulos: um capítulo existe quando há matéria para objetivos, explicação, prática e leitura próprias.

Fontes de pesquisa privada: o estudo de cursos de terceiros (num espaço de pesquisa privado, mantido fora deste repositório) serve só para identificar tópicos e avaliar a cobertura. Explicações, exemplos, diagramas e exercícios são escritos de novo, a partir das gramáticas de referência; nenhuma frase, exemplo, exercício ou sequência característica de um curso é reproduzida ou parafraseada.

Revisão: `creditos.revisao_gramatical` só é preenchido quando uma pessoa diferente do autor revisa o capítulo. A revisão interna do autor (conferência contra as gramáticas) é registrada em `conteudo/revisoes/`, sem marcar o capítulo como revisado externamente.

## 7. Convenções editoriais (decididas na auditoria de 2026-10-15)

Distinguir **variante legítima** (duas formas atestadas ou duas notações aceitas) de **inconsistência** (o livro escreve a mesma coisa de dois jeitos sem motivo). Variantes legítimas são explicadas uma vez, com a fonte, e depois o livro usa uma só forma.

### 7.1 Quantidade vocálica (mácrons)
- **Onde marcar:** todo latim do livro leva mácron nas vogais longas por natureza: paradigmas, exemplos, exercícios, glossários e os textos antigos que o livro edita, inclusive Vulgata, Agostinho, Tomás e hinos. A breve não se marca (nem ˘), salvo nas tabelas de métrica.
- **Referência:** Lewis & Short (Perseus/Logeion) e Allen & Greenough. Quando divergirem, use Bennett para desempatar e registre a divergência. **Na dúvida, sem mácron:** nunca se adivinha uma quantidade.
- **Quantidade oculta** (vogal longa antes de duas consoantes: *sānctus, quīnque, ōrdō*): marcar quando A&G ou Bennett a dão. O Lewis & Short em geral não marca quantidades ocultas, então o silêncio dele não conta contra. Sem indicação em A&G nem em Bennett, fica sem mácron (ex.: *stella*, decidido na auditoria).
- **Ditongos** (*ae, oe, au*) não levam mácron. O *i* consonantal entre vogais (*eius, huius, cuius, maior*) também não; a sílaba já é pesada. A notação de Bennett *ējus, hūjus* é registrada como notação dele, não usada no livro.
- **Exceção:** amostras de grafia medieval ou de uma edição citada como documento (cap. 50) ficam na grafia da fonte, sem mácrons, e são identificadas como tal.

### 7.2 *hīc, haec, hōc* (corrigido na auditoria)
- O pronome se escreve ***hīc, haec, hōc***, com genitivo *huius*, dativo *huic*, acusativo *hunc, hanc, hōc* e ablativo *hōc, hāc, hōc*; no plural, *hī, hae, haec; hōrum, hārum, hōrum; hīs; hōs, hās, haec*. É a grafia de Bennett § 87, de A&G § 146 e do verbete de L&S (*hīc, haec, hōc*), todos conferidos em 2026-10-15.
- A&G § 146 n. 1 informa que a vogal de *hīc, hōc* era originalmente breve, e talvez sempre o tenha sido; a sílaba é pesada no verso (antigo *hicc, hocc*). Muitas edições escolares escrevem por isso *hic, hoc*. O livro registra isso uma vez (cap. 15) e usa a grafia das gramáticas de referência.
- O advérbio *hīc* ("aqui") tem a mesma grafia; o contexto distingue.
- Uma primeira versão desta seção atribuía *hic, hoc* a A&G e L&S, o que estava errado; a auditoria corrigiu a atribuição.

### 7.3 Grafia
- *u* vocálico e *v* consonantal (*vīlla, vōx*); *i* para vocálico e consonantal (*iam, Iūlius, eius*), nunca *j*, inclusive em nomes bíblicos (*Iēsūs*: ver 7.4).
- *ae, oe* sem ligadura. Grafia clássica normalizada em todo o livro, também nos textos cristãos (*caelum*, não *cœlum*; *ae* por *æ*). A grafia medieval (*e* por *ae*, *michi, nichil*, *-cio* por *-tio*) aparece só como objeto de estudo (cap. 50), identificada.
- Variantes legítimas registradas uma vez e depois unificadas: *-ērunt/-ēre*, *-is/-ēs* (acusativo plural de temas em *-i*), *quom/cum*, *adulēscēns/adolēscēns*.

### 7.4 Nomes próprios
- **Nomes greco-latinos** (*Aenēās, Caesar, Cicerō, Ītalia*): mácrons conforme L&S. Se o verbete não for conferido, ficam sem mácron e o caso vai para as pendências.
- **Nomes bíblicos** de origem hebraica, indeclináveis ou de quantidade incerta (*Abel, Cain, Ioseph, Maria, Israel, Ierūsalem/Ierosolyma, Elias*): sem mácrons, com *i* inicial (não *j*). Exceção: *Iēsūs, Iēsū, Iēsum* tem quantidade estabelecida e declinação latina (L&S *Jesus*), e leva mácron.
- **Em português**, os nomes ficam na forma portuguesa usual: Jesus, João, César, Cícero, Virgílio.

### 7.5 Pronúncia
- **Restaurada (clássica):** a do capítulo 1, conforme Allen, *Vox Latina*, como descrita em Bennett §§ 1–6 e A&G §§ 1–12.
- **Eclesiástica (romana):**
  - É a das regras do *Liber Usualis*. O *h* é mudo, **exceto em *mihi* e *nihil*, pronunciados "míki", "níkil"**. A grafia medieval *michi, nichil* reflete essa pronúncia.
  - É uma regra de uso litúrgico do séc. XX, não universal: muitos cantores e escolas pronunciam *mi-i*.
  - O livro a apresenta como norma da tradição romana, sem dizer que é a única.

### 7.6 Terminologia gramatical
- **Tempos e aspecto:** *infectum/perfectum*; "tema do presente", "tema do perfeito", "supino" para a 4ª parte principal (cap. 13).
- **Nomes dos tempos:** presente, imperfeito, futuro, perfeito, mais-que-perfeito, futuro perfeito. Ravizza diz "futuro imperfeito" para o futuro simples; o livro registra isso uma vez, no cap. 12.
- **Modos:** "subjuntivo", nunca "conjuntivo", exceto no título latino *coniūnctīvus*.
- **Sequência dos tempos:** tempos "primários" e "secundários".
- **Conjugações:** 1ª, 2ª, 3ª, "3ª em -iō" e 4ª.
- **Orações e construções:** "oração infinitiva" (acusativo com infinitivo); "particípio conjunto"; "ablativo absoluto"; "gerúndio"/"gerundivo"; "perifrástica passiva/ativa".
- **Classes de adjetivo:** "adjetivos de primeira classe" (1ª/2ª declinação) e "de segunda classe" (3ª).

### 7.7 Citações
- **Gramáticas:**
  - Bennett § 21.2.e e A&G § 43.e: subdivisões separadas por ponto.
  - Ravizza n. 19 (não "nº").
  - Kennedy § 34.
  - Número inferido de OCR ilegível: marcado na revisão interna, nunca no texto como se fosse certo.
- **Bíblia:**
  - Formato: livro abreviado em português, capítulo e vírgula (Mt 6,9; Sl 22,1).
  - Os Salmos seguem a numeração da Vulgata, que é a do texto citado. Quando o número difere da numeração hebraica/moderna, esta vai entre parênteses na primeira menção: Sl 22,1 (23,1).
- **Autores clássicos:**
  - Nome do autor em português, título abreviado em itálico, livro, capítulo e seção ou verso em algarismos arábicos separados por ponto. Exemplos: César, *BG* 1.1.1; Virgílio, *En.* 2.1; Cícero, *Cat.* 1.1; Lívio 1.4.1; Ovídio, *Met.* 1.5.
- **Edições:**
  - Todo trecho antigo usado como texto de leitura (não só citação breve) indica a edição: editor e ano, ou "texto da The Latin Library, conferido com [edição]".

### 7.8 Edições e direitos
- **Sem restrição:** o texto antigo em si é de domínio público. Uma edição crítica, porém, pode ter direitos próprios: aparato, conjecturas modernas, e, em alguns países, a própria edição científica por prazo limitado.
- **Política:**
  1. Para textos de leitura (Parte IV e trechos longos), usar uma edição antiga identificada e em domínio público: Perseus (Greenough, Holmes, Clark, Conway & Walters, Magnus, Merrill, Mueller), scans do archive.org, Vulgata Clementina, Leonina de 1888, Migne. Também vale o texto da The Latin Library conferido contra uma dessas.
  2. Não usar texto de edição moderna protegida, como Oxford Classical Texts recentes, Teubner recentes, Corpus Thomisticum (que declara direitos) ou o texto DCC de Eutrópio.
  3. Citações breves com fonte são admitidas como citação (Lei 9.610/98, art. 46, III), mas também devem vir de uma edição identificada.
- **Variantes:** quando duas edições divergem, o livro não escolhe em silêncio. Indica a edição seguida e registra a variante numa nota.
- **`direitos.tipo`:** o texto do capítulo é original (CC BY 4.0). `dominio_publico` indica que o capítulo **contém** trechos antigos de edições em domínio público, e a regra vale para todo o livro.

### 7.9 Duração
- `tempo` estima uma sessão de estudo: 45–90 min.
- Capítulos acima de 90 min são divididos em duas sessões no próprio texto, com uma indicação ("Se preferir, pare aqui"), em vez de mudar o currículo.

## 8. Edição beta e canal de correções (2026-10-16)
- **Aviso:** o aviso de beta aparece no índice do livro e no topo de cada capítulo. O texto está em `AVISO_BETA`, em `ferramentas/construir.py`. A seção "Sobre esta edição beta" do índice explica:
  - a finalidade do livro;
  - a verificação interna assistida por IA;
  - a diferença entre revisão interna e revisão acadêmica humana;
  - a autoria independente;
  - o agradecimento a Rafael Falcão, sem endosso.
- **Duas indicações separadas em cada capítulo:**
  - a situação editorial (`status`: Rascunho, Em revisão final ou Publicado);
  - a revisão acadêmica, "pendente" enquanto `creditos.revisao_gramatical` estiver vazio.
  Publicar um capítulo não o torna revisado.
- **"Reportar problema":**
  - Fica no topo do capítulo e numa marca ⚑ ao lado de cada título de seção.
  - O formulário recolhe capítulo, seção, tipo de problema, descrição e sugestão opcional. Não pede nome nem e-mail.
  - Sem servidor próprio: com `FEEDBACK['url']` vazio, o leitor gera o relatório e o copia para o canal do beta. Com a URL de um formulário externo (ex.: Google Forms) e os ids `entry.NNN` em `FEEDBACK['campos']`, o botão abre o formulário já preenchido.
- **Triagem:** cada relato vira um item no estilo de `AUDITORIA-GERAL.md` (categoria, severidade, estado) antes de qualquer correção.
