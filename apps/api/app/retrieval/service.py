"""The single retrieval entrypoint used by /search, chat, and the eval."""
from dataclasses import dataclass
from typing import Literal
from uuid import UUID

from app.retrieval.types import RetrievalFilters, ScoredChunk

Mode = Literal["vector", "keyword", "hybrid", "hybrid_rerank"]


@dataclass
class RetrievalResult:
    chunks: list[ScoredChunk]
    candidates: list[ScoredChunk]   # everything considered before the final cut (for the trace)
    timings_ms: dict[str, float]    # {"embed": .., "vector": .., "keyword": .., "rerank": ..}


async def retrieve(org_id: UUID, query: str, mode: Mode = "hybrid_rerank", k: int = 6,
                   filters: RetrievalFilters | None = None) -> RetrievalResult:
    """TODO(M3):
    * vector:        embed query -> vector_search(k)
    * keyword:       keyword_search(k)
    * hybrid:        both with settings.retrieve_k (run concurrently with asyncio.gather,
                     each with its own session), RRF, take k
    * hybrid_rerank: hybrid with limit ~40 -> rerank(top_n=k)
    * time every stage with time.perf_counter()
    Stretch: cache the full result in Redis keyed by (org_id, mode, k, sha256(query), index_version).
    """
    raise NotImplementedError
