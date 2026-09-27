"""Is a retrieved chunk relevant? Ground truth is a quote, so labels survive re-chunking."""
from app.retrieval.types import ScoredChunk


def normalize(s: str) -> str:
    """TODO(M3): lowercase, collapse whitespace, strip punctuation that PDFs mangle
    (smart quotes, hyphenation)."""
    raise NotImplementedError


def chunk_contains_evidence(chunk: ScoredChunk, evidence: dict, threshold: int = 90) -> bool:
    """TODO(M3): True if the chunk's document matches evidence['doc'] (by title/filename)
    AND the normalized quote appears in the normalized chunk content.

    Use rapidfuzz.fuzz.partial_ratio(quote, content) >= threshold to tolerate
    parsing noise. A quote split across two chunks: count it if >= ~60% of it is in
    the chunk (think about what's fair and document your choice in EVALUATION.md).
    """
    raise NotImplementedError


def relevance_vector(chunks: list[ScoredChunk], evidence: list[dict]) -> list[list[bool]]:
    """TODO(M3): matrix [rank][evidence_idx] -> matched? Feeds all retrieval metrics."""
    raise NotImplementedError
