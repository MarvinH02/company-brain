from app.providers.base import Reranker
from app.retrieval.types import ScoredChunk


async def rerank(reranker: Reranker, query: str, candidates: list[ScoredChunk],
                 top_n: int) -> list[ScoredChunk]:
    """TODO(M3): send (query, section_title + content) pairs to the reranker, map the
    returned indices back to candidates, set .score and .scores["rerank"], keep top_n.
    Record ranks["rerank"] too. If candidates is empty return [] without calling the API."""
    raise NotImplementedError
