"""Structure-aware, token-budgeted chunking. The most important function you'll write.

The eval (M5) sweeps `max_tokens` and `overlap_tokens`, so keep them parameters.
"""
from dataclasses import dataclass

from app.ingestion.parsers import ParsedPage


@dataclass
class ChunkDraft:
    ordinal: int
    content: str
    section_title: str | None
    page_start: int
    page_end: int
    token_count: int


def count_tokens(text: str) -> int:
    """TODO(M2): tiktoken 'cl100k_base' is a fine approximation for any provider."""
    raise NotImplementedError


def split_into_blocks(pages: list[ParsedPage]) -> list[tuple[str, int, str | None]]:
    """TODO(M2): flatten pages into (block_text, page_number, current_section_title).

    Blocks = paragraphs (split on blank lines). Track the latest heading seen so
    each block knows its section. A heading itself starts a new section.
    """
    raise NotImplementedError


def chunk_pages(pages: list[ParsedPage], max_tokens: int = 500,
                overlap_tokens: int = 75) -> list[ChunkDraft]:
    """TODO(M2): pack blocks greedily into chunks <= max_tokens.

    * start a new chunk when the next block would overflow, OR when the section changes
      (prefer not to mix sections; a tiny trailing section may merge)
    * a single block bigger than max_tokens: split it by sentences, then by tokens
    * overlap: start each new chunk with the last ~overlap_tokens of the previous one
      (only within the same section)
    * page_start/page_end = min/max page of the blocks included
    * never emit empty chunks; ordinals are 0..n-1

    See tests/test_chunking.py for the contract.
    """
    raise NotImplementedError


def contextual_header(doc_title: str, section_title: str | None, content: str) -> str:
    """TODO(M2): the text that gets EMBEDDED (store plain `content` for display):
    "{doc_title} > {section_title}\\n\\n{content}" (omit the "> section" part if None).
    Toggle it via config so the eval can A/B it."""
    raise NotImplementedError
