"""Shared fixtures.

TODO(M1): add fixtures for an async test client (httpx.AsyncClient + ASGITransport),
a test database (separate DB or transaction-per-test rollback), and helpers
`make_user()`, `make_org(owner)`, `auth_headers(user)`.
"""
from uuid import uuid4

import pytest

from app.retrieval.types import ScoredChunk


@pytest.fixture
def make_chunk():
    def _make(content: str = "text", page: int = 1, chunk_id=None) -> ScoredChunk:
        return ScoredChunk(chunk_id=chunk_id or uuid4(), document_id=uuid4(),
                           document_title="Doc", content=content, section_title=None,
                           page_start=page, page_end=page, score=0.0)
    return _make
