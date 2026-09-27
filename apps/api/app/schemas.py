"""Pydantic request/response models. The frontend's TypeScript types are
generated from the OpenAPI schema these produce, so name them carefully."""
from pydantic import BaseModel

# TODO(M1): SignupIn, LoginIn, TokenOut, UserOut, OrgIn, OrgOut, MembershipOut, InviteIn
# TODO(M2): DocumentOut (id, title, status, page_count, chunk_count, error, created_at)
# TODO(M3): SearchIn (query, mode: 'vector'|'keyword'|'hybrid'|'hybrid_rerank', k,
#           document_ids filter), SearchHit (chunk_id, document_id, title, page_start,
#           page_end, snippet, scores: dict[str, float])
# TODO(M4): ConversationOut, MessageIn, MessageOut, CitationOut
# TODO(M6): UsageStats, FeedbackIn


class Health(BaseModel):
    db: bool
    redis: bool
