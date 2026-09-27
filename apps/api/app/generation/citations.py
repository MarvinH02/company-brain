"""Turn [n] markers in the answer into citation records. Pure: see tests/test_citations.py."""
from dataclasses import dataclass

from app.retrieval.types import ScoredChunk


@dataclass
class ParsedCitation:
    marker: int          # the n in [n]
    chunk: ScoredChunk
    sentence: str        # the sentence the marker was attached to (for citation checking)


def extract_citations(answer: str, sources: list[ScoredChunk]) -> list[ParsedCitation]:
    """TODO(M4):
    * find markers like [1], [2][3], and [1, 2]
    * n is 1-based into `sources`; ignore n < 1 or n > len(sources) (hallucinated markers)
    * one ParsedCitation per (marker, sentence); keep order of first appearance
    * the sentence = text from the previous sentence end up to the marker
    """
    raise NotImplementedError


def strip_invalid_markers(answer: str, n_sources: int) -> str:
    """TODO(M4): remove markers pointing at non-existent sources from the saved answer."""
    raise NotImplementedError
