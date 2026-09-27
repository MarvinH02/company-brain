from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.retrieval.types import RetrievalFilters, ScoredChunk


async def vector_search(session: AsyncSession, org_id: UUID, query_vec: list[float], k: int,
                        filters: RetrievalFilters | None = None) -> list[ScoredChunk]:
    """TODO(M3): ORDER BY embedding <=> :qvec (cosine distance), WHERE org_id = :org_id.

    * score = 1 - distance; ranks["vector"] = 1-based position
    * `SET LOCAL hnsw.ef_search = 100` in the same transaction so filtered
      queries still return k rows
    * join documents for the title; only documents with status='ready'
    """
    raise NotImplementedError
