"""Text cleanup applied before chunking. Pure functions: easy to unit test."""
from app.ingestion.parsers import ParsedPage


def strip_repeated_lines(pages: list[ParsedPage], threshold: float = 0.5) -> list[ParsedPage]:
    """TODO(M2): remove headers/footers.

    A line (after stripping digits, so "Page 3 of 40" matches "Page 7 of 40")
    that appears in the first/last 3 lines of more than `threshold` of pages is
    boilerplate: drop it everywhere. Only apply when len(pages) >= 3.
    """
    raise NotImplementedError


def normalize_text(text: str) -> str:
    """TODO(M2):
    * join words hyphenated across line breaks ("infor-\\nmation" -> "information")
    * collapse runs of spaces; keep paragraph breaks (blank lines)
    * normalize unicode (NFKC) and fancy quotes/ligatures
    """
    raise NotImplementedError
