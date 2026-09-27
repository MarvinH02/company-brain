"""Batched, cached, retrying embedding calls."""
from app.providers.base import Embedder


async def embed_texts(embedder: Embedder, texts: list[str], batch_size: int = 64) -> list[list[float]]:
    """TODO(M2):
    * look up each text in Redis first: key f"emb:{embedder.model}:{sha256(text)}"
    * embed only the misses, in batches of `batch_size`
    * retry on rate limit / 5xx with exponential backoff + jitter (max ~5 tries)
    * write new vectors back to the cache (store as bytes, e.g. numpy float32 .tobytes())
    * return vectors in the SAME order as `texts`
    """
    raise NotImplementedError
