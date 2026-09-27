"""Reciprocal Rank Fusion. Pure function: see tests/test_fusion.py."""
from app.retrieval.types import ScoredChunk


def reciprocal_rank_fusion(result_lists: dict[str, list[ScoredChunk]], k: int = 60,
                           weights: dict[str, float] | None = None,
                           limit: int | None = None) -> list[ScoredChunk]:
    """TODO(M3): fuse ranked lists by rank, not raw score.

    rrf(d) = sum over lists L containing d of  weight_L / (k + rank_L(d))   (rank is 1-based)

    * result_lists: {"vector": [...], "keyword": [...]} each already sorted best-first
    * weights default to 1.0 per list
    * dedupe by chunk_id; merge `ranks` and `scores` dicts from every list
    * output .score = rrf value and .scores["rrf"] = rrf value
    * sort desc by rrf; ties broken by best (lowest) individual rank, then chunk_id
    * truncate to `limit` if given
    """
    raise NotImplementedError
