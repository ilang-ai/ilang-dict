# I-Lang Dictionary v2.0 — PUBLIC

> AI-native compression protocol
> Full spec: [ilang-spec](https://github.com/ilang-ai/ilang-spec)

---

## Verbs (52)

### Data I/O

| Verb | Meaning | Args | Example |
|------|---------|------|---------|
| READ | Read data from source | @target, path | `[READ:@GH|path=config.json]` |
| WRIT | Write data to destination | @target, path | `[WRIT:@R2|path=out.md]` |
| DEL | Delete entity | @target, id | `[DEL:@LOCAL|path=tmp.log]` |
| LIST | List contents | @target, filter | `[LIST:@DRIVE|mch="*.pdf"]` |
| COPY | Copy data | @src, @dst | `[COPY:@R2|dst=@LOCAL]` |
| MOVE | Move data | @src, @dst | `[MOVE:@LOCAL|dst=@R2]` |
| STRM | Open data stream | @target, port | `[STRM:@ISEE|url=tgt]` |
| CACH | Cache payload | key, ttl | `[CACH:user_data|ttl=3600]` |
| SYNC | Synchronize state | @src, @dst | `[SYNC:@LOCAL|dst=@R2]` |
| Π | Batch process | array, action | `[Π:data_list|action=READ]` |

### Transform

| Verb | Meaning | Args | Example |
|------|---------|------|---------|
| Σ | Merge / Summarize | @src, strategy | `[Σ:@PREV|len=3]` |
| Δ | Calculate difference | @v1, @v2 | `[Δ:@old|dst=@new]` |
| φ | Filter dataset | condition | `[φ:@data|whr="type=ai"]` |
| ∇ | Sort / Rank | field, order | `[∇:@data|srt=date]` |
| DEDU | Deduplicate | key | `[DEDU:@list|key=id]` |
| ∂ | Split / Extract | delimiter | `[∂:@text|delim=","]` |
| CHNK | Chunk data | size | `[CHNK:@text|cap=1000]` |
| FLAT | Flatten nested | depth | `[FLAT:@json|dep=2]` |
| NEST | Nest flat structure | key | `[NEST:@csv|key=category]` |
| λ | Map / Apply function | func | `[λ:@array|func=upper]` |
| REDU | Reduce array | accumulator | `[REDU:@array|func=sum]` |
| PIVT | Pivot table | index, cols | `[PIVT:@data|col=month]` |
| TRNS | Transpose matrix | none | `[TRNS:@matrix]` |
| ENCD | Encode data | format | `[ENCD:@text|enc=base64]` |
| DECD | Decode data | format | `[DECD:@b64|enc=utf8]` |
| ξ | Hash / Encrypt | algo | `[ξ:@pwd|algo=sha256]` |
| ζ | Compress payload | algo | `[ζ:@data|algo=gzip]` |
| EXPN | Expand / Decompress | algo | `[EXPN:@gz]` |
| θ | Translate language | target_lang | `[θ:@text|lng=zh]` |
| FMT | Format data | type | `[FMT:@raw|fmt=md]` |

### Analysis

| Verb | Meaning | Args | Example |
|------|---------|------|---------|
| ψ | Analyze sentiment | context | `[ψ:@tweet]` |
| CLST | Cluster data | k, metric | `[CLST:@users|k=5]` |
| SCOR | Score against metric | metric | `[SCOR:@draft|metric=quality]` |
| BNCH | Benchmark | iterations | `[BNCH:@func|n=100]` |
| AUDT | Audit logs | scope | `[AUDT:@GH|scp=global]` |
| VALD | Validate schema | schema | `[VALD:@json|sch=api_v2]` |
| CNT | Count occurrences | target | `[CNT:@list|whr="active=true"]` |
| μ | Measure / Average | field | `[μ:@stats|col=latency]` |
| TRND | Trend analysis | timeframe | `[TRND:@sales|frm=30d]` |
| CORR | Correlate variables | var1, var2 | `[CORR:@data|col=x,y]` |
| FRCS | Forecast series | horizon | `[FRCS:@stock|to=7d]` |
| ANOM | Detect anomalies | threshold | `[ANOM:@logs|thr=3σ]` |

### Generation

| Verb | Meaning | Args | Example |
|------|---------|------|---------|
| CREA | Create entity | type, params | `[CREA:@GH|type=repo]` |
| DRFT | Draft content | topic, len | `[DRFT:marketing|len=med]` |
| PARA | Paraphrase / Rewrite | tone | `[PARA:@text|ton=casual]` |
| EXTD | Extend content | ratio | `[EXTD:@summary|len=long]` |
| SHRT | Shorten content | ratio | `[SHRT:@article|len=short]` |
| STYL | Apply style | style_guide | `[STYL:@draft|sty=ap]` |
| TMPL | Render template | data | `[TMPL:@invoice|data=@SRC]` |
| FILL | Fill missing data | strategy | `[FILL:@form|strategy=infer]` |

### Output

| Verb | Meaning | Args | Example |
|------|---------|------|---------|
| Ω | Standard output | none | `[Ω:@RESULT]` |
| DISP | Display to UI | view | `[DISP:dashboard_1]` |
| EXPT | Export file | type | `[EXPT:@data|fmt=csv]` |
| PRNT | Print to console | level | `[PRNT:"Done"]` |
| LOG | Write to log | level | `[LOG:@error|lvl=warn]` |

### Meta

| Verb | Meaning | Args | Example |
|------|---------|------|---------|
| VERS | Get version | none | `[VERS]` |
| HELP | Request help | cmd | `[HELP:SCRP]` |
| DESC | Describe entity | @target | `[DESC:@GH]` |
| INTR | Introspect state | scope | `[INTR:memory]` |
| SELF | Self-check | target | `[SELF:latency]` |
| ECHO | Echo payload | @target | `[ECHO:@SRC]` |
| NOOP | No operation | none | `[NOOP]` |

---

## Modifiers (28)

| Mod | Meaning | Values |
|-----|---------|--------|
| tgt | Target | entity_id, path |
| src | Source | entity_id, uri |
| dst | Destination | entity_id, uri |
| frm | From (temporal) | timestamp |
| to | To (temporal) | timestamp |
| scp | Scope | global, local, strict |
| dep | Depth | integer |
| rng | Range | start:end |
| whr | Where clause | condition_string |
| mch | Match pattern | regex_string |
| exc | Exclude pattern | regex_string |
| lim | Limit count | integer |
| off | Offset | integer |
| top | Top N | integer |
| bot | Bottom N | integer |
| fmt | Output format | json, md, csv, xml |
| lng | Language | ISO 639-1 |
| sty | Style | pro, casual, code |
| ton | Tone | urgent, neutral |
| len | Length | short, med, long |
| col | Columns | comma_separated |
| row | Rows | index_array |
| srt | Sort field | field_name |
| grp | Group by | field_name |
| typ | Data type | str, int, bool |
| enc | Encoding | utf8, base64, hex |
| chr | Character set | utf-8, ascii |
| cap | Capacity limit | bytes, tokens |

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

## Syntax

### Single operation
```
[VERB:@ENTITY|mod1=val1,mod2=val2]
```

### Pipe chain
```
[VERB1:@SRC]=>[VERB2]=>[VERB3:@DST]
```

Output of each step feeds into the next as @PREV.

### Urgency prefix
```
!!  = urgent / high priority
```

---

## Quick Reference

| Natural Language | I-Lang | Saved |
|------------------|--------|-------|
| Read config from GitHub, parse JSON | `[READ:@GH|path=config.json]=>[FMT|fmt=json]` | 55% |
| Summarize previous in 3 bullets | `[Σ:@PREV|sty=bullets,len=3]` | 52% |
| Extract URL text as Markdown | `[SCRP:@ISEE|url=tgt]=>[FMT|fmt=md]=>[Ω]` | 58% |
| Translate doc to Chinese, save to R2 | `[θ:@SRC|lng=zh]=>[WRIT:@R2]` | 60% |
| Read all .md files, merge, output | `[LIST:@LOCAL|mch="*.md"]=>[Π:READ]=>[Σ]=>[Ω]` | 65% |
| Filter logs for fatal errors only | `[φ:@LOG|whr="lvl=fatal"]` | 55% |
| Draft professional email from context | `[DRFT:@SRC|ton=pro,fmt=email]` | 48% |

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

*I-Lang v2.0 PUBLIC — [ilang.ai](https://ilang.ai) — Palm Media Technology © 2026*
