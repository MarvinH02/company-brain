"""Spec for chunk_pages (M2). Add cases for sentence splitting and section changes."""
from app.ingestion.chunking import chunk_pages, count_tokens
from app.ingestion.parsers import ParsedPage


def _pages(n: int, words_per_page: int = 400) -> list[ParsedPage]:
    return [ParsedPage(page_number=i + 1,
                       text="\n\n".join(" ".join(f"w{i}x{j}x{k}" for k in range(40))
                                        for j in range(words_per_page // 40)))
            for i in range(n)]


def test_no_chunk_exceeds_budget():
    chunks = chunk_pages(_pages(5), max_tokens=200, overlap_tokens=30)
    assert chunks
    assert all(c.token_count <= 200 for c in chunks)
    assert all(count_tokens(c.content) == c.token_count for c in chunks)


def test_ordinals_and_pages():
    chunks = chunk_pages(_pages(5), max_tokens=200, overlap_tokens=0)
    assert [c.ordinal for c in chunks] == list(range(len(chunks)))
    assert all(1 <= c.page_start <= c.page_end <= 5 for c in chunks)
    assert chunks[0].page_start == 1 and chunks[-1].page_end == 5


def test_no_empty_chunks_and_empty_input():
    assert chunk_pages([ParsedPage(1, "   ")]) == []
    assert all(c.content.strip() for c in chunk_pages(_pages(2)))


def test_overlap_repeats_text():
    chunks = chunk_pages(_pages(3), max_tokens=200, overlap_tokens=40)
    tail = chunks[0].content.split()[-5:]
    assert " ".join(tail) in chunks[1].content


def test_sections_are_tracked():
    pages = [ParsedPage(1, "Leave policy\n\nYou get 25 days.", headings=["Leave policy"]),
             ParsedPage(2, "Travel\n\nBook economy.", headings=["Travel"])]
    chunks = chunk_pages(pages, max_tokens=500, overlap_tokens=0)
    assert {c.section_title for c in chunks} == {"Leave policy", "Travel"}
