"""Spec for reciprocal_rank_fusion. Make these pass (M3)."""
import pytest

from app.retrieval.fusion import reciprocal_rank_fusion


def test_item_in_both_lists_beats_items_in_one(make_chunk):
    a, b, c = make_chunk(), make_chunk(), make_chunk()
    fused = reciprocal_rank_fusion({"vector": [a, b], "keyword": [c, b]}, k=60)
    assert fused[0].chunk_id == b.chunk_id


def test_score_formula(make_chunk):
    a = make_chunk()
    fused = reciprocal_rank_fusion({"vector": [a], "keyword": [a]}, k=60)
    assert fused[0].score == pytest.approx(2 / 61)
    assert fused[0].scores["rrf"] == pytest.approx(2 / 61)


def test_dedupes_and_merges_ranks(make_chunk):
    a, b = make_chunk(), make_chunk()
    fused = reciprocal_rank_fusion({"vector": [a, b], "keyword": [b]})
    assert len(fused) == 2
    merged_b = next(x for x in fused if x.chunk_id == b.chunk_id)
    assert merged_b.ranks == {"vector": 2, "keyword": 1}


def test_weights(make_chunk):
    a, b = make_chunk(), make_chunk()
    fused = reciprocal_rank_fusion({"vector": [a], "keyword": [b]},
                                   weights={"vector": 0.3, "keyword": 0.7})
    assert fused[0].chunk_id == b.chunk_id


def test_limit_and_empty(make_chunk):
    chunks = [make_chunk() for _ in range(10)]
    assert len(reciprocal_rank_fusion({"vector": chunks}, limit=3)) == 3
    assert reciprocal_rank_fusion({"vector": [], "keyword": []}) == []
