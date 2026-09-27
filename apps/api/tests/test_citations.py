"""Spec for citation parsing (M4)."""
from app.generation.citations import extract_citations, strip_invalid_markers


def test_basic_and_grouped_markers(make_chunk):
    s = [make_chunk("a"), make_chunk("b"), make_chunk("c")]
    cits = extract_citations("Leave is 25 days [1]. Travel is economy [2][3].", s)
    assert [c.marker for c in cits] == [1, 2, 3]
    assert cits[0].chunk is s[0]
    assert "Travel is economy" in cits[1].sentence


def test_comma_markers(make_chunk):
    s = [make_chunk(), make_chunk()]
    assert [c.marker for c in extract_citations("Both apply [1, 2].", s)] == [1, 2]


def test_ignores_out_of_range(make_chunk):
    s = [make_chunk()]
    assert [c.marker for c in extract_citations("X [1]. Y [4]. Z [0].", s)] == [1]
    assert strip_invalid_markers("X [1]. Y [4].", 1) == "X [1]. Y."
