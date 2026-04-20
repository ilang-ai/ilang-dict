# I-Lang Dictionary v3.0

## Genesis

I-Lang is an AI-native communication protocol.

Max (@SUN) designed, Claude Opus co-authored, GPT red-teamed.

Eastsoft Inc. | Palm Media Technology | ilang:v3.0:2026-04-20

---

## Syntax

### Operation (what something DOES)

```
[VERB:@TARGET|mod1=val1,mod2=val2]
```

### Pipe chain

```
[VERB1:@SRC]=>[VERB2]=>[VERB3:@DST]
```

Each step receives the previous output as `@PREV`.

### Declaration (what something IS)

```
::STATE{@ENTITY, key:value}
::GENE{name|conf:level|scope:context}
  T:trait_description
  A:anti_pattern⇒consequence
```

### Conventions

- Verbs: UPPERCASE
- Entities: `@` + UPPERCASE
- Modifiers: lowercase
- Pipes: `=>` connects operations left to right

---

## Verbs (88)

### Data I/O (12)

| Verb | Alias | Target is | Meaning |
|------|-------|-----------|---------|
| READ | | source | Read content from source |
| WRIT | | destination | Write input to destination |
| GET | | source | Fetch remote resource |
| DEL | | destination | Delete target |
| LIST | | source | Enumerate items in container |
| COPY | | destination | Copy without deleting source |
| MOVE | | destination | Move from source to destination |
| STRM | | source | Stream data |
| CACH | | n/a | Cache for fast retrieval |
| SYNC | | destination | Synchronize source and destination |
| SEND | | destination | Transmit to destination |
| RUN | | n/a | Execute command or script |

### Transform (22)

| Verb | Alias | Meaning |
|------|-------|---------|
| FMT | | Reformat into target format |
| CONV | | Convert type or representation |
| SPLIT | ∂ | Split by delimiter or rule |
| MERGE | Σ | Merge multiple items into one |
| MAP | λ | Apply function to each element |
| FILT | φ | Filter by condition |
| SORT | ∇ | Sort by field or rule |
| DEDU | | Remove duplicates |
| FLAT | | Flatten nested data |
| NEST | | Nest flat data by key |
| CHNK | | Chunk into sized pieces |
| REDU | | Reduce to single value |
| PIVT | | Pivot data by column |
| TRNS | | Transpose |
| ENCD | | Encode (base64, hex) |
| DECD | | Decode |
| HASH | ξ | Hash (one-way digest) |
| CMPR | ζ | Compress (gzip, etc.) |
| EXPN | | Decompress |
| XLAT | θ | Translate between languages |
| REWR | | Rewrite preserving meaning |
| DIFF | Δ | Show differences |

### Analysis (17)

| Verb | Alias | Meaning |
|------|-------|---------|
| SCAN | | Examine for patterns or features |
| MTCH | | Find matching elements |
| CNT | | Count items or occurrences |
| STAT | μ | Compute statistics |
| EVAL | | Assess against criteria |
| SCOR | | Score against metric |
| RANK | | Order by priority or score |
| TRND | | Detect trend |
| CORR | | Correlate variables |
| FRCS | | Forecast |
| ANOM | | Detect anomalies |
| SENT | ψ | Sentiment analysis |
| CLST | | Cluster |
| BNCH | | Benchmark |
| AUDT | | Audit |
| VALD | | Validate against schema or rule |
| CLSF | | Classify into categories |

### Generation (10)

| Verb | Alias | Meaning |
|------|-------|---------|
| CREA | | Create new resource |
| DRFT | | Generate first draft |
| EXPD | | Expand with detail |
| SHRT | | Shorten or condense |
| PARA | | Paraphrase |
| STYL | | Apply style |
| TMPL | | Apply template |
| FILL | | Fill form or structure |
| EXTC | | Extract specific data |
| GEN | | Generic generate |

### Execute (12)

| Verb | Alias | Meaning |
|------|-------|---------|
| PLAN | | Design approach |
| DECI | | Choose between options |
| CHEK | | Verify condition |
| FIX | | Repair errors |
| DPLO | | Deploy to production |
| SAVE | | Persist to storage |
| REVW | | Review completed work |
| LERN | | Update internal model |
| TEST | | Verify functionality |
| PARS | | Parse structured input |
| LOOP | | Repeat operation over set |
| WAIT | | Pause for condition |

### Output (5)

| Verb | Alias | Meaning |
|------|-------|---------|
| OUT | Ω | Mark final output |
| DISP | | Display to user |
| EXPT | | Export to file format |
| PRNT | | Print message |
| LOG | | Log event or state |

### Structure (5)

| Verb | Alias | Meaning |
|------|-------|---------|
| LINK | | Create connection |
| SET | | Assign value |
| TAG | | Attach metadata |
| GRP | | Group by criterion |
| EMBD | | Encode into vector space |

### Meta (4)

| Verb | Alias | Meaning |
|------|-------|---------|
| HELP | | Show help |
| DESC | | Describe entity |
| INTR | | Introspect internal state |
| NOOP | | No operation |

### Batch (1)

| Verb | Alias | Meaning |
|------|-------|---------|
| BATC | Π | Apply verb to each item in list |

---

## Aliases

| Alias | Verb | Alias | Verb |
|-------|------|-------|------|
| Σ | MERGE | ψ | SENT |
| Δ | DIFF | ξ | HASH |
| φ | FILT | ζ | CMPR |
| ∇ | SORT | θ | XLAT |
| λ | MAP | Ω | OUT |
| ∂ | SPLIT | Π | BATC |
| μ | STAT | | |

---

## Modifiers (29)

| Mod | Meaning | Values |
|-----|---------|--------|
| src | Explicit source | entity, URI |
| dst | Explicit destination | entity, URI |
| path | Path within entity | string |
| fmt | Output format | text, json, md, csv, xml, html, email |
| lng | Language | ISO 639-1 (en, zh, ja) |
| sty | Style | pro, casual, code, bullets |
| ton | Tone | urgent, neutral, formal |
| len | Length target | short, med, long, number |
| lim | Limit | integer |
| off | Offset | integer |
| top | Top N | integer |
| bot | Bottom N | integer |
| srt | Sort by | field name |
| grp | Group by | field name |
| whr | Filter condition | condition string |
| mch | Match pattern | glob (default) or regex with typ=regex |
| exc | Exclude pattern | glob or regex |
| dep | Depth | integer |
| rng | Range | start:end |
| typ | Type expectation | str, int, bool, regex |
| enc | Encoding | utf8, base64, hex |
| cap | Capacity | bytes, tokens |
| pri | Priority | p0, p1, p2 |
| col | Columns | comma separated |
| row | Rows | index array |
| frm | From (time) | timestamp |
| to | To (time) | timestamp |
| scp | Scope | global, local, strict |
| op | Operation ref | verb name (for BATC) |

---

## Entities

### Core

| Entity | Meaning |
|--------|---------|
| @SRC | Source payload |
| @DST | Destination |
| @PREV | Previous pipe output |
| @LOCAL | Local filesystem |
| @SCREEN | User-visible output |
| @LOG | System log |
| @NULL | Discard sink |
| @STDIN | Standard input |

### External

| Entity | Meaning |
|--------|---------|
| @GH | GitHub |
| @R2 | Cloudflare R2 Storage |
| @COS | Cloud Object Storage |
| @DRIVE | Google Drive |
| @WORKER | Cloudflare Worker |
| @CF | Cloudflare API |

---

## Quick Reference

| Natural Language | I-Lang |
|------------------|--------|
| Read config from GitHub, format as JSON | `[READ:@GH|path=config.json]=>[FMT|fmt=json]` |
| Summarize previous in 3 bullets | `[Σ:@PREV|sty=bullets,len=3]` |
| Translate to Chinese, save to R2 | `[θ:@SRC|lng=zh]=>[WRIT:@R2]` |
| Read all .md, merge, output | `[LIST:@LOCAL|mch=*.md]=>[Π:READ]=>[Σ]=>[Ω]` |
| Filter fatal errors from logs | `[φ:@LOG|whr=lvl:fatal]` |
| Draft professional email | `[DRFT:@SRC|ton=pro,fmt=email]` |

---

## Error Codes

| Code | Meaning |
|------|---------|
| E200 | Entity Not Found |
| E201 | Unsupported Entity |
| E300 | Syntax Error |
| E301 | Type Mismatch |
| E302 | Invalid Modifier |
| E303 | Invalid Value |
| E304 | Unknown Verb |
| E305 | Unknown Alias |
| E400 | Rate Limited |
| E401 | Capacity Exceeded |
| E402 | Timeout |
| E500 | Dependency Unavailable |
| E501 | Ambiguous Instruction |
| E502 | Unsupported Format |

---

## Resources

| Resource | Link |
|----------|------|
| Protocol Spec | [ilang-ai/ilang-spec](https://github.com/ilang-ai/ilang-spec) |
| Website | [ilang.ai](https://ilang.ai) |
| All Datasets | [huggingface.co/i-Lang](https://huggingface.co/i-Lang) |
| Book (Narrative) | [Amazon](https://www.amazon.com/dp/B0CZY6V3GM) |
| Book (Specification) | [Amazon](https://www.amazon.com/dp/B0F5FV64Q2) |
| Academic Paper | [ResearchGate](https://www.researchgate.net/publication/389513037) |

---

I-Lang v3.0 Final | Max (@SUN) designed, Claude Opus co-authored, GPT red-teamed.
Eastsoft Inc. | Palm Media Technology | MIT License
ilang.ai | github.com/ilang-ai
