from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.retrieval.types import RetrievalFilters, ScoredChunk


async def keyword_search(session: AsyncSession, org_id: UUID, query: str, k: int,
                         filters: RetrievalFilters | None = None) -> list[ScoredChunk]:
    """TODO(M3): full-text search over chunks.tsv.

    * websearch_to_tsquery('english', :q) handles quotes / OR / -minus safely
    * rank with ts_rank_cd(tsv, q); WHERE tsv @@ q AND org_id = :org_id
    * ranks["keyword"] = 1-based position
    * if the query has no matches (e.g. all stop-words) return []
    """
    raise NotImplementedError
