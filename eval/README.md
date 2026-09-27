# Evaluation

```bash
make eval c=hybrid_rerank          # one config
make eval c=vector && make eval c=hybrid && make eval c=hybrid_rerank   # compare
```

* `datasets/*.jsonl` — test cases (schema below)
* `configs/*.yaml` — one experiment each
* `reports/` — generated Markdown + charts (git-ignored; commit the ones you cite)

## Case schema

| field | type | notes |
|-------|------|-------|
| id | str | stable, e.g. `q017` |
| question | str | |
| reference_answer | str \| null | null for unanswerable |
| evidence | list[{doc, page, quote}] | quote = verbatim span from the source; empty for unanswerable |
| category | str | single_fact, exact_term, paraphrase, multi_doc, unanswerable, injection |
| answerable | bool | |
| source | str | `hand` or `generated_reviewed` |

Target mix for 100: 40 single_fact / 15 exact_term / 15 paraphrase / 15 multi_doc / 15 unanswerable
(+ a few injection cases).
