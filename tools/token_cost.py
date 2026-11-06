#!/usr/bin/env python3
"""Machine cost of every dictionary symbol: how many tokens the bare name costs in four public tokenizers.

    python tools/token_cost.py --check          # recompute and compare with the tok_* columns of train.csv (exit 1 on drift)
    python tools/token_cost.py --write          # recompute and write the tok_* columns
    python tools/token_cost.py --symbols "::" "=>" "⇒" "[Ω]"   # count arbitrary strings

Tokenizers: OpenAI cl100k_base and o200k_base (tiktoken), DeepSeek-V3 and Qwen3-8B (their tokenizer.json from
Hugging Face, fetched once into --cache, huggingface.co first, hf-mirror.com second). Requirements: tiktoken, tokenizers.
Counts are for the symbol alone, with no leading space and no surrounding syntax; a symbol inside `[V:` or `|m=` costs
the brackets on top. Anthropic's tokenizer is not public, so Claude models are not measured.
"""
import argparse, csv, io, os, sys, urllib.request

COLUMNS = ("tok_cl100k", "tok_o200k", "tok_deepseek_v3", "tok_qwen3")
HF = {"tok_deepseek_v3": "deepseek-ai/DeepSeek-V3", "tok_qwen3": "Qwen/Qwen3-8B"}
HOSTS = ("https://huggingface.co", "https://hf-mirror.com")


def fetch(repo, cache):
    name = repo.replace("/", "__") + ".tokenizer.json"
    path = os.path.join(cache, name)
    if os.path.exists(path):
        return path
    os.makedirs(cache, exist_ok=True)
    last = None
    for host in HOSTS:
        try:
            req = urllib.request.Request(host + "/" + repo + "/resolve/main/tokenizer.json", headers={"User-Agent": "ilang-dict-token-cost"})
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            if not data.lstrip().startswith(b"{"):
                raise ValueError("not a tokenizer.json")
            with open(path, "wb") as f:
                f.write(data)
            return path
        except Exception as e:  # try the mirror
            last = e
    raise SystemExit("could not fetch %s: %s" % (repo, last))


def load(cache):
    import tiktoken
    from tokenizers import Tokenizer
    enc = {
        "tok_cl100k": tiktoken.get_encoding("cl100k_base"),
        "tok_o200k": tiktoken.get_encoding("o200k_base"),
        "tok_deepseek_v3": Tokenizer.from_file(fetch(HF["tok_deepseek_v3"], cache)),
        "tok_qwen3": Tokenizer.from_file(fetch(HF["tok_qwen3"], cache)),
    }
    def count(col, s):
        t = enc[col]
        if t.__class__.__name__ == "Encoding":
            return len(t.encode(s, disallowed_special=()))
        return len(t.encode(s, add_special_tokens=False).ids)
    return count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "train.csv"))
    ap.add_argument("--cache", default=os.path.join(os.path.expanduser("~"), ".cache", "ilang-dict-tokenizers"))
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--symbols", nargs="*")
    a = ap.parse_args()
    count = load(a.cache)
    if a.symbols:
        print("%-20s" % "symbol" + "".join("%-18s" % c for c in COLUMNS))
        for s in a.symbols:
            print("%-20s" % repr(s) + "".join("%-18d" % count(c, s) for c in COLUMNS))
        return 0
    with io.open(a.csv, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys())
    for c in COLUMNS:
        if c not in fields:
            fields.append(c)
    drift = 0
    for r in rows:
        for c in COLUMNS:
            v = str(count(c, r["name"]))
            if a.check and r.get(c, "") != v:
                drift += 1
                print("drift %s %s: csv=%s now=%s" % (r["type"], r["name"], r.get(c, ""), v))
            r[c] = v
    by = {}
    for r in rows:
        by.setdefault(r["type"], []).append(r)
    print("single-token rate by type (symbol alone):")
    for t, rs in by.items():
        print("  %-22s n=%-3d " % (t, len(rs)) + "  ".join("%s %3d%%" % (c.replace("tok_", ""), 100 * sum(1 for r in rs if r[c] == "1") // len(rs)) for c in COLUMNS))
    if a.write:
        with io.open(a.csv, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
        print("wrote", a.csv)
    if a.check:
        print("drift:", drift)
        return 1 if drift else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
