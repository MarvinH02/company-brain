# Company Brain

Multi-tenant knowledge base: companies upload documents, employees ask questions
and get streamed answers with citations. Includes an evaluation harness that
measures retrieval and answer quality on ~100 test questions.

> This is a **starter skeleton**. Every function has a signature and a TODO
> docstring, but no body. Follow the build roadmap doc milestone by milestone.

## Layout

```
apps/api/        FastAPI app + ingestion worker (same Python package)
  app/routers/     HTTP endpoints
  app/ingestion/   parse -> clean -> chunk -> embed -> store   (M2)
  app/retrieval/   vector, keyword, RRF fusion, rerank          (M3)
  app/generation/  prompt, SSE streaming, citations, history    (M4)
  app/providers/   LLM / embedder / reranker interfaces         (M2-M4)
apps/web/        Next.js frontend                              (M1, M4, M6)
eval/            test set, metrics, LLM judge, reports         (M3, M5)
infra/           Terraform                                      (M6)
```

## Order of work

Grep for the milestone tag to see what belongs to each step:

```bash
grep -rn "TODO(M1)" apps eval    # then M2, M3 ...
```

| Milestone | Outcome |
|-----------|---------|
| M1 | `docker compose up`, auth, orgs, cross-tenant test passes |
| M2 | PDF upload -> chunks with page numbers |
| M3 | `/search` with vector / keyword / hybrid / rerank + 20-question eval |
| M4 | Streaming chat, clickable citations, history |
| M5 | 100-question eval, full metrics, judge agreement, report |
| M6 | Admin dashboard, hardening, deployed demo |

## Run locally

```bash
cp .env.example .env        # fill in provider keys
docker compose up --build
# api:  http://localhost:8000/docs
# web:  http://localhost:3000
# minio console: http://localhost:9001
```

Stub functions raise `NotImplementedError`, so things will fail loudly until you
implement them. That's intended.

## Tests

`apps/api/tests/` contains **spec tests** for the pure functions (chunking,
RRF, citation parsing, metrics). They describe expected behaviour; make them
pass. Add your own as you go.
