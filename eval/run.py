"""CLI: python -m eval.run --config eval/configs/hybrid_rerank.yaml [--limit N] [--no-generate]"""
import argparse


def load_config(path: str) -> dict:
    """TODO(M3): yaml.safe_load; validate required keys."""
    raise NotImplementedError


def load_dataset(path: str, limit: int | None = None) -> list[dict]:
    """TODO(M3): read JSONL; validate each case against the schema in eval/README.md."""
    raise NotImplementedError


async def run_case(case: dict, config: dict) -> dict:
    """TODO(M3 retrieval part, M5 generation part):
    1. result = retrieve(org_id, case["question"], mode=..., k=max(metrics_k))
    2. rel = relevance_vector(result.chunks, case["evidence"]) -> hit@k, recall@k, rr
    3. if generation enabled: run the SAME answer pipeline as chat (build_answer_messages
       + llm.complete), time it, count tokens, extract citations
    4. judge_answer(...) with the judge provider
    return a flat dict of metrics + raw outputs for the report
    """
    raise NotImplementedError


async def run(config: dict, limit: int | None) -> str:
    """TODO(M5): run cases with bounded concurrency (asyncio.Semaphore(4)), save EvalRun +
    EvalResults (with git SHA from `git rev-parse HEAD`), write a report, return its path."""
    raise NotImplementedError


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--fail-under", type=float,
                        help="CI: exit 1 if hit@5 is below this value")
    args = parser.parse_args()
    # TODO(M3): asyncio.run(run(load_config(args.config), args.limit)); handle --fail-under
    raise NotImplementedError


if __name__ == "__main__":
    main()
