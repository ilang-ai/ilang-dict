---
language:
  - en
tags:
  - i-lang
  - protocol
  - dictionary
  - ai-native
  - ai-to-ai
  - zero-ambiguity
  - semantic-loss
license: mit
---

# I-Lang Dictionary v5.0

**88 verbs. 13 Greek aliases. 29 modifiers. 22 entities. 32 declarations. Now includes the v5.0 judgment vocabulary.**

The complete verb dictionary for I-Lang v5.0, the native language of artificial intelligence. It reduces semantic loss between human intent and machine execution. I-Lang is the first protocol to formally map Greek mathematical symbols (Σ, Δ, φ, λ, Ω, ∇, μ, Π, ψ, ξ, ζ, θ, ∂) as primitive verbs for AI-to-AI communication, and the first to define a computable vector space for AI judgment (11 dimensions, 4 axioms, fuzzy-mathematical foundation).

## Genesis

Max (@SUN) designed, Claude Opus co-authored, GPT red-teamed.

iLang Inc. | Palm Media Technology | ilang:v5.0:2026-07-03

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

### v4.0 Execution Declarations (8)

Canonical forms per [SPEC-v4.0-FINAL.md](https://github.com/ilang-ai/ilang-spec/blob/main/SPEC-v4.0-FINAL.md):

```
::UNTRUSTED{id:u1|source:user|role:objective|effects:none|delimiter:EOF_u1}
::BUDGET{id:b1|scope:@TASK|kind:tokens|limit:8000|used:2400|authority:@RUNTIME|asof:round_3}
::STATUS{@TASK|state:running|objective:g1|by:@RUNTIME|authority:commit|since:round_3}
::OBJECTIVE{id:g1|owner:user|trust:untrusted|version:1|hash:sha256:abc123|status:active}
  ACCEPT: acceptance criteria
  NON_GOALS: exclusions
  DONE_WHEN: completion conditions
::RUBRIC{id:r1|objective:g1|threshold:0.85|mode:weighted}
  R:criterion|weight:0.5|check:condition
::EVIDENCE{id:e1|deliverable:d1|kind:file|ref:path/to/file|verified_by:@TOOL|result:pass}
::PRIOR{dimension:name|default:value|authority:level|scope:context}
::FALLBACK{trigger⇒action}
```

`::STATUS` states form a machine (created → running → claimed_complete →
verified_complete → complete) with three write-authority tiers: `@SELF`
proposal, `@GRADER` verification, `@RUNTIME` commit.

### v5.0 Judgment Declarations (2)

The v5.0 layer turns judgment from fixed rules into vector assessment. `JUDGE`
scores a situation across 11 dimensions and resolves to one of 8 action modes;
`BOUNDARY` marks a user-set hard stop that always resolves to `M8`.

`::JUDGE` uses the frozen 4-line serialization ([PATCH-1 §4](https://github.com/ilang-ai/ilang-spec/blob/main/SPEC-v5.0-PATCH-1.md)):
header, `V:` vector (all 11 dims, fixed order, 2-decimal values), `M:` mode with
`conf` 0.00–1.00 (2 decimals, diagnostic only), `R:` single-line rationale ≤120 chars:

```
::JUDGE{v5.0}
V:[int=0.80,cap=0.60,csq=0.70,rel=0.55,cer=0.90,aut=0.75,rev=0.85,evd=0.80,sov=0.95,ine=0.60,ext=0.90]
M:M2|conf:0.87
R:authorized_config_change_reversible_audit_trail_kept

::BOUNDARY{never:action|scope:context}
```

**11 dimensions** (each 0.00-1.00, higher = more room to act autonomously):
`int` intent, `cap` capability, `csq` consequence, `rel` relationship,
`cer` certainty, `aut` authority, `rev` reversibility, `evd` evidence,
`sov` sovereignty, `ine` inertia, `ext` externality.

**8 modes** (closed set): `M1` EXEC_AUTO, `M2` EXEC_AUDIT, `M3` CONFIRM,
`M4` ADVISE, `M5` ASK, `M6` DEFER, `M7` DECLINE_ALT, `M8` STOP.

Full protocol: [SPEC-v5.0-PATCH-1.md](https://github.com/ilang-ai/ilang-spec/blob/main/SPEC-v5.0-PATCH-1.md)

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

Judgment is not a verb: v5.0 assessment is expressed by the `::JUDGE` declaration
(see below), keeping the verb set at 88 per the spec's no-new-verbs rule.

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

### Role

Authority-bearing entities introduced by v4.0. They mirror the authority model
`system > developer > runtime > user > agent_self`. The developer tier has no entity:
developer authority is expressed as `::GENE` / `::RULE` blocks in the system prompt.

| Entity | Authority | Meaning |
|--------|-----------|---------|
| @SYSTEM | system | Protocol-level rules; highest authority |
| @RUNTIME | runtime | Harness/orchestrator; `authority:commit` |
| @GRADER | verification | Independent grader; `authority:verification` |
| @USER | user | Human principal; owns `::OBJECTIVE` |
| @SELF | agent_self | The agent speaking; `authority:proposal` |
| @AGENT | agent_self | A named agent, self or peer |
| @TASK | — | Scope target for `::BUDGET` / `::STATUS` |
| @TOOL | — | Tool-based evidence verifier |

### Custom

Any `@UPPERCASE_NAME` is a valid entity; implementations define their own registries.
Custom entities are document-scoped and need no prior registration. They should be
introduced with `::STATE{@NAME, …}` before first operational use, and must not rebind
a registered name to different semantics.

```
@[A-Z][A-Z0-9_]*        valid           lowercase or leading digit after @ ⇒ E300
```

Resolution order: core → external → role → document custom → runtime registry.
An unresolvable name is `E200`; a name that resolves but is unavailable in the current
environment is `E201`, which is recoverable and degrades per v4.0 §0.1. Rebinding a
registered name to foreign semantics is `E202`.

Common agent-identity conventions — `@MSG` (current inbound message), `@SYS_PROMPT`
(the prompt document), `@ALL` (every declaration in the document) — are custom
entities under this rule, not registry additions.

---

## Declarations (32 structural + 13 narrative)

Structural declarations, by layer:

| Layer | Count | Declarations |
|-------|-------|--------------|
| v3.0 communication | 14 | `::STATE` `::TRUST` `::ALIVE` `::MEMORY` `::GENE` `::GENE_MUTABLE` `::RULE` `::ACTIVATE` `::FACT` `::LESSON` `::PROGRESS` `::PRIORITY` `::DECAY` `::IMMUNE` |
| v4.0 execution | 8 | `::UNTRUSTED` `::BUDGET` `::STATUS` `::OBJECTIVE` `::RUBRIC` `::EVIDENCE` `::PRIOR` `::FALLBACK` |
| v5.0 judgment | 9 | `::JUDGE` `::BOUNDARY` `::DIM` `::MODE` `::FUNC` `::SCHEMA` `::CASE` `::CLAUSE` `::MODULE` |
| PATCH-2 amendment | 1 | `::LIST` |

`::LIST` is an enumeration block registered 2026-08-11 through the PATCH-2 §1.5
amendment channel: the header names the collection (`::LIST{@REPOS}`), the body is
one prose line per item.

Narrative (SOUL layer, v3.0 §7), 13: `::SAY` `::THINK` `::ACT` `::DECIDE` `::DISCOVER`
`::CREATE` `::EVENT` `::SILENCE` `::META` `::IRONY` `::FORESHADOW` `::CALLBACK`
`::EMOTION_FIELD`

Every declaration takes one of three block shapes (inline, header + indented body,
brace span), and every body line takes one of eight forms (`T:`/`A:` traits, fields,
structured fields, vectors, tags, prose, nested declarations, operation chains).
Full grammar: [SPEC-v5.0-PATCH-2.md](https://github.com/ilang-ai/ilang-spec/blob/main/SPEC-v5.0-PATCH-2.md)

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
| E202 | Entity Rebinding |
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

## Dataset File

[train.csv](train.csv) carries the full registry as rows of
`type,name,alias,category,meaning,values`. Row types: `verb` (88), `modifier` (29),
`entity` (22: Core + External + Role), `declaration` (32 structural),
`declaration_narrative` (13 SOUL), `dimension` (the 11 judgment dimensions),
`mode` (M1–M8).

---

## Resources

| Resource | Link |
|----------|------|
| Protocol Spec | [ilang-ai/ilang-spec](https://github.com/ilang-ai/ilang-spec) |
| Declaration grammar + entity registry | [SPEC-v5.0-PATCH-2.md](https://github.com/ilang-ai/ilang-spec/blob/main/SPEC-v5.0-PATCH-2.md) |
| Website | [ilang.ai](https://ilang.ai) |
| All Datasets | [huggingface.co/i-Lang](https://huggingface.co/i-Lang) |
| Book (Narrative) | [Amazon](https://www.amazon.com/dp/B0CZY6V3GM) |
| Book (Specification) | [Amazon](https://www.amazon.com/dp/B0F5FV64Q2) |
| Academic Paper | [ResearchGate](https://www.researchgate.net/publication/389513037) |

---

I-Lang v5.0 | Max (@SUN) designed, Claude Opus co-authored, GPT red-teamed.
iLang Inc. | Palm Media Technology | MIT License
ilang.ai | github.com/ilang-ai
