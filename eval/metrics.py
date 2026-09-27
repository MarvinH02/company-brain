"""Retrieval + aggregate metrics. Pure functions: see apps/api/tests/test_metrics.py.

`rel` everywhere = relevance_vector(...) output: rel[rank_idx][evidence_idx] -> bool
"""


def hit_at_k(rel: list[list[bool]], k: int) -> float:
    """TODO(M3): 1.0 if ANY evidence item is matched within the first k results, else 0.0."""
    raise NotImplementedError


def recall_at_k(rel: list[list[bool]], n_evidence: int, k: int) -> float:
    """TODO(M3): share of evidence items matched by at least one of the first k results."""
    raise NotImplementedError


def reciprocal_rank(rel: list[list[bool]]) -> float:
    """TODO(M3): 1 / (1-based rank of the first result matching any evidence); 0 if none."""
    raise NotImplementedError


def ndcg_at_k(rel: list[list[bool]], k: int) -> float:
    """TODO(M5): binary gains (a result is relevant if it matches any evidence).
    DCG = sum rel_i / log2(i + 1) for i = 1..k; divide by the ideal DCG. 0 if no relevant items exist."""
    raise NotImplementedError


def percentile(values: list[float], p: float) -> float:
    """TODO(M5): linear-interpolated percentile (p in 0..100). For latency p50/p95."""
    raise NotImplementedError


def summarize(results: list[dict]) -> dict:
    """TODO(M5): aggregate per-case metric dicts into
    {"overall": {...means...}, "by_category": {cat: {...}}, "n": len(results)}.
    Retrieval metrics only over answerable cases; abstention only over unanswerable ones."""
    raise NotImplementedError


def cohen_kappa(a: list[int], b: list[int]) -> float:
    """TODO(M5): agreement between your hand scores and the judge's (bucket 1-5 into
    fail 1-2 / partial 3 / pass 4-5 first). Report it in EVALUATION.md."""
    raise NotImplementedError
