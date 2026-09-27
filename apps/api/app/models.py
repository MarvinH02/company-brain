"""SQLAlchemy ORM models. Columns are described in TODOs; you declare them.

Rules that apply to every tenant-owned table:
  * has `org_id` (FK organizations.id, indexed)
  * UUID primary keys, `created_at` timestamptz default now()

After writing the models: `make revision m="initial"` then edit the migration to
  * `CREATE EXTENSION IF NOT EXISTS vector` first
  * HNSW index on chunks.embedding using vector_cosine_ops
  * GIN index on chunks.tsv
  * tsv as a GENERATED column: to_tsvector('english', coalesce(section_title,'') || ' ' || content)
"""
from app.db import Base


class User(Base):
    """TODO(M1): id, email (unique, lowercase), password_hash, created_at."""
    __tablename__ = "users"


class Organization(Base):
    """TODO(M1): id, name, slug (unique), plan, created_at."""
    __tablename__ = "organizations"


class Membership(Base):
    """TODO(M1): user_id, org_id, role ('owner'|'admin'|'member'); unique (user_id, org_id)."""
    __tablename__ = "memberships"


class Invite(Base):
    """TODO(M1): id, org_id, email, role, token_hash, expires_at, accepted_at."""
    __tablename__ = "invites"


class Document(Base):
    """TODO(M2): id, org_id, title, mime_type, storage_key, checksum (unique per org),
    status ('pending'|'processing'|'ready'|'failed'), error, page_count, uploaded_by,
    created_at. Relationship to chunks with cascade delete."""
    __tablename__ = "documents"


class Chunk(Base):
    """TODO(M2): id, org_id, document_id, ordinal, content, section_title,
    page_start, page_end, token_count, embedding Vector(settings.embedding_dim),
    embedding_model, tsv (TSVECTOR, generated in the migration)."""
    __tablename__ = "chunks"


class Conversation(Base):
    """TODO(M4): id, org_id, user_id, title, created_at, updated_at."""
    __tablename__ = "conversations"


class Message(Base):
    """TODO(M4): id, conversation_id, role ('user'|'assistant'), content,
    rewritten_query, model, prompt_version, latency_ms, prompt_tokens,
    completion_tokens, created_at."""
    __tablename__ = "messages"


class Citation(Base):
    """TODO(M4): id, message_id, chunk_id, marker (int, the n in [n]), score."""
    __tablename__ = "citations"


class RetrievalTrace(Base):
    """TODO(M3): message_id (nullable for /search calls), org_id, query,
    candidates JSONB [{chunk_id, vector_rank, keyword_rank, rrf, rerank}], timings JSONB."""
    __tablename__ = "retrieval_traces"


class Feedback(Base):
    """TODO(M6): id, message_id, user_id, rating (+1/-1), comment, created_at."""
    __tablename__ = "feedback"


class EvalRun(Base):
    """TODO(M5): id, created_at, git_sha, dataset, config JSONB, summary JSONB."""
    __tablename__ = "eval_runs"


class EvalResult(Base):
    """TODO(M5): id, run_id, case_id, answer, retrieved JSONB, metrics JSONB, judge JSONB."""
    __tablename__ = "eval_results"
