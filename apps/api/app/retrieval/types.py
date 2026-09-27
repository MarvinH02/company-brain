from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class ScoredChunk:
    chunk_id: UUID
    document_id: UUID
    document_title: str
    content: str
    section_title: str | None
    page_start: int
    page_end: int
    score: float                                   # the score of the stage that produced it
    scores: dict[str, float] = field(default_factory=dict)  # every stage's score, for the trace
    ranks: dict[str, int] = field(default_factory=dict)     # e.g. {"vector": 3, "keyword": 12}


@dataclass
class RetrievalFilters:
    document_ids: list[UUID] | None = None
