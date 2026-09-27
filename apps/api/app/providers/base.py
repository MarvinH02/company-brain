"""Provider interfaces. Everything else in the app depends on these, never on an SDK.

That lets you swap OpenAI / Anthropic / Voyage / Cohere / local models with an env
var, and lets the eval compare them.
"""
from collections.abc import AsyncIterator
from dataclasses import dataclass
from typing import Literal, Protocol


@dataclass
class ChatMessage:
    role: Literal["system", "user", "assistant"]
    content: str


@dataclass
class Usage:
    prompt_tokens: int
    completion_tokens: int


class LLMProvider(Protocol):
    model: str

    async def complete(self, messages: list[ChatMessage], *, temperature: float = 0.0,
                       max_tokens: int = 1024, json_mode: bool = False) -> tuple[str, Usage]:
        """Non-streaming call. Used for query rewriting, titles, the eval judge."""
        ...

    def stream(self, messages: list[ChatMessage], *, temperature: float = 0.0,
               max_tokens: int = 1024) -> AsyncIterator[str]:
        """Yield text deltas. Usage for streams: record it after the stream ends
        (most SDKs expose it on the final event)."""
        ...


class Embedder(Protocol):
    model: str
    dim: int

    async def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Some providers distinguish document vs query embeddings (input_type). Respect it."""
        ...

    async def embed_query(self, text: str) -> list[float]:
        ...


class Reranker(Protocol):
    model: str

    async def rerank(self, query: str, texts: list[str], top_n: int) -> list[tuple[int, float]]:
        """Return (index_into_texts, score) sorted by score desc, length <= top_n."""
        ...
