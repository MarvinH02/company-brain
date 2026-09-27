"""Spec for eval metrics (M3/M5). Run from repo root with PYTHONPATH=.:apps/api"""
import math

import pytest

metrics = pytest.importorskip("eval.metrics")

# 3 results x 2 evidence items
REL = [[False, False],
       [True, False],
       [False, True]]


def test_hit():
    assert metrics.hit_at_k(REL, 1) == 0.0
    assert metrics.hit_at_k(REL, 2) == 1.0


def test_recall():
    assert metrics.recall_at_k(REL, 2, 2) == 0.5
    assert metrics.recall_at_k(REL, 2, 3) == 1.0


def test_reciprocal_rank():
    assert metrics.reciprocal_rank(REL) == 0.5
    assert metrics.reciprocal_rank([[False], [False]]) == 0.0


def test_ndcg():
    dcg = 1 / math.log2(3) + 1 / math.log2(4)
    idcg = 1 / math.log2(2) + 1 / math.log2(3)
    assert metrics.ndcg_at_k(REL, 3) == pytest.approx(dcg / idcg)


def test_percentile():
    assert metrics.percentile([1, 2, 3, 4, 5], 50) == 3
    assert metrics.percentile([10, 20], 50) == 15
