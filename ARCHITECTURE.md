# Architecture

TODO: fill in as you build. Interviewers read this. Suggested sections:

1. Overview diagram (export from the roadmap doc or draw your own)
2. Request lifecycle of a question (retrieve -> rerank -> generate -> cite)
3. Ingestion pipeline and why it runs in a worker
4. Multi-tenancy: how org isolation is enforced (and tested)
5. Key trade-offs: RRF vs score normalization; cross-encoder reranking; quotes as ground truth;
   Postgres for both vectors and keywords instead of a separate vector DB
6. What I'd do next
