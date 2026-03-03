# I-Lang Dictionary v2.0 — PUBLIC

## Genesis

I-Lang is an AI-native compression protocol.

Max (@SUN) designed, Claude Opus (@OPUS) co-authored, Gemini (@GEMINI) reviewed.

静水流深 | Palm Media Technology | ilang:genesis:2026-03-04

---

## Syntax

### Single operation

```
[VERB:@ENTITY|mod1=val1,mod2=val2]
```

### Pipe chain

```
[VERB1:@SRC]=>[VERB2]=>[VERB3:@DST]
```

Each step receives the previous output as `@PREV`.

### Urgency prefix

```
!! = high priority
```

### Conventions

- Verbs: UPPERCASE or Greek symbols
- Entities: `@` prefix, UPPERCASE
- Modifiers: lowercase, comma-separated
- Pipes: `=>` connects operations left to right

---

## Verbs (52)

### Data I/O

| Verb | Meaning | Example |
|------|---------|---------|
| READ | Read from source | `[READ:@GH|path=config.json]` |
| WRIT | Write to destination | `[WRIT:@R2|path=out.md]` |
| DEL | Delete | `[DEL:@LOCAL|path=tmp.log]` |
| LIST | List contents | `[LIST:@DRIVE|mch="*.pdf"]` |
| COPY | Copy | `[COPY:@R2|dst=@LOCAL]` |
| MOVE | Move | `[MOVE:@LOCAL|dst=@R2]` |
| STRM | Stream data | `[STRM:@ISEE|url=tgt]` |
| CACH | Cache | `[CACH:user_data|ttl=3600]` |
| SYNC | Synchronize | `[SYNC:@LOCAL|dst=@R2]` |
| Π | Batch process | `[Π:data_list|action=READ]` |

### Transform

| Verb | Meaning | Example |
|------|---------|---------|
| Σ | Merge / Summarize | `[Σ:@PREV|len=3]` |
| Δ | Difference | `[Δ:@old|dst=@new]` |
| φ | Filter | `[φ:@data|whr="type=ai"]` |
| ∇ | Sort / Rank | `[∇:@data|srt=date]` |
| DEDU | Deduplicate | `[DEDU:@list|key=id]` |
| ∂ | Split / Extract | `[∂:@text|delim=","]` |
| CHNK | Chunk | `[CHNK:@text|cap=1000]` |
| FLAT | Flatten | `[FLAT:@json|dep=2]` |
| NEST | Nest | `[NEST:@csv|key=category]` |
| λ | Map / Apply | `[λ:@array|func=upper]` |
| REDU | Reduce | `[REDU:@array|func=sum]` |
| PIVT | Pivot | `[PIVT:@data|col=month]` |
| TRNS | Transpose | `[TRNS:@matrix]` |
| ENCD | Encode | `[ENCD:@text|enc=base64]` |
| DECD | Decode | `[DECD:@b64|enc=utf8]` |
| ξ | Hash / Encrypt | `[ξ:@pwd|algo=sha256]` |
| ζ | Compress | `[ζ:@data|algo=gzip]` |
| EXPN | Decompress | `[EXPN:@gz]` |
| θ | Translate | `[θ:@text|lng=zh]` |
| FMT | Format | `[FMT:@raw|fmt=md]` |

### Analysis

| Verb | Meaning | Example |
|------|---------|---------|
| ψ | Sentiment | `[ψ:@tweet]` |
| CLST | Cluster | `[CLST:@users|k=5]` |
| SCOR | Score | `[SCOR:@draft|metric=quality]` |
| BNCH | Benchmark | `[BNCH:@func|n=100]` |
| AUDT | Audit | `[AUDT:@GH|scp=global]` |
| VALD | Validate | `[VALD:@json|sch=api_v2]` |
| CNT | Count | `[CNT:@list|whr="active=true"]` |
| μ | Average | `[μ:@stats|col=latency]` |
| TRND | Trend | `[TRND:@sales|frm=30d]` |
| CORR | Correlate | `[CORR:@data|col=x,y]` |
| FRCS | Forecast | `[FRCS:@stock|to=7d]` |
| ANOM | Anomaly detect | `[ANOM:@logs|thr=3σ]` |

### Generation

| Verb | Meaning | Example |
|------|---------|---------|
| CREA | Create | `[CREA:@GH|type=repo]` |
| DRFT | Draft | `[DRFT:marketing|len=med]` |
| PARA | Paraphrase | `[PARA:@text|ton=casual]` |
| EXTD | Extend | `[EXTD:@summary|len=long]` |
| SHRT | Shorten | `[SHRT:@article|len=short]` |
| STYL | Style | `[STYL:@draft|sty=ap]` |
| TMPL | Template | `[TMPL:@invoice|data=@SRC]` |
| FILL | Fill | `[FILL:@form|strategy=infer]` |

### Output

| Verb | Meaning | Example |
|------|---------|---------|
| Ω | Output | `[Ω:@RESULT]` |
| DISP | Display | `[DISP:dashboard_1]` |
| EXPT | Export | `[EXPT:@data|fmt=csv]` |
| PRNT | Print | `[PRNT:"Done"]` |
| LOG | Log | `[LOG:@error|lvl=warn]` |

### Meta

| Verb | Meaning | Example |
|------|---------|---------|
| VERS | Version | `[VERS]` |
| HELP | Help | `[HELP:SCRP]` |
| DESC | Describe | `[DESC:@GH]` |
| INTR | Introspect | `[INTR:memory]` |
| SELF | Self-check | `[SELF:latency]` |
| ECHO | Echo | `[ECHO:@SRC]` |
| NOOP | No operation | `[NOOP]` |

---

## Modifiers (28)

| Mod | Meaning | Values |
|-----|---------|--------|
| tgt | Target | entity_id, path |
| src | Source | entity_id, uri |
| dst | Destination | entity_id, uri |
| frm | From | timestamp |
| to | To | timestamp |
| scp | Scope | global, local, strict |
| dep | Depth | integer |
| rng | Range | start:end |
| whr | Where | condition_string |
| mch | Match | regex_string |
| exc | Exclude | regex_string |
| lim | Limit | integer |
| off | Offset | integer |
| top | Top N | integer |
| bot | Bottom N | integer |
| fmt | Format | json, md, csv, xml |
| lng | Language | ISO 639-1 |
| sty | Style | pro, casual, code |
| ton | Tone | urgent, neutral |
| len | Length | short, med, long |
| col | Columns | comma_separated |
| row | Rows | index_array |
| srt | Sort | field_name |
| grp | Group by | field_name |
| typ | Type | str, int, bool |
| enc | Encoding | utf8, base64, hex |
| chr | Charset | utf-8, ascii |
| cap | Capacity | bytes, tokens |

---

## Entities (14)

| Entity | Meaning |
|--------|---------|
| @R2 | Cloudflare R2 Storage |
| @COS | Cloud Object Storage |
| @GH | GitHub |
| @DRIVE | Google Drive |
| @LOCAL | Local filesystem |
| @WORKER | Cloudflare Worker |
| @CF | Cloudflare API |
| @SCREEN | UI output |
| @LOG | System log |
| @NULL | Discard |
| @STDIN | Standard input |
| @SRC | Source payload |
| @DST | Destination |
| @PREV | Previous pipe output |

---

## Quick Reference

| Natural Language | I-Lang | Saved |
|------------------|--------|-------|
| Read config from GitHub, format as JSON | `[READ:@GH|path=config.json]=>[FMT|fmt=json]` | 55% |
| Summarize previous in 3 bullets | `[Σ:@PREV|sty=bullets,len=3]` | 52% |
| Translate doc to Chinese, save to R2 | `[θ:@SRC|lng=zh]=>[WRIT:@R2]` | 60% |
| Read all .md files, merge, output | `[LIST:@LOCAL|mch="*.md"]=>[Π:READ]=>[Σ]=>[Ω]` | 65% |
| Filter logs for fatal errors | `[φ:@LOG|whr="lvl=fatal"]` | 55% |
| Draft professional email | `[DRFT:@SRC|ton=pro,fmt=email]` | 48% |

---

## Error Codes

| Code | Meaning |
|------|---------|
| E200 | Entity Not Found |
| E300 | Syntax Error |
| E301 | Type Mismatch |
| E400 | Rate Limited |
| E401 | Token Capacity Exceeded |
| E500 | Dependency Unavailable |
| E501 | Ambiguous Instruction |

---

I-Lang v2.0 | Max (@SUN) designed, Claude Opus (@OPUS) co-authored, Gemini (@GEMINI) reviewed.
静水流深 | Palm Media Technology | ilang:genesis:2026-03-04
