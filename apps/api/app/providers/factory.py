"""Build providers from settings."""
from app.providers.base import Embedder, LLMProvider, Reranker


def get_llm(name: str | None = None, model: str | None = None) -> LLMProvider:
    """TODO(M4): return an implementation chosen by name (default settings.llm_provider).

    Implement ONE first (e.g. providers/openai_llm.py or anthropic_llm.py). Add a
    second later for the model-comparison experiment. The eval judge calls this
    with a different name/model than the answer generator.
    """
    raise NotImplementedError


def get_embedder() -> Embedder:
    """TODO(M2): implementation by settings.embedding_provider. Assert dim == settings.embedding_dim."""
    raise NotImplementedError


def get_reranker() -> Reranker | None:
    """TODO(M3): None when settings.rerank_provider == 'none'.

    Local option: sentence_transformers.CrossEncoder(settings.rerank_model); run
    predict() in a thread (asyncio.to_thread) so it doesn't block the event loop.
    """
    raise NotImplementedError
