"""Markdown report + charts for one run, compared with previous runs."""


def write_report(run_id: str, summary: dict, results: list[dict], previous: list[dict]) -> str:
    """TODO(M5): write eval/reports/{date}_{config_name}.md containing:
    * config + git SHA + dataset size
    * headline table: hit@1/5/10, recall@5, MRR, nDCG@10, correctness, faithfulness,
      abstention accuracy, p50/p95 latency, cost/question — with deltas vs the previous run
    * per-category table
    * the 10 worst cases: question, expected evidence, what was retrieved, answer, judge reason
    * charts (matplotlib PNGs): metric by config (grouped bars), hit@k curve
    Return the path.
    """
    raise NotImplementedError
